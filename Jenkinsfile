pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        SECRET_KEY = "dummy-secret-for-ci"   // avoid decouple error
        DEBUG = "0"
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
                Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

                # Create virtual environment
                if (!(Test-Path ${env.VENV_DIR})) {
                    python -m venv ${env.VENV_DIR}
                }

                # Activate venv
                & ${env.VENV_DIR}\\Scripts\\Activate.ps1

                python -m pip install --upgrade pip
                pip install -r requirements.txt

                # Run Django tests
                python manage.py test
                """
            }
        }
    }
}
