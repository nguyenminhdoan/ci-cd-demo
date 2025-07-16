pipeline {
    agent any
    
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
                    pip3 install -r requirements.txt
                '''
            }
        }
        
        stage('Static Code Analysis') {
            steps {
                echo 'Running static code analysis...'
                sh '''
                    flake8 . --max-line-length=120 --exclude=venv,__pycache__
                    pylint calc.py || true
                '''
            }
        }
        
        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    python3 -m unittest test_calc.py
                    python3 -m unittest tests/github/test_calc_validation.py
                    python3 -m unittest tests/github/test_calc_performance.py
                '''
            }
        }
        
        stage('Test Coverage') {
            steps {
                echo 'Running test coverage...'
                sh '''
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
            // Archive test results if needed
            archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}