pipeline{
    agent any
    environment
    {
        imageName = 'tgbot'
    }
    stages{
        stage("Fetch code"){
            steps{
                git branch 'main', url 'https://github.com/IceZyzel/korean-zyzel-bot.git'
            }
            }
        stage("Build bot image"){
            steps{
                script {
                    dockerImage = docker.build( imageName + ":$BUILD_NUMBER",".")
                }
            }
            }
    }
}
