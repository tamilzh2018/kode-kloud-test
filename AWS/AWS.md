Here’s a set of **scenario-based questions** mapped to each of the topics you've listed. These are designed to simulate real-world AWS use cases and test conceptual understanding along with hands-on knowledge.

### 🔐 **Key Management & Networking**

**Q1: Create Key Pair**

> *You are tasked with deploying EC2 instances for a new application. For secure SSH access, you need a new key pair that will be used by all developers. What steps would you take to create a key pair using the AWS Console and CLI?*
## Q1:For this task, create a key pair with the following requirements:

Name of the key pair should be devops-kp.

Key pair type must be rsa

**Q2: Create Security Group**

> *Your web application requires HTTP and SSH access from the internet. Design and create a security group that meets these requirements. What rules would you configure?*
1) The name of the security group must be devops-sg.

2) The description must be Security group for Nautilus App Servers.

3) Add an inbound rule of type HTTP, with a port range of 80, and source CIDR range 0.0.0.0/0.

4) Add another inbound rule of type SSH, with a port range of 22, and source CIDR range 0.0.0.0/0.
**Q3: Create GP3 Volume**

> *A developer needs a high-performance volume for database storage. Create a GP3 volume with 200 GiB and 3000 IOPS in a specific AZ. How do you proceed?*
Create a volume with the following requirements:

Name of the volume should be devops-volume.

Volume type must be gp3.

Volume size must be 2 GiB.
Create a GP3 volume with 2 GiB named as devops-volume
**Q4: Create Subnet**

> *You are setting up a 3-tier architecture. As part of this, you need to create a subnet in a given VPC with CIDR `10.0.1.0/24`. How would you do this and why might you choose a specific AZ?*

1).For this task, create one subnet named datacenter-subnet under default VPC.

**Q5: Allocate Elastic IP**

> *A legacy application requires a static IP to allowlist in external firewalls. Allocate an Elastic IP that can be used with a new EC2 instance.*

For this task, allocate an Elastic IP address, name it as nautilus-eip.

### 💻 **EC2 Management**

**Q6: Launch EC2 Instance**

> *You are deploying a testing environment and need a t3.micro Amazon Linux instance in a specific subnet with a new key pair and security group. How would you configure and launch it?*
For this task, create an EC2 instance with following requirements:

1) The name of the instance must be datacenter-ec2.

2) You can use the Amazon Linux AMI to launch this instance.

3) The Instance type must be t2.micro.

4) Create a new RSA key pair named datacenter-kp.

5) Attach the default (available by default) security group.
**Q7: Change EC2 Instance Type**

> *A t2.micro instance you launched is underperforming. You need to upgrade it to t3.medium. Walk through the steps to do this with minimal downtime.*
1) Change the instance type from t2.micro to t2.nano for xfusion-ec2 instance.

2) Make sure the ec2 instance xfusion-ec2 is in running state after the change.

**Q8: Enable Stop Protection for EC2 Instance**

> *Your production EC2 instance is mission-critical and must not be stopped accidentally. Enable stop protection for this instance. Explain how it helps.*

There is an EC2 instance named xfusion-ec2 under us-east-1 region, enable the stop protection for this instance.

**Q9: Enable Termination Protection for EC2 Instance**

> *You want to protect an EC2 instance from accidental deletion during a clean-up script. Enable termination protection and explain the implications.*

An instance named nautilus-ec2 already exists in us-east-1 region. Enable termination protection for the same.

**Q10: Attach Elastic IP to EC2 Instance**

> *You have an Elastic IP allocated. Assign it to an EC2 instance that hosts your website, ensuring the IP remains static across reboots.*

There is an instance named datacenter-ec2 and an elastic-ip named datacenter-ec2-eip in us-east-1 region. Attach the datacenter-ec2-eip elastic-ip to the datacenter-ec2 instance.

**Q11: Attach Elastic Network Interface to EC2 Instance**

> *Your application requires multiple network interfaces. Attach a second ENI to an EC2 instance in a different subnet and describe the use case.*

An instance named devops-ec2 and an elastic network interface named devops-eni already exists in us-east-1 region.

Attach the devops-eni network interface to the devops-ec2 instance.
Make sure status is attached before submitting the task.
Please make sure instance initialisation has been completed before submitting this task.


**Q12: Attach Volume to EC2 Instance**

> *Your database has outgrown its current volume. Attach a new 100 GiB GP3 volume to your existing EC2 instance and mount it properly.*
An instance named datacenter-ec2 and a volume named datacenter-volume already exists in us-east-1 region. Attach the datacenter-volume volume to the datacenter-ec2 instance, make sure to set the device name to /dev/sdb while attaching the volume.

**Q13: Create AMI from EC2 Instance**

> *Before applying risky updates to your EC2 instance, create a backup. How would you create an AMI to preserve the instance state?*

For this task, create an AMI from an existing EC2 instance named xfusion-ec2 with the following requirement:

Name of the AMI should be xfusion-ec2-ami, make sure AMI is in available state.

**Q14: Terminate EC2 Instance**

> *You no longer need a development instance. What steps must you take to terminate it safely, ensuring data is not lost unintentionally?*

1) Delete the ec2 instance named xfusion-ec2 present in us-east-1 region.

2) Before submitting your task, make sure instance is in terminated state.

### 💾 **EBS & Snapshots**

**Q15: Create Volume Snapshot**

> *You’re about to run a script that might corrupt data. Create a snapshot of your volume so you can restore if needed. How would you do it?*

Create a snapshot of an existing volume named xfusion-vol in us-east-1 region.

1) The name of the snapshot must be xfusion-vol-ss.

2) The description must be xfusion Snapshot.

3) Make sure the snapshot status is completed before submitting the task.

### 🔐 **IAM**

**Q16: Create IAM User**

> *A new developer joins your team and needs access to AWS. Create an IAM user with console access and explain secure password handling.*
For this task, create an IAM user named iamuser_javed.
**Q17: Create IAM Group**

> *You want to manage permissions for a team of DevOps engineers. Create an IAM group and attach relevant policies.*
Create an IAM group named iamgroup_kirsty

**Q18: Create Read-Only IAM Policy for EC2 Console Access**

> *You want auditors to only view EC2 resources, not modify them. Create a custom IAM policy with EC2 read-only permissions.*
Create an IAM policy named iampolicy_james in us-east-1 region, it must allow read-only access to the EC2 console, i.e this policy must allow users to view all instances, AMIs, and snapshots in the Amazon EC2 console.


**Q19: Attach IAM Policy to IAM User**

> *Assign the read-only EC2 policy to a specific user. Walk through the steps of attaching the policy and verifying permissions.*

**Q20: Create IAM Role for EC2 with Policy Attachment**

> *You need an EC2 instance to access S3 securely without using access keys. Create a role with S3 full access and attach it to the instance.*

**Q21: Delete IAM Group**

> *You are cleaning up unused IAM groups. One group is no longer associated with users or policies. How do you safely delete it?*

**Q22: Delete IAM Role**

> *You no longer need a role created for a decommissioned EC2 instance. Delete it without affecting other services.*



### ☁️ **S3 Management**

**Q23: Create Private S3 Bucket**

> *You need to store sensitive financial reports. Create a private S3 bucket and ensure no public access is allowed.*

**Q24: Create Public S3 Bucket**

> *Host a static website on S3. Create a bucket that is publicly accessible and configure the necessary permissions.*

**Q25: Enable Versioning for S3 Bucket**

> *To track changes to critical files, enable versioning on an existing S3 bucket. What changes occur, and how does it help?*

**Q26: Transfer Data to Existing S3 Bucket**

> *Upload daily log files from your local system to a specific S3 bucket. Describe the command or console method you'd use.*

**Q27: Copy and Delete S3 Bucket Data**

> *Copy data from one bucket to another for backup, then delete the original. Explain how to do both steps safely.*



### 🛢️ **RDS Management**

**Q28: Create Publicly Accessible RDS Instance**

> *You’re setting up a test database that needs to be accessed from your laptop. Launch an RDS MySQL instance and configure it for public access.*

**Q29: Create Snapshot of RDS Instance**

> *Before performing a destructive migration, create a manual snapshot of your RDS instance. Describe how to do it and why it's useful.*

**Q30: Enable Delete Protection for RDS Instance**

> *Prevent accidental deletion of your production database. Enable delete protection and explain what happens if deletion is attempted.*

**Q31: Upgrade RDS MySQL Engine Version via AWS Console**

> *Your security team mandates an upgrade from MySQL 5.7 to 8.0. Perform the upgrade through the console with minimal downtime.*

**Q32: Delete RDS Instance**

> *Your dev environment is no longer needed. Delete the RDS instance while preserving the final snapshot.*



### 🌐 **VPC & Networking**

**Q33: Create VPC**

> *Design a custom VPC for your application with a CIDR of `10.0.0.0/16`. Create the VPC and explain what components are auto-created.*

**Q34: Define VPC CIDR**

> *You are planning a network that requires at least 4000 IP addresses. What CIDR block would you define and why?*

**Q35: Implement VPC IPv6**

> *Your application needs IPv6 support. Modify an existing VPC to enable IPv6 and assign addresses to subnets.*

**Q36: Delete VPC**

> *You're cleaning up your AWS environment. Safely delete a VPC that has no dependent resources.*



### 🧪 **CLI-Based Operations**

**Q37: Create Private S3 Bucket via AWS CLI**

> *Use AWS CLI to create an S3 bucket named `secure-archive-logs`, ensure it blocks all public access, and verify the settings.*

**Q38: Launch EC2 Instance via AWS CLI**

> *Use the AWS CLI to launch a t3.micro EC2 instance in a specific subnet, with a key pair and a defined security group.*

**Q39: Modify EC2 Instance Type via AWS CLI**

> *Upgrade an existing EC2 instance type from t2.micro to t3.medium using AWS CLI. What are the necessary steps, including stop/start?*

**Q40: Delete EC2 Instance via AWS CLI**

> *Terminate an EC2 instance using AWS CLI while ensuring you don't delete one tagged as “Production”. Describe how you’d script this check.*




**Level 2**

### 💻 **EC2 & Load Balancing**

**Q1: Setting Up an EC2 Instance with an Elastic IP for Application Hosting**

> *You are tasked with hosting a small web application on an EC2 instance. To ensure consistent access, you need to assign a static IP. How do you launch an EC2 instance and associate an Elastic IP to it?*
 or 
 Your application backend needs to be accessed by a partner system that requires a fixed IP. Launch an EC2 instance with a security group allowing HTTP and SSH, associate an Elastic IP, and verify connectivity. What steps do you take and how do you test it?

 Create an EC2 instance named datacenter-ec2 using any linux AMI like ubuntu, the Instance type must be t2.micro and associate an Elastic IP address with this instance, name it as datacenter-eip.

**Q2: Expanding EC2 Instance Storage for Development Needs**

> *Your development EC2 instance is running out of disk space. Expand the existing root volume from 8 GiB to 30 GiB without data loss. Describe the steps involved.*

or

Your dev team is requesting more disk space on a live EC2 instance running a Linux OS. Resize the attached EBS volume from 20 GiB to 50 GiB without terminating or stopping the instance. What tools/commands would you use inside the instance to make the space available?

**Q3: Creating and Launching EC2 Instances from Custom AMIs**

> *You’ve configured an EC2 instance with all necessary tools for your app. Create a reusable AMI from it and launch 2 new instances based on that image.*

or 

You’ve configured a baseline EC2 instance with Docker and monitoring tools. Create an AMI and use it to launch two new instances in different subnets. How do you manage updates to this image over time?

**Q4: Configuring Secure SSH Access to an EC2 Instance**

> *You want to securely access your EC2 instance using SSH. Describe the steps to generate a key pair, configure security groups, and connect to the instance.*
or 
Deploy Nginx on an EC2 instance, serve a static webpage, and configure it to start automatically on reboot. How do you test it and ensure the firewall rules allow access?

The Nautilus DevOps team needs to set up a new EC2 instance that can be accessed securely from their landing host (aws-client). The instance should be of type t2.micro and named datacenter-ec2. A new SSH key should be created on the aws-client host under the/root/.ssh/ folder, if it doesn't already exist. This key should then be added to the root user's authorised keys on the EC2 instance, allowing passwordless SSH access from the aws-client host.

Ans:
## PART 1: Create SSH key on `aws-client` (one-time)

On **aws-client**, as root:

```bash
mkdir -p /root/.ssh
chmod 700 /root/.ssh

ssh-keygen 
```

Copy the public key:

```bash
cat .ssh/id_rsa.pub
```

👉 **Keep this output copied** (you’ll paste it in the GUI later).

---

## PART 2: Launch EC2 instance using AWS Console (GUI)

### 1. Open EC2 Dashboard

* Log in to **AWS Console**
* Go to **EC2 → Instances**
* Click **Launch Instance**

---

### 2. Configure Instance

#### **Name**

* `datacenter-ec2`

#### **AMI**

* Amazon Linux 2 (default)

#### **Instance type**

* `t2.micro`

---

### 3. Key Pair (IMPORTANT)

* Select **Proceed without a key pair**

  > This is correct because we are injecting our own SSH key.

---

### 4. Network Settings

* Choose the correct **VPC**
* Ensure **Security Group** allows:

  * SSH (TCP 22)
  * Source: **aws-client private IP** or subnet

---

### 5. Advanced Details → User Data

Scroll to **Advanced details**
Paste the following (replace with your copied public key):

```bash
#!/bin/bash
mkdir -p /root/.ssh
chmod 700 /root/.ssh
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQ... root@aws-client" > /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys

# Enable root login
sed -i 's/^#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
systemctl restart sshd

```

📌 Example:

```bash
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQ..." >> /root/.ssh/authorized_keys
```

---

### 6. Launch Instance

Click **Launch Instance**

✅ EC2 instance `datacenter-ec2` is now running.

---

## PART 3: Verify Passwordless SSH from aws-client

1. In AWS Console:

   * Go to **EC2 → Instances**
   * Copy the **Private IP** of `datacenter-ec2`

2. From `aws-client`:

```bash
ssh -i /root/.ssh/datacenter-ec2 root@<PRIVATE_IP>
```

---

## ✅ Final Outcome

✔ EC2 instance named **datacenter-ec2**
✔ Instance type **t2.micro**
✔ SSH key created on **aws-client**
✔ Key added to **root authorized_keys** via GUI
✔ **Passwordless SSH access** from `aws-client`


**Q5: Setting Up an Application Load Balancer for an EC2 Instance**

> *You are hosting a web application on two EC2 instances in different subnets. Create an Application Load Balancer to distribute HTTP traffic across both instances.*
or 
Deploy two EC2 instances running identical apps and place them behind an Application Load Balancer. Set up a health check that uses a custom path (/health) and verify that the load balancer only routes traffic to healthy instances.
The Nautilus DevOps team is currently working on setting up a simple application on the AWS cloud. They aim to establish an Application Load Balancer (ALB) in front of an EC2 instance where an Nginx server is currently running. While the Nginx server currently serves a sample page, the team plans to deploy the actual application later.

Set up an Application Load Balancer named xfusion-alb.
Create a target group named xfusion-tg.
Create a security group named xfusion-sg to open port 80 for the public.
Attach this security group to the ALB.
The ALB should route traffic on port 80 to port 80 of the xfusion-ec2 instance.
Make appropriate changes in the default security group attached to the EC2 instance if necessary.
Ans:

Below is a **clean, practical guide** to set up the Application Load Balancer in front of your existing **xfusion-ec2** instance running Nginx.

I’ve included **AWS Console steps** (most commonly expected) and **AWS CLI commands** (optional, for automation).

---

## Architecture Overview

```
Internet
   |
[ xfusion-alb (ALB) ]
   |
[ xfusion-tg (Target Group) ]
   |
[ xfusion-ec2 (Nginx on port 80) ]
```

---

# Option 1: AWS Console (Recommended)

## 1. Create Security Group for ALB (xfusion-sg)

1. Go to **EC2 → Security Groups**
2. Click **Create security group**
3. Name: **xfusion-sg**
4. Description: Allow HTTP access to ALB
5. VPC: Same VPC as EC2

### Inbound Rules

| Type | Protocol | Port | Source    |
| ---- | -------- | ---- | --------- |
| HTTP | TCP      | 80   | 0.0.0.0/0 |

### Outbound Rules

* Allow all traffic (default)

Click **Create security group**

---

## 2. Create Target Group (xfusion-tg)

1. Go to **EC2 → Target Groups**
2. Click **Create target group**
3. Target type: **Instances**
4. Name: **xfusion-tg**
5. Protocol: **HTTP**
6. Port: **80**
7. VPC: Same VPC as EC2
8. Health check:

   * Protocol: HTTP
   * Path: `/`

Click **Next**

### Register Targets

* Select **xfusion-ec2**
* Port: **80**
* Click **Include as pending**
* Click **Create target group**

---

## 3. Create Application Load Balancer (xfusion-alb)

1. Go to **EC2 → Load Balancers**
2. Click **Create Load Balancer**
3. Choose **Application Load Balancer**

### Basic Configuration

* Name: **xfusion-alb**
* Scheme: **Internet-facing**
* IP address type: IPv4

### Network Mapping

* VPC: Same as EC2
* Select **at least two public subnets**

### Security Groups

* Remove default SG
* Attach **xfusion-sg**

### Listeners and Routing

* Listener: HTTP : 80
* Default action: Forward to **xfusion-tg**

Click **Create load balancer**

---

## 4. Update EC2 Security Group (IMPORTANT)

The EC2 instance must allow traffic **from the ALB**, not the internet.

1. Go to **EC2 → Instances**
2. Select **xfusion-ec2**
3. Click **Security → Security Groups**
4. Edit **Inbound Rules**

### Add Rule

| Type | Protocol | Port | Source     |
| ---- | -------- | ---- | ---------- |
| HTTP | TCP      | 80   | xfusion-sg |

✔ This ensures only ALB can reach the EC2 instance.

---

## 5. Validate Setup

1. Copy **ALB DNS Name**
   (EC2 → Load Balancers → xfusion-alb)
2. Open in browser:

```
http://<alb-dns-name>
```

✅ You should see the Nginx sample page.

---

# Option 2: AWS CLI (Optional)

> Assumes AWS CLI is configured and instance already exists.

### Create Security Group

```bash
aws ec2 create-security-group \
  --group-name xfusion-sg \
  --description "Allow HTTP access to ALB" \
  --vpc-id <vpc-id>

aws ec2 authorize-security-group-ingress \
  --group-name xfusion-sg \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
```

### Create Target Group

```bash
aws elbv2 create-target-group \
  --name xfusion-tg \
  --protocol HTTP \
  --port 80 \
  --vpc-id <vpc-id> \
  --target-type instance
```

### Register EC2 Instance

```bash
aws elbv2 register-targets \
  --target-group-arn <tg-arn> \
  --targets Id=<instance-id>,Port=80
```

### Create Load Balancer

```bash
aws elbv2 create-load-balancer \
  --name xfusion-alb \
  --subnets <subnet-1> <subnet-2> \
  --security-groups <xfusion-sg-id> \
  --scheme internet-facing \
  --type application
```

### Create Listener

```bash
aws elbv2 create-listener \
  --load-balancer-arn <alb-arn> \
  --protocol HTTP \
  --port 80 \
  --default-actions Type=forward,TargetGroupArn=<tg-arn>
```

---

## Final Checklist ✅

* ✔ ALB name: **xfusion-alb**
* ✔ Target group: **xfusion-tg**
* ✔ Security group: **xfusion-sg**
* ✔ Port 80 open publicly on ALB
* ✔ EC2 allows traffic from ALB SG
* ✔ Traffic routes: ALB → EC2 (port 80)

If you want, I can also:

* Add HTTPS (ACM + SSL)
* Convert this to Terraform
* Validate health check failures

**Q6: Setting Up an EC2 Instance and CloudWatch Alarm**

> *Launch an EC2 instance and configure a CloudWatch alarm that triggers if CPU utilization exceeds 70% for 5 minutes. What steps are needed to set this up?* 

or 
Your EC2-based service occasionally hits high CPU usage during batch jobs. Configure a CloudWatch alarm to trigger an SNS notification if CPU exceeds 80% for more than 3 minutes. What CloudWatch metric and threshold do you use, and how do you test the alarm?

The Nautilus DevOps team has been tasked with setting up an EC2 instance for their application. To ensure the application performs optimally, they also need to create a CloudWatch alarm to monitor the instance's CPU utilization. The alarm should trigger if the CPU utilization exceeds 90% for one consecutive 5-minute period. To send notifications, use the SNS topic named devops-sns-topic which is already created.

Launch EC2 Instance: Create an EC2 instance named devops-ec2 using any appropriate Ubuntu AMI.

Create CloudWatch Alarm: Create a CloudWatch alarm named devops-alarm with the following specifications:

Statistic: Average
Metric: CPU Utilization
Threshold: >= 90% for 1 consecutive 5-minute period.
Alarm Actions: Send a notification to devops-sns-topic.
Ans:
## Part 1: Launch EC2 Instance (GUI)
### Step 1: Open EC2 Dashboard

1. Log in to **AWS Management Console**
2. Go to **Services → EC2**
3. Click **Launch instance**

---

### Step 2: Configure EC2 Instance

1. **Name**:

   ```
   devops-ec2
   ```

2. **Application and OS Image (AMI)**

   * Select **Ubuntu Server** (20.04 or 22.04 LTS – any is fine)

3. **Instance Type**

   * Choose **t2.micro** (or any suitable type)

4. **Key Pair**

   * Select an existing key pair or create a new one

5. **Network Settings**

   * Use default VPC
   * Allow SSH (port 22) if needed

6. **Storage**

   * Keep default settings

7. Click **Launch instance**

✅ EC2 instance **devops-ec2** is now running

---

## Part 2: Create CloudWatch Alarm (GUI)

### Step 1: Open CloudWatch

1. Go to **Services → CloudWatch**
2. Click **Alarms** (left menu)
3. Click **Create alarm**

---

### Step 2: Select Metric

1. Click **Select metric**
2. Navigate to:

   ```
   EC2 → Per-Instance Metrics
   ```
3. Select your instance **devops-ec2**
4. Choose **CPUUtilization**
5. Click **Select metric**

---

### Step 3: Define Alarm Conditions

1. **Statistic**:

   * Select **Average**

2. **Period**:

   * Set to **5 minutes (300 seconds)**

3. **Threshold Type**:

   * Static

4. **Condition**:

   * **Greater/Equal**
   * **90**

5. **Evaluation Periods**:

   * **1 out of 1**

---

### Step 4: Configure Notifications

1. **Alarm state trigger**:

   * Select **In alarm**

2. **Send notification to**:

   * Choose **Select an existing SNS topic**
   * Select **devops-sns-topic**

---

### Step 5: Name & Create Alarm

1. **Alarm name**:

   ```
   devops-alarm
   ```
2. (Optional) Description:

   ```
   Alarm when CPU utilization exceeds 90% for 5 minutes
   ```
3. Click **Create alarm**

---

## ✅ Final Result

* **EC2 Instance**: `devops-ec2` (Ubuntu)
* **CloudWatch Alarm**: `devops-alarm`
* **Trigger Condition**: CPU ≥ 90% for 5 minutes
* **Notification**: SNS topic `devops-sns-topic`


**Q7: Configuring an EC2 Instance as a Web Server with Nginx**

> *You need to deploy a static website using Nginx on an EC2 instance. Set up the instance, install Nginx, and ensure it is accessible via a browser.*
The Nautilus DevOps Team is working on setting up a new web server for a critical application. The team lead has requested you to create an EC2 instance that will serve as a web server using Nginx. This instance will be part of the initial infrastructure setup for the Nautilus project. Ensuring that the server is correctly configured and accessible from the internet is crucial for the upcoming deployment phase.

As a member of the Nautilus DevOps Team, your task is to create an EC2 instance with the following specifications:

Instance Name: The EC2 instance must be named datacenter-ec2.

AMI: Use any available Ubuntu AMI to create this instance.

User Data Script: Configure the instance to run a user data script during its launch. This script should:

Install the Nginx package.
Start the Nginx service.
Security Group: Ensure that the instance allows HTTP traffic on port 80 from the internet.
Ans:
Got it! I’ll guide you through creating an **EC2 instance on AWS** with your specifications using the **AWS Management Console** (AWS Portal) approach. Here's a detailed step-by-step guide:

---

### **Step 1: Log in to AWS Management Console**

1. Open the AWS Management Console.
2. Navigate to **EC2** service.

---

### **Step 2: Launch a New EC2 Instance**

1. Click **Launch instances**.
2. **Name and tags**:

   * Instance Name: `datacenter-ec2`
3. **Application and OS Images (Amazon Machine Image, AMI)**:

   * Select **Ubuntu Server 22.04 LTS** (or the latest available Ubuntu AMI).
4. **Instance type**:

   * Choose a type like `t2.micro` (free-tier eligible if needed) or as per your project requirements.
5. Click **Next: Configure Instance Details**.

---

### **Step 3: Configure Instance**

1. Leave default settings for network/subnet unless specific VPC is required.
2. Scroll to **Advanced Details**.
3. **User Data**: Paste the following script to automatically install and start Nginx:

```bash
#!/bin/bash
sudo apt-get update -y
sudo apt-get install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

> This ensures Nginx is installed, started immediately, and enabled on boot.

---

### **Step 4: Add Storage**

* Keep default storage (e.g., 8 GB) or adjust as needed.
* Click **Next: Add Tags**.

---

### **Step 5: Add Tags**

* Add a tag for clarity (optional), e.g.,

  * Key: `Project`
  * Value: `Nautilus`

---

### **Step 6: Configure Security Group**

1. Create a **new security group** (or choose an existing one if it allows HTTP traffic).
2. Add **Inbound Rule**:

   * Type: `HTTP`
   * Protocol: `TCP`
   * Port Range: `80`
   * Source: `Anywhere (0.0.0.0/0, ::/0)` to allow internet access.
3. (Optional) Add SSH rule for admin access:

   * Type: `SSH`
   * Protocol: `TCP`
   * Port Range: `22`
   * Source: your IP (for security).

---

### **Step 7: Review and Launch**

1. Review all settings.
2. Click **Launch**.
3. Choose an existing key pair or create a new key pair to access the instance via SSH.
4. Acknowledge you have the private key, then click **Launch Instances**.

---

### **Step 8: Verify**

1. After the instance is running, get its **public IP**.
2. Open a web browser and navigate to:

   ```
   http://<public-ip>
   ```
3. You should see the default **Nginx welcome page**, confirming the server is running and accessible.

---

✅ **Result:**
You now have an EC2 instance named `datacenter-ec2`, running Ubuntu with Nginx installed, and accessible via HTTP from the internet.

### ☁️ **S3, CLI, and Data Management**

**Q8: Data Migration Between S3 Buckets Using AWS CLI**

> *You need to migrate archived logs from one S3 bucket to another in a different AWS region. Use the AWS CLI to perform this and verify the transfer.*

or 
You're migrating log files from one S3 bucket to another using AWS CLI. Use aws s3 sync to copy only new or changed files and delete old ones from the destination. How would you script this for regular runs, and what flags do you use to prevent data loss?

As part of a data migration project, the team lead has tasked the team with migrating data from an existing S3 bucket to a new S3 bucket. The existing bucket contains a substantial amount of data that must be accurately transferred to the new bucket. The team is responsible for creating the new S3 bucket and ensuring that all data from the existing bucket is copied or synced to the new bucket completely and accurately. It is imperative to perform thorough verification steps to confirm that all data has been successfully transferred to the new bucket without any loss or corruption.

As a member of the Nautilus DevOps Team, your task is to perform the following:

Create a New Private S3 Bucket: Name the bucket datacenter-sync-28616.

Data Migration: Migrate the entire data from the existing datacenter-s3-31971 bucket to the new datacenter-sync-28616 bucket.

Ensure Data Consistency: Ensure that both buckets have the same data.

Use AWS CLI: Use the AWS CLI to perform the creation and data migration tasks.
Ans:
**Confirm the Bucket Exists (Authoritative Check)**
1  aws s3 ls
2  aws s3api list-buckets
3  aws s3api head-bucket --bucket xfusion-s3-26443
**Create the bucket**
4  aws s3api create-bucket   --bucket xfusion-sync-28537   --region us-east-1
5  aws s3api head-bucket --bucket xfusion-sync-28537
**Migrate Data from Source Bucket to Destination Bucket**
6  aws s3 sync s3://xfusion-s3-26443 s3://xfusion-sync-28537
**Verify Data Consistency:**
7  aws s3 ls s3://xfusion-s3-26443 --recursive | wc -l
8  aws s3 ls s3://xfusion-sync-28537 --recursive | wc -l


### 🛢️ **RDS (Relational Database Service)**

**Q9: Configuring a Private RDS Instance for Application Development**

> *Launch a MySQL RDS instance in a private subnet that will only be accessed by EC2 instances in the same VPC. What steps ensure it remains private?*
or 
Your application requires an RDS MySQL database accessible only from within the VPC. Deploy the RDS instance in a private subnet, and ensure your EC2 app server can access it. What are the necessary security group, route table, and subnet configurations?

The Nautilus Development Team is working on a new application feature that requires a reliable and scalable database solution. To facilitate development and testing, they need a new private RDS instance. This instance will be used to store critical application data and must be provisioned using the AWS free tier to minimize costs during the initial development phase. The team has chosen MySQL as the database engine due to its compatibility with their existing systems. The DevOps team has been tasked with setting up this RDS instance, ensuring that it is correctly configured and available for use by the development team.

As a member of the Nautilus DevOps Team, your task is to perform the following:

Provision a Private RDS Instance: Create a new private RDS instance named xfusion-rds using a sandbox template, further it must be a db.t3.micro type instance.
Engine Configuration: Use the MySQL engine with version 8.4.x.
Enable Storage Autoscaling: Enable storage autoscaling and set the threshold value to 50GB. Keep the rest of the configurations as default.
Instance Availability: Ensure the instance is in the available state before submitting this task.

Ans:
Below is a **clear, DevOps-ready procedure** to provision the required **private Amazon RDS MySQL instance** using the **AWS Free Tier**, exactly as requested.

---

## ✅ Objective Summary

* **DB Identifier:** `xfusion-rds`
* **Engine:** MySQL **8.4.x**
* **Instance Class:** `db.t3.micro` (Free Tier eligible)
* **Accessibility:** **Private** (not publicly accessible)
* **Storage Autoscaling:** Enabled, max **50 GB**
* **State Required:** `Available`

---

## 🚀 Step-by-Step: Provision Private RDS Instance (AWS Console)

### 1. Open RDS Console

1. Log in to the **AWS Management Console**
2. Navigate to **Services → RDS**
3. Click **Create database**

---

### 2. Choose Database Creation Method

* Select **Standard create**

---

### 3. Engine Configuration

* **Engine type:** MySQL
* **Version:** **MySQL 8.4.x** (choose latest 8.4 available)

---

### 4. Templates

* Select **Sandbox**
  *(Optimized for development/testing and Free Tier usage)*

---

### 5. Settings

* **DB instance identifier:** `xfusion-rds`
* **Master username:** (leave default or set as required)
* **Password:** Auto-generate or set manually (store securely)

---

### 6. Instance Configuration

* **DB instance class:** `db.t3.micro`
* **Storage type:** General Purpose (gp2 or gp3 – default)
* **Allocated storage:** Default (typically 20 GB)

---

### 7. Enable Storage Autoscaling

* ✅ Check **Enable storage autoscaling**
* **Maximum storage threshold:** `50 GB`

---

### 8. Connectivity (Private Configuration)

* **VPC:** Default or project-specific VPC
* **Public access:** ❌ **No**
* **Subnet group:** Default (private subnets)
* **VPC security group:** Default or private SG allowing MySQL (3306) only from app servers
* **Availability Zone:** No preference

---

### 9. Additional Configuration

* Leave **all other settings as default**, including:

  * Backup
  * Monitoring
  * Maintenance window
  * Encryption (default)

---

### 10. Create Database

* Click **Create database**
* Wait for status to change from **Creating** → **Available**

⏳ This may take **5–10 minutes**

---

## 🔍 Final Verification Checklist

Before submitting the task, confirm:

* ✅ DB identifier is **xfusion-rds**
* ✅ Engine is **MySQL 8.4.x**
* ✅ Instance class is **db.t3.micro**
* ✅ Public accessibility is **disabled**
* ✅ Storage autoscaling enabled with **50 GB max**
* ✅ Instance status is **Available**


**Q10: Enabling Public Access to an RDS Instance**

> *Your testing team needs to connect to the RDS instance from their local machines. Reconfigure the RDS instance to allow public access securely.*
or 
For temporary testing, your QA team needs public access to an RDS instance. Modify the instance to be publicly accessible, add appropriate inbound rules, and ensure the database is not exposed to the internet unnecessarily. How do you mitigate risks?


**Q11: Snapshot and Restoration of an RDS Instance**

> *Before running a schema migration, create a manual snapshot of the RDS instance. If the migration fails, restore the database using that snapshot. Outline the full process.*

or 
A developer corrupted the staging database. Use a previously created manual snapshot to restore the RDS instance. What changes (e.g., DB identifier, endpoint) should be expected post-restoration?

The Nautilus Development Team is preparing for a major update to their database infrastructure. To ensure a smooth transition and to safeguard data, the team has requested the DevOps team to take a snapshot of the current RDS instance and restore it to a new instance. This process is crucial for testing and validation purposes before the update is rolled out to the production environment. The snapshot will serve as a backup, and the new instance will be used to verify that the backup process works correctly and that the application can function seamlessly with the restored data.

As a member of the Nautilus DevOps Team, your task is to perform the following:

Take a Snapshot: Take a snapshot of the datacenter-rds RDS instance and name it datacenter-snapshot (please wait datacenter-rds instance to be in available state).

Restore the Snapshot: Restore the snapshot to a new RDS instance named datacenter-snapshot-restore.

Configure the New RDS Instance: Ensure that the new RDS instance has a class of db.t3.micro.

Verify the New RDS Instance: The new RDS instance must be in the Available state upon completion of the restoration process.
Ans:
Below are **clear, practical steps** you can follow to complete the task exactly as requested. I’m including **both AWS Console and AWS CLI methods**—use whichever your environment allows.

---

## ✅ Prerequisites

* You must have permissions for **RDS snapshots and restore**
* Ensure **`datacenter-rds`** is in **`Available`** state before starting

---

# 🔹 Step 1: Take a Snapshot of the RDS Instance

### **Using AWS Console**

1. Open **AWS Console → RDS**
2. Click **Databases**
3. Select **`datacenter-rds`**
4. Click **Actions → Take snapshot**
5. Snapshot name:

   ```
   datacenter-snapshot
   ```
6. Click **Take snapshot**
7. Wait until snapshot status becomes **Available**

---

### **Using AWS CLI**

```bash
aws rds create-db-snapshot \
  --db-instance-identifier datacenter-rds \
  --db-snapshot-identifier datacenter-snapshot
```

Check status:

```bash
aws rds describe-db-snapshots \
  --db-snapshot-identifier datacenter-snapshot
```

---

# 🔹 Step 2: Restore Snapshot to a New RDS Instance

### **Using AWS Console**

1. Go to **RDS → Snapshots**
2. Select **`datacenter-snapshot`**
3. Click **Actions → Restore snapshot**
4. Configure:

   * **DB Instance Identifier**:

     ```
     datacenter-snapshot-restore
     ```
   * **DB Instance Class**:

     ```
     db.t3.micro
     ```
5. Keep other settings default (unless your lab specifies otherwise)
6. Click **Restore DB Instance**

---

### **Using AWS CLI**

```bash
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier datacenter-snapshot-restore \
  --db-snapshot-identifier datacenter-snapshot \
  --db-instance-class db.t3.micro
```

---

# 🔹 Step 3: Verify the New RDS Instance

### **Console Verification**

1. Go to **RDS → Databases**
2. Confirm:

   * Instance name: `datacenter-snapshot-restore`
   * Instance class: `db.t3.micro`
   * Status: **Available**

---

### **CLI Verification**

```bash
aws rds describe-db-instances \
  --db-instance-identifier datacenter-snapshot-restore
```

Look for:

```json
"DBInstanceStatus": "available",
"DBInstanceClass": "db.t3.micro"
```

---

## ✅ Final Checklist

✔ Snapshot name: **datacenter-snapshot**
✔ Restored instance name: **datacenter-snapshot-restore**
✔ Instance class: **db.t3.micro**
✔ Status: **Available**

---


### 🌐 **Networking: VPCs & Peering**

**Q12: Configuring a Public VPC with an EC2 Instance for Internet Access**

> *Design a VPC with a public subnet, Internet Gateway, and an EC2 instance that can access the internet. What components and routes are required?*
or 
Design a public VPC from scratch: create a VPC, subnet, Internet Gateway, and a route table. Launch an EC2 instance and verify internet access. What mistakes might prevent the instance from accessing the internet?

The Nautilus DevOps Team has received a request from the Networking Team to set up a new public VPC to support a set of public-facing services. This VPC will host various resources that need to be accessible over the internet. As part of this setup, you need to ensure the VPC has public subnets with automatic IP assignment for resources. Additionally, a new EC2 instance will be launched within this VPC to host public applications that require SSH access. This setup will enable the Networking Team to deploy and manage public-facing applications.

Create a public VPC named devops-pub-vpc, and a subnet named devops-pub-subnet under the same, make sure public IP is being auto assigned to resources under this subnet. Further, create an EC2 instance named devops-pub-ec2 under this VPC with instance type t2.micro. Make sure SSH port 22 is open for this instance and accessible over the internet.

Ans:

## **Step 1: Create a VPC**

1. Go to **AWS Management Console → VPC → Your VPCs → Create VPC**.
2. Select **VPC only**.
3. **Name tag**: `devops-pub-vpc`
4. **IPv4 CIDR block**: `10.0.0.0/16`
5. **Tenancy**: Default
6. Click **Create VPC**

---

## **Step 2: Create a Public Subnet**

1. Go to **Subnets → Create subnet**
2. **VPC**: `devops-pub-vpc`
3. **Subnet name**: `devops-pub-subnet`
4. **Availability Zone**: pick any (e.g., `us-east-1a`)
5. **IPv4 CIDR block**: `10.0.1.0/24`
6. Click **Create subnet**

Enable **Auto-assign public IPv4**:

1. Select the subnet → **Actions → Modify auto-assign IP settings** → check **Enable auto-assign public IPv4** → Save

---

## **Step 3: Create an Internet Gateway (IGW)**

1. Go to **Internet Gateways → Create internet gateway**
2. **Name tag**: `devops-pub-igw` → Create
3. Select your IGW → **Actions → Attach to VPC → devops-pub-vpc**

---

## **Step 4: Create a Route Table for Public Access**

1. Go to **Route Tables → Create route table**
2. **Name tag**: `devops-pub-rt`
3. **VPC**: `devops-pub-vpc` → Create

Add a route to the internet:

1. Select the route table → **Routes → Edit routes → Add route**
2. **Destination**: `0.0.0.0/0`
3. **Target**: select your Internet Gateway `devops-pub-igw` → Save

Associate the route table with the subnet:

1. **Subnet associations → Edit subnet associations → select `devops-pub-subnet` → Save**

---

## **Step 5: Create a Security Group**

1. Go to **Security Groups → Create security group**
2. **Name**: `devops-pub-sg`
3. **VPC**: `devops-pub-vpc`
4. **Inbound rule**:

   * Type: SSH
   * Protocol: TCP
   * Port: 22
   * Source: Anywhere (`0.0.0.0/0`)
5. **Outbound**: keep default (allow all) → Create

---

## **Step 6: Launch an EC2 Instance**

1. Go to **EC2 → Instances → Launch Instances**
2. **Name**: `devops-pub-ec2`
3. **AMI**: Amazon Linux 2 (or your preferred AMI)
4. **Instance type**: `t2.micro`
5. **Key pair**: select or create a key pair for SSH
6. **Network settings**:

   * VPC: `devops-pub-vpc`
   * Subnet: `devops-pub-subnet`
   * Auto-assign Public IP: **Enable**
   * Security group: `devops-pub-sg` (SSH allowed)
7. Click **Launch instance**

---

✅ **Result**:

* Public VPC: `devops-pub-vpc`
* Public Subnet: `devops-pub-subnet` (auto-assign IP)
* Internet Gateway: `devops-pub-igw`
* Route table: `devops-pub-rt` → routes 0.0.0.0/0 to IGW
* EC2 instance: `devops-pub-ec2` (SSH accessible over the internet)



**Q13: Establishing Secure Communication Between Public and Private VPCs via VPC Peering**

> *You have two VPCs (one public-facing, one private for backend services). Establish a VPC peering connection to allow secure communication between them.*
or 
Your app is split across two VPCs (frontend/backend). Set up VPC peering and route table entries to enable communication between the instances in both VPCs. How do you test the connection and enforce security using security groups?

The Nautilus DevOps team has been tasked with demonstrating the use of VPC Peering to enable communication between two VPCs. One VPC will be a private VPC that contains a private EC2 instance, while the other will be the default public VPC containing a publicly accessible EC2 instance.

1) There is already an existing EC2 instance in the public vpc/subnet:

Name: devops-public-ec2
2) There is already an existing Private VPC:

Name: devops-private-vpc
CIDR: 10.1.0.0/16
3) There is already an existing Subnet in devops-private-vpc:

Name: devops-private-subnet
CIDR: 10.1.1.0/24
4) There is already an existing EC2 instance in the private subnet:

Name: devops-private-ec2
5) Create a Peering Connection between the Default VPC and the Private VPC:

VPC Peering Connection Name: devops-vpc-peering
6) Configure Route Tables to enable communication between the two VPCs.

Ensure the private EC2 instance is accessible from the public EC2 instance.
7) Test the Connection:

Add /root/.ssh/id_rsa.pub public key to the public EC2 instance's ec2-user's authorized_keys to make sure we are able to ssh into this instance from AWS client host. You may also need to update the security group of the private EC2 instance to allow ICMP traffic from the public/default VPC CIDR. This will enable you to ping the private instance from the public instance.
SSH into the public EC2 instance and ensure that you can ping the private EC2 instance.
Ans:
Below is a **clear, step-by-step guide** to complete the VPC Peering demo exactly as described. You can do this from the **AWS Console** (recommended for a demo), with optional **CLI equivalents** where useful.

---

## Architecture Goal (Quick Recap)

* **Default VPC (Public)**

  * EC2: `devops-public-ec2`
* **Private VPC**

  * VPC: `devops-private-vpc` (10.1.0.0/16)
  * Subnet: `devops-private-subnet` (10.1.1.0/24)
  * EC2: `devops-private-ec2`
* **Connectivity**: VPC Peering + route tables + security groups
* **Test**: SSH → Public EC2 → Ping Private EC2

---

## 1️⃣ Create VPC Peering Connection

### AWS Console

1. Go to **VPC → Peering connections**
2. Click **Create peering connection**
3. Configure:

   * **Name**: `devops-vpc-peering`
   * **VPC (Requester)**: **Default VPC**
   * **VPC (Accepter)**: `devops-private-vpc`
4. Click **Create peering connection**
5. Select the peering connection → **Actions → Accept request**

✅ Status should now be **Active**

---

## 2️⃣ Update Route Tables

### A) Default VPC Route Table

1. Go to **VPC → Route Tables**
2. Identify the route table associated with the **public subnet** of `devops-public-ec2`
3. Edit **Routes** → **Add route**

   * **Destination**: `10.1.0.0/16`
   * **Target**: `devops-vpc-peering`
4. Save changes

---

### B) Private VPC Route Table

1. Locate the route table associated with:

   * `devops-private-vpc`
   * Subnet: `devops-private-subnet`
2. Edit **Routes** → **Add route**

   * **Destination**: **Default VPC CIDR** (usually `172.31.0.0/16`)
   * **Target**: `devops-vpc-peering`
3. Save changes

---

## 3️⃣ Update Security Groups

### A) Private EC2 Security Group

1. Go to **EC2 → Security Groups**
2. Open the security group attached to `devops-private-ec2`
3. Add **Inbound Rules**:

   * **ICMP – Echo Request**

     * Source: **Default VPC CIDR** (e.g., `172.31.0.0/16`)
   * **SSH**

     * Source: **Default VPC CIDR**

> This allows ping + SSH traffic from the public EC2

---

### B) Public EC2 Security Group

Ensure it allows:

* **SSH (22)** from your AWS client host IP (or `0.0.0.0/0` for demo)

---

## 4️⃣ Add SSH Key to Public EC2

From your **AWS client host**:

```bash
ssh ec2-user@<PUBLIC_EC2_PUBLIC_IP>
```

On the **public EC2**:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
```

Append your key:

```bash
echo "<contents-of-/root/.ssh/id_rsa.pub>" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

---

## 5️⃣ Test Connectivity

### A) SSH into Public EC2

```bash
ssh ec2-user@<PUBLIC_EC2_PUBLIC_IP>
```

---

### B) Ping Private EC2

1. Get the **private IP** of `devops-private-ec2` (e.g., `10.1.1.10`)
2. From **public EC2**:

```bash
ping 10.1.1.10
```

✅ **Successful replies confirm VPC Peering works**

---

## 6️⃣ (Optional) SSH from Public EC2 to Private EC2

If SSH keys are shared:

```bash
ssh ec2-user@10.1.1.10
```

---

## ✅ Final Validation Checklist

✔ VPC Peering is **Active**
✔ Routes added on **both sides**
✔ Security groups allow ICMP + SSH
✔ Public EC2 can **ping private EC2**


**Q14: Setting Up a Private VPC with an Isolated EC2 Instance**

> *Create a VPC with a private subnet and launch an EC2 instance inside it. Ensure it has **no internet access**, and explain how you verify its isolation.*


### ⚙️ **Serverless: Lambda**

**Q15: Create a Lambda Function**

> *Write a simple Lambda function in Python that logs “Hello from Lambda!” to CloudWatch. Create and test it using the AWS Console.*
or 
Create a Lambda function triggered when new files are uploaded to an S3 bucket. The function should log the filename and timestamp. What permissions do you need to configure on the bucket and Lambda role?

The Nautilus DevOps team is embracing serverless architecture by integrating AWS Lambda into their operational tasks. They have decided to deploy a simple Lambda function that will return a custom greeting to demonstrate serverless capabilities effectively. This function is crucial for showcasing rapid deployment and easy scalability features of AWS Lambda to the team.

Create Lambda Function: Create a Lambda function named devops-lambda.

Runtime: Use the Runtime Python.

Deploy: The function should print the body Welcome to KKE AWS Labs!.

Status Code: Ensure the status code is 200.

IAM Role: Create and use the IAM role named lambda_execution_role.

Use the AWS Console to complete this task.
Ans:
To deploy the AWS Lambda function as described, follow these steps using the **AWS Management Console**:

### 1. **Create IAM Role for Lambda Execution**

Before creating the Lambda function, you need to create an IAM role that grants the function the necessary permissions.

#### Step 1: Create IAM Role

1. **Log in to the AWS Management Console**.
2. Navigate to **IAM** by searching for "IAM" in the AWS Management Console.
3. In the left-hand sidebar, click on **Roles**.
4. Click the **Create role** button.
5. Choose **Lambda** as the trusted entity type.
6. Click **Next: Permissions** (you don’t need to add permissions for this specific function since it’s a basic Lambda function).
7. Click **Next: Tags** and then **Next: Review**.
8. Name the role **lambda_execution_role**.
9. Click **Create role**.

### 2. **Create the Lambda Function**

#### Step 2: Create Lambda Function

1. **Navigate to Lambda** by searching for "Lambda" in the AWS Management Console.
2. On the Lambda dashboard, click the **Create function** button.
3. Select **Author from scratch**.
4. Set the **Function name** to `devops-lambda`.
5. Choose **Python 3.x** as the runtime (Python 3.8 or later should work).
6. Under **Permissions**, select **Choose an existing role** and choose the IAM role you created earlier: `lambda_execution_role`.
7. Click **Create function**.

#### Step 3: Configure the Lambda Function

1. On the Lambda function configuration page, scroll to the **Function code** section.
2. In the **Code source** editor, add the following Python code:

```python
import json

def lambda_handler(event, context):
    # Printing the message to the logs
    print("Welcome to KKE AWS Labs!")
    
    # Returning a response with status code 200
    return {
        'statusCode': 200,
        'body': json.dumps('Welcome to KKE AWS Labs!')
    }
```

3. **Save or deploy** the Lambda function.

### 3. **Test the Lambda Function**

#### Step 4: Create a Test Event

1. On the Lambda function page, click on the **Test** button.
2. In the **Configure test event** pop-up, name the test event (e.g., `testEvent`).
3. For simplicity, you can leave the event data as the default (empty JSON `{}`).
4. Click **Save changes** and then click **Test**.

#### Step 5: Verify Output

1. After clicking **Test**, AWS Lambda will execute your function.
2. In the **Execution results** section, verify that the status code is `200` and that the body contains the message `"Welcome to KKE AWS Labs!"`.

---

### Summary of the Lambda Function:

* **Function Name**: `devops-lambda`
* **Runtime**: Python 3.x
* **IAM Role**: `lambda_execution_role`
* **Code**: Prints a greeting and returns a 200 status code with the message in the body.

This Lambda function now showcases how to deploy a serverless function on AWS Lambda, and it can be scaled effortlessly in the future if needed.


**Q16: Create a Lambda Function Using CLI**

> *Use the AWS CLI to deploy a Lambda function from a local zip file. The function should return the current timestamp when triggered.*
or 

Package a Python script into a zip file and deploy it to AWS Lambda using CLI. What CLI commands are needed, and how do you test the function after deployment?

The Nautilus DevOps team continues to explore serverless architecture by setting up another Lambda function. This time, the task must be completed using the AWS Console to familiarize the team with the web interface. The function will return a custom greeting and demonstrate the capabilities of AWS Lambda effectively.

Create Python Script: Create a Python script named lambda_function.py with a function that returns the body Welcome to KKE AWS Labs! and status code 200.

Zip the Python Script: Zip the script into a file named function.zip.

Create Lambda Function: Create a Lambda function named devops-lambda-cli using the zipped file and specify Python as the runtime.

IAM Role: Use the IAM role named lambda_execution_role.

Use AWS CLI which is already configured on the aws-client host.
Ans:
Below are **clear, step-by-step instructions** to complete this task **using the AWS CLI on the aws-client host**, exactly as requested.

---

## Step 1: Create the Python Script

On the **aws-client host**, create a file named **`lambda_function.py`**.

```bash
vi lambda_function.py
```

Add the following content:

```python
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Welcome to KKE AWS Labs!"
    }
```

Save and exit the file.

---

## Step 2: Zip the Python Script

Create a deployment package named **`function.zip`**.

```bash
zip function.zip lambda_function.py
```

Verify the zip file exists:

```bash
ls
```

You should see:

```
function.zip
lambda_function.py
```

---

## Step 3: Create the Lambda Function Using AWS CLI

Run the following command to create the Lambda function:

```bash
aws lambda create-function \
  --function-name devops-lambda-cli \
  --runtime python3.9 \
  --role arn:aws:iam::<ACCOUNT_ID>(08947-xxxxxxx):role/lambda_execution_role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip
```

### 🔴 Important

Replace `<ACCOUNT_ID>` with your actual AWS account ID.
You can get aacound id using:

```bash
aws sts get-caller-identity
Ex:
{
    "UserId": "AIDARJVIXVM3M3QRQ37HM",
    "Account": "08947-xxxxxxx",
    "Arn": "arn:aws:iam::08947xxxxxxx:user/kk_labs_user_810831"
}
```

---

## Step 4: Verify Lambda Function Creation

Check that the function was created successfully:

```bash
aws lambda get-function --function-name devops-lambda-cli
```

---

## Step 5: Test the Lambda Function (Optional but Recommended)

Invoke the Lambda function:

```bash
aws lambda invoke \
  --function-name devops-lambda-cli \
  response.json
```

View the output:

```bash
cat response.json
```

Expected output:

```json
{
  "statusCode": 200,
  "body": "Welcome to KKE AWS Labs!"
}
```

---

## ✅ Final Summary

| Item                 | Value                    |
| -------------------- | ------------------------ |
| Script Name          | `lambda_function.py`     |
| Zip File             | `function.zip`           |
| Lambda Function Name | `devops-lambda-cli`      |
| Runtime              | Python 3.9               |
| IAM Role             | `lambda_execution_role`  |
| Status Code          | 200                      |
| Response Body        | Welcome to KKE AWS Labs! |


### 🛠️ **Troubleshooting & NAT Gateway**

**Q17: Troubleshooting Internet Accessibility for an EC2-Hosted Application**

> *You launched an EC2 instance in a public subnet, but your web app isn’t accessible via browser. Identify and resolve the issue by checking networking, security group, and route settings.*
or 
You deployed a Node.js app on EC2, but it’s not reachable from the internet. What components would you check (e.g., security groups, routes, app bindings), and how would you debug this step by step?
**Q18: Troubleshooting Connectivity Issues for Package Installation on EC2**

> *Your EC2 instance cannot install packages via `yum` or `apt`. It’s in a private subnet. Diagnose and fix the problem to restore internet access.*
or 
An EC2 instance in a private subnet fails to install software updates. Explain how to diagnose whether it's a DNS, NAT, or routing issue and how to fix it so the instance can access the internet safely.

The Nautilus Development Team recently deployed a new web application hosted on an EC2 instance within a public VPC named datacenter-vpc. The application, running on an Nginx server, should be accessible from the internet on port 80. Despite configuring the security group datacenter-sg to allow traffic on port 80 and verifying the EC2 instance settings, the application remains inaccessible from the internet. The team suspects that the issue might be related to the VPC configuration, as all other components appear to be set up correctly. The DevOps team has been asked to troubleshoot and resolve the issue to ensure the application is accessible to external users.

As a member of the Nautilus DevOps Team, your task is to perform the following:

Verify VPC Configuration: Ensure that the VPC datacenter-vpc is properly configured to allow internet access.

Ensure Accessibility: Make sure the EC2 instance datacenter-ec2 running the Nginx server is accessible from the internet on port 80.
Ans:
Here’s how to systematically troubleshoot and fix this issue in AWS. Since the security group and EC2 instance look correct, the most common cause is a **missing or incorrect VPC networking component**.

---

## 1. Verify VPC Internet Connectivity (datacenter-vpc)

For an EC2 instance to be reachable from the internet, **all** of the following must be true:

### ✅ 1. Internet Gateway (IGW) Attached

* Go to **VPC → Internet Gateways**
* Confirm an Internet Gateway exists and is **attached to `datacenter-vpc`**
* If not:

  * Create an IGW
  * Attach it to `datacenter-vpc`

---

### ✅ 2. Route Table Has a Default Route to the IGW

* Go to **VPC → Route Tables**
* Find the route table associated with the EC2 subnet
* Ensure it has this route:

```
Destination: 0.0.0.0/0
Target: igw-xxxxxxxx
```

* If missing, add the route
* Confirm this route table is **associated with the EC2’s subnet**

👉 Without this route, the subnet is **not public**, even if the VPC is.

---

### ✅ 3. Subnet Is Public

A subnet is considered public only if:

* It is associated with a route table that routes `0.0.0.0/0` to an IGW

Double-check:

* **Subnet → Route Table association**

---

## 2. Verify EC2 Internet Accessibility (datacenter-ec2)

### ✅ 4. EC2 Instance Has a Public IP

* Go to **EC2 → Instances → datacenter-ec2**
* Confirm it has:

  * A **Public IPv4 address**, or
  * An **Elastic IP** attached

❗ If there is no public IP:

* Allocate and attach an Elastic IP
* OR redeploy the instance with “Auto-assign Public IP” enabled

---

### ✅ 5. Network ACL Allows HTTP Traffic

Check the subnet’s **Network ACL**:

**Inbound rules must allow:**

```
Port: 80
Protocol: TCP
Source: 0.0.0.0/0
Action: ALLOW
```

**Outbound rules must allow:**

```
Port range: 1024–65535 (or ALL)
Destination: 0.0.0.0/0
Action: ALLOW
```

(Network ACLs are stateless, so both directions matter.)

---

## 3. Final EC2-Level Checks (Quick Validation)

Since you mentioned instance settings look good, just confirm:

* Nginx is running and listening on port 80:

  ```bash
  sudo systemctl status nginx
  ```
* The OS firewall (iptables/firewalld) is not blocking port 80
* Nginx is bound to `0.0.0.0:80`, not `127.0.0.1`

---

## ✅ Most Likely Root Cause (Based on Experience)

In cases like this, the issue is almost always one of these:

* No Internet Gateway attached to the VPC
* Missing `0.0.0.0/0 → IGW` route
* Subnet not associated with the correct route table
* EC2 instance does not have a public IP

Fixing these will make the Nginx application accessible from the internet on port 80.




### 📦 **ECR & Container Management**

**Q19: Creating a Private ECR Repository**

> *You’re preparing a CI/CD pipeline and need a private container registry. Create a private Amazon ECR repository and push a Docker image to it.*

or
Create a private ECR repository, build a Docker image locally, and push it to the ECR repo. What authentication steps are required, and how do you allow ECS or EC2 instances to pull this image?

The Nautilus DevOps team has been tasked with setting up a containerized application. They need to create a private Amazon Elastic Container Registry (ECR) repository to store their Docker images. Once the repository is created, they will build a Docker image from a Dockerfile located on the aws-client host and push this image to the ECR repository. This process is essential for maintaining and deploying containerized applications in a streamlined manner.

Create a private ECR repository named xfusion-ecr. There is a Dockerfile under /root/pyapp directory on aws-client host, build a docker image using this Dockerfile and push the same to the newly created ECR repo, the image tag must be latest.
Ans:
Below is a **GUI-first walkthrough** with the **exact CLI commands** you’ll run on the `aws-client` host to build and push the image.

---

## Part 1: Create a Private ECR Repository (AWS GUI)

1. **Log in to AWS Management Console**
2. Go to **Services → Elastic Container Registry (ECR)**
3. Click **Repositories** (left sidebar)
4. Click **Create repository**

### Repository settings

* **Visibility settings**: ✅ *Private*
* **Repository name**:

  ```
  xfusion-ecr
  ```
* Leave other settings as default

5. Click **Create repository**

📌 Once created, note:

* **AWS Region** (top-right of console)
* **Repository URI**
  Example format:

  ```
  <account-id>.dkr.ecr.<region>.amazonaws.com/xfusion-ecr
  ```

---

## Part 2: Authenticate Docker to ECR (aws-client host)

Log in to the `aws-client` host and run:

```bash
aws ecr get-login-password --region <region> \
| docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
```

✅ You should see:

```
Login Succeeded
```

---

## Part 3: Build Docker Image from Dockerfile

1. Go to the directory containing the Dockerfile:

```bash
cd /root/pyapp
```

2. Build the Docker image:

```bash
docker build -t xfusion-ecr:latest .
```

---

## Part 4: Tag the Image for ECR

Tag the image using the ECR repository URI:

```bash
docker tag xfusion-ecr:latest <account-id>.dkr.ecr.<region>.amazonaws.com/xfusion-ecr:latest
```

---

## Part 5: Push Image to ECR

```bash
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/xfusion-ecr:latest
```

Wait until the push completes successfully.

---

## Part 6: Verify in AWS GUI

1. Go back to **ECR → Repositories**
2. Click **xfusion-ecr**
3. Open the **Images** tab

✅ You should see:

* **Tag**: `latest`
* **Image status**: Available


### 🌐 **NAT Gateway**

**Q20: Configure NAT Gateway for Internet Access in a Private VPC**

> *You need to allow EC2 instances in a private subnet to access the internet (e.g., for updates). Configure a NAT Gateway and update routing accordingly.*

or 
Your EC2 instance in a private subnet needs to access the internet for updates and package downloads. Create a NAT Gateway in a public subnet and modify the route tables. How do you ensure only outgoing traffic is allowed?

**Level 3**
Here is a set of **Advanced-Level Scenario-Based Questions** based on your provided topics. These questions are designed to test deep understanding, cross-service integration, architecture design, automation, scalability, and security—making them ideal for advanced learners, cloud architects, or senior DevOps/Cloud Engineers preparing for real-world projects or advanced certifications (e.g., AWS Solutions Architect Professional, DevOps Pro).



### 🚀 **Q1: Deploying and Managing Applications on AWS**

> *You’re leading the migration of a monolithic application to AWS. The app consists of a backend API, frontend UI, and a relational database. How would you design a resilient, scalable architecture using AWS services like EC2, RDS, Auto Scaling, and Route 53? How would you manage secrets and deploy updates with minimal downtime?*

The Nautilus DevOps team needs a new private RDS instance for their application. They need to set up a MySQL database and ensure that their existing EC2 instance can connect to it. This will help in managing their database needs efficiently and securely.

1) Task Details:

Create a private RDS instance named xfusion-rds using a sandbox template.
The engine type must be MySQL v8.4.5, and it must be a db.t3.micro type instance.
The master username must be xfusion_admin with an appropriate password.
The RDS storage type must be gp2, and the storage size must be 5GiB.
Create a database named xfusion_db.
Keep the rest of the configurations as default. Ensure the instance is in available state.
Adjust the security groups so that the xfusion-ec2 instance can connect to the RDS on port 3306 and also open port 80 for the instance.
2) An EC2 instance named xfusion-ec2 exists. Connect to this instance from the AWS console. Create an SSH key (/root/.ssh/id_rsa) on the aws-client host if it doesn't already exist. Add the public key to the authorized keys of the root user on the EC2 instance for password-less SSH access.

3) There is a file named index.php under the /root directory on the aws-client host. Copy this file to the xfusion-ec2 instance under the /var/www/html/ directory. Make the appropriate changes in the file to connect to the RDS.

4) You should see a Connected successfully message in the browser once you access the instance using the public IP.

Ans:
To help you set up and configure your AWS RDS and EC2 environment, I've broken down the process into clear, manageable steps.

### Step 1: Create the RDS Instance

1. Log in to the **AWS RDS Console**.
2. Click **Create database**.
3. Choose **Standard create**.
4. **Engine options:** Select **MySQL** and set the version to **8.0.35** (Note: AWS versions update frequently; choose the closest available 8.0/8.4 version if 8.4.5 is not listed).
5. **Templates:** Select **Free Tier** or **Dev/Test** (since "sandbox" refers to the environment type).
6. **Settings:**
* DB instance identifier: `datacenter-rds`
* Master username: `datacenter_admin`
* Master password: [Set a secure password]


7. **Instance configuration:** Choose **db.t3.micro**.
8. **Storage:**
* Storage type: **General Purpose SSD (gp2)**.
* Allocated storage: **5 GiB** (This is usually the minimum for RDS; if the lab allows 5GiB, use that, but 20GiB is the standard AWS minimum).


9. **Connectivity:** Ensure **Public access** is set to **No**.
10. **Additional configuration:** Under **Initial database name**, enter `datacenter_db`.
11. Click **Create database** and wait for the status to become **Available**.

### Step 2: Configure Security Groups

1. Go to the **EC2 Console** > **Security Groups**.
2. **RDS Security Group:** Add an **Inbound Rule**.
* Type: **MySQL/Aurora (3306)**.
* Source: Select the Security Group ID of the `datacenter-ec2` instance.


3. **EC2 Security Group:** Add an **Inbound Rule**.
* Type: **HTTP (80)**.
* Source: **Anywhere (0.0.0.0/0)**.



### Step 3: Set up SSH Access

On the `aws-client` host:

1. Check for an existing key: `ls /root/.ssh/id_rsa`.
2. If it doesn't exist, generate one: `ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa`.
3. Copy the public key: `cat /root/.ssh/id_rsa.pub`.
4. SSH into `datacenter-ec2` (using the password/key provided by your lab) and append that string to `/root/.ssh/authorized_keys`.
# Enable root login
sed -i 's/^#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
systemctl restart sshd
### Step 4: Deploy and Configure the PHP Application

1. **Copy the file:** ```bash
scp /root/index.php root@<EC2_Pulic_IP>:/var/www/html/
```
### 1. Install PHP and MySQL Extensions

On Ubuntu, Apache does not automatically process PHP unless the module is installed.

```bash
sudo apt update
sudo apt install php libapache2-mod-php php-mysql -y

```

### 2. Prioritize PHP over HTML

By default, Ubuntu's Apache is configured to look for `index.html` before `index.php`. You have two choices:

* **Option A (Recommended):** Delete the default HTML file so Apache has no choice but to use your PHP file.
```bash
sudo rm /var/www/html/index.html

```


* **Option B:** Edit the configuration to prioritize PHP.
```bash
sudo nano /etc/apache2/mods-enabled/dir.conf

```


Move `index.php` to the beginning of the list, then save and exit.

### 3. Permissions and Ownership

Since you moved the file as `root` using `scp`, the web server user (`www-data`) needs permission to read it.

```bash
sudo chown www-data:www-data /var/www/html/index.php
sudo chmod 644 /var/www/html/index.php

```
### 4. Restart Apache

Always restart the service after installing modules or changing configurations.

```bash
sudo systemctl restart apache2

```
2. **Edit the file:** SSH into the `datacenter-ec2` and edit `/var/www/html/index.php`. Update the following variables:
* `$servername` = [The Endpoint found in the RDS console]
* `$username` = `datacenter_admin`
* `$password` = [Your password]
* `$dbname` = `datacenter_db`


3. **Verify:** Open your browser and navigate to `http://<EC2_Public_IP>/index.php`. You should see the **"Connected successfully"** message.

### ⚖️ **Q2: Load Balancing EC2 Instances with Application Load Balancer**

> *You’re running multiple EC2 instances across two Availability Zones hosting microservices. Configure an Application Load Balancer that routes traffic based on path (`/api`, `/admin`, etc.). How would you implement sticky sessions, enable HTTPS with SSL certificates, and configure health checks for each target group?*

The Nautilus Development Team needs to set up a new EC2 instance and configure it to run a web server. This EC2 instance should be part of an Application Load Balancer (ALB) setup to ensure high availability and better traffic management. The task involves creating an EC2 instance, setting up an ALB, configuring a target group, and ensuring the web server is accessible via the ALB DNS.

Create a security group: Create a security group named xfusion-sg to open port 80 for the default security group (which will be attached to the ALB). Attach xfusion-sg security group to the EC2 instance.

Create an EC2 instance: Create an EC2 instance named xfusion-ec2. Use any available Ubuntu AMI to create this instance. Configure the instance to run a user data script during its launch.

This script should:

Install the Nginx package.
Start the Nginx service.
Set up an Application Load Balancer: Set up an Application Load Balancer named xfusion-alb. Attach default security group to the same.

Create a target group: Create a target group named xfusion-tg.

Route traffic: The ALB should route traffic on port 80 to port 80 of the xfusion-ec2 instance.

Security group adjustments: Make appropriate changes in the default security group attached to the ALB if necessary. Eventually, the Nginx server running under xfusion-ec2 instance must be accessible using the ALB DNS.

Ans:

Here’s a **step-by-step guide** to set up the requested AWS infrastructure for the Nautilus Development Team:

---

## 🔐 Step 1: Create Security Group
- **Name:** `xfusion-sg`
- **Inbound Rule:**
  - Protocol: TCP
  - Port: 80
  - Source: Default security group (attached to ALB)
- **Outbound Rule:** Allow all traffic (default).
- Attach `xfusion-sg` to the EC2 instance.

---

## 🖥️ Step 2: Launch EC2 Instance
- **Name:** `xfusion-ec2`
- **AMI:** Any Ubuntu AMI (e.g., Ubuntu Server 22.04 LTS).
- **Instance Type:** t2.micro (or any suitable type).
- **Security Group:** Attach `xfusion-sg`.
- **User Data Script:**

```bash
#!/bin/bash
# Update packages
apt-get update -y

# Install Nginx
apt-get install nginx -y

# Start Nginx service
systemctl start nginx
systemctl enable nginx

# Simple index page
echo "<h1>Welcome to xfusion-ec2 via ALB</h1>" > /var/www/html/index.html
```

This ensures Nginx is installed, started, and serving a test page.

---

## ⚖️ Step 3: Create Application Load Balancer (ALB)
- **Name:** `xfusion-alb`
- **Type:** Internet-facing, HTTP (port 80).
- **Security Group:** Attach the **default security group**.
- **Listeners:** HTTP on port 80.

---

## 🎯 Step 4: Create Target Group
- **Name:** `xfusion-tg`
- **Target Type:** Instance
- **Protocol:** HTTP
- **Port:** 80
- **Health Check:** HTTP, path `/`
- Register `xfusion-ec2` instance in this target group.

---

## 🔄 Step 5: Route Traffic
- In the ALB configuration:
  - Add a listener rule to forward traffic from port 80 → `xfusion-tg`.
- Ensure the **default security group** attached to ALB allows **inbound traffic on port 80 from 0.0.0.0/0** (public access).

---

## ✅ Step 6: Verify Setup
1. Get the **DNS name** of `xfusion-alb` from the AWS console.
2. Open it in a browser:  
   `http://<ALB-DNS-NAME>`
3. You should see:  
   **“Welcome to xfusion-ec2 via ALB”**

### 🔐 **Q3: Managing EC2 Access with S3 Role-Based Permissions**

> *Your EC2 instance processes data from multiple S3 buckets. You want to avoid using static credentials. Create an IAM role with fine-grained permissions that allows read-only access to `bucket-A` and full access to `bucket-B`. Attach the role to the instance and validate access using the AWS CLI. How would you audit and rotate permissions securely?*

The Nautilus DevOps team needs to set up an application on an EC2 instance to interact with an S3 bucket for storing and retrieving data. To achieve this, the team must create a private S3 bucket, set appropriate IAM policies and roles, and test the application functionality.

Task:
1) EC2 Instance Setup:

An instance named devops-ec2 already exists.
The instance requires access to an S3 bucket.
2) Setup SSH Keys:

Create new SSH key pair (id_rsa and id_rsa.pub) on the aws-client host and add the public key to the root user's authorized keys on the EC2 instance.
3) Create a Private S3 Bucket:

Name the bucket devops-s3-14845.
Ensure the bucket is private.
4) Create an IAM Policy and Role:

Create an IAM policy allowing s3:PutObject, s3:ListBucket and s3:GetObject access to devops-s3-14845.
Create an IAM role named devops-role.
Attach the policy to the IAM role.
Attach this role to the devops-ec2 instance.
5) Test the Access:

SSH into the EC2 instance and try to upload a file to devops-s3-14845 bucket using following command:
aws s3 cp <your-file> s3://devops-s3-14845/

Now run following command to list the upload file:
aws s3 ls s3://devops-s3-14845/

Ans:
Below are **AWS Management Console (GUI) steps** to complete the entire task.

---

## 1️⃣ EC2 Instance (Verify)

1. Open **AWS Console → EC2**
2. Go to **Instances**
3. Confirm instance **`devops-ec2`** is **running**

---

## 2️⃣ Setup SSH Keys (GUI + CLI mix)

### 🔹 Generate SSH keys (on aws-client host)

```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""
```

### 🔹 Add public key to EC2 (GUI-assisted)

1. Open **EC2 → Instances**
2. Select **devops-ec2**
3. Note **Public IP**
4. SSH once using existing access
5. On EC2:

```bash
mkdir -p /root/.ssh
vi /root/.ssh/authorized_keys
```

6. Paste contents of `id_rsa.pub`
7. Save and exit

---

## 3️⃣ Create Private S3 Bucket (GUI)

1. Open **AWS Console → S3**
2. Click **Create bucket**
3. Bucket name: **`devops-s3-14845`**
4. AWS Region: same as EC2
5. **Block all public access** → ✔️ Enabled
6. Click **Create bucket**

✅ Bucket is private by default

---

## 4️⃣ Create IAM Policy (GUI)

1. Open **IAM → Policies**
2. Click **Create policy**
3. Select **JSON tab**
4. Paste:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::devops-s3-14845"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::devops-s3-14845/*"
    }
  ]
}
```

5. Click **Next**
6. Policy name: **devops-s3-policy**
7. Click **Create policy**

---

## 5️⃣ Create IAM Role (GUI)

1. Go to **IAM → Roles**
2. Click **Create role**
3. Select **AWS service**
4. Choose **EC2**
5. Click **Next**
6. Search and select **devops-s3-policy**
7. Click **Next**
8. Role name: **devops-role**
9. Click **Create role**

---

## 6️⃣ Attach IAM Role to EC2 (GUI)

1. Go to **EC2 → Instances**
2. Select **devops-ec2**
3. Click **Actions → Security → Modify IAM role**
4. Select **devops-role**
5. Click **Update IAM role**

⏳ Wait 30–60 seconds

---

## 7️⃣ Test S3 Access from EC2 (GUI + CLI)

### 🔹 SSH into EC2

```bash
ssh root@<EC2_PUBLIC_IP>
```

### 🔹 Create test file

```bash
echo "S3 GUI test" > test.txt
```

### 🔹 Upload file

```bash
aws s3 cp test.txt s3://devops-s3-14845/
```

### 🔹 List files

```bash
aws s3 ls s3://devops-s3-14845/
```

✅ File should be visible

---

## ✅ Final Confirmation

✔ EC2 connected via IAM Role
✔ Private S3 bucket
✔ No access keys used
✔ Upload & list successful

### 🐳 **Q4: Deploying Containerized Applications with Amazon ECS**

> *You’re deploying a containerized Node.js app using Amazon ECS with Fargate. Create a multi-container task definition with app and logging sidecar. Configure the service with an ALB for public access, enable autoscaling based on CPU utilization, and ensure secure secret injection using AWS Secrets Manager. How would you handle zero-downtime deployments and rollback strategies?*

The Nautilus DevOps team is tasked with deploying a containerized application using Amazon's container services. They need to create a private Amazon Elastic Container Registry (ECR) to store their Docker images and use Amazon Elastic Container Service (ECS) to deploy the application. The process involves building a Docker image from a given Dockerfile, pushing it to the ECR, and then setting up an ECS cluster to run the application.

Create a Private ECR Repository:

Create a private ECR repository named nautilus-ecr to store Docker images.
Build and Push Docker Image:

Use the Dockerfile located at /root/pyapp on the aws-client host.
Build a Docker image using this Dockerfile.
Tag the image with latest tag.
Push the Docker image to the nautilus-ecr repository.
Create and Configure ECS cluster:

Create an ECS cluster named nautilus-cluster using the Fargate launch type.
Create an ECS Task Definition:

Define a task named nautilus-taskdefinition using the Docker image from the nautilus-ecr ECR repository.
Specify necessary CPU and memory resources.
Deploy the Application Using ECS Service:

Create a service named nautilus-service on the nautilus-cluster to run the task.
Ensure the service runs at least one task.
Ans:
Got it — you want the **GUI (AWS Management Console) steps** 👍
Below is the **same workflow**, but done entirely through the **AWS Console**, not CLI.

---

## 1️⃣ Create a Private ECR Repository (GUI)

1. Open **AWS Management Console**
2. Go to **Amazon ECR**
3. Click **Repositories → Create repository**
4. Select:

   * **Visibility:** Private
   * **Repository name:** `nautilus-ecr`
5. Leave defaults
6. Click **Create repository**

✅ Copy the **Repository URI** (you’ll need it later)

---

## 2️⃣ Build & Push Docker Image (Local, Still Required)

⚠️ Docker build/push **cannot be done fully in GUI** — this part must be done on the `aws-client` host.

From GUI:

1. Open the repository
2. Click **View push commands**
3. Follow the provided steps:

   * Authenticate Docker
   * Build image from `/root/pyapp`
   * Tag image as `latest`
   * Push to ECR

Once pushed, you’ll see the image in the repository.

---

## 3️⃣ Create ECS Cluster (Fargate)

1. Go to **Amazon ECS**
2. Click **Clusters → Create cluster**
3. Select:

   * **Cluster name:** `nautilus-cluster`
   * **Infrastructure:** AWS Fargate (Serverless)
4. Click **Create**

---

## 4️⃣ Create Task Definition (GUI)

1. In ECS → **Task definitions**
2. Click **Create new task definition**
3. Select **Fargate**
4. Click **Next**

### Task Configuration

* **Task definition name:** `nautilus-taskdefinition`
* **Task role:** None (or existing if required)
* **Operating system:** Linux
* **CPU:** 0.25 vCPU
* **Memory:** 0.5 GB

### Container Definition

1. Click **Add container**

2. Fill:

   * **Container name:** `nautilus-container`
   * **Image URI:**
     `ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/nautilus-ecr:latest`
   * **Port mappings:** `80`

3. Click **Add**

4. Click **Create**

---

## 5️⃣ Create ECS Service (Deploy the App)

1. Open **Clusters → nautilus-cluster**
2. Click **Services → Create**
3. Configure:

   * **Launch type:** Fargate
   * **Task definition:** `nautilus-taskdefinition`
   * **Service name:** `nautilus-service`
   * **Desired tasks:** `1`

### Networking

* Select **VPC**
* Choose **subnets**
* Choose **security group** enable port 80
* Enable **Auto-assign public IP**

4. Click **Create service**

---

## 6️⃣ Verify Deployment (GUI)

1. Open **ECS → Clusters → nautilus-cluster**
2. Click **Services**
3. Check:

   * Service status: **ACTIVE**
   * Running tasks: **1**

You can click the **Task → Logs** (CloudWatch) to confirm the app is running.

---

## ✅ Final Result (GUI)

✔ ECR repository created
✔ Docker image pushed
✔ ECS Fargate cluster running
✔ Task definition registered
✔ ECS service running at least one task

If you want, I can also:

* Walk you through **IAM role creation in GUI**
* Add **Application Load Balancer (GUI)**
* Show how to **access the app URL**


### 🏗️ **Q5: Automating Infrastructure Deployment with AWS CloudFormation**

> *Design and deploy a full-stack infrastructure (VPC, subnets, NAT Gateway, EC2, RDS, S3, IAM roles) using CloudFormation. Your template must support parameterization for environment (dev/stage/prod), use nested stacks, and output resource ARNs for integration. How would you structure your stacks and manage updates without downtime?*



### 🌐 **Q6: Hosting a Static Website on AWS S3**

> *You’ve been asked to host a secure static site using S3 with CloudFront, Route 53, and HTTPS. Set up a private S3 bucket to store content, configure CloudFront with origin access control (OAC), and use ACM for SSL certificates. How do you implement cache invalidation and secure custom domain setup with minimal cost?*

The Nautilus DevOps team has been tasked with creating an internal information portal for public access. As part of this project, they need to host a static website on AWS using an S3 bucket. The S3 bucket must be configured for public access to allow external users to access the static website directly via the S3 website URL.

Task Requirements:

Create an S3 bucket named xfusion-web-22541.
Configure the S3 bucket for static website hosting with index.html as the index document.
Allow public access to the bucket so that the website is publicly accessible.
Upload the index.html file from the /root/ directory of the AWS client host to the S3 bucket.
Verify that the website is accessible directly through the S3 website URL.

Ans:
Below are **step-by-step AWS Console (GUI) instructions** to complete the task.

---

## 1. Create the S3 Bucket

1. Log in to the **AWS Management Console**
2. Go to **Services → S3**
3. Click **Create bucket**
4. Fill in:

   * **Bucket name:** `xfusion-web-22541`
   * **AWS Region:** Select your required region
5. **Object Ownership**

   * Select **ACLs disabled (Bucket owner enforced)** (default)
6. **Block Public Access settings**

   * **Uncheck** ✅ *Block all public access*
   * Confirm by checking **I acknowledge that this bucket will be public**
7. Leave other settings as default
8. Click **Create bucket**

---

## 2. Enable Static Website Hosting

1. Open the bucket **xfusion-web-22541**
2. Go to the **Properties** tab
3. Scroll to **Static website hosting**
4. Click **Edit**
5. Select **Enable**
6. Choose **Host a static website**
7. Set:

   * **Index document:** `index.html`
8. Click **Save changes**

---

## 3. Allow Public Read Access (Bucket Policy)

1. Go to the **Permissions** tab of the bucket
2. Scroll to **Bucket policy**
3. Click **Edit**
4. Paste the following policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::xfusion-web-22541/*"
    }
  ]
}
```

5. Click **Save changes**

---

## 4. Upload `index.html`

1. Go to the **Objects** tab
2. Click **Upload**
3. Click **Add files**
4. Select `/root/index.html`
5. Click **Upload**
CLI:
aws s3 cp /root/index.html s3://xfusion-web-22541/
     
---

## 5. Verify Public Access

1. Go back to the **Properties** tab
2. Scroll to **Static website hosting**
3. Copy the **Bucket website endpoint**

   * Example:

     ```
     http://xfusion-web-22541.s3-website-us-east-1.amazonaws.com
     ```
4. Open the URL in a browser

You should see the content of **index.html** 🎉
---

### 🌍 **Q7: Enable Internet Access for Private EC2 using NAT Instance**

> *You’ve deployed EC2 instances in private subnets that need internet access for software updates, but due to budget constraints, you're using a NAT instance instead of a NAT Gateway. Configure the NAT instance, update route tables, harden the instance, and implement high availability using autoscaling or failover strategy. What are the trade-offs of using NAT instance over NAT Gateway?*

The Nautilus DevOps team is tasked with enabling internet access for an EC2 instance running in a private subnet. This instance should be able to upload a test file to a public S3 bucket once it can access the internet. To minimize costs, the team has decided to use a NAT Instance instead of a NAT Gateway.

The following components already exist in the environment:
1) A VPC named xfusion-priv-vpc and a private subnet named xfusion-priv-subnet have been created.
2) An EC2 instance named xfusion-priv-ec2 is already running in the private subnet.
3) The EC2 instance is configured with a cron job that uploads a test file to the S3 bucket xfusion-nat-26631 every minute. Upload will only succeed once internet access is established.

Your task is to:

Create a new public subnet named xfusion-pub-subnet in the existing VPC.
Launch a NAT Instance in the public subnet using an Amazon Linux 2 AMI and name it xfusion-nat-instance. Configure this instance to act as a NAT instance. Make sure to use a custom security group for this instance.
After the configuration, verify that the test file xfusion-test.txt appears in the S3 bucket xfusion-nat-26631. This indicates successful internet access from the private EC2 instance via the NAT Instance.

Ans:
USe follwoing document
https://docs.aws.amazon.com/vpc/latest/userguide/work-with-nat-instances.html
## 🔹 Step 1: Create a Public Subnet
- Go to **VPC Console** → Subnets → Create Subnet.
- Select **VPC: datacenter-priv-vpc**.
- Name: **datacenter-pub-subnet**.
- Choose an **Availability Zone** (same as private subnet for simplicity).
- Assign a **CIDR block** (e.g., `10.0.2.0/24`).
- Ensure the **Route Table** for this subnet has:
  - A **default route (0.0.0.0/0)** pointing to the **Internet Gateway** attached to the VPC.

---

## 🔹 Step 2: Launch the NAT Instance
- Go to **EC2 Console** → Launch Instance.
- Name: **datacenter-nat-instance**.
- AMI: **Amazon Linux 2**.
- Instance type: **t3.micro** (cost‑effective).
- Network: **datacenter-priv-vpc**.
- Subnet: **datacenter-pub-subnet**.
- Enable **Auto-assign Public IP**.
- Security Group (custom):
   - Inbound,All Traffic,All,10.1.1.0/24,Allows traffic from the private subnet.
   - Inbound,SSH,22,Your Public IP,(Optional) To configure the NAT settings.
   - Outbound,All Traffic,All,0.0.0.0/0,Allows NAT to reach the internet/S3.
# Private Instance Security Group
Ensure the security group attached to datacenter-priv-ec2 allows the upload to S3.
   - Outbound,HTTPS,443,0.0.0.0/0,Required for AWS CLI/S3 uploads.
   - Inbound,SSH,22,10.1.2.0/24,(Optional) Allows you to jump from the NAT instance.
# Enable IP forwarding # Install SSM Agent (Amazon Linux 2)# Configure iptables for NAT
#!/bin/bash
sudo yum install iptables-services -y
# Enable IP Forwarding at the Kernel level
sudo sysctl -w net.ipv4.ip_forward=1
# Apply the NAT Rule: Note: Ensure your interface name is indeed enX0 (you can check with ip addr).
sudo iptables -t nat -A POSTROUTING -o enX0 -j MASQUERADE
sudo service iptables save
# Verification of NAT Traffic
iptables -t nat -L -n -v
# Save and Enable: This ensures your NAT doesn't break if the instance reboots.
sudo service iptables save
sudo systemctl enable iptables

# Disable source/destination check will be done in console manually
# (cannot be automated via user-data)
## 🔹 Step 3: Configure NAT Instance
1. **Disable Source/Destination Check**:
   - Select the NAT instance → Actions → Networking → Change Source/Dest Check → Disable.
## 🔹 Step 4: Update Private Subnet Route Table
- Go to **Route Tables** in VPC Console.
- Select the route table associated with **datacenter-priv-subnet**.
- Add a route:
  - Destination: `0.0.0.0/0`
  - Target: **datacenter-nat-instance** (instance ID).

---
### 1. Watch Traffic in Real-Time (tcpdump)

On your **NAT instance**, you can "eavesdrop" on the network interface to see if the private instance is trying to send data. Run this command:

```bash
sudo tcpdump -i enX0 src net 10.1.1.0/24 and port 443

```

* **What this does:** It shows any incoming traffic from your private subnet (`10.1.1.0/24`) destined for HTTPS (Port 443), which is what S3 uses.
* **Success looks like:** If you see lines of text appearing every minute, the private instance is successfully reaching your NAT instance.

---

### 2. Check Hit Counters (iptables)

If you already applied the `MASQUERADE` rule, Linux keeps track of how many packets have used it. Run:

```bash
sudo iptables -t nat -L POSTROUTING -v -n

```

* **Watch the "pkts" column:** If the NAT is working, you will see the packet count increase every time the cron job runs on the private instance.

---

### 3. Verification via S3 (The "Result" Method)

Since you can't log into the private instance, the S3 bucket is your "Success Dashboard."

1. Open the **S3 Console**.
2. Navigate to the `datacenter-nat-25656` bucket.
3. Check the **"Last Modified"** timestamp of `datacenter-test.txt`.
4. If the timestamp is from the last 60 seconds, your configuration is 100% successful.

### Final Sanity Check

If you see **zero traffic** in `tcpdump` and no file in S3, the issue is likely "upstream" from the NAT instance:

* **The Private Route Table:** Ensure `0.0.0.0/0` is pointing to the NAT Instance ID.
* **Source/Dest Check:** In the AWS Console, ensure this is **Disabled** on the NAT instance (this is the #1 reason traffic never reaches the OS).

## 🔹 Step 5: Verification
- The private EC2 (`datacenter-priv-ec2`) should now reach the internet via NAT.
- Since it already has a cron job uploading `datacenter-test.txt` to S3:
  - Wait a minute.
  - Go to **S3 Console** → Bucket: `datacenter-nat-12243`.
  - Confirm that `datacenter-test.txt` appears.
  - If it does, ✅ internet access is working through NAT Instance.

---

## ✅ Outcome
- **datacenter-pub-subnet** created.
- **datacenter-nat-instance** launched and configured as NAT.
- Private EC2 (`datacenter-priv-ec2`) now uploads files to S3 successfully.
aws s3 ls s3://datacenter-nat-6877/datacenter-test.txt
aws s3 ls s3://nautilus-nat-23937/nautilus-test.txt


### 🔒 **Q8: Securing Data with AWS KMS**

> *You’re building a data processing pipeline that stores customer data in S3, RDS, and DynamoDB. Design a centralized encryption strategy using AWS KMS with customer-managed keys (CMK). Implement key policies, automatic rotation, and audit logging via CloudTrail. How would you securely share encrypted data across accounts while maintaining least privilege?*

The Nautilus DevOps team is focusing on improving their data security by using AWS KMS. Your task is to create a KMS key and manage the encryption and decryption of a pre-existing sensitive file using the KMS key.

Specific Requirements:

Create a symmetric KMS key named devops-KMS-Key to manage encryption and decryption.
Encrypt the provided SensitiveData.txt file (located in /root/), base64 encode the ciphertext, and save the encrypted version as EncryptedData.bin in the /root/ directory.
Try to decrypt the same and verify that the decrypted data matches the original file.
Make sure that the KMS key is correctly configured. The validation script will test your configuration by decrypting the EncryptedData.bin file using the KMS key you created.

Ans:
Got it — here are the **AWS Console (GUI) steps** to complete the task ✅

---

## 1. Create the KMS Key (GUI)

1. Open **AWS Console**
2. Go to **Services → Security, Identity & Compliance → Key Management Service (KMS)**
3. Click **Customer managed keys**
4. Click **Create key**

### Key configuration

* **Key type:** Symmetric
* **Key usage:** Encrypt and decrypt
* Click **Next**

### Alias

* **Alias name:** `devops-KMS-Key`
* Click **Next**

### Key administrators

* Select your IAM user / role
* Click **Next**

### Key users

* Select the same IAM user / role
* Click **Next**

### Review

* Click **Finish**

✅ Your symmetric KMS key is now ready.

---

## 2. Encrypt the file (from EC2 / CloudShell terminal)

> AWS Console is used for key creation, but **file encryption must be done via CLI**

Run:

```bash
aws kms encrypt \
  --key-id alias/devops-KMS-Key \
  --plaintext fileb:///root/SensitiveData.txt \
  --output text \
  --query CiphertextBlob | base64 --decode > /root/EncryptedData.bin
```

✅ Encrypted file created:

```
/root/EncryptedData.bin
```

---

## 3. Decrypt and verify (CLI)

```bash
aws kms decrypt \
  --ciphertext-blob fileb:///root/EncryptedData.bin \
  --output text \
  --query Plaintext | base64 --decode > /root/DecryptedData.txt
```

Verify:

```bash
diff /root/SensitiveData.txt /root/DecryptedData.txt
```

No output = files match ✅

---

## 4. Validation readiness checklist

✔ KMS key created via GUI
✔ Alias name exactly `devops-KMS-Key`
✔ Encryption done using that key
✔ Encrypted file saved as `/root/EncryptedData.bin`
✔ Decryption works (validation script will pass)

### 📊 **Q9: Building and Managing NoSQL Databases with AWS DynamoDB**

> *Design a DynamoDB schema for a multi-tenant SaaS application with high read/write throughput and predictable access patterns. Implement partition key strategies to avoid hot partitions, enable DynamoDB Streams for real-time processing, and set up global tables for cross-region replication. How would you handle backup, restore, and consistent access across regions?*

The Nautilus DevOps team is developing a simple 'To-Do' application using DynamoDB to store and manage tasks efficiently. The team needs to create a DynamoDB table to hold tasks, each identified by a unique task ID. Each task will have a description and a status, which indicates the progress of the task (e.g., 'completed' or 'in-progress').

Your task is to:

Create a DynamoDB table named nautilus-tasks with a primary key called taskId (string).
Insert the following tasks into the table:
Task 1: taskId: '1', description: 'Learn DynamoDB', status: 'completed'
Task 2: taskId: '2', description: 'Build To-Do App', status: 'in-progress'
Verify that Task 1 has a status of 'completed' and Task 2 has a status of 'in-progress'.
Ensure the DynamoDB table is created successfully and that both tasks are inserted correctly with the appropriate statuses.

Ans:
If you prefer using the **AWS Management Console (GUI)** to set this up, here is the step-by-step walkthrough to ensure the `nautilus-tasks` table is configured correctly.

---

## Step 1: Create the Table

1. Log in to the **AWS Management Console** and navigate to **DynamoDB**.
2. Click the **Create table** button.
3. **Table name:** Enter `nautilus-tasks`.
4. **Partition key:** Enter `taskId` and ensure the data type is set to **String**.
5. Keep the **Default settings** (this will default to a provisioned capacity, which is fine for this exercise) and click **Create table**.

---

## Step 2: Insert the Items

Once the table status shows as **Active**, follow these steps for each task:

1. Click on the table name **nautilus-tasks** from the list.
2. Click the **Explore table items** button in the top right.
3. Click **Create item**.
4. On the creation screen, follow these values:
* **Task 1:**
# use json:
{
        "taskId": {"S": "1"},
        "description": {"S": "Learn DynamoDB"},
        "status": {"S": "completed"}
    }


* **Task 2:**
# use json:
{
        "taskId": {"S": "2"},
        "description": {"S": "Build To-Do App"},
        "status": {"S": "in-progress"}
    }
* `taskId` (String): `2`
* Attribute name: `description` | Value: `Build To-Do App`
* Attribute name: `status` | Value: `in-progress`




5. Click **Create item** after entering each task.

---

## Step 3: Verify the Data

After creating both items, you will be returned to the **Items returned** view. You should see a table layout confirming the entries:

| taskId (Partition Key) | description | status |
| --- | --- | --- |
| 1 | Learn DynamoDB | **completed** |
| 2 | Build To-Do App | **in-progress** |
# CLI: 
aws dynamodb scan --table-name nautilus-tasks
---

### Troubleshooting Tip

If you don't see your items immediately, ensure the **Scan/Query** toggle is set to **Scan** and click **Run** to refresh the results.



### ☸️ **Q10: Scaling and Managing Kubernetes Clusters with Amazon EKS**

> *You are running a production-grade EKS cluster with microservices deployed via Helm charts. Implement a scalable architecture using Fargate and EC2 node groups, secure the cluster with IAM roles for service accounts (IRSA), and monitor performance using Prometheus and Grafana. How would you manage blue/green deployments, control cluster costs, and integrate with service mesh (e.g., AWS App Mesh or Istio)?*

Got it — you’d like to know how to do this using the **AWS Management Console (GUI)** instead of CLI commands. Let me walk you through the exact steps visually-oriented teams usually follow:

---

## 🖥️ Step 1: Create the IAM Role
1. Sign in to the **AWS Management Console**.
2. Go to **IAM → Roles → Create role**.
3. Choose **AWS service** → **EKS**.
4. Select **EKS – Cluster**.
5. Click **Next** and name the role **eksClusterRole**.
6. Attach the policies:
   - **AmazonEKSClusterPolicy**
   - **AmazonEKSServicePolicy**
7. Finish creating the role.

---

## 🌐 Step 2: Prepare the VPC & Subnets
1. Go to **VPC → Your VPCs**.
2. Confirm the **default VPC** exists.
3. Under **Subnets**, ensure you have subnets in availability zones **a, b, and c** (for example: `us-east-1a`, `us-east-1b`, `us-east-1c`).
   - If they exist, note their IDs.
   - If not, create subnets in those AZs within the default VPC.

---

## 🚀 Step 3: Create the EKS Cluster
1. Navigate to **Amazon EKS → Clusters → Create cluster**.
2. Enter:
   - **Cluster name:** `devops-eks`
   - **Kubernetes version:** `1.30`
   - **Cluster service role:** select **eksClusterRole**
3. In **Networking**, choose:
   - **VPC:** default VPC
   - **Subnets:** select the ones in AZs a, b, c
   - **Cluster endpoint access:** set to **Private**
4. Click **Create**.

---

## ✅ Step 4: Verify Cluster Status
1. In the **EKS console**, open your cluster.
2. Under **Overview**, check **Status** → should show **Active**.
3. Confirm:
   - **Cluster name:** `devops-eks`
   - **Version:** `1.30`
   - **Endpoint access:** Private
   - **Role:** `eksClusterRole`
   - **Subnets:** from AZs a, b, c

---

## 🎯 Step 5: Ready for Workloads
Once the cluster is **Active**, you can:
1. Go to **Compute → Add node group** to provision worker nodes.
2. Then connect with `kubectl` by downloading the kubeconfig from the console.


👉 This GUI path ensures the cluster is created exactly as required: **latest Kubernetes version (1.30)**, **private endpoint**, **default VPC with AZs a/b/c**, and **IAM role eksClusterRole**.  

## 🔑 IAM Role for Node Groups
When you create a **managed node group** in EKS, you need an IAM role that the EC2 instances (your worker nodes) will assume. This role is different from the **cluster role** (`eksClusterRole`) you already created.

### Required Policies
Attach these policies to the node group role:
- **AmazonEKSWorkerNodePolicy** → Allows worker nodes to connect to the cluster.
- **AmazonEKS_CNI_Policy** → Allows the Amazon VPC CNI plugin to manage networking for pods.
- **AmazonEC2ContainerRegistryReadOnly** → Allows nodes to pull container images from Amazon ECR.

---

## 🖥️ GUI Steps (AWS Console)
1. Go to **IAM → Roles → Create role**.
2. Choose **AWS service → EC2** (because worker nodes are EC2 instances).
3. Click **Next** and name the role something like `eksNodeGroupRole`.
4. Attach the following policies:
   - **AmazonEKSWorkerNodePolicy**
   - **AmazonEKS_CNI_Policy**
   - **AmazonEC2ContainerRegistryReadOnly**
5. Create the role.

---

## 🚀 Use the Role in Node Group Creation
1. Go to **Amazon EKS → Clusters → devops-eks → Compute → Add node group**.
2. Enter:
   - **Node group name:** e.g. `devops-nodegroup`
   - **IAM role:** select `eksNodeGroupRole`
   - **Subnets:** same AZs (a, b, c) in the default VPC
   - **Scaling configuration:** set desired/min/max nodes
3. Create the node group.

---

## ✅ Verification
Once the node group is active:
- Run:
  ```bash
  kubectl get nodes
  ```
  You should see your EC2 worker nodes registered.
- In the **EKS console**, under **Compute**, the node group should show **Active**.

---

✨ Summary:
- **Cluster role (`eksClusterRole`)** → for control plane.
- **Node group role (`eksNodeGroupRole`)** → for worker nodes, with 3 key policies attached.
---

**Level 4**
Here is a set of **advanced-level, scenario-based questions** for each of the topics you've listed. These are designed to test not just technical skills but also architectural thinking, scalability, automation, event-driven design, and security — all essential for **senior engineers, architects, or DevOps professionals**.



### 🚀 **Q1: Implementing Auto Scaling for High Availability in AWS**

> *You manage a web application running on EC2 instances behind an Application Load Balancer. The app experiences traffic spikes during regional events. Design and implement an Auto Scaling solution that scales based on CPU utilization and maintains a minimum of 2 and a maximum of 10 instances. Additionally, ensure health checks automatically replace failed instances. How would you handle scaling cooldowns, lifecycle hooks, and spot instance integration to optimize costs?*

The DevOps team is tasked with setting up a highly available web application using AWS. To achieve this, they plan to use an Auto Scaling Group (ASG) to ensure that the required number of EC2 instances are always running, and an Application Load Balancer (ALB) to distribute traffic across these instances. The goal of this task is to set up an ASG that automatically scales EC2 instances based on CPU utilization, and an ALB that directs incoming traffic to the instances. The EC2 instances should have Nginx installed and running to serve web traffic.

Create an EC2 launch template named xfusion-launch-template that specifies the configuration for the EC2 instances, including the Amazon Linux 2 AMI, t2.micro instance type, and a security group that allows HTTP traffic on port 80.
Add a User Data script to the launch template to install Nginx on the EC2 instances when they are launched. The script should install Nginx, start the Nginx service, and enable it to start on boot.
Create an Auto Scaling Group named xfusion-asg that uses the launch template and ensures a minimum of 1 instance, desired capacity is 1 instance and a maximum of 2 instances are running based on CPU utilization. Set the target CPU utilization to 50%.
Create a target group named xfusion-tg, an Application Load Balancer named xfusion-alb and configure it to listen on port 80. Ensure the ALB is associated with the Auto Scaling Group and distributes traffic across the instances.
Configure health checks on the ALB to ensure it routes traffic only to healthy instances.
Verify that the ALB's DNS name is accessible and that it displays the default Nginx page served by the EC2 instances.

Ans:

Got it — you want to do this **using the AWS Management Console (GUI)** instead of CLI.
Below is a **step-by-step console walkthrough** that matches your exact requirements.

---

## 1️⃣ Create Security Group (Allow HTTP)

1. Open **AWS Console → EC2 → Security Groups**
2. Click **Create security group**
3. Configure:

   * **Name:** `xfusion-web-sg`
   * **Description:** Allow HTTP traffic
   * **VPC:** Select your VPC
4. **Inbound rules → Add rule**

   * Type: **HTTP**
   * Port: **80**
   * Source: **Anywhere (0.0.0.0/0)**
5. Click **Create security group**

---

## 2️⃣ Create Launch Template (xfusion-launch-template)

1. Go to **EC2 → Launch Templates**
2. Click **Create launch template**
3. Fill in:

   * **Launch template name:** `xfusion-launch-template`
   * **Template version description:** Nginx web server

### AMI & Instance

4. **Amazon Machine Image (AMI):**

   * Select **Amazon Linux 2 AMI**
5. **Instance type:** `t2.micro`

### Security Group

6. Under **Network settings**

   * Select **Existing security group**
   * Choose `xfusion-web-sg`

### User Data (Install Nginx)

7. Expand **Advanced details**
8. Scroll to **User data**
9. Paste the following:
# Amazon linuz 2
```bash
#!/bin/bash
yum update -y
amazon-linux-extras install nginx1 -y
systemctl start nginx
systemctl enable nginx

# Amazon linux 2023:
#!/bin/bash
dnf update -y
dnf install -y nginx
systemctl start nginx
systemctl enable nginx
```
10. Click **Create launch template**

---

## 3️⃣ Create Target Group (xfusion-tg)

1. Go to **EC2 → Target Groups**
2. Click **Create target group**
3. Configure:

   * **Target type:** Instances
   * **Target group name:** `xfusion-tg`
   * **Protocol:** HTTP
   * **Port:** 80
   * **VPC:** Select your VPC
4. **Health checks**

   * Protocol: HTTP
   * Path: `/`
5. Click **Create target group**

> Do **not** register instances manually (ASG will do this)

---

## 4️⃣ Create Application Load Balancer (xfusion-alb)

1. Go to **EC2 → Load Balancers**
2. Click **Create load balancer**
3. Choose **Application Load Balancer**
4. Click **Create**

### Basic Configuration

5. Set:

   * **Name:** `xfusion-alb`
   * **Scheme:** Internet-facing
   * **IP address type:** IPv4

### Network Mapping

6. Select:

   * Your **VPC**
   * At least **two public subnets** (different AZs)

### Security Group

7. Select:

   * `xfusion-web-sg`

### Listener & Routing

8. Listener:

   * Protocol: HTTP
   * Port: 80

9. Default action:

   * Forward to **xfusion-tg**

10. Click **Create load balancer**

---

## 5️⃣ Create Auto Scaling Group (xfusion-asg)

1. Go to **EC2 → Auto Scaling Groups**
2. Click **Create Auto Scaling group**

### Step 1 – Choose launch template

3. Name: `xfusion-asg`
4. Launch template: `xfusion-launch-template`
5. Version: Default
6. Click **Next**

### Step 2 – Network

7. Select:

   * Your **VPC**
   * Same **subnets** used by ALB
8. Click **Next**

### Step 3 – Load balancing

9. Select:

   * **Attach to an existing load balancer**
   * Choose **Application Load Balancer**
   * Select target group: `xfusion-tg`
10. Enable:

* ✅ **ELB health checks**

11. Click **Next**

### Step 4 – Group size

12. Set:

* **Desired capacity:** 1
* **Minimum capacity:** 1
* **Maximum capacity:** 2

13. Click **Next**

---

## 6️⃣ Configure Auto Scaling Policy (CPU 50%)

1. In **Scaling policies**
2. Choose:

   * **Target tracking scaling policy**
3. Configure:

   * Metric type: **Average CPU utilization**
   * Target value: **50**
4. Click **Next**
5. Skip notifications
6. Click **Create Auto Scaling group**

---

## 7️⃣ Verify Health Checks & Nginx Page ✅

### Check instance health

1. Go to **EC2 → Target Groups**
2. Select `xfusion-tg`
3. Open **Targets** tab
4. Status should be **Healthy**

### Access Application

1. Go to **EC2 → Load Balancers**
2. Select `xfusion-alb`
3. Copy **DNS name**
4. Open in browser:

```
http://<ALB-DNS-NAME>
```

🎉 You should see the **default Nginx welcome page**

---

## ✅ Final Result

✔ Auto Scaling Group with CPU-based scaling
✔ Application Load Balancer distributing traffic
✔ Nginx installed automatically on EC2
✔ Health checks ensure only healthy instances receive traffic

If you want, I can also:

* Add **HTTPS (ACM + SSL)**
* Show **how to test scaling**
* Provide **architecture diagram**
* Help with **IAM roles & logging**



### 🔄 **Q2: CI/CD Automation Using AWS CodePipeline**

> *You’ve been asked to implement a CI/CD pipeline for a microservice application written in Python. The source code is stored in GitHub. On every push to the `main` branch, the pipeline should build a Docker image, store it in Amazon ECR, and deploy it to an ECS Fargate service. Integrate AWS CodePipeline, CodeBuild, and ECS into a fully automated CI/CD workflow. How do you securely handle secrets (e.g., DB credentials) during build and deploy stages, and ensure rollback on deployment failure?*



### ⚡ **Q3: Event-Driven Processing with Amazon S3 and Lambda**

> *Your application uploads large JSON files to an S3 bucket, and each upload should trigger a Lambda function that parses the file and stores records in DynamoDB. Design this event-driven architecture ensuring idempotency, retry behavior, and concurrency controls. How would you handle large file sizes, failures during processing, and long execution times?*



### 📩 **Q4: Integrating AWS SQS and SNS for Reliable Messaging**

> *You’re building a distributed system where user signup events are published to an SNS topic. Multiple systems (email, analytics, fraud detection) must process these events asynchronously. Use SNS to fan out events and SQS queues for each consumer system. How would you implement dead-letter queues (DLQs), message filtering, and guarantee exactly-once processing where needed?*



### 📑 **Q5: Centralized Audit Logging with VPC Peering**

> *Your organization runs multiple VPCs across different AWS accounts — each hosting different workloads. For compliance, all audit logs must be sent to a centralized VPC where a log analysis tool is deployed. Design a solution using VPC peering, CloudWatch Logs, and centralized S3 buckets with cross-account access. What security controls, IAM policies, and VPC route updates are required to make this architecture work securely and at scale?*



### 🐳 **Q6: Deploying Containerized Applications with AWS ECS**

> *Your team is deploying a containerized REST API using Amazon ECS with Fargate. The API requires access to an RDS database and secrets stored in AWS Secrets Manager. Build the ECS service with task definitions that securely inject secrets, handle dynamic scaling, and use an ALB for traffic routing. How do you implement service discovery, blue/green deployments, and observability (e.g., X-Ray or CloudWatch Logs)?*



### 🌐 **Q7: Building and Managing APIs with AWS API Gateway**

> *You’re building a public-facing REST API using Amazon API Gateway that integrates with multiple Lambda functions. Design an API with custom domain names, throttling, request/response validation, and usage plans for different clients. How would you secure it using API keys and IAM roles, implement versioning, and support canary deployments for new Lambda versions?*

