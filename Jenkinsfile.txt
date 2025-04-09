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
                    def salida = bat(script: 'python tarifa.py', returnStdout: true)
                    echo salida
                }
            }
        }
    }
}
