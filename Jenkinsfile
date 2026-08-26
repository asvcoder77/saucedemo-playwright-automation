pipeline {
    agent { label 'linux' }

    options {
        timestamps()
        skipDefaultCheckout()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up test environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                    .venv/bin/python -m playwright install --with-deps chromium
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    mkdir -p reports test-results
                    .venv/bin/python -m pytest \
                      --junitxml=reports/junit.xml \
                      --output=test-results
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
            archiveArtifacts allowEmptyArchive: true, artifacts: 'test-results/**/*'
        }
    }
}
