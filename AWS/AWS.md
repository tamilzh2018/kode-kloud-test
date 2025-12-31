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


**Q10: Enabling Public Access to an RDS Instance**

> *Your testing team needs to connect to the RDS instance from their local machines. Reconfigure the RDS instance to allow public access securely.*
or 
For temporary testing, your QA team needs public access to an RDS instance. Modify the instance to be publicly accessible, add appropriate inbound rules, and ensure the database is not exposed to the internet unnecessarily. How do you mitigate risks?


**Q11: Snapshot and Restoration of an RDS Instance**

> *Before running a schema migration, create a manual snapshot of the RDS instance. If the migration fails, restore the database using that snapshot. Outline the full process.*

or 
A developer corrupted the staging database. Use a previously created manual snapshot to restore the RDS instance. What changes (e.g., DB identifier, endpoint) should be expected post-restoration?


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


**Q14: Setting Up a Private VPC with an Isolated EC2 Instance**

> *Create a VPC with a private subnet and launch an EC2 instance inside it. Ensure it has **no internet access**, and explain how you verify its isolation.*


### ⚙️ **Serverless: Lambda**

**Q15: Create a Lambda Function**

> *Write a simple Lambda function in Python that logs “Hello from Lambda!” to CloudWatch. Create and test it using the AWS Console.*
or 
Create a Lambda function triggered when new files are uploaded to an S3 bucket. The function should log the filename and timestamp. What permissions do you need to configure on the bucket and Lambda role?


**Q16: Create a Lambda Function Using CLI**

> *Use the AWS CLI to deploy a Lambda function from a local zip file. The function should return the current timestamp when triggered.*
or 

Package a Python script into a zip file and deploy it to AWS Lambda using CLI. What CLI commands are needed, and how do you test the function after deployment?

### 🛠️ **Troubleshooting & NAT Gateway**

**Q17: Troubleshooting Internet Accessibility for an EC2-Hosted Application**

> *You launched an EC2 instance in a public subnet, but your web app isn’t accessible via browser. Identify and resolve the issue by checking networking, security group, and route settings.*
or 
You deployed a Node.js app on EC2, but it’s not reachable from the internet. What components would you check (e.g., security groups, routes, app bindings), and how would you debug this step by step?
**Q18: Troubleshooting Connectivity Issues for Package Installation on EC2**

> *Your EC2 instance cannot install packages via `yum` or `apt`. It’s in a private subnet. Diagnose and fix the problem to restore internet access.*
or 
An EC2 instance in a private subnet fails to install software updates. Explain how to diagnose whether it's a DNS, NAT, or routing issue and how to fix it so the instance can access the internet safely.


### 📦 **ECR & Container Management**

**Q19: Creating a Private ECR Repository**

> *You’re preparing a CI/CD pipeline and need a private container registry. Create a private Amazon ECR repository and push a Docker image to it.*

or
Create a private ECR repository, build a Docker image locally, and push it to the ECR repo. What authentication steps are required, and how do you allow ECS or EC2 instances to pull this image?

### 🌐 **NAT Gateway**

**Q20: Configure NAT Gateway for Internet Access in a Private VPC**

> *You need to allow EC2 instances in a private subnet to access the internet (e.g., for updates). Configure a NAT Gateway and update routing accordingly.*

or 
Your EC2 instance in a private subnet needs to access the internet for updates and package downloads. Create a NAT Gateway in a public subnet and modify the route tables. How do you ensure only outgoing traffic is allowed?

**Level 3**
Here is a set of **Advanced-Level Scenario-Based Questions** based on your provided topics. These questions are designed to test deep understanding, cross-service integration, architecture design, automation, scalability, and security—making them ideal for advanced learners, cloud architects, or senior DevOps/Cloud Engineers preparing for real-world projects or advanced certifications (e.g., AWS Solutions Architect Professional, DevOps Pro).



### 🚀 **Q1: Deploying and Managing Applications on AWS**

> *You’re leading the migration of a monolithic application to AWS. The app consists of a backend API, frontend UI, and a relational database. How would you design a resilient, scalable architecture using AWS services like EC2, RDS, Auto Scaling, and Route 53? How would you manage secrets and deploy updates with minimal downtime?*



### ⚖️ **Q2: Load Balancing EC2 Instances with Application Load Balancer**

> *You’re running multiple EC2 instances across two Availability Zones hosting microservices. Configure an Application Load Balancer that routes traffic based on path (`/api`, `/admin`, etc.). How would you implement sticky sessions, enable HTTPS with SSL certificates, and configure health checks for each target group?*



### 🔐 **Q3: Managing EC2 Access with S3 Role-Based Permissions**

> *Your EC2 instance processes data from multiple S3 buckets. You want to avoid using static credentials. Create an IAM role with fine-grained permissions that allows read-only access to `bucket-A` and full access to `bucket-B`. Attach the role to the instance and validate access using the AWS CLI. How would you audit and rotate permissions securely?*



### 🐳 **Q4: Deploying Containerized Applications with Amazon ECS**

> *You’re deploying a containerized Node.js app using Amazon ECS with Fargate. Create a multi-container task definition with app and logging sidecar. Configure the service with an ALB for public access, enable autoscaling based on CPU utilization, and ensure secure secret injection using AWS Secrets Manager. How would you handle zero-downtime deployments and rollback strategies?*



### 🏗️ **Q5: Automating Infrastructure Deployment with AWS CloudFormation**

> *Design and deploy a full-stack infrastructure (VPC, subnets, NAT Gateway, EC2, RDS, S3, IAM roles) using CloudFormation. Your template must support parameterization for environment (dev/stage/prod), use nested stacks, and output resource ARNs for integration. How would you structure your stacks and manage updates without downtime?*



### 🌐 **Q6: Hosting a Static Website on AWS S3**

> *You’ve been asked to host a secure static site using S3 with CloudFront, Route 53, and HTTPS. Set up a private S3 bucket to store content, configure CloudFront with origin access control (OAC), and use ACM for SSL certificates. How do you implement cache invalidation and secure custom domain setup with minimal cost?*



### 🌍 **Q7: Enable Internet Access for Private EC2 using NAT Instance**

> *You’ve deployed EC2 instances in private subnets that need internet access for software updates, but due to budget constraints, you're using a NAT instance instead of a NAT Gateway. Configure the NAT instance, update route tables, harden the instance, and implement high availability using autoscaling or failover strategy. What are the trade-offs of using NAT instance over NAT Gateway?*



### 🔒 **Q8: Securing Data with AWS KMS**

> *You’re building a data processing pipeline that stores customer data in S3, RDS, and DynamoDB. Design a centralized encryption strategy using AWS KMS with customer-managed keys (CMK). Implement key policies, automatic rotation, and audit logging via CloudTrail. How would you securely share encrypted data across accounts while maintaining least privilege?*



### 📊 **Q9: Building and Managing NoSQL Databases with AWS DynamoDB**

> *Design a DynamoDB schema for a multi-tenant SaaS application with high read/write throughput and predictable access patterns. Implement partition key strategies to avoid hot partitions, enable DynamoDB Streams for real-time processing, and set up global tables for cross-region replication. How would you handle backup, restore, and consistent access across regions?*



### ☸️ **Q10: Scaling and Managing Kubernetes Clusters with Amazon EKS**

> *You are running a production-grade EKS cluster with microservices deployed via Helm charts. Implement a scalable architecture using Fargate and EC2 node groups, secure the cluster with IAM roles for service accounts (IRSA), and monitor performance using Prometheus and Grafana. How would you manage blue/green deployments, control cluster costs, and integrate with service mesh (e.g., AWS App Mesh or Istio)?*



**Level 4**
Here is a set of **advanced-level, scenario-based questions** for each of the topics you've listed. These are designed to test not just technical skills but also architectural thinking, scalability, automation, event-driven design, and security — all essential for **senior engineers, architects, or DevOps professionals**.



### 🚀 **Q1: Implementing Auto Scaling for High Availability in AWS**

> *You manage a web application running on EC2 instances behind an Application Load Balancer. The app experiences traffic spikes during regional events. Design and implement an Auto Scaling solution that scales based on CPU utilization and maintains a minimum of 2 and a maximum of 10 instances. Additionally, ensure health checks automatically replace failed instances. How would you handle scaling cooldowns, lifecycle hooks, and spot instance integration to optimize costs?*



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

