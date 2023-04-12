pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python -Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true sources/add2vals.py sources/calc.py'
            }
        }
    }
}