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
      script {
        docker.build("db", "src")
      }
    }
  }
  post {
    always {
      echo 'Post action fired'

    }

  }
}
