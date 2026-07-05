pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Banani07/devops-python-toolkit.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t system-health .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run --rm system-health'
            }
        }

        stage('Verify Build') {
            steps {
                echo 'Build completed successfully!'
            }
        }
    }
}