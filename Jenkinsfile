pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup, Install & Test') {
            steps {
                powershell """
                # Allow script execution for the venv activation
                Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

                # Create virtual environment
                if (!(Test-Path ${VENV_DIR})) {
                    python -m venv ${VENV_DIR}
                }

                # Activate venv
                & ${VENV_DIR}\\Scripts\\Activate.ps1

                # Upgrade pip and install dependencies
                pip install --upgrade pip
                pip install flake8 pytest
                if (Test-Path requirements.txt) { pip install -r requirements.txt }

                # Run linter
                flake8 . --exclude=${VENV_DIR},.git,__pycache__ --count --select=E9,F63,F7,F82 --show-source --statistics; if ($LASTEXITCODE -ne 0) { Write-Host "flake8 errors detected" }
                flake8 . --exclude=${VENV_DIR},.git,__pycache__ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics


                # Run tests
                pytest
                """
            }
        }
    }
}
