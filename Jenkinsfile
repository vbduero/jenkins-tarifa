pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/vbduero/jenkins-tarifa.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
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
            echo 'Pipeline completado.'
        }
    }
}

