pipeline {
  agent {
    docker {
      image 'docker'
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
        sh "docker images"
      }
    }
  }
  post {
    always {
      echo 'Post action fired'

    }

  }
}
