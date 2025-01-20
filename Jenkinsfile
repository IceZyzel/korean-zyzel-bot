pipeline{
    agent{
        label "master"
    }
    stages{
        stage("Fetch code"){
            steps{
                git branch 'main', url 'https://github.com/IceZyzel/korean-zyzel-bot.git'
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}