Day 1: **Install Docker Packages and Start Docker Service** 
The Nautilus DevOps team aims to containerize various applications following a recent meeting with the application development team. They intend to conduct testing with the following steps:
Install docker-ce and docker compose packages on App Server 3.

Initiate the docker service.

Ans:
# Install using the rpm repository: 
sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
# Install Docker Engine
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable --now docker

Day 2: **Deploy Nginx Container on Application Server** 
The Nautilus DevOps team is conducting application deployment tests on selected application servers. They require a nginx container deployment on Application Server 2. Complete the task with the following instructions:

On Application Server 2 create a container named nginx_2 using the nginx image with the alpine tag. Ensure container is in a running state.
Ans:
docker pull nginx:alpine
docker run -d -p 8080:80 --name nginx_2 nginx:alpine
docker ps
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nginx_2
curl 172.12.0.2

Day 3: **Delete Docker Container** 
To delete the `kke-container` from **App Server 3** in Stratos DC, follow these steps:
### 🧹 Steps to Remove the Container

1. **Access App Server 3**  
   First, SSH into App Server 3. If you're using a bastion host or jump server, make sure to route through it:
   
   ssh user@appserver3
2. **Verify the container exists**  
   Run:
   docker ps -a | grep kke-container
   
  This confirms the container is present and shows its status.

3. **Stop the container (if running)**  
   docker stop kke-container

4. **Remove the container**  
    docker rm kke-container
   
5. **Confirm deletion**  
   Run:
      docker ps -a
      Ensure `kke-container` no longer appears in the list.

### ✅ Don't Forget:
If the container was created with volumes or networks, you might want to clean those up too:
docker volume prune
docker network prune

Day 4: **Copy File to Docker Container**
The Nautilus DevOps team possesses confidential data on App Server 1 in the Stratos Datacenter. A container named ubuntu_latest is running on the same server. Copy an encrypted file /tmp/nautilus.txt.gpg from the docker host to the ubuntu_latest container located at /tmp/. Ensure the file is not modified during this operation.

Ans:
To copy the encrypted file `/tmp/nautilus.txt.gpg` from the Docker host to the `ubuntu_latest` container without modifying it, follow these steps:

### 🛠️ Step-by-Step Instructions

1. **Identify the container ID or name**  
   Since the container is named `ubuntu_latest`, you can confirm it's running with:   
   docker ps
   
   Look for the container named `ubuntu_latest` and note its **CONTAINER ID** if needed.

2. **Copy the file into the container**  
   Use the `docker cp` command to copy the file from the host to the container:
   
   docker cp /tmp/nautilus.txt.gpg ubuntu_latest:/tmp/nautilus.txt.gpg

   This command ensures the file is transferred **as-is**, preserving its encrypted state.

3. **Verify the file inside the container (optional)**  
   You can exec into the container to confirm the file exists:
   
   docker exec -it ubuntu_latest ls -l /tmp/nautilus.txt.gpg

Day 5 **Troubleshoot Docker Container Issue**
An issue has arisen with a static website running in a container named nautilus on App Server 1. To resolve the issue, investigate the following details:

Check if the container's volume /usr/local/apache2/htdocs is correctly mapped with the host's volume /var/www/html.

Verify that the website is accessible on host port 8080 on App Server 1. Confirm that the command curl http://localhost:8080/ works on App Server 1.

Ans:
To troubleshoot the static website issue on App Server 1 with the container named `nautilus`, follow these steps:

### 🔍 Step 1: Check Volume Mapping

Ensure that the container's internal path `/usr/local/apache2/htdocs` is correctly mapped to the host's `/var/www/html`.

1. **Inspect the container:**
   
   docker inspect nautilus
   

2. **Look for the `Mounts` section** in the output. You should see something like:
   json
   "Mounts": [
     {
       "Type": "bind",
       "Source": "/var/www/html",
       "Destination": "/usr/local/apache2/htdocs",
       ...
     }
   ]
   

   ✅ If this mapping is present, the volume is correctly configured.

   ❌ If not, you may need to recreate the container with the correct volume mapping:
   
   docker run -d --name nautilus -p 8080:80 -v /var/www/html:/usr/local/apache2/htdocs httpd

### 🌐 Step 2: Verify Website Accessibility on Port 8080

1. **Check if the container is running:**
   
   docker ps

   Ensure `nautilus` is listed and port `8080` is mapped to container port `80`.

2. **Test with curl:**
   
   curl http://localhost:8080/
   

   ✅ If you see HTML output or the expected page content, the site is accessible.

   ❌ If you get an error (e.g., connection refused), check:
   - Whether the container is running.
   - Whether port `8080` is correctly mapped.
   - Whether the container has content in `/usr/local/apache2/htdocs`.

**Final Test Question:**
Q1:
The Nautilus team wants to create a debug container on Application Server 3. However, they had some specific requirements related to the CMD. Please complete the task as per details given below:


a. On Application Server 3 create a container named debug_3 using image ubuntu/apache2:latest.

b. Overwrite the default CMD with command sleep 1000.

c. Make sure the container is in running state.
Ans:
To fulfill the Nautilus team's requirements, you can run the following command on Application Server 3:
docker run -d --name debug_3 ubuntu/apache2:latest sleep 1000
Verification:
docker ps -f name=debug_3

Q2:
The Nautilus DevOps team is testing some applications deployment on some of the application servers. They need to deploy a nginx container on Application Server 3. Please complete the task as per details given below:


On Application Server 3 create a container named nginx_3 using image nginx with alpine tag and make sure container is in running state.
Ans:
To deploy the required Nginx container on Application Server 3, use the following command:
docker run -d --name nginx_3 nginx:alpine
Verify it's running:
docker ps -f name=nginx_3

Q3:
The Nautilus DevOps team has some confidential data present on App Server 3 in Stratos Datacenter. There is a container ubuntu_latest running on the same server. We received a request to copy some of the data from the docker host to the container. Below are more details about the task:



On App Server 3 in Stratos Datacenter copy an encrypted file /tmp/nautilus.txt.gpg from docker host to ubuntu_latest container (running on same server) in /home/ location (create this location if doesn't exit). Please do not try to modify this file in any way.
Ans:
To copy the encrypted file from the Docker host to the `ubuntu_latest` container on **App Server 3**, follow these steps:

### ✅ Step-by-step Instructions

1. **Ensure the container is running**:
   
   docker ps -f name=ubuntu_latest
   

2. **Create `/home` directory inside the container (if it doesn't exist)**:
   
   docker exec ubuntu_latest mkdir -p /home
   

3. **Copy the file from host to container**:
   
   docker cp /tmp/nautilus.txt.gpg ubuntu_latest:/home/
   

### 🔍 Verification

To confirm the file was copied successfully:

docker exec ubuntu_latest ls -l /home/


You should see `nautilus.txt.gpg` listed there.
Q4:
We received a request to copy some of the data from one of the docker containers to the docker host. The container is running on App Server 3 in Stratos Datacenter. Below are more details about the task:


On App Server 3 in Stratos Datacenter copy an encrypted file /tmp/test.txt.gpg from development_3 docker container to the docker host in /tmp location. Please do not try to modify this file in any way.
Ans:
To copy the encrypted file from the `development_3` container to the Docker host on **App Server 3**, follow these steps:

### ✅ Step-by-step Instructions

1. **Ensure the container is running**:
   
   docker ps -f name=development_3
   

2. **Copy the file from container to host**:
   
   docker cp development_3:/tmp/test.txt.gpg /tmp/
   

### 🔍 Verification

To confirm the file was copied successfully:

ls -l /tmp/test.txt.gpg


You should see the file listed with its original size and timestamp intact.

Q5:
The Nautilus DevOps team is doing some cleanup work on all servers in Stratos DC. They were also looking for some unwanted and heavy docker images if present and can be cleaned.


On App Server 3 in Stratos Datacenter look for the docker images with size more than 100MB, delete all such docker images.

List all Docker images with their sizes:
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.ID}}"
Delete those images:

docker images --format "{{.ID}} {{.Size}}" | while read id size; do
  num=$(echo $size | grep -oE '^[0-9]+')
  unit=$(echo $size | grep -oE '[A-Z]+$')
  if [ "$unit" = "MB" ] && [ "$num" -gt 100 ]; then
    docker rmi -f "$id"
  fi
done
Verify Cleanup:
docker images

Q6:
There is a docker image on Application Server 3 in Stratos DC. This image needs to be retagged as per details given below:


Re-tag the nginx:mainline-alpine3.18-slim image as nginx:nautilus
Ans:
To re-tag the Docker image on Application Server 3, use the following command:
docker tag nginx:mainline-alpine3.18-slim nginx:nautilus

Verify tag:
docker images | grep nginx

Q7:
The Nautilus DevOps team is planning to do some cleanup on App Server 3 in Stratos Datacenter, some old and unused docker networks need to be deleted. Find below more details:


Delete a docker network named php-network from App Server 3 in Stratos Datacenter.
Ans:
To delete the Docker network named `php-network` on **App Server 3**, run the following command:


docker network rm php-network


### ✅ Before You Run It:
You can verify the network exists with:

docker network ls | grep php-network


If the network is currently in use by any containers, you'll need to disconnect them first:

docker network disconnect php-network <container_name_or_id>


Q8:
The Nautilus DevOps team is planning to setup/create some docker containers on App Server 3 in Stratos Datacenter, some prerequisites are needs to be done on this server. Find below more details:

Create a new network named mysql-network using the bridge driver. Allocate subnet 182.18.0.0/24, configure Gateway 182.18.0.1.
Ans:
To create the Docker network `mysql-network` with the specified subnet and gateway on **App Server 3**, run the following command:

docker network create \
  --driver bridge \
  --subnet 182.18.0.0/24 \
  --gateway 182.18.0.1 \
  mysql-network

### ✅ What this does:
- `--driver bridge`: Uses the bridge network driver.
- `--subnet`: Allocates the IP range `182.18.0.0/24`.
- `--gateway`: Sets the gateway to `182.18.0.1`.
- `mysql-network`: Names the network.

### 🔍 Verify the network:

docker network inspect mysql-network

You’ll see the subnet and gateway listed in the output.

Q9:
There was a docker container deployed on App Server 3. Suddenly, team found that the container is crashing. Look into the issue to fix the same, you can find more details below:


The container name is apple_alpine. You can even re-create the container if needed, just make sure its in running state
Ans:
To troubleshoot and resolve the issue with the `apple_alpine` container on **App Server 3**, follow these steps:

### 🔍 Step 1: Check Container Status and Logs

docker ps -a | grep apple_alpine
docker logs apple_alpine

This will show whether the container exited and why. Common issues include missing commands, misconfigured entrypoints, or missing images.

### 🔧 Step 2: Remove and Re-create the Container
If the container is crashing and logs don’t help, it’s best to re-create it cleanly:

docker rm -f apple_alpine
docker run -d --name apple_alpine alpine sleep 1000

- `alpine`: Uses the lightweight Alpine Linux image.
- `sleep 1000`: Keeps the container running for a long time.

### ✅ Step 3: Verify It's Running

docker ps -f name=apple_alpine

You should see the container listed with status `Up`.

**Level 2**
# Q1: Pull Docker Image
Nautilus project developers are planning to start testing on a new project. As per their meeting with the DevOps team, they want to test containerized environment application features. As per details shared with DevOps team, we need to accomplish the following task:

a. Pull busybox:musl image on App Server 2 in Stratos DC and re-tag (create new tag) this image as busybox:blog.
Ans:
# Pull the image
docker pull busybox:musl

# Re-tag the image old tag new tag
docker tag busybox:musl busybox:blog


# Q2: Docker Update Permissions
One of the Nautilus project developers need access to run docker commands on App Server 1. This user is already created on the server. Accomplish this task as per details given below:

User james is not able to run docker commands on App Server 1 in Stratos DC, make the required changes so that this user can run docker commands without sudo.
Ans:
# Run the following command on App Server 1:
sudo usermod -aG docker james
# You can check if user james is added to the docker group using any of the following methods on App Server 1:
groups james  or id james or  grep docker /etc/group


# Q3: Create a Docker Image From Container
One of the Nautilus developer was working to test new changes on a container. He wants to keep a backup of his changes to the container. A new request has been raised for the DevOps team to create a new image from this container. Below are more details about it:


a. Create an image media:devops on Application Server 1 from a container ubuntu_latest that is running on same server.
Ans:
To create a new Docker image named **`media:devops`** from the **`ubuntu_latest`** container on **App Server 1**, follow the steps below:

### ✅ Step-by-step Instructions (on App Server 1)

1. **Ensure the container `ubuntu_latest` is running:**

docker ps | grep ubuntu_latest

> If it's not running, you may need to start it with:

docker start ubuntu_latest

2. **Commit the container as a new image:**

docker commit ubuntu_latest media:devops

> 🔸 This creates a new image called `media` with the tag `devops` from the current state of `ubuntu_latest`.

3. **Verify the image was created:**

docker images | grep media

You should see something like:

media        devops     <IMAGE_ID>   ...


### ✅ Summary

* `docker commit <container> <image>:<tag>` is the command to create an image from a container’s current state.
* In your case:
  `docker commit ubuntu_latest media:devops`

# Q4: Docker EXEC Operations
One of the Nautilus DevOps team members was working to configure services on a kkloud container that is running on App Server 3 in Stratos Datacenter. Due to some personal work he is on PTO for the rest of the week, but we need to finish his pending work ASAP. Please complete the remaining work as per details given below:

a. Install apache2 in kkloud container using apt that is running on App Server 3 in Stratos Datacenter.

b. Configure Apache to listen on port 3004 instead of default http port. Do not bind it to listen on specific IP or hostname only, i.e it should listen on localhost, 127.0.0.1, container ip, etc.

c. Make sure Apache service is up and running inside the container. Keep the container in running state at the end
Ans:

 1  apt update
    2  apt install apache2
    3  sed -i 's/^Listen 80$/Listen 3004/' /etc/apache2/ports.conf
    4  srevice apache2 restart 
    5  service apache2 restart 
    * Restarting Apache httpd web server apache2                                                                                                                    AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.12.0.2. Set the 'ServerName' directive globally to suppress this message
                
    6  echo "ServerName localhost" > /etc/apache2/conf-available/servername.conf
    7  a2enconf servername
    8  service apache2 restart 
    9  netstat -tuln | grep 3004 or ss -tuln | grep 3004
   12  apt install -y net-tools
   13  netstat -tuln | grep 3004
# Q5: Write a Docker File
As per recent requirements shared by the Nautilus application development team, they need custom images created for one of their projects. Several of the initial testing requirements are already been shared with DevOps team. Therefore, create a docker file /opt/docker/Dockerfile (please keep D capital of Dockerfile) on App server 2 in Stratos DC and configure to build an image with the following requirements:

a. Use ubuntu:24.04 as the base image.

b. Install apache2 and configure it to work on 6400 port. (do not update any other Apache configuration settings like document root etc).
Ans:
# Use Ubuntu 24.04 base image
FROM ubuntu:24.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install apache2
RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean

# Change Apache to listen on port 6400
RUN sed -i 's/^Listen 80$/Listen 6400/' /etc/apache2/ports.conf

# Expose port 6400
EXPOSE 6400

# Start Apache in foreground
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

**Level 3**
# Q1 Create a Docker Network
The Nautilus DevOps team needs to set up several docker environments for different applications. One of the team members has been assigned a ticket where he has been asked to create some docker networks to be used later. Complete the task based on the following ticket description:

a. Create a docker network named as beta on App Server 1 in Stratos DC.

b. Configure it to use bridge drivers.

c. Set it to use subnet 172.28.0.0/24 and iprange 172.28.0.0/24.
Ans:
docker network create \
  --driver bridge \
  --subnet 172.28.0.0/24 \
  --ip-range 172.28.0.0/24 \
  beta
# Verify the Network:
docker network inspect beta

# Q2 Docker Volumes Mapping
The Nautilus DevOps team is testing applications containerization, which is supposed to be migrated on docker container-based environments soon. In today's stand-up meeting one of the team members has been assigned a task to create and test a docker container with certain requirements. Below are more details:

a. On App Server  1 in Stratos DC pull nginx image (preferably latest tag but others should work too).

b. Create a new container with name demo from the image you just pulled.

c. Map the host volume /opt/sysops with container volume /tmp. There is an sample.txt file present on same server under /tmp; copy that file to /opt/sysops. Also please keep the container in running state.
Ans:

### 1️⃣ Pull the NGINX image

docker pull nginx:latest

You can also use:

docker pull nginx

### 2️⃣ Create the host directory `/opt/sysops` (if it doesn’t exist)

mkdir -p /opt/sysops

### 3️⃣ Copy the file `sample.txt` to `/opt/sysops`

cp /tmp/sample.txt /opt/sysops/

You can verify:
ls -l /opt/sysops/

### 4️⃣ Run the container with volume mounted

docker run -d \
  --name demo \
  -v /opt/sysops:/tmp \
  nginx

Explanation:

* `-d`: run in detached mode (keeps it running)
* `--name demo`: name the container
* `-v /opt/sysops:/tmp`: mount host `/opt/sysops` to container’s `/tmp`

### 5️⃣ ✅ Verify Container and File

#### Check if the container is running:

docker ps

You should see a container named `demo` running.

#### Check if the file is visible inside the container:

docker exec demo ls /tmp

Expected output:

sample.txt

# Q3 Docker Ports Mapping
The Nautilus DevOps team is planning to host an application on a nginx-based container. There are number of tickets already been created for similar tasks. One of the tickets has been assigned to set up a nginx container on Application Server 3 in Stratos Datacenter. Please perform the task as per details mentioned below:

a. Pull nginx:stable docker image on Application Server 3.

b. Create a container named beta using the image you pulled.

c. Map host port 8088 to container port 80. Please keep the container in running state.
Ans:
docker run -d --name beta -p 8088:80 nginx:stable

# Q4 Save, Load and Transfer Docker Image
One of the DevOps team members was working on to create a new custom docker image on App Server 1 in Stratos DC. He is done with his changes and image is saved on same server with name blog:datacenter. Recently a requirement has been raised by a team to use that image for testing, but the team wants to test the same on App Server 3. So we need to provide them that image on App Server 3 in Stratos DC.

a. On App Server 1 save the image blog:datacenter in an archive.

b. Transfer the image archive to App Server 3.

c. Load that image archive on App Server 3 with same name and tag which was used on App Server 1.

Note: Docker is already installed on both servers; however, if its service is down please make sure to start it.
Ans:
**On Server1:**
1 docker images
# Save the Docker image to a tar archive
2 docker save -o blog_datacenter_image.tar blog:datacenter
# Transfer the archive from App Server 1 to App Server 3 
3 scp blog_datacenter_image.tar banner@stapp03:/home/banner/
**On Server3:**
# Load the Docker image from the archive
1  docker load -i /home/banner/blog_datacenter_image.tar 
# Verify the image is loaded with the correct tag
2  docker images | grep blog

# Q5 Write a Docker Compose File
The Nautilus application development team shared static website content that needs to be hosted on the httpd web server using a containerised platform. The team has shared details with the DevOps team, and we need to set up an environment according to those guidelines. Below are the details:

a. On App Server 1 in Stratos DC create a container named httpd using a docker compose file /opt/docker/docker-compose.yml (please use the exact name for file).

b. Use httpd (preferably latest tag) image for container and make sure container is named as httpd; you can use any name for service.

c. Map 80 number port of container with port 8085 of docker host.

d. Map container's /usr/local/apache2/htdocs volume with /opt/finance volume of docker host which is already there. (please do not modify any data within these locations).

Ans:
version: '3'
services:
  webserver:
    image: httpd:latest
    container_name: httpd
    ports:
      - "8085:80"
    volumes:
      - /opt/finance:/usr/local/apache2/htdocs

**Level 4**
# Q1 Resolve Dockerfile Issues
The Nautilus DevOps team is working to create new images per requirements shared by the development team. One of the team members is working to create a Dockerfile on App Server 2 in Stratos DC. While working on it she ran into issues in which the docker build is failing and displaying errors. Look into the issue and fix it to build an image as per details mentioned below:

a. The Dockerfile is placed on App Server 2 under /opt/docker directory.

b. Fix the issues with this file and make sure it is able to build the image.

c. Do not change base image, any other valid configuration within Dockerfile, or any of the data been used — for example, index.html.

Note: Please note that once you click on FINISH button all the existing containers will be destroyed and new image will be built from your Dockerfile.
Ans:
SSH steve@stapp02
# Exising FIle: cat /opt/docker/Dockerfile

FROM httpd:2.4.43

RUN sed -i "s/Listen 80/Listen 8080/g" /usr/local/apache2/conf/httpd.conf

RUN sed -i '/LoadModule\ ssl_module modules\/mod_ssl.so/s/^#//g' conf/httpd.conf

RUN sed -i '/LoadModule\ socache_shmcb_module modules\/mod_socache_shmcb.so/s/^#//g' conf/httpd.conf

RUN sed -i '/Include\ conf\/extra\/httpd-ssl.conf/s/^#//g' conf/httpd.conf

RUN cp certs/server.crt /usr/local/apache2/conf/server.crt

RUN cp certs/server.key /usr/local/apache2/conf/server.key

RUN cp html/index.html /usr/local/apache2/htdocs
# Solution:
# Missing WORKDIR and COPY usage:

You're using RUN cp assuming that certs/ and html/ already exist in the container context. They likely exist on your host, so you should be using COPY instead.

# Use a single RUN for multiple commands:
Combine the multiple sed commands into a single RUN to reduce image layers.
# Expose port 8080 and 443:
Since HTTP is moved to port 8080 and SSL is enabled (default on 443), explicitly expose those.

**Final Optimized Dockerfile**
FROM httpd:2.4.43
# Switch Apache to listen on port 8080 and enable SSL
RUN sed -i "s/Listen 80/Listen 8080/g" /usr/local/apache2/conf/httpd.conf && \
    sed -i '/LoadModule\ ssl_module modules\/mod_ssl.so/s/^#//g' conf/httpd.conf && \
    sed -i '/LoadModule\ socache_shmcb_module modules\/mod_socache_shmcb.so/s/^#//g' conf/httpd.conf && \
    sed -i '/Include\ conf\/extra\/httpd-ssl.conf/s/^#//g' conf/httpd.conf

# Copy certificate and key
COPY certs/server.crt /usr/local/apache2/conf/
COPY certs/server.key /usr/local/apache2/conf/

# Replace index page
COPY html/index.html /usr/local/apache2/htdocs/

# Expose HTTP and HTTPS ports
EXPOSE 8080 443


# Q2 Resolve Docker Compose Issues
# Q3 Deploy an App on Docker Containers
# Q4 Docker Node App
# Q5 Docker Python App