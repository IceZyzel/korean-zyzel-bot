pipeline{
    agent any
    environment
    {
        registry = "credentials('ecr-registry-url')" 
        registryCredential = 'ecr:us-east-1:awscreds' 
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
                    dockerImage = docker.build( registry + ":$BUILD_NUMBER",".")
                }
            }
            }
         stage("Upload bot image") {
            steps {
                script {
                    docker.withRegistry("https://${registry}", registryCredential) {
                        dockerImage.push("${BUILD_NUMBER}")
                        dockerImage.push("latest")
                    }
                }
            }
    }
}
}