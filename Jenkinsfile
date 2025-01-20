pipeline{
    agent any
    environment
    {
        registry = "529088291614.dkr.ecr.us-east-1.amazonaws.com" 
        registryCredential = 'ecr:us-east-1:awscreds' 
        imageName = "529088291614.dkr.ecr.us-east-1.amazonaws.com/jenkinstgbot529088291614.dkr.ecr.us-east-1.amazonaws.com/jenkinstgbot" 
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
}
}