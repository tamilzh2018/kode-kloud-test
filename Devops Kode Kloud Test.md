Day 1: **Linux User Setup with Non-Interactive Shell**

Create a user named kirsty with a non-interactive shell on App Server 3
sudo useradd -s /usr/sbin/nologin kirsty

Day 2: **Temporary User Setup with Expiry**
As part of the temporary assignment to the Nautilus project, a developer named mark requires access for a limited duration. To ensure smooth access management, a temporary user account with an expiry date is needed. Here's what you need to do:

Create a user named mark on App Server 2 in Stratos Datacenter. Set the expiry date to 2024-01-28, ensuring the user is created in lowercase as per standard protocol.
Ans:
sudo useradd mark -e 2024-01-28

sudo chage -l mark

Day 3: **Secure Root SSH Access**

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

 **Edit the SSH configuration file**

   Use a text editor like `vi` or `nano` to edit the SSH daemon config:   
   sudo vi /etc/ssh/sshd_config
   
 **Locate and update the `PermitRootLogin` directive**

   Find this line:
   plaintext
   #PermitRootLogin yes  

   Change it to:
   plaintext
   PermitRootLogin no   

   > ⚠️ If the line is commented out (`#`), remove the `#` and set it to `no`.

 **Restart the SSH service to apply changes**

   Depending on the system (typically a systemd-based Linux):   
   sudo systemctl restart sshd
   
**Check for overrides in included config files**
sudo grep -ri permitrootlogin /etc/ssh/sshd_config.d/

Double-check the effective config using sshd -T
   sudo sshd -T | grep permitrootlogin

**Repeat for all app servers**

Day 4: **Script Execution Permissions**

In a bid to automate backup processes, the xFusionCorp Industries sysadmin team has developed a new bash script named xfusioncorp.sh. While the script has been distributed to all necessary servers, it lacks executable permissions on App Server 2 within the Stratos Datacenter.

Your task is to grant executable permissions to the /tmp/xfusioncorp.sh script on App Server 2. Additionally, ensure that all users have the capability to execute it.

Ans:

chmod a+rx /tmp/xfusioncorp.sh
ls -l /tmp/xfusioncorp.sh

Day 5: **SElinux Installation and Configuration**

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

Day 6: **Create a Cron Job**
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

Day 7: **Linux SSH Authentication**
The system admins team of xFusionCorp Industries has set up some scripts on jump host that run on regular intervals and perform operations on all app servers in Stratos Datacenter. To make these scripts work properly we need to make sure the thor user on jump host has password-less SSH access to all app servers through their respective sudo users (i.e tony for app server 1). Based on the requirements, perform the following:

Set up a password-less authentication from user thor on jump host to all app servers through their respective sudo users.

Ans: 
Generate SSH key pair (if not already exists):
Check if keys already exist:
ls ~/.ssh/id_rsa.pub
If it doesn’t exist, generate it:
ssh-keygen -t rsa -b 2048
# Copy the public key to the remote servers:
ssh-copy-id tony@stapp01
ssh-copy-id steve@stapp02
ssh-copy-id banner@stapp03
# Test SSH access to the remote servers:
ssh tony@stapp01
ssh steve@stapp02
ssh banner@stapp03

Day 8: **Install Ansible**

During the weekly meeting, the Nautilus DevOps team discussed about the automation and configuration management solutions that they want to implement. While considering several options, the team has decided to go with Ansible for now due to its simple setup and minimal pre-requisites. The team wanted to start testing using Ansible, so they have decided to use jump host as an Ansible controller to test different kind of tasks on rest of the servers.

Install ansible version 4.10.0 on Jump host using pip3 only. Make sure Ansible binary is available globally on this system, i.e all users on this system are able to run Ansible commands.

Ans:
Ensure Python 3 and pip3 are installed: python3 --version and pip3 --version

Install Ansible version 4.10.0 via pip3 to a system-wide location: sudo pip3 install ansible==4.10.0

ansible --version  : ansible [core 2.11.x]   config file = ... Note: Ansible 4.x uses ansible-core 2.11.x internally. That is expected.


Day 9: **MariaDB Troubleshooting**
There is a critical issue going on with the Nautilus application in Stratos DC. The production support team identified that the application is unable to connect to the database. After digging into the issue, the team found that mariadb service is down on the database server.

Look into the issue and fix the same.
Ans:
sudo systemctl status mariadb
chown -R mysql:mysql /var/lib/mysql
sudo systemctl start mariadb
sudo cat /var/log/mariadb/mariadb.log | tail -30
sudo mkdir -p /run/mariadb
sudo chown mysql:mysql /run/mariadb

Day 10: **Linux  Scripts**
The production support team of xFusionCorp Industries is working on developing some bash scripts to automate different day to day tasks. One is to create a bash script for taking websites backup. They have a static website running on App Server 2 in Stratos Datacenter, and they need to create a bash script named beta_backup.sh which should accomplish the following tasks. (Also remember to place the script under /scripts directory on App Server 2).

a. Create a zip archive named xfusioncorp_beta.zip of /var/www/html/beta directory.

b. Save the archive in /backup/ on App Server 2. This is a temporary storage, as backups from this location will be clean on weekly basis. Therefore, we also need to save this backup archive on Nautilus Backup Server.

c. Copy the created archive to Nautilus Backup Server server in /backup/ location.

d. Please make sure script won't ask for password while copying the archive file. Additionally, the respective server user (for example, tony in case of App Server 1) must be able to run it.

e. Do not use sudo inside the script.

Note:
The zip package must be installed on given App Server before executing the script. This package is essential for creating the zip archive of the website files. Install it manually outside the script.
Ans:
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

Day 11: **Install and Configure Tomcat Server**
The Nautilus application development team recently finished the beta version of one of their Java-based applications, which they are planning to deploy on one of the app servers in Stratos DC. After an internal team meeting, they have decided to use the tomcat application server. Based on the requirements mentioned below complete the task:

a. Install tomcat server on App Server 2.

b. Configure it to run on port 3003.

c. There is a ROOT.war file on Jump host at location /tmp.

Deploy it on this tomcat server and make sure the webpage works directly on base URL i.e curl http://stapp02:3003

Ans:
To complete this task, follow the steps below to install and configure **Apache Tomcat** on **App Server 2** (`stapp02`) to serve a Java application (`ROOT.war`) from the base URL on port `3003`.



## ✅ Task Summary

| Task              | Details                                          |
| -- |  |
| Install           | Tomcat                                           |
| Port              | 3003                                             |
| WAR File          | `/tmp/ROOT.war` on Jump Host                     |
| Deployment Target | App Server 2 (`stapp02`)                         |
| Final URL Test    | `curl http://stapp02:3003` should return webpage |



## 🧩 Step-by-Step Instructions

### 🔐 1. SSH into App Server 2

From the **Jump Host**, SSH into App Server 2:

ssh steve@stapp02

### 📦 2. Install Java and Tomcat

Tomcat requires Java to run.

#### Install Java (OpenJDK):

sudo yum install -y java-11-openjdk

> If using Ubuntu/Debian:

sudo apt update
sudo apt install -y openjdk-11-jdk

#### Create Tomcat User and Directories:

sudo useradd -m -U -d /opt/tomcat -s /bin/false tomcat

#### Download and Install Tomcat:
cd /tmp
curl -O https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.109/bin/apache-tomcat-9.0.109.tar.gz
sudo mkdir -p /opt/tomcat
sudo tar -xvzf apache-tomcat-9.0.109.tar.gz -C /opt/tomcat --strip-components=1

#### Set Permissions:
user tomcat exists: getent passwd tomcat
group tomcat exists: getent group tomcat
# if not avail  # Create the tomcat group
sudo groupadd tomcat

# Create the tomcat user, set its home to /opt/tomcat, and disable shell access
sudo useradd -M -s /bin/false -g tomcat -d /opt/tomcat tomcat

cd /opt/tomcat
sudo chown -R tomcat: /opt/tomcat
sudo chmod +x /opt/tomcat/bin/*.sh

### ⚙️ 3. Configure Tomcat to Use Port 3003

Edit the `server.xml` file:

sudo vi /opt/tomcat/conf/server.xml

Find the connector block (around line 69) and change the port from 8080 to 3003:

xml
<Connector port="3003" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443" />


Save and exit.


### 📁 4. Create Systemd Service for Tomcat

Create the service file:

sudo vi /etc/systemd/system/tomcat.service

Paste the following:

[Unit]
Description=Apache Tomcat Web Application Container
After=network.target

[Service]
Type=forking

User=tomcat
Group=tomcat

Environment="JAVA_HOME=/usr/lib/jvm/jre"
Environment="CATALINA_PID=/opt/tomcat/temp/tomcat.pid"
Environment="CATALINA_HOME=/opt/tomcat"
Environment="CATALINA_BASE=/opt/tomcat"

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

Restart=on-failure

[Install]
WantedBy=multi-user.target


Reload and enable the service:

sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable tomcat
sudo systemctl start tomcat

Verify it's running:

sudo systemctl status tomcat

### 📤 5. Copy the `ROOT.war` File from Jump Host to App Server 2

Log On **Jump Host**, run:
scp /tmp/ROOT.war steve@ stapp02:/tmp/

Log On **stapp02**, deploy it:

sudo cp /tmp/ROOT.war /opt/tomcat/webapps/

Tomcat will automatically deploy it. Wait a few seconds and check:

sudo ls /opt/tomcat/webapps/
You should see a `ROOT/` directory created.

### ✅ 7. Test the Application

Back on the **Jump Host**, test using `curl`:

curl http://stapp02:3003


Day 12: **Linux Network Services**
Our monitoring tool has reported an issue in Stratos Datacenter. One of our app servers has an issue, as its Apache service is not reachable on port 8089 (which is the Apache port). The service itself could be down, the firewall could be at fault, or something else could be causing the issue.

Use tools like telnet, netstat, etc. to find and fix the issue. Also make sure Apache is reachable from the jump host without compromising any security settings.

Once fixed, you can test the same using command curl http://stapp01:8089 command from jump host.

Note: Please do not try to alter the existing index.html code, as it will lead to task failure.

Ans:
To resolve the issue with Apache not being reachable on port **8089** on `stapp01`, follow the step-by-step investigation and fix process below. We'll diagnose and correct the root cause without altering application content (like `index.html`).

## ✅ Goal

* Ensure Apache on `stapp01` is **reachable from the jump host** at `http://stapp01:8089`
* **Do not** modify existing web content.
* Diagnose using tools like `telnet`, `netstat`, `ss`, `curl`, etc.
* Fix services or firewall without compromising security.

## 🧩 Step-by-Step Process

### 1. 🔐 SSH into `stapp01`

From the **Jump Host**:
ssh stapp01

### 2. 🕵️ Check Apache Service Status
sudo systemctl status httpd

> If it’s inactive or failed, start it:
sudo systemctl start httpd
sudo systemctl enable httpd

### 3. 🔍 Check if Apache is Listening on Port 8089

Apache usually listens on **port 80** by default, so verify:
sudo netstat -tuln | grep 8089
If netstat is not found, install it:
sudo yum install -y net-tools

If nothing shows, Apache is not configured to listen on port 8089.

### 4. 🛠️ Configure Apache to Listen on Port 8089
grep -i "Listen" /etc/httpd/conf/httpd.conf or 
Edit the Apache port config:

sudo vi /etc/httpd/conf/httpd.conf
Look for:

apache
Listen 80

Change it to:
apache
Listen 8089

Also ensure the `VirtualHost` (if present) is on `*:8089`.

Save and exit.

### 5. 🔁 Restart Apache
sudo systemctl restart httpd
sudo tail -n 50 /var/log/httpd/error_log

### 6. 🔥 Check Firewall Rules

Firewall Service Enabled

sudo systemctl list-units | grep firewalld
sudo systemctl list-units | grep iptables
If neither is active, then the firewall is not the issue, and we should focus on:

Apache config (port 8089)

Apache service status

SELinux (if enforcing)
If iptables is used instead of firewalld, run:
sudo iptables -L -n

Look for any rules that block or allow traffic on port 8089.

If needed, you can temporarily allow port 8089:
If 8089 is **not** listed, add it:

sudo iptables -I INPUT -p tcp --dport 8089 -j ACCEPT
sudo service iptables save
**Check Apache Configuration Syntax**
sudo apachectl configtest

### Check Detailed Error from systemd
sudo systemctl status httpd -l --no-pager

Look for lines containing:

AH00072, AH00558, etc.

Address already in use

Permission denied

Syntax error
**Check if Port 8089 is Already in Use**
sudo netstat -tulnp | grep 8089
This will show you which process is already using port 8089, like this:
tcp  0  0 0.0.0.0:8089  0.0.0.0:*  LISTEN  1234/someprocess

Note: the PID (e.g., 1234) and process name (someprocess).
Stop the Conflicting Process

If port 8089 is used by another service that’s not needed:
sudo kill -9 <PID> or Stop and Disable that service: sudo systemctl stop servicename, sudo systemctl disable servicename
Then try restarting Apache:
sudo systemctl start httpd
 
### Port Conflict

### 7. ✅ Test from Jump Host

From the **Jump Host**, test with:


curl http://stapp01:8089


You should see the website content (HTML) returned.

### 8. 📌 Don't Modify index.html

As instructed, **do not edit** any files like `/var/www/html/index.html` — just ensure they're served correctly on port 8089.

Day 13: **IPtables Installation And Configuration**

We have one of our websites up and running on our Nautilus infrastructure in Stratos DC. Our security team has raised a concern that right now Apache’s port i.e 8083 is open for all since there is no firewall installed on these hosts. So we have decided to add some security layer for these hosts and after discussions and recommendations we have come up with the following requirements:

1. Install iptables and all its dependencies on each app host.

2. Block incoming port 8083 on all apps for everyone except for LBR host.

3. Make sure the rules remain, even after system reboot.

Ans: 
To meet your security team's requirements for securing Apache's port `8083` using `iptables`, here's a step-by-step guide to:

* Install `iptables`
* Restrict access to port `8083` (only allow from LBR host)
* Make sure rules persist after reboot

### ✅ **Assumptions**

* Your OS is Linux (like CentOS, RHEL, Ubuntu, etc.)
* The **LBR host IP** is known (let’s say: `192.168.1.10`)
* Apache is listening on port `8083`
* You are working on **each app host**

Replace the IP address and commands as per your environment if different.

## 🔧 Step-by-Step Solution

### **1. Install `iptables` and dependencies**

**On each app server host:**

# For RHEL/CentOS
sudo yum install -y iptables iptables-services

### **2. Configure iptables rules**

#### 🔐 Block port 8083 for everyone **except** LBR host


# Flush existing rules (optional, if starting clean)
sudo iptables -F

# Allow all existing loopback and established connections
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow LBR host to access port 8083
sudo iptables -A INPUT -p tcp -s 172.16.238.14 --dport 8083 -j ACCEPT

# Block everyone else from port 8083
sudo iptables -A INPUT -p tcp --dport 8083 -j DROP
# List iptables rules with line numbers
sudo iptables -L INPUT --line-numbers

# Allow other necessary ports (SSH, HTTP, etc.)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT     # SSH (if needed)
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT     # HTTP (if needed)
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT    # HTTPS (if needed)

# Reject all other incoming traffic (optional, for tight security)
# sudo iptables -A INPUT -j DROP


Replace `172.16.238.14` with your **actual LBR host IP**.

### **3. Save iptables rules to persist after reboot**

#### On **CentOS/RHEL**:


# Save rules
sudo service iptables save

# Enable iptables service to start at boot
sudo systemctl enable iptables
sudo systemctl start iptables

### ✅ Verification

To confirm rules are in effect:

sudo iptables -L -n

You should see `ACCEPT` for port 8083 from LBR IP and `DROP` for others.

### 🧪 Test Connectivity
log in to LBR server try the testing
| App Server | IP            | Command Example                  |
| - | - | -- |
| stapp01    | 172.16.238.10 | `curl http://172.16.238.10:8083` |
| stapp02    | 172.16.238.11 | `curl http://172.16.238.11:8083` |
| stapp03    | 172.16.238.12 | `curl http://172.16.238.12:8083` |

From:

* **LBR Host**: Test that it can reach Apache on port 8083.
* **Other Hosts**: Ensure they are blocked from accessing port 8083.

Day 14: **Linux Process Troubleshooting**

The production support team of xFusionCorp Industries has deployed some of the latest monitoring tools to keep an eye on every service, application, etc. running on the systems. One of the monitoring systems reported about Apache service unavailability on one of the app servers in Stratos DC.

Identify the faulty app host and fix the issue. Make sure Apache service is up and running on all app hosts. They might not have hosted any code yet on these servers, so you don’t need to worry if Apache isn’t serving any pages. Just make sure the service is up and running. Also, make sure Apache is running on port 8088 on all app servers.

Ans:

## ✅ STEP-BY-STEP SOLUTION

### 🔐 Step 1: SSH into the Jump Host

From your terminal:

ssh thor@jump_host.stratos.xfusioncorp.com
# Password: mjolnir123

### 🔍 Step 2: Check Apache Status on Each App Server

From the **jump host**, SSH into each app server using the provided credentials:

#### A. Check `stapp01`


ssh tony@stapp01
# Password: Ir0nM@n

# Check Apache status
sudo systemctl status httpd

# Check port
sudo ss -tuln | grep 8088 or sudo ss -lptn 'sport = :5002'
exit


#### B. Check `stapp02`


ssh steve@stapp02
# Password: Am3ric@

sudo systemctl status httpd
sudo ss -tuln | grep 8088
exit


#### C. Check `stapp03`


ssh banner@stapp03
# Password: BigGr33n

sudo systemctl status httpd
sudo ss -tuln | grep 8088
sudo netstat -tulpn | grep 8088

exit


> 🔎 One of these will show Apache is **inactive**, **not installed**, or **not running on port 8088**.

## 🛠️ Step 3: Fix Apache on the Faulty Server

Let’s say, for example, `stapp02` is the faulty one (adjust based on what you find):

### A. Install Apache (if missing):


sudo yum install httpd -y    # For RHEL/CentOS


### B. Configure Apache to Listen on Port `8088`

Edit the config:


sudo vi /etc/httpd/conf/httpd.conf


Find the line:


Listen 80


Change it to:


Listen 8088


Also, update any `<VirtualHost *:80>` blocks to:


<VirtualHost *:8088>


Save and exit.

### C. Start and Enable Apache

sudo systemctl restart httpd
sudo systemctl enable httpd

### D. Confirm Apache is Running on Port 8088
sudo ss -tuln | grep 8088


You should see:


LISTEN  0  128  *:8088  *:*

### 🔁 Step 4: Repeat Configuration on All App Servers

Ensure **each** `stapp0X` server has:

* Apache installed
* Listening on port `8088`
* Apache service running and enabled

## ✅ FINAL CHECKLIST (Per Server)

Run these:


sudo systemctl is-active httpd      # should show 'active'
sudo ss -tuln | grep 8088           # should show Apache listening

### 🧪 Test Connectivity
From Jump server try the testing
| App Server | IP            | Command Example                  |
| - | - | -- |
| stapp01    | 172.16.238.10 | `curl http://172.16.238.10:8088` |
| stapp02    | 172.16.238.11 | `curl http://172.16.238.11:8088` |
| stapp03    | 172.16.238.12 | `curl http://172.16.238.12:8088` |

Day 15: **Setup SSL for Nginx**

The system admins team of xFusionCorp Industries needs to deploy a new application on App Server 3 in Stratos Datacenter. They have some pre-requites to get ready that server for application deployment. Prepare the server as per requirements shared below:

1. Install and configure nginx on App Server 3.

2. On App Server 3 there is a self signed SSL certificate and key present at location /tmp/nautilus.crt and /tmp/nautilus.key. Move them to some appropriate location and deploy the same in Nginx.

3. Create an index.html file with content Welcome! under Nginx document root.

4. For final testing try to access the App Server 3 link (either hostname or IP) from jump host using curl command. For example curl -Ik https://<app-server-ip>/.

Ans:

## ✅ Step-by-Step Instructions

### 🔹 1. Install and Configure Nginx on App Server 3

**Login to App Server 3**:
From the **jump host**, SSH into App Server 3:

ssh tony@appserver3
**Install nginx**:
sudo yum install -y nginx     # For RHEL/CentOS
# or
sudo apt update && sudo apt install -y nginx   # For Ubuntu/Debian

**Enable and start nginx**:
sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemctl status nginx

### 🔹 2. Move SSL Certificate and Key to Appropriate Location and Configure Nginx

**Move certificate and key**:

sudo mkdir -p /etc/nginx/ssl
sudo mv /tmp/nautilus.crt /etc/nginx/ssl/
sudo mv /tmp/nautilus.key /etc/nginx/ssl/
sudo chmod 600 /etc/nginx/ssl/nautilus.*

**Configure nginx for SSL**:

Edit the default nginx config or create a new server block:

sudo vi /etc/nginx/nginx.conf

Add the following:

nginx
server {
    listen 443 ssl;
    server_name localhost;

    ssl_certificate /etc/nginx/ssl/nautilus.crt;
    ssl_certificate_key /etc/nginx/ssl/nautilus.key;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}

Optional (to redirect HTTP to HTTPS):

nginx
server {
    listen 80;
    return 301 https://$host$request_uri;
}

**Test and reload nginx**:

sudo nginx -t
sudo systemctl reload nginx

### 🔹 3. Create `index.html` with Content `Welcome!`

echo "Welcome!" | sudo tee /usr/share/nginx/html/index.html

### 🔹 4. Test From Jump Host

Go back to the **jump host** and run:

curl -Ik https://<App-Server-3-IP>/

You should see a response with HTTP/1.1 200 OK and the certificate details, e.g.:


HTTP/1.1 200 OK
Server: nginx/1.x.x
Date: ...
Content-Type: text/html
> Note: If you're using a self-signed cert, add `-k` to bypass certificate verification:

curl -Ik https://<App-Server-3-IP>/

## ✅ Summary of Key Paths

| Component        | Path                          |
| - | -- |
| SSL Certificate  | `/etc/nginx/ssl/nautilus.crt` |
| SSL Key          | `/etc/nginx/ssl/nautilus.key` |
| Web Root         | `/usr/share/nginx/html/`      |
| Nginx SSL Config | `/etc/nginx/conf.d/ssl.conf`  |


Day 16: **Install and Configure Nginx as an LBR**
Day by day traffic is increasing on one of the websites managed by the Nautilus production support team. Therefore, the team has observed a degradation in website performance. Following discussions about this issue, the team has decided to deploy this application on a high availability stack i.e on Nautilus infra in Stratos DC. They started the migration last month and it is almost done, as only the LBR server configuration is pending. Configure LBR server as per the information given below:

a. Install nginx on LBR (load balancer) server.

b. Configure load-balancing with the an http context making use of all App Servers. Ensure that you update only the main Nginx configuration file located at /etc/nginx/nginx.conf.

c. Make sure you do not update the apache port that is already defined in the apache configuration on all app servers, also make sure apache service is up and running on all app servers.

d. Once done, you can access the website using StaticApp button on the top bar.

Ans:
To configure the **LBR (Load Balancer) server** using **NGINX** for the Nautilus team as described, here is a step-by-step guide based on the given requirements:

### ✅ **Step 1: Install NGINX on the LBR Server**

SSH into the LBR server and install NGINX:

sudo yum install nginx -y  # For RHEL/CentOS
# or
sudo apt update && sudo apt install nginx -y  # For Ubuntu/Debian

Enable and start NGINX:

sudo systemctl enable nginx
sudo systemctl start nginx

# SSH into the app servers one by one and check Apache
Once connected to the app server:sudo systemctl status httpd

sudo grep ^Listen /etc/httpd/conf/httpd.conf
 update the port details
### ✅ **Step 2: Configure Load Balancing in `/etc/nginx/nginx.conf`**

You are instructed to update **only** the main config file (`/etc/nginx/nginx.conf`), **not separate config files** under `sites-available` or `conf.d`.

Edit the config:

sudo vi /etc/nginx/nginx.conf

Add a load balancing configuration using the **`http`** context.

Here's an example block you can place **within the `http` block** in `nginx.conf`:

#### 🔧 Example `nginx.conf` additions:

nginx
http {
    upstream backend {
        server <App_Server_1_IP>:<Apache_Port>;
        server <App_Server_2_IP>:<Apache_Port>;
        # Add more if needed
    }

    server {
        listen 80;
        
        location / {
            proxy_pass http://backend;
        }
    }

    # Keep other existing http block configs
}

✅ Replace:

* `<App_Server_1_IP>` and `<App_Server_2_IP>` with the real IP addresses of the app servers.
* `<Apache_Port>` with the port Apache is running on **(usually 80 or 8080)** — **do not change this port**.

Make sure the structure of the file remains valid, and the new `upstream` and `server` blocks are within the `http` context.
sudo nginx -t
sudo systemctl reload nginx

### ✅ **Step 3: Check Apache Services on App Servers**

SSH into each app server and make sure Apache is running:

sudo systemctl status httpd   # For CentOS/RHEL
# or
sudo systemctl status apache2  # For Ubuntu/Debian

Start/enable if needed:

sudo systemctl start httpd
sudo systemctl enable httpd


### ✅ **Step 4: Test and Restart NGINX**

Test the configuration for syntax errors:

sudo nginx -t

If OK, reload/restart NGINX:

sudo systemctl reload nginx
# or
sudo systemctl restart nginx

### ✅ **Step 5: Validate Using StaticApp Button**

After configuration, use the **StaticApp button** on the top bar (as per the interface instructions) to verify that the site is accessible and load balancing is working correctly.

### ✅ **Summary Checklist**

| Task                                                   | Status |
|  |  |
| NGINX installed on LBR server                          | ✅      |
| Load balancing config added to `/etc/nginx/nginx.conf` | ✅      |
| Apache running on all app servers (no port changes)    | ✅      |
| NGINX config tested and reloaded                       | ✅      |
| Website accessible via StaticApp                       | ✅      |

Day 17: **Install and Configure PostgreSQL**
The Nautilus application development team has shared that they are planning to deploy one newly developed application on Nautilus infra in Stratos DC. The application uses PostgreSQL database, so as a pre-requisite we need to set up PostgreSQL database server as per requirements shared below:

PostgreSQL database server is already installed on the Nautilus database server.

a. Create a database user kodekloud_cap and set its password to YchZHRcLkL.

b. Create a database kodekloud_db4 and grant full permissions to user kodekloud_cap on this database.

Note: Please do not try to restart PostgreSQL server service.

To set up the PostgreSQL database user and database as requested — **without restarting the service** — follow these steps. Since PostgreSQL is already installed, we'll connect to it and run the appropriate SQL commands.

### ✅ **Objective Recap:**

1. **User to create:** `kodekloud_cap`
2. **Password:** `YchZHRcLkL`
3. **Database to create:** `kodekloud_db4`
4. **Grant full permissions on database to user:** `kodekloud_cap`

## ✅ Step-by-Step Instructions

### 🔹 Step 1: Switch to the `postgres` user

PostgreSQL is typically managed via the `postgres` Linux user:

sudo -i -u postgres

### 🔹 Step 2: Access the PostgreSQL prompt
psql

You’ll now be at the `psql` prompt:

postgres=#

### 🔹 Step 3: Create the user and set password

CREATE USER kodekloud_cap WITH PASSWORD 'YchZHRcLkL';

### 🔹 Step 4: Create the database

CREATE DATABASE kodekloud_db4;

### 🔹 Step 5: Grant privileges

GRANT ALL PRIVILEGES ON DATABASE kodekloud_db4 TO kodekloud_cap;

### 🔹 Step 6: Exit psql and logout from `postgres` user

\q

Then:

exit

### ✅ Verification (Optional but recommended)

You can verify the connection as the new user:

psql -U kodekloud_cap -d kodekloud_db4 -h localhost

psql -U  kodekloud_aim -d kodekloud_db8 -h localhost

If `.pg_hba.conf` allows password authentication, this will succeed (but **do not modify configs or restart service** as per the instructions).

### ✅ Summary

| Task                             | Status |
| -- |  |
| User `kodekloud_cap` created     | ✅      |
| Password set                     | ✅      |
| Database `kodekloud_db4` created | ✅      |
| Permissions granted              | ✅      |
| PostgreSQL not restarted         | ✅      |

You're all done!

Let me know if you want a quick script version of the SQL commands too.

Day 18: **Configure LAMP server**
xFusionCorp Industries is planning to host a WordPress website on their infra in Stratos Datacenter. They have already done infrastructure configuration—for example, on the storage server they already have a shared directory /vaw/www/html that is mounted on each app host under /var/www/html directory. Please perform the following steps to accomplish the task:

a. Install httpd, php and its dependencies on all app hosts.

b. Apache should serve on port 3004 within the apps.

c. Install/Configure MariaDB server on DB Server.

d. Create a database named kodekloud_db8 and create a database user named kodekloud_tim identified as password TmPcZjtRQx. Further make sure this newly created user is able to perform all operation on the database you created.

e. Finally you should be able to access the website on LBR link, by clicking on the App button on the top bar. You should see a message like App is able to connect to the database using user kodekloud_tim
Ans: 

To complete the task for **xFusionCorp Industries** to host a WordPress website with a shared `/var/www/html` directory, follow these steps on the appropriate hosts. I’ll break it down by part:

## ✅ a. Install `httpd`, `php` and dependencies (on all **app hosts**)

### Run on all app hosts:
sudo yum install -y httpd php php-mysqlnd php-fpm

> If using a Debian-based system (like Ubuntu), replace with:

sudo apt update
sudo apt install -y apache2 php php-mysql libapache2-mod-php

## ✅ b. Configure Apache to serve on **port 3004** (on all **app hosts**)

### Edit Apache config:

sudo sed -i 's/^Listen 80/Listen 3004/' /etc/httpd/conf/httpd.conf
sudo grep ^Listen /etc/httpd/conf/httpd.conf

> On Ubuntu/Debian, update `/etc/apache2/ports.conf` and the default virtual host config:
sudo sed -i 's/80/3004/g' /etc/apache2/ports.conf
sudo sed -i 's/<VirtualHost \*:80>/<VirtualHost \*:3004>/' /etc/apache2/sites-available/000-default.conf

### Allow the new port in the firewall (if applicable):
sudo systemctl list-units | grep firewalld
sudo systemctl list-units | grep iptables
sudo firewall-cmd --permanent --add-port=3004/tcp
sudo firewall-cmd --reload

### Restart Apache:
sudo systemctl enable httpd
sudo systemctl restart httpd

> Ubuntu:
sudo systemctl enable apache2
sudo systemctl restart apache2

## ✅ c. Install & Configure **MariaDB** server (on **DB server**)
### Install MariaDB:
sudo yum install -y mariadb-server
sudo systemctl enable mariadb
sudo systemctl start mariadb

> For Debian-based:
sudo apt install -y mariadb-server
sudo systemctl enable mariadb
sudo systemctl start mariadb

## ✅ d. Create DB, user and grant privileges

### Run in MySQL shell on the DB server:

mysql -u root or sudo mysql

Then execute:

CREATE DATABASE kodekloud_db6;
CREATE USER 'kodekloud_gem'@'%' IDENTIFIED BY 'ksH85UJjhb';
GRANT ALL PRIVILEGES ON kodekloud_db6.* TO 'kodekloud_gem'@'%';
FLUSH PRIVILEGES;
EXIT;

### Optional: Edit `my.cnf` to allow external access (if needed):

sudo sed -i 's/^bind-address.*/bind-address = 0.0.0.0/' /etc/my.cnf
sudo grep ^bind-address /etc/my.cnf
sudo systemctl restart mariadb

## ✅ e. Test connection & verify via LBR (Load Balancer)

At this point:

1. The website files are under `/var/www/html` (shared mount).
2. Apache is running on port `3004`.
3. DB is set up with user `kodekloud_tim` and password `TmPcZjtRQx`.
4. WordPress (or PHP test script) should be configured to connect to DB using these credentials.

## ✅ Add Test PHP Page (on one App Host)

Create a `test.php` file to verify DB connection:

<?php
$servername = "172.16.239.10";  // Replace with actual DB IP or hostname
$username = "kodekloud_gem";
$password = "ksH85UJjhb";
$dbname = "kodekloud_db6";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "App is able to connect to the database using user kodekloud_tim";
?>


Save as `/var/www/html/test.php`, then access it via browser:

http://<LBR_IP>:3004/test.php

## ✅ Final Notes

* Ensure **SELinux** isn’t blocking connections (set to permissive or configure correctly).
* Ensure **DB server’s firewall** allows MySQL port (`3306`).
* Ensure all hostnames or IPs are resolvable between app and DB nodes.

Day 19: **Install and Configure Web Application**
xFusionCorp Industries is planning to host two static websites on their infra in Stratos Datacenter. The development of these websites is still in-progress, but we want to get the servers ready. Please perform the following steps to accomplish the task:

a. Install httpd package and dependencies on app server 3.

b. Apache should serve on port 6100.

c. There are two website's backups /home/thor/official and /home/thor/apps on jump_host. Set them up on Apache in a way that official should work on the link http://localhost:6100/official/ and apps should work on link http://localhost:6100/apps/ on the mentioned app server.


d. Once configured you should be able to access the website using curl command on the respective app server, i.e curl http://localhost:6100/official/ and curl http://localhost:6100/apps/
Ans:
# Install httpd package: 
sudo yum install httpd -y
# Check Listening Port and Modify:
sudo grep ^Listen /etc/httpd/conf/httpd.conf
sudo sed -i 's/^Listen 80/Listen 6100/' /etc/httpd/conf/httpd.conf
sudo grep ^Listen /etc/httpd/conf/httpd.conf
# website's backups avail On jump host, copy the directories to App Server 3
ls /tmp
scp -r /home/thor/beta banner@stapp03:/tmp/
# On App Server 3, move them to Apache document root
sudo mv /tmp/beta /var/www/html/
sudo mv /tmp/cluster /var/www/html/
ls /var/www/html/
    8  curl http://localhost:6100/beta/
    9  sudo systemctl enable httpd
   10  sudo systemctl start httpd
   13  curl http://localhost:6100/beta/
   15  curl http://localhost:6100/cluster/

Day 20: **Configure Nginx + PHP-FPM Using Unix Sock**
The Nautilus application development team is planning to launch a new PHP-based application, which they want to deploy on Nautilus infra in Stratos DC. The development team had a meeting with the production support team and they have shared some requirements regarding the infrastructure. Below are the requirements they shared:

a. Install nginx on app server 2 , configure it to use port 8095 and its document root should be /var/www/html.

b. Install php-fpm version 8.3 on app server 2, it must use the unix socket /var/run/php-fpm/default.sock (create the parent directories if don't exist).

c. Configure php-fpm and nginx to work together.

d. Once configured correctly, you can test the website using curl http://stapp02:8095/index.php command from jump host.

NOTE: We have copied two files, index.php and info.php, under /var/www/html as part of the PHP-based application setup. Please do not modify these files.

Ans:
Here’s a step-by-step guide to **set up Nginx and PHP-FPM 8.3** on **App Server 2** for the Nautilus application, based on your requirements.


### ✅ **Environment** Assumptions:

* OS: **RHEL/CentOS 8 or 9** (uses `dnf`)
* Hostname of App Server 2: `stapp02`
* You are operating from **jump host** with SSH access
* PHP 8.3 will be installed from **Remi repository**, as it’s not available in default repos

## 🚀 Step-by-Step Setup


### 🔧 Step 1: SSH into App Server 2

From the **jump host**, run:

ssh banner@stapp02

### 📦 Step 2: Install Nginx

sudo dnf install -y nginx

### 📁 Step 3: Configure Nginx to Listen on Port 8095

Edit the default config:

sudo vi /etc/nginx/nginx.conf


Inside the `http` block, find or define the `server` block like this:


server {
    listen       8095;
    server_name  localhost;

    root   /var/www/html;
    index  index.php index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
        include        fastcgi_params;
        fastcgi_pass   unix:/var/run/php-fpm/default.sock;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
    }
}


### 🐘 Step 4: Enable PHP 8.3 (via Remi repo)

#### a. Enable Remi Repository:
sudo dnf install -y dnf-utils
sudo dnf install -y https://rpms.remirepo.net/enterprise/remi-release-8.rpm or sudo dnf install -y https://rpms.remirepo.net/enterprise/remi-release-9.rpm
#### b. Enable PHP 8.3 module:
sudo dnf module reset php -y
sudo dnf module enable php:remi-8.3 -y

#### c. Install php-fpm:

sudo dnf install -y php-fpm php-cli php-common

### ⚙️ Step 5: Configure PHP-FPM to Use Custom Socket

Edit PHP-FPM pool configuration:

sudo vi /etc/php-fpm.d/www.conf

Find and change the following lines:

ini
listen = /var/run/php-fpm/default.sock
user = nginx
group = nginx


Also ensure these are uncommented or properly set:

ini
listen.owner = nginx
listen.group = nginx
listen.mode = 0660

> ✅ Create the directory if it doesn’t exist:

sudo mkdir -p /var/run/php-fpm

### ▶️ Step 6: Start and Enable Services

sudo systemctl enable php-fpm --now
sudo systemctl enable nginx --now

### ✅ Step 7: Verify and Test

#### a. Ensure both services are running:
sudo systemctl status php-fpm
sudo systemctl status nginx

#### b. From the **jump host**, test:

curl http://stapp02:8095/index.php

Day 21: **Set Up Git Repository on Storage Server**

The Nautilus development team has provided requirements to the DevOps team for a new application development project, specifically requesting the establishment of a Git repository. Follow the instructions below to create the Git repository on the Storage server in the Stratos DC:

Utilize yum to install the git package on the Storage Server.

Create a bare repository named /opt/news.git (ensure exact name usage).

To meet the Nautilus team's requirements, here's how to **install Git using `yum`** and create a **bare Git repository named `/opt/news.git`** on the **Storage Server**.
Ans:
### 📦 Step 2: Install Git using YUM

sudo yum install -y git

> ✅ This installs Git and its dependencies from the default YUM repositories.
### 🗂️ Step 3: Create a Bare Git Repository
sudo git init --bare /opt/news.git
> ✅ A **bare repo** contains no working directory and is used for collaboration (like a central remote repo).
> ✅ Make sure the path is **exactly** `/opt/news.git` as requested.
### 📂 Step 4: Verify the Repository
ls /opt/news.git
# You should see contents like:
HEAD  config  description  hooks  info  objects  refs

Day 22: **Clone Git Repository on Storage Server**
The DevOps team established a new Git repository last week, which remains unused at present. However, the Nautilus application development team now requires a copy of this repository on the Storage Server in the Stratos DC. Follow the provided details to clone the repository:

The repository to be cloned is located at /opt/official.git

Clone this Git repository to the /usr/src/kodekloudrepos directory. Perform this task using the natasha user, and ensure that no modifications are made to the repository or existing directories, such as changing permissions or making unauthorized alterations.
Ans:
To clone the Git repository located at `/opt/official.git` to `/usr/src/kodekloudrepos` using the `natasha` user **without modifying permissions or making unauthorized changes**, follow these exact steps:

## ✅ Step-by-Step Instructions

### 1. **Switch to the `natasha` user** (if you're not already):

#SSH to Storage Server
ssh natasha@ststor01
Bl@kW

### 2. **Clone the repository to the target directory**

Ensure the target directory exists (create it if needed), then clone the repository:

mkdir -p /usr/src/kodekloudrepos

cd /usr/src/kodekloudrepos
git clone /opt/apps.git

> ✅ This clones the **bare** Git repository into a working directory at the desired location.

### 3. **Verify the clone**

You can verify that the repository was cloned by running:

cd /usr/src/kodekloudrepos or cd official
git status or ls -al

Day 23: **Fork a Git Repository**
There is a Git server utilized by the Nautilus project teams. Recently, a new developer named Jon joined the team and needs to begin working on a project. To begin, he must fork an existing Git repository. Follow the steps below:

Click on the Gitea UI button located on the top bar to access the Gitea page.

Login to Gitea server using username jon and password Jon_pass123.

Once logged in, locate the Git repository named sarah/story-blog and fork it under the jon user.

Note: For tasks requiring web UI changes, screenshots are necessary for review purposes. Additionally, consider utilizing screen recording software such as loom.com to record and share your task completion process.
Ans:
login and choose specific repo and fork

Day 24: **Git Create Branches**

Day 25: **Git Merge Branches**
The Nautilus application development team has been working on a project repository /opt/demo.git. This repo is cloned at /usr/src/kodekloudrepos on storage server in Stratos DC. They recently shared the following requirements with DevOps team:

Create a new branch datacenter in /usr/src/kodekloudrepos/demo repo from master and copy the /tmp/index.html file (present on storage server itself) into the repo. Further, add/commit this file in the new branch and merge back that branch into master branch. Finally, push the changes to the origin for both of the branches.

Ans:
Here's a step-by-step guide to fulfill the Nautilus team's requirements using Git and basic shell commands:

### 🛠️ Step-by-Step Instructions

#### 1. **Navigate to the cloned repo**
cd /usr/src/kodekloudrepos/demo

#### 2. **Create and switch to the new branch `datacenter`**

git checkout -b datacenter

#### 3. **Copy the `index.html` file into the repo**

cp /tmp/index.html .

> This assumes you want `index.html` in the root of the repo. If it needs to go into a subdirectory, adjust the path accordingly.

#### 4. **Add and commit the file**

git add index.html
git commit -m "Add index.html to datacenter branch"

#### 5. **Switch back to `master` branch**
git checkout master

#### 6. **Merge `datacenter` branch into `master`**
git merge datacenter

#### 7. **Push both branches to origin**
git push origin master
git push origin datacenter

Day 26: **Git Manage Remotes**
The xFusionCorp development team added updates to the project that is maintained under /opt/cluster.git repo and cloned under /usr/src/kodekloudrepos/cluster. Recently some changes were made on Git server that is hosted on Storage server in Stratos DC. The DevOps team added some new Git remotes, so we need to update remote on /usr/src/kodekloudrepos/cluster repository as per details mentioned below:

a. In /usr/src/kodekloudrepos/cluster repo add a new remote dev_cluster and point it to /opt/xfusioncorp_cluster.git repository.

b. There is a file /tmp/index.html on same server; copy this file to the repo and add/commit to master branch.

c. Finally push master branch to this new remote origin.

Ans:

### ✅ a. Add a new remote `dev_cluster` pointing to `/opt/xfusioncorp_cluster.git`

cd /usr/src/kodekloudrepos/cluster
git remote add dev_cluster /opt/xfusioncorp_cluster.git

You can verify it was added correctly with:

git remote -v

### ✅ b. Copy `/tmp/index.html` to the repo and commit it to `master`

cp /tmp/index.html /usr/src/kodekloudrepos/cluster/
cd /usr/src/kodekloudrepos/cluster
git add index.html
git commit -m "Add index.html to master branch"

### ✅ c. Push `master` branch to the new remote `dev_cluster`

git push dev_cluster master

### 🧠 Don't Forget:
Make sure you’re on the `master` branch before committing and pushing. You can check with:

git branch

If you're not on `master`, switch to it using:

git checkout master

Day 27: **Git Revert Some Changes**
The Nautilus application development team was working on a git repository /usr/src/kodekloudrepos/official present on Storage server in Stratos DC. However, they reported an issue with the recent commits being pushed to this repo. They have asked the DevOps team to revert repo HEAD to last commit. Below are more details about the task:

In /usr/src/kodekloudrepos/official git repository, revert the latest commit ( HEAD ) to the previous commit (JFYI the previous commit hash should be with initial commit message ).

Use revert official message (please use all small letters for commit message) for the new revert commit.
Ans:
# Navigate to the repository directory:
 cd /usr/src/kodekloudrepos/official/
# Verify the commit history:
git log
# output like: latest commit (4764745a...) added data.txt
Revert the latest commit:
# Set the commit message to revert official:
 git revert 4764745a687769f8a430f587fb4d4aca9c98873b
 
 After running the above command, Git will open your default editor (likely vi or vim). In that editor:

 Delete the default message.

Type exactly: revert official
# Verify the revert commit:
 git log

Day 28: **Git Cherry Pick**
The Nautilus application development team has been working on a project repository /opt/beta.git. This repo is cloned at /usr/src/kodekloudrepos on storage server in Stratos DC. They recently shared the following requirements with the DevOps team:

There are two branches in this repository, master and feature. One of the developers is working on the feature branch and their work is still in progress, however they want to merge one of the commits from the feature branch to the master branch, the message for the commit that needs to be merged into master is Update info.txt. Accomplish this task for them, also remember to push your changes eventually.
Ans:
To merge a specific commit (with message `Update info.txt`) from the `feature` branch into the `master` branch without merging the entire branch, you can use **cherry-pick**. Here's how to do it:

### 🛠️ Step-by-Step Instructions

1. **Navigate to the cloned repo:**
   
   cd /usr/src/kodekloudrepos/beta/
   
2. **Ensure you're on the `master` branch:**
   
   git checkout master
   
3. **Find the commit hash in the `feature` branch:**
   
   git log feature --oneline
   
   Look for the commit with the message `Update info.txt` and copy its hash (e.g., ` 80cf960361e13c8e852798b0187b3366f82ca515`).

4. **Cherry-pick the commit into `master`:**
   
   git cherry-pick  80cf960361e13c8e852798b0187b3366f82ca515
   
5. **Push the updated `master` branch to the remote:**
   
   git push origin master
   
✅ This will merge only the desired commit into `master` without affecting other work in the `feature` branch.

Day 29: **Manage Git Pull Requests**
Max want to push some new changes to one of the repositories but we don't want people to push directly to master branch, since that would be the final version of the code. It should always only have content that has been reviewed and approved. We cannot just allow everyone to directly push to the master branch. So, let's do it the right way as discussed below:


SSH into storage server using user max, password Max_pass123 . There you can find an already cloned repo under Max user's home.

Max has written his story about The 🦊 Fox and Grapes 🍇

Max has already pushed his story to remote git repository hosted on Gitea branch story/fox-and-grapes

Check the contents of the cloned repository. Confirm that you can see Sarah's story and history of commits by running git log and validate author info, commit message etc.

Max has pushed his story, but his story is still not in the master branch. Let's create a Pull Request(PR) to merge Max's story/fox-and-grapes branch into the master branch

Click on the Gitea UI button on the top bar. You should be able to access the Gitea page.

UI login info:

- Username: max

- Password: Max_pass123

PR title : Added fox-and-grapes story

PR pull from branch: story/fox-and-grapes (source)

PR merge into branch: master (destination)

Before we can add our story to the master branch, it has to be reviewed. So, let's ask tom to review our PR by assigning him as a reviewer

Add tom as reviewer through the Git Portal UI

Go to the newly created PR

Click on Reviewers on the right

Add tom as a reviewer to the PR

Now let's review and approve the PR as user Tom

Login to the portal with the user tom

Logout of Git Portal UI if logged in as max

UI login info:

- Username: tom

- Password: Tom_pass123

PR title : Added fox-and-grapes story

Review and merge it.

Great stuff!! The story has been merged! 👏

Note: For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:

Login in to stoarge server 
cd /home/max/story-blog
- git log and git status  to check coomit details
- go to ui portal: create pull request with max and assign to tom once request created
- go to ui portal: review pull request with tom and approve the pull request and merge

Day 30: **Git hard reset**
The Nautilus application development team was working on a git repository /usr/src/kodekloudrepos/official present on Storage server in Stratos DC. This was just a test repository and one of the developers just pushed a couple of changes for testing, but now they want to clean this repository along with the commit history/work tree, so they want to point back the HEAD and the branch itself to a commit with message add data.txt file. Find below more details:

In /usr/src/kodekloudrepos/official git repository, reset the git commit history so that there are only two commits in the commit history i.e initial commit and add data.txt file.

Also make sure to push your changes.

Ans:
To reset the Git commit history in `/usr/src/kodekloudrepos/cluster` so that only the **initial commit** and the commit with message **"add data.txt file"** remain, follow these steps carefully:

### 🛠️ Step-by-Step Instructions

1. **Navigate to the repository:**
   
   cd /usr/src/kodekloudrepos/cluster
  
2. **Find the commit hash for "add data.txt file":**
   
   git log --oneline
   
   Look for the commit with the message `add data.txt file` and copy its hash (e.g., `abc1234`).

3. **Reset the branch to that commit:**
   
   git reset --hard abc1234

4. **Remove all commits before the initial and "add data.txt file" using rebase:**
   If the initial commit is still part of the history, you can use interactive rebase:
   
   git rebase -i --root
   
   - This will open an editor showing all commits.
   - Keep only the initial commit and the `add data.txt file` commit.
   - Delete or mark others with `drop`.

5. **Force push the cleaned history to remote:**
   
   git push origin HEAD --force
   
### ✅ Final Check
To verify:

git log --oneline

You should see only two commits:
- The initial commit
- The `add data.txt file` commit

Day 31: **Git Stash**
The Nautilus application development team was working on a git repository /usr/src/kodekloudrepos/cluster present on Storage server in Stratos DC. One of the developers stashed some in-progress changes in this repository, but now they want to restore some of the stashed changes. Find below more details to accomplish this task:

Look for the stashed changes under /usr/src/kodekloudrepos/cluster git repository, and restore the stash with stash@{1} identifier. Further, commit and push your changes to the origin.

Ans:
To complete the task of restoring a specific stashed change (`stash@{1}`), committing it, and pushing it to the remote repository for the Nautilus application development team, follow these steps:

## ✅ **Step-by-Step Solution**

### 🔹 1. **Go to the repository**

cd /usr/src/kodekloudrepos/cluster

### 🔹 2. **Check stash list**
To confirm the stash exists:

git stash list
You should see something like:
stash@{0}: WIP on ...
stash@{1}: WIP on ...

Confirm that `stash@{1}` is the one you need.
### 🔹 3. **Apply the stash**

Restore the changes from `stash@{1}`:

git stash apply stash@{1}

> 📝 Note: This applies the stash without deleting it. If you want to apply and remove it from stash, use `pop` instead of `apply`. But here we are only applying.

### 🔹 4. **Check status**

Make sure the changes were applied:

git status

Verify which files are modified or added.

### 🔹 5. **Add and commit changes**
git add .
git commit -m "Restored changes from stash@{1}"

### 🔹 6. **Push to origin**
git branch --show-current

git push origin <branch-name>

Day 32: **Git Rebase**
The Nautilus application development team has been working on a project repository /opt/media.git. This repo is cloned at /usr/src/kodekloudrepos on storage server in Stratos DC. They recently shared the following requirements with DevOps team:

One of the developers is working on feature branch and their work is still in progress, however there are some changes which have been pushed into the master branch, the developer now wants to rebase the feature branch with the master branch without loosing any data from the feature branch, also they don't want to add any merge commit by simply merging the master branch into the feature branch. Accomplish this task as per requirements mentioned.

Also remember to push your changes once done.

Ans:
To accomplish the task of **rebasing a feature branch with the master branch without losing data and without creating a merge commit**, follow these steps **on the storage server** (`Stratos DC`) where the repository is located at `/usr/src/kodekloudrepos`.

## ✅ Summary of the Task:

* Path to cloned repo: `/usr/src/kodekloudrepos`
* You need to:

  * Rebase the **feature branch** with the **master** branch.
  * Avoid merge commits (so **do not use** `git merge`, use `git rebase`).
  * Ensure no data is lost from the feature branch.
  * Push changes after the rebase.



## 🧪 Step-by-Step Solution:

### 1. Navigate to the repo

cd /usr/src/kodekloudrepos/media

### 2. Confirm current branches

git branch
* You should see `master` and a `feature` branch (could be named something like `feature-x`, `feature-1`, etc.)
* Assume it’s called `feature` for this example.

### 3. Checkout the feature branch

git checkout feature

### 4. Rebase the feature branch with master

git rebase master

* This reapplies the commits from `feature` branch **on top of** the latest `master`.
* It avoids a merge commit and keeps the history linear.
* If there are conflicts, Git will prompt you to resolve them.

### 5. If conflicts occur (optional)

If you get a conflict:

# Edit the conflicting files and fix the issues
git add <conflicted-file>

# Continue the rebase
git rebase --continue

Repeat until rebase is complete.

### 6. Push the rebased feature branch

Since the rebase rewrites commit history, you’ll need to force push:

git push origin feature --force

> ⚠️ Use `--force` **only** because you are intentionally rewriting history with a rebase.
 veiry : git log

Day 33: **Resolve Git Merge Conflicts**
Sarah and Max were working on writting some stories which they have pushed to the repository. Max has recently added some new changes and is trying to push them to the repository but he is facing some issues. Below you can find more details:

SSH into storage server using user max and password Max_pass123. Under /home/max you will find the story-blog repository. Try to push the changes to the origin repo and fix the issues. The story-index.txt must have titles for all 4 stories. Additionally, there is a typo in The Lion and the Mooose line where Mooose should be Mouse.

Click on the Gitea UI button on the top bar. You should be able to access the Gitea page. You can login to Gitea server from UI using username sarah and password Sarah_pass123 or username max and password Max_pass123.

Note: For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.
Ans:

1  cd /home/max/story-blog/
2  sudo git status
3  sudo git pull
4  sudo vi story-index.txt 
5  sudo git add story-index.txt 
6 git commit -m "Fix typo and ensure all 4 story titles are listed"
7  sudo git push origin master
8  sudo git status
 
Day 34: **Git Hook**
The Nautilus application development team was working on a git repository /opt/beta.git which is cloned under /usr/src/kodekloudrepos directory present on Storage server in Stratos DC. The team want to setup a hook on this repository, please find below more details:

Merge the feature branch into the master branch`, but before pushing your changes complete below point.

Create a post-update hook in this git repository so that whenever any changes are pushed to the master branch, it creates a release tag with name release-2023-06-15, where 2023-06-15 is supposed to be the current date. For example if today is 20th June, 2023 then the release tag must be release-2023-06-20. Make sure you test the hook at least once and create a release tag for today's release.

Finally remember to push your changes.
Note: Perform this task using the natasha user, and ensure the repository or existing directory permissions are not altered.

Ans:

    1  cd /opt/cluster.git/hooks/
    2  vi post-update
    3  cd /usr/src/kodekloudrepos/cluster/
    4  git branch
    5  git checkout master
    6  git pull
    7  git merge feature -m "Merging feature into master"
    8  chmod +x /opt/cluster.git/hooks/post-update
    9  vi /opt/cluster.git/hooks/post-update
    #!/bin/bash

# Set tag name with current date
DATE=$(date +%F)
TAG="release-$DATE"

# Path to the Git repo (bare)
REPO_PATH="/opt/beta.git"

# Check if 'master' branch exists
if git --git-dir="$REPO_PATH" rev-parse refs/heads/master >/dev/null 2>&1; then
    # Check if the tag already exists
    if ! git --git-dir="$REPO_PATH" rev-parse "refs/tags/$TAG" >/dev/null 2>&1; then
        # Create the tag on the latest commit of master
        git --git-dir="$REPO_PATH" tag "$TAG" refs/heads/master
        echo "✅ Tag $TAG created on master branch"
    else
        echo "⚠️ Tag $TAG already exists"
    fi
else
    echo "❌ 'master' branch not found"
fi

   10  git config list
   11  git config --global user.name "Natasha"
   12  git config --global user.email "natasha@ststor01.stratos.xfusioncorp.com"
   13  git push origin master
   14  cd /opt/cluster.git/
   15  git show-ref --tags

Day 35: **Install Docker Packages and Start Docker Service**
*Install Docker Packages and Start Docker Service** 
The Nautilus DevOps team aims to containerize various applications following a recent meeting with the application development team. They intend to conduct testing with the following steps:
Install docker-ce and docker compose packages on App Server 3.

Initiate the docker service.

Ans:
# Install using the rpm repository: 
sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
# Install Docker Engine
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable --now docker

Day 36: **Deploy Nginx Container on Application Server**
The Nautilus DevOps team is conducting application deployment tests on selected application servers. They require a nginx container deployment on Application Server 1. Complete the task with the following instructions:


On Application Server 1 create a container named nginx_1 using the nginx image with the alpine tag. Ensure container is in a running state.
Ans:
docker pull nginx:alpine
docker run -d -p 8080:80 --name nginx_1 nginx:alpine
docker ps
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nginx_1
curl 172.12.0.2
Day 37: **Copy File to Docker Container**
The Nautilus DevOps team possesses confidential data on App Server 1 in the Stratos Datacenter. A container named ubuntu_latest is running on the same server. Copy an encrypted file /tmp/nautilus.txt.gpg from the docker host to the ubuntu_latest container located at /home/. Ensure the file is not modified during this operation.

Ans:
To copy the encrypted file `/tmp/nautilus.txt.gpg` from the Docker host to the `ubuntu_latest` container without modifying it, follow these steps:
 1  docker ps -a
    2  docker cp /tmp/nautilus.txt.gpg ubuntu_latest:/home/nautilus.txt.gpg
    3  docker exec -it ubuntu_latest ls -l /home
    4  history
Day 38: **Pull Docker Image**
Ans:
# Pull the image
docker pull busybox:musl

# Re-tag the image old tag new tag
docker tag busybox:musl busybox:blog
Day 39: **Create a Docker Image From Container**
One of the Nautilus developer was working to test new changes on a container. He wants to keep a backup of his changes to the container. A new request has been raised for the DevOps team to create a new image from this container. Below are more details about it:

a. Create an image media:devops on Application Server 1 from a container ubuntu_latest that is running on same server.
Ans:
docker ps
docker commit ubuntu_latest media:devops
Day 40: **Docker EXEC Operations**
One of the Nautilus DevOps team members was working to configure services on a kkloud container that is running on App Server 3 in Stratos Datacenter. Due to some personal work he is on PTO for the rest of the week, but we need to finish his pending work ASAP. Please complete the remaining work as per details given below:

a. Install apache2 in kkloud container using apt that is running on App Server 3 in Stratos Datacenter.

b. Configure Apache to listen on port 3004 instead of default http port. Do not bind it to listen on specific IP or hostname only, i.e it should listen on localhost, 127.0.0.1, container ip, etc.

c. Make sure Apache service is up and running inside the container. Keep the container in running state at the end
Ans:

    1 apt install apache2
    2 sed -i 's/^Listen 80$/Listen 6100/' /etc/apache2/ports.conf
    3 service apache2 restart
    4  echo "ServerName localhost" > /etc/apache2/conf-available/servername.conf
    5  a2enconf servername
    6  service apache2 reload
    7  service apache2 restart
    8  apt install -y net-tools
    9  netstat -plant | grep 6100
Day 41: **Write a Docker File**
As per recent requirements shared by the Nautilus application development team, they need custom images created for one of their projects. Several of the initial testing requirements are already been shared with DevOps team. Therefore, create a docker file /opt/docker/Dockerfile (please keep D capital of Dockerfile) on App server 2 in Stratos DC and configure to build an image with the following requirements:

a. Use ubuntu:24.04 as the base image.

b. Install apache2 and configure it to work on 8085 port. (do not update any other Apache configuration settings like document root etc).
Ans:
# Use Ubuntu 24.04 base image
FROM ubuntu:24.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Updates package lists, installs Apache2, and cleans up cached files to reduce image size.
RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean

# Modifies Apache’s configuration to listen on port 8085 instead of 80.
RUN sed -i 's/^Listen 80$/Listen 8085/' /etc/apache2/ports.conf

# Declares that the container will listen on port 8085.
EXPOSE 8085

# Starts Apache in the foreground so the container stays alive.
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
Day 42: **Create a Docker Network**
The Nautilus DevOps team needs to set up several docker environments for different applications. One of the team members has been assigned a ticket where he has been asked to create some docker networks to be used later. Complete the task based on the following ticket description:

a. Create a docker network named as news on App Server 1 in Stratos DC.

b. Configure it to use macvlan drivers.

c. Set it to use subnet 192.168.30.0/24 and iprange 192.168.30.0/24.
Ans:
# Interface (eth0): You must confirm the actual name of the physical interface on App Server 1. Use:
ip link show
ex: default primary interface : eth0
# Docker Command to Create the news macvlan Network:
docker network create \
  -d macvlan \
  --subnet=192.168.30.0/24 \
  --ip-range=192.168.30.0/24 \
  --gateway=192.168.30.1 \
  -o parent=eth0 \
  news

# Test:After running the command, confirm that the network has been created:
docker network ls
docker network inspect news

Day 43: **Docker Ports Mapping**
The Nautilus DevOps team is planning to host an application on a nginx-based container. There are number of tickets already been created for similar tasks. One of the tickets has been assigned to set up a nginx container on Application Server 1 in Stratos Datacenter. Please perform the task as per details mentioned below:

a. Pull nginx:stable docker image on Application Server 1.
b. Create a container named ecommerce using the image you pulled.
c. Map host port 8088 to container port 80. Please keep the container in running state.
Ans:
docker run -itd --name ecommerce -p 8088:80 nginx:stable

Day 44: **Write a Docker Compose File**
The Nautilus application development team shared static website content that needs to be hosted on the httpd web server using a containerised platform. The team has shared details with the DevOps team, and we need to set up an environment according to those guidelines. Below are the details:

a. On App Server 3 in Stratos DC create a container named httpd using a docker compose file /opt/docker/docker-compose.yml (please use the exact name for file).
b. Use httpd (preferably latest tag) image for container and make sure container is named as httpd; you can use any name for service.
c. Map 80 number port of container with port 5001 of docker host.
d. Map container's /usr/local/apache2/htdocs volume with /opt/data volume of docker host which is already there. (please do not modify any data within these locations).
Ans:
version: '3.8'
services:
  httpd_service:
    image: httpd:latest
    container_name: httpd
    ports:
      - "5001:80"  # Maps port 80 of the container to port 5001 of the host
    volumes:
      - /opt/data:/usr/local/apache2/htdocs  # Maps /opt/data on host to container's /usr/local/apache2/htdocs
    restart: always  # Ensure the container restarts automatically if it fails
    networks:
      - webnet
Day 45: **Resolve Dockerfile Issues**
The Nautilus DevOps team is working to create new images per requirements shared by the development team. One of the team members is working to create a Dockerfile on App Server 1 in Stratos DC. While working on it she ran into issues in which the docker build is failing and displaying errors. Look into the issue and fix it to build an image as per details mentioned below:

a. The Dockerfile is placed on App Server 1 under /opt/docker directory.
b. Fix the issues with this file and make sure it is able to build the image.
c. Do not change base image, any other valid configuration within Dockerfile, or any of the data been used — for example, index.html.

Note: Please note that once you click on FINISH button all the existing containers will be destroyed and new image will be built from your Dockerfile.
Ans:
SSH steve@stapp01
# Exising FIle: cat /opt/docker/Dockerfile

FROM httpd:2.4.43

RUN sed -i "s/Listen 80/Listen 8080/g" /usr/local/apache2/conf/httpd.conf

RUN sed -i '/LoadModule\ ssl_module modules\/mod_ssl.so/s/^#//g' conf/httpd.conf

RUN sed -i '/LoadModule\ socache_shmcb_module modules\/mod_socache_shmcb.so/s/^#//g' conf/httpd.conf

RUN sed -i '/Include\ conf\/extra\/httpd-ssl.conf/s/^#//g' conf/httpd.conf

RUN cp certs/server.crt /usr/local/apache2/conf/server.crt

RUN cp certs/server.key /usr/local/apache2/conf/server.key

RUN cp html/index.html /usr/local/apache2/htdocs
# Solution:
# Missing WORKDIR and COPY usage:

You're using RUN cp assuming that certs/ and html/ already exist in the container context. They likely exist on your host, so you should be using COPY instead.

# Use a single RUN for multiple commands:
Combine the multiple sed commands into a single RUN to reduce image layers.
# Expose port 8080 and 443:
Since HTTP is moved to port 8080 and SSL is enabled (default on 443), explicitly expose those.

**Final Optimized Dockerfile**
FROM httpd:2.4.43
# Switch Apache to listen on port 8080 and enable SSL
RUN sed -i "s/Listen 80/Listen 8080/g" /usr/local/apache2/conf/httpd.conf && \
    sed -i '/LoadModule\ ssl_module modules\/mod_ssl.so/s/^#//g' conf/httpd.conf && \
    sed -i '/LoadModule\ socache_shmcb_module modules\/mod_socache_shmcb.so/s/^#//g' conf/httpd.conf && \
    sed -i '/Include\ conf\/extra\/httpd-ssl.conf/s/^#//g' conf/httpd.conf

# Copy certificate and key
COPY certs/server.crt /usr/local/apache2/conf/
COPY certs/server.key /usr/local/apache2/conf/

# Replace index page
COPY html/index.html /usr/local/apache2/htdocs/

# Expose HTTP and HTTPS ports
EXPOSE 8080 443

# Start Apache in the foreground
CMD ["httpd-foreground"]

**build the image:**
docker build -t myhttpd . or docker build -t httpd-2.4.3 -f /opt/docker/Dockerfile . #-f /opt/docker/Dockerfile: Specifies the path to the Dockerfile you want to use for the build. In this case, it's located at /opt/docker/Dockerfile.
**run a container to test it:**
docker run -d -p 8080:8080 -p 443:443 --name webtest myhttpd
**Test via browser or curl:**
curl http://localhost:8080
Day 46: **Deploy an App on Docker Containers**

Day 47: **Docker Python App**

Day 48: **Deploy Pods in Kubernetes Cluster**

Day 49: **Deploy Applications with Kubernetes Deployments**

Day 50: **Set Resource Limits in Kubernetes Pods**

Day 51: **Execute Rolling Updates in Kubernetes**

Day 52: **Revert Deployment to Previous Version in Kubernetes**

Day 53: **Resolve VolumeMounts Issue in Kubernetes**

Day 54: **Kubernetes Shared Volumes**

Day 55: **Kubernetes Sidecar Containers**

Day 56: **Deploy Nginx Web Server on Kubernetes Cluster**

Day 57: **Print Environment Variables**

Day 58: **Deploy Grafana on Kubernetes Cluster**

Day 59: **Troubleshoot Deployment issues in Kubernetes**

Day 60: **Persistent Volumes in Kubernetes**

Day 61: **Init Containers in Kubernetes**

Day 62: **Manage Secrets in Kubernetes**

Day 63: **Deploy Iron Gallery App on Kubernetes**

Day 64: **Fix Python App Deployed on Kubernetes Cluster**

Day 65: **Deploy Redis Deployment on Kubernetes**

Day 66: **Deploy MySQL on Kubernetes**

Day 67: **Deploy Guest Book App on Kubernetes**

Day 68: **Set Up Jenkins Server**

Day 69: **Install Jenkins Plugins**

Day 70: **Configure Jenkins User Access**

Day 71: **Configure Jenkins Job for Package Installation**

Day 72: **Jenkins Parameterized Builds**

Day 73: **Jenkins Scheduled Jobs**

Day 74: **Jenkins Database Backup Job**

Day 75: **Jenkins Slave Nodes**

Day 76: **Jenkins Project Security**

Day 77: **Jenkins Deploy Pipeline**

Day 78: **Jenkins Conditional Pipeline**

Day 79: **Jenkins Deployment Job**

Day 80: **Jenkins Chained Builds**

Day 81: **Jenkins Multistage Pipeline**

Day 82: **Create Ansible Inventory for App Server Testing**

Day 83: **Troubleshoot and Create Ansible Playbook**

Day 84: **Copy Data to App Servers using Ansible**

Day 85: **Create Files on App Servers using Ansible**

Day 86: **Ansible Ping Module Usage**

Day 87: **Ansible Install Package**

Day 88: **Ansible Blockinfile Module**

Day 89: **Ansible Manage Services**

Day 90: **Managing ACLs Using Ansible**

Day 91: **Ansible Lineinfile Module**

Day 92: **Managing Jinja2 Templates Using Ansible**

Day 93: **Using Ansible Conditionals**

Day 94: **Create VPC Using Terraform**

Day 95: **Create Security Group Using Terraform**

Day 96: **Create EC2 Instance Using Terraform**

Day 97: **Create IAM Policy Using Terraform**

Day 98: **Launch EC2 in Private VPC Subnet Using Terraform**

Day 99: **Attach IAM Policy for DynamoDB Access Using Terraform**

Day 100: **Create and Configure Alarm Using CloudWatch Using Terraform**