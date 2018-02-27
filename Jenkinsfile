pipeline {
  agent any
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
