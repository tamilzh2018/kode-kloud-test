## 🧩 **Azure Virtual Machines & Networking**

### **Q1: Create SSH Key Pair for Azure Virtual Machine**

> *Your company has a policy to allow only SSH key-based access to virtual machines. Generate a secure SSH key pair for Linux VM deployment in Azure using CLI. How would you securely store the private key and share access with team members?*

### **Q2: Create an Azure Virtual Machine**

> *Deploy a Linux-based Azure VM in the `East US` region with a Standard B2s size and a new resource group. Ensure it uses SSH for authentication and is placed in a custom virtual network. What are the minimal required configurations?*

### **Q3: Create a Virtual Network (VNet) in Azure**

> *You are setting up an isolated environment for a three-tier application. Create a virtual network with a /16 CIDR range and explain how you would subdivide it into subnets for web, app, and database tiers.*

### **Q4: Create a Virtual Network (IPv4) in Azure**

> *A legacy system requires IPv4-only communication. Create a VNet that supports only IPv4 addressing and launch a VM in it. How do you ensure the VM can access external services securely?*

### **Q5: Create a Virtual Network (IPv6) in Azure**

> *Your organization is migrating to IPv6 to future-proof its infrastructure. Create a dual-stack (IPv4 + IPv6) VNet. What address prefixes, subnets, and route configurations are required to enable IPv6 traffic?*

### **Q6: Create a Subnet in Azure Virtual Network**

> *Add a subnet named `web-subnet` (CIDR: 10.0.1.0/24) to an existing VNet. How do you ensure this subnet is later associated with a network security group and routing table?*

### **Q7: Create a Public IP Address for Azure VM**

> *Your customer wants a public-facing application. Allocate a static public IP address and assign it to a new or existing VM. Should you choose Basic or Standard SKU, and why?*

### **Q8: Delete Azure Virtual Machine Using Console**

> *A developer VM is no longer in use. Delete the VM and optionally remove associated resources (NIC, disk, IP) from the Azure portal. What precautions should you take to avoid orphaned or shared resources being deleted?*

### **Q9: Delete Azure Virtual Machine Using CLI**

> *Write the CLI command to delete a VM in the `dev-rg` resource group without deleting its managed disk and public IP. Why might this approach be useful for backups or reattachments?*

### **Q10: Delete a Virtual Network (VNet) in Azure**

> *Attempt to delete a VNet, but the operation fails. Investigate the dependencies (e.g., subnets with NICs or gateways) and list the steps to safely remove all associated resources before deleting the VNet.*

## 🏷️ **Tagging, Access & Connectivity**

### **Q11: Add and Manage Tags for Azure Virtual Machines**

> *Your finance team needs to track costs by environment. Add `Environment=Production` and `Owner=DevOps` tags to existing VMs using both portal and CLI. How do tags impact billing and governance?*

### **Q12: SSH into an Azure Virtual Machine**

> *You deployed a Linux VM but can't SSH into it. Verify your key pair, NSG rules, and public IP configuration. How do you troubleshoot and securely access the VM?*

## 💾 **Disk and Network Configuration**

### **Q13: Attach Managed Disk to Azure Virtual Machine**

> *Your VM needs additional storage for data logging. Create and attach a 128 GB managed disk. Format and mount it on a Linux instance. What performance tier would you choose for medium I/O workloads?*

### **Q14: Attach Network Interface Card (NIC) to Azure Virtual Machine**

> *To improve network throughput, add a second NIC to your VM. What are the prerequisites, and how does this impact VM size and OS-level configuration?*

### **Q15: Attach Public IP to Azure Virtual Machine**

> *You created a VM without a public IP. Now you need to access it remotely. Create and associate a static public IP to the VM using both portal and CLI. What is the impact of Basic vs. Standard IP SKUs?*

### **Q16: Change Azure Virtual Machine Size Using Console**

> *Your VM is underpowered for its workload. Resize it to a `Standard D2s v3` instance using the portal. What must you consider regarding downtime, available quotas, and regional availability?*

### **Q17: Create and Attach Managed Disks in Azure**

> *A VM requires two new data disks: one for logs, one for app data. Create two disks, attach them, and configure Linux to use LVM for redundancy. What are the IOPS limitations for the selected disk types?*

## 🔐 **Security & Access Control**

### **Q18: Create and Configure Network Security Group (NSG) in Azure**

> *Create an NSG to allow inbound SSH and HTTP traffic but deny all other inbound access. Associate it with a subnet. How do you test and verify the NSG is working correctly?*

## ☁️ **Azure Storage - Blob Containers**

### **Q19: Create a Private Azure Blob Storage Container**

> *Create a blob container in a storage account with private access. Upload a sample file and verify that it cannot be accessed without credentials. How would you grant time-limited access via a Shared Access Signature (SAS)?*

### **Q20: Create a Public Azure Blob Storage Container**

> *You’re hosting public documents like product manuals. Create a container with anonymous read access. What are the security and compliance implications of this approach?*

### **Q21: Backup and Delete Azure Storage Blob Container**

> *Before deleting a storage container, you must back it up. Copy all blobs to another container in a different storage account. Then delete the original container safely. What tools or automation could you use for backup?*

### **Q22: Copy Data to an Azure Blob Storage Container**

> *You need to upload 10 GB of data from your on-premises machine to Azure Blob Storage. Use `azcopy` to perform the operation efficiently. How do you monitor progress and resume failed transfers?*

### **Q23: Convert Public Azure Blob Container to Private**

> *You mistakenly created a container with public access. Update it to private without deleting or re-uploading the contents. What changes in access behavior occur post-conversion?*

## 📊 **Azure SQL**

### **Q24: Create Azure SQL Database**

> *Deploy an Azure SQL Database in the `Basic` tier within a new SQL Server. Configure a firewall rule to allow access from your current IP only. How do you connect from Azure Data Studio or SQL Server Management Studio?*

### **Q25: Backup an Azure SQL Database**

> *Implement long-term retention (LTR) for an Azure SQL Database. Set weekly backups for 12 months. Where are backups stored, and how can you restore a database to a specific point in time?*

## 🔧 **Infrastructure as Code & Automation**

### **Q26: Deploy Azure Resources Using ARM Template**

> *Use an ARM template to deploy a virtual network, storage account, and virtual machine as a single deployment. Include parameters for region, VM size, and storage type. How would you validate and test the deployment before applying it?*

## 💻 **Azure CLI Operations**

### **Q27: Create VM using Azure CLI**

> *Create a Windows Server VM using Azure CLI, including a new resource group, virtual network, NSG, and public IP. What are the minimum parameters needed to launch a working VM?*

### **Q28: Change Azure Virtual Machine Size Using CLI**

> *Resize an existing VM to `Standard F2s v2` using CLI. What steps are required if the VM is currently running, and how do you confirm the new size is applied?*

### **Q29: Create a Public Blob Container Using Azure CLI**

> *Use CLI to create a storage account and blob container with public read access. Upload a file and share its public URL. How would you verify public access from a browser?*

### **Q30: Create a Private Blob Container Using Azure CLI**

> *Using CLI, create a storage account with secure transfer enabled. Create a private blob container and upload a file. How do you generate a SAS token and use it to access the file securely?*


**Level 2**

### 🔌 **Q1: Assigning Public IP to Virtual Machines**

> *You deployed multiple VMs in a load-balanced setup but only one VM has a public IP. Update the configuration so each VM can be reached individually for admin purposes without disrupting the application traffic. Should you use dynamic or static public IPs? What are the security implications?*

### 📝 **Q2: Configuring Instances with User Data**

> *You want every Linux VM created in your environment to automatically install Docker and start an Nginx container on boot. Use cloud-init/user data to achieve this. What format should the script be in, and how would you debug it if it fails?*

### 🔄 **Q3: Automating User Data Configuration Using the CLI**

> *You’re automating VM provisioning via Azure CLI. Include a custom user data script that installs software on boot. How do you encode the script properly, pass it in the `az vm create` command, and verify it was executed successfully?*

### 🔐 **Q4: Securing Virtual Machine SSH Access**

> *You need to restrict SSH access to your VMs to only a specific IP range and disable password-based authentication. Implement this using NSGs and VM OS-level changes. What extra steps are needed if using Azure Bastion instead of public IPs?*

### 💽 **Q5: Expanding and Managing Disk Storage**

> *Your VM is running out of space. Attach a new data disk and expand the root volume by 50 GB without downtime. How do you perform this safely and validate the operation inside the VM (Linux or Windows)?*

### 🌐 **Q6: Deploying Virtual Machines in a Public Virtual Network**

> *You’re deploying a VM that hosts a public-facing web application. Configure a public subnet with internet access, NSG rules, and a VM with a static IP. What routing and security changes are required to make the application accessible securely?*

### 🔒 **Q7: Deploying Virtual Machines in a Private Virtual Network**

> *For compliance, you need to deploy a VM in a private subnet with no internet exposure. Use NAT Gateway or Azure Bastion for outbound access or management. How do you configure routing and DNS resolution in such an environment?*

### 🧰 **Q8: Troubleshooting Public Virtual Network Configurations**

> *Your VM in a public subnet is not accessible via its public IP. List and explain all the configuration points (e.g., NSGs, NIC, public IP association, route tables) you would inspect to identify and fix the issue.*

### 📦 **Q9: Working with Azure Container Registry (ACR)**

> *Push a custom Docker image to ACR and deploy it on an Azure VM. Authenticate securely, set up `docker login`, and configure the VM to pull and run the image on boot. How would you automate this as part of a CI/CD pipeline?*

### 🔧 **Q10: Set Up and Manage a Secure Azure DevOps Repository**

> *Your team is building infrastructure using ARM templates stored in Azure Repos. Create a private repository, configure branch policies for code reviews, and integrate it with Azure Pipelines. How would you implement secret scanning and access control?*

### 🌍 **Q11: Deploying and Managing a Web Application**

> *Deploy a multi-tier web application consisting of frontend and backend components. Use VMs or containers, secure communication with HTTPS, and manage scaling based on load. How would you monitor performance and perform zero-downtime updates?*

### 🔄 **Q12: Synchronizing Containers Using the CLI**

> *You updated a Docker image and need to synchronize your ACR with the latest build. Use Azure CLI to push the image, verify it’s available, and redeploy the container on an Azure App Service or VM. How do you automate this with minimal downtime?*

### ⚖️ **Q13: Integrating Virtual Machines with Application Load Balancer**

> *Distribute traffic across multiple VMs hosting a web application using Azure Load Balancer. Implement health probes and ensure VMs automatically register/deregister during scaling. What type of load balancer (Basic vs. Standard) is appropriate, and why?*

### 🌐 **Q14: Enabling Internet Connectivity for Virtual Machines**

> *Your VMs in a private subnet need internet access for software updates. Set up a NAT Gateway and configure route tables accordingly. How do you verify connectivity without exposing the VMs publicly?*

### 🌉 **Q15: Configuring Virtual Network Peering**

> *You deployed backend services in a separate VNet from your frontend services. Configure VNet peering to allow secure communication between the two VNets. How do you handle DNS resolution across VNets and restrict unnecessary access?*

**Level 3**

### 📦 **Q1: Managing Storage Lifecycle in Azure**

> *You are storing large volumes of infrequently accessed backup files in Azure Blob Storage. Design and implement a lifecycle management policy that moves data from Hot to Cool to Archive tiers after 30, 90, and 180 days respectively. How would you validate the policy and monitor cost savings over time?*

### 🐬 **Q2: Setting Up MySQL on a Virtual Machine in Azure**

> *Your development team requires a MySQL database on a Linux VM. Deploy the VM, install and configure MySQL using a startup script, and secure it using a firewall and NSG. How would you ensure remote access is encrypted and restrict access to only specific IP ranges?*

### 🐳 **Q3: Running Containers on Azure Virtual Machines**

> *You have a Dockerized Python app and need to deploy it to a Linux-based Azure VM using Docker. Set up the VM, install Docker, and ensure the container starts automatically on reboot. How would you monitor and update the container remotely?*

### 🌐 **Q4: Deploying a Static Website Using Containers on Azure**

> *Build a container image for a static HTML website, push it to Azure Container Registry (ACR), and deploy it on a Linux VM. Ensure it's publicly accessible and secured with HTTPS using a reverse proxy like Nginx inside the container. What are the pros and cons of using a VM vs App Service or Azure Container Apps for this use case?*

### 🔐 **Q5: Managing Secrets with Azure Key Vault**

> *You’re deploying a web application that requires secure access to a database connection string and API key. Store the secrets in Azure Key Vault and configure access policies. Integrate it with a VM or containerized application to fetch the secrets at runtime without hardcoding them. How would you automate rotation of secrets?*

### 📋 **Q6: Working with Azure Table Storage**

> *A lightweight, NoSQL-like solution is needed to store user activity logs with high write and moderate read patterns. Set up and integrate Azure Table Storage into your application. How do you design the partition/row key schema for optimal performance, and how do you query the data efficiently using SDK or REST API?*

### 🚀 **Q7: Deploying a Web Application from Repository on Azure**

> *You’ve built a Node.js web application and pushed it to a GitHub repo. Deploy this app to Azure App Service with continuous deployment enabled. Configure build and deployment settings, environment variables, and logging. How would you enable staging slots for testing before production rollout?*

### ⚙️ **Q8: Configuring Azure VM with Application Gateway**

> *You want to expose a VM-hosted web application securely over HTTPS using Azure Application Gateway. Set up the gateway, configure backend pools, listeners, and rules. Add SSL termination and implement Web Application Firewall (WAF) policies. How do you verify traffic routing and troubleshoot if the VM is not responding?*

### 📡 **Q9: Integrating Azure Event Hub with Virtual Machines**

> *A logging agent on your VM should forward application logs to Azure Event Hub for downstream processing. Set up Event Hub, configure the agent to send logs using SDK or Event Hub REST API, and monitor throughput. How would you handle retries, dead-lettering, and scaling the ingestion layer?*

### ☸️ **Q10: Azure Kubernetes Service (AKS) Setup and Management**

> *Set up a production-ready AKS cluster with autoscaling and integrated ACR for image pulling. Deploy a multi-container app using Helm or YAML manifests, and secure it with ingress controller, TLS, and Azure AD Pod Identity. How do you enable observability with Prometheus/Grafana and handle secret injection securely in the cluster?*

**Level 4**

### 🛠️ **Q1: VM Setup and Configuration for Azure API Gateway**

> **Scenario:**
> You need to host a backend REST API on an Azure VM and expose it securely through **Azure API Management (APIM)** to external clients.
> **Question:**
> Set up an Azure Linux or Windows VM to host the REST API. Configure Azure API Management to act as a gateway in front of the VM. Implement rate limiting and IP whitelisting in APIM.
> How would you:

* Secure API access using subscription keys or OAuth2?
* Route traffic via a custom domain with HTTPS?
* Protect the VM with NSGs and restrict public access to only the APIM instance?

### 🔄 **Q2: EventHub to Blob Storage Integration Setup**

> **Scenario:**
> Your application pushes real-time sensor data to Azure Event Hub. You are required to archive this data automatically into Azure Blob Storage for analytics.
> **Question:**
> Configure Azure Event Hub Capture to store data directly into Blob Storage in AVRO format.
> How would you:

* Set up the storage container and policy securely?
* Ensure the Event Hub is partitioned for performance?
* Process AVRO data later using Azure Data Factory or Synapse?

### 🧭 **Q3: SQL Database Migration and Setup**

> **Scenario:**
> You’re tasked with migrating a large on-premises SQL Server database to **Azure SQL Database** with minimal downtime.
> **Question:**
> Plan and implement the migration using **Data Migration Assistant (DMA)** or **Azure Database Migration Service (DMS)**.
> How would you:

* Assess compatibility and resolve issues?
* Ensure replication for near-zero downtime cutover?
* Implement firewall and VNet rules to restrict access to the new database?

### 📦 **Q4: VM and ACR Integration for Storage**

> **Scenario:**
> Your organization uses Docker to package applications. You need to run these containers on Azure VMs and store the images in **Azure Container Registry (ACR)**.
> **Question:**
> Deploy a Linux VM with Docker installed and connect it to ACR securely.
> How would you:

* Authenticate the VM using a service principal or managed identity?
* Pull and run an image on VM startup using a custom script?
* Ensure ACR access logs and image scanning are enabled?

### 🌐 **Q5: VM Setup with Web Storage Integration**

> **Scenario:**
> You’re deploying a web application on a VM that stores user-uploaded files in **Azure Blob Storage**.
> **Question:**
> Provision the VM, install the web app, and configure it to store all uploads in Blob Storage using a storage account key or SAS.
> How would you:

* Secure the storage connection (Key Vault vs environment variables)?
* Scale storage access using a private endpoint or VNet service endpoint?
* Handle failures when Blob Storage is unreachable?
