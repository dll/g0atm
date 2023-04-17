pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'python -m py_compile g0atm0/LoginATM-mysql.py'
            }
        }
        stage('Test') {
            echo "待开发"
            //steps {
            //    bat 'py.test --verbose --junit-xml test-reports/results.xml g0atm0/test_LoginATM-mysql.py'
            //}
            //post {
            //    always {
            //        junit 'test-reports/results.xml'
            //    }
            //}
        }
        stage('Deliver') {
            steps {
                bat 'pyinstaller --onefile g0atm0/LoginATM-mysql.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/LoginATM-mysql.exe'
                }
            }
        }
    }
}