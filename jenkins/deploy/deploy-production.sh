#!/usr/bin/env bash
# IDEKO SDK production environment: 153.92.30.56
# OSR SDK production environment: 153.92.30.225

# SSH to the IDEKO and deploy SDK component there
ssh -i /opt/keypairs/ideko-sdk-key.pem cloudsigma@153.92.30.56 << 'ENDSSH'
# Ensure that a previously running instance is stopped (-f stops and removes in a single step)
# || true - "docker stop" fails with exit status 1 if image doen't exists, what makes the Pipeline fail. the "|| true" forces the command to exit with 0
# Try a graceful stop: 20 seconds for SIGTERM and SIGKILL after that
sudo docker stop --time 20 data-utility-refinement || true
sudo docker rm --force data-utility-refinement || true
sudo docker pull ditas/data-utility-refinement:production
# Get the host IP
HOST_IP="$(ip route get 8.8.8.8 | awk '{print $NF; exit}')"
# Run the docker mapping the ports and passing the host IP via the environmental variable "DOCKER_HOST_IP"
sudo docker run -p 50000:8080 -e DOCKER_HOST_IP=$HOST_IP --restart unless-stopped -d --name data-utility-refinement ditas/data-utility-refinement:production
ENDSSH

# SSH to the OSR and deploy SDK component there
ssh -i /opt/keypairs/osr-sdk-key.pem cloudsigma@153.92.30.225 << 'ENDSSH'
# Ensure that a previously running instance is stopped (-f stops and removes in a single step)
# || true - "docker stop" fails with exit status 1 if image doen't exists, what makes the Pipeline fail. the "|| true" forces the command to exit with 0
# Try a graceful stop: 20 seconds for SIGTERM and SIGKILL after that
sudo docker stop --time 20 data-utility-refinement || true
sudo docker rm --force data-utility-refinement || true
sudo docker pull ditas/data-utility-refinement:production
# Get the host IP
HOST_IP="$(ip route get 8.8.8.8 | awk '{print $NF; exit}')"
# Run the docker mapping the ports and passing the host IP via the environmental variable "DOCKER_HOST_IP"
sudo docker run -p 50000:8080 -e DOCKER_HOST_IP=$HOST_IP --restart unless-stopped -d --name data-utility-refinement ditas/data-utility-refinement:production
ENDSSH