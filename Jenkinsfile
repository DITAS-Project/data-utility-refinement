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
    stage('Docker build') {
      steps {
        sh 'docker build -t plebanip/data-utility-refinement:latest .'
      }
    }
  }
  post {
    always {
      echo 'Post action fired'

    }

  }
}
