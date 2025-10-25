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

# *Q5Jenkins Scheduled Jobs**

**Level 3**
# *Q1 Jenkins Slave Nodes
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



