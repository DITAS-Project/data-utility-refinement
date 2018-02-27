pipeline {
  agent {
    docker {
      image 'node:6-alpine'
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'echo "Building! new"'
        sh 'npm install --prefix src'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying!'
      }
    }
  }
  post {
    always {
      echo 'Post action fired'

    }

  }
}
