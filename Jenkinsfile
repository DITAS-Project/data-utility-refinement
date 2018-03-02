pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.build'
            // Bind mount the docker socker to allow a container with docker installed to create images
            // TO-DO add a cache volume for NPM?
            args '-u 0 -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building! new"'
                sh 'npm install --prefix src'
            }
        }
        stage('Image creation') {
            steps {
                echo 'Creating the image...'
                // This will search for a Dockerfile in the src folder and will build the image to the local repository
                sh "docker build -t \"aitorf/data-utility-refinement:${env.BUILD_ID}\" -f src/Dockerfile ."
                echo "Done"
            }
        }
        stage('Push image') {
            steps {
                echo 'Retrieving Docker Hub password from /opt/ditas-docker-hub.passwd...'
                // Get the password from a file. This reads the file from the host, not the container. Slaves already have the password in there.
                script {
                    password = readFile '/opt/ditas-docker-hub.passwd'
                }
                echo "Done"
                // TODO change this to the ditas official Docker Hub user
                echo 'Login to Docker Hub as aitorf...'
                sh "docker login -u aitorf -p ${password}"
                echo "Done"
                echo "Pushing the image aitorf/data-utility-refinement:${env.BUILD_ID}..."
                sh "docker push aitorf/sdata-utility-refinement:${env.BUILD_ID}"
                echo "Done"
            }
        }
    }
    post {
        always {
            echo 'Post action fired'

        }

    }
}
