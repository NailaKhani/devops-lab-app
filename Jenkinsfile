pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Nailakhani/devops-lab-app.git', branch: 'main'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("devops-lab-app:latest")
                }
            }
        }
        
        stage('Run Docker Container') {
            steps {
                script {
                    docker.image("devops-lab-app:latest").run("-p 5000:5000 -d --name myapp-jenkins")
                }
            }
        }
        
        stage('Verify Application') {
            steps {
                sh 'echo "Application is running on http://localhost:5000"'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}