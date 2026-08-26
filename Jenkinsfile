pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Set up test environment') {
            steps {
                bat '''
                    py -m venv .venv
                    .venv\Scripts\python.exe -m pip install --upgrade pip
                    .venv\Scripts\python.exe -m pip install -r requirements.txt
                    .venv\Scripts\python.exe -m playwright install chromium
                '''
            }
        }

        stage('Run tests') {
            steps {
                bat '''
                    if not exist reports mkdir reports
                    if not exist test-results mkdir test-results
                    .venv\Scripts\python.exe -m pytest --junitxml=reports\junit.xml --output=test-results
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
        }
    }
}
