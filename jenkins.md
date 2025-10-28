**Level 1:**
# Q1 Set Up Jenkins Server

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

#### 4. **Configure the Build Step**
- Scroll to **Build** section.
- Click **Add build step** → choose **Execute shell**.
- Enter the following shell script:

ssh -o StrictHostKeyChecking=no natasha@ststor01.stratos.xfusioncorp.com "echo 'Bl@kW' | sudo -S yum install -y $PACKAGE"

> Replace `user@storage-server` with the actual SSH user and hostname/IP of the storage server in the Stratos Datacenter.

#### 5. **Save and Run**
- Click **Save** at the bottom.
- To test, click **Build with Parameters**, enter a package name (e.g., `curl`), and click **Build**.

**Level 2:**
**Q1: Jenkins Views**
The DevOps team of xFusionCorp Industries is planning to create a number of Jenkins jobs for different tasks. So to easily manage the jobs within Jenkins UI they decided to create different views for all Jenkins jobs based on usage/nature of these jobs, - for example datacenter-crons view for all cron jobs. Based on the requirements shared below please perform the below mentioned task:

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

1. Create a Jenkins job named datacenter-test-job.

2. Configure this job to run a simple bash command i.e echo "hello world!!".

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

  ```
  Username: admin
  Password: Adm!n321
  ```

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

```
Name: stapp01
Hostname: 172.16.238.10
Username: tony
Password: Ir0nM@n
```

**For Storage Server (Destination):**

```
Name: ststor01
Hostname: 172.16.238.15
Username: natasha
Password: Bl@kW
```

✅ Click **Test Configuration** to verify connections.
✅ Click **Save**.

---

### **4. Create the Jenkins Job**

1. Go to the Jenkins dashboard.
2. Click **“New Item”**.
3. Enter:

   ```
   Item name: copy-logs
   ```
4. Choose **Freestyle project** → Click **OK**.

---

### **5. Configure Build Triggers**

Under **Build Triggers**, check:

```
Build periodically
```

And enter this CRON expression:

```
*/6 * * * *
```

➡️ This runs every 6 minutes.

---

### **6. Add Build Step**

Under **Build → Add build step → Execute shell**

Paste the following shell script:

```bash
#!/bin/bash
# Temporary location on Jenkins
WORKDIR=/tmp/apache_logs
mkdir -p $WORKDIR

# Copy logs from App Server 1
sshpass -p 'Ir0nM@n' scp -o StrictHostKeyChecking=no tony@172.16.238.10:/var/log/httpd/access_log $WORKDIR/
sshpass -p 'Ir0nM@n' scp -o StrictHostKeyChecking=no tony@172.16.238.10:/var/log/httpd/error_log $WORKDIR/

# Copy logs to Storage Server
sshpass -p 'Bl@kW' scp -o StrictHostKeyChecking=no $WORKDIR/* natasha@172.16.238.15:/usr/src/dba/
```

> 🧩 Note: If `sshpass` is not installed, install it with:
>
> ```bash
> sudo yum install -y sshpass
> ```

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

```bash
ssh natasha@172.16.238.15
Password: Bl@kW
```

Check that logs are copied:

```bash
ls -l /usr/src/dba/
```

You should see:

```
access_log
error_log
```

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
# *Q3 Jenkins Build Images
# *Q4 Jenkins Deploy Pipeline
# *Q5 Jenkins Conditional Pipeline

**Level 4**
# *Q1 Jenkins Deployment Job
# *Q2 Jenkins Chained Builds
# *Q3 Jenkins MR Jobs
# *Q4 Jenkins Multistage Pipeline
# *Q5 Jenkins Setup Node App

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



