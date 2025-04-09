pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                echo 'Repositorio clonado automáticamente por Jenkins.'
            }
        }

        stage('Ejecutar tarifa.py') {
            steps {
                script {
                    sh 'python3 tarifa.py'
                }
            }
        }
    }
}
