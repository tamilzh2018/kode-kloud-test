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

# Q5: Write a Docker File

**Level 3**
# Q1 Create a Docker Network
# Q2 Docker Volumes Mapping
# Q3 Docker Ports Mapping
# Q4 Save, Load and Transfer Docker Image
# Q5 Write a Docker Compose File

**Level 4**
# Q1 Resolve Dockerfile Issues
# Q2 Resolve Docker Compose Issues
# Q3 Deploy an App on Docker Containers
# Q4 Docker Node App
# Q5 Docker Python App