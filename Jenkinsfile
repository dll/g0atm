pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'python -m py_compile g0atm0/LoginATM-mysql.py'
            }
        }
        stage('Test') {
            steps {
                //echo "待开发"
                bat 'py.test --verbose --junit-xml test-reports/results.xml g0atm0/test_login_atm_mysql.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
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