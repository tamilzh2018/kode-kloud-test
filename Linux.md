# Q1 Custom Apache User Setup

In response to heightened security concerns, the xFusionCorp Industries security team has opted for custom Apache users for their web applications. Each user is tailored specifically for an application, enhancing security measures. Your task is to create a custom Apache user according to the outlined specifications:

a. Create a user named mark on App server 3 within the Stratos Datacenter.

b. Assign a unique UID 1781 and designate the home directory as /var/www/mark.
Ans:
To create a custom Apache user named `mark` with the specified UID and home directory on **App Server 3** in the **Stratos Datacenter**, follow these steps:

### 🧑‍💻 Step-by-Step Instructions
1. **Create the user with custom UID and home directory**
   - Run the following command:
  
     sudo useradd -u 1781 -d /var/www/mark -m mark
  
   - Explanation:
     - `-u 1781` sets the UID.
     - `-d /var/www/mark` sets the home directory.
     - `-m` ensures the home directory is created if it doesn’t exist.

2. **Verify the user creation**
   - Check the user details:
  
     id mark
  
   - Confirm the home directory:
  
     ls -ld /var/www/mark

# Q2 Group Creation and User Assignment
The system admin team at xFusionCorp Industries has streamlined access management by implementing group-based access control. Here's what you need to do:


a. Create a group named nautilus_noc across all App servers within the Stratos Datacenter.


b. Add the user sonya into the nautilus_noc group on all App servers. If the user doesn't exist, create it as well.

Ans:
To implement group-based access control as requested, follow these steps on **each App server** within the **Stratos Datacenter**:

### 🛠️ Step-by-Step Instructions

#### a. **Create the group `nautilus_noc`**

sudo groupadd nautilus_noc

- This creates the group if it doesn't already exist.
- If the group exists, the command will return an error—but it's safe to ignore.

#### b. **Add the user `sonya` to the group**
1. **Check if the user exists**:
   
   id sonya
   
   - If the user does **not** exist, create her:
     
     sudo useradd sonya
     

2. **Add `sonya` to the `nautilus_noc` group**:
   
   sudo usermod -aG nautilus_noc sonya
   

3. **Verify group membership**:
   
   groups sonya
   
   - You should see `nautilus_noc` listed among her groups.

### 🔁 Repeat on All App Servers
Run the above steps on **App Server 1**, **App Server 2**, and **App Server 3** to ensure consistent access control across the datacenter.

# Q3 Linux User Setup with Non-Interactive Shell
Create a user named kirsty with a non-interactive shell on App Server 1.

Ans: 
#### a. **Create a user `kristy`**
sudo useradd -s /usr/sbin/nologin kirsty

# Q4 Service User Creation without Home Directory

In response to the latest tool implementation at xFusionCorp Industries, the system admins require the creation of a service user account. Here are the specifics:

Create a user named siva in App Server 1 without a home directory.
Ans:
# Create the User Without a Home Directory
sudo useradd siva -M  **-M ensures no home directory is created.**
id siva
# Confirm the Home Directory Is Not Created
ls -ld /home/siva
You should see: ls: cannot access '/home/siva': No such file or directory

# Q5 Temporary User Setup with Expiry
As part of the temporary assignment to the Nautilus project, a developer named mark requires access for a limited duration. To ensure smooth access management, a temporary user account with an expiry date is needed. Here's what you need to do:

Create a user named mark on App Server 2 in Stratos Datacenter. Set the expiry date to 2024-01-28, ensuring the user is created in lowercase as per standard protocol.
Ans:
sudo useradd mark -e 2024-01-28

sudo chage -l mark
# Q6 Linux User Data Transfer
Due to an accidental data mix-up, user data was unintentionally mingled on Nautilus App Server 2 at the /home/usersdata location by the Nautilus production support team in Stratos DC. To rectify this, specific user data needs to be filtered and relocated. Here are the details:

Locate all files (excluding directories) owned by user mariyam within the /home/usersdata directory on App Server 2. Copy these files while preserving the directory structure to the /media directory.

Ans:
# Run the following find command:
find /home/usersdata -type f -user mariyam -exec cp --parents {} /media \;
# Verify that the files have been copied with structure preserved:
find /news -type f

# Q7 Secure Root SSH Access
Following security audits, the xFusionCorp Industries security team has rolled out new protocols, including the restriction of direct root SSH login.

Your task is to disable direct SSH root login on all app servers within the Stratos Datacenter.

To disable **direct SSH root login** on all **app servers** in the **Stratos Datacenter**, follow these steps:
Ans:
### ✅ Step-by-Step Instructions

 **SSH into each app server**
   You’ll need to access each app server individually. The naming pattern might be something like:

   * `stapp01`
   * `stapp02`
   * `stapp03`
     *(Replace with actual hostnames/IPs if different)*   
   ssh user@stapp01
   **Check where the value inside config files avail**
  sudo grep -i permitrootlogin /etc/ssh/sshd_config /etc/ssh/sshd_config.d/*.conf
  **Replace those yes to no**
  sudo sed -i 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
  **Verify and restart**
  sudo sshd -T | grep permitrootlogin
  sudo systemctl restart sshd
# Q8 Data Backup for Developer
Within the Stratos DC, the Nautilus storage server hosts a directory named /data, serving as a repository for various developers non-confidential data. Developer james has requested a copy of their data stored in /data/james. The System Admin team has provided the following steps to fulfill this request:

a. Create a compressed archive named james.tar.gz of the /data/james directory.

b. Transfer the archive to the /home directory on the Storage Server.
Ans:

### ✅ **Step a: Create a compressed archive**

Create a `tar.gz` archive of the `/data/james` directory:


tar -czf /tmp/james.tar.gz /data/james


* `tar` – archive command
* `-c` – create archive
* `-z` – compress using gzip
* `-f` – filename of the archive
* `/tmp/james.tar.gz` – path to the archive file (temporary location)
* `/data/james` – source directory



### ✅ **Step b: Move the archive to `/home`**

Transfer the archive to the `/home` directory:


mv /tmp/james.tar.gz /home/


Now the file `/home/james.tar.gz` contains the compressed copy of James's data.



### ✅ Final Check:

You can verify the archive is in the correct place:


ls -l /home/james.tar.gz


You should see the file listed with its size and timestamp.

Let me know if you'd like to automate this with a script or cronjob.


# Q9 Script Execution Permissions
In a bid to automate backup processes, the xFusionCorp Industries sysadmin team has developed a new  script named xfusioncorp.sh. While the script has been distributed to all necessary servers, it lacks executable permissions on App Server 2 within the Stratos Datacenter.

Your task is to grant executable permissions to the /tmp/xfusioncorp.sh script on App Server 2. Additionally, ensure that all users have the capability to execute it.
Ans:
chmod a+rx /tmp/xfusioncorp.sh
ls -l /tmp/xfusioncorp.sh

# Q10 File Permission Correction
After conducting a security audit within the Stratos DC, the Nautilus security team discovered misconfigured permissions on critical files. To address this, corrective actions are being taken by the production support team. Specifically, the file named /etc/hostname on Nautilus App 2 server requires adjustments to its Access Control Lists (ACLs) as follows:

1. The file's user owner and group owner should be set to root.

2. Others should possess read only permissions on the file.

3. User mariyam must not have any permissions on the file.

4. User ryan should be granted read only permission on the file.
Ans:

### 1️⃣ Set ownership to `root:root`
sudo chown root:root /etc/hostname

### 2️⃣ Set base permissions so "others" have read-only access
sudo chmod 644 /etc/hostname

Explanation:

* Owner: read/write (`rw-`)
* Group: read-only (`r--`)
* Others: read-only (`r--`)
### 3️⃣ Remove all permissions for user `mariyam` using ACL
sudo setfacl -m u:mariyam:0 /etc/hostname

OR use `--remove-all` if needed:

sudo setfacl -x u:mariyam /etc/hostname
### 4️⃣ Grant **read-only** permission to user `ryan` using ACL

sudo setfacl -m u:ryan:r-- /etc/hostname

### 5️⃣ Verify All Settings

# Check ownership
ls -l /etc/hostname

# Check ACLs
getfacl /etc/hostname

## 🔍 Expected Outcome

# ls -l output
-rw-r--r-- 1 root root ... /etc/hostname

# getfacl output
# file: /etc/hostname
# owner: root
# group: root
user::rw-
user:mariyam:
user:ryan:r--
group::r--
other::r--

# Q11 String Replacement
Within the Stratos DC, the backup server holds template XML files crucial for the Nautilus application. Before utilization, these files require valid data insertion. As part of routine maintenance, system admins at xFusionCorp Industries employ string and file manipulation commands.

Your task is to substitute all occurrences of the string Random with Marine within the XML file located at /root/nautilus.xml on the backup server.
Ans:
Run the following command on the backup server:
sudo sed -i 's/Random/Marine/g' /root/nautilus.xml
You can check that the replacements were successful using:
sudo grep 'Marine' /root/nautilus.xml
sudo grep 'Random' /root/nautilus.xml
# Q12 Secure Data Transfer
A Nautilus developer has stored confidential data on the jump host within Stratos DC. To ensure security and compliance, this data must be transferred to one of the app servers. Given developers lack direct access to these servers, the system admin team has been enlisted for assistance.

Copy /tmp/nautilus.txt.gpg file from jump server to App Server 1 placing it in the directory /home/opt.
Ans:
sudo scp /tmp/nautilus.txt.gpg tony@stapp01:/home/opt/
# Q13 Restrict Cron Access
In alignment with security compliance standards, the Nautilus project team has opted to impose restrictions on crontab access. Specifically, only designated users will be permitted to create or update cron jobs.

Configure crontab access on App Server 1 as follows: Allow crontab access to ammar user while denying access to the garrett user.
Ans:
To configure **crontab access** on **App Server 1** so that:

* ✅ User `ammar` **can** use `crontab`
* ❌ User `garrett` **cannot** use `crontab`

you'll need to manage two special files:

* `/etc/cron.allow` – users **listed here are allowed**
* `/etc/cron.deny` – users **listed here are denied**

> 💡 If `cron.allow` exists, **only users in that file are allowed** to use `crontab`. `cron.deny` will be ignored in that case.

### ✅ Step-by-step Instructions

1. **SSH into App Server 1:**

ssh <your-user>@<app-server-1>

2. **Create or update `/etc/cron.allow` to include `ammar`:**

echo "ammar" | sudo tee /etc/cron.allow

This restricts crontab access **only to users listed**, i.e., `ammar`.

> ⚠️ If this file exists already, make sure you **append** the user rather than overwrite (unless overwrite is desired):

echo "ammar" | sudo tee -a /etc/cron.allow

3. **Ensure `garrett` is *not* in `/etc/cron.allow`:**

If `cron.allow` exists, any user not listed there is automatically denied — so no need to explicitly deny `garrett`.

You can confirm:

sudo grep garrett /etc/cron.allow

If it returns nothing, you’re good.

4. **(Optional) Remove or ignore `/etc/cron.deny`:**

Since `/etc/cron.allow` exists, the `cron.deny` file is ignored, but to keep things clean:

sudo rm -f /etc/cron.deny

Or ensure `garrett` is listed there **only if** you’re not using `cron.allow`.

### ✅ Verification

* **Test for `ammar`:**
sudo -u ammar crontab -l

If allowed, this should show the current crontab (or an empty one).

* **Test for `garrett`:**
sudo -u garrett crontab -l

Expected output:

You (garrett) are not allowed to use this program (crontab)

# Q14 Default GUI Boot Configuration
With the installation of new tools on the app servers within the Stratos Datacenter, certain functionalities now necessitate graphical user interface (GUI) access.

Adjust the default runlevel on all App servers in Stratos Datacenter to enable GUI booting by default. It's imperative not to initiate a server reboot after completing this task.
Ans:
To adjust the default runlevel to enable GUI booting (i.e., set the system to boot into **graphical.target** by default) **without rebooting** on all App servers in the **Stratos Datacenter**, follow these steps:

### ✅ **Step-by-step Instructions**

1. **SSH into each App server** in the Stratos Datacenter.

   (Assuming you have SSH access like this:
   `ssh user@app-server-x.stratos.local`)

2. **Check the current default target**:
  
   systemctl get-default
  
   If it returns `multi-user.target`, it means the system is booting into CLI (non-GUI) mode.

3. **Set the default target to graphical**:
  
   sudo systemctl set-default graphical.target

   This sets GUI mode as the default boot target **without restarting the system**.

4. **Confirm the change**:
  
   systemctl get-default

   It should now show:
 
   graphical.target

### ⚠️ Do **Not** Reboot

* This change modifies the default target for future boots only.
* It will not start the GUI on the current session or reboot the system.
* You are explicitly instructed **not to reboot** any servers after making this change.

### 🧠 Optional: Verify target file (for learning purposes)

You can also verify the symlink created:

ls -l /etc/systemd/system/default.target

Should point to:

/usr/lib/systemd/system/graphical.target

# Q15 Timezone Alignment
In the daily standup, it was noted that the timezone settings across the Nautilus Application Servers in the Stratos Datacenter are inconsistent with the local datacenter's timezone, currently set to Pacific/Enderbury.

Synchronize the timezone settings to match the local datacenter's timezone (Pacific/Enderbury).
Ans:
Set Timezone:
sudo timedatectl set-timezone Pacific/Enderbury
Verify: timedatectl
# Q16 Firewall Configuration
The Nautilus system admins team has rolled out a web UI application for their backup utility on the Nautilus backup server within the Stratos Datacenter. This application operates on port 8084, and firewalld is active on the server. To meet operational needs, the following requirements have been identified:

Allow all incoming connections on port 8084/tcp. Ensure the zone is set to public.
Ans:
ssh backupserver
## ✅ Step-by-Step Instructions
| Task                | Command                                                           |
| - | -- |
| Confirm active zone | `sudo firewall-cmd --get-active-zones`                            |
| Allow port 8084/tcp | `sudo firewall-cmd --zone=public --add-port=8084/tcp --permanent` |
| Reload firewall     | `sudo firewall-cmd --reload`                                      |
| Verify              | `sudo firewall-cmd --zone=public --list-ports`                    |

# Q17 Process Limit Adjustment
In the Stratos Datacenter, our Storage server is encountering performance degradation due to excessive processes held by the nfsuser user. To mitigate this issue, we need to enforce limitations on its maximum processes. Please set the maximum process limits as specified below:

a. Set the soft limit to 1027

b. Set the hard limit to 2027
Ans:
# Open the limits configuration file and Add the following lines at the end of the file::
sudo vi /etc/security/limits.conf
nfsuser    soft    nproc    1025
nfsuser    hard    nproc    2025

# Q18 SElinux Installation and Configuration
Following a security audit, the xFusionCorp Industries security team has opted to enhance application and server security with SELinux. To initiate testing, the following requirements have been established for App server 2 in the Stratos Datacenter:

Install the required SELinux packages.

Permanently disable SELinux for the time being; it will be re-enabled after necessary configuration changes.

No need to reboot the server, as a scheduled maintenance reboot is already planned for tonight.

Disregard the current status of SELinux via the command line; the final status after the reboot should be disabled.

Ans:
sudo yum install selinux-policy selinux-policy-targeted -y
sudo vi /etc/selinux/config

Change it to: SELINUX=enforcing
SELINUX=disabled
Verify Configuration: 
grep SELINUX= /etc/selinux/config

or sudo sed -i 's/^SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
**Level 2**
# Q1 Create a Cron Job
The Nautilus system admins team has prepared scripts to automate several day-to-day tasks. They want them to be deployed on all app servers in Stratos DC on a set schedule. Before that they need to test similar functionality with a sample cron job. Therefore, perform the steps below:

a. Install cronie package on all Nautilus app servers and start crond service.

b. Add a cron */5 * * * * echo hello > /tmp/cron_text for root user.
Ans:
ssh into stapp01 stapp02 stapp03

change to root user: sudo su -
Verify crond is running: systemctl status crond
  if not avail 
  yum install -y cronie
  systemctl enable crond
  systemctl start crond
Add the Cron Job for Root User: crontab -e

Add the following line at the bottom: */5 * * * * echo hello > /tmp/cron_text

After 5 minutes, check if the file was created and contains the text: cat /tmp/cron_text
You should see: hello
# Q2 Linux Banner
During the monthly compliance meeting, it was pointed out that several servers in the Stratos DC do not have a valid banner. The security team has provided serveral approved templates which should be applied to the servers to maintain compliance. These will be displayed to the user upon a successful login.

Update the message of the day on all application and db servers for Nautilus. Make use of the approved template located at /home/thor/nautilus_banner on jump host
Ans:
ssh-keygen -t rsa -b 2048en -t rsa -b 2048
ssh-copy-id tony@stapp01
ssh-copy-id steve@stapp01
ssh-copy-id banner@stapp03
ssh-copy-id peter@stdb01

| Server  | User   | Hostname     |
| - |  |  |
| stapp01 | tony   | App Server 1 |
| stapp02 | steve  | App Server 2 |
| stapp03 | banner | App Server 3 |
| stdb01  | peter  | DB Server 1  |

Now, let's complete the task of **updating the Message of the Day (MOTD)** using the banner located at `/home/thor/nautilus_banner`.

### ✅ Final Steps – Apply MOTD on All Servers
Run the following **one-liner SSH commands** from the **jump host** (`thor@jumphost`) for each server:

#### 🚀 1. **stapp01 (App Server 1)**
scp /home/thor/nautilus_banner tony@stapp01:/tmp/
ssh tony@stapp01 "sudo mv /tmp/nautilus_banner /etc/motd && sudo chmod 644 /etc/motd"

#### 🚀 2. **stapp02 (App Server 2)**
scp /home/thor/nautilus_banner steve@stapp02:/tmp/
ssh -t steve@stapp02 "sudo mv /tmp/nautilus_banner /etc/motd && sudo chmod 644 /etc/motd"
#### 🚀 3. **stapp03 (App Server 3)**
scp /home/thor/nautilus_banner banner@stapp03:/tmp/
ssh -t banner@stapp03 "sudo mv /tmp/nautilus_banner /etc/motd && sudo chmod 644 /etc/motd"

#### 🚀 4. **stdb01 (DB Server 1)**

scp /home/thor/nautilus_banner peter@stdb01:/tmp/
ssh -t peter@stdb01 "sudo mv /tmp/nautilus_banner /etc/motd && sudo chmod 644 /etc/motd"

### 🧪 Verify Banner Display

After updating each server, log into them to confirm the banner appears:

ssh tony@stapp01     # or other users/servers

You should see the ASCII art and the warning message displayed immediately after login.

# Q3 Linux Collaborative Directories
The Nautilus team doesn't want its data to be accessed by any of the other groups/teams due to security reasons and want their data to be strictly accessed by the dbadmin group of the team.

Setup a collaborative directory /dbadmin/data on app server 3 in Stratos Datacenter.

The directory should be group owned by the group dbadmin and the group should own the files inside the directory. The directory should be read/write/execute to the user and group owners, and others should not have any access.

Ans:
To set up the collaborative directory `/dbadmin/data` on **App Server 3** in the **Stratos Datacenter** with the specified security and group ownership requirements, follow these steps:

## ✅ **Objective**

Create `/dbadmin/data` on **App Server 3** with:

* Group ownership: `dbadmin`
* Permissions: `rwx` for user and group, no access for others (`770`)
* All files created inside should be owned by the group `dbadmin`

#### 1. **Login to App Server 3**
ssh banner@stapp03
Use the appropriate credentials if you're accessing it in a lab environment.
#### 2. **Create the directory structure**
sudo mkdir -p /dbadmin/data
#### 3. **Create the group (if it doesn't exist)**
getent group dbadmin || sudo groupadd dbadmin
#### 4. **Change group ownership to `dbadmin`**
sudo chown :dbadmin /dbadmin/data

#### 5. **Set directory permissions**
sudo chmod 770 /dbadmin/data
> This gives:
>
> * User: Read, write, execute
> * Group: Read, write, execute
> * Others: No access

#### 6. **Set the setgid bit**

This ensures new files/directories inherit the group `dbadmin`:

sudo chmod g+s /dbadmin/data

You can verify it with `ls -ld /dbadmin/data`, which should show something like:

drwxrws 2 root dbadmin 4096 Oct  5 10:00 /dbadmin/data

Note the `s` in the group permissions (`rws`).

# Q4 Linux String Substitute (sed)
There is some data on Nautilus App Server 2 in Stratos DC. Data needs to be altered in several of the files. On Nautilus App Server 2, alter the /home/BSD.txt file as per details given below:

a. Delete all lines containing word copyright and save results in /home/BSD_DELETE.txt file. (Please be aware of case sensitivity)

b. Replace all occurrence of word from to is and save results in /home/BSD_REPLACE.txt file.

Note: Let's say you are asked to replace word to with from. In that case, make sure not to alter any words containing the string itself; for example upto, contributor etc.
Ans:
# Task a
grep -v 'copyright' /home/BSD.txt > /home/BSD_DELETE.txt

# Task b
sed 's/\bfrom\b/is/g' /home/BSD.txt > /home/BSD_REPLACE.txt

# Q5 Linux SSH Authentication
The system admins team of xFusionCorp Industries has set up some scripts on jump host that run on regular intervals and perform operations on all app servers in Stratos Datacenter. To make these scripts work properly we need to make sure the thor user on jump host has password-less SSH access to all app servers through their respective sudo users (i.e tony for app server 1). Based on the requirements, perform the following:

Set up a password-less authentication from user thor on jump host to all app servers through their respective sudo users.
Ans:
To set up password-less SSH authentication from the `thor` user on the **jump host** to all **app servers** via their respective **sudo users** (e.g., `tony` for app server 1), follow these steps:



### 🛠️ Step-by-Step Setup

#### 1. **Generate SSH Key on Jump Host (as `thor`)**

ssh-keygen -t rsa -b 2048

- Press Enter to accept default file location (`~/.ssh/id_rsa`)
- Leave passphrase empty for password-less access

#### 2. **Copy Public Key to App Servers via Sudo Users**

Assuming:
- App Server 1: `tony@<app_server_1_ip>`
- App Server 2: `steve@<app_server_2_ip>`
- App Server 3: `banner@<app_server_3_ip>`

Run the following **from the jump host as `thor`**:


ssh-copy-id tony@<app_server_1_ip>
ssh-copy-id steve@<app_server_2_ip>
ssh-copy-id banner@<app_server_3_ip>


> This command appends `thor`'s public key to the `~/.ssh/authorized_keys` file of each sudo user on the respective app server.

#### 3. **Verify Password-less SSH Access**

Test the connection from jump host:

ssh tony@<app_server_1_ip>
ssh steve@<app_server_2_ip>
ssh banner@<app_server_3_ip>

# Q6 Linux Find Command
During a routine security audit, the team identified an issue on the Nautilus App Server. Some malicious content was identified within the website code. After digging into the issue they found that there might be more infected files. Before doing a cleanup they would like to find all similar files and copy them to a safe location for further investigation. Accomplish the task as per the following requirements:

a. On App Server 1 at location /var/www/html/news find out all files (not directories) having .css extension.
b. Copy all those files along with their parent directory structure to location /news on same server.
c. Please make sure not to copy the entire /var/www/html/news directory content.
Ans:
### 🧩 a. Find all `.css` files (excluding directories)

Run the following command:

find /var/www/html/news -type f -name "*.css"

- `-type f`: ensures only files are selected
- `-name "*.css"`: filters for `.css` extension

### 📦 b. Copy those files **with parent directory structure** to `/news`

Use `find` with `cp --parents`:

mkdir -p /news
find /var/www/html/news -type f -name "*.css" -exec cp --parents {} /news \;

- `--parents`: preserves the full directory structure relative to root
- `{} /news`: copies each matched file into `/news` with its path

### ✅ c. Ensure only `.css` files are copied, not the entire directory

This method **only copies matched `.css` files** and their paths — not other content from `/var/www/html/news`.
find /news -type f -name "*.css"

# Q7 Install a package
As per new application requirements shared by the Nautilus project development team, serveral new packages need to be installed on all app servers in Stratos Datacenter. Most of them are completed except for telnet.

Therefore, install the telnet package on all app-servers.
Ans:
Install telnet: sudo yum install -y telnet
Verify installation: telnet
# Q8 Install Ansible
During the weekly meeting, the Nautilus DevOps team discussed about the automation and configuration management solutions that they want to implement. While considering several options, the team has decided to go with Ansible for now due to its simple setup and minimal pre-requisites. The team wanted to start testing using Ansible, so they have decided to use jump host as an Ansible controller to test different kind of tasks on rest of the servers.

Install ansible version 4.10.0 on Jump host using pip3 only. Make sure Ansible binary is available globally on this system, i.e all users on this system are able to run Ansible commands.

Ans:
Ensure Python 3 and pip3 are installed: python3 --version and pip3 --version

Install Ansible version 4.10.0 via pip3 to a system-wide location: sudo pip3 install ansible==4.10.0

ansible --version  : ansible [core 2.11.x]   config file = ... Note: Ansible 4.x uses ansible-core 2.11.x internally. That is expected.
# Q9 Configure Local Yum repos
The Nautilus production support team and security team had a meeting last month in which they decided to use local yum repositories for maintaing packages needed for their servers. For now they have decided to configure a local yum repo on Nautilus Backup Server. This is one of the pending items from last month, so please configure a local yum repository on Nautilus Backup Server as per details given below.

a. We have some packages already present at location /packages/downloaded_rpms/ on Nautilus Backup Server.
b. Create a yum repo named epel_local and make sure to set Repository ID to epel_local. Configure it to use package's location /packages/downloaded_rpms/.
c. Install package samba from this newly created repo.
Ans:
To set up a local `yum` repository on the Nautilus Backup Server, follow the steps below:

### Step 1: Create the Local Yum Repository

1. **Create the Repository Directory**:
   Ensure the `/packages/downloaded_rpms/` directory exists and contains the RPM packages.

   If it's not already created:

   
   sudo mkdir -p /packages/downloaded_rpms
   

2. **Install the `createrepo` Tool** (if not already installed):
   The `createrepo` tool will be used to create the repository metadata. You can install it using `yum` (or `dnf` depending on your distro):

      sudo yum install createrepo -y
    if error throws like Error: There are no enabled repositories in "/etc/yum.repos.d", "/etc/yum/repos.d", "/etc/distro.repos.d".
    # Ensure that the epel_local.repo file is correctly created and placed in the /etc/yum.repos.d/ directory.
    sudo vi /etc/yum.repos.d/epel_local.repo
It looks like the `/etc/yum.repos.d/` directory is empty, which is likely the cause of the issue. `yum` requires repository configuration files in this directory to function properly.

### Let's fix this by creating the `epel_local.repo` file manually in the `/etc/yum.repos.d/` directory.

### Step 2: Create the Repository Configuration File

1. **Create the `epel_local.repo` file**:

   Run the following command to create the `.repo` file:

   
   sudo vi /etc/yum.repos.d/epel_local.repo
   

2. **Add the repository configuration**:

   In the editor, add the following content to the file:

   ini
   [epel_local]
   name=EPEL Local Repository
   baseurl=file:///packages/downloaded_rpms/
   enabled=1
   gpgcheck=0
   repo_gpgcheck=0
   

   Explanation of the fields:

   * **name**: The name of the repository (you can change it if you wish).
   * **baseurl**: The path to the local RPM package directory. Since this is a local directory, the URL starts with `file:///`.
   * **enabled**: Set to `1` to enable the repository.
   * **gpgcheck**: Set to `0` as we are not using GPG keys for the local repository.
   * **repo_gpgcheck**: Set to `0` for the same reason.

3. **Save and exit** the editor (`:wq` in `vi`).

### Step 3: Verify the File Permissions

Ensure that the `.repo` file has the correct permissions for `yum` to read it:

sudo chmod 644 /etc/yum.repos.d/epel_local.repo

### Step 4: Create the Repository Metadata

If you haven't already done so, you will need to create repository metadata for the RPM packages located in `/packages/downloaded_rpms/`. This is done using the `createrepo` tool.

1. **Install `createrepo` if it's not already installed**:
   
   sudo yum install createrepo -y

2. **Run `createrepo` to generate the metadata**:
  
   sudo createrepo /packages/downloaded_rpms/
   
### Step 5: Clean the Yum Cache

To ensure `yum` picks up the new repository, clear the cache:

sudo yum clean all

### Step 6: Test the Repository

Check if `yum` can now find the new repository:

sudo yum repolist

You should see the `epel_local` repository listed.

### Step 7: Install the `samba` Package

Now that the local repository is configured correctly, you should be able to install the `samba` package:

sudo yum install samba --disablerepo="*" --enablerepo="epel_local"

### Step 5: Verify the Installation

Once the package is installed, verify that `samba` was successfully installed:

samba --version

# Q10 Linux Services
As per details shared by the development team, the new application release has some dependencies on the back end. There are some packages/services that need to be installed on all app servers under Stratos Datacenter. As per requirements please perform the following steps:

a. Install squid package on all the application servers.

b. Once installed, make sure it is enabled to start during boot.
Ans:
### **For CentOS/Red Hat-based Servers:**

1. **Login to the Server(s):**
   SSH into each application server.

2. **Install Squid:**
   Run the following command to install the squid package:
 
   sudo yum install squid -y 

3. **Enable Squid to Start on Boot:**
   After the installation, ensure that Squid is enabled to start on boot with the following command:
   
   sudo systemctl enable squid
   
4. **Start the Squid Service:**
   Once Squid is installed, you can start the service using:
   
   sudo systemctl start squid

5. **Verify Squid is Running:**
   To verify that Squid is running, use:
   
   sudo systemctl status squid

# Q11 Linux Configure sudo
We have some users on all app servers in Stratos Datacenter. Some of them have been assigned some new roles and responsibilities, therefore their users need to be upgraded with sudo access so that they can perform admin level tasks.

a. Provide sudo access to user javed on all app servers.

b. Make sure you have set up password-less sudo for the user.
Ans:
To grant **sudo access** and enable **password-less sudo** for user `javed` on all app servers in the Stratos Datacenter, follow these steps on each server:

### 🛠️ Step A: Provide Sudo Access to `javed`

1. **Log in to each app server** as root or a user with sudo privileges.
2. **Add `javed` to the `sudo` group**:
   
   usermod -aG sudo javed or usermod -aG wheel javed
   
   > This assumes your system uses the `sudo` group for sudo privileges. On some systems (like CentOS/RHEL), it might be `wheel`.

### 🔐 Step B: Enable Password-less Sudo for `javed`

1. **Create a custom sudoers file** for `javed`:
   
   echo 'javed ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/javed
   
2. **Set correct permissions**:
   
   sudo chmod 440 /etc/sudoers.d/javed
   
### ✅ Verification

After completing the steps on each server, verify with:

sudo -l -U javed or sudo -l

You should see:

User javed may run the following commands on this host:
    (ALL) NOPASSWD: ALL

# Q12 DNS Troubleshooting
The system admins team of xFusionCorp Industries has noticed intermittent issues with DNS resolution in several apps . App Server 3 in Stratos Datacenter is having some DNS resolution issues, so we want to add some additional DNS nameservers on this server.

As a temporary fix we have decided to go with Google public DNS (ipv4). Please make appropriate changes on this server.
Ans:
To resolve DNS issues on App Server 3 in the Stratos Datacenter by adding Google Public DNS (IPv4), you can update the server's DNS configuration. Here's how to do it on a Linux system:

### 🛠 Steps to Add Google Public DNS

1. **Edit the resolv.conf file**:
   Open the DNS configuration file using a text editor like `vi` or `nano`:
      sudo vi /etc/resolv.conf
   
2. **Add Google DNS entries**:
   Add the following lines at the top of the file:
   
   nameserver 8.8.8.8
   nameserver 8.8.4.4

3. **Save and exit**:
   - In `vi`, press `Esc`, type `:wq`, and hit `Enter`.
   - In `nano`, press `Ctrl+O` to write out, then `Ctrl+X` to exit.

4. **Prevent overwriting (optional but recommended)**:
   If your system uses a network manager or DHCP client that overwrites `/etc/resolv.conf`, you can make the changes persistent by:
   - Editing the appropriate network configuration file (e.g., `/etc/network/interfaces`, `/etc/netplan/*.yaml`, or NetworkManager settings).
   - Or by creating a custom `resolv.conf` and symlinking it:
     
     sudo chattr +i /etc/resolv.conf
     
     If Error comes like :chattr: command not found
     sudo yum install e2fsprogs


   > ⚠️ Use `chattr +i` with caution—it makes the file immutable.
# Q13 Linux Firewalld Setup
To secure our Nautilus infrastructure in Stratos Datacenter we have decided to install and configure firewalld on all app servers. We have Apache and Nginx services running on these apps. Nginx is running as a reverse proxy server for Apache. We might have more robust firewall settings in the future, but for now we have decided to go with the given requirements listed below:

a. Allow all incoming connections on Nginx port, i.e 80.

b. Block all incoming connections on Apache port, i.e 8080.

c. All rules must be permanent.

d. Zone should be public.

e. If Apache or Nginx services aren't running already, please make sure to start them.
Ans:
## ✅ **Requirements Recap:**

1. **Allow** port **80 (Nginx)** — public zone, permanent.
2. **Block** port **8080 (Apache)** — public zone, permanent.
3. Ensure **Nginx and Apache are running**.
4. Use **firewalld**, with rules set to **permanent** and in the **public** zone.
## 🔧 Step-by-Step Instructions:

### 1. **Install firewalld (if not installed)**
sudo yum install firewalld -y  # For RHEL/CentOS
# OR
sudo apt install firewalld -y  # For Debian/Ubuntu
### 2. **Enable and start firewalld**
sudo systemctl enable firewalld
sudo systemctl start firewalld
### 3. **Set default zone to public (optional but recommended)**
sudo firewall-cmd --set-default-zone=public
### 4. **Allow Nginx (port 80) permanently**
sudo firewall-cmd --zone=public --add-port=80/tcp --permanent

### 5. **Remove/block Apache port (8080)** if previously allowed
sudo firewall-cmd --zone=public --remove-port=8080/tcp --permanent
> 💡 If it wasn't previously added, this command still ensures it's not allowed.
### 6. **Reload firewalld to apply changes**
sudo firewall-cmd --reload
### 7. **Start Apache and Nginx services**
sudo systemctl enable nginx
sudo systemctl start nginx

sudo systemctl enable httpd   # Apache is typically 'httpd' on RHEL-based systems
sudo systemctl start httpd

> 🔎 On Ubuntu/Debian, the Apache service is usually named `apache2`, so replace `httpd` with `apache2` if needed.

### 8. **Verify firewall rules**

sudo firewall-cmd --zone=public --list-ports

✅ You should see:

80/tcp

🔴 You should **not** see:

8080/tcp

# Q14 Linux Postfix Mail Server
xFusionCorp Industries has planned to set up a common email server in Stork DC. After several meetings and recommendations they have decided to use postfix as their mail transfer agent and dovecot as an IMAP/POP3 server. We would like you to perform the following steps:

1. Install and configure postfix on Stork DC mail server.

2. Create an email account siva@stratos.xfusioncorp.com identified by YchZHRcLkL.

3. Set its mail directory to /home/siva/Maildir.

4. Install and configure dovecot on the same server
Ans:
# 🛠️ Email Server Setup on CentOS using Postfix and Dovecot
### ✅ **1. Install and Configure Postfix**

#### 1.1 Install Postfix
sudo yum install postfix -y
#### 1.2 Enable and Start Postfix
sudo systemctl enable postfix
sudo systemctl start postfix

#### 1.3 Configure Postfix
Edit the Postfix config file:

sudo vi /etc/postfix/main.cf

**Make sure the following lines are added or edited:**

myhostname = mail.stratos.xfusioncorp.com
mydomain = stratos.xfusioncorp.com
myorigin = $mydomain
inet_interfaces = all
inet_protocols = all
mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain
home_mailbox = Maildir/

**Then restart Postfix:**
sudo systemctl restart postfix

### ✅ **2. Create the Email Account `siva@stratos.xfusioncorp.com`**

#### 2.1 Create a System User

sudo useradd siva
echo 'YchZHRcLkL' | sudo passwd --stdin siva

#### 2.2 Set Up Maildir for the User

sudo dnf install dovecot -y  # Dovecot provides maildirmake tool
sudo maildirmake /home/siva/Maildir
sudo chown -R siva:siva /home/siva/Maildir

### ✅ **3. Install and Configure Dovecot**

#### 3.1 Install Dovecot

sudo yum install dovecot -y

#### 3.2 Enable and Start Dovecot

sudo systemctl enable dovecot
sudo systemctl start dovecot

### ✅ **4. Configure Dovecot**

#### 4.1 Set Mail Location

Edit `/etc/dovecot/conf.d/10-mail.conf`:

mail_location = maildir:~/Maildir

#### 4.2 Enable Login Mechanisms

Edit `/etc/dovecot/conf.d/10-auth.conf`:

disable_plaintext_auth = no
auth_mechanisms = plain login
!include auth-system.conf.ext

#### 4.3 Enable IMAP and POP3 Protocols

Edit `/etc/dovecot/dovecot.conf`:

protocols = imap pop3

#### 4.4 Restart Dovecot

sudo systemctl restart dovecot

### ✅ **5. Firewall Configuration (if enabled)**

Allow required mail ports:

sudo firewall-cmd --permanent --add-service=smtp
sudo firewall-cmd --permanent --add-service=imap
sudo firewall-cmd --permanent --add-service=pop3
sudo firewall-cmd --reload

### ✅ **6. Verify Services**

* Check Postfix status:
 
  systemctl status postfix
  
* Check Dovecot status:
 
  systemctl status dovecot
  
* Confirm listening ports:
 
  sudo netstat -tulnp | grep -E '110|143|25' or sudo ss -tulnp | grep -E '110|143|25'
# Q15 Linux Postfix Troubleshooting
Some users of the monitoring app have reported issues with xFusionCorp Industries mail server. They have a mail server in Stork DC where they are using postfix mail transfer agent. Postfix service seems to fail. Try to identify the root cause and fix it.
Ans:
Error: Msg:
ct 11 08:13:48 stmail01.stratos.xfusioncorp.com postfix[778]: warning: /etc/postfix/main.cf, line 135: overriding earlier entry: inet_interfaces=all
Oct 11 08:13:48 stmail01.stratos.xfusioncorp.com postfix[778]: fatal: parameter inet_interfaces: no local interface found for ::1
Oct 11 08:13:49 stmail01.stratos.xfusioncorp.com systemd[1]: postfix.service: Child 778 belongs to postfix.service.
Oct 11 08:13:49 stmail01.stratos.xfusioncorp.com systemd[1]: postfix.service: Control process exited, code=exited, status=1/FAILURE
░░ Subject: Unit process exited
░░ Defined-By: systemd
░░ Support: https://access.redhat.com/support
░░ 
░░ An ExecStart= process belonging to unit postfix.service has exited.
░░ 
░░ The process' exit code is 'exited' and its exit status is 1.
Oct 11 08:13:49 stmail01.stratos.xfusioncorp.com systemd[1]: postfix.service: Got final SIGCHLD for state start.
Oct 11 08:13:49 stmail01.stratos.xfusioncorp.com systemd[1]: postfix.service: Failed with result 'exit-code'.
░░ Subject: Unit failed
░░ Defined-By: systemd
░░ Support: https://access.redhat.com/support
░░ 
░░ The unit postfix.service has entered the 'failed' state with result 'exit-code'.
Oct 11 08:13:49 stmail01.stratos.xfusioncorp.com systemd[1]: postfix.service: Service will not restart (restart setting)
Oct 11 08:13:49 stmail01.stratos.xfusioncorp.com systemd[1]: postfix.service: Changed start -> failed
Oct 11 08:13:49 stmail01.stratos.xfusioncorp.com systemd[1]: postfix.service: Job 36 postfix.service/start finished, result=failed
Oct 11 08:13:49 stmail01.stratos.xfusioncorp.com systemd[1]: Failed to start Postfix Mail Transport Agent.
░░ Subject: A start job for unit postfix.service has failed
░░ Defined-By: systemd
░░ Support: https://access.redhat.com/support
░░ 
░░ A start job for unit postfix.service has finished with a failure.
░░ 
░░ The job identifier is 36 and the job result is failed.
Solution:
**Edit configuration file**
sudo vi /etc/postfix/main.cf
inet_interfaces=all to inet_interfaces=localhost
inet_protocols=all to inet_protocol=ipv4
 **save the document**
sudo systemctl start postfix
# Q16 Install and Configure HaProxy LBR
There is a static website running in Stratos Datacenter. They have already configured the app servers and code is already deployed there. To make it work properly, they need to configure LBR server. There are number of options for that, but team has decided to go with HAproxy. FYI, apache is running on port 8084 on all app servers. Complete this task as per below details.

a. Install and configure HAproxy on LBR server using yum only and make sure all app servers are added to HAproxy load balancer. HAproxy must serve on default http port (Note: Please do not remove stats socket /var/lib/haproxy/stats entry from haproxy default config.).

b. Once done, you can access the website using StaticApp button on the top bar.
Ans:
To complete the HAProxy setup on the LBR server as described, follow these steps:

### 🛠️ Step A: Install and Configure HAProxy
#### 1. **Install HAProxy using `yum`**

sudo yum install haproxy -y

#### 2. **Edit HAProxy Configuration**
Open the HAProxy configuration file:

sudo vi /etc/haproxy/haproxy.cfg

Make sure the default `stats socket` line is **not removed**:

stats socket /var/lib/haproxy/stats

Then, update the configuration to include your app servers. Here's an example assuming three app servers (`app1`, `app2`, `app3`) running Apache on port `8084`:
1. Update the frontend to listen on port 80
Change:frontend main
    bind *:5000
 To:
frontend http_front
    bind *:80
    default_backend http_back
2. Update backend app server ports to 8084
Change:
backend app
    balance     roundrobin
    server  app1 127.0.0.1:5001 check
    server  app2 127.0.0.1:5002 check
    server  app3 127.0.0.1:5003 check
    server  app4 127.0.0.1:5004 check
To:

backend http_back
    balance roundrobin
    server stapp01 172.16.238.10:8084 check
    server stapp02 172.16.238.11:8084 check
    server stapp03 172.16.238.12:8084 check


Replace the IPs (`172.16.238.10`, etc.) with the actual IP addresses of your app servers.

#### 3. **Enable and Start HAProxy**

sudo systemctl enable haproxy
sudo systemctl start haproxy

### ✅ Step B: Verify Access

Once HAProxy is running and properly configured, click the **StaticApp** button on the top bar to verify that the static website is accessible through the load balancer.

# Q17 Haproxy LBR Troubleshooting
xFusionCorp Industries has an application running on Nautlitus infrastructure in Stratos Datacenter. The monitoring tool recognised that there is an issue with the haproxy service on LBR server. That needs to fixed to make the application work properly.

Troubleshoot and fix the issue, and make sure haproxy service is running on Nautilus LBR server. Once fixed, make sure you are able to access the website using StaticApp button on the top bar.
Ans:

To troubleshoot and fix the HAProxy service issue on the Nautilus LBR server, follow these steps:

### 🛠️ Step-by-Step Troubleshooting Guide

#### 1. **Access the LBR Server**
Log into the Nautilus LBR server using SSH:

ssh tony@lbr.stratos.xfusioncorp.com

Use the appropriate credentials provided by your infrastructure team.

#### 2. **Check HAProxy Service Status**
Run:

sudo systemctl status haproxy

This will show whether the service is active, inactive, or failed.

#### 3. **Inspect Logs for Errors**
Check HAProxy logs for clues:

sudo journalctl -u haproxy

Or:

sudo tail -n 50 /var/log/haproxy.log

Look for configuration errors or port binding issues.

#### 4. **Validate HAProxy Configuration**
Run a syntax check:

sudo haproxy -c -f /etc/haproxy/haproxy.cfg

If there are errors, edit the config file:

sudo vi /etc/haproxy/haproxy.cfg

Ensure the frontend and backend sections are correctly defined and pointing to the right application servers.

#### 5. **Restart HAProxy**
Once the configuration is fixed:

sudo systemctl restart haproxy

Then verify it's running:

sudo systemctl status haproxy

# Q18 MariaDB Troubleshooting
There is a critical issue going on with the Nautilus application in Stratos DC. The production support team identified that the application is unable to connect to the database. After digging into the issue, the team found that mariadb service is down on the database server.

Look into the issue and fix the same.
Ans:
sudo systemctl status mariadb
chown -R mysql:mysql /var/lib/mysql
sudo systemctl start mariadb
sudo cat /var/log/mariadb/mariadb.log | tail -30
sudo mkdir -p /run/mariadb
sudo chown mysql:mysql /run/mariadb
# Q19 Linux  Scripts

The production support team of xFusionCorp Industries is working on developing some bash scripts to automate different day to day tasks. One is to create a bash script for taking websites backup. They have a static website running on App Server 2 in Stratos Datacenter, and they need to create a bash script named beta_backup.sh which should accomplish the following tasks. (Also remember to place the script under /scripts directory on App Server 2).

a. Create a zip archive named xfusioncorp_beta.zip of /var/www/html/beta directory.

b. Save the archive in /backup/ on App Server 2. This is a temporary storage, as backups from this location will be clean on weekly basis. Therefore, we also need to save this backup archive on Nautilus Backup Server.

c. Copy the created archive to Nautilus Backup Server server in /backup/ location.

d. Please make sure script won't ask for password while copying the archive file. Additionally, the respective server user (for example, tony in case of App Server 1) must be able to run it.

e. Do not use sudo inside the script.

Note:
The zip package must be installed on given App Server before executing the script. This package is essential for creating the zip archive of the website files. Install it manually outside the script.
Ans: 
# SSH into App server2:
 mkdir -p /scripts
 ls /scripts/
 vi /scripts/ecommerce_backup.sh
#!/bin/bash

# Variables
SOURCE_DIR="/var/www/html/ecommerce"
ARCHIVE_NAME="xfusioncorp_ecommerce.zip"
LOCAL_BACKUP_DIR="/backup"
REMOTE_BACKUP_DIR="/backup"
REMOTE_USER="clint"
REMOTE_HOST="stbkp01.stratos.xfusioncorp.com"
SCRIPT_LOG="/scripts/ecommerce_backup.log"

# Create zip archive
zip -r "${LOCAL_BACKUP_DIR}/${ARCHIVE_NAME}" "$SOURCE_DIR" > "$SCRIPT_LOG" 2>&1

# Check zip success
if [ $? -ne 0 ]; then
    echo "[$(date)] Zip creation failed. Check log at $SCRIPT_LOG"
    exit 1
fi

# Copy archive to backup server
scp "${LOCAL_BACKUP_DIR}/${ARCHIVE_NAME}" "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_BACKUP_DIR}" >> "$SCRIPT_LOG" 2>&1

# Check SCP success
if [ $? -ne 0 ]; then
    echo "[$(date)] File transfer failed. Check log at $SCRIPT_LOG"
    exit 2
fi

echo "[$(date)] Backup completed successfully." >> "$SCRIPT_LOG"

Make the script executable by the intended user (tony in this case):
 chmod +x /scripts/ecommerce_backup.sh
 chown tony:tony /scripts/ecommerce_backup.sh

 Passwordless SSH Setup:

 ssh-keygen -t rsa 

 ssh-copy-id clint@stbkp01.stratos.xfusioncorp.com
Test it:
 ssh clint@stbkp01.stratos.xfusioncorp.com
# install zip on appserver 1
 sudo yum install zip -y 
Run the script manually to test:
 sh /scripts/ecommerce_backup.sh
 ls -l /backup/
 
ssh clint@stbkp01.stratos.xfusioncorp.com
ls /backup/

# Q20 Add Response Headers in Apache
We are working on hardening Apache web server on all app servers. As a part of this process we want to add some of the Apache response headers for security purpose. We are testing the settings one by one on all app servers. As per details mentioned below enable these headers for Apache:

Install httpd package on App Server 2 using yum and configure it to run on 8086 port, make sure to start its service.

Create an index.html file under Apache's default document root i.e /var/www/html and add below given content in it.

Welcome to the xFusionCorp Industries!

Configure Apache to enable below mentioned headers:

X-XSS-Protection header with value 1; mode=block

X-Frame-Options header with value SAMEORIGIN

X-Content-Type-Options header with value nosniff

Note: You can test using curl on the given app server as LBR URL will not work for this task.
Ans:

### 🧰 1. Install Apache and Configure Port
sudo yum install httpd -y

Edit the Apache configuration to listen on port `8086`:

sudo sed -i 's/^Listen 80/Listen 8086/' /etc/httpd/conf/httpd.conf

Also update the `<VirtualHost>` block (if present) to:

<VirtualHost *:8086>
    DocumentRoot "/var/www/html"
    <Directory "/var/www/html">
        Require all granted
    </Directory>
</VirtualHost>

### 📂 2. Create `index.html`
echo "Welcome to the xFusionCorp Industries!" | sudo tee /var/www/html/index.html
### 🔐 3. Enable Security Headers

Add the following lines to the Apache configuration file (`httpd.conf`) or create a separate config file under `/etc/httpd/conf.d/security.conf`:

<IfModule mod_headers.c>
    Header set X-XSS-Protection "1; mode=block"
    Header set X-Frame-Options "SAMEORIGIN"
    Header set X-Content-Type-Options "nosniff"
</IfModule>

Ensure the `mod_headers` module is enabled (usually it is by default on CentOS/RHEL).

### ▶️ 4. Start and Enable Apache
sudo systemctl start httpd
sudo systemctl enable httpd

### 🧪 5. Test with `curl`

Run this from App Server 2:

curl -I http://localhost:8086

You should see headers like:

X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
# Q21 Apache Troubleshooting
xFusionCorp Industries uses some monitoring tools to check the status of every service, application, etc running on the systems. Recently, the monitoring system identified that Apache service is not running on some of the Nautilus Application Servers in Stratos Datacenter.

1. Identify the faulty Nautilus Application Server and fix the issue. Also, make sure Apache service is up and running on all Nautilus Application Servers. Do not try to stop any kind of firewall that is already running.

2. Apache is running on 8089 port on all Nautilus Application Servers and its document root must be /var/www/html on all app servers.

3. Finally you can test from jump host using curl command to access Apache on all app servers and it should be reachable and you should get some static page. E.g. curl http://172.16.238.10:8089/.

Ans:
udo systemctl start httpd

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for banner: 
Job for httpd.service failed because the control process exited with error code.
See "systemctl status httpd.service" and "journalctl -xeu httpd.service" for details.
[banner@stapp03 ~]$ journalctl -xeu httpd.service"
AH00526: Syntax error on line 47 of /etc/httpd/conf/httpd.conf:
Oct 14 13:03:10 stapp03.stratos.xfusioncorp.com httpd[2231]: Invalid command 'Listen 8089', perhaps misspelled or defined by a module not included in the server configuration
Oct 14 13:03:10 stapp03.stratos.xfusioncorp.com systemd[1]: httpd.service: Got notification message from PID 2231 (RELOADING=1, STATUS=Reading configuration...)
Oct 14 13:03:10 stapp03.stratos.xfusioncorp.com systemd[1]: httpd.service: Child 2231 belongs to httpd

 sudo systemctl start httpd
    2  sudo systemctl start httpd
    3  journalctl -xeu httpd.service"
    4  journalctl -xeu httpd.service
    5  sudo vi  /etc/httpd/conf/httpd.conf
    6  sudo systemctl start httpd
    7  journalctl -xeu httpd.service
    8  sudo vi  /etc/httpd/conf/httpd.conf
    9  sudo systemctl start httpd
   10  curl http://172.16.238.12:808
# Q22 Linux GPG Encryption
We have confidential data that needs to be transferred to a remote location, so we need to encrypt that data.We also need to decrypt data we received from a remote location in order to understand its content.

On storage server in Stratos Datacenter we have private and public keys stored at /home/*_key.asc. Use these keys to perform the following actions.

- Encrypt /home/encrypt_me.txt to /home/encrypted_me.asc.

- Decrypt /home/decrypt_me.asc to /home/decrypted_me.txt. (Passphrase for decryption and encryption is kodekloud).

- The user ID you can use is kodekloud@kodekloud.com.
Ans:

### 🔐 **1. Encrypt `/home/encrypt_me.txt` to `/home/encrypted_me.asc`**

#### ✅ Prerequisites:

* Public and private keys are stored at `/home/*_key.asc`
* The recipient (user ID): `kodekloud@kodekloud.com`
* Passphrase for private key (used in decryption): `kodekloud`

#### 🛠 Step-by-Step Encryption:

# Import public and private keys
gpg --import /home/*_key.asc

> This imports both the public and private keys needed.

# Encrypt the file for the recipient
gpg --armor --recipient kodekloud@kodekloud.com --encrypt /home/encrypt_me.txt

> This will create `/home/encrypt_me.txt.asc` in the current directory. Rename it:

mv /home/encrypt_me.txt.asc /home/encrypted_me.asc

### 🔓 **2. Decrypt `/home/decrypt_me.asc` to `/home/decrypted_me.txt`**

# Decrypt the file using the private key
gpg --batch --yes --passphrase kodekloud -o /home/decrypted_me.txt --decrypt /home/decrypt_me.asc

# Q23 Linux LogRotate
The Nautilus DevOps team is ready to launch a new application, which they will deploy on app servers in Stratos Datacenter. They are expecting significant traffic/usage of httpd on app servers after that. This will generate massive logs, creating huge log files. To utilise the storage efficiently, they need to compress the log files and need to rotate old logs. Check the requirements shared below:

a. In all app servers install httpd package.
b. Using logrotate configure httpd logs rotation to monthly and keep only 3 rotated logs.

(If by default log rotation is set, then please update configuration as needed)
Ans:

### 🔧 **a. Install the `httpd` package on all app servers**

On each app server:

sudo yum install -y httpd

Or for systems using `dnf`:

sudo dnf install -y httpd

> Make sure `httpd` is installed on **all** app servers.
###  Start the httpd service:
sudo systemctl start httpd
sudo systemctl enable httpd

### 🔁 **b. Configure logrotate for `httpd`**

The log rotation for httpd is typically managed by a file like:

ls /etc/logrotate.d/httpd

#### ✏️ Edit the config file:

sudo vi /etc/logrotate.d/httpd

Update or ensure the following configuration exists:

/var/log/httpd/*log {
    monthly
    missingok
    rotate 3
    compress
    delaycompress
    notifempty
    create 0640 root adm
    sharedscripts
    postrotate
        /bin/systemctl reload httpd.service > /dev/null 2>/dev/null || true
    endscript
}
### 🔎 Verify your configuration

Run a dry-run of logrotate to make sure the config is valid:

sudo logrotate -d /etc/logrotate.conf

This will **simulate** rotation and confirm there are no errors.

# Generate a log entry: 
curl http://localhost
Then check if logs are created: ls -l /var/log/httpd/
You should see something like access_log and error_log.

# Q24 Application Security
We have a backup management application UI hosted on Nautilus's backup server in Stratos DC. That backup management application code is deployed under Apache on the backup server itself, and Nginx is running as a reverse proxy on the same server. Apache and Nginx ports are 8083 and 8098, respectively. We have iptables firewall installed on this server. Make the appropriate changes to fulfill the requirements mentioned below:

We want to open all incoming connections to Nginx's port and block all incoming connections to Apache's port. Also make sure rules are permanent.
Ans:
To meet your requirements using `iptables`, you’ll need to:

- **Allow incoming traffic** on port **8098** (Nginx).
- **Block incoming traffic** on port **8083** (Apache).
- **Save the rules** so they persist after reboot.

Here’s how you can do it:

### 🛠 Step-by-Step iptables Configuration

1. **Allow incoming traffic to Nginx (port 8098):**
   
   sudo iptables -A INPUT -p tcp --dport 8098 -j ACCEPT
   
2. **Block incoming traffic to Apache (port 8083):**
   
   sudo iptables -A INPUT -p tcp --dport 8083 -j DROP 

3. **Save the rules permanently:**
   - On **Ubuntu/Debian**:
     
     sudo apt install iptables-persistent
     sudo netfilter-persistent save
  
   - On **CentOS/RHEL**:
     
     sudo service iptables save
     
   - On **systems using `iptables-save`**:
     
     sudo iptables-save > /etc/iptables/rules.v4
   
4. **Verify the rules:**
   
   sudo iptables -L -n --line-numbers
   
**Level 3**
# Q1 Apache Redirects
The Nautilus devops team got some requirements related to some Apache config changes. They need to setup some redirects for some URLs. There might be some more changes need to be done. Below you can find more details regarding that:

1.) httpd is already installed on app server 2. Configure Apache to listen on port 8088.

Configure Apache to add some redirects as mentioned below:

a.) Redirect http://stapp02.stratos.xfusioncorp.com:<Port>/ to http://www.stapp02.stratos.xfusioncorp.com:<Port>/ i.e non www to www. This must be a permanent redirect i.e 301

b.) Redirect http://www.stapp02.stratos.xfusioncorp.com:<Port>/blog/ to http://www.stapp02.stratos.xfusioncorp.com:<Port>/news/. This must be a temporary redirect i.e 302.
Ans:

### **Step 1: Update Apache to Listen on Port 8088**

1. SSH into app server 2.
 
   ssh tony@stapp02
   
2. Edit the Apache configuration file (usually one of the following):
   
   sudo vi /etc/httpd/conf/httpd.conf
 
   or on Ubuntu/Debian:
   
   sudo vi /etc/apache2/ports.conf

3. Find the line:

   
   Listen 80
   
   Change it to:
  
   Listen 8088

   sudo grep -i "Listen" /etc/httpd/conf/httpd.conf
   sudo sed -i 's/^Listen 8080/Listen 8088/' /etc/httpd/conf/httpd.conf

4. Save and exit the file.

### **Step 2: Configure Virtual Hosts**

Create or edit a virtual host configuration file (for RHEL/CentOS systems):

sudo vi /etc/httpd/conf.d/redirects.conf

For Ubuntu/Debian:

sudo vi /etc/apache2/sites-available/redirects.conf

Add the following configuration:
# Non-www to www permanent redirect
<VirtualHost *:8088>
    ServerName stapp02.stratos.xfusioncorp.com
    Redirect 301 / http://www.stapp02.stratos.xfusioncorp.com:8088/
</VirtualHost>

# www site with blog -> news temporary redirect
<VirtualHost *:8088>
    ServerName www.stapp02.stratos.xfusioncorp.com
    DocumentRoot /var/www/html

    # Temporary redirect from /blog to /news
    Redirect 302 /blog/ http://www.stapp02.stratos.xfusioncorp.com:8088/news/
</VirtualHost>

Save and close the file.

### **Step 3: Verify Configuration Syntax**

Before restarting Apache, always test the syntax:

sudo apachectl configtest

You should see:

Syntax OK

### **Step 4: Restart Apache**

Restart the Apache service to apply the changes.

For RHEL/CentOS:

sudo systemctl restart httpd

For Ubuntu/Debian:

sudo systemctl restart apache2

### **Step 5: Verify the Redirects**

You can use `curl` to test the redirects:

#### a) Non-www to www (Permanent 301)

curl -I http://stapp02.stratos.xfusioncorp.com:8088/

Expected output includes:

HTTP/1.1 301 Moved Permanently
Location: http://www.stapp02.stratos.xfusioncorp.com:8088/

#### b) Blog to News (Temporary 302)

curl -I http://www.stapp02.stratos.xfusioncorp.com:8088/blog/

Expected output includes:

HTTP/1.1 302 Found
Location: http://www.stapp02.stratos.xfusioncorp.com:8088/news/

# Q2 Install And Configure SFTP
Some of the developers from Nautilus project team have asked for SFTP access to at least one of the app server in Stratos DC. After going through the requirements, the system admins team has decided to configure the SFTP server on App Server 2 server in Stratos Datacenter. Please configure it as per the following instructions:

a. Create a SFTP user ravi and set its password to ksH85UJjhb. There is already a group called ftp, you can utilise the same.

b. Password authentication should be enabled for this user.

c. SFTP user should only be allowed to make SFTP connections.
Ans:
### **1️⃣ Create the user and set the password**

sudo useradd -m -g ftp -s /sbin/nologin ravi
echo "ksH85UJjhb" | sudo passwd --stdin ravi  # (For CentOS/RHEL)

> 🟢 If you’re on Ubuntu/Debian, use:

echo "ravi:ksH85UJjhb" | sudo chpasswd

### **2️⃣ Configure SSHD for SFTP restrictions**

Edit the SSH configuration file:

sudo vi /etc/ssh/sshd_config

Add the following lines **at the end** of the file (or modify if already present):

Match User ravi
    ForceCommand internal-sftp
    PasswordAuthentication yes
    ChrootDirectory /home/ravi
    PermitTunnel no
    AllowTcpForwarding no
    X11Forwarding no

### **3️⃣ Set correct permissions for chroot**
SFTP chroot requires strict ownership:

sudo chown root:root /home/ravi
sudo chmod 755 /home/ravi
sudo mkdir -p /home/ravi/data
sudo chown ravi:ftp /home/ravi/data

This ensures the SFTP root is secure while allowing the user to write inside `/home/ravi/data`.

### **4️⃣ Restart SSH service**

sudo systemctl restart sshd

> (or `sudo systemctl restart ssh` on Ubuntu/Debian)

### **5️⃣ Verify the setup**

From another machine (or local terminal):
# ➡️ Should deny access with a message like “This account is currently not available.”
ssh ravi@stapp02
ravi@stapp02's password: 
This service allows sftp connections only.
Connection to stapp02 closed.

#➡️ Should still work and give you the sftp> prompt.
sftp ravi@<appserver2-ip>
# Q3 Install and Configure Tomcat Server
# Q4 Linux Network Services
# Q5 IPtables Installation And Configuration
# Q6 Linux Nginx as Reverse Proxy
# Q7 Configure protected directories in Apache
# Q8 Linux Process Troubleshooting
# Q9 PAM Authentication For Apache
# Q10 Setup SSL for Nginx

**Level 4**
# Q1 Install and Configure Nginx as an LBR
# Q2 LEMP Troubleshooting
# Q3 Install and Configure PostgreSQL
# Q4  scripts if/else statements
# Q5 Configure LAMP server
# Q6 Install and Configure DB Server
# Q7 Install and Configure Web Application
# Q8 Install and Configure PHP-FPM
# Q9 Configure Nginx + PHP-FPM Using Unix Sock

**Certification Test**
Q1:
One of the developers at Nautilus has stored sensitive data on the jump host in Stratos DC. This data needs to be transferred to an app server. As developers lack access to the app servers, they've requested the system admin team to complete this task.

Please copy the file /tmp/nautilus.txt.gpg from the jump server to App Server 3 at the following location: /home/appdata.
Ans:
sudo scp /tmp/nautilus.txt.gpg banner@stapp03:/home/appdata/

Q2:
After conducting comprehensive security audits on its servers, xFusionCorp Industries security team has instituted several new security measures. Among these measures is the discontinuation of direct root login through SSH.

Disable direct SSH root login across all application servers located in the Stratos Datacenter
Ans:
Disable Root Access: sudo sed -i 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
Reboot sshd Service: sudo systemctl restart sshd
Verify: sudo sshd -T | grep permitrootlogin

Q3:
There is a cron job that needs to be added to the Nautilus storage server in Stratos DC.The cron details is as below:

a. Install cronie package and start crond service.

b. Add this command to the crontab of root user:

/usr/bin/touch test_passed

Make it run every day at 21:30 (use 30 21 format in the expression).

Ans:
Add the cron job to the root user's crontab: 
sudo crontab -e
30 21 * * * /usr/bin/touch /test_passed
You can verify it with: sudo crontab -l

Q4:
The application development team needs some directories created on one of the app servers in Stratos Datacenter. They will use these directories to store some data. They have shared below requirements with us:

Create some directories as below under /opt directory on App server 3 in Stratos Datacenter.

/opt/app/backup/latest
Ans:
Create the required directory structure: mkdir -p /opt/app/backup/latest
Verify the directory: ls -ld /opt/app/backup/latest

Q5:
The Nautilus security team performed an audit on all servers present in Stratos DC. During the audit some critical data/files were identified which were having the wrong permissions as per security standards. Once the report was shared with the production support team, they started fixing the issues one by one. It has been identified that one of the files named /etc/resolv.conf on Nautilus App 3 server has wrong permissions, so that needs to be fixed and the correct ACLs needs to be applied.

a. User virat must not have any permission on this file.

b. User vivek should have read only permission on this file. Further, devops group should have read/write permissions on this file.
Ans:
Double-check: Do users and group exist?:
id virat
id vivek
getent group devops

If not avail:
Create the devops group: sudo groupadd devops
Create users virat and vivek: sudo useradd virat and sudo useradd vivek
Permission removal or ading
sudo setfacl -m u:virat: /etc/resolv.conf
sudo setfacl -m u:vivek:r-- /etc/resolv.conf
sudo setfacl -m g:devops:rw- /etc/resolv.conf
verify:
getfacl /etc/resolv.conf

Q6:
The development team requires specific logs stored within the Nautilus storage server situated in the Stratos DC. Access the designated location on the server to retrieve the necessary logs. Further, perform below actions:

Create a tar archive named logs.tar (under natasha's home) of /var/log/ directory.
Now, create a compressed tar archive as well named logs.tar.gz (under natasha's home) of /var/log/ directory.

Ans:
Create logs.tar in natasha's home directory: sudo tar -cvf /home/natasha/logs.tar /var/log/
Create compressed archive logs.tar.gz in the same directory: sudo tar -czvf /home/natasha/logs.tar.gz /var/log/
Verify: ls -lh /home/natasha/logs.tar*

Q7:
There is some data on Nautilus App Server 3 in Stratos DC. Data needs to be altered in some of the files. On Nautilus App Server 3, alter the /home/BSD.txt file as per details given below.

a. Delete all lines containing the word code and save the results in /home/BSD_DELETE.txt file. (Please be aware of case sensitivity)

b. Replace all occurrences of the word the (look for the exact match) with is and save the results in /home/BSD_REPLACE.txt file.

Note: Let's say you are asked to replace the word to with from. In that case, make sure not to alter any words containing the string itself, for example; upto, contributor etc.
Ans:
Delete all lines that contain the word code (case-sensitive): grep -v 'code' /home/BSD.txt > /home/BSD_DELETE.txt
Replace exact match of the word the with is: sed 's/\bthe\b/is/g' /home/BSD.txt > /home/BSD_REPLACE.txt

Q8:
Some new requirements have been shared by the Nautilus application development team, a new package need to be installed on all app servers in Stratos Datacenter.

Install the bind package on all app servers in Stratos Datacenter and start/enable its service.
Ans:
Install bind package: sudo yum install -y bind
Enable and start the named service: 
sudo systemctl enable named
sudo systemctl start named
Verify: sudo systemctl status named

Q9:
On our Storage server in Stratos Datacenter we are having some issues where the nfsuser user is holding hundreds of processes, which is degrading the performance of the server. Therefore, we have a requirement to limit its maximum processes. Please set its maximum process limits as below:

a. soft limit = 1025

b. hard_limit = 2026
Ans:
Check User Avail: id nfsuser
Modify soft and hard value: sudo vi /etc/security/limits.conf
nfsuser soft nproc 1025
nfsuser hard nproc 2026

Q10:
During recent servers audit, its was observed that some cleanup is needed on all app servers in Stratos Datacenter. Find below more details:

Remove logrotate package from all app servers in Stratos Datacenter.
Ans:
Remove logrotate package: yum remove logrotate -y
Verify removal: rpm -q logrotate
