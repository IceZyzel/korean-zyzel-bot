pipeline{
    agent any
    environment
    {
        registry = "https://529088291614.dkr.ecr.us-east-1.amazonaws.com" 
        registryCredential = 'ecr:us-east-1:awscreds' 
        imageName = "529088291614.dkr.ecr.us-east-1.amazonaws.com/jenkinstgbot" 
        cluster = "jenkinstgbot"
        service = "tgbot"
    }
    stages{
        stage("Fetch code"){
            steps{
                git branch: 'main', url: 'https://github.com/IceZyzel/korean-zyzel-bot.git'
            }
            }
        stage("Build bot image"){
            steps{
                script {
                    dockerImage = docker.build( imageName + ":$BUILD_NUMBER",".")
                }
            }
            }
         stage("Upload bot image") {
            steps {
                script {
                    docker.withRegistry(registry, registryCredential) {
                        dockerImage.push("${BUILD_NUMBER}")
                        dockerImage.push("latest")
                    }
                }
            }
    }
         stage("remove container") {
    steps {
        sh '''
        containers=$(docker ps -a -q)
        if [ -n "$containers" ]; then
            docker rm -f $containers
        else
            echo "No containers to remove"
        fi
        '''
        
        // Удалить образы, если они есть
        sh '''
        images=$(docker images -a -q)
        if [ -n "$images" ]; then
            docker rmi -f $images
        else
            echo "No images to remove"
        fi
        '''
    }
}
    }
}