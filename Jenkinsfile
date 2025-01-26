pipeline {
    agent any
    environment {
        registry = "https://529088291614.dkr.ecr.us-east-1.amazonaws.com"
        registryCredential = 'ecr:us-east-1:awscreds'
        imageName = "529088291614.dkr.ecr.us-east-1.amazonaws.com/jenkinstgbot"
        ec2Host = "54.208.129.52"
        sshCredentialsId = "54.165.247.133" // ID сохранённых SSH кредов Jenkins
        remotePath = "/home/ec2-user/tgbot" // Путь на EC2 для хранения файлов
    }
    stages {
        stage("Fetch code") {
            steps {
                git branch: 'main', url: 'https://github.com/IceZyzel/korean-zyzel-bot.git'
            }
        }
        stage("Build bot image") {
            steps {
                script {
                    dockerImage = docker.build(imageName + ":$BUILD_NUMBER", ".")
                }
            }
        }
       stage("Deploy to EC2") {
            steps {
                sshagent(credentials: [sshCredentialsId]) {
                    // Копируем docker-compose.yml и token.env на EC2
                    sh """
                    scp -o StrictHostKeyChecking=no docker-compose.yml ec2-user@${ec2Host}:${remotePath}
                    scp -o StrictHostKeyChecking=no token.env ec2-user@${ec2Host}:${remotePath}
                    """

                    // Запускаем контейнеры на EC2
                    sh """
                    ssh -o StrictHostKeyChecking=no ec2-user@${ec2Host} "
                    cd ${remotePath} &&
                    docker-compose down &&
                    docker-compose up -d"
                    """
                }
            }
        }
        stage("Cleanup local Docker images") {
            steps {
                sh 'docker system prune -af'
            }
        }
    }
}
