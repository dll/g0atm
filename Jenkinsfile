pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python sources/add2vals.py sources/calc.py'
            }
        }
    }
}