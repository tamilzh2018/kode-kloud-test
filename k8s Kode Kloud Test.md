To deploy **Qwen** (the large language model from Tongyi Lab) in your **Kubernetes (K8s) cluster**, you need to follow several key steps, including:

1. **Obtaining the Qwen model**
2. **Setting up the environment**
3. **Creating a Docker image**
4. **Deploying the model to Kubernetes (K8s)**

Here's a step-by-step guide based on the assumption that you are using a GPU-enabled Kubernetes cluster.



## ✅ Prerequisites

- A running Kubernetes cluster with access for deployment (e.g. via `kubectl`)
- Access to Docker registry (e.g. Docker Hub, or your own private registry)
- GPU support if using GPU acceleration (e.g. NVIDIA devices and NVIDIA's Kubernetes device plugin)
- Python 3.8+ and CUDA (if training or inference uses GPU)



## 🔧 Step 1: Build or Pull Qwen Docker Image

You can find the Qwen model (Tongyi Chat, Qwen, etc.) on [Qwen's GitHub repository](https://github.com/QwenLM).

### Option A: Use an Existing Image

Check if there's a publicly available Docker image for Qwen (e.g. on Docker Hub or Harbor):

docker pull qwen/qwen:latest

### Option B: Build Your Own Image

1. Clone the repo:

git clone https://github.com/QwenLM/Qwen.git
cd Qwen


2. Build a Docker container:

docker build -t qwen-app:latest .

> Note: You may need to include `cu118`, `nvidia/cuda`, or other CUDA versions in your Dockerfile if GPU is involved.



## 📦 Step 2: Push Image to Registry

If you're using a private registry or Docker Hub (recommended for Kubernetes use):

docker tag qwen-app:latest your-registry/qwen-app:latest
docker push your-registry/qwen-app:latest

## 🚀 Step 3: Deploy to Kubernetes

Create a `deployment.yaml` file (adjust it for your environment):

apiVersion: apps/v1
kind: Deployment
metadata:
  name: qwen-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: qwen
  template:
    metadata:
      labels:
        app: qwen
    spec:
      containers:
      - name: qwen
        image: your-registry/qwen-app:latest
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 8000  # Replace with the model server port
        resources:
          limits:
            nvidia.com/gpu: 1  # If using GPU
          requests:
            nvidia.com/gpu: 1
      imagePullSecrets:
        - name: regcred  # If using a private registry


Also, create a `service.yaml`:

yaml
apiVersion: v1
kind: Service
metadata:
  name: qwen-svc
spec:
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 8000
  selector:
    app: qwen


Apply the configuration:


kubectl apply -f deployment.yaml
kubectl apply -f service.yaml




## 🔄 Step 4: Access the Model

Once deployed:

- Get the LoadBalancer IP or Ingress URL.
- You can send requests via:


curl -X POST http://<ip>:80/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello, how are you?"}'


Make sure your Qwen implementation includes a REST or HTTP-based endpoint like this.



## 🧠 Optional: GPU Configuration

If using NVIDIA GPUs:

- Install [NVIDIA Kubernetes device plugin](https://github.com/NVIDIA/k8s-device-plugin).
- Ensure your worker nodes have NVIDIA drivers and `nvidia-docker` set up properly.



## 🔐 Security and Best Practices

- Use a private registry with imagePullSecrets.
- Ensure access to your model is secured.
- Consider using Ingress with TLS if exposing publicly.



## 📚 References

- [Qwen GitHub Repository](https://github.com/QwenLM/Qwen)
- [NVIDIA Kubernetes GPU Setup](https://github.com/NVIDIA/k8s-device-plugin)
- [Kubernetes Deployment Guide](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)



## 🛠 Need Help with Specific Version or Setup?

Let me know:

- Which Qwen version? (Chat, Max, Qwen2, etc.)
- Are you using CPU or GPU?
- Do you have a specific framework (like Transformers, FastAPI, etc.)?
- Are you using a private registry?

I can generate a full `Dockerfile`, `deployment.yaml`, and setup script tailored to your needs.


1. **Deploy Pods in Kubernetes Cluster**
The Nautilus DevOps team is diving into Kubernetes for application management. One team member has a task to create a pod according to the details below:


Create a pod named pod-httpd using the httpd image with the latest tag. Ensure to specify the tag as httpd:latest.

Set the app label to httpd_app, and name the container as httpd-container.

Note: The kubectl utility on jump_host is configured to operate with the Kubernetes cluster.
Use the below yaml code:

apiVersion: v1
kind: Pod
metadata:
  name: pod-httpd
  labels:
    app: httpd_app
spec:
  containers:
    - name: httpd-container
      image: httpd:latest
      ports:
      - containerPort: 80


2. **Deploy Applications with Kubernetes Deployments**

The Nautilus DevOps team is delving into Kubernetes for app management. One team member needs to create a deployment following these details:


Create a deployment named nginx to deploy the application nginx using the image nginx:latest (ensure to specify the tag)




3. **Setup Kubernetes Namespaces and PODs**

The Nautilus DevOps team is planning to deploy some micro services on Kubernetes platform. The team has already set up a Kubernetes cluster and now they want to set up some namespaces, deployments etc. Based on the current requirements, the team has shared some details as below:

Create a namespace named dev and deploy a POD within it. Name the pod dev-nginx-pod and use the nginx image with the latest tag. Ensure to specify the tag as nginx:latest.

4. **Set Resource Limits in Kubernetes Pods**

The Nautilus DevOps team has noticed performance issues in some Kubernetes-hosted applications due to resource constraints. To address this, they plan to set limits on resource utilization. Here are the details:


Create a pod named httpd-pod with a container named httpd-container. Use the httpd image with the latest tag (specify as httpd:latest). Set the following resource limits:

Requests: Memory: 15Mi, CPU: 100m

Limits: Memory: 20Mi, CPU: 100m

5. **Execute Rolling Updates in Kubernetes**

An application currently running on the Kubernetes cluster employs the nginx web server. The Nautilus application development team has introduced some recent changes that need deployment. They've crafted an image nginx:1.19 with the latest updates.


Execute a rolling update for this application, integrating the nginx:1.19 image. The deployment is named nginx-deployment.

Ensure all pods are operational post-update.

To perform a **rolling update** for the `nginx-deployment` in your Kubernetes cluster using the updated image `nginx:1.19`, follow these steps:
### ✅ Step 1: Verify the Deployment Exists and Check the Actual Container Name

Run this to check if `nginx-deployment` exists:

kubectl get deployments
# You should see `nginx-deployment` in the output.
kubectl get deployment nginx-deployment -o jsonpath='{.spec.template.spec.containers[*].name}'

# This will return the container name(s). For example, it might return: `nginx-container`

### ✅ Step 2: Perform the Rolling Update

Update the image for the deployment using:

kubectl set image deployment/nginx-deployment nginx=nginx:1.19

* This will trigger a **rolling update**.
* The pod name `nginx` must match the container name in the deployment spec. If unsure, inspect the deployment:

kubectl get deployment nginx-deployment -o yaml

### ✅ Step 3: Monitor the Rollout Status

Watch the status of the rollout:

kubectl rollout status deployment/nginx-deployment

It should output something like:

deployment "nginx-deployment" successfully rolled out

### ✅ Step 4: Verify All Pods Are Running

Check the status of the pods:

kubectl get pods -l app=nginx

### ✅ Step 5: (Optional) Confirm Image Version in Deployment

kubectl get deployment nginx-deployment -o=jsonpath='{.spec.template.spec.containers[*].image}'

You should see: `nginx:1.19`

6. **Revert Deployment to Previous Version in Kubernetes**

Earlier today, the Nautilus DevOps team deployed a new release for an application. However, a customer has reported a bug related to this recent release. Consequently, the team aims to revert to the previous version.


There exists a deployment named nginx-deployment; initiate a rollback to the previous revision.

Ans: 
View Deployment History: kubectl rollout history deployment nginx-deployment
Rollback Command: kubectl rollout undo deployment nginx-deployment
Verify Rollback Status: kubectl rollout status deployment nginx-deployment
verify the current image (to confirm it's no longer using nginx:stable): kubectl get deployment nginx-deployment -o=jsonpath='{.spec.template.spec.containers[*].image}'
Verify Pods running: kubectl get po

7. **Deploy ReplicaSet in Kubernetes Cluster**

The Nautilus DevOps team is gearing up to deploy applications on a Kubernetes cluster for migration purposes. A team member has been tasked with creating a ReplicaSet outlined below:



Create a ReplicaSet using nginx image with latest tag (ensure to specify as nginx:latest) and name it nginx-replicaset.


Apply labels: app as nginx_app, type as front-end.


Name the container nginx-container. Ensure the replica count is 4.

Ans:
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicaset
  labels:
    app: nginx_app
    type: front-end
spec:
  replicas: 4 
  selector:
    matchLabels:
      app: nginx_app
      type: front-end
  template:
    metadata:
      labels:
        app: nginx_app
        type: front-end
    spec:
      containers:
      - name: nginx-container
        image: nginx:latest
        ports:
        - containerPort: 80

8. **Schedule Cronjobs in Kubernetes**
The Nautilus DevOps team is setting up recurring tasks on different schedules. Currently, they're developing scripts to be executed periodically. To kickstart the process, they're creating cron jobs in the Kubernetes cluster with placeholder commands. Follow the instructions below:

Create a cronjob named nautilus.

Set Its schedule to something like */6 * * * *. You can set any schedule for now.


Name the container cron-nautilus.


Utilize the httpd image with latest tag (specify as httpd:latest).


Execute the dummy command echo Welcome to xfusioncorp!.


Ensure the restart policy is OnFailure.

Ans:
apiVersion: batch/v1
kind: CronJob
metadata:
  name: nautilus
spec:
  schedule: "*/6 * * * *"  # Runs every 6 minutes
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: cron-nautilus
            image: httpd:latest
            command: ["echo", "Welcome to xfusioncorp!"]
          restartPolicy: OnFailure

kubectl apply -f nautilus-cronjob.yaml
Check the CronJob:kubectl get cronjob nautilus


9. **Create Countdown Job in Kubernetes**

The Nautilus DevOps team is crafting jobs in the Kubernetes cluster. While they're developing actual scripts/commands, they're currently setting up templates and testing jobs with dummy commands. Please create a job template as per details given below:


Create a job named countdown-devops.

The spec template should be named countdown-devops (under metadata), and the container should be named container-countdown-devops

Utilize image ubuntu with latest tag (ensure to specify as ubuntu:latest), and set the restart policy to Never.

Execute the command sleep 5

Ans:
apiVersion: batch/v1
kind: Job
metadata:
  name: countdown-devops
spec:
  template:
    metadata:
      name: countdown-devops
    spec:
      containers:
      - name: container-countdown-devops
        image: ubuntu:latest
        command: ["sleep", "5"]
      restartPolicy: Never

10. **Set Up Time Check Pod in Kubernetes**
The Nautilus DevOps team needs a time check pod created in a specific Kubernetes namespace for logging purposes. Initially, it's for testing, but it may be integrated into an existing cluster later. Here's what's required:


Create a pod called time-check in the datacenter namespace. The pod should contain a container named time-check, utilizing the busybox image with the latest tag (specify as busybox:latest).

Create a config map named time-config with the data TIME_FREQ=2 in the same namespace.

Configure the time-check container to execute the command: while true; do date; sleep $TIME_FREQ;done. Ensure the result is written /opt/security/time/time-check.log. Also, add an environmental variable TIME_FREQ in the container, fetching its value from the config map TIME_FREQ key.

Create a volume log-volume and mount it at /opt/security/time within the container.

Ans:
To fulfill the requirements, you’ll need to create:

A namespace called datacenter

A ConfigMap called time-config with the TIME_FREQ=2

A Pod named time-check in the same namespace with:

A container named time-check using busybox:latest

Environment variable TIME_FREQ from the ConfigMap

A command to log the time every $TIME_FREQ seconds

A volume mounted at /opt/security/time

The log output directed to /opt/security/time/time-check.log

apiVersion: v1
kind: Namespace
metadata:
  name: datacenter

apiVersion: v1
kind: ConfigMap
metadata:
  name: time-config
  namespace: datacenter
data:
  TIME_FREQ: "2"

apiVersion: v1
kind: Pod
metadata:
  name: time-check
  namespace: datacenter
spec:
  containers:
  - name: time-check
    image: busybox:latest
    command: ["/bin/sh", "-c"]
    args:
      - while true; do date >> /opt/security/time/time-check.log; sleep $TIME_FREQ; done
    env:
    - name: TIME_FREQ
      valueFrom:
        configMapKeyRef:
          name: time-config
          key: TIME_FREQ
    volumeMounts:
    - name: log-volume
      mountPath: /opt/security/time
  volumes:
  - name: log-volume
    emptyDir: {}


11. **Resolve Pod Deployment Issue**
A junior DevOps team member encountered difficulties deploying a stack on the Kubernetes cluster. The pod fails to start, presenting errors. Let's troubleshoot and rectify the issue promptly.


There is a pod named webserver, and the container within it is named nginx-container, its utilizing the nginx:latest image.

Additionally, there's a sidecar container named sidecar-container using the ubuntu:latest image.

Identify and address the issue to ensure the pod is in the running state and the application is accessible.
Ans:
kubectl get pods webserver -o wide
kubectl logs webserver -c nginx-container
kubectl describe pod webserver
kubectl edit pod webserver


12. **Update Deployment and Service in Kubernetes**

An application deployed on the Kubernetes cluster requires an update with new features developed by the Nautilus application development team. The existing setup includes a deployment named nginx-deployment and a service named nginx-service. Below are the necessary changes to be implemented without deleting the deployment and service:


1.) Modify the service nodeport from 30008 to 32165

2.) Change the replicas count from 1 to 5

3.) Update the image from nginx:1.18 to nginx:latest

Ans:
kubectl edit service nginx-service
kubectl edit deployment nginx-deployment
kubectl get deployment nginx-deployment
kubectl get svc nginx-service


13. **Deploy Highly Available Pods with ReplicationController**
The Nautilus DevOps team is establishing a ReplicationController to deploy multiple pods for hosting applications that require a highly available infrastructure. Follow the specifications below to create the ReplicationController:


Create a ReplicationController using the httpd image with latest tag, and name it httpd-replicationcontroller.

Assign labels app as httpd_app, and type as front-end. Ensure the container is named httpd-container and set the replica count to 3.

All pods should be running state post-deployment.

ans:
apiVersion: v1
kind: ReplicationController
metadata:
  name: httpd-replicationcontroller
spec:
  replicas: 3
  selector:
    app: httpd_app
    type: front-end
  template:
    metadata:
      labels:
        app: httpd_app
        type: front-end
    spec:
      containers:
        - name: httpd-container
          image: httpd:latest

14. **Resolve VolumeMounts Issue in Kubernetes**

We encountered an issue with our Nginx and PHP-FPM setup on the Kubernetes cluster this morning, which halted its functionality. Investigate and rectify the issue:

The pod name is nginx-phpfpm and configmap name is nginx-config. Identify and fix the problem.

Once resolved, copy /home/thor/index.php file from the jump host to the nginx-container within the nginx document root. After this, you should be able to access the website using Website button on the top bar.

--

Q. 1-Task:
We've successfully deployed a pod named httpd-app-t1q3. We require some data to be copied from the jump_host to this specific Pod. Further details are outlined below:

Copy file /home/thor/welcome.txt to pod httpd-app-t1q3 Pod under location /opt.

Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

Q. 2 Task:
An engineer was tasked with creating a Kubernetes Pod template for a specific application deployment within the Kubernetes cluster. To ensure easy modification in the future.

The directive is to generate a template file named official-t1q2.yml within the /usr/official-t1q2/ directory on the jump_host. This template will facilitate the creation of a pod named official-nginx-t1q2, utilizing the nginx image.

The objective is to establish a template that streamlines the process of generating the designated pod within the Kubernetes cluster.

Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

Q. 3 Task:
Recently, during an audit, it was identified that there are some deployments on Kubernetes cluster which are no longer needed. Therefore, the team wants to delete some obslete deployments. Find below more details about the same.

There is a deployment named web-app-t2q4, delete the same.

Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

Q. 4 Task:
There is an application deployed on Kubernetes cluster. Recently, the Nautilus application development team developed a new version of the application that needs to be deployed now. As per new updates some new changes need to be made in this existing setup. So update the deployment and service as per details mentioned below:

We already have a deployment named nginx-deployment1-t2q3 and service named nginx-service1-t2q3. Some changes need to be made in this deployment and service, make sure not to delete the deployment and service.

Change the image from nginx:mainline-alpine3.18-slim to nginx:mainline-alpine-slim

Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

Q. 5 Task:
Recently, the Nautilus DevOps team identified performance issues affecting certain applications on the Kubernetes cluster. Analysis revealed resource constraints, with some applications exhausting memory and CPU, while others were overconsuming resources beyond their requirements. To address this, the team plans to implement resource limits. Here are the details:

Create a pod named httpd-pod-t3q6 and a container under it named as httpd-container-t3q6, use httpd image with latest tag only (remember to mention the tag i.e httpd:latest), further set the following limits:

Requests:

Memory: 15Mi
CPU: 100m
Limits:

Memory: 20Mi
CPU: 100m
Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

Q. 6 Task:
The Nautilus DevOps team is actively creating jobs within the Kubernetes cluster. While they are in the process of finalizing actual scripts/commands, they are presently structuring templates and testing the jobs using placeholder commands. Below are the specifications for creating a job template:

Create a job named countdown-nautilus-t3q2.

The spec template should be named as countdown-nautilus-t3q2 (under metadata), and the container should be named as container-countdown-nautilus-t3q2.

Use image debian with latest tag only and remember to mention tag i.e debian:latest, and restart policy should be Never.

Use command sleep 5.

Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

Q. 7 Task:
One of our junior DevOps team members encountered an issue while deploying a stack on the Kubernetes cluster. The webserver-t4q1 pod, with the nginx-container and a sidecar container named sidecar-container, is failing to start and remains in an error state.

Your task is to investigate and rectify the problem to ensure the successful running state of the webserver-t4q1 pod. The nginx-container uses the nginx:latest image, while the sidecar-container utilizes the ubuntu:latest image. Ensure the webserver-t4q1 pod is running as expected and the application is accessible.

Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

Q. 8 Task:
We encountered complications while deploying an app on the Kubernetes cluster, resulting in its improper functionality. Your task is to investigate and restore its proper operation.

App deployment name is purple-app-deployment-t4q5. The service associated with the app is currently non-operational on nodePort 32232.

Your objective is to troubleshoot the service issue associated with the purple-app-deployment-t4q5. Ensure that the app becomes accessible and functional on nodePort 32232.

Please proceed with the necessary diagnostics and adjustments to resolve the service issue and access the app using Purple App button on the top.

Note: The kubectl on jump_host has been configured to work with the kubernetes cluster.

Q. 9 Task:
One of the services named service-t5q6 needs some updates, as during deployment some required labels were missing from this service. Make changes to this service as per details mentioned below:

Update service-t5q6 service to add a label component: front-end-t5q6.

Q. 10: Task
During an investigating it was found that one of the applications on the Kubernetes cluster is having some issues, the team discovered that the service was configured with an incorrect target port. We need to update the service as follows:

Update service-t5q4 service to use target port 80.

Here are the step-by-step commands and explanations to complete **each of the 10 Kubernetes tasks** using the `kubectl` CLI on the `jump_host`, as requested.



## ✅ **Q1: Copy file to Pod**

### **Task:** Copy `/home/thor/welcome.txt` to pod `httpd-app-t1q3` under `/opt`

kubectl cp /home/thor/welcome.txt httpd-app-t1q3:/opt/

## ✅ **Q2: Create a Pod template YAML**

### **Task:** Create `official-t1q2.yml` in `/usr/official-t1q2/` for a pod `official-nginx-t1q2` using `nginx` image

mkdir -p /usr/official-t1q2/
cat <<EOF > /usr/official-t1q2/official-t1q2.yml
apiVersion: v1
kind: Pod
metadata:
  name: official-nginx-t1q2
spec:
  containers:
  - name: nginx
    image: nginx
EOF

## ✅ **Q3: Delete a deployment**

### **Task:** Delete deployment named `web-app-t2q4`

kubectl delete deployment web-app-t2q4


## ✅ **Q4: Update Deployment Image**

### **Task:** Update `nginx-deployment1-t2q3` deployment image from `nginx:mainline-alpine3.18-slim` to `nginx:mainline-alpine-slim`


kubectl set image deployment/nginx-deployment1-t2q3 *nginx*=nginx:mainline-alpine-slim


> Replace `*nginx*` with the actual container name if it is not `nginx`.



## ✅ **Q5: Create pod with resource limits**

### **Task:** Create pod `httpd-pod-t3q6` with container using `httpd:latest` and the specified CPU/memory limits


cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: httpd-pod-t3q6
spec:
  containers:
  - name: httpd-container-t3q6
    image: httpd:latest
    resources:
      requests:
        memory: "15Mi"
        cpu: "100m"
      limits:
        memory: "20Mi"
        cpu: "100m"
EOF




## ✅ **Q6: Create a Job**

### **Task:** Create a job `countdown-nautilus-t3q2` with `debian:latest`, running `sleep 5`, restart policy `Never`


cat <<EOF | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: countdown-nautilus-t3q2
spec:
  template:
    metadata:
      name: countdown-nautilus-t3q2
    spec:
      containers:
      - name: container-countdown-nautilus-t3q2
        image: debian:latest
        command: ["sleep", "5"]
      restartPolicy: Never
EOF




## ✅ **Q7: Fix `webserver-t4q1` pod**

### **Task:** Investigate and fix pod `webserver-t4q1` with `nginx-container` and `sidecar-container` (ubuntu)


kubectl describe pod webserver-t4q1
kubectl logs webserver-t4q1 -c sidecar-container
kubectl logs webserver-t4q1 -c nginx-container


> Common issues could be missing commands for `ubuntu` container.

### If sidecar container has no command, update pod YAML like:

yaml
...
  containers:
  - name: sidecar-container
    image: ubuntu:latest
    command: ["sleep", "3600"]


**Fix command (if Pod is managed by a Deployment, edit the deployment):**


kubectl edit pod webserver-t4q1


Update `sidecar-container` to include a valid `command`, e.g.:


command: ["sleep", "3600"]


Then delete the pod to restart it (if not a deployment):


kubectl delete pod webserver-t4q1




## ✅ **Q8: Fix `purple-app-deployment-t4q5` service**

### **Task:** Service on `nodePort 32232` not working.

1. **Check service:**


kubectl get svc
kubectl describe svc <service-name>


2. **Verify ports:**


kubectl edit svc <service-name>


* Ensure correct `targetPort`
* Ensure `type: NodePort`
* Ensure `nodePort: 32232`

3. **Verify Pods backing the deployment are running:**


kubectl get pods -l app=purple-app-deployment-t4q5


4. **Check if selector matches the deployment's labels.**

Fix mismatch, then:


kubectl rollout restart deployment purple-app-deployment-t4q5




## ✅ **Q9: Add a label to a service**

### **Task:** Add label `component=front-end-t5q6` to service `service-t5q6`


kubectl label svc service-t5q6 component=front-end-t5q6 --overwrite




## ✅ **Q10: Update service target port**

### **Task:** Update `service-t5q4` targetPort to 80


kubectl edit svc service-t5q4


* Find `targetPort` field and update:

yaml
ports:
- port: 80
  targetPort: 80


> Save and exit editor.

**Level 2:**
# Day 1: Kubernetes Shared Volumes
We are working on an application that will be deployed on multiple containers within a pod on Kubernetes cluster. There is a requirement to share a volume among the containers to save some temporary data. The Nautilus DevOps team is developing a similar template to replicate the scenario. Below you can find more details about it.

Create a pod named volume-share-xfusion.

For the first container, use image ubuntu with latest tag only and remember to mention the tag i.e ubuntu:latest, container should be named as volume-container-xfusion-1, and run a sleep command for it so that it remains in running state. Volume volume-share should be mounted at path /tmp/blog.

For the second container, use image ubuntu with the latest tag only and remember to mention the tag i.e ubuntu:latest, container should be named as volume-container-xfusion-2, and again run a sleep command for it so that it remains in running state. Volume volume-share should be mounted at path /tmp/apps.

Volume name should be volume-share of type emptyDir.

After creating the pod, exec into the first container i.e volume-container-xfusion-1, and just for testing create a file blog.txt with any content under the mounted path of first container i.e /tmp/blog.

The file blog.txt should be present under the mounted path /tmp/apps on the second container volume-container-xfusion-2 as well, since they are using a shared volume.

# Day2: Kubernetes Sidecar Containers
We have a web server container running the nginx image. The access and error logs generated by the web server are not critical enough to be placed on a persistent volume. However, Nautilus developers need access to the last 24 hours of logs so that they can trace issues and bugs. Therefore, we need to ship the access and error logs for the web server to a log-aggregation service. Following the separation of concerns principle, we implement the Sidecar pattern by deploying a second container that ships the error and access logs from nginx. Nginx does one thing, and it does it well—serving web pages. The second container also specializes in its task—shipping logs. Since containers are running on the same Pod, we can use a shared emptyDir volume to read and write logs.

Create a pod named webserver.

Create an emptyDir volume shared-logs.

Create two containers from nginx and ubuntu images with latest tag only and remember to mention tag i.e nginx:latest, nginx container name should be nginx-container and ubuntu container name should be sidecar-container on webserver pod.

Add command on sidecar-container "sh","-c","while true; do cat /var/log/nginx/access.log /var/log/nginx/error.log; sleep 30; done"

Mount the volume shared-logs on both containers at location /var/log/nginx, all containers should be up and running.

Ans:
apiVersion: v1
kind: Pod
metadata:
  name: webserver
spec:
  volumes:
    - name: shared-logs
      emptyDir: {}
  containers:
    - name: nginx-container
      image: nginx:latest
      volumeMounts:
        - name: shared-logs
          mountPath: /var/log/nginx
    - name: sidecar-container
      image: ubuntu:latest
      command: ["sh", "-c", "while true; do cat /var/log/nginx/access.log /var/log/nginx/error.log; sleep 30; done"]
      volumeMounts:
        - name: shared-logs
          mountPath: /var/log/nginx
# Day3: Deploy Nginx Web Server on Kubernetes Cluster
Some of the Nautilus team developers are developing a static website and they want to deploy it on Kubernetes cluster. They want it to be highly available and scalable. Therefore, based on the requirements, the DevOps team has decided to create a deployment for it with multiple replicas. Below you can find more details about it:

Create a deployment using nginx image with latest tag only and remember to mention the tag i.e nginx:latest. Name it as nginx-deployment. The container should be named as nginx-container, also make sure replica counts are 3.

Create a NodePort type service named nginx-service. The nodePort should be 30011.

Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.
Ans:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-deployment
  template:
    metadata:
      labels:
        app: nginx-deployment
    spec:
      containers:
      - name: nginx-container
        image: nginx:latest
        ports:
        - containerPort: 80

apiVersion: v1
kind: Service 
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx-deployment
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      nodePort: 30011
  type: NodePort

# Day 4: Print Environment Variables
The Nautilus DevOps team is working on to setup some pre-requisites for an application that will send the greetings to different users. There is a sample deployment, that needs to be tested. Below is a scenario which needs to be configured on Kubernetes cluster. Please find below more details about it.

Create a pod named print-envars-greeting.

Configure spec as, the container name should be print-env-container and use bash image.

Create three environment variables:

a. GREETING and its value should be Welcome to

b. COMPANY and its value should be xFusionCorp

c. GROUP and its value should be Industries

Use command ["/bin/sh", "-c", 'echo "$(GREETING) $(COMPANY) $(GROUP)"'] (please use this exact command), also set its restartPolicy policy to Never to avoid crash loop back.

You can check the output using kubectl logs -f print-envars-greeting command.

Ans:
Here's the Kubernetes manifest YAML file to create the pod as described:

apiVersion: v1
kind: Pod
metadata:
  name: print-envars-greeting
spec:
  containers:
  - name: print-env-container
    image: bash
    env:
    - name: GREETING
      value: "Welcome to"
    - name: COMPANY
      value: "xFusionCorp"
    - name: GROUP
      value: "Industries"
    command: ["/bin/sh", "-c", 'echo "$(GREETING) $(COMPANY) $(GROUP)"']
  restartPolicy: Never

### Steps to apply and verify:
1. **Save the file** as `print-envars-greeting.yaml`.
2. **Apply it** to your cluster:
   bash
   kubectl apply -f print-envars-greeting.yaml
   
3. **Check the output**:
   bash
   kubectl logs -f print-envars-greeting

You should see:

Welcome to xFusionCorp Industries

# Day5: Rolling Updates And Rolling Back Deployments in Kubernetes

Create a namespace nautilus.
Deployment name should be: `httpd-deploy`**
- Deploys 2 replicas of the `httpd:2.4.28` container.
- Uses **RollingUpdate** strategy:
  - `maxUnavailable: 1`: At most one pod can be unavailable during the update.
  - `maxSurge: 1`: At most one extra pod can be created during the update.
- Labels: `app: httpd-deploy` used for pod selection.

Service name should be  `httpd-service`**
- Type: `NodePort` — exposes the app externally on port `30011`.
- Namespace: `nautilus` — make sure this namespace exists.
- Selects pods with label `app: httpd-deploy`.

Ans:
### 🧪 Steps to Deploy

1. **Create Namespace :**
 
   kubectl create namespace nautilus
 

2. **Create the Configuration:**
 apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpd-deploy
  labels:
    app: httpd-deploy
spec:
  replicas: 2
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  selector:
    matchLabels:
      app: httpd-deploy
  template:
    metadata:
      labels:
        app: httpd-deploy
    spec:
      containers:
      - name: httpd
        image: httpd:2.4.28
        ports:
        - containerPort: 80

apiVersion: v1
kind: Service 
metadata:
  name: httpd-service
  namespace: nautilus
spec:
  selector:
    app: httpd-deploy
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      nodePort: 30011
  type: NodePort

kubectl apply -f your-config.yaml
 
3. **Verify Deployment:**
 
   kubectl get pods -n nautilus
   kubectl rollout status deployment/httpd-deploy -n nautilus
 
4. **Check Service Exposure:**
 
  kubectl get svc httpd-service -n nautilus
 
5. **Access the App:**
   - Use any node’s IP and port `30011`:
   
     http://<node-ip>:30011
   
### 🔁 Rolling Update & Rollback Commands

- **Update Image:**

  kubectl set image deployment/httpd-deploy httpd=httpd:2.4.29 -n nautilus

- **Rollback:**
  kubectl rollout undo deployment/httpd-deploy -n nautilus

- **View History:**
  kubectl rollout history deployment/httpd-deploy -n nautilus

# Day 6: Deploy Jenkins on Kubernetes
The Nautilus DevOps team is planning to set up a Jenkins CI server to create/manage some deployment pipelines for some of the projects. They want to set up the Jenkins server on Kubernetes cluster. Below you can find more details about the task:

1) Create a namespace jenkins

2) Create a Service for jenkins deployment. Service name should be jenkins-service under jenkins namespace, type should be NodePort, nodePort should be 30008

3) Create a Jenkins Deployment under jenkins namespace, It should be name as jenkins-deployment , labels app should be jenkins , container name should be jenkins-container , use jenkins/jenkins image , containerPort should be 8080 and replicas count should be 1.

Make sure to wait for the pods to be in running state and make sure you are able to access the Jenkins login screen in the browser before hitting the Check button.

Ans:
### ✅ **Step 1: Create a Namespace `jenkins`**

kubectl create namespace jenkins

### ✅ **Step 2: Create a NodePort Service for Jenkins and Jenkins Deployment***

Create a YAML file called `jenkins.yaml` with the following content:

apiVersion: v1
kind: Service
metadata:
  name: jenkins-service
  namespace: jenkins
spec:
  type: NodePort
  selector:
    app: jenkins
  ports:
    - port: 8080
      targetPort: 8080
      nodePort: 30008

apiVersion: apps/v1
kind: Deployment
metadata:
  name: jenkins-deployment
  namespace: jenkins
spec:
  replicas: 1
  selector:
    matchLabels:
      app: jenkins
  template:
    metadata:
      labels:
        app: jenkins
    spec:
      containers:
        - name: jenkins-container
          image: jenkins/jenkins
          ports:
            - containerPort: 8080

kubectl apply -f jenkins.yaml

### ✅ **Step 3: Wait for Jenkins Pod to be Running**

Use this command to watch the pod status:

kubectl get pods -n jenkins -w

Wait until the pod status changes to `Running`.

### ✅ **Step 4: Access Jenkins in Browser**

If you're running Minikube or a local cluster, get the node IP:

Then open the following URL in your browser:

http://<Node-IP>:30008

You should see the **Jenkins login screen**.

# Day 7: Deploy Grafana on Kubernetes Cluster

The Nautilus DevOps teams is planning to set up a Grafana tool to collect and analyze analytics from some applications. They are planning to deploy it on Kubernetes cluster. Below you can find more details.

1.) Create a deployment named grafana-deployment-devops using any grafana image for Grafana app. Set other parameters as per your choice.

2.) Create NodePort type service with nodePort 32000 to expose the app.

You need not to make any configuration changes inside the Grafana app once deployed, just make sure you are able to access the Grafana login page

Ans:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: grafana-deployment-devops
  labels:
    app: grafana
spec:
  replicas: 1
  selector:
    matchLabels:
      app: grafana
  template:
    metadata:
      labels:
        app: grafana
    spec:
      containers:
      - name: grafana
        image: grafana/grafana:latest
        ports:
        - containerPort: 3000


apiVersion: v1
kind: Service
metadata:
  name: grafana-service
spec:
  type: NodePort
  selector:
    app: grafana
  ports:
  - protocol: TCP
    port: 3000
    targetPort: 3000
    nodePort: 32000
# Day 8: Deploy Tomcat App on Kubernetes
A new java-based application is ready to be deployed on a Kubernetes cluster. The development team had a meeting with the DevOps team to share the requirements and application scope. The team is ready to setup an application stack for it under their existing cluster. Below you can find the details for this:


Create a namespace named tomcat-namespace-datacenter.

Create a deployment for tomcat app which should be named as tomcat-deployment-datacenter under the same namespace you created. Replica count should be 1, the container should be named as tomcat-container-datacenter, its image should be gcr.io/kodekloud/centos-ssh-enabled:tomcat and its container port should be 8080.

Create a service for tomcat app which should be named as tomcat-service-datacenter under the same namespace you created. Service type should be NodePort and nodePort should be 32227.

Before clicking on Check button please make sure the application is up and running.

You can use any labels as per your choice.

Ans:
apiVersion: v1
kind: Service
metadata:
  name: tomcat-service-datacenter
  namespace: tomcat-namespace-datacenter
  labels:
    app: tomcat
spec:
  type: NodePort
  selector:
    app: tomcat
  ports:
  - protocol: TCP
    port: 8080
    targetPort: 8080
    nodePort: 32227


apiVersion: apps/v1
kind: Deployment
metadata:
  name: tomcat-deployment-datacenter
  namespace: tomcat-namespace-datacenter
  labels:
    app: tomcat
spec:
  replicas: 1
  selector:
    matchLabels:
      app: tomcat
  template:
    metadata:
      labels:
        app: tomcat
    spec:
      containers:
      - name: tomcat-container-datacenter
        image: gcr.io/kodekloud/centos-ssh-enabled:tomcat
        ports:
        - containerPort: 8080
# Day 9: Deploy Node App on Kubernetes
The Nautilus development team has completed development of one of the node applications, which they are planning to deploy on a Kubernetes cluster. They recently had a meeting with the DevOps team to share their requirements. Based on that, the DevOps team has listed out the exact requirements to deploy the app. Find below more details:


Create a deployment using gcr.io/kodekloud/centos-ssh-enabled:node image, replica count must be 2.

Create a service to expose this app, the service type must be NodePort, targetPort must be 8080 and nodePort should be 30012.

Make sure all the pods are in Running state after the deployment.

You can check the application by clicking on NodeApp button on top bar.

You can use any labels as per your choice.
Ans:
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-app-deployment
  labels:
    app: node-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: node-app
  template:
    metadata:
      labels:
        app: node-app
    spec:
      containers:
        - name: node-app
          image: gcr.io/kodekloud/centos-ssh-enabled:node
          ports:
            - containerPort: 8080

apiVersion: v1
kind: Service
metadata:
  name: node-app-service
spec:
  selector:
    app: node-app
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
      nodePort: 30012
  type: NodePort
# Day 10: Troubleshoot Deployment issues in Kubernetes
Last week, the Nautilus DevOps team deployed a redis app on Kubernetes cluster, which was working fine so far. This morning one of the team members was making some changes in this existing setup, but he made some mistakes and the app went down. We need to fix this as soon as possible. Please take a look.

The deployment name is redis-deployment. The pods are not in running state right now, so please look into the issue and fix the same.
Ans:
1  kubectl get deploy
2  kubectl get po
3  kubectl logs redis-deployment-6fd9d5fcb-sklsz 
4  kubectl describe po redis-deployment-6fd9d5fcb-sklsz 
5  kubectl edit deploy redis-deployment  
 Check is there typo on image or volume attachemnet or configmap or secret resolve that
Thanks for sharing part of the deployment YAML snippet! I can see the `volumeMounts` section where the `config` volume is mounted at `/redis-master`. This corresponds to the volume named `config`, which tries to use a ConfigMap (likely the `redis-cofig` typo you mentioned earlier).



### Here’s what you should do:

Look for the **volumes** section (usually under `spec.template.spec.volumes`) in your deployment YAML. It should look something like:

yaml
volumes:
  - name: config
    configMap:
      name: redis-cofig   # <-- This is the typo to fix


Change it to:

yaml
volumes:
  - name: config
    configMap:
      name: redis-config   # <-- Corrected ConfigMap name




### Full example snippet:

yaml
spec:
  containers:
  - name: redis-container
    image: redis:latest
    imagePullPolicy: IfNotPresent
    ports:
    - containerPort: 6379
      protocol: TCP
    resources:
      requests:
        cpu: 300m
    volumeMounts:
    - mountPath: /redis-master-data
      name: data
    - mountPath: /redis-master
      name: config
  volumes:
  - name: config
    configMap:
      name: redis-config
  - name: data
    emptyDir: {}




### Next steps:

1. Fix the typo in the deployment by running:

kubectl edit deployment redis-deployment

2. Save after correcting the ConfigMap name under volumes.

3. Make sure the ConfigMap `redis-config` exists:

kubectl get configmap redis-config

If it does not exist, create it. For example:

kubectl create configmap redis-config --from-literal=redis.conf="maxmemory 2mb"

(or use your actual redis config)

4. Then rollout restart the deployment:

kubectl rollout restart deployment redis-deployment

5. Check pods:

kubectl get pods -l app=redis-deployment

# Day 11: Fix issue with LAMP Environment in Kubernetes
One of the DevOps team member was trying to install a WordPress website on a LAMP stack which is essentially deployed on Kubernetes cluster. It was working well and we could see the installation page a few hours ago. However something is messed up with the stack now due to a website went down. Please look into the issue and fix it:

FYI, deployment name is lamp-wp and its using a service named lamp-service. The Apache is using http default port and nodeport is 30008. From the application logs it has been identified that application is facing some issues while connecting to the database in addition to other issues. Additionally, there are some environment variables associated with the pods like MYSQL_ROOT_PASSWORD, MYSQL_DATABASE,  MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST.

Also do not try to delete/modify any other existing components like deployment name, service name, types, labels etc.

Ans:
    1 kubectl get deployment lamp-wp -o yaml > lamp-wp-deployment.yaml
    2  kubectl get svc mysql-service -o yaml > mysql-svc.yaml
    3  kubectl get svc lamp-service -o yaml > lamp-svc.yaml
    4  kubectl get cm
    5  kubectl get secret
    6  kubectl get cm php-config -o yaml > cm.yaml
    7  kubectl get secret mysql-db-url -o yaml > db-url.yaml
    8  kubectl get secret mysql-host -o yaml > host.yaml
    9  kubectl get secret mysql-root-pass -o yaml > root.yaml
   10  kubectl get secret mysql-user-pass -o yaml > user.yaml
   11  cat cm.yaml 
   12  cat db-url.yaml 
   13  cat host.yaml 
   14  cat lamp-svc.yaml 
   15  cat lamp-wp-deployment.yaml 
   16  cat root.yaml 
   17  cat user.yaml 
   18  cat mysql-svc.yaml 
   19  kubectl get svc -o wide
   20  kubectl patch svc lamp-service -p '{"spec":{"ports":[{"port":8080,"targetPort":80,"nodePort":30008}]}}'
   21  kubectl edit svc lamp-service 
   22  kubectl get po
   23  kubectl exec -it lamp-wp-56c7c454fc-s4gb6 -- /bin/bash
   24  kubectl logs -f deployment/lamp-wp
   25  kubectl exec -it lamp-wp-56c7c454fc-s4gb6 -c httpd-php-container -- printenv | grep MYSQL

**Level 3**
# Day 1 Deploy Apache Web Server on Kubernetes CLuster
There is an application that needs to be deployed on Kubernetes cluster under Apache web server. The Nautilus application development team has asked the DevOps team to deploy it. We need to develop a template as per requirements mentioned below:


1.Create a namespace named as httpd-namespace-xfusion.
2.Create a deployment named as httpd-deployment-xfusion under newly created namespace. For the deployment use httpd image with latest tag only and remember to mention the tag i.e httpd:latest, and make sure replica counts are 2
3. Create a service named as httpd-service-xfusion under same namespace to expose the deployment, nodePort should be 30004.
Ans:
# Create a namespace:
kubectl create namespace httpd-namespace-xfusion
# Create a deployment and service Deply.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpd-deployment-xfusion
  namespace: httpd-namespace-xfusion
  labels:
    app: httpd    
spec:
  replicas: 2
  selector:
    matchLabels:
      app: httpd     
  template:
    metadata:
      labels:
        app: httpd        
    spec:
      containers:
      - name: httpd-container
        image: httpd:latest
        ports:
        - containerPort: 80


apiVersion: v1
kind: Service 
metadata:
  name: httpd-service-xfusion
  namespace: httpd-namespace-xfusion
spec:
  selector:
    app: httpd
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      nodePort: 30004
  type: NodePort

# Day 2 Deploy Lamp Stack on Kubernetes Cluster
The Nautilus DevOps team want to deploy a PHP website on Kubernetes cluster. They are going to use Apache as a web server and Mysql for database. The team had already gathered the requirements and now they want to make this website live. Below you can find more details:

1) Create a config map php-config for php.ini with variables_order = "EGPCS" data.

2) Create a deployment named lamp-wp.

3) Create two containers under it. First container must be httpd-php-container using image webdevops/php-apache:alpine-3-php7 and second container must be mysql-container from image mysql:5.6. Mount php-config configmap in httpd container at /opt/docker/etc/php/php.ini location.

4) Create kubernetes generic secrets for mysql related values like myql root password, mysql user, mysql password, mysql host and mysql database. Set any values of your choice.

5) Add some environment variables for both containers:

a) MYSQL_ROOT_PASSWORD, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD and MYSQL_HOST. Take their values from the secrets you created. Please make sure to use env field (do not use envFrom) to define the name-value pair of environment variables.

6) Create a node port type service lamp-service to expose the web application, nodePort must be 30008.

7) Create a service for mysql named mysql-service and its port must be 3306.

8) We already have /tmp/index.php file on jump_host server.

a) Copy this file into httpd container under Apache document root i.e /app and replace the dummy values for mysql related variables with the environment variables you have set for mysql related parameters. Please make sure you do not hard code the mysql related details in this file, you must use the environment variables to fetch those values.

b) You must be able to access this index.php on node port 30008 at the end, please note that you should see Connected successfully message while accessing this page.
Ans:
You're very close to completion — based on your logs and actions, the PHP-Apache container (`httpd-php-container`) is up and serving traffic on NodePort `30008`. ✅

Let’s walk through a few **important checks** and steps to **finalize** everything based on your recent output and command (`kubectl edit secret mysql-secret`).



## ✅ Your Current Status

* ✔️ Apache and PHP are **running fine**.
* ✔️ The service is available externally at port **30008**.
* ✔️ HTTP requests are returning **HTTP 200**, which means Apache is serving **some content**.
* ✔️ You're editing the **`mysql-secret`**, which means you're likely fine-tuning the database credentials.



## 🧪 What You Need to Check/Do Next

### 1. ✅ **Ensure `index.php` is in the right location (`/app`)**

On your **jump host**, copy the updated `index.php` into the correct container:


kubectl cp /tmp/index.php <pod-name>:/app/index.php -c httpd-php-container


Get the pod name:


kubectl get pods


Example:


kubectl cp /tmp/index.php lamp-wp-7946b4684c-h8t8c:/app/index.php -c httpd-php-container




### 2. ✅ **Ensure `index.php` uses environment variables**

Your file should **NOT** hardcode MySQL values. It should use `getenv()`:

php
<?php
$host = getenv('MYSQL_HOST');
$db   = getenv('MYSQL_DATABASE');
$user = getenv('MYSQL_USER');
$pass = getenv('MYSQL_PASSWORD');

$conn = mysqli_connect($host, $user, $pass, $db);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
?>


You can verify it was copied correctly:


kubectl exec -it <pod> -c httpd-php-container -- cat /app/index.php




### 3. ✅ **Ensure MySQL is initialized and ready**

Check logs for the **`mysql-container`**:


kubectl logs lamp-wp-7946b4684c-h8t8c -c mysql-container


You're looking for messages like:


ready for connections


Also, make sure the environment variables match your secret values. If not, you can update the secret:


kubectl edit secret mysql-secret


Update any value (base64 encoded). For example, to set `MYSQL_DATABASE` to `wpdb`, encode it:


echo -n "wpdb" | base64


Paste that into the secret YAML under the correct key.



### 4. ✅ **Test the Application**

Now open in browser:


http://<node-ip>:30008


Or in lab:


https://ilgcehjizfxiofcg.labs.kodekloud.com:30008


Expected output:


Connected successfully


If you still see only Apache default page or error:

* File may not be copied
* MySQL not ready
* Apache doc root may not be `/app` (verify via DockerHub docs of the image)


# Day 3 Init Containers in Kubernetes
There are some applications that need to be deployed on Kubernetes cluster and these apps have some pre-requisites where some configurations need to be changed before deploying the app container. Some of these changes cannot be made inside the images so the DevOps team has come up with a solution to use init containers to perform these tasks during deployment. Below is a sample scenario that the team is going to test first.

Create a Deployment named as ic-deploy-datacenter.

Configure spec as replicas should be 1, labels app should be ic-datacenter, template's metadata lables app should be the same ic-datacenter.

The initContainers should be named as ic-msg-datacenter, use image fedora with latest tag and use command '/bin/bash', '-c' and 'echo Init Done - Welcome to xFusionCorp Industries > /ic/beta'. The volume mount should be named as ic-volume-datacenter and mount path should be /ic.

Main container should be named as ic-main-datacenter, use image fedora with latest tag and use command '/bin/bash', '-c' and 'while true; do cat /ic/beta; sleep 5; done'. The volume mount should be named as ic-volume-datacenter and mount path should be /ic.

Volume to be named as ic-volume-datacenter and it should be an emptyDir type
Ans:
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ic-deploy-datacenter
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ic-datacenter
  template:
    metadata:
      labels:
        app: ic-datacenter
    spec:
      volumes:
        - name: ic-volume-datacenter
          emptyDir: {}
      initContainers:
        - name: ic-msg-datacenter
          image: fedora:latest
          command: ["/bin/bash", "-c", "echo Init Done - Welcome to xFusionCorp Industries > /ic/beta"]
          volumeMounts:
            - name: ic-volume-datacenter
              mountPath: /ic
      containers:
        - name: ic-main-datacenter
          image: fedora:latest
          command: ["/bin/bash", "-c", "while true; do cat /ic/beta; sleep 5; done"]
          volumeMounts:
            - name: ic-volume-datacenter
              mountPath: /ic

# Day 4 Persistent Volumes in Kubernetes
The Nautilus DevOps team is working on a Kubernetes template to deploy a web application on the cluster. There are some requirements to create/use persistent volumes to store the application code, and the template needs to be designed accordingly. Please find more details below:


Create a PersistentVolume named as pv-devops. Configure the spec as storage class should be manual, set capacity to 3Gi, set access mode to ReadWriteOnce, volume type should be hostPath and set path to /mnt/devops (this directory is already created, you might not be able to access it directly, so you need not to worry about it).

Create a PersistentVolumeClaim named as pvc-devops. Configure the spec as storage class should be manual, request 1Gi of the storage, set access mode to ReadWriteOnce.

Create a pod named as pod-devops, mount the persistent volume you created with claim name pvc-devops at document root of the web server, the container within the pod should be named as container-devops using image nginx with latest tag only (remember to mention the tag i.e nginx:latest).

Create a node port type service named web-devops using node port 30008 to expose the web server running within the pod.
Ans:
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-devops
spec:
  storageClassName: manual
  capacity:
    storage: 3Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /mnt/devops

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-devops
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi

apiVersion: v1
kind: Pod
metadata:
  name: pod-devops
  labels:
    app: devops-web
spec:
  volumes:
    - name: devops-storage
      persistentVolumeClaim:
        claimName: pvc-devops
  initContainers:
    - name: init-html
      image: busybox
      command: ["/bin/sh", "-c"]
      args:
        - |
          echo "<h1>Welcome to Nautilus DevOps!</h1>" > /mnt/index.html
      volumeMounts:
        - name: devops-storage
          mountPath: /mnt
  containers:
    - name: container-devops
      image: nginx:latest
      volumeMounts:
        - name: devops-storage
          mountPath: /usr/share/nginx/html


apiVersion: v1
kind: Service
metadata:
  name: web-devops
spec:
  type: NodePort
  selector:

    app: devops-web
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30008

# Day 5 Manage Secrets in Kubernetes
The Nautilus DevOps team is working to deploy some tools in Kubernetes cluster. Some of the tools are licence based so that licence information needs to be stored securely within Kubernetes cluster. Therefore, the team wants to utilize Kubernetes secrets to store those secrets. Below you can find more details about the requirements:

We already have a secret key file news.txt under /opt location on jump host. Create a generic secret named news, it should contain the password/license-number present in news.txt file.

Also create a pod named secret-xfusion.

Configure pod's spec as container name should be secret-container-xfusion, image should be ubuntu with latest tag (remember to mention the tag with image). Use sleep command for container so that it remains in running state. Consume the created secret and mount it under /opt/apps within the container.

To verify you can exec into the container secret-container-xfusion, to check the secret key under the mounted path /opt/apps. Before hitting the Check button please make sure pod/pods are in running state, also validation can take some time to complete so keep patience.

# Exiting details:
cat /opt/news.txt 
5ecur3

Ans:
Here's a step-by-step guide to complete the task as described. This includes:

* Creating a Kubernetes secret from the file `/opt/news.txt`
* Creating a pod with an Ubuntu container that mounts this secret into a specified path.

### ✅ Step 1: Create the Kubernetes Secret

You already have the file `/opt/news.txt` containing the secret (`5ecur3`). To create the secret named `news`:

kubectl create secret generic news --from-file=/opt/news.txt

> This will create a secret named `news`, and the key will be `news.txt`.

You can verify it with:
kubectl describe secret news



### ✅ Step 2: Create a Pod Spec YAML

Now, create a file named `secret-pod.yaml` with the following content:

yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-xfusion
spec:
  containers:
    - name: secret-container-xfusion
      image: ubuntu:latest
      command: [ "sleep", "3600" ]
      volumeMounts:
        - name: secret-volume
          mountPath: "/opt/apps"
          readOnly: true
  volumes:
    - name: secret-volume
      secret:
        secretName: news


### ✅ Step 3: Deploy the Pod

Apply the YAML:

kubectl apply -f secret-pod.yaml

Wait for the pod to be in **Running** state:

kubectl get pods


### ✅ Step 4: Verify the Secret is Mounted

Exec into the container:

kubectl exec -it secret-xfusion -- bash

Inside the container, check the content:

cat /opt/apps/news.txt

You should see:

5ecur3

# Day 6 Environment Variables in Kubernetes
There are a number of parameters that are used by the applications. We need to define these as environment variables, so that we can use them as needed within different configs. Below is a scenario which needs to be configured on Kubernetes cluster. Please find below more details about the same.

Create a pod named envars.

Container name should be fieldref-container, use image httpd preferable latest tag, use command 'sh', '-c' and args should be

'while true; do
      echo -en '/n';
                                  printenv NODE_NAME POD_NAME;
                                  printenv POD_IP POD_SERVICE_ACCOUNT;
              sleep 10;
         done;'

(Note: please take care of indentations)

Define Four environment variables as mentioned below:
a.) The first env should be named as NODE_NAME, set valueFrom fieldref and fieldPath should be spec.nodeName.

b.) The second env should be named as POD_NAME, set valueFrom fieldref and fieldPath should be metadata.name.

c.) The third env should be named as POD_IP, set valueFrom fieldref and fieldPath should be status.podIP.

d.) The fourth env should be named as POD_SERVICE_ACCOUNT, set valueFrom fieldref and fieldPath shoulbe be spec.serviceAccountName.

Set restart policy to Never.

To check the output, exec into the pod and use printenv command.
Ans:
apiVersion: v1
kind: Pod
metadata:
  name: envars
spec:
  restartPolicy: Never
  containers:
    - name: fieldref-container
      image: httpd:latest
      command: ["sh", "-c"]
      args:
        - |
          while true; do
            echo -en '\n';
            printenv NODE_NAME POD_NAME;
            printenv POD_IP POD_SERVICE_ACCOUNT;
            sleep 10;
          done;
      env:
        - name: NODE_NAME
          valueFrom:
            fieldRef:
              fieldPath: spec.nodeName
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: POD_IP
          valueFrom:
            fieldRef:
              fieldPath: status.podIP
        - name: POD_SERVICE_ACCOUNT
          valueFrom:
            fieldRef:
              fieldPath: spec.serviceAccountName
**Verify** kubectl exec -it envars -- printenv

# Day 7 Kubernetes LEMP Setup
The Nautilus DevOps team want to deploy a static website on Kubernetes cluster. They are going to use Nginx, phpfpm and MySQL for the database. The team had already gathered the requirements and now they want to make this website live. Below you can find more details:

Create some secrets for MySQL.

Create a secret named mysql-root-pass wih key/value pairs as below:

name: password
value: R00t

Create a secret named mysql-user-pass with key/value pairs as below:

name: username
value: kodekloud_rin

name: password
value: GyQkFRVNr3

Create a secret named mysql-db-url with key/value pairs as below:

name: database
value: kodekloud_db4

Create a secret named mysql-host with key/value pairs as below:

name: host
value: mysql-service

Create a config map php-config for php.ini with variables_order = "EGPCS" data.

Create a deployment named lemp-wp.

Create two containers under it. First container must be nginx-php-container using image webdevops/php-nginx:alpine-3-php7 and second container must be mysql-container from image mysql:5.6. Mount php-config configmap in nginx container at /opt/docker/etc/php/php.ini location.

5) Add some environment variables for both containers:

MYSQL_ROOT_PASSWORD, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD and MYSQL_HOST. Take their values from the secrets you created. Please make sure to use env field (do not use envFrom) to define the name-value pair of environment variables.

6) Create a node port type service lemp-service to expose the web application, nodePort must be 30008.

7) Create a service for mysql named mysql-service and its port must be 3306.

We already have a /tmp/index.php file on jump_host server.

Copy this file into the nginx container under document root i.e /app and replace the dummy values for mysql related variables with the environment variables you have set for mysql related parameters. Please make sure you do not hard code the mysql related details in this file, you must use the environment variables to fetch those values.

Once done, you must be able to access this website using Website button on the top bar, please note that you should see Connected successfully message while accessing this page.
Ans:
Here’s a complete guide to help the Nautilus DevOps team deploy the static website on Kubernetes using Nginx, PHP-FPM, and MySQL:

### 🔐 Step 1: Create MySQL Secrets

kubectl create secret generic mysql-root-pass \
  --from-literal=password=R00t

kubectl create secret generic mysql-user-pass \
  --from-literal=username=kodekloud_rin \
  --from-literal=password=GyQkFRVNr3

kubectl create secret generic mysql-db-url \
  --from-literal=database=kodekloud_db4

kubectl create secret generic mysql-host \
  --from-literal=host=mysql-service


### ⚙️ Step 2: Create ConfigMap for PHP
kubectl create configmap php-config \
  --from-literal=variables_order="EGPCS"

### 🚀 Step 3: Create Deployment `lemp-wp`

Here’s the YAML for the deployment:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: lemp-wp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: lemp-wp
  template:
    metadata:
      labels:
        app: lemp-wp
    spec:
      containers:
      - name: nginx-php-container
        image: webdevops/php-nginx:alpine-3-php7
        volumeMounts:
        - name: php-config-volume
          mountPath: /opt/docker/etc/php/php.ini
          subPath: php.ini
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-root-pass
              key: password
        - name: MYSQL_DATABASE
          valueFrom:
            secretKeyRef:
              name: mysql-db-url
              key: database
        - name: MYSQL_USER
          valueFrom:
            secretKeyRef:
              name: mysql-user-pass
              key: username
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-user-pass
              key: password
        - name: MYSQL_HOST
          valueFrom:
            secretKeyRef:
              name: mysql-host
              key: host

      - name: mysql-container
        image: mysql:5.6
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-root-pass
              key: password
        - name: MYSQL_DATABASE
          valueFrom:
            secretKeyRef:
              name: mysql-db-url
              key: database
        - name: MYSQL_USER
          valueFrom:
            secretKeyRef:
              name: mysql-user-pass
              key: username
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-user-pass
              key: password
        - name: MYSQL_HOST
          valueFrom:
            secretKeyRef:
              name: mysql-host
              key: host

      volumes:
      - name: php-config-volume
        configMap:
          name: php-config
          items:
          - key: variables_order
            path: php.ini

### 🌐 Step 4: Create NodePort Service for Web App

apiVersion: v1
kind: Service
metadata:
  name: lemp-service
spec:
  type: NodePort
  selector:
    app: lemp-wp
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30008

### 🛢️ Step 5: Create MySQL Service

apiVersion: v1
kind: Service
metadata:
  name: mysql-service
spec:
  selector:
    app: lemp-wp
  ports:
  - port: 3306
    targetPort: 3306

### 📁 Step 6: Copy `index.php` to Nginx Container

Assuming you're on the jump_host and the pod is running:

# Get the pod name
POD_NAME=$(kubectl get pods -l app=lemp-wp -o jsonpath="{.items[0].metadata.name}")

# Copy index.php into the container
kubectl cp /tmp/index.php $POD_NAME:/app -c nginx-php-container

Make sure `index.php` uses environment variables like:

php
<?php
$host = getenv('MYSQL_HOST');
$db = getenv('MYSQL_DATABASE');
$user = getenv('MYSQL_USER');
$pass = getenv('MYSQL_PASSWORD');

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>

# Day 8 Kubernetes Troubleshooting
One of the Nautilus DevOps team members was working on to update an existing Kubernetes template. Somehow, he made some mistakes in the template and it is failing while applying. We need to fix this as soon as possible, so take a look into it and make sure you are able to apply it without any issues. Also, do not remove any component from the template like pods/deployments/volumes etc.

/home/thor/mysql_deployment.yml is the template that needs to be fixed.
Ans:
# Isuse with ApiVersion and Indentation is fixed:
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mysql-pv
  labels:
    type: local
spec:
  storageClassName: standard
  capacity:
    storage: 250Mi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
  persistentVolumeReclaimPolicy: Retain

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claim
  labels:
    app: mysql-app
spec:
  storageClassName: standard
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 250Mi

apiVersion: v1
kind: Service
metadata:
  name: mysql
  labels:
    app: mysql-app
spec:
  type: NodePort
  ports:
    - port: 3306
      targetPort: 3306
      nodePort: 30011
  selector:
    app: mysql-app
    tier: mysql

apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql-deployment
  labels:
    app: mysql-app
spec:
  selector:
    matchLabels:
      app: mysql-app
      tier: mysql
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: mysql-app
        tier: mysql
    spec:
      containers:
        - name: mysql
          image: mysql:5.6
          env:
            - name: MYSQL_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql-root-pass
                  key: password
            - name: MYSQL_DATABASE
              valueFrom:
                secretKeyRef:
                  name: mysql-db-url
                  key: database
            - name: MYSQL_USER
              valueFrom:
                secretKeyRef:
                  name: mysql-user-pass
                  key: username
            - name: MYSQL_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql-user-pass
                  key: password
          ports:
            - containerPort: 3306
              name: mysql
          volumeMounts:
            - name: mysql-persistent-storage
              mountPath: /var/lib/mysql
      volumes:
        - name: mysql-persistent-storage
          persistentVolumeClaim:
            claimName: mysql-pv-claim

# Day 9 Deploy Iron Gallery App on Kubernetes
There is an iron gallery app that the Nautilus DevOps team was developing. They have recently customized the app and are going to deploy the same on the Kubernetes cluster. Below you can find more details:

Create a namespace iron-namespace-nautilus

Create a deployment iron-gallery-deployment-nautilus for iron gallery under the same namespace you created.

:- Labels run should be iron-gallery.

:- Replicas count should be 1.

:- Selector's matchLabels run should be iron-gallery.

:- Template labels run should be iron-gallery under metadata.

:- The container should be named as iron-gallery-container-nautilus, use kodekloud/irongallery:2.0 image ( use exact image name / tag ).

:- Resources limits for memory should be 100Mi and for CPU should be 50m.

:- First volumeMount name should be config, its mountPath should be /usr/share/nginx/html/data.

:- Second volumeMount name should be images, its mountPath should be /usr/share/nginx/html/uploads.

:- First volume name should be config and give it emptyDir and second volume name should be images, also give it emptyDir.

Create a deployment iron-db-deployment-nautilus for iron db under the same namespace.

:- Labels db should be mariadb.

:- Replicas count should be 1.

:- Selector's matchLabels db should be mariadb.

:- Template labels db should be mariadb under metadata.

:- The container name should be iron-db-container-nautilus, use kodekloud/irondb:2.0 image ( use exact image name / tag ).

:- Define environment, set MYSQL_DATABASE its value should be database_blog, set MYSQL_ROOT_PASSWORD and MYSQL_PASSWORD value should be with some complex passwords for DB connections, and MYSQL_USER value should be any custom user ( except root ).

:- Volume mount name should be db and its mountPath should be /var/lib/mysql. Volume name should be db and give it an emptyDir.

Create a service for iron db which should be named iron-db-service-nautilus under the same namespace. Configure spec as selector's db should be mariadb. Protocol should be TCP, port and targetPort should be 3306 and its type should be ClusterIP.

Create a service for iron gallery which should be named iron-gallery-service-nautilus under the same namespace. Configure spec as selector's run should be iron-gallery. Protocol should be TCP, port and targetPort should be 80, nodePort should be 32678 and its type should be NodePort.


Note:

We don't need to make connection b/w database and front-end now, if the installation page is coming up it should be enough for now.

The kubectl on jump_host has been configured to work with the kubernetes cluster.
Ans:
### ✅ 1. **Namespace**
apiVersion: v1
kind: Namespace
metadata:
  name: iron-namespace-nautilus
### ✅ 2. **iron-gallery Deployment**

apiVersion: apps/v1
kind: Deployment
metadata:
  name: iron-gallery-deployment-nautilus
  namespace: iron-namespace-nautilus
spec:
  replicas: 1
  selector:
    matchLabels:
      run: iron-gallery
  template:
    metadata:
      labels:
        run: iron-gallery
    spec:
      containers:
      - name: iron-gallery-container-nautilus
        image: kodekloud/irongallery:2.0
        resources:
          limits:
            memory: "100Mi"
            cpu: "50m"
        volumeMounts:
        - name: config
          mountPath: /usr/share/nginx/html/data
        - name: images
          mountPath: /usr/share/nginx/html/uploads
      volumes:
      - name: config
        emptyDir: {}
      - name: images
        emptyDir: {}

### ✅ 3. **iron-db Deployment**

apiVersion: apps/v1
kind: Deployment
metadata:
  name: iron-db-deployment-nautilus
  namespace: iron-namespace-nautilus
spec:
  replicas: 1
  selector:
    matchLabels:
      db: mariadb
  template:
    metadata:
      labels:
        db: mariadb
    spec:
      containers:
      - name: iron-db-container-nautilus
        image: kodekloud/irondb:2.0
        env:
            - name: MYSQL_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql-secret
                  key: mysql-root-password
            - name: MYSQL_DATABASE
              valueFrom:
                secretKeyRef:
                  name: mysql-secret
                  key: mysql-database
            - name: MYSQL_USER
              valueFrom:
                secretKeyRef:
                  name: mysql-secret
                  key: mysql-user
            - name: MYSQL_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql-secret
                  key: mysql-password
        volumeMounts:
        - name: db
          mountPath: /var/lib/mysql
      volumes:
      - name: db
        emptyDir: {}
### **Secret**
apiVersion: v1
kind: Secret
metadata:
  name: mysql-secret
type: Opaque
data:
  # Base64-encoded values:
  mysql-root-password: cm9vdHBhc3N3b3Jk   
  mysql-database: d3BiZGI=               
  mysql-user: d3B1c2Vy                   
  mysql-password: c3VwZXJzcXJ0  
### ✅ 4. **iron-db Service**

apiVersion: v1
kind: Service
metadata:
  name: iron-db-service-nautilus
  namespace: iron-namespace-nautilus
spec:
  selector:
    db: mariadb
  ports:
  - protocol: TCP
    port: 3306
    targetPort: 3306
  type: ClusterIP

### ✅ 5. **iron-gallery Service**

apiVersion: v1
kind: Service
metadata:
  name: iron-gallery-service-nautilus
  namespace: iron-namespace-nautilus
spec:
  selector:
    run: iron-gallery
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 32678
  type: NodePort

### 🧪 How to Apply All:

If you save all the above into a single file (e.g. `iron-gallery-deployment.yaml`), run:

kubectl apply -f iron-gallery-deployment.yaml

Or split them into separate files and apply one by one:

kubectl apply -f namespace.yaml
kubectl apply -f iron-gallery-deployment.yaml
kubectl apply -f iron-db-deployment.yaml
kubectl apply -f iron-db-service.yaml
kubectl apply -f iron-gallery-service.yaml

### ✅ Final Checks:

* Run `kubectl get all -n iron-namespace-nautilus` to verify Pods, Deployments, and Services are up and running.
* Access the **NodePort service** via any Kubernetes node IP and port `32678`.

Let me know if you'd like to create and apply them directly using a script.

# Day 10 Fix Python App Deployed on Kubernetes Cluster
One of the DevOps engineers was trying to deploy a python app on Kubernetes cluster. Unfortunately, due to some mis-configuration, the application is not coming up. Please take a look into it and fix the issues. Application should be accessible on the specified nodePort.

The deployment name is python-deployment-xfusion, its using poroko/flask-demo-app image. The deployment and service of this app is already deployed.

nodePort should be 32345 and targetPort should be python flask app's default port.
Ans:
issue with contianer port(instead 5000 was 8080) and image(instead of poroko/flask-demo-app was poroko/flask-demo)

**Level 4**
# Day 1 Deploy Redis Deployment on Kubernetes
The Nautilus application development team observed some performance issues with one of the application that is deployed in Kubernetes cluster. After looking into number of factors, the team has suggested to use some in-memory caching utility for DB service. After number of discussions, they have decided to use Redis. Initially they would like to deploy Redis on kubernetes cluster for testing and later they will move it to production. Please find below more details about the task:

Create a redis deployment with following parameters:

Create a config map called my-redis-config having maxmemory 2mb in redis-config.

Name of the deployment should be redis-deployment, it should use
redis:alpine image and container name should be redis-container. Also make sure it has only 1 replica.

The container should request for 1 CPU.

Mount 2 volumes:

a. An Empty directory volume called data at path /redis-master-data.

b. A configmap volume called redis-config at path /redis-master.

c. The container should expose the port 6379.

Finally, redis-deployment should be in an up and running state.
Ans:
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-redis-config
data:
  redis-config: |
    maxmemory 2mb

apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis-container
        image: redis:alpine
        ports:
        - containerPort: 6379
        resources:
          requests:
            cpu: "1"
        volumeMounts:
        - name: data
          mountPath: /redis-master-data
        - name: redis-config
          mountPath: /redis-master
          subPath: redis-config
      volumes:
      - name: data
        emptyDir: {}
      - name: redis-config
        configMap:
          name: my-redis-config

# Day 2 Deploy MySQL on Kubernetes
 A new MySQL server needs to be deployed on Kubernetes cluster. The Nautilus DevOps team was working on to gather the requirements. Recently they were able to finalize the requirements and shared them with the team members to start working on it. Below you can find the details:

1.) Create a PersistentVolume mysql-pv, its capacity should be 250Mi, set other parameters as per your preference.

2.) Create a PersistentVolumeClaim to request this PersistentVolume storage. Name it as mysql-pv-claim and request a 250Mi of storage. Set other parameters as per your preference.

3.) Create a deployment named mysql-deployment, use any mysql image as per your preference. Mount the PersistentVolume at mount path /var/lib/mysql.

4.) Create a NodePort type service named mysql and set nodePort to 30007.

5.) Create a secret named mysql-root-pass having a key pair value, where key is password and its value is YUIidhb667, create another secret named mysql-user-pass having some key pair values, where frist key is username and its value is kodekloud_sam, second key is password and value is Rc5C9EyvbU, create one more secret named mysql-db-url, key name is database and value is kodekloud_db1

6.) Define some Environment variables within the container:

a) name: MYSQL_ROOT_PASSWORD, should pick value from secretKeyRef name: mysql-root-pass and key: password

b) name: MYSQL_DATABASE, should pick value from secretKeyRef name: mysql-db-url and key: database

c) name: MYSQL_USER, should pick value from secretKeyRef name: mysql-user-pass key key: username

d) name: MYSQL_PASSWORD, should pick value from secretKeyRef name: mysql-user-pass and key: password

Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.
Ans:
### 1. **Create PersistentVolume (mysql-pv)**

This will define the storage available for MySQL. We're setting the capacity to 250Mi and defining other parameters such as the access mode and storage class.

apiVersion: v1
kind: PersistentVolume
metadata:
  name: mysql-pv
spec:
  capacity:
    storage: 250Mi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: manual
  hostPath:
    path: /mnt/data/mysql


### 2. **Create PersistentVolumeClaim (mysql-pv-claim)**

This will request the 250Mi storage from the PersistentVolume you defined above.

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 250Mi
  storageClassName: manual


### 3. **Create MySQL Deployment (mysql-deployment)**

This will create a MySQL deployment and mount the PersistentVolume at `/var/lib/mysql`.

apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
        - name: mysql
          image: mysql:8.0 # You can choose another version if needed
          ports:
            - containerPort: 3306
          volumeMounts:
            - mountPath: /var/lib/mysql
              name: mysql-storage
          env:
            - name: MYSQL_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql-root-pass
                  key: password
            - name: MYSQL_DATABASE
              valueFrom:
                secretKeyRef:
                  name: mysql-db-url
                  key: database
            - name: MYSQL_USER
              valueFrom:
                secretKeyRef:
                  name: mysql-user-pass
                  key: username
            - name: MYSQL_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql-user-pass
                  key: password
      volumes:
        - name: mysql-storage
          persistentVolumeClaim:
            claimName: mysql-pv-claim


### 4. **Create NodePort Service (mysql)**

This will expose MySQL via a NodePort on port 30007.

apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  selector:
    app: mysql
  ports:
    - protocol: TCP
      port: 3306
      targetPort: 3306
      nodePort: 30007
  type: NodePort

### 5. **Create Secrets**

You'll create three secrets: `mysql-root-pass`, `mysql-user-pass`, and `mysql-db-url`.

#### `mysql-root-pass` Secret:

apiVersion: v1
kind: Secret
metadata:
  name: mysql-root-pass
type: Opaque
data:
  password: WlVJaWRoYjY2Nw== # "YUIidhb667" encoded in base64


#### `mysql-user-pass` Secret:

apiVersion: v1
kind: Secret
metadata:
  name: mysql-user-pass
type: Opaque
data:
  username: a29kZWtsb3VkX3NhbQ== # "kodekloud_sam" encoded in base64
  password: UmM1QzllWXZiVg== # "Rc5C9EyvbU" encoded in base64


#### `mysql-db-url` Secret:

apiVersion: v1
kind: Secret
metadata:
  name: mysql-db-url
type: Opaque
data:
  database: a29kZWtsb3VkX2RiMQ== # "kodekloud_db1" encoded in base64

### 6. **Deploying the Resources**

Once you have the YAML files for all the resources, you can deploy them using `kubectl`. Here's the sequence of commands:

1. **Create PersistentVolume and PersistentVolumeClaim:**
  
   kubectl apply -f mysql-pv.yaml
   kubectl apply -f mysql-pv-claim.yaml
   
2. **Create Secrets:**
  
   kubectl apply -f mysql-root-pass.yaml
   kubectl apply -f mysql-user-pass.yaml
   kubectl apply -f mysql-db-url.yaml

3. **Create Deployment:**
  
   kubectl apply -f mysql-deployment.yaml
   
4. **Create Service:**
 
   kubectl apply -f mysql-service.yaml
   
# Day 3 Kubernetes Nginx and PhpFPM Setup
The Nautilus Application Development team is planning to deploy one of the php-based applications on Kubernetes cluster. As per the recent discussion with DevOps team, they have decided to use nginx and phpfpm. Additionally, they also shared some custom configuration requirements. Below you can find more details. Please complete this task as per requirements mentioned below:

1) Create a service to expose this app, the service type must be NodePort, nodePort should be 30012.

2.) Create a config map named nginx-config for nginx.conf as we want to add some custom settings in nginx.conf.

a) Change the default port 80 to 8095 in nginx.conf.

b) Change the default document root /usr/share/nginx to /var/www/html in nginx.conf.

c) Update the directory index to index  index.html index.htm index.php in nginx.conf.

3.) Create a pod named nginx-phpfpm .

b) Create a shared volume named shared-files that will be used by both containers (nginx and phpfpm) also it should be a emptyDir volume.

c) Map the ConfigMap we declared above as a volume for nginx container. Name the volume as nginx-config-volume, mount path should be /etc/nginx/nginx.conf and subPath should be nginx.conf

d) Nginx container should be named as nginx-container and it should use nginx:latest image. PhpFPM container should be named as php-fpm-container and it should use php:8.3-fpm-alpine image.

e) The shared volume shared-files should be mounted at /var/www/html location in both containers. Copy /opt/index.php from jump host to the nginx document root inside the nginx container, once done you can access the app using App button on the top bar.

Before clicking on finish button always make sure to check if all pods are in running state.

You can use any labels as per your choice.
Ans:
To complete this task, you'll need to:

1. **Create a ConfigMap for the custom `nginx.conf`**.
2. **Create a Pod with two containers (nginx and php-fpm)**.
3. **Mount shared and config volumes properly**.
4. **Create a NodePort service to expose the nginx container**.
5. **Copy `/opt/index.php` to the appropriate path inside the nginx container**.

### ✅ 1. Create `nginx.conf` file with custom configuration

Save the following content in a file named `nginx.conf`:


worker_processes 1;

events { worker_connections 1024; }

http {
    server {
        listen 8095;
        server_name localhost;

        root /var/www/html;
        index index.html index.htm index.php;

        location / {
            try_files $uri $uri/ =404;
        }

        location ~ \.php$ {
            include fastcgi_params;
            fastcgi_pass 127.0.0.1:9000;
            fastcgi_index index.php;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        }
    }
}

### ✅ 2. Create the ConfigMap `nginx-config`

Run the following command to create it:

kubectl create configmap nginx-config --from-file=nginx.conf

### ✅ 3. Create the Pod `nginx-phpfpm`

Save the following YAML as `nginx-phpfpm-pod.yaml`:

apiVersion: v1
kind: Pod
metadata:
  name: nginx-phpfpm
  labels:
    app: php-nginx
spec:
  volumes:
    - name: shared-files
      emptyDir: {}
    - name: nginx-config-volume
      configMap:
        name: nginx-config
  containers:
    - name: nginx-container
      image: nginx:latest
      ports:
        - containerPort: 8095
      volumeMounts:
        - name: shared-files
          mountPath: /var/www/html
        - name: nginx-config-volume
          mountPath: /etc/nginx/nginx.conf
          subPath: nginx.conf
    - name: php-fpm-container
      image: php:8.3-fpm-alpine
      volumeMounts:
        - name: shared-files
          mountPath: /var/www/html


Apply the pod configuration:

kubectl apply -f nginx-phpfpm-pod.yaml

### ✅ 4. Create the NodePort Service

Save the following YAML as `nginx-service.yaml`:

apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: php-nginx
  type: NodePort
  ports:
    - protocol: TCP
      port: 8095
      targetPort: 8095
      nodePort: 30012

Apply the service configuration:

kubectl apply -f nginx-service.yaml
### ✅ 5. Copy `/opt/index.php` to container

Use the following command to copy the file from your host into the container:

kubectl cp /opt/index.php nginx-phpfpm:/var/www/html/index.php -c nginx-container

### ✅ 6. Verify Everything

* Check pod status:

kubectl get pods

Ensure the pod `nginx-phpfpm` is in `Running` state.

* Test the service by accessing it on port **30012** (use App button or browser depending on your environment).

# Day 4 Deploy Drupal App on Kubernetes
We need to deploy a Drupal application on Kubernetes cluster. The Nautilus application development team want to setup a fresh Drupal as they will do the installation on their own. Below you can find the requirements, they have shared with us.

1) Configure a persistent volume drupal-mysql-pv with hostPath = /drupal-mysql-data (/drupal-mysql-data directory already exists on the worker Node i.e jump host), 5Gi of storage and ReadWriteOnce access mode.

2) Configure one PersistentVolumeClaim named drupal-mysql-pvc with storage request of 3Gi and ReadWriteOnce access mode.

3) Create a deployment drupal-mysql with 1 replica, use mysql:5.7 image. Mount the claimed PVC at /var/lib/mysql.

4) Create a deployment drupal with 1 replica and use drupal:8.6 image.

5) Create a NodePort type service which should be named as drupal-service and nodePort should be 30095.

6) Create a service drupal-mysql-service to expose mysql deployment on port 3306.

7) Set rest of the configration for deployments, services, secrets etc as per your preferences. At the end you should be able to access the Drupal installation page by clicking on App button
Ans:
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: drupal-mysql-pv
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: manual
  hostPath:
    path: /drupal-mysql-data
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: drupal-mysql-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 3Gi
  storageClassName: manual

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: drupal-mysql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: drupal-mysql
  template:
    metadata:
      labels:
        app: drupal-mysql
    spec:
      containers:
        - name: mysql
          image: mysql:5.7
          env:
            - name: MYSQL_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql-secret
                  key: mysql-root-password
            - name: MYSQL_DATABASE
              valueFrom:
                secretKeyRef:
                  name: mysql-secret
                  key: mysql-database
            - name: MYSQL_USER
              valueFrom:
                secretKeyRef:
                  name: mysql-secret
                  key: mysql-user
            - name: MYSQL_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql-secret
                  key: mysql-password
          ports:
            - containerPort: 3306
          volumeMounts:
            - mountPath: /var/lib/mysql
              name: mysql-storage
      volumes:
        - name: mysql-storage
          persistentVolumeClaim:
            claimName: drupal-mysql-pvc
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: drupal
spec:
  replicas: 1
  selector:
    matchLabels:
      app: drupal
  template:
    metadata:
      labels:
        app: drupal
    spec:
      containers:
        - name: drupal
          image: drupal:8.6
          ports:
            - containerPort: 80
          env:
            - name: DRUPAL_DB_HOST
              value: drupal-mysql-service
            - name: DRUPAL_DB_NAME
              valueFrom:
                secretKeyRef:
                  name: mysql-secret
                  key: mysql-database
            - name: DRUPAL_DB_USER
              valueFrom:
                secretKeyRef:
                  name: mysql-secret
                  key: mysql-user
            - name: DRUPAL_DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql-secret
                  key: mysql-password      
---
apiVersion: v1
kind: Service
metadata:
  name: drupal-service
spec:
  type: NodePort
  selector:
    app: drupal
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30095
---
apiVersion: v1
kind: Service
metadata:
  name: drupal-mysql-service
spec:
  selector:
    app: drupal-mysql
  ports:
    - port: 3306
      targetPort: 3306

---
apiVersion: v1
kind: Secret
metadata:
  name: mysql-secret
type: Opaque
data:
  mysql-root-password: cGFzc3dvcmQ=          # 'password' (base64 encoded)
  mysql-database: ZHJ1cGFs                   # 'drupal'
  mysql-user: ZHJ1cHVzZXI=                   # 'drupuser'
  mysql-password: ZHJ1cHBhc3M=               # 'druppass'

# Day 5 Deploy Guest Book App on Kubernetes
The Nautilus Application development team has finished development of one of the applications and it is ready for deployment. It is a guestbook application that will be used to manage entries for guests/visitors. As per discussion with the DevOps team, they have finalized the infrastructure that will be deployed on Kubernetes cluster. Below you can find more details about it.


BACK-END TIER

Create a deployment named redis-master for Redis master.

a.) Replicas count should be 1.

b.) Container name should be master-redis-datacenter and it should use image redis.

c.) Request resources as CPU should be 100m and Memory should be 100Mi.

d.) Container port should be redis default port i.e 6379.

Create a service named redis-master for Redis master. Port and targetPort should be Redis default port i.e 6379.

Create another deployment named redis-slave for Redis slave.

a.) Replicas count should be 2.

b.) Container name should be slave-redis-datacenter and it should use gcr.io/google_samples/gb-redisslave:v3 image.

c.) Requests resources as CPU should be 100m and Memory should be 100Mi.

d.) Define an environment variable named GET_HOSTS_FROM and its value should be dns.

e.) Container port should be Redis default port i.e 6379.

Create another service named redis-slave. It should use Redis default port i.e 6379.

FRONT END TIER

Create a deployment named frontend.

a.) Replicas count should be 3.

b.) Container name should be php-redis-datacenter and it should use gcr.io/google-samples/gb-frontend@sha256:a908df8486ff66f2c4daa0d3d8a2fa09846a1fc8efd65649c0109695c7c5cbff image.

c.) Request resources as CPU should be 100m and Memory should be 100Mi.

d.) Define an environment variable named as GET_HOSTS_FROM and its value should be dns.

e.) Container port should be 80.

Create a service named frontend. Its type should be NodePort, port should be 80 and its nodePort should be 30009.

Finally, you can check the guestbook app by clicking on App button.


You can use any labels as per your choice.
Ans:
#BACK-END TIER
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-master
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
      tier: backend
      role: master
  template:
    metadata:
      labels:
        app: redis
        tier: backend
        role: master
    spec:
      containers:
      - name: master-redis-datacenter
        image: redis:6.0.9-alpine
        ports:
        - containerPort: 6379
        resources:
          requests:
            memory: "100Mi"
            cpu: "100m"
---
#Back-end Service
apiVersion: v1
kind: Service
metadata:
  name: redis-master
spec:
  selector:
    app: redis
    tier: backend
    role: master
  ports:
    - port: 6379
      targetPort: 6379
---
#BACK-END TIER-Slave
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-slave
spec:
  replicas: 2
  selector:
    matchLabels:
      app: redis
      tier: backend
      role: slave
  template:
    metadata:
      labels:
        app: redis
        tier: backend
        role: slave
    spec:
      containers:
      - name: slave-redis-datacenter
        image: gcr.io/google_samples/gb-redisslave:v3
        env:
        - name: GET_HOSTS_FROM
          value: "dns"
        ports:
        - containerPort: 6379
        resources:
          requests:
            memory: "100Mi"
            cpu: "100m"
---
#Slave Service
apiVersion: v1
kind: Service
metadata:
  name: redis-slave
spec:
  selector:
    app: redis
    tier: backend
    role: slave
  ports:
    - port: 6379
      targetPort: 6379
---
#FRONT-END TIER
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: guestbook
      tier: frontend
  template:
    metadata:
      labels:
        app: guestbook
        tier: frontend
    spec:
      containers:
      - name: php-redis-datacenter
        image: gcr.io/google-samples/gb-frontend@sha256:a908df8486ff66f2c4daa0d3d8a2fa09846a1fc8efd65649c0109695c7c5cbff
        env:
        - name: GET_HOSTS_FROM
          value: "dns"
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "100Mi"
            cpu: "100m"
---
#Front-end Service
apiVersion: v1
kind: Service
metadata:
  name: frontend
spec:
  type: NodePort
  selector:
    app: guestbook
    tier: frontend
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30009
---