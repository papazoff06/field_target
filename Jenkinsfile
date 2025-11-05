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
                    . ${VENV_DIR}\\Scripts\\Activate.ps1

                    flake8 . --exclude=${VENV_DIR},.git,__pycache__ --count --select=E9,F63,F7,F82 --show-source --statistics
                    if (\$LASTEXITCODE -ne 0) { Write-Host "flake8 strict errors detected (this will not stop build)" }

                    flake8 . --exclude=${VENV_DIR},.git,__pycache__ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
                    pytest
"""

            }
        }
    }
}
