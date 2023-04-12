pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python -m compileall  sources/add2vals.py sources/calc.py'
            }
        }
    }
}