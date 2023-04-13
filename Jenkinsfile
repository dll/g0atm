// 2023-04-13，改写自Jenkins docs官网Docker版本
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile /sources/add2vals.py /sources/calc.py'
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
                }
            }
        }
    }
}