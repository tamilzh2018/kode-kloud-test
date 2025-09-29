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

# Q9 Script Execution Permissions

# Q10 File Permission Correction

# Q11 String Replacement

# Q12 Secure Data Transfer

# Q13 Restrict Cron Access

# Q14 Default GUI Boot Configuration

# Q15 Timezone Alignment

# Q16 Firewall Configuration

# Q17 Process Limit Adjustment

# Q18 SElinux Installation and Configuration

**Level 2**
# Q1 Create a Cron Job
# Q2 Linux Banner
# Q3 Linux Collaborative Directories
# Q4 Linux String Substitute (sed)
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
# Q19 Linux Bash Scripts
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
# Q4 Bash scripts if/else statements
# Q5 Configure LAMP server
# Q6 Install and Configure DB Server
# Q7 Install and Configure Web Application
# Q8 Install and Configure PHP-FPM
# Q9 Configure Nginx + PHP-FPM Using Unix Sock