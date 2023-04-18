<<<<<<< HEAD
//2023-04-13
//ldl 改写自Jenkins docs官网simple-python-pyinstaller-app的Docker版本
//JDK11，JDK17 +
=======
>>>>>>> b2dd236 (g0atm流水线登录功能的初始版本，连接MySQL v0.0.1)
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
<<<<<<< HEAD
                bat 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
        stage('Test') {
            steps {
                bat 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            steps {
                bat 'pyinstaller --onefile sources/add2vals.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/add2vals.exe'
=======
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
>>>>>>> b2dd236 (g0atm流水线登录功能的初始版本，连接MySQL v0.0.1)
                }
            }
        }
    }
}