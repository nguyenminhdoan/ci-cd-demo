# Jenkins CI/CD Setup with Docker Compose

This directory contains a complete Jenkins CI/CD setup with Python support using Docker Compose.

## Quick Start

### 1. Start Jenkins
```bash
docker-compose up -d
```

### 2. Access Jenkins
- Open your browser and go to: http://localhost:8080
- Get the initial admin password:
```bash
docker-compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### 3. Stop Jenkins
```bash
docker-compose down
```

## Files Overview

- **`Dockerfile.jenkins`** - Custom Jenkins image with Python 3.11 pre-installed
- **`docker-compose.yml`** - Docker Compose configuration for easy deployment
- **`Jenkinsfile`** - CI/CD pipeline definition
- **`requirements.txt`** - Python dependencies for the project

## Features

✅ **Jenkins LTS** with Python 3.11 support  
✅ **Pre-installed Python tools**: pytest, flake8, pylint, coverage  
✅ **Persistent data** using Docker volumes  
✅ **Easy deployment** with single command  
✅ **Network isolation** with custom Docker network  

## Pipeline Stages

1. **Checkout** - Get source code from Git
2. **Setup Python Environment** - Verify Python installation
3. **Install Dependencies** - Create virtual environment and install packages
4. **Static Code Analysis** - Run flake8 and pylint
5. **Unit Tests** - Execute test suite
6. **Test Coverage** - Generate coverage reports

## Usage Commands

```bash
# Start Jenkins in background
docker-compose up -d

# View logs
docker-compose logs -f jenkins

# Stop Jenkins
docker-compose down

# Stop and remove all data
docker-compose down -v

# Rebuild Jenkins image
docker-compose build --no-cache

# Access Jenkins container shell
docker-compose exec jenkins bash
```

## Troubleshooting

### Get Jenkins Admin Password
```bash
docker-compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### Check Jenkins Status
```bash
docker-compose ps
```

### View Jenkins Logs
```bash
docker-compose logs jenkins
```

### Reset Jenkins (⚠️ This will delete all data)
```bash
docker-compose down -v
docker-compose up -d
```

## Jenkins Job Configuration

1. **Create New Pipeline Job**
   - Name: `ci-cd-demo`
   - Type: Pipeline

2. **Configure Pipeline**
   - Definition: Pipeline script from SCM
   - SCM: Git
   - Repository URL: `https://github.com/nguyenminhdoan/ci-cd-demo.git`
   - Branch: `main`
   - Script Path: `Jenkinsfile`

3. **Save and Build**
   - Click "Save"
   - Click "Build Now"

## Notes

- Jenkins data is persisted in Docker volume `jenkins_data`
- Python virtual environment is created automatically during pipeline execution
- All Python dependencies are installed in the virtual environment to avoid conflicts
- The pipeline runs static analysis, unit tests, and generates coverage reports