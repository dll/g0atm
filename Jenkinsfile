pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'python -m py_compile g0atm0/login_atm.py'
            }
        }
        stage('Test') {
            steps {
                bat 'py.test --verbose --junit-xml test-reports/results.xml g0atm0/test_login_atm.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            steps {
                bat 'pyinstaller --onefile g0atm0/login_atm.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/login_atm.exe'
                }
            }
        }
    }
}