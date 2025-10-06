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
sudo nano /etc/security/limits.conf
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
# Q6 Linux Find Command
# Q7 Install a package
# Q8 Install Ansible
# Q9 Configure Local Yum repos
# Q10 Linux Services
# Q11 Linux Configure sudo
# Q12 DNS Troubleshooting
# Q13 Linux Firewalld Setup
# Q14 Linux Postfix Mail Server
# Q15 Linux Postfix Troubleshooting
# Q16 Install and Configure HaProxy LBR
# Q17 Haproxy LBR Troubleshooting
# Q18 MariaDB Troubleshooting
# Q19 Linux  Scripts
# Q20 Add Response Headers in Apache
# Q21 Apache Troubleshooting
# Q22 Linux GPG Encryption
# Q23 Linux LogRotate
# Q24 Application Security

**Level 3**
# Q1 Apache Redirects
# Q2 Install And Configure SFTP
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