pipeline {
  agent {
    docker {
      image 'node:9-alpine'
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'echo "Building! new"'
        sh 'npm install --prefix src'
      }
    }
    stage('Docker build') {
      steps {
        script {
          docker.build("db", "src")
        }
      }
    }
  }
  post {
    always {
      echo 'Post action fired'

    }

  }
}
