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
    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
         echo 'Build image'
        app = docker.build("ditas-project/data-utility-refinement")
    }
    stage('Push image') {
            /* Finally, we'll push the image with two tags:
             * First, the incremental build number from Jenkins
             * Second, the 'latest' tag.
             * Pushing multiple tags is cheap, as all the layers are reused. */
            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials-plebanip') {
                app.push("${env.BUILD_NUMBER}")
                app.push("latest")
            }
        }
  }
  post {
    always {
      echo 'Post action fired'

    }

  }
}
