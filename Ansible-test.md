Day 1: **Troubleshoot and Create Ansible Playbook**
An Ansible playbook needs completion on the jump host, where a team member left off. Below are the details:

The inventory file /home/thor/ansible/inventory requires adjustments. The playbook must run on App Server 1 in Stratos DC. Update the inventory accordingly.


Create a playbook /home/thor/ansible/playbook.yml. Include a task to create an empty file /tmp/file.txt on App Server 1.


Note: Validation will run the playbook using the command ansible-playbook -i inventory playbook.yml. Ensure the playbook works without any additional arguments.

Ans:
# Edit the inventory file 
vi /home/thor/ansible/inventory
[appserver]
stapp01 ansible_host=172.16.238.10 ansible_user=tony ansible_ssh_pass=YourPasswordHere

#Crate a playbook 
vi /home/thor/ansible/playbook.yml

- name: Create a file on App Server 1
  hosts: appserver
  become: yes
  tasks:
    - name: Create empty file /tmp/file.txt
      file:
        path: /tmp/file.txt
        state: touch

# Test- Make sure both files are saved with proper permissions, then validate with:
cd /home/thor/ansible
ansible-playbook -i inventory playbook.yml

Day 2: **Create Ansible Inventory for App Server Testing**
The Nautilus DevOps team is testing Ansible playbooks on various servers within their stack. They've placed some playbooks under /home/thor/playbook/ directory on the jump host and now intend to test them on app server 1 in Stratos DC. However, an inventory file needs creation for Ansible to connect to the respective app. Here are the requirements:

a. Create an ini type Ansible inventory file /home/thor/playbook/inventory on jump host.

b. Include App Server 1 in this inventory along with necessary variables for proper functionality.

c. Ensure the inventory hostname corresponds to the server name as per the wiki, for example stapp01 for app server 1 in Stratos DC.

Note: Validation will execute the playbook using the command ansible-playbook -i inventory playbook.yml. Ensure the playbook functions properly without any extra arguments.
Ans:
Absolutely! Here's how to create a valid **INI-style Ansible inventory file** that meets all the requirements for testing playbooks on **App Server 1 (stapp01)** in Stratos DC.
### 🛠️ Step-by-Step Inventory File Setup

Create the file at `/home/thor/playbook/inventory` with the following content:

[webservers]
stapp01 ansible_host=172.16.238.10 ansible_user=tony ansible_ssh_private_key_file=/home/thor/.ssh/id_rsa

### 📋 Explanation of Each Component

- **[webservers]**: This is a group name. You can name it anything relevant (e.g., `appservers`, `stratos`, etc.), but `webservers` is commonly used.
- **stapp01**: This is the hostname that matches the wiki naming convention for App Server 1.
- **ansible_host=172.16.238.10**: The IP address of App Server 1 in Stratos DC.
- **ansible_user=tony**: The SSH user used to connect to the server.
- **ansible_ssh_private_key_file=/home/thor/.ssh/id_rsa**: Path to the SSH private key used for authentication.

> ⚠️ Make sure the SSH key exists at that path and has the correct permissions (`chmod 600` is typical).

### ✅ Final Check

Once the inventory file is saved, you can run the playbook using:

ansible-playbook -i /home/thor/playbook/inventory /home/thor/playbook/playbook.yml

Day 3: **Configure Default SSH User for Ansible**
The Nautilus DevOps team aims to manage all servers within the stack using Ansible, utilizing a common sudo user across all servers. They plan to use this user for various tasks on each server. While this isn't finalized, they're starting with testing. Ansible is already installed on the jump host via yum. Here's the requirement:

On the jump host, modify the default configuration of Ansible to enable the use of jim as the default SSH user for all hosts. Ensure to make changes within Ansible's default configuration without creating a new one.
Ans:
# Edit the ansible.cfg file:
sudo nano /etc/ansible/ansible.cfg
# Add the remote_user setting:
In the [defaults] section, add the following line:

remote_user = jim
# So, the [defaults] section will look like this:

[defaults]
host_key_checking = False
remote_user = jim

Day 4: **Copy Data to App Servers using Ansible**

# Edit the inventory file 
vi /home/thor/ansible/inventory
[appservers]
stapp01 ansible_host=172.16.238.10 ansible_user=tony ansible_ssh_pass=Ir0nM@n
stapp02 ansible_host=172.16.238.11 ansible_user=steve ansible_ssh_pass=Am3ric@
stapp03 ansible_host=172.16.238.12 ansible_user=banner ansible_ssh_pass=BigGr33n

#Crate a playbook 
vi /home/thor/ansible/playbook.yml

- name: Copy a file on App Servers
  hosts: appservers
  become: yes
  tasks:
    - name: Copy index.html to /opt/data/html on remote servers
      copy:
        source: /tmp/index.html
        dest: /opt/data/html
        owner: root
        group: root
        mode: '0644'

Day 5: **Create Files on App Servers using Ansible**
The Nautilus DevOps team is testing various Ansible modules on servers in Stratos DC. They're currently focusing on file creation on remote hosts using Ansible. Here are the details:

a. Create an inventory file ~/playbook/inventory on jump host and include all app servers.

b. Create a playbook ~/playbook/playbook.yml to create a blank file /opt/appdata.txt on all app servers.

c. Set the permissions of the /opt/appdata.txt file to 0655.

d. Ensure the user/group owner of the /opt/appdata.txt file is tony on app server 1, steve on app server 2 and banner on app server 3.

Note: Validation will execute the playbook using the command ansible-playbook -i inventory playbook.yml, so ensure the playbook functions correctly without any additional arguments.
Ans:
# Step 1: Create the Inventory File

vi ~/playbook/inventory
[appservers]
stapp01 ansible_host=172.16.238.10 ansible_user=tony ansible_ssh_pass=Ir0nM@n
stapp02 ansible_host=172.16.238.11 ansible_user=steve ansible_ssh_pass=Am3ric@
stapp03 ansible_host=172.16.238.12 ansible_user=banner ansible_ssh_pass=BigGr33n

# Step 2: Create the Playbook
vi ~/playbook/playbook.yml

- name: Create and manage appdata.txt on all app servers
  hosts: appservers
  become: true   # Use sudo to execute tasks as root

  tasks:
    - name: Create blank file /opt/appdata.txt
      ansible.builtin.file:
        path: /opt/appdata.txt
        state: touch  # This creates an empty file if it doesn't exist

    - name: Set permissions to 0655 for /opt/appdata.txt
      ansible.builtin.file:
        path: /opt/appdata.txt
        mode: '0655'

    - name: Set owner and group for /opt/appdata.txt on app server 1
      ansible.builtin.file:
        path: /opt/appdata.txt
        owner: tony
        group: tony
      when: inventory_hostname == 'stapp01'

    - name: Set owner and group for /opt/appdata.txt on app server 2
      ansible.builtin.file:
        path: /opt/appdata.txt
        owner: steve
        group: steve
      when: inventory_hostname == 'stapp02'

    - name: Set owner and group for /opt/appdata.txt on app server 3
      ansible.builtin.file:
        path: /opt/appdata.txt
        owner: banner
        group: banner
      when: inventory_hostname == 'stapp03'

# Step 3: Running the Playbook
ansible-playbook -i ~/playbook/inventory ~/playbook/playbook.yml

**Ansible Test:**
# Q1:
The Nautilus DevOps team will be managing multiple hosts using Ansible. Each host possesses unique properties such as hostnames, login credentials, etc. Therefore, a custom inventory file is necessary to manage these hosts efficiently. The team has delineated the following requirements to address this situation.


Ensure that the default inventory path is appropriately modified to point to /home/thor/ansible-t5q6/inventory-t5q6 in the Ansible configuration file located at /home/thor/ansible-t5q6/ansible-t5q6.cfg. Please refrain from creating a new configuration file.

Note: This is a sample Ansible configuration. If you intend to test an Ansible playbook using this configuration, you may need to explicitly set the ANSIBLE_CONFIG variable

Ans:
vi /home/thor/ansible-t5q6/ansible-t5q6.cfg
[defaults]
inventory = /home/thor/ansible-t5q6/inventory-t5q6
remote_user = deploy

# Q2:
Ansible utilizes SSH connections to communicate with remote hosts. The Nautilus DevOps team intends to employ a unified Ansible manager for overseeing several remote hosts. To streamline operations, they seek to use a common remote user to connect with all remote hosts.

Update the Ansible configuration file located at /home/thor/ansible-t5q5/ansible-t5q5.cfg on the jump host to set a default remote user as deploy. Please refrain from creating a new configuration file.

Note: This is a sample Ansible configuration. If you intend to test an Ansible playbook using this configuration, you may need to explicitly set the ANSIBLE_CONFIG variable.

Ans:
vi /home/thor/ansible-t5q6/ansible-t5q6.cfg
[defaults]
remote_user = deploy

# Q3:
a. on jump host create a playbook /home/thor/ansible/playbook-t2q5.yml to copy /usr/src/sysops-t2q5/story-t2q5.txt file from App Server 2 at location /opt/sysops-t2q5 on App Server 2.

b. An inventory is already placed under /home/thor/ansible/inventory-t2q5.

Note: Validation will try to run the playbook using command ansible-playbook -i inventory-t2q5 playbook-t2q5.yml so please make sure the playbook works this way without passing any extra arguments.
Ans:
#Playbook
cat  /home/thor/ansible/playbook-t2q5.yml

- name: Copy story-t2q5.txt on App Server 2
  hosts: stapp02
  become: true
  tasks:
    - name: Ensure destination directory exists
      file:
        path: /opt/sysops-t2q5
        state: directory
        mode: '0755'

    - name: Copy story-t2q5.txt to /opt/sysops-t2q5
      copy:
        src: /usr/src/sysops-t2q5/story-t2q5.txt
        dest: /opt/sysops-t2q5/story-t2q5.txt
        remote_src: true
        mode: '0644'

# Q4:
There is data on jump host that needs to be copied on all application servers in Stratos DC. Nautilus DevOps team want to perform this task using Ansible. Perform the task as per details mentioned below:
a. On jump host we already have inventory file /home/thor/ansible/inventory-t2q1.

b. On jump host create a playbook /home/thor/ansible/playbook-t2q1.yml to copy /usr/src/sysops-t2q1/index-t2q1.html file to all application servers at location /opt/sysops-t2q1.

Note: Validation will try to run the playbook using command ansible-playbook -i inventory-t2q1 playbook-t2q1.yml so please make sure the playbook works this way without passing any extra arguments.
Ans:

- name: Copy index-t2q1.html to all application servers
  hosts: all
  become: true
  tasks:
    - name: Ensure destination directory exists
      file:
        path: /opt/sysops-t2q1
        state: directory
        mode: '0755'

    - name: Copy index-t2q1.html to /opt/sysops-t2q1
      copy:
        src: /usr/src/sysops-t2q1/index-t2q1.html
        dest: /opt/sysops-t2q1/index-t2q1.html
        mode: '0644'

# Q5:
The Nautilus DevOps team is working to create some data on different app servers in using Ansible. They want to create some files/directories and have some specific requirements related to this task. Find below more details about the same:

a. Utilise the inventory file /home/thor/playbook/inventory-t4q3, present on the jump host.

b. Create a playbook named /home/thor/playbook/playbook-t4q3.yml to create a directory named /opt/backup-t4q3 on all App Servers.

Note: Validation will attempt to execute the playbook using the command ansible-playbook -i inventory-t4q3 playbook-t4q3.yml. Please ensure the playbook functions correctly with this command alone, without requiring any additional arguments.

Ans:

- name: Create /opt/backup-t4q3 directory on all app servers
  hosts: all
  become: true
  tasks:
    - name: Create /opt/backup-t4q3 directory
      file:
        path: /opt/backup-t4q3
        state: directory
        mode: '0755'

# Q6:
The Nautilus DevOps team is working to create some data on different app servers in using Ansible. They have some specific requirements related to this task. Find below more details about the same:

a. You can utilise the inventory file /home/thor/playbook/inventory-t4q2, present on the jump host.

b. Create a playbook named /home/thor/playbook/playbook-t4q2.yml to update the permissions of file /opt/file-t4q2.txt to 0444 on all app servers.

Note: Validation will attempt to execute the playbook using the command ansible-playbook -i inventory-t4q2 playbook-t4q2.yml. Please ensure the playbook functions correctly with this command alone, without requiring any additional arguments.

Ans:

- name: Update file permissions on all app servers
  hosts: all
  become: true
  tasks:
    - name: Set permissions of /opt/file-t4q2.txt to 0444
      file:
        path: /opt/file-t4q2.txt
        mode: '0444'
        state: file

# Q7:
The Nautilus Application development team wanted to update some Ansible inventory files which are present on the jump host. They shared some pre-requisites with the DevOps team, the updates should be done as per details mentioned below.

There is a sample inventory file called inventory-t3q5 under /home/thor/playbook directory. It has 3 servers listed, add another server called server4.company.com in this file.
Existing:
cat inventory-t3q5 
# Sample Inventory File

server1.company.com
server2.company.com
server3.company.com
Ans:
# Add the new host
server4.company.com
You can verify by running:: cat /home/thor/playbook/inventory-t3q5

# Q8:
The Nautilus DevOps team intends to test multiple Ansible playbooks across various app servers in the Stratos DC. Before proceeding, certain prerequisites must be addressed. Specifically, the team requires the establishment of a password-less SSH connection between the Ansible controller and the managed nodes. An assigned ticket outlines the task; please carry out the following details:

a. The Jump host serves as our Ansible controller, and the Ansible playbooks will be executed through the thor user from the jump host.

b. An inventory file, /home/thor/playbook/inventory-t3q2, is available on the jump host. Utilize this inventory file to perform an Ansible ping from the jump host to App Server 3 and ensure the successful execution of the ping command.

### ✅ **Goal:**

Set up **password-less SSH (key-based authentication)** from the **jump host (Ansible controller)** as user `thor` to **App Server 3**, and then **verify connectivity** using the Ansible `ping` module with the given inventory.

### 🔹 1. Check how App Server 3 is defined in the inventory

cat /home/thor/playbook/inventory-t3q2

Look for something like:

[appservers]
stapp03 ansible_host=172.16.238.12 ansible_user=rob ansible_ssh_pass=SomePassword
# update into
stapp03 ansible_host=172.16.238.12 ansible_user=banner

Take note of the host name (e.g. `stapp03`) and remote user (`banner`).

### 🔹 2. Generate an SSH key (if not already generated)
As `thor` on the jump host:

ssh-keygen -t rsa -b 2048

Just press `Enter` at all prompts to use default location (`~/.ssh/id_rsa`) and no passphrase.
### 🔹 3. Copy the SSH key to App Server 3

ssh-copy-id banner@172.16.238.12

You'll be prompted for the password (e.g. `SomePassword`) **once**, and after that, key-based auth will work.

### 🔹 4. Test password-less SSH

ssh banner@172.16.238.12

You should be logged in **without a password prompt**.

Exit the session:
exit
### 🔹 5. Run Ansible `ping` to App Server 3

Now test the connection using the Ansible inventory:

ansible -i /home/thor/playbook/inventory-t3q2 stapp03 -m ping

### ✅ Expected Output:
stapp03 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}

# Q9:
We plan to utilize various Ansible modules moving forward. To enhance our familiarity, the team intends to practice commonly used modules by creating playbooks for specific tasks.

Create a playbook named /home/thor/ansible/playbook-t1q4.yml on the jump host. Configure the playbook to generate a file named /tmp/file.txt on the jump host itself. Utilize the copy module and ensure the file contains the content: Welcome to the KKE Tests!

Ans:

- name: Create /tmp/file.txt on the jump host using copy module
  hosts: localhost
  become: true
  tasks:
    - name: Create file with specific content
      copy:
        dest: /tmp/file.txt
        content: "Welcome to the KKE Tests!"
        mode: '0644'

# Q10:
One of the Nautilus DevOps team members initiated work on testing an Ansible playbook on the jump host. However, the completion stalled after creating the inventory due to higher-priority tasks. We need assistance in resuming this task from where it was left off. Below are the specific details regarding the task at hand.

a. The inventory file located at /home/thor/ansible/inventory-t1q1 appears to have encountered some issues. It requires correction to execute the playbook on App Server 3 within the Stratos DC.

b. Generate a playbook named /home/thor/ansible/playbook-t1q1.yml and add a task to create an empty file named /tmp/file-t1q1.txt on App Server 3.

Note: Ensure the playbook functions seamlessly using the command ansible-playbook -i inventory-t1q1 playbook-t1q1.yml for validation purposes, avoiding any additional arguments during execution.

## 🔧 Step 1: Fix the Inventory File

First, check the contents:

cat /home/thor/ansible/inventory-t1q1

### 🛠 Fix common issues:

1. If App Server 3 isn't listed or has a wrong IP or username
2. Add `ansible_user` and (if password-based login is used) `ansible_ssh_pass`

✅ **Correct example:**

[appserver3]
stapp03 ansible_host=172.16.238.12 ansible_user=banner

## 📝 Step 2: Create the Playbook
Create the playbook:

nano /home/thor/ansible/playbook-t1q1.yml

### ✅ Paste the following:

- name: Create file /tmp/file-t1q1.txt on App Server 3
  hosts: stapp03
  become: true
  tasks:
    - name: Create empty file
      file:
        path: /tmp/file-t1q1.txt
        state: touch
        mode: '0644'
## 🚀 Step 3: Run the Playbook
cd /home/thor/ansible
ansible-playbook -i inventory-t1q1 playbook-t1q1.yml

Level 2:
Day1: 
The Nautilus DevOps team is planning to test several Ansible playbooks on different app servers in Stratos DC. Before that, some pre-requisites must be met. Essentially, the team needs to set up a password-less SSH connection between Ansible controller and Ansible managed nodes. One of the tickets is assigned to you; please complete the task as per details mentioned below:


a. Jump host is our Ansible controller, and we are going to run Ansible playbooks through thor user from jump host.


b. There is an inventory file /home/thor/ansible/inventory on jump host. Using that inventory file test Ansible ping from jump host to App Server 2, make sure ping works.

Ans:
To complete this task and verify password-less SSH connectivity from the Ansible controller (Jump Host) to App Server 2 using the `thor` user, follow these steps:

### 🔐 Step 1: Set Up SSH Key-Based Authentication

1. **Switch to `thor` user on the Jump Host:**
   
   sudo su - thor   

2. **Generate SSH key pair (if not already created):**
   
   ssh-keygen -t rsa
   
   - Press Enter to accept default location (`/home/thor/.ssh/id_rsa`)
   - Leave passphrase empty for password-less access

3. **Copy the public key to App Server 2:**
   
   ssh-copy-id <app_server_2_user>@<app_server_2_ip>
   
   Replace `<app_server_2_user>` and `<app_server_2_ip>` with the actual username and IP address of App Server 2.

### 📂 Step 2: Verify Inventory File

Ensure `/home/thor/ansible/inventory` contains the correct entry for App Server 2. Example:

[appservers]
appserver2 ansible_host=<app_server_2_ip> ansible_user=<app_server_2_user>

### 📡 Step 3: Test Ansible Ping

Run the ping module using the inventory file:

ansible -i /home/thor/ansible/inventory stapp02 -m ping

✅ If everything is set up correctly, you should see:
json
appserver2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}

Day2:
The Nautilus Application development team wanted to test some applications on app servers in Stratos Datacenter. They shared some pre-requisites with the DevOps team, and packages need to be installed on app servers. Since we are already using Ansible for automating such tasks, please perform this task using Ansible as per details mentioned below:


Create an inventory file /home/thor/playbook/inventory on jump host and add all app servers in it.

Create an Ansible playbook /home/thor/playbook/playbook.yml to install httpd package on all  app servers using Ansible yum module.

Make sure user thor should be able to run the playbook on jump host.

Note: Validation will try to run playbook using command ansible-playbook -i inventory playbook.yml so please make sure playbook works this way, without passing any extra arguments.

Ans:

### 📁 Step 1: Create the Inventory File

1. **Switch to `thor` user (if not already):**
   
   sudo su - thor
   
2. **Create the inventory file:**
   
   mkdir -p /home/thor/playbook
   vi /home/thor/playbook/inventory
 
3. **Add all app servers to the inventory:**
   Example (replace with actual hostnames or IPs):
[appservers]
stapp01 ansible_host=172.16.238.10 ansible_user=tony ansible_ssh_pass=Ir0nM@n
stapp02 ansible_host=172.16.238.11 ansible_user=steve ansible_ssh_pass=Am3ric@
stapp03 ansible_host=172.16.238.12 ansible_user=banner ansible_ssh_pass=BigGr33n

### 📜 Step 2: Create the Ansible Playbook

1. **Create the playbook file:**
   
   nano /home/thor/playbook/playbook.yml
   

2. **Add the following content:**
   yaml
   - name: Install httpd on all app servers
     hosts: appservers
     become: yes
     tasks:
       - name: Install httpd package
         yum:
           name: httpd
           state: present
   
### ✅ Step 3: Run and Validate

Make sure the playbook runs with the exact command:

cd /home/thor/playbook
ansible-playbook -i inventory playbook.yml

Day 3:
The Nautilus DevOps team has some data on each app server in Stratos DC that they want to copy to a different location. However, they want to create an archive of the data first, then they want to copy the same to a different location on the respective app server. Additionally, there are some specific requirements for each server. Perform the task using Ansible playbook as per requirements mentioned below:


Create a playbook named playbook.yml under /home/thor/ansible directory on jump host, an inventory file is already placed under /home/thor/ansible/ directory on Jump Server itself.


Create an archive ecommerce.tar.gz (make sure archive format is tar.gz) of /usr/src/dba/ directory ( present on each app server ) and copy it to /opt/dba/ directory on all app servers. The user and group owner of archive ecommerce.tar.gz should be tony for App Server 1, steve for App Server 2 and banner for App Server 3.

Note: Validation will try to run playbook using command ansible-playbook -i inventory playbook.yml so please make sure playbook works this way, without passing any extra arguments.
Ans:
Here's how you can create the required **Ansible playbook** to archive and copy the data with specific ownership per app server.

### ✅ File: `/home/thor/ansible/playbook.yml`

- name: Archive and copy dba data on app servers
  hosts: all
  become: yes
  tasks:

    - name: Create archive of /usr/src/dba directory
      archive:
        path: /usr/src/dba
        dest: /opt/dba/ecommerce.tar.gz
        format: gz
      notify: Set ownership

  handlers:
    - name: Set ownership
      ansible.builtin.file:
        path: /opt/dba/ecommerce.tar.gz
        owner: "{{ ansible_user }}"
        group: "{{ ansible_user }}"


### ✅ Inventory file: `/home/thor/ansible/inventory`

Make sure your inventory defines each app server with a variable for ownership:
[appservers]
stapp01 ansible_host=172.16.238.10 ansible_user=tony ansible_ssh_pass=Ir0nM@n
stapp02 ansible_host=172.16.238.11 ansible_user=steve ansible_ssh_pass=Am3ric@
stapp03 ansible_host=172.16.238.12 ansible_user=banner ansible_ssh_pass=BigGr33n

### 🧪 Validation Command

Run the playbook using:

ansible-playbook -i /home/thor/ansible/inventory /home/thor/ansible/playbook.yml

This setup ensures:
- Archive is created in `.tar.gz` format.
- Archive is placed in `/opt/dba/`.
- Ownership is set per server using variables from inventory.

Day 4:
One of the DevOps team members has created a zip archive on jump host in Stratos DC that needs to be extracted and copied over to all app servers in Stratos DC itself. Because this is a routine task, the Nautilus DevOps team has suggested automating it. We can use Ansible since we have been using it for other automation tasks. Below you can find more details about the task:

We have an inventory file under /home/thor/ansible directory on jump host, which should have all the app servers added already.

There is a zip archive /usr/src/dba/xfusion.zip on jump host.

Create a playbook.yml under /home/thor/ansible/ directory on jump host itself to perform the below given tasks.

Unzip /usr/src/dba/xfusion.zip archive in /opt/dba/ location on all app servers.

Make sure the extracted data must has the respective sudo user as their user and group owner, i.e tony for app server 1, steve for app server 2, banner for app server 3.

The extracted data permissions must be 0655.

Note: Validation will try to run the playbook using command ansible-playbook -i inventory playbook.yml so please make sure playbook works this way, without passing any extra arguments.

Ans:
# Create a playbook named playbook.yml under /home/thor/ansible/ with the following content:
---
- name: Unzip and distribute xfusion.zip to app servers
  hosts: all
  become: yes
  vars:
    unzip_dest: /opt/dba
    file_mode: '0655'
  tasks:

    - name: Copy zip file from jump host to app server
      copy:
        src: /usr/src/dba/xfusion.zip
        dest: /tmp/xfusion.zip
        mode: '0644'

    - name: Ensure destination directory exists
      file:
        path: "{{ unzip_dest }}"
        state: directory
        mode: '0755'

    - name: Unzip archive to destination
      unarchive:
        src: /tmp/xfusion.zip
        dest: "{{ unzip_dest }}"
        remote_src: yes

    - name: Set ownership and permissions on extracted files
      file:
        path: "{{ unzip_dest }}"
        owner: "{{ ansible_user }}"
        group: "{{ ansible_user }}"
        mode: "{{ file_mode }}"
        recurse: yes
# Validate th eplaybook 
cd /home/thor/ansible/
ansible-playbook -i inventory playbook.yml

Day 5:
The Nautilus DevOps team wants to install and set up a simple httpd web server on all app servers in Stratos DC. Additionally, they want to deploy a sample web page for now using Ansible only. Therefore, write the required playbook to complete this task. Find more details about the task below.


We already have an inventory file under /home/thor/ansible directory on jump host. Create a playbook.yml under /home/thor/ansible directory on jump host itself.

Using the playbook, install httpd web server on all app servers. Additionally, make sure its service should up and running.

Using blockinfile Ansible module add some content in /var/www/html/index.html file. Below is the content:

Welcome to XfusionCorp!

This is  Nautilus sample file, created using Ansible!

Please do not modify this file manually!

The /var/www/html/index.html file's user and group owner should be apache on all app servers.

The /var/www/html/index.html file's permissions should be 0777 on all app servers.

Note:

i. Validation will try to run the playbook using command ansible-playbook -i inventory playbook.yml so please make sure the playbook works this way without passing any extra arguments.

ii. Do not use any custom or empty marker for blockinfile module.
Ans:
Here is the Ansible playbook that meets **all the specified requirements**. This playbook:

* Installs the `httpd` web server
* Ensures the service is up and running
* Adds a block of content to `/var/www/html/index.html` using `blockinfile` (without custom markers)
* Sets file ownership to `apache:apache`
* Sets file permissions to `0777`

---

### ✅ Final Playbook: `/home/thor/ansible/playbook.yml`

---
- name: Setup httpd and deploy sample web page
  hosts: all
  become: true

  tasks:

    - name: Install httpd package
      package:
        name: httpd
        state: present

    - name: Ensure httpd service is running and enabled
      service:
        name: httpd
        state: started
        enabled: true

    - name: Ensure /var/www/html/index.html file exists
      file:
        path: /var/www/html/index.html
        state: touch
        owner: apache
        group: apache
        mode: '0777'

    - name: Add content to /var/www/html/index.html using blockinfile
      blockinfile:
        path: /var/www/html/index.html
        block: |
          Welcome to XfusionCorp!
          
          This is  Nautilus sample file, created using Ansible!
          
          Please do not modify this file manually!

    - name: Set ownership of index.html to apache
      file:
        path: /var/www/html/index.html
        owner: apache
        group: apache

    - name: Set permissions of index.html to 0777
      file:
        path: /var/www/html/index.html
        mode: '0777'

---

### 📌 Additional Notes:

* **Inventory File**: Already located at `/home/thor/ansible/inventory`
* **Run Command**: Validation will run the playbook using:

ansible-playbook -i inventory playbook.yml

So ensure both `inventory` and `playbook.yml` are in `/home/thor/ansible/`

Verify the ownership : ls -l /var/www/html/index.html

**Level 3:**

# Q1: Creating Soft Links Using Ansible
The Nautilus DevOps team is practicing some of the Ansible modules and creating and testing different Ansible playbooks to accomplish tasks. Recently they started testing an Ansible file module to create soft links on all app servers. Below you can find more details about it.

Write a playbook.yml under /home/thor/ansible directory on jump host, an inventory file is already present under /home/thor/ansible directory on jump host itself. Using this playbook accomplish below given tasks:

Create an empty file /opt/dba/blog.txt on app server 1; its user owner and group owner should be tony. Create a symbolic link of source path /opt/dba to destination /var/www/html.

Create an empty file /opt/dba/story.txt on app server 2; its user owner and group owner should be steve. Create a symbolic link of source path /opt/dba to destination /var/www/html.

Create an empty file /opt/dba/media.txt on app server 3; its user owner and group owner should be banner. Create a symbolic link of source path /opt/dba to destination /var/www/html.

Note: Validation will try to run the playbook using command ansible-playbook -i inventory playbook.yml so please make sure playbook works this way without passing any extra arguments.
Ans:
---
- name: Create files and symbolic links on app servers
  hosts: all
  become: yes
  tasks:

    - name: Create blog.txt on app server 1
      file:
        path: /opt/dba/blog.txt
        state: touch
        owner: tony
        group: tony
      when: inventory_hostname == "stapp01"

    - name: Create story.txt on app server 2
      file:
        path: /opt/dba/story.txt
        state: touch
        owner: steve
        group: steve
      when: inventory_hostname == "stapp02"

    - name: Create media.txt on app server 3
      file:
        path: /opt/dba/media.txt
        state: touch
        owner: banner
        group: banner
      when: inventory_hostname == "stapp03"

    - name: Create symbolic link /var/www/html to /opt/dba
      file:
        src: /opt/dba
        dest: /var/www/html
        state: link
      when: inventory_hostname in ["stapp01", "stapp02", "stapp03"]

# Q2 Managing ACLs Using Ansible
There are some files that need to be created on all app servers in Stratos DC. The Nautilus DevOps team want these files to be owned by user root only however, they also want that the app specific user to have a set of permissions on these files. All tasks must be done using Ansible only, so they need to create a playbook. Below you can find more information about the task.

Create a playbook named playbook.yml under /home/thor/ansible directory on jump host, an inventory file is already present under /home/thor/ansible directory on Jump Server itself.

Create an empty file blog.txt under /opt/sysops/ directory on app server 1. Set some acl properties for this file. Using acl provide read '(r)' permissions to group tony (i.e entity is tony and etype is group).

Create an empty file story.txt under /opt/sysops/ directory on app server 2. Set some acl properties for this file. Using acl provide read + write '(rw)' permissions to user steve (i.e entity is steve and etype is user).

Create an empty file media.txt under /opt/sysops/ on app server 3. Set some acl properties for this file. Using acl provide read + write '(rw)' permissions to group banner (i.e entity is banner and etype is group).

Note: Validation will try to run the playbook using command ansible-playbook -i inventory playbook.yml so please make sure the playbook works this way, without passing any extra arguments.

Ans:
---
- name: Create files and set ACLs on App Servers
  hosts: all
  become: yes
  tasks:

    - name: Ensure /opt/sysops directory exists
      file:
        path: /opt/sysops
        state: directory
        owner: root
        group: root
        mode: '0755'

    - name: Create blog.txt and set ACL for group tony (App Server 1)
      when: inventory_hostname == 'stapp01'
      block:
        - name: Create empty blog.txt
          file:
            path: /opt/sysops/blog.txt
            state: touch
            owner: root
            group: root
            mode: '0644'

        - name: Set ACL for group tony (read-only)
          acl:
            path: /opt/sysops/blog.txt
            entity: tony
            etype: group
            permissions: r
            state: present

    - name: Create story.txt and set ACL for user steve (App Server 2)
      when: inventory_hostname == 'stapp02'
      block:
        - name: Create empty story.txt
          file:
            path: /opt/sysops/story.txt
            state: touch
            owner: root
            group: root
            mode: '0644'

        - name: Set ACL for user steve (read/write)
          acl:
            path: /opt/sysops/story.txt
            entity: steve
            etype: user
            permissions: rw
            state: present

    - name: Create media.txt and set ACL for group banner (App Server 3)
      when: inventory_hostname == 'stapp03'
      block:
        - name: Create empty media.txt
          file:
            path: /opt/sysops/media.txt
            state: touch
            owner: root
            group: root
            mode: '0644'

        - name: Set ACL for group banner (read/write)
          acl:
            path: /opt/sysops/media.txt
            entity: banner
            etype: group
            permissions: rw
            state: present

# Q3 Ansible Manage Services
Developers are looking for dependencies to be installed and run on Nautilus app servers in Stratos DC. They have shared some requirements with the DevOps team. Because we are now managing packages installation and services management using Ansible, some playbooks need to be created and tested. As per details mentioned below please complete the task:

a. On jump host create an Ansible playbook /home/thor/ansible/playbook.yml and configure it to install vsftpd on all app servers.

b. After installation make sure to start and enable vsftpd service on all app servers.

c. The inventory /home/thor/ansible/inventory is already there on jump host.

d. Make sure user thor should be able to run the playbook on jump host.

Note: Validation will try to run playbook using command ansible-playbook -i inventory playbook.yml so please make sure playbook works this way, without passing any extra arguments.
Ans:
---
- name: Install and configure vsftpd on app servers
  hosts: all
  become: true  # This will ensure privilege escalation (sudo) is used to install packages and manage services
  tasks:

    - name: Install vsftpd package
      package:
        name: vsftpd
        state: present

    - name: Ensure vsftpd service is started
      service:
        name: vsftpd
        state: started

    - name: Ensure vsftpd service is enabled
      service:
        name: vsftpd
        enabled: yes

# Q4 Ansible Lineinfile Module
The Nautilus DevOps team want to install and set up a simple httpd web server on all app servers in Stratos DC. They also want to deploy a sample web page using Ansible. Therefore, write the required playbook to complete this task as per details mentioned below.


We already have an inventory file under /home/thor/ansible directory on jump host. Write a playbook playbook.yml under /home/thor/ansible directory on jump host itself. Using the playbook perform below given tasks:

Install httpd web server on all app servers, and make sure its service is up and running.

Create a file /var/www/html/index.html with content:

This is a Nautilus sample file, created using Ansible!

Using lineinfile Ansible module add some more content in /var/www/html/index.html file. Below is the content:
Welcome to Nautilus Group!

Also make sure this new line is added at the top of the file.

The /var/www/html/index.html file's user and group owner should be apache on all app servers.

The /var/www/html/index.html file's permissions should be 0755 on all app servers.

Note: Validation will try to run the playbook using command ansible-playbook -i inventory playbook.yml so please make sure the playbook works this way without passing any extra arguments.

Ans:
---
- name: Install and configure httpd on app servers
  hosts: all
  become: yes

  tasks:
    - name: Install httpd web server
      yum:
        name: httpd
        state: present

    - name: Ensure httpd service is started and enabled
      service:
        name: httpd
        state: started
        enabled: yes

    - name: Create /var/www/html/index.html with initial content
      copy:
        dest: /var/www/html/index.html
        content: |
          This is a Nautilus sample file, created using Ansible!
        owner: apache
        group: apache
        mode: '0755'

    - name: Add "Welcome to Nautilus Group!" at the top of index.html
      lineinfile:
        path: /var/www/html/index.html
        line: "Welcome to Nautilus Group!"
        insertafter: BOF
        owner: apache
        group: apache
        mode: '0755'

# Q5 Ansible Replace Module

**Level 4**
# Q1 Ansible Facts Gathering
# Q2 Ansible Create Users and Groups
# Q3 Managing Jinja2 Templates Using Ansible
# Q4 Ansible Setup Httpd and PHP
# Q5 Using Ansible Conditionals