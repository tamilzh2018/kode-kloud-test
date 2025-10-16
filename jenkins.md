Q2:
The Nautilus DevOps team has recently setup a Jenkins server, which they want to use for some CI/CD jobs. Before that they want to install some plugins which will be used in most of the jobs. Please find below more details about the task

1. Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and Adm!n321 password.


2. Once logged in, install the Git and GitLab plugins. Note that you may need to restart Jenkins service to complete the plugins installation, If required, opt to Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre.

Note:

1. After restarting the Jenkins service, wait for the Jenkins login page to reappear before proceeding.

2. For tasks involving web UI changes, capture screenshots to share for review or consider using screen recording software like loom.com for documentation and sharing.

Q3:
The Nautilus team is integrating Jenkins into their CI/CD pipelines. After setting up a new Jenkins server, they're now configuring user access for the development team, Follow these steps:

1. Click on the Jenkins button on the top bar to access the Jenkins UI. Login with username admin and password Adm!n321.

2. Create a jenkins user named ammar with the password LQfKeWWxWD. Their full name should match Ammar.

3. Utilize the Project-based Matrix Authorization Strategy to assign overall read permission to the ammar user.

4. Remove all permissions for Anonymous users (if any) ensuring that the admin user retains overall Administer permissions.

5. For the existing job, grant ammar user only read permissions, disregarding other permissions such as Agent, SCM etc.

Note:

1. You may need to install plugins and restart Jenkins service. After plugins installation, select Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page.


2. After restarting the Jenkins service, wait for the Jenkins login page to reappear before proceeding. Avoid clicking Finish immediately after restarting the service.

Q4:
xFusionCorp Industries' DevOps team aims to streamline the management of Jenkins jobs by organizing them into distinct folders based on their purpose. Complete the task following the provided requirements:


1.Access the Jenkins UI by clicking on the Jenkins button in the top bar. Log in using the credentials: username admin and password Adm!n321.

2. Create a new folder named Apache within the Jenkins UI.

3. Move the existing jobs httpd-php and services under the newly created Apache folder.

Note:

1. Ensure to install any required plugins and restart the Jenkins service if necessary. Opt for Restart Jenkins when installation is complete and no jobs are running on the plugin installation/update page.

2. Be aware that Jenkins UI may experience temporary unresponsiveness during the service restart. Refresh the UI page if needed.

3. Capture screenshots of your work for documentation and review purposes. Alternatively, utilize screen recording software like loom.com for detailed documentation and sharing.

Q5:
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

