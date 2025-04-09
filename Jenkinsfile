pipeline {
    agent {
        docker {
            image 'python:3.10'   // Imagen oficial de Python con pip incluido
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/vbduero/jenkins-tarifa.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                echo "Ejecutando tests con unittest"
                sh 'python -m unittest test_calcular_tarifa.py'
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

