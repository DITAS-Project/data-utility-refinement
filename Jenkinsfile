pipeline {
  agent {
    docker {
      image 'node:carbon'
      args '-p 8080:8080'
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'echo "Building! new"'
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
