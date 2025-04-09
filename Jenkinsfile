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
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt || true'  // por si no tienes dependencias
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                echo "Ejecutando tests con unittest"
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
