**Level 1:**
# Q1 Set Up Jenkins Server
The DevOps team at xFusionCorp Industries is initiating the setup of CI/CD pipelines and has decided to utilize Jenkins as their server. Execute the task according to the provided requirements:

1. Install Jenkins on the jenkins server using the yum utility only, and start its service.

If you face a timeout issue while starting the Jenkins service, refer to this.
2. Jenkin's admin user name should be theadmin, password should be Adm!n321, full name should be Javed and email should be javed@jenkins.stratos.xfusioncorp.com.

Note:

1. To access the jenkins server, connect from the jump host using the root user with the password S3curePass.

2. After Jenkins server installation, click the Jenkins button on the top bar to access the Jenkins UI and follow on-screen instructions to create an admin user.
Ans:


To complete the Jenkins setup on the `jenkins` server using `yum` and configure the admin user, follow these steps:

---

### 🖥️ Step 1: Connect to the Jenkins Server
1. SSH into the jump host:
   
   ssh root@<jump_host_ip>
   
   Use password: `S3curePass`

2. From the jump host, SSH into the Jenkins server:
   
   ssh root@jenkins
   

---

### 📦 Step 2: Install Jenkins via `yum`
1. Add the Jenkins repository:
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat/jenkins.io-2023.key
sudo yum upgrade
# Add required dependencies for the jenkins package
sudo yum install fontconfig java-21-openjdk
sudo yum install jenkins

### ▶️ Step 3: Start Jenkins Service
1. Enable and start Jenkins:
   
   systemctl enable jenkins
   systemctl start jenkins
   

2. If you face a timeout issue:
   - Check firewall settings:
     
     firewall-cmd --permanent --add-port=8080/tcp
     firewall-cmd --reload
     
   - Confirm Jenkins is running:
     
     systemctl status jenkins
     

---

### 🌐 Step 4: Access Jenkins UI
1. Open a browser and go to:
   
   http://<jenkins_server_ip>:8080
   

2. Retrieve the initial admin password:
   
   cat /var/lib/jenkins/secrets/initialAdminPassword
   

3. Paste it into the Jenkins setup wizard.

---

### 👤 Step 5: Create Admin User
During the setup wizard:
- **Username:** `theadmin`
- **Password:** `Adm!n321`
- **Full name:** `Javed`
- **Email:** `javed@jenkins.stratos.xfusioncorp.com`


# Q2: Install Jenkins Plugins
The Nautilus DevOps team has recently setup a Jenkins server, which they want to use for some CI/CD jobs. Before that they want to install some plugins which will be used in most of the jobs. Please find below more details about the task

1. Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and Adm!n321 password.

2. Once logged in, install the Git and GitLab plugins. Note that you may need to restart Jenkins service to complete the plugins installation, If required, opt to Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre.

Note:

1. After restarting the Jenkins service, wait for the Jenkins login page to reappear before proceeding.

2. For tasks involving web UI changes, capture screenshots to share for review or consider using screen recording software like loom.com for documentation and sharing.

# Q3: Configure Jenkins User Access
The Nautilus team is integrating Jenkins into their CI/CD pipelines. After setting up a new Jenkins server, they're now configuring user access for the development team, Follow these steps:

1. Click on the Jenkins button on the top bar to access the Jenkins UI. Login with username admin and password Adm!n321.

2. Create a jenkins user named ammar with the password LQfKeWWxWD. Their full name should match Ammar.

3. Utilize the Project-based Matrix Authorization Strategy to assign overall read permission to the ammar user.

4. Remove all permissions for Anonymous users (if any) ensuring that the admin user retains overall Administer permissions.

5. For the existing job, grant ammar user only read permissions, disregarding other permissions such as Agent, SCM etc.

Note:

1. You may need to install plugins and restart Jenkins service. After plugins installation, select Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page.


2. After restarting the Jenkins service, wait for the Jenkins login page to reappear before proceeding. Avoid clicking Finish immediately after restarting the service.

Ans: 

# Q4:Organize Jenkins Jobs with Folders
xFusionCorp Industries' DevOps team aims to streamline the management of Jenkins jobs by organizing them into distinct folders based on their purpose. Complete the task following the provided requirements:


1.Access the Jenkins UI by clicking on the Jenkins button in the top bar. Log in using the credentials: username admin and password Adm!n321.

2. Create a new folder named Apache within the Jenkins UI.

3. Move the existing jobs httpd-php and services under the newly created Apache folder.

Note:

1. Ensure to install any required plugins and restart the Jenkins service if necessary. Opt for Restart Jenkins when installation is complete and no jobs are running on the plugin installation/update page.

2. Be aware that Jenkins UI may experience temporary unresponsiveness during the service restart. Refresh the UI page if needed.

3. Capture screenshots of your work for documentation and review purposes. Alternatively, utilize screen recording software like loom.com for detailed documentation and sharing.

# Q5:Configure Jenkins Job for Package Installation
Some new requirements have come up to install and configure some packages on the Nautilus infrastructure under Stratos Datacenter. The Nautilus DevOps team installed and configured a new Jenkins server so they wanted to create a Jenkins job to automate this task. Find below more details and complete the task accordingly:

1. Access the Jenkins UI by clicking on the Jenkins button in the top bar. Log in using the credentials: username admin and password Adm!n321.

2. Create a new Jenkins job named install-packages and configure it with the following specifications:

Add a string parameter named PACKAGE.
Configure the job to install a package specified in the $PACKAGE parameter on the storage server within the Stratos Datacenter.
Ans:

#### 1. **Log into Jenkins**
- Click the **Jenkins** button in the top bar.
- Use the credentials:
  - **Username:** `admin`
  - **Password:** `Adm!n321`

#### 2. **Create a New Job**
- From the Jenkins dashboard, click **New Item**.
- Enter the name: `install-packages`.
- Select **Freestyle project** and click **OK**.

#### 3. **Add a String Parameter**
- In the job configuration page:
  - Scroll to **Build Parameters**.
  - Check **This project is parameterized**.
  - Click **Add Parameter** → choose **String Parameter**.
    - **Name:** `PACKAGE`
    - **Default Value:** *(leave blank or specify a common package like `vim`)*
    - **Description:** `Name of the package to install on the storage server`
#### Generate SSH key on Jenkins
ssh-keygen -t ed25519
ssh-copy-id natasha@ststor0
#### 4. **Configure the Build Step**
- Scroll to **Build** section.
- Click **Add build step** → choose **Execute shell**.
- Enter the following shell script:

ssh -o StrictHostKeyChecking=no natasha@ststor01.stratos.xfusioncorp.com "echo 'Bl@kW' | sudo -S yum install -y $PACKAGE"
ssh natasha@ststor01 "echo 'Bl@kW' | sudo -S yum install -y $PACKAGE"

> Replace `user@storage-server` with the actual SSH user and hostname/IP of the storage server in the Stratos Datacenter.

#### 5. **Save and Run**
- Click **Save** at the bottom.
- To test, click **Build with Parameters**, enter a package name (e.g., `curl`), and click **Build**.

**Level 2:**
**Q1: Jenkins Views**
The DevOps team of xFusionCorp Industries is planning to create a number of Jenkins jobs for different tasks. So to easily manage the jobs within Jenkins UI they decided to create different views for all Jenkins jobs based on usage/nature of these jobs, - for example datacenter-crons view for all cron jobs. Based on the requirements shared below please perform the below mentioned task:

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

1. Create a Jenkins job named datacenter-test-job.

2. Configure this job to run a simple  command i.e echo "hello world!!".

3. Create a view named datacenter-crons (it must be a global view of type List View) and make sure datacenter-test-job and datacenter-cron-job (which is already present on Jenkins) jobs are listed under this new view.

4. Schedule this newly created job to build periodically at every minute i.e * * * * * (please make sure to use the cron expression exactly same how it is mentioned here)

5. Make sure the job builds successfully.

Note:

1. You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case please make sure to refresh the UI page.

2. For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:
### 🧭 **Step 1: Access Jenkins**

1. Go to the Jenkins web UI (via the link or internal dashboard provided).
2. **Login** with:

   * **Username:** `admin`
   * **Password:** `Adm!n321`

### ⚙️ **Step 2: Create a Jenkins Job**

1. On the Jenkins Dashboard, click **“New Item”** (top left corner).
2. Enter **Item Name:** `datacenter-test-job`
3. Select **“Freestyle project”**.
4. Click **OK**.

### 🧾 **Step 3: Configure the Job**

1. In the job configuration page:

   * Scroll to **Build** section.
   * Click **“Add build step” → “Execute shell”**.
   * In the command box, enter:
      echo "hello world!!"
     
2. Scroll down to the **Build Triggers** section.

   * Check **“Build periodically”**.
   * In the **Schedule** box, enter exactly:
     
     * * * * *   
   * (This means: run every minute.)
3. Click **Save**.

### 🧩 **Step 4: Create a View**

1. Go back to the **Jenkins Dashboard**.
2. Click **“+” (plus)** next to the existing tabs at the top (or **“New View”** link on the left).
3. Enter:

   * **View name:** `datacenter-crons`
   * **Type:** Select **“List View”**
4. Click **OK**.
5. On the next screen:

   * Under **Job Filters**, check **“datacenter-test-job”** and **“datacenter-cron-job”**.
   * Click **OK** or **Save**.

Now the view `datacenter-crons` should show both jobs:
✅ `datacenter-test-job`
✅ `datacenter-cron-job`

### 🧪 **Step 5: Verify Job Build**

1. Go to **datacenter-test-job**.
2. Wait one minute for the cron to trigger automatically.
3. You should see builds appearing in the **Build History** (left side).
4. Click the latest build number → then **Console Output**.

   * You should see:
    
     hello world!!
     Finished: SUCCESS

### 🧰 **Optional: Plugins & Restart**

If the **“List View”** option or **cron scheduling** doesn’t appear:

1. Go to **Manage Jenkins → Plugins → Available plugins**.
2. Search and install:

   * *View Job Filters Plugin*
   * *Build Pipeline Plugin* (optional)
3. Once installed, click **“Restart Jenkins when installation is complete and no jobs are running.”**
4. After restart, **refresh** the browser.

# *Q2:Jenkins Parameterized Builds**
A new DevOps Engineer has joined the team and he will be assigned some Jenkins related tasks. Before that, the team wanted to test a simple parameterized job to understand basic functionality of parameterized builds. He is given a simple parameterized job to build in Jenkins. Please find more details below:

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

1. Create a parameterized job which should be named as parameterized-job

2. Add a string parameter named Stage; its default value should be Build.

3. Add a choice parameter named env; its choices should be Development, Staging and Production.

4. Configure job to execute a shell command, which should echo both parameter values (you are passing in the job).

5. Build the Jenkins job at least once with choice parameter value Staging to make sure it passes.

Note:

1. You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.


2. For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:
### 🔑 Login

1. Open Jenkins in your browser.
2. Login using:

   * **Username:** `admin`
   * **Password:** `Adm!n321`

### 🧱 Step 1: Create a Parameterized Job

1. On the Jenkins dashboard, click **“New Item”** (usually on the left sidebar).
2. Enter the **Item Name** as `parameterized-job`.
3. Select **“Freestyle project”** and click **OK**.
### ⚙️ Step 2: Add Parameters

Once inside the job configuration screen:

1. Scroll down and check the box **“This project is parameterized”**.
2. Click **“Add Parameter”** → select **“String Parameter”**.

   * **Name:** `Stage`
   * **Default Value:** `Build`
   * (You can add a short description like “Pipeline stage name” if you want.)
3. Click **“Add Parameter”** again → select **“Choice Parameter”**.

   * **Name:** `env`
   * **Choices:**

     
     Development
     Staging
     Production
     
   * (Each choice on a new line.)

### 🧩 Step 3: Configure Build Step

1. Scroll to the **Build** section.
2. Click **“Add build step” → “Execute shell”**.
3. Enter the following command:

   echo "Stage parameter value: $Stage"
   echo "Environment parameter value: $env"
   
   (These will print the values passed when the job is triggered.)

### 💾 Step 4: Save the Job

1. Click **Save** at the bottom of the page.

### ▶️ Step 5: Build the Job with Parameters

1. On the job’s main page, click **“Build with Parameters”** from the left sidebar.
2. You will see two input fields:

   * **Stage** → default: `Build`
   * **env** → dropdown: `Development`, `Staging`, `Production`
3. Select **Staging** from the dropdown.
4. Click **Build**.

### 🧩 Step 6: Verify the Build

1. Once the build completes, click on the **Build Number** (e.g., `#1`) in the **Build History** sidebar.
2. Click **Console Output**.
3. You should see output similar to:
 
   Stage parameter value: Build
   Environment parameter value: Staging
   Finished: SUCCESS
   
### 🧰 Optional (If You Need Plugins)

If “Build with Parameters” doesn’t appear, you may need to install:

* **Pipeline Plugin**
* **Parameterized Trigger Plugin**

After installation:

* Click **“Restart Jenkins when installation is complete and no jobs are running”**.
* Refresh the page after Jenkins restarts.

# *Q3:Jenkins Workspaces**
Some developers are working on a common repository where they are testing some features for an application. They are having three branches (excluding the master branch) in this repository where they are adding changes related to these different features. They want to test these changes on Stratos DC app servers so they need a Jenkins job using which they can deploy these different branches as per requirements. Configure a Jenkins job accordingly.

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

Similarly, click on Gitea button to access the Gitea page. Login to Gitea server using username sarah and password Sarah_pass123.

There is a Git repository named web_app on Gitea where developers are pushing their changes. It has three branches version1, version2 and version3 (excluding the master branch). You need not to make any changes in the repository.

Create a Jenkins job named app-job.

Configure this job to have a choice parameter named Branch with choices as given below:

version1

version2

version3

Configure the job to fetch changes from above mentioned Git repository and make sure it should fetches the changes from the respective branch which you are passing as a choice in the choice parameter while building the job. For example if you choose version1 then it must fetch and deploy the changes from branch version1.

Configure this job to use custom workspace rather than a default workspace and custom workspace directory should be created under /var/lib/jenkins (for example /var/lib/jenkins/version1) location rather than under any sub-directory etc. The job should use a workspace as per the value you will pass for Branch parameter while building the job. For example if you choose version1 while building the job then it should create a workspace directory called version1 and should fetch Git repository etc within that directory only.

Configure the job to deploy code (fetched from Git repository) on storage server (in Stratos DC) under /var/www/html directory. Since its a shared volume.

You can access the website by clicking on App button.

Note:

You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case please make sure to refresh the UI page.

For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:
### ✅ Prerequisites

1. **SSH Access to `ststor01`**
   - Ensure the Jenkins server can SSH into `ststor01` without a password prompt.
   - Typically done by generating an SSH key on the Jenkins server and adding the public key to `~/.ssh/authorized_keys` on `ststor01`.

   On the Jenkins server:
   
   ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa
   ssh-copy-id user@ststor01
   

2. **Remote Directory Exists**
   - Ensure `/var/www/html` exists on `ststor01` and is writable by the SSH user.

### 🧩 Jenkins Job: `app-job` Adjustments

1. ###  **Add Choice Parameter**
- Go to **Configure** for `app-job`
- Scroll to **Build Parameters**
- Check **This project is parameterized**
- Click **Add Parameter → Choice Parameter**
  - Name: `Branch`
  - Choices:
    
    version1
    version2
    version3
    
2. **Set Custom Workspace**
- Scroll to **Advanced Project Options**
- Check **Use custom workspace**
- Set directory to:
  
  /var/lib/jenkins/${Branch}

3. **Configure Git Repository**
   - Repository: `http://git.stratos.xfusioncorp.com/sarah/web_app.git`
   - Branch: `*/${Branch}`

4. **Build Step: Remote Deployment via SCP or rsync**
   - Go to **Build → Add build step → Execute shell**
   - Use this script (replace `user` with actual SSH user on `ststor01`):

   
   echo "Deploying branch ${Branch} to ststor01"
 
   # Copy files to remote server
   scp -r /var/lib/jenkins/${Branch}/* natasha@ststor01:/var/www/html/
   

   Or, for better performance and syncing:
   
   rsync -avz --delete ./ user@ststor01:/var/www/html/
  
### 🔐 Jenkins Credentials 
If you prefer not to use SSH keys, you can:
- Add SSH credentials in **Jenkins → Manage Jenkins → Credentials**
- Use the **Publish over SSH** plugin to configure remote deployment

### ✅ Final Test
- Run **Build with Parameters**
- Choose a branch (e.g., `version1`)
- Confirm:
  - Code is fetched into `/var/lib/jenkins/version1`
  - Files are copied to `/var/www/html` on `ststor01`
  - App is accessible via the **App** button

# *Q4Jenkins Database Backup Job**
There is a requirement to create a Jenkins job to automate the database backup. Below you can find more details to accomplish this task:



Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.


Create a Jenkins job named database-backup.


Configure it to take a database dump of the kodekloud_db01 database present on the Database server in Stratos Datacenter, the database user is kodekloud_roy and password is asdfgdsd.


The dump should be named in db_$(date +%F).sql format, where date +%F is the current date.

Copy the db_$(date +%F).sql dump to the Backup Server under location /home/clint/db_backups.


Further, schedule this job to run periodically at */10 * * * * (please use this exact schedule format).


Note:


You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case please make sure to refresh the UI page.


Please make sure to define you cron expression like this */10 * * * * (this is just an example to run job every 10 minutes).


For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.
Ans:

## 🛠️ Jenkins Job Setup for Database Backup

### 1. **Login to Jenkins**
- Open Jenkins UI via the provided link or button.
- Login with:
  - **Username:** `admin`
  - **Password:** `Adm!n321`

---

### 2. **Create a New Job**
- Click **“New Item”**.
- Enter **Item Name:** `database-backup`
- Select **“Freestyle project”** and click **OK**.

---

### 3. **Configure the Job**
#### Under **Build Triggers**
- Check **“Build periodically”**
- Enter schedule: `*/10 * * * *`  
  _(This runs the job every 10 minutes)_

#### Under **Build Environment**
**Passwordless Access between jenkins server to DB and Backup Server**
ssh-keygen -t rsa -b 2048
ssh-copy-id clint@stbkp01
ssh-copy-id peter@stdb01
#### Under **Build Steps**
- Click **“Add build step” → “Execute shell”**
- Paste the following shell script:

#!/bin/bash
set -e

# Variables
DATE=$(date +%F)
DUMP_NAME="db_${DATE}.sql"
DB_USER="kodekloud_roy"
DB_PASS="asdfgdsd"
DB_NAME="kodekloud_db01"
DB_SERVER="stdb01"
BACKUP_SERVER="stbkp01"
BACKUP_PATH="/home/clint/db_backups"

echo "Creating backup directory on backup server..."
ssh clint@${BACKUP_SERVER} "mkdir -p ${BACKUP_PATH}"

echo "Dumping database from DB server..."
ssh peter@${DB_SERVER} "mysqldump -u ${DB_USER} -p${DB_PASS} ${DB_NAME}" > /tmp/${DUMP_NAME}

echo "Transferring dump to backup server..."
scp /tmp/${DUMP_NAME} clint@${BACKUP_SERVER}:${BACKUP_PATH}

echo "Cleaning up local dump..."
rm /tmp/${DUMP_NAME}

echo "Backup completed successfully."

> 🔐 Replace `<Backup_Server_IP>` with the actual IP or hostname of the Backup Server. Ensure SSH access is set up between Jenkins host and Backup Server.

### 4. **Install Required Plugins**
- Go to **Manage Jenkins → Plugins → Available**
- Search and install:
  - **SSH Plugin**
  - **Pipeline Plugin** (if using scripted pipelines)
- After installation, click **“Restart Jenkins when installation is complete…”**

### 5. **Verify & Save**
- Click **“Save”** to finalize the job.
- Run a **manual build** to test it.
- Check the **console output** for success or errors.

# *Q5Jenkins Scheduled Jobs**
The devops team of xFusionCorp Industries is working on to setup centralised logging management system to maintain and analyse server logs easily. Since it will take some time to implement, they wanted to gather some server logs on a regular basis. At least one of the app servers is having issues with the Apache server. The team needs Apache logs so that they can identify and troubleshoot the issues easily if they arise. So they decided to create a Jenkins job to collect logs from the server. Please create/configure a Jenkins job as per details mentioned below:

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321

1. Create a Jenkins jobs named copy-logs.

2. Configure it to periodically build every 3 minutes to copy the Apache logs (both access_log and error_logs) from App Server 3 (from default logs location) to location /usr/src/sysops on Storage Server.

Note:

1. You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case please make sure to refresh the UI page.

2. Please make sure to define you cron expression like this */10 * * * * (this is just an example to run job every 10 minutes).

3. For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.
Ans:
Here’s how you can **create and configure the Jenkins job (`copy-logs`)** step by step to collect Apache logs every 6 minutes from the App Server 1 (`stapp01`) and copy them to the storage server (`ststor01`) under `/usr/src/dba`.

---

### 🧠 **Goal Recap**

✅ Jenkins job name: `copy-logs`
✅ Frequency: Every 6 minutes (`*/6 * * * *`)
✅ Source: `/var/log/httpd/access_log` and `/var/log/httpd/error_log` on `stapp01`
✅ Destination: `/usr/src/dba` on `ststor01`
✅ Jenkins Server: `jenkins.stratos.xfusioncorp.com`

---

## ⚙️ Step-by-Step Setup

---

### **1. Login to Jenkins**

* Access Jenkins at:
  `http://jenkins.stratos.xfusioncorp.com:8080`
* Login using:

  
  Username: admin
  Password: Adm!n321
  

---

### **2. Install Required Plugins**

You need plugins to allow Jenkins to run shell commands and connect via SSH.

1. Go to **Manage Jenkins → Plugins → Available Plugins**.
2. Search and install the following:

   * **SSH Pipeline Steps**
   * **Publish Over SSH**
   * **Pipeline**
3. After installation, **click** “Restart Jenkins when installation is complete”.

---

### **3. Configure SSH Connections**

You’ll need SSH access for both servers (`stapp01` and `ststor01`).

#### a. Go to:

**Manage Jenkins → Configure System → Publish over SSH**

#### b. Add SSH Servers:

**For App Server 1 (Source):**


Name: stapp01
Hostname: 172.16.238.10
Username: tony
Password: Ir0nM@n


**For Storage Server (Destination):**


Name: ststor01
Hostname: 172.16.238.15
Username: natasha
Password: Bl@kW


✅ Click **Test Configuration** to verify connections.
✅ Click **Save**.

---

### **4. Create the Jenkins Job**

1. Go to the Jenkins dashboard.
2. Click **“New Item”**.
3. Enter:

   
   Item name: copy-logs
   
4. Choose **Freestyle project** → Click **OK**.

---

### **5. Configure Build Triggers**

Under **Build Triggers**, check:


Build periodically


And enter this CRON expression:


*/6 * * * *


➡️ This runs every 6 minutes.

---

### **6. Add Build Step**

Under **Build → Add build step → Execute shell**

Paste the following shell script:


#!/bin/
# Temporary location on Jenkins
WORKDIR=/tmp/apache_logs
mkdir -p $WORKDIR

# Copy logs from App Server 1
sshpass -p 'Ir0nM@n' scp -o StrictHostKeyChecking=no tony@172.16.238.10:/var/log/httpd/access_log $WORKDIR/
sshpass -p 'Ir0nM@n' scp -o StrictHostKeyChecking=no tony@172.16.238.10:/var/log/httpd/error_log $WORKDIR/

# Copy logs to Storage Server
sshpass -p 'Bl@kW' scp -o StrictHostKeyChecking=no $WORKDIR/* natasha@172.16.238.15:/usr/src/dba/


> 🧩 Note: If `sshpass` is not installed, install it with:
>
> 
> sudo yum install -y sshpass
> 

---

### **7. Save and Test the Job**

* Click **Save**.
* Click **Build Now** to run manually once.
* Then go to **Build History → Console Output** and verify:

  * Files are copied successfully.
  * No authentication or permission errors.

---

### **8. Verify on Storage Server**

SSH into the storage server:


ssh natasha@172.16.238.15
Password: Bl@kW


Check that logs are copied:


ls -l /usr/src/dba/


You should see:


access_log
error_log


---

## ✅ **Validation Checklist**

| Step                                            | Description | Status |
| ----------------------------------------------- | ----------- | ------ |
| Jenkins job `copy-logs` created                 | ✔️          |        |
| CRON schedule every 6 min (`*/6 * * * *`)       | ✔️          |        |
| Logs copied from `/var/log/httpd/` on `stapp01` | ✔️          |        |
| Logs stored in `/usr/src/dba` on `ststor01`     | ✔️          |        |
| Verified via manual test                        | ✔️          |        |

**Level 3**
# *Q1 Jenkins Slave Nodes
The Nautilus DevOps team has installed and configured new Jenkins server in Stratos DC which they will use for CI/CD and for some automation tasks. There is a requirement to add all app servers as slave nodes in Jenkins so that they can perform tasks on these servers using Jenkins. Find below more details and accomplish the task accordingly.

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

1. Add all app servers as SSH build agent/slave nodes in Jenkins. Slave node name for app server 1, app server 2 and app server 3 must be App_server_1, App_server_2, App_server_3 respectively.

2. Add labels as below:

App_server_1 : stapp01

App_server_2 : stapp02

App_server_3 : stapp03

3. Remote root directory for App_server_1 must be /home/tony/jenkins, for App_server_2 must be /home/steve/jenkins and for App_server_3 must be /home/banner/jenkins.

4. Make sure slave nodes are online and working properly.

Note:

1. You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.

2. For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.
Ans:
To complete this Jenkins configuration task, follow these steps carefully:

---

### 🛠 Pre-Requiste
Java should be installed on all server

#### 1. **Login to Jenkins**
- Go to the Jenkins UI via the "Jenkins" button on the top bar.
- Use credentials:
  - **Username:** `admin`
  - **Password:** `Adm!n321`

---

#### 2. **Install Required Plugins**
- Navigate to: **Manage Jenkins → Plugins → Available**
- Search and install:
  - **SSH Build Agents Plugin**
  - **Credentials Plugin**
- After installation, click **“Restart Jenkins when installation is complete and no jobs are running”**.

---

#### 3. **Add SSH Credentials**
- Go to: **Manage Jenkins → Credentials → (Global) → Add Credentials**
- Type: **SSH Username with Private Key**
- Add credentials for each app server:
  - **App_server_1:** Username `tony`, Private Key or password
  - **App_server_2:** Username `steve`, Private Key or password
  - **App_server_3:** Username `banner`, Private Key or password

---

#### 4. **Add Slave Nodes**
For each app server, follow these steps:

##### 🔹 App_server_1
- Go to: **Manage Jenkins → Nodes → New Node**
- Name: `App_server_1`
- Type: **Permanent Agent**
- Configure:
  - **Remote root directory:** `/home/tony/jenkins`
  - **Labels:** `stapp01`
  - **Launch method:** Launch agents via SSH
  - **Host:** IP or hostname of App Server 1
  - **Credentials:** Select `tony`'s SSH credentials
  - Save and launch agent

##### 🔹 App_server_2
- Name: `App_server_2`
- Remote root directory: `/home/steve/jenkins`
- Labels: `stapp02`
- Credentials: `steve`'s SSH credentials

##### 🔹 App_server_3
- Name: `App_server_3`
- Remote root directory: `/home/banner/jenkins`
- Labels: `stapp03`
- Credentials: `banner`'s SSH credentials

---

#### 5. **Verify Nodes Are Online**
- Go to: **Manage Jenkins → Nodes**
- Ensure all three nodes show **“Connected”** or **“Online”** status.
- If not, check:
  - SSH connectivity
  - Correct credentials
  - Proper permissions on remote directories

---

###  Optional Test
### 1. Create a New Freestyle Project

* Enter a name like: `Test_Build_App_Server_1`
* Choose **“Freestyle project”**
* Click **OK**

---

### 2. Configure the Job

Under **General →** (optional) add a description like:

> “Simple test build to verify SSH agent connection on App_server_1”

---

### 3. Restrict Job to a Specific Node

Scroll down to **“General”** section and:

* Check ✅ **Restrict where this project can be run**
* In the **Label Expression** box, enter the label of the node you want to test:

  * For App_server_1 → `stapp01`
  * For App_server_2 → `stapp02`
  * For App_server_3 → `stapp03`

This tells Jenkins to run the job only on that agent.

# *Q2 Jenkins Project Security
The xFusionCorp Industries has recruited some new developers. There are already some existing jobs on Jenkins and two of these new developers need permissions to access those jobs. The development team has already shared those requirements with the DevOps team, so as per details mentioned below grant required permissions to the developers.

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

There is an existing Jenkins job named Packages, there are also two existing Jenkins users named sam with password sam@pass12345 and rohan with password rohan@pass12345.

Grant permissions to these users to access Packages job as per details mentioned below:

a.) Make sure to select Inherit permissions from parent ACL under inheritance strategy for granting permissions to these users.

b.) Grant mentioned permissions to sam user : build, configure and read.

c.) Grant mentioned permissions to rohan user : build, cancel, configure, read, update and tag.

Note:

Please do not modify/alter any other existing job configuration.

You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.

For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:
Here’s exactly how to complete this Jenkins permissions task step-by-step:

---

### **Step 1: Log into Jenkins**

1. Open the Jenkins UI (click the **Jenkins** button on the top bar).
2. Login with:
   **Username:** `admin`
   **Password:** `Adm!n321`

---

### **Step 2: Confirm the Job and Users**

1. On the Jenkins dashboard, verify that the job named **“Packages”** exists.
2. Check that the users **sam** and **rohan** exist:

   * Go to **Manage Jenkins → Manage Users**.
   * Ensure both are listed:

     * `sam / sam@pass12345`
     * `rohan / rohan@pass12345`

---

### **Step 3: Verify or Install Role/Matrix Authorization Plugin**

To assign fine-grained permissions to specific users on a specific job, you need the **Matrix Authorization Strategy Plugin** (or **Role-Based Authorization Strategy Plugin**).

1. Go to **Manage Jenkins → Plugins → Available Plugins**.
2. Search for **Matrix Authorization Strategy Plugin**.
3. Install it.
4. Once installed, choose **Restart Jenkins when installation is complete and no jobs are running**.

---

### **Step 4: Enable Project-Based Matrix Authorization**

1. Go to the Jenkins dashboard.
2. Click on the job **Packages**.
3. Select **Configure**.
4. Scroll down to the **Build Authorization Strategy** section (if not visible, enable it under **Manage Jenkins → Configure Global Security**).
5. Under **Enable project-based security**, check the box.

---

### **Step 5: Set Inheritance and Add Permissions**

1. Under **Inheritance Strategy**, select:
   ✅ **Inherit permissions from parent ACL**
2. You’ll now see a permissions matrix table.

---

### **Step 6: Grant Permissions for Each User**

#### **For `sam`:**

Grant the following permissions:

* ✅ **Job → Build**
* ✅ **Job → Configure**
* ✅ **Job → Read**

To do this:

* Click **Add user or group**, type `sam`, press Enter.
* Then check the three boxes mentioned above for `sam`.

#### **For `rohan`:**

Grant the following permissions:

* ✅ **Job → Build**
* ✅ **Job → Cancel**
* ✅ **Job → Configure**
* ✅ **Job → Read**
* ✅ **Job → Update**
* ✅ **Job → Tag**

To do this:

* Click **Add user or group**, type `rohan`, press Enter.
* Then check the boxes for these six permissions.

---

### **Step 7: Save Configuration**

* Click **Save** (or **Apply and Save**) at the bottom of the job configuration page.

---

### **Step 8: Verify Permissions**

1. Log out of Jenkins.
2. Log in as **sam (sam@pass12345)** and verify:

   * Can open and read the “Packages” job.
   * Can configure and build it.
   * Cannot perform other restricted actions.
3. Log out, then log in as **rohan (rohan@pass12345)** and verify:

   * Can build, cancel builds, configure, update, tag, and read the job.



# *Q3 Jenkins Build Images
One of the DevOps engineers was working on to create a Dockerfile for Nginx. We need to build an image using that Dockerfile. The deployment must be done using a Jenkins pipeline. Below you can find more details about the same.

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

Similarly, click on the Gitea button on the top bar to access the Gitea UI. Login using username sarah and password Sarah_pass123. There is a repository named sarah/web in Gitea.

Create/configure a Jenkins pipeline job named nginx-container, configure it to run on server App Server 3.

The pipeline can have just one stage named Build. (name is case sensitive)

In the Build stage, build an image named stregi01.stratos.xfusioncorp.com:5000/nginx:latest using the Dockerfile present under the Git repository. stregi01.stratos.xfusioncorp.com:5000 is the image registry server. After building the image push the same to the image registry server.

Note:

You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.

For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:
Here’s a **step-by-step guide** to complete the Jenkins pipeline deployment task you described — building and pushing an Nginx Docker image from a Gitea repo.

---

## 🚀 Objective

Create a **Jenkins pipeline job** called `nginx-container` that:

* Builds a Docker image using the Dockerfile in `sarah/web` repo (on Gitea)
* Tags it as `stregi01.stratos.xfusioncorp.com:5000/nginx:latest`
* Pushes it to the Docker registry at `stregi01.stratos.xfusioncorp.com:5000`
* Runs on **App Server 3**
* Has **one stage only** → `Build`

---

## 🧰 Step 1: Jenkins Access and Setup

1. Click **Jenkins** (from top bar).

2. Login:

   * **Username:** `admin`
   * **Password:** `Adm!n321`

3. If this is the first time logging in:

   * Go to **Manage Jenkins → Plugins → Available plugins**
   * Install:

     * **Docker Pipeline**
     * **Git plugin**
     * **Pipeline: Job , Pipeline,Pipeline: API plugins**
     * **Credentials Binding Plugin**
     * **SSH Build Agents**
   * Click **“Download now and install after restart”**
   * Then select **“Restart Jenkins when installation is complete”**
## 🧱 Step 2: Create Jenkins Credentials

1. Go to **Manage Jenkins → Credentials → (global)** → **Add Credentials**
2. Add:

   * **Type:** Username with password
   * **ID:** `gitea-cred`
   * **Username:** `sarah`
   * **Password:** `Sarah_pass123`
3. Add another credential for Docker registry:

   * **Type:** Username with password
   * **ID:** `docker-registry-cred`
   * (Use the registry credentials if available; if not, use the same Jenkins admin credentials if permitted)

---

## 🧑‍💻 Step 3: Create Pipeline Job

1. From Jenkins dashboard → **New Item**
2. Enter name: `nginx-container`
3. Choose **Pipeline** → Click **OK**
4. Under **General**, check **Restrict where this project can be run**

   * Label Expression: `App Server 3`
5. Under **Pipeline Definition**, choose **Pipeline script from SCM**

   * **SCM:** Git
   * **Repository URL:** (from Gitea)

     
     http://gitea.stratos.xfusioncorp.com/sarah/web.git
     
   * **Credentials:** Select `gitea-cred`
   * **Branch Specifier:** `*/main` or `*/master` (verify in Gitea)
   * **Script Path:** `Jenkinsfile` (you’ll create this next)

---

## 🧾 Step 4: Create the Jenkinsfile in Gitea Repo

Login to **Gitea** (`sarah / Sarah_pass123`):

1. Open repo: `sarah/web`
2. Click **Add File → Create New File**
3. Name it: `Jenkinsfile`
4. Paste the following content:


pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Docker registry details
                    def registry = "stregi01.stratos.xfusioncorp.com:5000"
                    def imageName = "${registry}/nginx:latest"

                    // Build the image
                    echo "Building Docker image..."
                    sh "docker build -t ${imageName} ."

                    // If docker cred avail to the Login and push else without login step, process other command
                    withCredentials([usernamePassword(credentialsId: 'docker-registry-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                        sh "echo $PASS | docker login ${registry} -u $USER --password-stdin"
                        sh "docker push ${imageName}"
                        sh "docker logout ${registry}"
                    }
                }
            }
        }
    }
}


5. Commit the file directly to the default branch (main/master).

---

## ⚙️ Step 5: Run the Pipeline

1. Go back to Jenkins → **nginx-container**
2. Click **Build Now**
3. Monitor progress under **Build Console Output**

Expected output:

* Docker image builds successfully using the repo’s Dockerfile
* Image is pushed to:
  `stregi01.stratos.xfusioncorp.com:5000/nginx:latest`
* Stage name shows as **Build**

---

## ✅ Step 6: Verify the Image

On **App Server 3**, verify with:


docker login stregi01.stratos.xfusioncorp.com:5000
docker pull stregi01.stratos.xfusioncorp.com:5000/nginx:latest
docker images


You should see the new image listed.

---

## 🧩 Troubleshooting Tips

* If `docker` command not found → install Docker on App Server 3.
* If Jenkins can’t use Docker → ensure Jenkins user is in the `docker` group:

  
  sudo usermod -aG docker jenkins
  sudo systemctl restart jenkins
  
* If authentication fails during push → double-check credentials for the registry.

# *Q4 Jenkins Deploy Pipeline
The development team of xFusionCorp Industries is working on to develop a new static website and they are planning to deploy the same on Nautilus App Servers using Jenkins pipeline. They have shared their requirements with the DevOps team and accordingly we need to create a Jenkins pipeline job. Please find below more details about the task:

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

Similarly, click on the Gitea button on the top bar to access the Gitea UI. Login using username sarah and password Sarah_pass123. There under user sarah you will find a repository named web_app that is already cloned on Storage server under /var/www/html. sarah is a developer who is working on this repository.

Add a slave node named Storage Server. It should be labeled as ststor01 and its remote root directory should be /var/www/html.

We have already cloned repository on Storage Server under /var/www/html.

Apache is already installed on all app Servers its running on port 8080.

Create a Jenkins pipeline job named nautilus-webapp-job (it must not be a Multibranch pipeline) and configure it to:

Deploy the code from web_app repository under /var/www/html on Storage Server, as this location is already mounted to the document root /var/www/html of app servers. The pipeline should have a single stage named Deploy ( which is case sensitive ) to accomplish the deployment.

LB server is already configured. You should be able to see the latest changes you made by clicking on the App button. Please make sure the required content is loading on the main URL https://<LBR-URL> i.e there should not be a sub-directory like https://<LBR-URL>/web_app etc.

Note:

You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.

For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:
Here's a step-by-step guide to help you complete the Jenkins pipeline deployment for xFusionCorp Industries:

---

## ✅ Step-by-Step Instructions

### 1. **Access Jenkins and Gitea**
- **Jenkins UI**: Click the Jenkins button → Login with:
  - Username: `admin`
  - Password: `Adm!n321`
- **Gitea UI**: Click the Gitea button → Login with:
  - Username: `sarah`
  - Password: `Sarah_pass123`
  - Locate the repository: `web_app` under user `sarah`

---

### 2. **Add Jenkins Slave Node (Storage Server)**
**Login into Storage Server Change Permission and Install java**
sudo chown -R natasha:natasha /var/www/html
sudo chmod -R 755 /var/www/html
 then 
- Go to **Manage Jenkins** → **Manage Nodes and Clouds**
- Click **New Node**
  - Name: `Storage Server`
  - Type: **Permanent Agent**
- Configure the node:
  - **# of Executors**: 1
  - **Remote root directory**: `/var/www/html`
  - **Labels**: `ststor01`
  - **Launch method**: Use SSH or appropriate method to connect to Storage Server
- Save and ensure the node is **online**

---

### 3. **Create Jenkins Pipeline Job**
- Go to Jenkins Dashboard → Click **New Item**
  - Name: `nautilus-webapp-job`
  - Type: **Pipeline**
- Click OK and configure:
  - **Description**: Deploy static website from Gitea to Storage Server
  - **Restrict where this project can run**: `ststor01`

---

### 4. **Configure Pipeline Script**
In the **Pipeline** section, choose **Pipeline script** and paste the following:


pipeline {
    agent { label 'ststor01' }

    stages {
        stage('Deploy') {
            steps {
                echo 'Deploying web_app to /var/www/html...'
                sh '''
                    cd /var/www/html/
                    git clone http://git.stratos.xfusioncorp.com/sarah/web_app.git /tmp/web_app
                    cp -r /tmp/web_app/* /var/www/html/
                '''
            }
        }
    }
}



### 5. **Install Required Plugins**
- Go to **Manage Jenkins** → **Plugins**
- Install:
  - **Pipeline**
  - **Git**
  - **SSH BuildAgent** 
- After installation, click **Restart Jenkins when installation is complete and no jobs are running**


### 6. **Verify Deployment**
- Click the **App** button to access the Load Balancer URL
- Confirm the site loads at `https://<LBR-URL>` (not in a subdirectory)
- If needed, remove nested `web_app` folder and move contents directly to `/var/www/html`


# *Q5 Jenkins Conditional Pipeline
The development team of xFusionCorp Industries is working on to develop a new static website and they are planning to deploy the same on Nautilus App Servers using Jenkins pipeline. They have shared their requirements with the DevOps team and accordingly we need to create a Jenkins pipeline job. Please find below more details about the task:

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

Similarly, click on the Gitea button on the top bar to access the Gitea UI. Login using username sarah and password Sarah_pass123. There under user sarah you will find a repository named web_app that is already cloned on Storage server under /var/www/html. sarah is a developer who is working on this repository.

Add a slave node named Storage Server. It should be labeled as ststor01 and its remote root directory should be /var/www/html.

We have already cloned repository on Storage Server under /var/www/html.

Apache is already installed on all app Servers its running on port 8080.

Create a Jenkins pipeline job named datacenter-webapp-job (it must not be a Multibranch pipeline) and configure it to:

Add a string parameter named BRANCH.

It should conditionally deploy the code from web_app repository under /var/www/html on Storage Server, as this location is already mounted to the document root /var/www/html of app servers. The pipeline should have a single stage named Deploy ( which is case sensitive ) to accomplish the deployment.

The pipeline should be conditional, if the value master is passed to the BRANCH parameter then it must deploy the master branch, on the other hand if the value feature is passed to the BRANCH parameter then it must deploy the feature branch.

LB server is already configured. You should be able to see the latest changes you made by clicking on the App button. Please make sure the required content is loading on the main URL https://<LBR-URL> i.e there should not be a sub-directory like https://<LBR-URL>/web_app etc.
Ans:

### 🛠️ Step 1: Add the Storage Server as a Jenkins Slave Node

1. **Login to Jenkins UI** using:
   - Username: `admin`
   - Password: `Adm!n321`

2. Go to **Manage Jenkins → Nodes → New Node**:
**Login into Storage Server Change Permission and Install java**
sudo chown -R sarah:sarah /var/www/html
sudo chmod -R 755 /var/www/html
 then 
   - Name: `Storage Server`
   - Type: `Permanent Agent`
   - Labels: `ststor01`
   - Remote root directory: `/var/www/html`
   - Launch method: Choose appropriate method (e.g., SSH or via agent script)
   - Save and connect the node

---

### 📦 Step 2: Verify Repository on Storage Server

Ensure that the repository is already cloned under `/var/www/html`. You can verify this by logging into the Storage Server and running:


cd /var/www/html/
git status


---

### 🚀 Step 3: Create Jenkins Pipeline Job

1. In Jenkins UI, go to **New Item**:
   - Name: `xfusion-webapp-job`
   - Type: `Pipeline`
   - Click OK

2. Under **General → This project is parameterized**:
   - Add **String Parameter**:
     - Name: `BRANCH`
     - Default value: `master` (optional)

---

### 📄 Step 4: Configure Pipeline Script

Paste the following into the **Pipeline Script** section:

pipeline {
    agent { label 'ststor01' }

    parameters {
        string(name: 'BRANCH', defaultValue: 'master', description: 'Branch to deploy (master or feature)')
    }

    stages {
        stage('Deploy') {
            steps {
                script {
                    if (params.BRANCH == 'master') {
                        echo "Deploying master branch..."
                        sh '''
                            cd /var/www/html/
                            git fetch origin
                            git checkout master
                            git pull origin master
                        '''
                    } else if (params.BRANCH == 'feature') {
                        echo "Deploying feature branch..."
                        sh '''
                            cd /var/www/html/
                            git fetch origin
                            git checkout feature
                            git pull origin feature
                        '''
                    } else {
                        error "Invalid branch specified: ${params.BRANCH}. Use master or feature."
                    }
                }
            }
        }
    }
}


---

### 🌐 Step 5: Validate Deployment

- Click the **App** button or visit `https://<LBR-URL>` directly.
- Ensure the content loads from `/var/www/html` without any subdirectory like `/web_app`.

---

### 🔄 Optional: Plugin Installation & Restart

If required:
- Go to **Manage Jenkins → Plugin Manager**
- Install necessary plugins (e.g., Pipeline, Git)
- Click **Restart Jenkins when installation is complete and no jobs are running**


**Level 4**
# *Q1 Jenkins Deployment Job
The Nautilus development team had a meeting with the DevOps team where they discussed automating the deployment of one of their apps using Jenkins (the one in Stratos Datacenter). They want to auto deploy the new changes in case any developer pushes to the repository. As per the requirements mentioned below configure the required Jenkins job.

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and Adm!n321 password.

Similarly, you can access the Gitea UI using Gitea button, username and password for Git is sarah and Sarah_pass123 respectively. Under user sarah you will find a repository named web that is already cloned on the Storage server under sarah's home. sarah is a developer who is working on this repository.

1. Install httpd (whatever version is available in the yum repo by default) and configure it to serve on port 8080 on All app servers. You can make it part of your Jenkins job or you can do this step manually on all app servers.

2. Create a Jenkins job named nautilus-app-deployment and configure it in a way so that if anyone pushes any new change to the origin repository in master branch, the job should auto build and deploy the latest code on the Storage server under /var/www/html directory. Since /var/www/html on Storage server is shared among all apps.
Before deployment, ensure that the ownership of the /var/www/html directory is set to user sarah, so that Jenkins can successfully deploy files to that directory.

3. SSH into Storage Server using sarah user credentials mentioned above. Under sarah user's home you will find a cloned Git repository named web. Under this repository there is an index.html file, update its content to Welcome to the xFusionCorp Industries, then push the changes to the origin into master branch. This push must trigger your Jenkins job and the latest changes must be deployed on the servers, also make sure it deploys the entire repository content not only index.html file.

Click on the App button on the top bar to access the app, you should be able to see the latest changes you deployed. Please make sure the required content is loading on the main URL https://<LBR-URL> i.e there should not be any sub-directory like https://<LBR-URL>/web etc.

Note:
1. You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also some times Jenkins UI gets stuck when Jenkins service restarts in the back end so in such case please make sure to refresh the UI page.

2. Make sure Jenkins job passes even on repetitive runs as validation may try to build the job multiple times.

3. Deployment related tasks should be done by sudo user on the destination server to avoid any permission issues so make sure to configure your Jenkins job accordingly.

4. For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:

## ✅ Step 1: Install and Configure `httpd` on All App Servers

You can do this manually or via Jenkins. Here's how to do it manually:

1. **SSH into each app server**.
2. Run the following commands:
   
   sudo yum install httpd -y
   sudo sed -i 's/Listen 80/Listen 8080/' /etc/httpd/conf/httpd.conf
   sudo systemctl enable httpd
   sudo systemctl start httpd
   ss -tulnp | grep 8080


---

This is a comprehensive task involving **Jenkins, Gitea, SSH, and basic web server configuration**. I will guide you through the necessary steps to set up the continuous deployment pipeline as requested.

-----

## 🚀 Part 1: Install and Configure HTTPD on App Servers

The first step is to ensure **HTTPD** is running on the specified port on all App servers. Since the requirement mentions the App servers, and the deployment target is the **Storage Server**'s `/var/www/html` directory which is shared, the App servers will serve the content from that shared location.

### Manual Configuration on App Servers

You need to SSH into each App server and run these commands.

1.  **Install `httpd`:**
    
    sudo yum install httpd -y
    
2.  **Change the listening port to 8080:**
      * Edit the main configuration file: `sudo vi /etc/httpd/conf/httpd.conf`
      * Find the line that says `Listen 80` and change it to:
        conf
        Listen 8080
        
3.  **Set the DocumentRoot:**
      * Find the line `DocumentRoot "/var/www/html"` and ensure it points to the correct shared directory. Since the requirement specifies deployment to **Storage Server's** `/var/www/html`, and this is a shared mount, this step should be correct by default.
4.  **Start and Enable the `httpd` service:**
    
    sudo systemctl start httpd
    sudo systemctl enable httpd
    

**Note:** Repeat these steps for **all App servers**.

-----

## 🛠️ Part 2: Configure Jenkins for Auto-Deployment

This section involves installing necessary plugins, configuring SSH credentials, and setting up the Jenkins job.

### 2.1 Install Required Plugins

You will likely need the **Git Plugin** (usually installed by default) and the **Pipeline Plugin** (also often default). Most critically, you will need the **Generic Webhook Trigger Plugin** for Gitea to trigger the job.

1.  Log in to Jenkins with `admin`/`Adm!n321`.
2.  Go to **Manage Jenkins** $\rightarrow$ **Manage Plugins**.
3.  Go to the **Available** tab and search for and install:
      * **Generic Webhook Trigger Plugin**
4.  After installation, click the **Restart Jenkins** checkbox and wait for the service to restart.

### 2.2 Configure SSH for Deployment

Jenkins needs to be able to connect to the **Storage Server** as user `sarah` to deploy the files.

1.  Go to **Manage Jenkins** $\rightarrow$ **Configure System**.
2.  Scroll down to the **Publish over SSH** section.
3.  Click **Add**.
      * **Name:** `Storage-Server`
      * **Hostname:** The IP or hostname of the **Storage Server**.
      * **Username:** `sarah`
      * **Remote Directory:** `/var/www/html` (This is the default path that the job will use).
      * Click **Advanced**.
      * Select **Use password authentication**.
      * **Passphrase:** `Sarah_pass123`
      * Click **Test Configuration** to ensure it connects successfully.
      * Click **Save**.

### 2.3 Create and Configure the Jenkins Job

1.  Click **New Item** on the Jenkins dashboard.
2.  **Item Name:** `nautilus-app-deployment`
3.  Select **Freestyle project**.
4.  Click **OK**.

#### A. Source Code Management

  * Select **Git**.
  * **Repository URL:** The Gitea URL for the `sarah/web` repository (e.g., `http://<Gitea_IP_or_URL>/sarah/web.git`). http://git.stratos.xfusioncorp.com/sarah/web.git
  * **Credentials:** Click **Add** $\rightarrow$ **Jenkins**.
      * **Kind:** **Username with password**
      * **Username:** `sarah`
      * **Password:** `Sarah_pass123`
      * **ID:** `gitea-sarah` (or similar)
      * Click **Add**. Select the newly created credential.
  * **Branches to build:** `*/master` (Keep the default).

#### B. Build Triggers (WebHook)
Enable “Trigger builds remotely (e.g., from scripts)”:
http://172.16.238.19:8080/job/nautilus-app-deployment/build


## Configure Generic Webhook Trigger

In Build Triggers, check:

✔ Generic Webhook Trigger

🔹 Token

Set a token (example):

nautilus-webhook

🔹 Post content parameters

Leave empty (not required for this lab).

🔹 Headers

Leave empty.

🔹 Optional filter

Leave unchecked.

#### C. Build Steps (Deployment)

First, you need a step to **set the ownership** of the deployment directory on the Storage Server.

1.  Click **build Execute shell**.

sshpass -p 'Sarah_pass123' ssh -o StrictHostKeyChecking=no sarah@<Storage-Server-IP> << EOF
cp -r ~/web/* /var/www/html/
EOF

-----

## 🔗 Part 3: Configure Gitea Webhook

Now, you need to tell Gitea to notify Jenkins when a push happens.

1.  Access the Gitea UI with `sarah`/`Sarah_pass123`.
2.  Navigate to the **web** repository.
3.  Go to **Repository Settings** $\rightarrow$ **Webhooks**.
4.  Click **Add Webhook** $\rightarrow$ **Gitea**.
      * **Target URL:** The Jenkins URL with the webhook trigger. It should look like this:
        
        http://<JENKINS_IP_or_URL>/generic-webhook-trigger/invoke?token=nautilus_secret_token

        http://172.16.238.19:8080/generic-webhook-trigger/invoke?token=nautilus-webhook
        
        
        Replace `<JENKINS_IP_or_URL>` and use the token you set in the job (`nautilus_secret_token`).
      * **HTTP Method:** **POST**
      * **Content Type:** **application/json**
      * **Trigger On:** Check **Just the Push event**.
      * Click **Add Webhook**.
      * Click **Test Delivery** to ensure Jenkins receives the payload successfully (it might show a 400 or 404 the first time, but check the Jenkins logs/job history to ensure it's functional).

-----

## 💾 Part 4: Trigger the Deployment

This is the final step where you make a change to initiate the pipeline.

1.  SSH into the **Storage Server** using `sarah`/`Sarah_pass123`.
2.  Navigate to the cloned repository:
    
    cd ~/web
    
3.  Modify the `index.html` file:
    
    vi index.html
    # Update content to: Welcome to the xFusionCorp Industries
    
4.  Stage, commit, and push the changes:
    
    git add .
    git commit -m "Updated main welcome message"
    git push origin master
    

# *Q2 Jenkins Chained Builds
The DevOps team was looking for a solution where they want to restart Apache service on all app servers if the deployment goes fine on these servers in Stratos Datacenter. After having a discussion, they came up with a solution to use Jenkins chained builds so that they can use a downstream job for services which should only be triggered by the deployment job. So as per the requirements mentioned below configure the required Jenkins jobs.

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and Adm!n321 password.

Similarly you can access Gitea UI on port 8090 and username and password for Git is sarah and Sarah_pass123 respectively. Under user sarah you will find a repository named web.

Apache is already installed and configured on all app server so no changes are needed there. The doc root /var/www/html on all these app servers is shared among the Storage server under /var/www/html directory.

1. Create a Jenkins job named nautilus-app-deployment and configure it to pull change from the master branch of web repository on Storage server under /var/www/html directory, which is already a local git repository tracking the origin web repository. Since /var/www/html on Storage server is a shared volume so changes should auto reflect on all apps.

2. Create another Jenkins job named manage-services and make it a downstream job for nautilus-app-deployment job. Things to take care about this job are:

a. This job should restart httpd service on all app servers.

b. Trigger this job only if the upstream job i.e nautilus-app-deployment is stable.

LB server is already configured. Click on the App button on the top bar to access the app. You should be able to see the latest changes you made. Please make sure the required content is loading on the main URL https://<LBR-URL> i.e there should not be a sub-directory like https://<LBR-URL>/web etc.

Note:

1. You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also some times Jenkins UI gets stuck when Jenkins service restarts in the back end so in such case please make sure to refresh the UI page.

2. Make sure Jenkins job passes even on repetitive runs as validation may try to build the job multiple times.

3. Deployment related tasks should be done by sudo user on the destination server to avoid any permission issues so make sure to configure your Jenkins job accordingly.

4. For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:
## ✅ Job 1: `nautilus-app-deployment`

### 🎯 Goal:
Pull latest code from the `web` repository (hosted on Gitea) into `/var/www/html` on the Storage server (`ststor01`), which is shared with all app servers.

### 🔧 Configuration Steps:

1. **Login to Jenkins**
   - URL: `http://jenkins.stratos.xfusioncorp.com`
   - Username: `admin`
   - Password: `Adm!n321`

2. **Create Freestyle Project**
   - Name: `nautilus-app-deployment`

3. **Source Code Management**
   - Select **Git**
   - Repository URL: `/var/www/html` (since it's a local Git repo on `ststor01`)
   - Branch: `master`

4. **Build Environment**
   - Ensure Jenkins has SSH access to `ststor01` as user `natasha` (password: `Bl@kW`)
   - Use SSH credentials or `sshpass` in shell script

5. **Build Step: Execute Shell**
   
   sshpass -p 'Bl@kW' ssh -o StrictHostKeyChecking=no natasha@172.16.238.15 "cd /var/www/html && git pull origin master"
   

6. **Post-build Actions**
   - Add **Build other projects**
   - Project to build: `manage-services`
   - Trigger only if build is **stable**

## ✅ Job 2: `manage-services`

### 🎯 Goal:
Restart Apache (`httpd`) service on all app servers (`stapp01`, `stapp02`, `stapp03`) only if deployment succeeds.

### 🔧 Configuration Steps:

1. **Create Freestyle Project**
   - Name: `manage-services`

2. **Build Triggers**
   - Leave empty (triggered by upstream job)

3. **Build Step: Execute Shell**
   
   for host in stapp01.stratos.xfusioncorp.com stapp02.stratos.xfusioncorp.com stapp03.stratos.xfusioncorp.com; do
     case $host in
       stapp01*) user="tony"; pass="Ir0nM@n" ;;
       stapp02*) user="steve"; pass="Am3ric@" ;;
       stapp03*) user="banner"; pass="BigGr33n" ;;
     esac
     sshpass -p "$pass" ssh -o StrictHostKeyChecking=no $user@$host " echo $pass | sudo -S systemctl restart httpd"
   done
   

> 🔐 **Note:** Ensure `sshpass` is installed on the Jenkins server. Alternatively, configure SSH keys and use Jenkins credentials securely.

---

## 🔍 Validation

After setting up:

1. **Push a change** to the `web` repo via Gitea (port 8090)
   - Login: `sarah / Sarah_pass123`
   - Repo: `web`
   - Push to `master`

2. **Run `nautilus-app-deployment`**
   - It should pull the latest code to `/var/www/html` on `ststor01`

3. **Check `manage-services`**
   - It should restart Apache on all app servers

4. **Verify App**
   - Visit: `https://stlb01.stratos.xfusioncorp.com`
   - Ensure latest content is visible (no `/web` subdirectory)

# *Q3 Jenkins MR Jobs
Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.


Similarly, click on the Gitea button on the top bar to access the Gitea UI. Login using username sarah and password Sarah_pass123.

There is a repository named sarah/mr_job in Gitea, which is cloned on the Storage server under /home/natasha/mr_job directory.

Update the index.html file under dev branch, and change its content from Welcome to Nautilus Group! to Welcome to xFusionCorp Industries!. Remember to push your changes to the origin repository.

After pushing the required changes, login to the Gitea server and you will find a pull request with title My First PR under mr_job repository. Merge this pull request.

Create/configure a Jenkins pipeline job named nginx-container, configure a pipeline as per details given below and run the pipeline on server App Server 3.

The pipeline must have two stages Build and Deploy (names are case sensitive).

In the Build stage, first clone the sarah/mr_job repository, then build an image named stregi01.stratos.xfusioncorp.com:5000/nginx:latest using the Dockerfile present under the root of the repository. stregi01.stratos.xfusioncorp.com:5000 is the image registry server. After building the image push the same to the image registry server.

In the Deploy stage, create a container named nginx-app using the image you built in the Build stage. Make sure to map container port to the host port 8080 and run the container in detached mode.

Make sure to build a successful job at least once so that you have at least one successful build # in the job history. Further, you can test the app using command curl http://stapp03:8080 from the jump host.

Note:

1. You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.


2. For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:
## 🛠️ Part 1: Update `index.html` in Gitea Repository

### 1. Access Gitea UI
- Click the **Gitea** button on the top bar.
- Login with:
  - **Username:** `sarah`
  - **Password:** `Sarah_pass123`

### 2. Modify the Repository
- Navigate to the `sarah/mr_job` repository.
- Switch to the **dev** branch.
- Open `index.html` and click **Edit**.
- Change the content:
  html
  Welcome to Nautilus Group!
  
  to:
  html
  Welcome to xFusionCorp Industries!
  
- Commit the change with a message like `"Updated welcome message"`.

### 3. Push Changes
- If working locally on the Storage server:
  
  cd /home/natasha/mr_job
  git checkout dev
  sed -i 's/Welcome to Nautilus Group!/Welcome to xFusionCorp Industries!/' index.html
  git add index.html
  git commit -m "Updated welcome message"
  git push origin dev
  

---

## 🔀 Part 2: Merge Pull Request in Gitea

- Go back to the Gitea UI.
- Navigate to the `mr_job` repository.
- You should see a pull request titled **My First PR**.
- Open it and click **Merge**.

---

## 🚀 Part 3: Jenkins Pipeline Setup

### 1. Access Jenkins UI
- Click the **Jenkins** button on the top bar.
- Login with:
  - **Username:** `admin`
  - **Password:** `Adm!n321`

### 2. Install Required Plugins
- Go to **Manage Jenkins > Plugins**.
- Install:
  - Docker Pipeline
  - Git plugin
  - SSH Build Agent
- Restart Jenkins if prompted.
**Add Slave Nodes**
For app server3 , follow these steps:
Install openjdk on stapp03
##### 🔹 App_server_3
- Go to: **Manage Jenkins → Nodes → New Node**
- Name: `App_server_3`
- Type: **Permanent Agent**
- Configure:
  - **Remote root directory:** `/home/banner/jenkins`
  - **Labels:** `stapp03`
  - **Launch method:** Launch agents via SSH
  - **Host:** IP or hostname of App Server 1
  - **Credentials:** Select `tony`'s SSH credentials
  - Save and launch agent
### 3. Create Pipeline Job
- Go to **New Item**.
- Name it: `nginx-container`
- Select **Pipeline**, then click OK.

### 4. Configure Pipeline Script
Paste the following into the pipeline script section:

pipeline {
    agent { label 'stapp03' }

    stages {
        stage('Build') {
            steps {
                git branch: 'dev', credentialsId: 'git-pass', url: 'http://git.stratos.xfusioncorp.com/sarah/mr_job.git'
                sh '''
                    docker build -t stregi01.stratos.xfusioncorp.com:5000/nginx:latest .
                    docker push stregi01.stratos.xfusioncorp.com:5000/nginx:latest
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker run -d --name nginx-app -p 8080:80 stregi01.stratos.xfusioncorp.com:5000/nginx:latest
                '''
            }
        }
    }
}

> 🔧 Adjust the `git url` if needed based on your Gitea server address.

### 5. Run the Pipeline
- Click **Build Now**.
- Wait for the job to complete successfully.

---

## ✅ Final Verification

- From the **jump host**, run:
  
  curl http://stapp03:8080
  
- You should see:
  
  Welcome to xFusionCorp Industries!
  

---


# *Q4 Jenkins Multistage Pipeline
The development team of xFusionCorp Industries is working on to develop a new static website and they are planning to deploy the same on Nautilus App Servers using Jenkins pipeline. They have shared their requirements with the DevOps team and accordingly we need to create a Jenkins pipeline job. Please find below more details about the task:

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

Similarly, click on the Gitea button on the top bar to access the Gitea UI. Login using username sarah and password Sarah_pass123.

There is a repository named sarah/web in Gitea that is already cloned on Storage server under /var/www/html directory.

Update the content of the file index.html under the same repository to Welcome to xFusionCorp Industries and push the changes to the origin into the master branch.

Apache is already installed on all app Servers its running on port 8080.

Create a Jenkins pipeline job named deploy-job (it must not be a Multibranch pipeline job) and pipeline should have two stages Deploy and Test ( names are case sensitive ). Configure these stages as per details mentioned below.

a. The Deploy stage should deploy the code from web repository under /var/www/html on the Storage Server, as this location is already mounted to the document root /var/www/html of all app servers.

b. The Test stage should just test if the app is working fine and website is accessible. Its up to you how you design this stage to test it out, you can simply add a curl command as well to run a curl against the LBR URL (http://stlb01:8091) to see if the website is working or not. Make sure this stage fails in case the website/app is not working or if the Deploy stage fails.

Click on the App button on the top bar to see the latest changes you deployed. Please make sure the required content is loading on the main URL http://stlb01:8091 i.e there should not be a sub-directory like http://stlb01:8091/web etc.

Note:

You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.

For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.
Ans:
Here’s a step-by-step guide to help you complete the Jenkins pipeline deployment task for xFusionCorp Industries:

## 🛠️ Step-by-Step Instructions

### 1. 🔐 Login to Gitea
- Go to the Gitea UI via the top bar.
- Login with:
  - **Username:** `sarah`
  - **Password:** `Sarah_pass123`

### 2. 📝 Update `index.html`
- Navigate to the `sarah/web` repository.
- Edit the `index.html` file.
- Change its content to:
  ```
  Welcome to xFusionCorp Industries
  ```
- Commit the changes to the **master** branch.

### 3. 🔧 Verify File on Storage Server
- SSH into the Storage Server.
- Navigate to `/var/www/html`.
- Confirm the updated `index.html` file reflects the new content.

### 4. 🔐 Login to Jenkins
- Go to the Jenkins UI via the top bar.
- Login with:
  - **Username:** `admin`
  - **Password:** `Adm!n321`

### 5. 🔌 Install Required Plugins
- Go to **Manage Jenkins > Plugins**.
- Install:
  - **Pipeline**
  - **Git**
  - Any other required plugins for Git integration and pipeline execution.
- Restart Jenkins if prompted.

### 6. 🚀 Create Pipeline Job
- Go to **New Item**.
- Name it: `deploy-job`
- Select **Pipeline** (not Multibranch).
- Click OK.

### 7. 🧱 Configure Pipeline Script
Go to the **Pipeline** section and paste the following script:

pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                // Get code from Gitea repository
                git credentialsId: 'git-cred', url: 'http://git.stratos.xfusioncorp.com/sarah/web.git'

                // Deploy remotely via SSH
                sh '''
                    ssh natasha@ststor01 "
                        echo 'Bl@kW'
                        cd /var/www/html && git pull origin master
                    "
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing website accessibility...'
                sh '''
                    STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://stlb01:8091)
                    if [ "$STATUS" -ne 200 ]; then
                        echo "Website not accessible. Status code: $STATUS"
                        exit 1
                    fi
                '''
            }
        }
    }
}


### 8. ✅ Save and Run
- Save the job.
- Click **Build Now** to trigger the pipeline.

### 9. 🔍 Verify Deployment
- Click the **App** button on the top bar.
- Visit: [http://stlb01:8091](http://stlb01:8091)
- Confirm the page shows: `Welcome to xFusionCorp Industries`
- Ensure there’s no subdirectory like `/web`.

# *Q5 Jenkins Setup Node App
The Nautilus application development team is working on to develop a Node app. They are still in the development phase however they want to deploy and test their app on a containerized environment and using a Jenkins pipeline. Please find below more details to complete this task.

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

Similarly, click on the Gitea button on the top bar to access the Gitea UI. Login using username sarah and password Sarah_pass123.

There is a repository named sarah/web in Gitea, which is cloned on the Storage server under /home/sarah/web directory.

A Dockerfile is already present under the git repository, please push the same to the origin repo if not pushed already.

Create a jenkins pipeline job named node-app and configure it as below:

Configure it to deploy the app on App Server 1

The pipeline must have two stages Build and Deploy (names are case sensitive)

In the Build stage, build an image named stregi01.stratos.xfusioncorp.com:5000/node-app:latest using the Dockerfile present under the Git repository. stregi01.stratos.xfusioncorp.com:5000 is the image registry server. After building the image push the same to the image registry server.

In the Deploy stage, create a container named node-app using the image you build it the Build stage. Make sure to map the container port with host port 8080.

Note:

You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.

For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:
Here’s a step-by-step guide to help you complete the Jenkins pipeline setup for the Nautilus Node.js application:

---

## 🚀 Step-by-Step Deployment Guide

### 1. ✅ Push Dockerfile to Gitea Repository
Ensure the Dockerfile is committed and pushed to the `sarah/web` repository:

```bash
cd /home/sarah/web
git add Dockerfile
git commit -m "Add Dockerfile for Node app"
git push origin main
```

---

### 2. 🔧 Jenkins Setup

#### a. Login to Jenkins
- URL: Click the **Jenkins** button on the top bar
- Username: `admin`
- Password: `Adm!n321`

#### b. Install Required Plugins
Go to **Manage Jenkins → Plugins** and install:
- Docker Pipeline
- Git plugin
- Pipeline
- sshagent
- dockerpipeline
Restart Jenkins after installation.
add credentials of git and jenkins-appserver communication private key
---

### 3. 🛠️ Create Pipeline Job

#### a. Create Job
- Go to **New Item**
- Name: `node-app`
- Type: **Pipeline**
- Click OK

#### b. Configure Pipeline
In the **Pipeline** section, use the following script:

pipeline {
    agent any

    environment {
        IMAGE_NAME = "stregi01.stratos.xfusioncorp.com:5000/node-app:latest"
        APP_CONTAINER = "node-app"
        APP_SERVER = "tony@stapp01" // Replace with actual user@host
    }

    stages {
        stage('Build') {
            steps {
                git credentialsId: 'git-cred', url: 'http://git.stratos.xfusioncorp.com/sarah/web.git'
                sshagent(['appserver-ssh']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no $APP_SERVER '
                        rm -rf /tmp/web &&
                        git clone http://git.stratos.xfusioncorp.com/sarah/web.git /tmp/web &&
                        cd /tmp/web &&
                        docker build -t $IMAGE_NAME . &&
                        docker push $IMAGE_NAME
                    '
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                sshagent(['appserver-ssh']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no $APP_SERVER '
                        docker rm -f $APP_CONTAINER || true &&
                        docker run -d --name $APP_CONTAINER -p 8080:8080 $IMAGE_NAME
                    '
                    """
                }
            }
        }
    }
}
## 🧪 Next Steps

To verify the app is running:

1. **SSH into App Server 1**:
   ```bash
   ssh tony@stapp01
   ```

2. **Check running container**:
   ```bash
   docker ps | grep node-app
   ```

3. **Test the app endpoint**:
   ```bash
   curl http://localhost:8080
   ```

Or open a browser and visit:  
**`http://stapp01:8080`** (or the server’s public IP if available)


**Certificateion Test**
Q1:
Since the Jenkins server was set up recently, there are still some configurations that need to be done. The team has just realised that they need to update the default executors in the Jenkins configuration.

Change the number of default executors to 5.

Q2:
The Nautilus team wanted to set a custom welcome/system message for a new Jenkins server which will be a greeting basically to welcome new Jenkins users. They came up with a custom message as per details given below.


Add a system message Welcome to KKE Labs for the Jenkins server.
Q3:
While testing the new Jenkins server, the Nautilus team created several test jobs, some of which now need to be deleted. Below are further details about this task.

Delete the job named app-t3q3.
Q4:
To manage the increasing number of jobs on the Jenkins server, the Nautilus team recognized the need to categorize them based on their nature, environment, etc. This categorization would facilitate easier visualization and organization of the jobs. Consequently, the team intends to create a new view and relocate specific jobs accordingly.


Create a list view named jobs-t3q4 and list the job app-t3q4 under the same. Make sure this view is a global view.

Q5:
The Nautilus DevOps team want to install and setup some Jenkins plugins which are needed by some of the jobs they are going to create. Recently they have shared below requirements.


Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and Adm!n321 password.

Install the Jenkins plugin Mailer, please keep it disabled for now. You might need to restart Jenkins service to install these plugins, so we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre.

Q6:
The Nautilus DevOps team has recently setup a Jenkins server, which they want to use for some CI/CD jobs. Before that they want to install some plugins which will be used in most of the jobs. Please find below more details about the task.


Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and Adm!n321 password.

Once logged in, install Git and GitLab plugins. You might need to restart Jenkins service to install these plugins, so we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre.

Q7:
The Nautilus DevOps team was using new Jenkins server to test few jobs, so earlier they created few users. As now they are done with their testing so they want to delete one of the users they created earlier.

Delete the user robt4q3.
Q8:
The Nautilus DevOps team is configuring user permissions to ensure they can perform necessary operations within the Jenkins server, such as job creation, updating, deletion, and Jenkins configuration updates. Below are the shared requirements:


Grant below mentioned permissions to rohant4q4 user on app-t4q4 job. Also, make sure to select Inherit permissions from parent ACL under inheritance strategy for granting these permissions.

build
cancel
read
Ans:

## 🧭 Step-by-Step Guide (Using Jenkins UI)

### **Step 1: Log in to Jenkins**

1. Go to your Jenkins URL (e.g. `http://<jenkins-server>:8080`).
2. Log in using an account with **Administrator privileges** (for example, `admin / Adm!n321`).

### **Step 2: Open the Job Configuration**

1. From the Jenkins dashboard, find the job named **`app-t4q4`**.
2. Click on the job name (`app-t4q4`) to open it.
3. In the left sidebar, click **“Configure”**.
### **Step 3: Enable Project-Based Security (if not already)**

1. Scroll down to the **“Build Triggers”** or **“Build Environment”** section — just below it, look for **“Enable project-based security.”**
2. Check the box **“Enable project-based security.”**
  (This allows custom permissions for this specific job.)

### **Step 4: Configure Permissions for the User**

1. In the permissions matrix that appears:

   * Click **“Add user or group.”**
   * Enter the username:

     
     rohant4q4
     
   * Press **OK** or **Enter.**
2. For `rohant4q4`, check the following boxes:

   * **Build**
   * **Cancel**
   * **Read**

These are located under **Job**-related permissions.



### **Step 5: Configure Inheritance Strategy**

1. Still in the permissions area, look for **“Inheritance Strategy.”**
2. Select:

   
   Inherit permissions from parent ACL
   

   (This ensures the job inherits base/global permissions from Jenkins but allows job-level overrides.)



### **Step 6: Save the Configuration**

1. Scroll to the bottom of the page.
2. Click **Save** or **Apply**.

✅ **Result:**
User `rohant4q4` now has **build**, **cancel**, and **read** permissions on the job `app-t4q4`, and the job inherits higher-level permissions from its parent configuration.



