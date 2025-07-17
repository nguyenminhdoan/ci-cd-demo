pipeline {
    agent any
    
    triggers {
        githubPush()
    }
    
    environment {
        PYTHON_VERSION = '3.11'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 --version
                    pip3 --version
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    # Create virtual environment
                    python3 -m venv venv
                    
                    # Activate virtual environment and install dependencies
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Static Code Analysis') {
            steps {
                echo 'Running static code analysis...'
                sh '''
                    . venv/bin/activate
                    flake8 . --max-line-length=120 --exclude=venv,__pycache__
                    pylint calc.py || true
                '''
            }
        }
        
        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    . venv/bin/activate
                    python -m pytest test_calc.py --junitxml=test-results.xml
                    python -m pytest tests/github/test_calc_validation.py --junitxml=test-results-validation.xml
                    python -m pytest tests/github/test_calc_performance.py --junitxml=test-results-performance.xml
                '''
            }
        }
        
        stage('Test Coverage') {
            steps {
                echo 'Running test coverage...'
                sh '''
                    . venv/bin/activate
                    coverage run -m unittest discover -s . -p "test_*.py"
                    coverage report
                    coverage html
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed'
            // Archive test results and coverage reports
            archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
            
            // Publish test results
            junit testResults: 'test-results*.xml'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}