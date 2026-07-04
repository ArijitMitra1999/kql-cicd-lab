pipeline {
    agent any

    stages {
        stage('CI: Validate KQL') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    reuseNode true
                }
            }
            steps {
                echo 'Running KQL validation...'
                sh 'python3 scripts/validate_kql.py'
            }
        }

        stage('Approval Gate') {
            steps {
                input message: 'KQL passed. Approve deployment?', ok: 'Deploy'
            }
        }

        stage('CD: Deploy') {
            steps {
                echo 'Deploying validated KQL to Sentinel...'
                echo 'Deployment complete.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}