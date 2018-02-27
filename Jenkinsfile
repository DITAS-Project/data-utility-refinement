pipeline {
  agent {
    docker {
      image 'node:6-alpine'
      wget https://get.docker.com/builds/Linux/x86_64/docker-1.11.0.tgz -O docker.tgz
      tar -xvzf docker.tgz
      mv docker/* /usr/bin/
      chmod +x /usr/bin/docker
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
