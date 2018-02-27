pipeline {
  agent {
    dockerfile {
      dir 'build'
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
