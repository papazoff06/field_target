pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.10"
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                powershell """
                python -m venv ${VENV_DIR}
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                powershell """
                ${VENV_DIR}\\Scripts\\Activate.ps1
                pip install --upgrade pip
                pip install flake8 pytest
                if (Test-Path requirements.txt) { pip install -r requirements.txt }
                """
            }
        }

        stage('Lint') {
            steps {
                powershell """
                ${VENV_DIR}\\Scripts\\Activate.ps1
                flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
                """
            }
        }

        stage('Test') {
            steps {
                powershell """
                ${VENV_DIR}\\Scripts\\Activate.ps1
                pytest
                """
            }
        }
    }
}
