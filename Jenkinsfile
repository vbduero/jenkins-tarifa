pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/vbduero/jenkins-tarifa.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh '''
                    which pip3 || (apt update && apt install -y python3-pip)
                    pip3 install --upgrade pip
                    pip3 install -r requirements.txt || true
                '''
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh 'python3 -m unittest test_calcular_tarifa.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado.'
        }
        success {
            echo '✅ Todas las pruebas pasaron correctamente.'
        }
        failure {
            echo '❌ Fallaron algunas pruebas.'
        }
    }
}

