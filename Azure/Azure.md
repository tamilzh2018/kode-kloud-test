## 🧩 **Azure Virtual Machines & Networking**

### **Q1: Create SSH Key Pair for Azure Virtual Machine**

> *Your company has a policy to allow only SSH key-based access to virtual machines. Generate a secure SSH key pair for Linux VM deployment in Azure using CLI. How would you securely store the private key and share access with team members?*
## Q21: For this task, create an SSH key pair with the following requirements:

The name of the SSH key pair should be xfusion-kp.

The key pair type must be rsa.
### **Q2: Create an Azure Virtual Machine**

> *Deploy a Linux-based Azure VM in the `East US` region with a Standard B2s size and a new resource group. Ensure it uses SSH for authentication and is placed in a custom virtual network. What are the minimal required configurations?*
## Q2
The Nautilus DevOps team is planning to migrate a portion of their infrastructure to the Azure cloud incrementally. As part of this migration, you are tasked with creating an Azure Virtual Machine (VM). The requirements are: 1) Use the existing resource group. 2) The VM name must be devops-vm, it should be in West US region. 3) Use the Ubuntu 22.04 LTS image for the VM. 4) The VM size must be Standard_B1s. 5) Attach a default Network Security Group (NSG) that allows inbound SSH (port 22). 6) Attach a 30 GB storage disk of type Standard HDD. 7) The rest of the configurations should remain as default. After completing these steps, make sure you can SSH into the virtual machine.

Ans:

## 🖥️ Step‑by‑Step in Azure Portal

1. **Log in to Azure Portal**
   - Go to [https://portal.azure.com](https://portal.azure.com).
   - Sign in with your Microsoft account.

2. **Navigate to Virtual Machines**
   - In the left menu, click **Virtual Machines**.
   - Select **+ Create → Azure Virtual Machine**.

3. **Basics Tab**
   - **Subscription**: Choose your subscription.
   - **Resource Group**: Select your existing resource group.
   - **Virtual Machine Name**: Enter `devops-vm`.
   - **Region**: Choose **West US**.
   - **Image**: Select **Ubuntu Server 22.04 LTS**.
   - **Size**: Pick **Standard_B1s**.

4. **Administrator Account**
   - Choose **SSH public key** authentication (recommended).
   - Enter a username (e.g., `azureuser`).
   - Upload your public SSH key or let Azure generate one.

5. **Disks Tab**
   - OS Disk type: Select **Standard HDD**.
   - OS Disk size: Set to **30 GB**.
   - Leave other options as default.

6. **Networking Tab**
   - Virtual Network: Use default or existing.
   - Subnet: Default.
   - Public IP: Enabled.
   - Network Security Group: Select **Basic** and allow **SSH (port 22)** inbound.

7. **Management, Monitoring, Advanced Tabs**
   - Leave defaults unless you need extra monitoring or backup.

8. **Review + Create**
   - Azure will validate your configuration.
   - Click **Create** to deploy the VM.

---

## 🔑 Connect via SSH

Once deployment finishes:
1. Go back to the **Virtual Machines** blade.
2. Select `devops-vm`.
3. Copy the **Public IP address**.
4. From your terminal:

```bash
ssh azureuser@<PUBLIC_IP>
```


### **Q3: Create a Virtual Network (VNet) in Azure**

> *You are setting up an isolated environment for a three-tier application. Create a virtual network with a /16 CIDR range and explain how you would subdivide it into subnets for web, app, and database tiers.*

The Nautilus DevOps team is in the process of migrating some of their workloads to Azure. One of the tasks involves creating a new Virtual Machine (VM) using the Azure CLI. The team does not have access to the Azure portal but can manage Azure resources via the azure-client host (the landing host for this lab).

1) Create a new Azure Virtual Machine named xfusion-vm using the Azure CLI.

2) Use the Ubuntu2204 image and set the VM size to Standard_B2s.

3) Make sure the admin username is set to azureuser and SSH keys are generated for secure access.

4) Use Standard_LRS storage account, disk size must be 30GB and ensure the VM xfusion-vm is in the running state after creation.

Ans:
# If you don’t know the resource group name:List all resource groups with their regions
az group list --query "[].{name:name, location:location}" -o table
output: Name                          Location
----------------------------  ----------
kml_rg_main-22d6db0709e14b45  westus


## ✅ **1. Create a Resource Group i fnot avail**

```bash
az group create \
  --name $RESOURCE_GROUP \
  --location $LOCATION
```

---

## ✅ **3. Create the VM**

This command automatically generates SSH keys and creates the VM with:

* **Ubuntu 22.04 (Ubuntu2204)**
* **Standard_B2s size**
* **Standard_LRS OS disk**
* **30GB OS disk size**

```bash
az vm create \
  --resource-group kml_rg_main-22d6db0709e14b45 \
  --name xfusion-vm \
  --image Ubuntu2204 \
  --size Standard_B2s \
  --admin-username azureuser \
  --generate-ssh-keys \
  --os-disk-size-gb 30 \
  --storage-sku Standard_LRS
```

---

## ✅ **4. Verify VM is running**

```bash
az vm get-instance-view \
  --resource-group kml_rg_main-22d6db0709e14b45 \
  --name xfusion-vm \
  --query "instanceView.statuses[?starts_with(code, 'PowerState')].displayStatus" \
  --output table
```


### **Q4: Create a Virtual Network (IPv4) in Azure**

> *A legacy system requires IPv4-only communication. Create a VNet that supports only IPv4 addressing and launch a VM in it. How do you ensure the VM can access external services securely?*
Create a Virtual Network (VNet) named xfusion-vnet in the East US region with any IPv4 CIDR block.
Create a Virtual Network (VNet) named datacenter-vnet in the East US region with 192.168.0.0/24 IPv4 CIDR.
### **Q5: Create a Virtual Network (IPv6) in Azure**

> *Your organization is migrating to IPv6 to future-proof its infrastructure. Create a dual-stack (IPv4 + IPv6) VNet. What address prefixes, subnets, and route configurations are required to enable IPv6 traffic?*
For this task, create a Virtual Network (VNet) named datacenter-vnet and one subnet named datacenter-subnet within the VNet in the East US region. Make sure the IPv4 address range is 10.0.0.0/16.
### **Q6: Create a Subnet in Azure Virtual Network**

> *Add a subnet named `web-subnet` (CIDR: 10.0.1.0/24) to an existing VNet. How do you ensure this subnet is later associated with a network security group and routing table?*

### **Q7: Create a Public IP Address for Azure VM**

> *Your customer wants a public-facing application. Allocate a static public IP address and assign it to a new or existing VM. Should you choose Basic or Standard SKU, and why?*
For this task, allocate a Public IP address, name it as nautilus-pip.
Go to Azure Portal → search Public IP addresses

Click Create

Fill out:

Name: nautilus-pip

SKU: Basic or Standard (your choice)

Assignment: Static or Dynamic

Region: Choose your region

Click Review + Create → Create
### **Q: Delete Azure Virtual Machine Using Console**
The Nautilus DevOps team is migrating a portion of their infrastructure to Azure. During the migration, they have created several virtual machines (VMs) in different regions. The team has identified one VM that is underutilized and has decided to change its size to optimize resource usage.

1) Change the VM size from Standard_B1s to Standard_B2s for the virtual machine named datacenter-vm.

2) Ensure the VM is in the running state after the size change is complete.

Ans:


## 🔧 Steps to Change VM Size in Azure Portal

1. **Sign in to Azure Portal**
   - Go to [portal.azure.com](https://portal.azure.com) and log in with your Azure credentials.

2. **Locate the Virtual Machine**
   - In the left-hand menu, select **Virtual Machines**.
   - Find and click on the VM named **datacenter-vm**.

3. **Stop the VM (if required)**
   - Some VM size changes require the VM to be stopped.
   - On the VM overview page, click **Stop** and wait until the status shows **Stopped (deallocated)**.

4. **Change the VM Size**
   - In the VM’s menu, under **Settings**, select **Size**.
   - Browse or search for **Standard_B2s**.
   - Click on **Standard_B2s** and then select **Resize**.

5. **Restart the VM**
   - Once resizing is complete, go back to the **Overview** page.
   - If the VM is not already running, click **Start**.
   - Confirm that the **Status** shows **Running**.

---

## ✅ Verification

- Check the **Overview** blade of **datacenter-vm**:
  - **Size** should now display **Standard_B2s**.
  - **Status** should display **Running**.

---

Would you like me to also outline the equivalent **Azure CLI commands** for automation, so the DevOps team can script this change instead of doing it manually in the portal?
### **Q8: Delete Azure Virtual Machine Using Console**

> *A developer VM is no longer in use. Delete the VM and optionally remove associated resources (NIC, disk, IP) from the Azure portal. What precautions should you take to avoid orphaned or shared resources being deleted?*

### **Q9: Delete Azure Virtual Machine Using CLI**

> *Write the CLI command to delete a VM in the `dev-rg` resource group without deleting its managed disk and public IP. Why might this approach be useful for backups or reattachments?*

### **Q10: Delete a Virtual Network (VNet) in Azure**

> *Attempt to delete a VNet, but the operation fails. Investigate the dependencies (e.g., subnets with NICs or gateways) and list the steps to safely remove all associated resources before deleting the VNet.*

## 🏷️ **Tagging, Access & Connectivity**

### **Q11: Add and Manage Tags for Azure Virtual Machines**

> *Your finance team needs to track costs by environment. Add `Environment=Production` and `Owner=DevOps` tags to existing VMs using both portal and CLI. How do tags impact billing and governance?*

Add the tag Environment=dev to the virtual machine named datacenter-vm.

### **Q12: SSH into an Azure Virtual Machine**

> *You deployed a Linux VM but can't SSH into it. Verify your key pair, NSG rules, and public IP configuration. How do you troubleshoot and securely access the VM?*
Task Details:
1) VM Details:

The VM is named xfusion-vm and is running in the West US region. The default SSH user is azureuser — use this user to connect to the VM.
You need to add the root user's SSH public key from the Azure client host to the authorized_keys file of the VM's root user.
The SSH public key of the root user on the Azure client host is located at /root/.ssh/id_rsa.pub.
2) Public Key Addition:

Copy the public key located at /root/.ssh/id_rsa.pub on the Azure client host to the authorized_keys file of the root user on xfusion-vm.
Ensure that the proper permissions for the .ssh folder and authorized_keys file are set on the VM.
3) Verification:

After adding the public key, make sure that you are able to SSH into the xfusion-vm VM as the root user from the Azure client host without needing a password.
Important Notes:
Ensure that the VM is up and running before attempting to SSH.
You may need to adjust the firewall or security group rules for the VM to allow SSH access.

Ans:
Here’s a clean, reliable walkthrough to get this done. I’ll give you the exact steps you’d run on both the Azure client host and the VM, plus the permission rules you must follow so SSH key‑based login works smoothly.

---

# ✅ Overview  
You want to:

- Connect to **xfusion-vm** as *azureuser*  
- Add the **root user’s public key** from the Azure client host  
- Place it into **/root/.ssh/authorized_keys** on the VM  
- Fix permissions  
- Verify passwordless SSH as **root**

Let’s go step by step.

---

# ✅ 1. Connect to the VM as *azureuser*

From the Azure client host:

```bash
ssh azureuser@<public-ip-of-xfusion-vm>
```

Make sure the VM is running and SSH (port 22) is allowed in its NSG/firewall.

---

# ✅ 2. Prepare the root account on the VM

Once logged in as *azureuser*:

 sudo mkdir -p /root/.ssh
 sudo chmod 700 /root/.ssh
 sudo vi /root/.ssh/authorized_keys
 paste key and remove anything existing # key available clint machine cat /root/.ssh/id_rsa.pub
 sudo chmod 600 /root/.ssh/authorized_keys


# ✅ 4. Ensure SSH allows root login with keys

On xfusion-vm, check:

```bash
sudo nano /etc/ssh/sshd_config
```

Ensure these lines exist:

```
PermitRootLogin yes
PubkeyAuthentication yes
```

Then restart SSH:

```bash
sudo systemctl restart sshd
```

---

# ✅ 5. Verification

From the Azure client host:

```bash
ssh root@<public-ip-of-xfusion-vm>
```

If everything is correct, you should log in **without a password**.

---

# ✅ 6. Security Group / Firewall Check

If SSH fails, verify:

- **[NSG allows inbound port 22](guide://action?prefill=Tell%20me%20more%20about%3A%20NSG%20allows%20inbound%20port%2022)**
- **[No deny rules override SSH](guide://action?prefill=Tell%20me%20more%20about%3A%20No%20deny%20rules%20override%20SSH)**
- **[VM firewall (ufw/firewalld) allows SSH](guide://action?prefill=Tell%20me%20more%20about%3A%20VM%20firewall%20(ufw%2Ffirewalld)%20allows%20SSH)**




## 💾 **Disk and Network Configuration**

### **Q13: Attach Managed Disk to Azure Virtual Machine**

> *Your VM needs additional storage for data logging. Create and attach a 128 GB managed disk. Format and mount it on a Linux instance. What performance tier would you choose for medium I/O workloads?*

An existing VM named devops-vm and a managed disk named devops-disk already exist in the East US region.

Attach the disk devops-disk to the VM devops-vm as a data disk.
Ensure the disk is attached to the VM devops-vm.
Make sure that the virtual machine initialization has been completed before submitting this task.

Ans: 

Go to the Azure portal to find the VM. Search for and select Virtual machines.

Select the VM you'd like to attach the disk to from the list.

In the Virtual machines page, under Settings, select Disks.

Attach a new disk
Follow these steps:

On the Disks pane, under Data disks, select Create and attach a new disk.

Enter a name for your managed disk. Review the default settings, and update the Storage type, Size (GiB), Encryption and Host caching as necessary.

Screenshot of review disk settings.

When you're done, select Save at the top of the page to create the managed disk and update the VM configuration.

Attach an existing disk
Follow these steps:

On the Disks pane, under Data disks, select Attach existing disks.

Select the drop-down menu for Disk name and select a disk from the list of available managed disks.

Select Save to attach the existing managed disk and update the VM configuration:



### **Q14: Attach Network Interface Card (NIC) to Azure Virtual Machine**

> *To improve network throughput, add a second NIC to your VM. What are the prerequisites, and how does this impact VM size and OS-level configuration?*


An existing VM named xfusion-vm and a network interface named xfusion-nic already exist in the West US region.

Attach the network interface xfusion-nic to the VM xfusion-vm.
Ensure the NIC's status is attached before submitting the task.
Make sure that the virtual machine initialization has been completed before submitting this task.

Ans: 


## 💻 Azure Portal Steps: Attach NIC to VM

### Step 1: Navigate to the Virtual Machine
1.  In the Azure portal search bar, type **"Virtual machines"** and select the service.
2.  Locate and select the virtual machine named **$\mathbf{xfusion-vm}$** in the **West US** region.
    * *Note: Ensure the VM's initialization is complete, as stated in the requirement.*

---

### Step 2: Access Networking Settings
1.  In the left-hand menu blade for the $\mathbf{xfusion-vm}$, under **Settings**, select **Networking**.

---

### Step 3: Attach the Network Interface
1.  On the Networking page, you will see a list of attached network interfaces (if any).
2.  At the top of the Networking page, click the **Attach network interface** button.
    * 
3.  A pane will open where you can select the network interface.
4.  From the dropdown menu, select the existing network interface named **$\mathbf{xfusion-nic}$**.
5.  Click **OK** or **Attach** (button text may vary) to confirm the attachment.

---

### Step 4: Verify the NIC Status
1.  After the attachment operation is complete, the $\mathbf{xfusion-vm}$ Networking page will refresh.
2.  Verify that the **$\mathbf{xfusion-nic}$** now appears in the list of network interfaces for the VM.
3.  The status of the NIC should show as **Attached** (or similar wording indicating it is successfully connected to the VM).

### **Q15: Attach Public IP to Azure Virtual Machine**

> *You created a VM without a public IP. Now you need to access it remotely. Create and associate a static public IP to the VM using both portal and CLI. What is the impact of Basic vs. Standard IP SKUs?*
An existing VM named nautilus-vm-pip and a public IP address named nautilus-pip already exist.

Attach the public IP nautilus-pip to the network interface of the VM nautilus-vm-pip.
Make sure the VM is properly assigned the public IP.


### **Q16: Change Azure Virtual Machine Size Using Console**

> *Your VM is underpowered for its workload. Resize it to a `Standard D2s v3` instance using the portal. What must you consider regarding downtime, available quotas, and regional availability?*

### **Q17: Create and Attach Managed Disks in Azure**

> *A VM requires two new data disks: one for logs, one for app data. Create two disks, attach them, and configure Linux to use LVM for redundancy. What are the IOPS limitations for the selected disk types?*
Create a managed disk with the following requirements:

Name of the disk should be nautilus-disk.

Disk type must be Standard_LRS.

Disk size must be 2 GiB.
Ans:
az disk create \
  --resource-group <your-resource-group> \
  --name nautilus-disk \
  --size-gb 2 \
  --sku Standard_LRS


## 🔐 **Security & Access Control**

### **Q18: Create and Configure Network Security Group (NSG) in Azure**

> *Create an NSG to allow inbound SSH and HTTP traffic but deny all other inbound access. Associate it with a subnet. How do you test and verify the NSG is working correctly?*
For this task, create a network security group (NSG) with the following requirements:

Name of the NSG should be xfusion-nsg.

Add an inbound security rule named Allow-HTTP for HTTP service on port 80, with the source CIDR range of 0.0.0.0/0.

Add another inbound security rule named Allow-SSH for SSH service on port 22, with the source CIDR range of 0.0.0.0/0.

Ans:
## 🌐 Steps in Azure Portal

### 1. Create the NSG
- Sign in to the [Azure Portal](https://portal.azure.com).
- In the left menu, select **All services** → search for **Network security groups**.
- Click **+ Create**.
- Fill in the details:
  - **Subscription**: choose your subscription.
  - **Resource group**: select an existing one or create a new one.
  - **Name**: `xfusion-nsg`.
  - **Region**: choose the same region as your resources (VMs, subnets).
- Click **Review + Create** → then **Create**.

---

### 2. Add Inbound Rule for HTTP
- Open the newly created NSG (`xfusion-nsg`).
- In the **Settings** section, select **Inbound security rules**.
- Click **+ Add**.
- Configure:
  - **Source**: IP Addresses.
  - **Source IP addresses/CIDR ranges**: `0.0.0.0/0`.
  - **Source port ranges**: `*`.
  - **Destination**: Any.
  - **Destination port ranges**: `80`.
  - **Protocol**: TCP.
  - **Action**: Allow.
  - **Priority**: e.g., `100` (lower numbers = higher priority).
  - **Name**: `Allow-HTTP`.
- Click **Add**.

---

### 3. Add Inbound Rule for SSH
- Still under **Inbound security rules**, click **+ Add** again.
- Configure:
  - **Source**: IP Addresses.
  - **Source IP addresses/CIDR ranges**: `0.0.0.0/0`.
  - **Source port ranges**: `*`.
  - **Destination**: Any.
  - **Destination port ranges**: `22`.
  - **Protocol**: TCP.
  - **Action**: Allow.
  - **Priority**: e.g., `110` (must be unique and higher than HTTP rule).
  - **Name**: `Allow-SSH`.
- Click **Add**.

---

### ✅ Verification
- You should now see two inbound rules under `xfusion-nsg`:
  - `Allow-HTTP` → TCP, Port 80, Source `0.0.0.0/0`.
  - `Allow-SSH` → TCP, Port 22, Source `0.0.0.0/0`.



## ☁️ **Azure Storage - Blob Containers**

### **Q19: Create a Private Azure Blob Storage Container**

> *Create a blob container in a storage account with private access. Upload a sample file and verify that it cannot be accessed without credentials. How would you grant time-limited access via a Shared Access Signature (SAS)?*
Create a new storage account named nautilusst31292 and a private Blob container named nautilus-blob-24518 within the storage account.


### Step 1: Create the Storage Account
1. Sign in to the [Azure Portal](https://portal.azure.com).
2. In the left-hand menu, click **Storage accounts**.
3. Select **+ Create**.
4. Fill in the details:
   - **Subscription**: Choose your subscription.
   - **Resource group**: Select an existing one or create a new one.
   - **Storage account name**: Enter `nautilusst31292` (must be globally unique, all lowercase).
   - **Region**: Pick the region closest to you.
   - **Performance**: Standard is fine unless you need Premium.
   - **Redundancy**: Choose your replication option (e.g., LRS, GRS).
5. Click **Review + Create**, then **Create**.

### Step 2: Create the Blob Container
1. Once the storage account is deployed, go to **Storage accounts** and select `nautilusst31292`.
2. In the left menu, under **Data storage**, click **Containers**.
3. Select **+ Container**.
4. Enter the name: `nautilus-blob-24518`.
5. Set **Public access level** to **Private (no anonymous access)**.
6. Click **Create**.

That’s it — you’ll now have a storage account named `nautilusst31292` and a private blob container named `nautilus-blob-24518`.  

### **Q20: Create a Public Azure Blob Storage Container**

> *You’re hosting public documents like product manuals. Create a container with anonymous read access. What are the security and compliance implications of this approach?*
Create a new storage account named xfusionst3123 and a public Blob container named xfusion-blob-4255 within the storage account. Make sure anonymous read access for containers and blobs is enabled.
Ans:


* **Storage Account:** `xfusionst3123`
* **Blob Container:** `xfusion-blob-4255`
* **With anonymous read access enabled**

---

# ⭐ **Azure Portal (GUI) Instructions**

## **Step 1 — Create the Storage Account**

1. Go to the Azure Portal:
   **[https://portal.azure.com](https://portal.azure.com)**

2. In the left menu, click **Storage accounts**.

3. Click **+ Create**.

4. **Basics tab:**

   * **Subscription:** Select your subscription
   * **Resource group:** Select or create one
   * **Storage account name:** `xfusionst3123`
   * **Region:** Choose your region
   * **Performance:** Standard
   * **Redundancy:** LRS (or your choice)

5. Click the **Advanced** tab.

6. Under **Security**, ensure:
   ✔ **Allow blob anonymous access** → **Enabled**

7. Click **Review + Create**, then **Create**.

---

## **Step 2 — Create the Blob Container**

1. After deployment completes, click **Go to resource**.

2. In the left sidebar, choose **Containers** under **Data storage**.

3. Click **+ Container**.

4. Enter:

   * **Name:** `xfusion-blob-4255`
   * **Public access level:**
     Select **Container (anonymous read access for containers and blobs)**

5. Click **Create**.



### **Q21: Backup and Delete Azure Storage Blob Container**

> *Before deleting a storage container, you must back it up. Copy all blobs to another container in a different storage account. Then delete the original container safely. What tools or automation could you use for backup?*
Below are **exact, runnable steps** you can execute from the **azure-client (landing host)** to complete both tasks using the **Azure CLI**.

The Nautilus DevOps team is currently engaged in a cleanup process, focusing on removing unnecessary data and services from their Azure environment. As part of the migration process, several resources were created for one-time use only, necessitating a cleanup effort to optimize their Azure environment.

A private blob container named datacenter-blob-13829 already exists in the East US region under storage account datacenterst7726.

1) Copy the contents of datacenter-blob-13829 blob container to the /opt directory on the azure-client host (the landing host once you load this lab).

2) Delete the blob container datacenter-blob-13829 from the storage account.

---

## Assumptions

* You are logged into Azure (`az login`)
* You have **permission** on storage account `devopsst1541`
* The container is **private**, so we’ll authenticate using the **storage account key**

---

## Step 0: Set variables (recommended)

```bash
STORAGE_ACCOUNT=devopsst1541
CONTAINER_NAME=devops-blob-28639
DESTINATION=/opt
```

---

## Step 1: Get the storage account key

```bash
ACCOUNT_KEY=$(az storage account keys list \
  --account-name $STORAGE_ACCOUNT \
  --query "[0].value" \
  -o tsv)
```

---

## Step 2: Copy the blob container contents to `/opt`

This downloads **all blobs** in the container to `/opt`, preserving directory structure.

```bash
az storage blob download-batch \
  --account-name nautilusst19982 \
  --account-key  \
  --source nautilus-blob-21868 \
  --destination /opt
```

✅ At this point, the contents of `devops-blob-28639` should be available under `/opt`.

---

## Step 3: Verify contents (optional but recommended)

```bash
ls -l /opt
```

---

## Step 4: Delete the blob container

Once you’ve confirmed the data is copied:

```bash
az storage container delete \
  --account-name nautilusst19982 \
  --account-key  \
  --name nautilus-blob-21868 

```

---

## Step 5: Confirm deletion (optional)

```bash
az storage container list \
  --account-name nautilusst19982 \
  --account-key  \
  -o table
```

---

### ✔ Outcome

* All blobs copied to `/opt` on the azure-client host
* Container `devops-blob-28639` **deleted** from storage account `devopsst1541`


### **Q22: Copy Data to an Azure Blob Storage Container**

> *You need to upload 10 GB of data from your on-premises machine to Azure Blob Storage. Use `azcopy` to perform the operation efficiently. How do you monitor progress and resume failed transfers?*
A Blob container named nautilus-blob-8616 already exists in the East US region under the storage account nautilusst5454. Copy the file /tmp/nautilus.txt to the Blob container nautilus-blob-8616.

### Steps in Azure Portal

1. **Open Azure Portal**

   * Go to: [https://portal.azure.com](https://portal.azure.com)
   * Sign in with your Azure account.

2. **Navigate to the Storage Account**

   * Search for **Storage accounts**.
   * Click on **nautilusst5454**.

3. **Open the Blob Container**

   * In the left menu, click **Containers** (under *Data storage*).
   * Select **nautilus-blob-8616**.

4. **Upload the File**

   * Click the **Upload** button at the top.
   * In the upload panel:

     * Click **Browse for files**
     * Select `/tmp/nautilus.txt` from your system
       *(download it locally first if it’s on a remote server)*.
   * Leave other settings as default.
   * Click **Upload**.

5. **Verify**

   * Ensure **nautilus.txt** appears in the container list.

### Important Note

If `/tmp/nautilus.txt` is on a **Linux VM or server**, you must first download it to your local machine before uploading via the portal GUI.


### **Q23: Convert Public Azure Blob Container to Private**

> *You mistakenly created a container with public access. Update it to private without deleting or re-uploading the contents. What changes in access behavior occur post-conversion?*
Two blob containers named datacenter-container-31524 and datacenter-priv-14874 are available in the East US region within the storage account datacenterst29442. The datacenter-container-31524 is currently public, and datacenter-priv-14874 is private.

1) Convert the blob container datacenter-container-31524 from public to private while leaving datacenter-priv-14874 unchanged.

2) Make sure the access level for datacenter-container-31524 is set to private with no public access.

Ans:
Below are **clear, correct ways to convert `datacenter-container-31524` from public to private** while leaving `datacenter-priv-14874` unchanged.
This fully satisfies both requirements.

---

## ✅ Option 1: Azure Portal (GUI)

1. Sign in to the **Azure Portal**
2. Go to **Storage accounts**
3. Open **`datacenterst29442`**
4. Select **Containers** under *Data storage*
5. Click **`datacenter-container-31524`**
6. Select **Change access level**
7. Set **Public access level** to:

   * **Private (no anonymous access)**
8. Click **OK / Save**

🔒 Result:

* `datacenter-container-31524` → **Private**
* `datacenter-priv-14874` → **Unchanged (already private)**

---

## ✅ Option 2: Azure CLI (Fast & Precise)

Run the following command:

```bash
az storage container set-permission \
  --account-name datacenterst29442 \
  --name datacenter-container-31524 \
  --public-access off
```

✔ This explicitly removes all public access.

> No command is run against `datacenter-priv-14874`, so it remains private.

---

## ✅ Option 3: Azure PowerShell

```powershell
Set-AzStorageContainerAcl `
  -Name "datacenter-container-31524" `
  -Context (Get-AzStorageAccount -ResourceGroupName <RG_NAME> -Name datacenterst29442).Context `
  -Permission Off
```

---

## 🔍 Final State Verification

After the change:

* **Access level:** Private (no anonymous access)
* **Public blob/container access:** Disabled
* **Only authorized users via Azure AD, SAS, or account keys can access data**


## 📊 **Azure SQL**

### **Q24: Create Azure SQL Database**

> *Deploy an Azure SQL Database in the `Basic` tier within a new SQL Server. Configure a firewall rule to allow access from your current IP only. How do you connect from Azure Data Studio or SQL Server Management Studio?*
The Nautilus DevOps team is strategizing the migration of a portion of their infrastructure to Azure. Recognizing the scale of this undertaking, they have opted to approach the migration in incremental steps rather than as a single massive transition. Recently, they started working on creating and configuring some database instances on Azure.

For this task, create one publicly accessible Azure SQL Database instance along with the following details:

1) The name of the Azure SQL Database must be datacenter-sqldb.

2) The server name must be datacenter-server-31660.

3) The compute + storage configuration should be Basic (For less demanding workloads).

4) The backup storage redundancy should be Locally-redundant backup storage.

5) Set the login admin username to datacenter-admin and set an appropriate password.

6) Set the database size to 2 GiB.

7) Keep the rest of the configurations as default. Finally, make sure the database is in the Ready state before submitting this task.
Ans:
I can guide you step by step on how to create this Azure SQL Database using the **Azure portal**, following all your specified requirements. Here’s how you can do it:

---

### **Step 1: Sign in to Azure Portal**

1. Go to [https://portal.azure.com](https://portal.azure.com) and sign in with your Azure credentials.

---

### **Step 2: Create a SQL Database**

1. In the left-hand menu, select **Create a resource** → **Databases** → **SQL Database**.
2. In the **Basics** tab:

   * **Subscription**: Choose your subscription.
   * **Resource group**: Select an existing one or create a new one (e.g., `datacenter-rg`).
   * **Database name**: `datacenter-sqldb`
   * **Server**: Click **Create new**.

     * **Server name**: `datacenter-server-31660`
     * **Server admin login**: `datacenter-admin`
     * **Password**: Set a strong password (e.g., `Datacenter@1234` – ensure it meets Azure password rules)
     * **Location**: Pick the region closest to your users.
     * Click **OK**.
   * **Want to use SQL elastic pool?**: No.
   * **Compute + storage**: Click **Configure database**.

     * **Service tier**: Basic
     * **Max size**: 2 GiB
     * Click **Apply**.

---

### **Step 3: Backup Storage Redundancy**

1. Still in the **Basics** tab, find **Backup storage redundancy**:

   * Choose **Locally-redundant backup storage (LRS)**

---

### **Step 4: Networking**

1. Under **Networking**, make the database **publicly accessible**:

   * Select **Public endpoint**.
   * Add your IP to the **Firewall rules** so you can connect to the database from your network.

---

### **Step 5: Additional Settings**

1. Leave **Additional settings** as default (no need to restore from backup or use sample data unless you want).

---

### **Step 6: Review + Create**

1. Click **Review + create**.
2. Verify the summary matches your requirements.
3. Click **Create**.

---

### **Step 7: Wait for Deployment**

1. Azure will deploy the database.
2. Go to **All resources** → select your database.
3. Make sure the database **status shows “Ready”** before using it.

---

✅ **Checklist after creation**:

* Database name: `datacenter-sqldb` ✅
* Server name: `datacenter-server-31660` ✅
* Compute + storage: Basic, 2 GiB ✅
* Backup redundancy: Locally-redundant ✅
* Admin username: `datacenter-admin` ✅
* Publicly accessible: Yes ✅
* Status: Ready ✅


### **Q25: Backup an Azure SQL Database**

> *Implement long-term retention (LTR) for an Azure SQL Database. Set weekly backups for 12 months. Where are backups stored, and how can you restore a database to a specific point in time?*

## 🔧 **Infrastructure as Code & Automation**

### **Q26: Deploy Azure Resources Using ARM Template**

> *Use an ARM template to deploy a virtual network, storage account, and virtual machine as a single deployment. Include parameters for region, VM size, and storage type. How would you validate and test the deployment before applying it?*

## 💻 **Azure CLI Operations**

### **Q27: Create VM using Azure CLI**

> *Create a Windows Server VM using Azure CLI, including a new resource group, virtual network, NSG, and public IP. What are the minimum parameters needed to launch a working VM?*

### **Q28: Change Azure Virtual Machine Size Using CLI**

> *Resize an existing VM to `Standard F2s v2` using CLI. What steps are required if the VM is currently running, and how do you confirm the new size is applied?*

### **Q29: Create a Public Blob Container Using Azure CLI**

> *Use CLI to create a storage account and blob container with public read access. Upload a file and share its public URL. How would you verify public access from a browser?*

### **Q30: Create a Private Blob Container Using Azure CLI**

> *Using CLI, create a storage account with secure transfer enabled. Create a private blob container and upload a file. How do you generate a SAS token and use it to access the file securely?*


**Level 2**

### 🔌 **Q1: Assigning Public IP to Virtual Machines**

> *You deployed multiple VMs in a load-balanced setup but only one VM has a public IP. Update the configuration so each VM can be reached individually for admin purposes without disrupting the application traffic. Should you use dynamic or static public IPs? What are the security implications?*

The Nautilus DevOps Team has received a new request from the Development Team to set up a new Azure Virtual Machine (VM). This VM will be used to host a new application that requires a stable public IP address. To ensure that the VM has a consistent public IP, a Static Public IP address needs to be associated with it. The VM will be named xfusion-vm, and the Static Public IP will be named xfusion-pip. This setup will help the Development Team to have a reliable and consistent access point for their application.

Create an Azure VM named xfusion-vm using any available Ubuntu image, with the VM size Standard_B1s.
Generate an SSH public key on the azure-client host and associate it with the VM for SSH access.
Associate a Static Public IP address named xfusion-pip with this VM.
Ensure the VM is accessible via SSH using the generated public key.

Ans:
# If you don’t know the resource group name:List all resource groups with their regions
az group list --query "[].{name:name, location:location}" -o table

ssh-keygen -t rsa -C azureuser 

az network public-ip create \
  --resource-group kml_rg_main-845dfc36a0e341e4 \
  --name datacenter-pip \
  --sku Standard \
  --allocation-method Static \
  --location westus

az vm create \
  --resource-group kml_rg_main-845dfc36a0e341e4 \
  --name datacenter-vm \
  --image Ubuntu2204 \
  --size Standard_B1s \
  --admin-username azureuser \
  --ssh-key-values /root/.ssh/id_rsa.pub \
  --storage-sku Standard_LRS \
  --os-disk-size-gb 30 \
  --public-ip-address datacenter-pip \
  --location westus

az vm show \
  --resource-group  kml_rg_main-845dfc36a0e341e4 \
  --name datacenter-vm \
  --show-details \
  --query "powerState"

ssh -i <private-key-file-path> azureuser@IP

### 📝 **Q2: Configuring Instances with User Data**

> *You want every Linux VM created in your environment to automatically install Docker and start an Nginx container on boot. Use cloud-init/user data to achieve this. What format should the script be in, and how would you debug it if it fails?*
The Nautilus DevOps Team is working on setting up a new virtual machine (VM) to host a web server for a critical application. The team lead has requested you to create an Azure VM that will serve as a web server using Nginx. This VM will be part of the initial infrastructure setup for the Nautilus project. Ensuring that the server is correctly configured and accessible from the internet is crucial for the upcoming deployment phase.

As a member of the Nautilus DevOps Team, your task is to create a VM with the following specifications:

Instance Name: The VM must be named nautilus-vm.

Image: Use any available Ubuntu image to create this VM.

Custom Script Extension/User Data: Configure the VM to run a custom script during its launch. This script should:

Install the Nginx package.
Start the Nginx service.
Network Security Group (NSG): Ensure that the VM allows HTTP traffic on port 80 from the internet.
Ans:
To create the VM and set it up using **Azure Portal (GUI)**, here's a step-by-step guide on how to achieve the same result with a graphical interface.

---

### **Step 1: Create the Virtual Machine**

1. **Log in to Azure Portal:**

   * Go to the [Azure Portal](https://portal.azure.com/).
   * Log in with your Azure account credentials.

2. **Create a Resource Group:**

   * In the left sidebar, click on **Resource Groups**.
   * Click on **+ Create** to create a new resource group.
   * Provide a **Name** (e.g., `nautilus-rg`) and choose a **Region** (e.g., East US).
   * Click **Review + Create** and then click **Create**.

3. **Create a Virtual Machine:**

   * In the left sidebar, click on **Create a resource**.
   * In the search box, type **Virtual Machine**, and select **Virtual Machine**.
   * Click on **Create** to begin the VM creation process.

#### **Fill out the VM Creation Form:**

* **Subscription**: Choose the subscription you want to use.
* **Resource Group**: Choose the `nautilus-rg` resource group you created.
* **Virtual Machine Name**: Enter `nautilus-vm`.
* **Region**: Select the region (e.g., **East US**).
* **Image**: Choose **Ubuntu 20.04 LTS** (or another Ubuntu version available).
* **Size**: Select an appropriate VM size, such as **Standard_B1s**.
* **Authentication Type**: Choose **SSH public key** or **Password**.

  * If SSH is selected, make sure you have your SSH keys ready.
  * If using Password, set a strong admin password.

Click **Next** through the tabs for **Disks**, **Networking**, and **Management**.

4. **Networking Settings:**

   * Under the **Networking** tab, ensure that your **Network Security Group (NSG)** allows **HTTP traffic (port 80)**.
   * You should see a pre-configured Network Security Group associated with the VM.
   * If it doesn't already allow port 80, you can edit it to ensure HTTP traffic is allowed.

   **To configure HTTP (port 80)**:

   * Click on **Manage inbound ports**.
   * Select **Allow selected ports** and make sure **HTTP (port 80)** is checked.

#### **Review and Create the VM:**

* Click on **Review + Create** to validate your settings.
* If everything looks good, click **Create** to deploy your VM.

---

### **Step 2: Configure the VM with Nginx**

Once the VM is created, you need to configure it to install and start Nginx.

#### **1. SSH into the VM:**

* Once the VM is deployed, go to the **Overview** tab of your VM.
* Copy the **Public IP Address** of your VM.
* Use an SSH client (e.g., **Putty** or the **terminal** on macOS/Linux) to connect to the VM using the SSH public key or password you provided earlier.

Example command:

```bash
ssh azureuser@<public-ip-address>
```

#### **2. Create the Custom Script (Optional)**

You can either manually configure the VM after SSH access or use a custom script to automate the process.

1. **Create a Script to Install Nginx:**
   Create a file called `nginx-setup.sh` on your local machine with the following content:

```bash
#!/bin/bash
# Update and Install Nginx
sudo apt-get update -y
sudo apt-get install -y nginx

# Start Nginx service
sudo systemctl start nginx
sudo systemctl enable nginx
```

2. **Upload the Script to Azure (Optional):**

   * You can upload the script using an Azure Storage account and use it as a custom script extension for your VM. Alternatively, you can copy-paste the script directly once you SSH into the VM.

#### **3. Using the Custom Script Extension (via Azure Portal):**

To automate this with Azure’s **Custom Script Extension**, follow these steps:

1. **Go to your Virtual Machine:**

   * In the **Azure Portal**, search for and select the **Virtual Machines** section.
   * Choose the `nautilus-vm` that you just created.

2. **Add a Custom Script Extension:**

   * In the left sidebar under the VM’s settings, click on **Extensions + applications**.
   * Click on **+ Add**.
   * Select **Custom Script for Linux**.
   * Click **Next**.

3. **Upload the Script:**

   * In the **Script file** section, upload your `nginx-setup.sh` file.
   * If you don’t have the file uploaded already, you’ll need to use **Azure Storage** or **GitHub** to host the script file.
   * After uploading, click **Review + Create**.

4. **Run the Script:**

   * Click **Create** to add the extension and run the script on the VM.
   * Once the script runs successfully, Nginx should be installed and running.

---

### **Step 3: Verify the Nginx Installation**

1. **Check Nginx Status:**

   * SSH into the VM again if needed.
   * Check the status of Nginx:

   ```bash
   sudo systemctl status nginx
   ```

2. **Test in a Browser:**

   * Open your web browser.
   * Enter the **Public IP address** of the VM (which you copied earlier).
   * You should see the **Nginx default welcome page**.

---

### **Step 4: Finalize and Ensure HTTP Access**

1. **Test HTTP Access:**

   * Verify that your VM is accessible over HTTP (port 80) by visiting the public IP address in any web browser.
   * You should see the default Nginx page.




### 🔄 **Q3: Automating User Data Configuration Using the CLI**

> *You’re automating VM provisioning via Azure CLI. Include a custom user data script that installs software on boot. How do you encode the script properly, pass it in the `az vm create` command, and verify it was executed successfully?*
The Nautilus DevOps Team is working on setting up a new virtual machine (VM) to host a web server for a critical application. The team lead has requested you to create an Azure VM that will serve as a web server using Nginx. This VM will be part of the initial infrastructure setup for the Nautilus project. Ensuring that the server is correctly configured and accessible from the internet is crucial for the upcoming deployment phase.

As a member of the Nautilus DevOps Team, your task is to create a VM using Azure CLI with the following specifications:

Instance Name: The VM must be named xfusion-vm.

Image: Use any available Ubuntu image to create this VM.

Custom Script Extension/User Data: Configure the VM to run a custom script during its launch. This script should:

Install the Nginx package.
Start the Nginx service.
Network Security Group (NSG): Ensure that the VM allows HTTP traffic on port 80 from the internet.

Instructions:

Use Azure CLI commands to set up the VM in the specified configuration.
Ensure the VM is accessible from the internet on port 80.
The Nginx service should be running after setup.


Use the Azure CLI commands to complete the task.


Notes:

Create the resources only in the East US region.
You may use the default resource group or create a new one if needed.

Ans:
# If you don’t know the resource group name:List all resource groups with their regions
az group list --query "[].{name:name, location:location}" -o table
- **OS Disk size:** 30 GB  
- **Storage SKU:** Standard_LRS (standard storage)  
- **VM size:** `B1s`  

Here’s the updated **Azure CLI** command set with those specifications included:

---

## 🖥️ Create the VM with Disk, Storage, and Size
```bash
az vm create \
  --resource-group kml_rg_main-c91e637771de403f \
  --name xfusion-vm \
  --image Ubuntu2204 \
  --size Standard_B1s \
  --storage-sku Standard_LRS \
  --os-disk-size-gb 30 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --location westus
```

---

## 🌐 Open Port 80 for HTTP
```bash
az vm open-port \
  --resource-group kml_rg_main-c91e637771de403f \
  --name xfusion-vm \
  --port 80
```

---

## 📜 Custom Script Extension to Install Nginx
```bash
az vm extension set \
  --resource-group kml_rg_main-c91e637771de403f \
  --vm-name xfusion-vm \
  --publisher Microsoft.Azure.Extensions \
  --name CustomScript \
  --settings '{"commandToExecute":"sudo apt-get update && sudo apt-get install -y nginx && sudo systemctl start nginx && sudo systemctl enable nginx"}'
```

---

## ✅ Verify
1. Get the public IP:

az vm show \
  --resource-group kml_rg_main-c91e637771de403f \
  --name xfusion-vm \
  --show-details \
  --query publicIps \
  --output tsv

2. Visit `http://<PUBLIC_IP>` — you should see the **Nginx welcome page**.


### 🔐 **Q4: Securing Virtual Machine SSH Access**

> *You need to restrict SSH access to your VMs to only a specific IP range and disable password-based authentication. Implement this using NSGs and VM OS-level changes. What extra steps are needed if using Azure Bastion instead of public IPs?*

The Nautilus DevOps team needs to set up a new Virtual Machine (VM) on the Azure cloud that can be accessed securely from their landing host (azure-client). Follow the steps below to complete this task:

Create an SSH Key: On the azure-client host, check if an SSH key already exists. If it doesn’t exist, create a new SSH key on the azure-client host that will be used for password-less SSH access.

Create a Virtual Machine: Use the Azure Portal or Azure CLI to create a new Virtual Machine named datacenter-vm in the westus region. Set the VM size to Standard_B1s and configure the VM with SSH access for the azureuser account using the newly created SSH key.

Configure SSH Access: Ensure that the SSH key from the azure-client host is added to the azureuser account on datacenter-vm, enabling secure, password-less SSH access from the azure-client host.

Verify Connectivity: Test the connection from azure-client to datacenter-vm using SSH to confirm that password-less access has been set up correctly.

Complete these tasks entirely within the Azure Portal or Azure CLI.
Ans:
Got it — let’s walk through how the Nautilus DevOps team can complete this **entirely within the Azure Portal**. I’ll break it down step by step so you can follow along clearly:

---

## 🔑 Step 1: Create an SSH Key on `azure-client`
Since you’re working from the **azure-client landing host**, you’ll need an SSH key pair.

- Open a terminal on `azure-client`.
- Check if an SSH key already exists:
  ```bash
  ls ~/.ssh/id_rsa.pub
  ```
- If it doesn’t exist, generate a new one:
  ```bash
  ssh-keygen -t rsa -b 4096 -C "azureuser@azure-client"
  ```
- The public key will be saved at `~/.ssh/id_rsa.pub`.

👉 You’ll need this public key when creating the VM in the Azure Portal.

---

## 🖥️ Step 2: Create the Virtual Machine in Azure Portal
1. Sign in to the [Azure Portal](https://portal.azure.com).
2. Navigate to **Virtual Machines** → **Create** → **Azure Virtual Machine**.
3. Fill in the details:
   - **Subscription**: Select your subscription.
   - **Resource Group**: Choose an existing one or create new.
   - **VM Name**: `datacenter-vm`
   - **Region**: `West US`
   - **Size**: `Standard_B1s`
   - **Authentication type**: SSH public key
   - **Username**: `azureuser`
   - **SSH public key source**: Paste the contents of `~/.ssh/id_rsa.pub` from `azure-client`.
4. Networking:
   - Ensure **Inbound port rules** allow SSH (port 22).
   - Leave defaults for other settings unless your org requires changes.
5. Review + Create → Click **Create**.

---

## 🔐 Step 3: Configure SSH Access
Azure automatically provisions the VM with the SSH key you pasted. That means the `azureuser` account on `datacenter-vm` is already configured for password-less SSH.

---

## ✅ Step 4: Verify Connectivity
From the `azure-client` host, test the connection:

```bash
ssh azureuser@datacenter-vm-public-ip
```

- Replace `datacenter-vm-public-ip` with the VM’s public IP address (visible in the Azure Portal under the VM’s **Overview**).
- If everything is set up correctly, you’ll connect without being prompted for a password.

---

## 🎯 Summary
- **SSH key** created on `azure-client`.
- **VM** `datacenter-vm` deployed in **West US** with size `Standard_B1s`.
- **SSH access** configured for `azureuser` using the public key.
- **Connectivity verified** with password-less SSH.


### 💽 **Q5: Expanding and Managing Disk Storage**

> *Your VM is running out of space. Attach a new data disk and expand the root volume by 50 GB without downtime. How do you perform this safely and validate the operation inside the VM (Linux or Windows)?*
The Nautilus DevOps team needs to expand the storage capacity of an existing virtual machine and add an additional data disk to support increased workloads. This task requires resizing the existing VM disk and mounting a new data disk to the VM.

As a member of the team, perform the following steps:

1) Expand the existing VM xfusion-vm disk from 32Gi to 64Gi.

2) Also create a new standard HDD data disk named xfusion-disk of 64Gi and mount the disk to VM xfusion-vm at location /mnt/xfusion-disk.

Ans:
Got it — you’d like to see how this task is done through the **cloud provider’s GUI (portal)** instead of CLI. Let’s walk through the steps visually-oriented, assuming you’re using **Azure Portal** (the process is very similar in AWS or GCP):

---

## 🔹 Step 1: Expand the existing VM disk (xfusion-vm)
1. Log in to the **Azure Portal**.
2. Navigate to **Virtual Machines** → select **xfusion-vm**.
3. In the left menu, go to **Disks**.
4. Click on the **OS Disk** (currently 32Gi).
5. Select **Size + performance**.
6. Change the size from **32Gi → 64Gi**.
7. Click **Save**.
8. Restart the VM if prompted.
9. Inside the VM (via SSH or RDP), expand the filesystem:
   - Linux: `lsblk`, then `sudo growpart /dev/sda 1` and `sudo resize2fs /dev/sda1`.
   - Windows: use **Disk Management** → right-click → **Extend Volume**.

---

## 🔹 Step 2: Create and attach a new data disk
1. In the same **Disks** section of **xfusion-vm**, click **+ Add data disk**.
2. Choose **Create disk**.
3. Name it **xfusion-disk**.
4. Select **Standard HDD** as the storage type.
5. Set size to **64Gi**.
6. Click **Save** → the disk will be attached to the VM.

---

## 🔹 Step 3: Format and mount the new disk
### Linux VM:
1. SSH into the VM.
2. Run `lsblk` to identify the new disk (likely `/dev/sdc`).
3. Partition and format:
   ```bash
   sudo fdisk /dev/sdc
   sudo mkfs.ext4 /dev/sdc1
   ```
4. Create mount point:
   ```bash
   sudo mkdir -p /mnt/xfusion-disk
   sudo mount /dev/sdc1 /mnt/xfusion-disk
   ```
5. Persist across reboots:
   ```bash
   echo "/dev/sdc1 /mnt/xfusion-disk ext4 defaults,nofail 0 2" | sudo tee -a /etc/fstab
   ```

### Windows VM:
1. Open **Disk Management**.
2. Initialize the new disk.
3. Create a new volume, format as NTFS.
4. Assign a drive letter (e.g., `D:`).
5. Use it as your data disk.

---

✅ **End Result:**
- The OS disk of **xfusion-vm** is expanded to **64Gi**.  
- A new **64Gi Standard HDD disk** named **xfusion-disk** is attached and mounted at **`/mnt/xfusion-disk`** (Linux) or as a new drive (Windows).  


### 🌐 **Q6: Deploying Virtual Machines in a Public Virtual Network**

> *You’re deploying a VM that hosts a public-facing web application. Configure a public subnet with internet access, NSG rules, and a VM with a static IP. What routing and security changes are required to make the application accessible securely?*
The Nautilus DevOps Team has received a request from the Networking Team to set up a new public VNet to support a set of public-facing services. This VNet will host various resources that need to be accessible over the internet. As part of this setup, you need to ensure the VNet has public subnets with automatic public IP assignment for resources. Additionally, a new VM will be launched within this VNet to host public applications that require SSH access. This setup will enable the Networking Team to deploy and manage public-facing applications.

Create a public VNet named xfusion-pub-vnet, and a subnet named xfusion-pub-subnet under the same, make sure public IP is being auto-assigned to resources under this subnet. Further, create a VM named xfusion-pub-vm under this VNet. Make sure SSH port 22 is open for this instance and accessible over the internet. Use the Azure portal to complete the task and ensure that SSH access is configured correctly.
Ans:
Here’s how you can complete this setup step‑by‑step in the **Azure Portal GUI**:

---

## 🔹 Step 1: Create the Public VNet
1. Sign in to the **Azure Portal**.
2. In the left menu, select **Virtual networks** → **+ Create**.
3. Fill in:
   - **Name**: `xfusion-pub-vnet`
   - **Region**: same region where you’ll deploy the VM
   - **Resource Group**: choose or create one (e.g., `NautilusRG`)
4. Click **Next: IP Addresses**.
5. Define the **Address space** (e.g., `10.0.0.0/16`).
6. Add a **Subnet**:
   - **Subnet name**: `xfusion-pub-subnet`
   - **Subnet address range**: e.g., `10.0.1.0/24`
   - Ensure **Public IP assignment** is enabled (this is controlled later when attaching NICs, but subnet must allow it).
7. Click **Review + Create** → **Create**.

---

## 🔹 Step 2: Create the VM in the Public VNet
1. Go to **Virtual machines** → **+ Create** → **Azure virtual machine**.
2. Fill in:
   - **Name**: `xfusion-pub-vm`
   - **Region**: same as VNet
   - **Image**: Ubuntu Server (or your preferred OS)
   - **Size**: choose based on workload
   - **Authentication type**: SSH public key (recommended) or password
3. Under **Networking**:
   - Select **Virtual network**: `xfusion-pub-vnet`
   - Select **Subnet**: `xfusion-pub-subnet`
   - **Public IP**: set to **Create new** (this ensures auto‑assignment of a public IP)
   - **NIC network security group**: choose **Basic** and allow **SSH (22)** inbound
4. Click **Review + Create** → **Create**.

---

## 🔹 Step 3: Configure SSH Access
1. Once the VM is deployed, go to **xfusion-pub-vm → Networking**.
2. Confirm inbound port rules:
   - **Port**: 22
   - **Protocol**: TCP
   - **Source**: Any (or restrict to your IP for security)
   - **Action**: Allow
3. Copy the **Public IP address** from the VM overview.
4. Test SSH access:
   ```bash
   ssh azureuser@<public-ip>
   ```

---

## ✅ Final Setup
- **VNet**: `xfusion-pub-vnet`
- **Subnet**: `xfusion-pub-subnet` (public IP auto‑assigned)
- **VM**: `xfusion-pub-vm` with a public IP
- **SSH port 22** open and accessible over the internet

### 🔒 **Q7: Deploying Virtual Machines in a Private Virtual Network**

> *For compliance, you need to deploy a VM in a private subnet with no internet exposure. Use NAT Gateway or Azure Bastion for outbound access or management. How do you configure routing and DNS resolution in such an environment?*
The Nautilus DevOps team is expanding their Azure infrastructure and requires the setup of a private Virtual Network (VNet) along with a subnet. This VNet and subnet configuration will ensure that resources deployed within them remain isolated from external networks and can only communicate within the VNet. Additionally, the team needs to provision a Virtual Machine (VM) under the newly created private VNet. This VM should be accessible over SSH from within the VNet only, allowing for secure communication and resource management within the Azure environment.

The name of the VNet must be datacenter-priv-vnet, create a subnet named datacenter-priv-subnet under the same. Further, create a Virtual Machine named datacenter-priv-vm under this VNet. Additionally, create a Network Security Group (NSG) named datacenter-priv-nsg, and ensure that the NSG rules for the VM allow access only from within the VNet's CIDR block. Ensure all resources are created in the East US region.
Ans:
## 🌐 Step 1: Create the Virtual Network (VNet)
1. Sign in to the [Azure Portal](https://portal.azure.com).
2. In the left menu, select **Create a resource** → **Networking** → **Virtual Network**.
3. Fill in:
   - **Name:** `datacenter-priv-vnet`
   - **Region:** East US
   - **Resource Group:** (create or select one, e.g., `NautilusRG`)
   - **Address space:** `10.0.0.0/16`
4. Under **Subnets**, click **Add subnet**:
   - **Subnet name:** `datacenter-priv-subnet`
   - **Subnet address range:** `10.0.1.0/24`
   - **Private Subnet**: Enabled
5. Click **Review + Create** → **Create**.

---

## 🔒 Step 2: Create the Network Security Group (NSG)
1. Go to **Create a resource** → **Networking** → **Network Security Group**.
2. Fill in:
   - **Name:** `datacenter-priv-nsg`
   - **Region:** East US
   - **Resource Group:** `NautilusRG`
3. After creation, open the NSG and go to **Inbound security rules**.
4. Add a rule:
   - **Name:** `Allow-SSH-From-VNet`
   - **Priority:** 100
   - **Source:** IP addresses
   - **Source IP range:** `10.0.0.0/16`
   - **Destination:** `10.0.0.0/16`
   - **Port:** 22
   - **Protocol:** TCP
   - **Action:** Allow

---
## 💻 Step 3: Create the Virtual Machine
1. In the Azure Portal, go to **Create a resource** → **Virtual Machine**.
2. Fill in:
   - **Name:** `datacenter-priv-vm`  
   - **Region:** West US (same as VNet)  
   - **Resource Group:** `kml_rg_main-cdb8d615621b42b6`  
   - **Image:** Ubuntu LTS (or preferred OS)  
   - **Authentication:** SSH public key  
   - **Username:** e.g., `azureuser`  
   - Upload or generate SSH key.  
3. Under **Networking**:
   - **Virtual Network:** `datacenter-priv-vnet`  
   - **Subnet:** `datacenter-priv-subnet`  
   - **Public IP:** None (to keep it private)  
   - **NIC NSG:** Select `datacenter-priv-nsg`  
4. Click **Review + Create** → **Create**.

---

## 🏗 Final Architecture
- **VNet:** `datacenter-priv-vnet`  
- **Subnet:** `datacenter-priv-subnet`  
- **NSG:** `datacenter-priv-nsg` (SSH restricted to VNet CIDR)  
- **VM:** `datacenter-priv-vm` (private, only accessible via SSH inside VNet)  



### 🧰 **Q8: Troubleshooting Public Virtual Network Configurations**

> *Your VM in a public subnet is not accessible via its public IP. List and explain all the configuration points (e.g., NSGs, NIC, public IP association, route tables) you would inspect to identify and fix the issue.*
The Nautilus DevOps Team deployed an Nginx server on an Azure VM in a public VNet named devops-vnet. However, the server is still inaccessible from the internet.

As a DevOps team member, complete the following tasks:

Verify VNet Configuration: Ensure devops-vnet allows internet access.
Attach Public IP: A public IP named devops-pip already exists. Attach this public IP to the VM devops-vm to make it accessible from the internet.
Ensure Accessibility: Confirm the VM devops-vm is accessible on port 80.
Use the provided Azure credentials to troubleshoot and resolve the issue.

Ans:

## 1. Verify VNet Configuration (Azure Portal)

1. Sign in to **Azure Portal**
2. Go to **Virtual networks**
3. Select **nautilus-vnet**
4. Click **Subnets**
5. Select the subnet used by **nautilus-vm**

✔️ Verify:

* No **User Defined Route** forcing `0.0.0.0/0` to a firewall or virtual appliance
* No restrictive **Network Security Group** blocking inbound traffic

If a route table is attached and blocks internet, remove and add new.

## How to Add This via Azure Portal (GUI)

Go to Route tables

Select nautilus-rtb

Click + Add route

Fill in:

Route name: InternetRoute (or any name)

Address prefix: 0.0.0.0/0

Next hop type: Internet

Save the route
---

## 2. Attach Public IP (nautilus-pip) to VM

> Public IPs are attached to the **Network Interface**, not directly to the VM.

1. Go to **Virtual machines**
2. Open **nautilus-vm**
3. Select **Networking** from the left menu
4. Click the **Network interface** (e.g., `nautilus-vm-nic`)
5. Click **IP configurations**
6. Select **ipconfig1**
7. Under **Public IP address**, select **nautilus-pip**
8. Click **Save**

✔️ VM now has a public IP.

---

## 3. Ensure Port 80 Is Allowed (NSG)

### 3.1 Check NSG Rules

1. In **nautilus-vm → Networking**
2. Under **Inbound port rules**, verify **HTTP (80)** is allowed

If not present:

### 3.2 Add Inbound Rule

1. Click **Add inbound port rule**
2. Configure:

   * **Source**: Any
   * **Source port ranges**: *
   * **Destination**: Any
   * **Destination port ranges**: `80`
   * **Protocol**: TCP
   * **Action**: Allow
   * **Priority**: `100`
   * **Name**: `Allow-HTTP`
3. Click **Add**

✔️ Port 80 is now open.

---

## 4. Verify Nginx Is Running

1. Go to **nautilus-vm**
2. Click **Connect → SSH**
3. Use **Azure Bastion** or native SSH

Run:

```bash
sudo systemctl status nginx
```

If not running:

```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```

Test locally:

```bash
curl http://localhost
```

---

## 5. Confirm Internet Access

1. Copy the **Public IP address** from the VM Overview page
2. Open a browser:

```
http://<PUBLIC-IP>
```

✔️ You should see the **Nginx Welcome Page**

### 📦 **Q9: Working with Azure Container Registry (ACR)**

> *Push a custom Docker image to ACR and deploy it on an Azure VM. Authenticate securely, set up `docker login`, and configure the VM to pull and run the image on boot. How would you automate this as part of a CI/CD pipeline?*

The Nautilus DevOps team has been tasked with setting up a containerized application. They need to create a Azure Container Registry (ACR) to store their Docker images. Once the repository is created, they will build a Docker image from a Dockerfile located on the azure-client host and push this image to the ACR repository. This process is essential for maintaining and deploying containerized applications in a streamlined manner.

1) Create a ACR repository named datacenteracr15866 under East US.

2) Pricing plan must be Basic.

3) Dockerfile already exists under /root/pyapp directory on azure-client host.

4) Build a Docker image using this Dockerfile and push the same to the newly created ACR repo. The image tag must be latest i.e datacenteracr15866:latest.

Ans:

## **Step 1: Create a Resource Group (if you don’t have one)**

1. Log in to the [Azure Portal](https://portal.azure.com).
2. Search for **Resource groups** in the top search bar.
3. Click **+ Create**.
4. Fill in:

   * **Resource group name:** `datacenter-rg` (or any name you prefer)
   * **Region:** `East US`
5. Click **Review + Create**, then **Create**.

---

## **Step 2: Create an Azure Container Registry (ACR)**

1. In the portal search bar, type **Container registries** and select it.
2. Click **+ Create**.
3. Fill in the form:

   * **Subscription:** Your subscription
   * **Resource group:** `datacenter-rg`
   * **Registry name:** `datacenteracr15866`
   * **Location:** `East US`
   * **SKU:** `Basic`
4. Click **Review + Create**, then **Create**.

---

## **Step 3: Get the Login Server**

1. Open your newly created registry `datacenteracr15866`.
2. On the **Overview** page, note the **Login server** (it will look like `datacenteracr15866.azurecr.io`).

   > You will need this for Docker tagging.

---

## **Step 4: Build and Push Docker Image**

Unfortunately, Azure Portal doesn’t let you directly build Docker images from a local host. You have **two GUI options**:

### **Option A: Use Azure Cloud Shell (GUI-integrated terminal)**

1. Open **Azure Cloud Shell** (top-right corner of the portal).
2. Upload your `/root/pyapp` directory files to the Cloud Shell.
3. Run the commands:

```bash
# Log in to ACR
az acr login --name datacenteracr15866

# Build Docker image
docker build -t datacenteracr15866.azurecr.io/datacenteracr15866:latest /path/to/pyapp

# Push image
docker push datacenteracr15866.azurecr.io/datacenteracr15866:latest
```
# Incase Error Occured to pull:
**Docker Hub’s rate limit for unauthenticated pulls**. You **cannot pull any more images without logging in**.

Here’s how to fix it:

---

### **Step 1: Log in to Docker Hub**

```bash
docker login
```

* Username: your Docker Hub username(tamizh2022)
* Password: your Docker Hub password (or personal access token if 2FA is enabled)

> After successful login, Docker knows who you are and increases your pull limit.

---

### **Step 2: Pull the base image again**

```bash
docker pull python:3.8-slim
```

It should now succeed.

---

### **Step 3: Build your application image**

```bash
d  ocker build -t datacenteracr15866.azurecr.io/datacenteracr15866:latest /root/pyapp
```

---

### **Step 4: Push the image to your ACR**

```bash
docker push datacenteracr15866.azurecr.io/datacenteracr15866:latest
```

---

💡 **Alternative workaround if you want to avoid Docker Hub limits permanently:**

1. Pull the base image **once** on a machine with Docker Hub login.
2. Tag it and push it to your **ACR**:

```bash
docker tag python:3.8-slim datacenteracr15866.azurecr.io/python:3.8-slim
docker push datacenteracr15866.azurecr.io/python:3.8-slim
```

3. Then update your Dockerfile to use your ACR-hosted base image:

```dockerfile
FROM datacenteracr15866.azurecr.io/python:3.8-slim
```

Now all builds will come from your ACR instead of Docker Hub, bypassing rate limits.

---

If you want, I can write a **ready-to-run sequence of commands** that logs in to Docker Hub, builds your image, tags it, and pushes it to ACR in one shot. It’s fully automated.

Do you want me to do that?

> Replace `/path/to/pyapp` with the Cloud Shell path.

### **Option B: Use Azure Container Registry Tasks (Full GUI)**

1. Go to your **ACR** in the portal.
2. Select **Tasks** → **+ Quick Task**.
3. Configure:

   * **Source Type:** `Local Git` (if your Dockerfile is in a Git repo) or `GitHub`
   * **Image Name and Tag:** `datacenteracr15866:latest`
   * **Dockerfile Path:** `/Dockerfile` or relative path
4. Click **Run Task**.
5. ACR will build the Docker image and push it automatically.

---

## **Step 5: Verify Image in GUI**

1. Go to your **ACR** → **Repositories**.
2. You should see `datacenteracr15866` with tag `latest`.


### 🔧 **Q10: Set Up and Manage a Secure Azure DevOps Repository**

> *Your team is building infrastructure using ARM templates stored in Azure Repos. Create a private repository, configure branch policies for code reviews, and integrate it with Azure Pipelines. How would you implement secret scanning and access control?*

### 🌍 **Q11: Deploying and Managing a Web Application**

> *Deploy a multi-tier web application consisting of frontend and backend components. Use VMs or containers, secure communication with HTTPS, and manage scaling based on load. How would you monitor performance and perform zero-downtime updates?*
The Nautilus DevOps team is tasked with deploying a Python-based web application on Azure. You need to create a web app using the following specifications:

1) The Web App name should be xfusion-webapp.
2) It should be created in the West US region under the default resource group.
3) The publish option should be set to Code.
4) The Runtime Stack should be Python with Linux as the operating system.
5) Create a new App Service Plan named xfusion-learn-python with the SKU Basic B1.
6) Application Insights should be disabled.
7) Add tags:

Name: WebAppLearning
Environment: Dev
Make sure the web app is in Running state after creation.
Ans:
Here’s a clear, step-by-step guide to create the **Python-based web app** in **Azure Portal** based on your specifications. I’ll make it precise so you can follow easily:

---

### **Step 1: Sign in to Azure Portal**

1. Go to [https://portal.azure.com](https://portal.azure.com).
2. Sign in with your Azure account.

---

### **Step 2: Create the Web App**

1. In the left-hand menu, click **Create a resource** → **Compute** → **Web App**.
2. Fill in the **Basics** tab:

   | Field            | Value                                         |
   | ---------------- | --------------------------------------------- |
   | Subscription     | Select your subscription                      |
   | Resource Group   | Use the default resource group                |
   | Name             | `xfusion-webapp`                              |
   | Publish          | `Code`                                        |
   | Runtime stack    | `Python <latest version>` (e.g., Python 3.11) |
   | Operating System | `Linux`                                       |
   | Region           | `West US` Quota isssue create central us                                    |

---

### **Step 3: Configure the App Service Plan**

1. Under **App Service Plan**, choose **Create new**.
2. Enter the following:

   | Field        | Value                                       |
   | ------------ | ------------------------------------------- |
   | Name         | `xfusion-learn-python`                      |
   | Pricing tier | Click **Change size** → Select **Basic B1** |

---

### **Step 4: Configure Monitoring**

1. In the **Monitoring** tab:

   * **Application Insights** → Set to **Off**.

---

### **Step 5: Add Tags**

1. Go to the **Tags** tab.
2. Add the following key-value pairs:

   | Name        | Value          |
   | ----------- | -------------- |
   | Name        | WebAppLearning |
   | Environment | Dev            |

---

### **Step 6: Review + Create**

1. Click **Review + create**.
2. Validate the configuration.
3. Click **Create**.
4. Wait for deployment to complete.

---

### **Step 7: Verify the Web App**

1. After deployment, go to the **Web App resource**.
2. Ensure the **Status** shows **Running**.
3. You can browse the web app by clicking **Browse** at the top.

---

✅ Following these steps will ensure:

* Web App name: `xfusion-webapp`
* Location: West US
* Runtime: Python on Linux
* App Service Plan: `xfusion-learn-python`, Basic B1
* Application Insights: Disabled
* Tags applied
* Web app is running

### 🔄 **Q12: Synchronizing Containers Using the CLI**

> *You updated a Docker image and need to synchronize your ACR with the latest build. Use Azure CLI to push the image, verify it’s available, and redeploy the container on an Azure App Service or VM. How do you automate this with minimal downtime?*
To complete this data migration task efficiently using the Azure CLI, you will need to follow a structured process: creating the destination, performing the copy, and verifying the integrity of the data.

As part of a data migration project, the team lead has tasked the team with migrating data from an existing Azure Blob container to a new Blob container. The existing container contains a substantial amount of data that must be accurately transferred to the new container. The team is responsible for creating the new Blob container and ensuring that all data from the existing container is copied or synced to the new container completely and accurately. It is imperative to perform thorough verification steps to confirm that all data has been successfully transferred to the new container without any loss or corruption.
As a member of the Nautilus DevOps Team, your task is to perform the following:
Create a New Private Azure Blob Container: Name the container devops-dest-6318 under the storage account devopsst2010.
Data Migration: Migrate the file devops.txt from the existing devops-source-28162 container to the new devops-dest-6318 container.
Ensure Data Consistency: Ensure that both containers have the file devops.txt and confirm the file content is identical in both containers.
Use Azure CLI: Use the Azure CLI to perform the creation and data migration tasks.

---

### Phase 1: Create the New Container

First, create the private destination container as requested.

```bash
az storage container create \
    --name devops-dest-6318 \
    --account-name devopsst2010 \
    --public-access off \
    --auth-mode login


# Confirm it’s private (access off):  
az storage container show \
--name devops-dest-6318 \
--account-name devopsst2010 \
--auth-mode login \
--query "publicAccess"
```
### Phase 2: Migrate the Data

To move the specific file `devops.txt` from the source to the destination, use the `az storage blob copy start` command. This performs a server-side copy within Azure.

```bash
#Start server-side copy (same storage account):  
az storage blob copy start \
    --account-name devopsst2010 \
    --destination-container devops-dest-6318 \
    --destination-blob devops.txt \
    --source-container devops-source-28162 \
    --source-blob devops.txt \
    --auth-mode login

```

### Phase 3: Verification and Consistency Check

To ensure data consistency and accuracy, you should verify the file's existence and compare the **MD5 hashes (Content-MD5)**. This confirms the data was not corrupted during the transfer.

**1. Check if the file exists in the destination:**

```bash
# erify both containers contain devops.txt
# List source container:  
az storage blob list \
--account-name devopsst2010 \
--container-name devops-source-28162 \
--auth-mode login \
--query "[?name=='devops.txt'].name"

# List destination container:  
az storage blob list \
--account-name devopsst2010 \
--container-name devops-dest-6318 \
--auth-mode login \
--query "[?name=='devops.txt'].name"
```

**2. Compare Content Hashes:**
Run the following to retrieve the properties of both blobs and compare their `contentSettings.contentMd5` values.

```bash
# Get Source MD5
az storage blob show \
    --account-name devopsst2010 \
    --container-name devops-source-28162 \
    --name devops.txt \
    --query "properties.contentSettings.contentMd5"

# Get Destination MD5
az storage blob show \
    --account-name devopsst2010 \
    --container-name devops-dest-6318 \
    --name devops.txt \
    --query "properties.contentSettings.contentMd5"

```

---

### Summary of Actions

| Action | Command/Tool | Result |
| --- | --- | --- |
| **Provisioning** | `az storage container create` | Created `devops-dest-6318` |
| **Migration** | `az storage blob copy start` | Transferred `devops.txt` |
| **Integrity Check** | `az storage blob show` | Verified MD5 Hash match |

> [!IMPORTANT]
> Because `copy start` is asynchronous for large files, you can check the status using `az storage blob show --query "properties.copy.status"`. For a single `.txt` file, this is usually instantaneous.



### ⚖️ **Q13: Integrating Virtual Machines with Application Load Balancer**

> *Distribute traffic across multiple VMs hosting a web application using Azure Load Balancer. Implement health probes and ensure VMs automatically register/deregister during scaling. What type of load balancer (Basic vs. Standard) is appropriate, and why?*
The Nautilus DevOps team is currently working on setting up a simple application on the Azure cloud. They aim to establish an Azure Load Balancer in front of a Virtual Machine (VM) where an Nginx server is currently running. While the Nginx server currently serves a sample page, the team plans to deploy the actual application later.

Set up an Azure Load Balancer named xfusion-lb.
Configure the Load Balancer’s frontend IP configuration with the name xfusion-lb-ip and assign a public IP address with the same name (xfusion-lb-ip).
Create a backend pool named xfusion-backend-pool and add the VM running Nginx to this pool.
Create a health probe named xfusion-health-probe on port 80 to check the VM's health.
Set up a load balancer rule named xfusion-lb-rule to route traffic on port 80 to the backend pool on port 80.
Add an inbound rule to the existing NSG of the VM to allow HTTP traffic on port 80.
Ans:
Got it! Since you want to set up an **Azure Load Balancer** in front of your Nginx VM using the **Azure Portal**, I’ll walk you **step by step**. I’ll make it clear and sequential so the DevOps team can follow along.

---

## **Step 1: Create the Public IP Address**

1. Go to the **Azure Portal**: [https://portal.azure.com](https://portal.azure.com)
2. In the search bar, type **Public IP addresses** and click it.
3. Click **+ Create**.
4. Fill in:

   * **Name:** `xfusion-lb-ip`
   * **SKU:** Standard (recommended for production)
   * **IP Version:** IPv4
   * **Assignment:** Static
5. Click **Review + create**, then **Create**.

---

## **Step 2: Create the Load Balancer**

1. Search for **Load Balancers** in the portal.
2. Click **+ Create**.
3. Choose **Resource Group** and **Region** (same as your VM).
4. Fill in:

   * **Name:** `xfusion-lb`
   * **Type:** Public
   * **SKU:** Standard
5. Under **Frontend IP configuration**:

   * **Name:** `xfusion-lb-ip`
   * **IP address:** Select the **existing public IP** `xfusion-lb-ip` created earlier
6. Click **Review + create**, then **Create**.

---

## **Step 3: Create the Backend Pool**

1. Open the newly created Load Balancer (`xfusion-lb`) from **Load Balancers**.
2. In the left menu, click **Backend pools** → **+ Add**.
3. Fill in:

   * **Name:** `xfusion-backend-pool`
   * **Virtual network:** Select the network your VM is in
   * **Associated to:** Virtual machine
   * **Target:** Select your **Nginx VM**
4. Click **Add**.

---

## **Step 4: Create a Health Probe**

1. In the Load Balancer settings, go to **Health probes** → **+ Add**.
2. Fill in:

   * **Name:** `xfusion-health-probe`
   * **Protocol:** HTTP
   * **Port:** 80
   * **Path:** `/` (default)
   * **Interval:** 5 seconds
   * **Unhealthy threshold:** 2
3. Click **Add**.

---

## **Step 5: Create a Load Balancer Rule**

1. Go to **Load balancing rules** → **+ Add**.
2. Fill in:

   * **Name:** `xfusion-lb-rule`
   * **IP Version:** IPv4
   * **Frontend IP:** `xfusion-lb-ip`
   * **Backend Pool:** `xfusion-backend-pool`
   * **Protocol:** TCP
   * **Port:** 80 (both frontend and backend)
   * **Health Probe:** `xfusion-health-probe`
3. Click **Add**.

---

## **Step 6: Allow HTTP in the VM’s NSG**

1. Go to your VM → **Networking** → click the **Network Security Group (NSG)**.
2. Click **Inbound security rules** → **+ Add**.
3. Fill in:

   * **Source:** Any
   * **Source port ranges:** *
   * **Destination:** Any
   * **Destination port ranges:** 80
   * **Protocol:** TCP
   * **Action:** Allow
   * **Priority:** 100 (or any number that doesn’t conflict)
   * **Name:** `Allow-HTTP-80`
4. Click **Add**.
5. Verify: Curl lb-publicip

### 🌐 **Q14: Enabling Internet Connectivity for Virtual Machines**

> *Your VMs in a private subnet need internet access for software updates. Set up a NAT Gateway and configure route tables accordingly. How do you verify connectivity without exposing the VMs publicly?*

The Nautilus DevOps team has encountered an issue with an Azure VM named xfusion-vm. They are unable to install any packages on this VM due to connectivity issues. The team needs to identify the root cause of the problem and resolve it to restore normal operations.

Investigate the connectivity issue preventing package installation on the Azure VM xfusion-vm.
Implement a solution to resolve the connectivity issue and restore package installation capabilities on the VM.
Note: The SSH key required to access the Azure VM is already created and added to the VM's authorized keys. You can find the SSH key at /root/.ssh/id_rsa on the azure-client host.

Ans:

## 1. Access the Azure VM

From the **azure-client** host:

```bash
ssh -i /root/.ssh/id_rsa azureuser@xfusion-vm
```

(Replace `azureuser` with the actual VM username if different.)

---

## 2. Confirm the Problem

### Test basic connectivity

```bash
ping -c 3 8.8.8.8
```

* ✅ Works → outbound network is fine
* ❌ Fails → routing/NSG issue (rare in this lab)

### Test DNS resolution

```bash
ping -c 3 google.com
```

* ❌ Fails while IP ping works → **DNS is broken** (most likely root cause)

### Try package installation

```bash
yum install -y vim   # RHEL/CentOS
# or
apt update           # Ubuntu/Debian
```

You’ll typically see:

* `Could not resolve host`
* `Temporary failure resolving`

---

## 3. Root Cause Identified ✅

**The VM does not have a valid DNS resolver configured**, so it cannot resolve repository hostnames.
Without DNS, package managers cannot reach mirrors even if internet access exists.

---

## 4. Fix the Connectivity Issue (DNS)

### Step 1: Edit resolv.conf

```bash
sudo vi /etc/resolv.conf
```

Add **Google DNS** (or Azure DNS):

```ini
nameserver 8.8.8.8
nameserver 8.8.4.4
```

Save and exit.

---

### Step 2 (IMPORTANT): Prevent DNS from being overwritten

If the VM uses NetworkManager:

```bash
sudo vi /etc/NetworkManager/NetworkManager.conf
```

Ensure this exists:

```ini
[main]
dns=none
```

Restart NetworkManager:

```bash
sudo systemctl restart NetworkManager
```

---

## 5. Verify the Fix

### Test DNS

```bash
ping -c 3 google.com
```

### Test package installation

```bash
yum install -y vim
# or
apt update
```

✅ Packages should now install normally.

---

## 6. Final Status

✔ Root Cause: **Missing or incorrect DNS configuration**
✔ Resolution: **Manually configured valid DNS servers**
✔ Result: **Outbound connectivity restored, package installation working**

# Real Root Cause:
A Network Security Group rule (Block-All-Outbound, priority 200) explicitly denied all outbound traffic, overriding Azure’s default AllowInternetOutbound rule.

# Resolution:
Removed the outbound deny rule or added a higher-priority allow rule for Internet traffic, restoring outbound connectivity and package installation functionality.

### 🌉 **Q15: Configuring Virtual Network Peering**

> *You deployed backend services in a separate VNet from your frontend services. Configure VNet peering to allow secure communication between the two VNets. How do you handle DNS resolution across VNets and restrict unnecessary access?*

The Nautilus DevOps team has been tasked with demonstrating the use of VNet Peering to enable communication between two VNets. One VNet will be a private VNet that contains a private Azure VM, while the other will be a public VNet containing a publicly accessible Azure VM.

1) Existing Azure Resources:

Public VM: datacenter-pub-vm is already in the public VNet.
Private VNet and VM: datacenter-priv-vnet and datacenter-priv-vm exist in the private VNet with its subnet: datacenter-priv-subnet.
2) Create VNet Peering:

Create a VNet Peering between the Public VNet and Private VNet.
VNet Peering Name: datacenter-pub-to-priv-peering.
3) Test the Connection:

SSH into the public VM and verify that you can ping the private VM.
Ans:

## 1️⃣ Verify Existing Resources

You already have:

* **Public VNet**

  * VM: `datacenter-pub-vm` (publicly accessible)
* **Private VNet**

  * VNet: `datacenter-priv-vnet`
  * Subnet: `datacenter-priv-subnet`
  * VM: `datacenter-priv-vm` (private)

Ensure both VNets are:

* In the **same Azure region**
* Using **non-overlapping address spaces**

---

## 2️⃣ Create VNet Peering

> Azure VNet peering is **bi-directional**, so two peerings are created (one in each direction).

### Option A: Azure Portal (Recommended for demos)

1. Go to **Virtual networks**

2. Open the **Public VNet** (the one hosting `datacenter-pub-vm`)

3. Select **Peerings** → **+ Add**

4. Configure:

   * **Peering link name (this VNet → remote VNet)**

     ```
     datacenter-pub-to-priv-peering
     ```
   * **Virtual network**: `datacenter-priv-vnet`
   * **Allow virtual network access**: ✅ Enabled
   * **Allow forwarded traffic**: ✅ Enabled

5. Under **Remote peering link name**, Azure will ask for a name for the reverse peering.
   You can use any name but keep same else lab will fail:

   ```
   datacenter-pub-to-priv-peering
   ```

6. Click **Add**

✔️ After a few seconds, both peerings should show **Connected**

---

### Option B: Azure CLI (if required)

```bash
az network vnet peering create \
  --name datacenter-pub-to-priv-peering \
  --resource-group <resource-group> \
  --vnet-name <public-vnet-name> \
  --remote-vnet datacenter-priv-vnet \
  --allow-vnet-access
```

(Repeat in reverse direction for full connectivity.)

---

## 3️⃣ Validate Network Connectivity

### Step 1: Get the Private VM IP

From the Azure Portal:

* Open `datacenter-priv-vm`
* Copy its **Private IP address** (example: `10.1.0.4`)

---

### Step 2: SSH into the Public VM

```bash
ssh <username>@<public-vm-public-ip>
```

---

### Step 3: Ping the Private VM

```bash
ping <private-vm-private-ip>
```

✅ Successful replies confirm:

* VNet peering is working
* Routing between VNets is established

---

## ⚠️ If Ping Fails, Check These

* **NSG on private subnet/VM** allows ICMP (or at least inbound traffic from public VNet)
* **OS firewall** on `datacenter-priv-vm` allows ICMP
* VNets do **not** have overlapping CIDR ranges

---

## ✅ Final Result

* Public VM communicates with Private VM
* No VPN or gateway required
* Demonstrates secure, private Azure backbone connectivity via **VNet Peering**

If you want, I can also help you:

* Capture screenshots for documentation
* Test SSH instead of ping
* Lock down traffic using NSGs for best practices


**Level 3**

### 📦 **Q1: Managing Storage Lifecycle in Azure**

> *You are storing large volumes of infrequently accessed backup files in Azure Blob Storage. Design and implement a lifecycle management policy that moves data from Hot to Cool to Archive tiers after 30, 90, and 180 days respectively. How would you validate the policy and monitor cost savings over time?*

The Nautilus DevOps team needs to optimize data retention costs by automating the deletion of old blobs. They plan to implement Blob Lifecycle Management for a specific container in Azure Storage.

Task:
1) Create a Storage Account:

Name the storage account datacenterstor9481.
Set the region to East US.
Use Locally-redundant storage (LRS) as the redundancy option.
2) Create a Blob Container:

Name the container datacenter-container9481.
3) Upload a File to the Container:

Upload the file named tempfile.txt to the container. The file is present under /root of the client host.
4) Configure Blob Lifecycle Management:

Apply a Lifecycle Management rule named datacenter-del-rule to the container datacenter-container9481 to delete blobs after 7 days of last modification.
5) Validation:

Verify that the Lifecycle Management rule named datacenter-del-rule is correctly applied.

Ans:
Got it! You want to do **all of this using the Azure Portal (GUI)** instead of CLI. Here’s a **step-by-step guide** for each task:

---

## **1) Create the Storage Account**

1. Sign in to the [Azure Portal](https://portal.azure.com).
2. Click **Create a resource → Storage → Storage account**.
3. Fill in the details:

   * **Storage account name:** `datacenterstor9481`
   * **Region:** `East US`
   * **Performance:** `Standard`
   * **Redundancy:** `Locally-redundant storage (LRS)`
   * **Account kind:** `StorageV2 (general purpose v2)`
4. Click **Review + create**, then **Create**.

---

## **2) Create a Blob Container**

1. Navigate to your newly created storage account `datacenterstor9481`.
2. In the left menu, click **Containers**.
3. Click **+ Container**.
4. Name it `datacenter-container9481`.
5. Set **Public access level** to `Private (no anonymous access)`.
6. Click **Create**.

---

## **3) Upload a File to the Container**

1. Open the container `datacenter-container9481`.
2. Click **Upload**.
3. Browse and select `/root/tempfile.txt` from your computer.
4. Click **Upload**.

> Note: If `/root/tempfile.txt` is on a Linux server, you may need to download it locally first or use **Azure Storage Explorer** to upload it directly from the server.
# Fetch Rg Name
az group list --query "[].{name:name, location:location}" -o table
# Upload file from azure clinet machine
az storage blob upload \
  --account-name datacenterstor9481 \
  --account-key $ACCOUNT_KEY \
  --container-name datacenter-container9481 \
  --name tempfile.txt \
  --file /root/tempfile.txt


ACCOUNT_KEY=$(az storage account keys list \
  --resource-group Resource-Group \
  --account-name datacenterstor9481 \
  --query "[0].value" -o tsv)
---

## **4) Configure Blob Lifecycle Management**

1. Go to the **storage account** `datacenterstor9481`.
2. In the left menu, scroll down to **Data management → Lifecycle management**.
3. Click **+ Add rule**.

**Rule setup:**

* **Rule name:** `datacenter-del-rule`
* **Scope:** Choose **Limit blobs with filters** → **Blob type:** `Block blob`
* **Filter:** Add prefix `datacenter-container9481/` (ensures rule applies only to this container)
* **Base blob action:** **Delete**
* **Days after last modification:** `7`

4. Click **Add**, then **Save**.

---

## **5) Validation**

1. Go back to **Lifecycle management** in the storage account.
2. Check that the rule `datacenter-del-rule` appears in the list and is **Enabled**.
3. Make sure the rule shows **Delete after 7 days** and applies to **datacenter-container9481**.

✅ If it shows as above, your lifecycle rule is correctly applied.

az storage account management-policy show \
  --account-name datacenterstor9481 \
  --resource-group Resource-Group \
  --output json
---


### 🐬 **Q2: Setting Up MySQL on a Virtual Machine in Azure**

> *Your development team requires a MySQL database on a Linux VM. Deploy the VM, install and configure MySQL using a startup script, and secure it using a firewall and NSG. How would you ensure remote access is encrypted and restrict access to only specific IP ranges?*
The Nautilus DevOps team is tasked with integrating a PHP application hosted on an Azure VM with a MySQL database hosted on another Azure VM. This will validate the application's ability to connect to the database in the cloud.

Create the MySQL VM:

Create a VM named datacenter-mysql-vm using the MySQL Jetware image from the Azure Marketplace.
Configure the VM in the East US region.
Use Password as the authentication type.
Set the username as datacenter_admin and the password as Namin@123456.
Allow inbound traffic on port 3306 to enable MySQL access.
Setup the MySQL Database:

SSH into the datacenter-mysql-vm.
Use the sudo /jet/enter mysql command to access the MySQL shell.
Create a database named datacenter_db.
Create a MySQL user named datacenter_user with password password123.
Grant all privileges on the datacenter_db database to this user.
PHP VM Setup:

A VM named datacenter-php-vm already exists in the East US region.
This VM is hosting a PHP application and contains a pre-existing db_test.php file in the /var/www/html/ directory.
Database Connection Configuration:

Retrieve the public IP address of the datacenter-mysql-vm.
Update the database connection settings in the db_test.php file to use the MySQL credentials and public IP address of the datacenter-mysql-vm.
Validation:

Access the db_test.php file from the datacenter-php-vm using its public IP address.
Ensure the file displays the message Connected successfully, confirming the connection between the PHP application and the MySQL database.

Ans:
Ah! You want to do this **through the Azure Portal (GUI)** instead of the command line. No problem — let’s go **step by step using the Azure Portal**.

---

## **Step 1: Create the MySQL VM**

1. Go to the [Azure Portal](https://portal.azure.com/).
2. Click **Create a resource** → **Compute** → **Virtual Machine**.
3. Fill in the VM details:

   * **Name:** `datacenter-mysql-vm`
   * **Region:** `East US`
   * **Image:** Search for **MySQL Jetware** in the Marketplace
   * **Size:** Choose any size (B1s is fine for testing)
   * **Authentication type:** Password
   * **Username:** `datacenter_admin`
   * **Password:** `Namin@123456`
4. In **Inbound port rules**, select **Allow selected ports** → check **MySQL (3306)**.
5. Click **Review + Create** → **Create**.

> ✅ Wait until the VM is deployed.

---

## **Step 2: SSH into the MySQL VM**

1. In the Portal, go to **Virtual Machines** → click `datacenter-mysql-vm`.
2. Click **Connect** → **SSH** and follow the instructions.

Once connected:

```bash
sudo /jet/enter mysql
```

Inside MySQL:

```sql
CREATE DATABASE datacenter_db;
CREATE USER 'datacenter_user'@'%' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON datacenter_db.* TO 'datacenter_user'@'%';
FLUSH PRIVILEGES;
EXIT;
```

> ✅ `'%'` allows connections from any VM/public IP.

---

## **Step 3: Get the MySQL VM Public IP**

1. In Azure Portal, go to `datacenter-mysql-vm` → **Overview** → copy **Public IP address**.

> Example: `20.50.100.25`

---

## **Step 4: Update the PHP VM**

1. Go to your `datacenter-php-vm` in Azure Portal → **Connect** → SSH.
2. Open the file `/var/www/html/db_test.php`:

```bash
sudo nano /var/www/html/db_test.php
```

3. Update the connection info:

```php
<?php
$servername = "20.50.100.25"; // MySQL VM public IP
$username = "datacenter_user";
$password = "password123";
$dbname = "datacenter_db";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>
```

4. Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

---

## **Step 5: Test the PHP Connection**

1. In Azure Portal, go to `datacenter-php-vm` → **Overview** → copy **Public IP**.
2. Open a browser:

```
http://<datacenter-php-vm-public-ip>/db_test.php
```

> ✅ You should see: `Connected successfully`



### 🐳 **Q3: Running Containers on Azure Virtual Machines**

> *You have a Dockerized Python app and need to deploy it to a Linux-based Azure VM using Docker. Set up the VM, install Docker, and ensure the container starts automatically on reboot. How would you monitor and update the container remotely?*
Below is a clear, end-to-end guide the Nautilus DevOps team can follow to complete the task using the **Azure Portal and Azure CLI**.
(These are **instructions**, not actions performed by me.)

---

## 1) Azure Virtual Machine Setup

* The VM **datacenter-vm** already exists.
* Verify:

  * **Region**: East US
  * **Username**: `azureuser`
  * **SSH access** is enabled

No changes are required for the VM itself.

---

## 2) Create a Private Storage Account and Blob Container

### a) Create the Storage Account

Using **Azure Portal**:

1. Go to **Storage accounts** → **Create**
2. Configure:

   * **Subscription**: Your subscription
   * **Resource Group**: Same as VM (recommended)
   * **Storage account name**: `datacenterstor15117`
   * **Region**: East US
   * **Performance**: Standard
   * **Redundancy**: **Locally-redundant storage (LRS)**
3. Under **Networking**:

   * Set **Public network access** to **Enabled** (default)
4. Review + Create → **Create**

---

### b) Create the Private Blob Container

1. Open the storage account **datacenterstor15117**
2. Go to **Data storage → Containers**
3. Click **+ Container**
4. Configure:

   * **Name**: `datacenter-container15117`
   * **Public access level**: **Private (no anonymous access)**
5. Click **Create**

---

## 3) Retrieve the Storage Account Access Key

1. In **datacenterstor15117**, go to:

   * **Security + networking → Access keys**
2. Copy **Key1 → Key value**
3. Save it securely (this will be used in the CLI command)

> ⚠️ Treat this key like a password.

---

## 4) Create a Test File on the VM

### a) SSH into the VM

From your local terminal:

```bash
ssh azureuser@<VM_PUBLIC_IP>
```

### b) Create the Test File

```bash
cd /home/azureuser
echo "this is a test file" > testfile.txt
```

### c) Verify the File

```bash
cat testfile.txt
```

Expected output:

```
this is a test file
```

---

## 5) Upload the File to Azure Blob Storage

### a) Ensure Azure CLI Is Installed on the VM

```bash
az --version
```

If not installed:

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

### b) Upload the File

Run the following command **on the VM**, replacing `<access-key>` with the key you copied earlier:

```bash
az storage blob upload \
  --account-name datacenterstor15117 \
  --account-key <access-key> \
  --container-name datacenter-container15117 \
  --name testfile.txt \
  --file /home/azureuser/testfile.txt
```

---

## 6) Verify the Upload (Optional but Recommended)

```bash
az storage blob list \
  --account-name datacenterstor15117 \
  --account-key <access-key> \
  --container-name datacenter-container15117 \
  --output table
```

You should see:

```
testfile.txt
```

---

## ✅ Task Completion Checklist

✔ VM exists in East US
✔ Private storage account created (LRS)
✔ Private blob container created
✔ Storage access key retrieved
✔ Test file created on VM
✔ File successfully uploaded to Blob Storage

### 🌐 **Q4: Deploying a Static Website Using Containers on Azure**

> *Build a container image for a static HTML website, push it to Azure Container Registry (ACR), and deploy it on a Linux VM. Ensure it's publicly accessible and secured with HTTPS using a reverse proxy like Nginx inside the container. What are the pros and cons of using a VM vs App Service or Azure Container Apps for this use case?*

The Nautilus DevOps team has been tasked with creating an internal information portal for public access. As part of this project, they need to host a static website on Azure using an Azure Storage account. The Storage account must be configured for public access to allow external users to access the static website directly via the Azure Storage URL.

Task Requirements:

Create an Azure Storage account named datacenterwebst15998 in an existing resource group.
Configure the Storage account for static website hosting with index.html as the index document.
Allow public access to the static website so that the website is publicly accessible.
Upload the index.html file from the /root/ directory of the Azure client host to the Storage account's $web container.
Verify that the website is accessible directly through the Azure Storage static website URL.

Ans:
Perfect — here’s how to do the **same task using the Azure Portal (GUI)**, step by step.

---

## 1. Open Azure Portal

* Go to **[https://portal.azure.com](https://portal.azure.com)**
* Sign in with your Azure credentials

---

## 2. Create the Storage Account

1. In the left menu, click **Storage accounts**
2. Click **+ Create**

**Basics tab**

* **Subscription:** Select your subscription
* **Resource group:** Select the **existing resource group**
* **Storage account name:** `datacenterwebst15998`
* **Region:** Choose the required region (e.g., *East US*)
* **Performance:** Standard
* **Redundancy:** LRS

Click **Next**

---

## 3. Enable Public Access

1. Go to the **Advanced** tab
2. Set:

   * **Allow enabling anonymous access on individual containers:** ✅ **Enabled**

Click **Next → Next → Create**

Wait for deployment to finish, then click **Go to resource**

---

## 4. Enable Static Website Hosting

1. In the storage account menu, select **Data management → Static website**
2. Set:

   * **Static website:** **Enabled**
   * **Index document name:** `index.html`
3. Click **Save**

✔ Azure automatically creates the **$web** container
✔ You will see a **Primary endpoint** URL — this is your website URL

---

## 5. Upload `index.html` to `$web`

1. Go to **Data storage → Containers**
2. Click **$web**
3. Click **Upload**
4. Browse and select `/root/index.html`
5. Click **Upload**
az storage blob upload \
  --account-name datacenterwebst15998 \
  --container-name '$web' \
  --name index.html \
  --file /root/index.html \
  --auth-mode login
---

## 6. Verify Public Access

1. Go back to **Static website**
2. Copy the **Primary endpoint URL**

   * Example:

     ```
     https://datacenterwebst15998.z13.web.core.windows.net/
     ```
3. Open it in a browser (no login required)

You should see the contents of **index.html**.

---

## ✅ You’re Done!

✔ Storage account created
✔ Static website enabled
✔ Public access allowed
✔ File uploaded
✔ Website accessible publicly

If you want, next we can:

* Add a **custom domain**
* Enable **HTTPS**
* Troubleshoot **403 / 404 errors**

### 🔐 **Q5: Managing Secrets with Azure Key Vault**

> *You’re deploying a web application that requires secure access to a database connection string and API key. Store the secrets in Azure Key Vault and configure access policies. Integrate it with a VM or containerized application to fetch the secrets at runtime without hardcoding them. How would you automate rotation of secrets?*

The Nautilus DevOps team is focusing on improving their data security by using Azure Key Vault. Your task is to create a Key Vault with a key and manage the encryption and decryption of a pre-existing sensitive file using this key.

Specific Requirements:

Create a Key Vault:

Name the Key Vault datacenter-25022.
Set access policies to allow encryption and decryption operations.
Set Soft Delete retention to 7 days.
Create a Key:

Create a symmetric key named datacenter-key within the Key Vault for encryption and decryption operations.
Encrypt the Sensitive Data:

Use the key to encrypt the provided SensitiveData.txt file (located in /root/) on the azure-client host.
Base64 encode the ciphertext and save the encrypted version as EncryptedData.bin in the /root/ directory.
Verify Decryption:

Attempt to decrypt EncryptedData.bin and verify that the decrypted data matches the original SensitiveData.txt file.
Ensure that the Key Vault and key are correctly configured. The validation script will test your configuration by decrypting the EncryptedData.bin file using the key you created.

Ans:
Got it — you want to do **everything via the Azure Portal (GUI)**.
Below is the **exact GUI-only workflow** that matches the requirements and will pass validation.

---

# ✅ Azure Portal (GUI) Steps

## 1️⃣ Create the Key Vault

1. Open **Azure Portal**

2. Go to **Create a resource → Security → Key Vault**

3. Fill in **Basics**:

   * **Key vault name:** `xfusion-31365`
   * **Subscription:** your lab subscription
   * **Resource group:** select or create one
   * **Region:** same region as your VM (e.g., East US)
   * **Pricing tier:** Standard

4. Click **Next: Access configuration**

   * Select **Vault access policy**
   * Click **Next**
   * Edit Access policies and Check encrypt,decrypt,wrap and unwrap 
5. Click **Next: Networking**

   * Leave default (Public endpoint)

6. Click **Next: Advanced**

   * ✅ **Enable soft delete**
   * **Soft delete retention period:** `7` days
   * Leave purge protection **disabled** (unless required)

7. Click **Review + Create → Create**

---

## 2️⃣ Configure Access Policy (Encrypt / Decrypt)

1. Open **Key Vault → xfusion-31365**
2. Go to **Access policies**
3. Click **+ Create**
4. Under **Key permissions**, check:

   * ✅ Get
   * ✅ List
   * ✅ Encrypt
   * ✅ Decrypt
5. Click **Next**
6. Select **your identity**:

   * If using Azure CLI in the lab → select the **Service Principal**
7. Click **Next → Create**

⏳ Wait **1 minute** for permissions to apply.

---

## 3️⃣ Create the Key (GUI)

1. Inside **xfusion-31365**
2. Go to **Keys → + Generate/Import**
3. Choose:

   * **Create method:** Generate
   * **Key name:** `xfusion-key`
   * **Key type:** RSA
   * **Key size:** 2048
   * **Permitted operations:**

     * ✅ Encrypt
     * ✅ Decrypt
4. Click **Create**

---

## 4️⃣ Encrypt the Sensitive File (Portal + CLI)

> ⚠️ Encryption of files **cannot be done in the GUI**
> Azure Portal **only manages keys**, not file encryption.

Use CLI **only for crypto operation**:

```bash
az account show --query user

az keyvault set-policy   --name xfusion-31365   --spn above-command-gives-pricipal-name   --key-permissions encrypt decrypt wrapKey unwrapKey get list

az keyvault key encrypt \
  --vault-name xfusion-31365 \
  --name xfusion-key \
  --algorithm RSA-OAEP \
  --value "$(base64 /root/SensitiveData.txt)" \
| jq -r '.result' > /root/EncryptedData.bin
```

---

## 5️⃣ Decrypt & Verify

```bash
az keyvault key decrypt \
  --vault-name xfusion-31365 \
  --name xfusion-key \
  --algorithm RSA-OAEP \
  --value "$(cat /root/EncryptedData.bin)" \
| jq -r '.result' | base64 --decode > /root/DecryptedData.txt
```

Verify:

```bash
diff /root/SensitiveData.txt /root/DecryptedData.txt
```

---

# 🔑 Important Notes (GUI Reality Check)

| Task                      | GUI Possible     |
| ------------------------- | ---------------- |
| Create Key Vault          | ✅                |
| Set soft delete           | ✅                |
| Configure access policies | ✅                |
| Create key                | ✅                |
| Encrypt file              | ❌ (CLI required) |
| Decrypt file              | ❌ (CLI required) |

Azure Portal **does not encrypt files**, it only provides keys.

---

## ✅ What the validator checks

* Correct vault name
* Key exists
* Encrypt/decrypt permissions
* Ciphertext decrypts correctly

You are fully compliant with the GUI + minimal CLI approach.

If you want **screenshots mapping**, **RBAC-only GUI flow**, or **managed identity setup**, tell me 👍

### 📋 **Q6: Working with Azure Table Storage**

> *A lightweight, NoSQL-like solution is needed to store user activity logs with high write and moderate read patterns. Set up and integrate Azure Table Storage into your application. How do you design the partition/row key schema for optimal performance, and how do you query the data efficiently using SDK or REST API?*

The Nautilus DevOps team is developing a simple 'To-Do' application using Azure Table Storage to store and manage tasks efficiently. The team needs to create an Azure Table to hold tasks, each identified by a unique taskId. Each task will have a description and a status, which indicates the progress of the task (e.g., 'completed' or 'in-progress').

Your task is to:

Create an Azure Storage Account named datacentertablest24721 with a Table Storage table called tasks.
Insert the following tasks into the table:
Task 1: PartitionKey: 'tasks', RowKey: '1', description: 'Learn Table Storage', status: 'completed'
Task 2: PartitionKey: 'tasks', RowKey: '2', description: 'Build To-Do App', status: 'in-progress'
Verify that Task 1 has a status of 'completed' and Task 2 has a status of 'in-progress'.
Note: Use the Azure CLI to insert these tasks into the table.
Ans:
Here’s how to do **the same task using the Azure Portal (GUI)** — no CLI required.

---

## 1. Create the Storage Account

1. Sign in to **Azure Portal**
   👉 [https://portal.azure.com](https://portal.azure.com)

2. In the left menu, click **Storage accounts**

3. Click **➕ Create**

4. Fill in the **Basics** tab:

   * **Subscription**: Select your subscription
   * **Resource group**: Select existing or click **Create new**
   * **Storage account name**:

     ```
     datacentertablest24721
     ```
   * **Region**: Choose a nearby region (e.g., East US)
   * **Performance**: Standard
   * **Redundancy**: LRS

5. Click **Review + create**

6. Click **Create**

✅ Wait until deployment completes.

---

## 2. Create the Table (`tasks`)

1. Open the **datacentertablest24721** storage account
2. In the left pane, scroll to **Data storage**
3. Click **Tables**
4. Click **➕ Table**
5. Enter table name:

   ```
   tasks
   ```
6. Click **OK**

---
Use CLI to Insert .Azure new GUI disabled By defualt
Go storage account-->securityy+Networking --> access keys-->connection string
export AZURE_STORAGE_CONNECTION_STRING="<PASTE_CONNECTION_STRING_HERE>"

## 3. Insert Task 1

1. Click the **tasks** table

2. Click **➕ Add entity**

3. Enter:

   * **PartitionKey**: `tasks`
   * **RowKey**: `1`

4. Click **➕ Add property**

   * Name: `description`
   * Type: `String`
   * Value: `Learn Table Storage`

5. Click **➕ Add property**

   * Name: `status`
   * Type: `String`
   * Value: `completed`

6. Click **Insert**

# CLI: 
az storage entity insert   --table-name tasks   --entity PartitionKey=tasks RowKey=1 description="Learn Table Storage" status="completed"


---

## 4. Insert Task 2

1. In the **tasks** table, click **➕ Add entity**

2. Enter:

   * **PartitionKey**: `tasks`
   * **RowKey**: `2`

3. Add properties:

   * `description` → `Build To-Do App`
   * `status` → `in-progress`

4. Click **Insert**

---

## 5. Verify the Tasks

In the **tasks** table view:

* **Task 1**

  * RowKey: `1`
  * status: ✅ `completed`

* **Task 2**

  * RowKey: `2`
  * status: ✅ `in-progress`

You’ll see both entities listed directly in the table grid.
# CLI: 
az storage entity insert \
  --table-name tasks \
  --entity PartitionKey=tasks RowKey=2 description="Build To-Do App" status="in-progress"


# Verify Task 1 Status
az storage entity show \
  --table-name tasks \
  --partition-key tasks \
  --row-key 1

# Verify Task 2 Status:
az storage entity show \
  --table-name tasks \
  --partition-key tasks \
  --row-key 2

---

## ✅ Final Confirmation

* Storage Account: **datacentertablest24721**
* Table: **tasks**
* Task statuses verified correctly

If you want, I can also show how to:

* Edit or delete tasks in the GUI
* Export table data
* Connect this table to an app or Azure Function

### 🚀 **Q7: Deploying a Web Application from Repository on Azure**

> *You’ve built a Node.js web application and pushed it to a GitHub repo. Deploy this app to Azure App Service with continuous deployment enabled. Configure build and deployment settings, environment variables, and logging. How would you enable staging slots for testing before production rollout?*

You are tasked with modifying an ARM template for deploying a virtual network. The current template is located in the /root/arm-templates directory under the filename vnet-deployment-template.json. You need to make the following changes to the template:

Change the name and displayName tag of the virtual network to arm-vnet-nautilus.

Update the addressPrefixes to 192.168.0.0/16.

Add one more tag named Environment with value KKE-nautilus.

After making these changes, you need to deploy the ARM template using the Azure CLI.

Use the following command to find out the resource group to use:

az group list --query '[].name' --output table | grep 'kml'

Ans:
 Existing Arm:
 cat vnet-deployment-template.json 
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {},
    "functions": [],
    "variables": {},
    "resources": [
        {
            "name": "virtualNetwork1",
            "type": "Microsoft.Network/virtualNetworks",
            "apiVersion": "2023-11-01",
            "location": "[resourceGroup().location]",
            "tags": {
                "displayName": "virtualNetwork1"
            },
            "properties": {
                "addressSpace": {
                    "addressPrefixes": [
                        "10.10.10.0/24"
                    ]
                }
            }
        }
    ],
    "outputs": {
    }
}
To update your ARM template and deploy it correctly, follow the steps below. I have modified your JSON structure to include the specific naming, tags, and address space you requested.

### 1. Update the ARM Template

You should overwrite the contents of `/root/arm-templates/vnet-deployment-template.json` with the following code.

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {},
    "functions": [],
    "variables": {},
    "resources": [
        {
            "name": "arm-vnet-nautilus",
            "type": "Microsoft.Network/virtualNetworks",
            "apiVersion": "2023-11-01",
            "location": "[resourceGroup().location]",
            "tags": {
                "displayName": "arm-vnet-nautilus",
                "Environment": "KKE-nautilus"
            },
            "properties": {
                "addressSpace": {
                    "addressPrefixes": [
                        "192.168.0.0/16"
                    ]
                }
            }
        }
    ],
    "outputs": {}
}

```

---

### 2. Identify the Resource Group

Run this command in your terminal to find the exact name of the resource group containing "kml":

```bash
az group list --query '[].name' --output table | grep 'kml'

```

*Note: This will likely return a name like `kml-resource-group-123`. Copy this name for the next step.*

---

### 3. Deploy via Azure CLI

Run the following command to deploy the template. Replace `<YOUR_RESOURCE_GROUP>` with the name you found in step 2.

```bash
az deployment group create \
  --resource-group <YOUR_RESOURCE_GROUP> \
  --template-file /root/arm-templates/vnet-deployment-template.json

```

---

### Summary of Changes Made

| Field | Original Value | New Value |
| --- | --- | --- |
| **Name** | `virtualNetwork1` | `arm-vnet-nautilus` |
| **Tag: displayName** | `virtualNetwork1` | `arm-vnet-nautilus` |
| **Tag: Environment** | *None* | `KKE-nautilus` |
| **Address Prefixes** | `10.10.10.0/24` | `192.168.0.0/16` |

Would you like me to show you how to add a **Subnet** to this configuration before you deploy?
### ⚙️ **Q8: Configuring Azure VM with Application Gateway**

> *You want to expose a VM-hosted web application securely over HTTPS using Azure Application Gateway. Set up the gateway, configure backend pools, listeners, and rules. Add SSL termination and implement Web Application Firewall (WAF) policies. How do you verify traffic routing and troubleshoot if the VM is not responding?*

The Nautilus Development Team needs to set up a new Azure Virtual Machine (VM) and configure it to run a web server. This VM should be part of an Azure Application Gateway (AGW) setup to ensure high availability and better traffic management. The task involves creating a VM, setting up an AGW, configuring a backend pool, and ensuring the web server is accessible via the AGW public IP.

Create a Network Security Group (NSG): Create an NSG named nautilus-nsg and add an inbound security rule Allow-HTTP to allow TCP traffic on port 80.

Create a Virtual Machine: Create a VM named nautilus-vm using any available Ubuntu image. Configure the instance with the following settings:

Size: Choose a lightweight VM size (e.g., Standard_B1s).

Authentication: Use SSH public key authentication. (Please select use existing public key option, create public-key locally and paste contents of ~/.ssh/id_rsa.pub)

OS Disk: Use a Standard HDD.

Networking: Under the Advanced section, attach an existing NSG (e.g., nautilus-nsg).

Additionally, configure the instance to run a user data script during launch that:

Install the Nginx package.

Start the Nginx service.

Set up an Application Gateway: Set up an Azure Application Gateway named nautilus-agw with the following:

Create and Associate it with a public IP address named nautilus-agw-ip.

Attach the backend pool:nautilus-backendpool to the VM nautilus-vm.

Select a subnet for the Application Gateway (you can create a new one if needed).

Configure HTTP Settings: Create an HTTP setting named nautilus-http-settings on port 80

Route Traffic: Add a listener named nautilus-listener and a routing rule named nautilus-routing-rule to route traffic from the AGW frontend to the backend pool:

Listener: Frontend IP = public IP, Frontend port = 80, Protocol = HTTP

Routing rule: Connects nautilus-listener to nautilus-backendpool using nautilus-http-settings.

NSG Adjustments: Make sure the NSG attached to the VM allows inbound TCP traffic on port 80, so the Nginx server running on nautilus-vm is accessible via the Application Gateway public IP.

Note: Wait for the Application Gateway resource to be fully deployed before proceeding with the next steps. Deployment may take several minutes to complete.

Ans:
Below are **step-by-step Azure Portal (GUI) instructions** to complete the entire task exactly as described.

---

# 🔹 Step 1: Create Network Security Group (NSG)

1. Go to **Azure Portal** → **Network security groups**
2. Click **Create**

### Basics

* **Subscription**: Select yours
* **Resource group**: `nautilus-rg` (or existing)
* **Name**: `nautilus-nsg`
* **Region**: Same region as VM

Click **Review + Create** → **Create**

### Add Inbound Rule

1. Open **nautilus-nsg**
2. Go to **Inbound security rules**
3. Click **Add**

| Field                   | Value          |
| ----------------------- | -------------- |
| Source                  | Any            |
| Source port ranges      | *              |
| Destination             | Any            |
| Destination port ranges | **80**         |
| Protocol                | TCP            |
| Action                  | Allow          |
| Priority                | **100**        |
| Name                    | **Allow-HTTP** |

Click **Add**

---

# 🔹 Step 2: Create Virtual Machine (Ubuntu + Nginx)

1. Go to **Virtual machines** → **Create** → **Azure virtual machine**

## Basics Tab

* **Resource group**: `nautilus-rg`
* **Virtual machine name**: `nautilus-vm`
* **Region**: Same region
* **Image**: **Ubuntu Server LTS**
* **Size**: **Standard_B1s**

### Authentication

* **Authentication type**: SSH public key
* **Username**: `azureuser`
* **SSH public key source**: **Use existing public key**
* Paste contents of:

  ```bash
  ~/.ssh/id_rsa.pub
  ```

Click **Next: Disks**

---

## Disks Tab

* **OS disk type**: **Standard HDD**

Click **Next: Networking**

---

## Networking Tab

* **Virtual network**: Create new or select existing
* **Subnet**: Select VM subnet
* **Public IP**: Optional (not required for AGW access)
* **NIC network security group**: **Advanced**
* **Configure network security group**: **Existing**
* **Select NSG**: `nautilus-nsg`

Click **Next: Advanced**

---

## Advanced Tab (User Data Script)

Paste this into **Custom data**:

```bash
#!/bin/bash
apt update
apt install -y nginx
systemctl start nginx
systemctl enable nginx
```

Click **Review + Create** → **Create**

---

# 🔹 Step 3: Create Public IP for Application Gateway

1. Go to **Public IP addresses**
2. Click **Create**

| Field          | Value             |
| -------------- | ----------------- |
| Name           | `nautilus-agw-ip` |
| SKU            | **Standard**      |
| Assignment     | **Static**        |
| Resource group | `nautilus-rg`     |

Click **Create**

---

# 🔹 Step 4: Create Application Gateway

1. Go to **Application Gateways**
2. Click **Create**

## Basics

* **Name**: `nautilus-agw`
* **Region**: Same region
* **Tier**: **Standard V2**
* **Enable autoscaling**: No
* **Instance count**: 1
* **Resource group**: `nautilus-rg`

Click **Next: Frontends**

---

## Frontends

* **Frontend IP type**: Public
* **Public IP address**: `nautilus-agw-ip`

Click **Next: Backends**

---

## Backends

1. Click **Add a backend pool**
2. **Name**: `nautilus-backendpool`
3. **Target type**: Virtual machine
4. **Virtual machine**: `nautilus-vm`
5. **IP configuration**: Select VM NIC

Click **Add**

---

## Configuration (HTTP Settings + Rule)

Click **Add a routing rule**

### Listener

| Setting       | Value               |
| ------------- | ------------------- |
| Listener name | `nautilus-listener` |
| Frontend IP   | Public              |
| Protocol      | HTTP                |
| Port          | 80                  |

### Backend targets

| Setting       | Value                  |
| ------------- | ---------------------- |
| Backend pool  | `nautilus-backendpool` |
| HTTP settings | **Add new**            |

#### HTTP Settings

| Field                 | Value                    |
| --------------------- | ------------------------ |
| Name                  | `nautilus-http-settings` |
| Backend port          | 80                       |
| Protocol              | HTTP                     |
| Cookie-based affinity | Disabled                 |

Click **Add**

Click **Add routing rule**

---

## Networking (Subnet)

* **Virtual network**: Same VNet as VM
* **Subnet**: **Create new subnet**

  * Name: `agw-subnet`
  * Address range: e.g. `10.0.2.0/24`

---

Click **Review + Create** → **Create**

⏳ **Wait 5–10 minutes for deployment to complete**

---

# 🔹 Step 5: Verify NSG Configuration

Ensure `nautilus-nsg`:

* Has inbound **TCP 80 allowed**
* Is attached to **VM NIC or subnet**

---

# 🔹 Step 6: Test Web Access

1. Go to **Application Gateway → nautilus-agw**
2. Copy **Frontend public IP address**
3. Open browser:

```
http://<AGW_PUBLIC_IP>
```

✅ You should see the **Nginx Welcome Page**


### 📡 **Q9: Integrating Azure Event Hub with Virtual Machines**

> *A logging agent on your VM should forward application logs to Azure Event Hub for downstream processing. Set up Event Hub, configure the agent to send logs using SDK or Event Hub REST API, and monitor throughput. How would you handle retries, dead-lettering, and scaling the ingestion layer?*

The Nautilus DevOps team wants to integrate an Azure Virtual Machine with Azure Event Hubs for centralized log collection. Follow these steps to complete the task:

Create Azure Event Hubs Namespace:

Create an Event Hubs namespace named nautilus-namespace in the East US region.
Select the Standard pricing tier. Make sure to enable Enable Auto-inflate.
Create an Event Hub:

Within the namespace, create an Event Hub named nautilus-hub.
Verify the Virtual Machine Configuration:

A VM named nautilus-vm already exists.
A Python script named send_logs.py already exists on the VM under /home/azureuser. This script is used to send logs to the Event Hub. Make sure to execute this script mutiple times.
Verify Logs:

Ensure the logs are successfully sent to the Event Hub by checking the Event Hubs metrics in the Azure portal.

Ans:
Below is a **clear, end-to-end procedure** to integrate the existing **Azure VM** with **Azure Event Hubs** and verify centralized log collection. This assumes you have appropriate Azure permissions and CLI access.

---

## 1. Create Azure Event Hubs Namespace

### Using Azure Portal

1. Go to **Azure Portal → Create a resource → Analytics → Event Hubs**
2. Configure:

   * **Namespace name:** `nautilus-namespace`
   * **Region:** `East US`
   * **Pricing tier:** `Standard`
   * **Enable Auto-inflate:** ✅ Enabled
3. Click **Review + Create → Create**

---

### (Optional) Using Azure CLI

```bash
az eventhubs namespace create \
  --name nautilus-namespace \
  --resource-group <RESOURCE_GROUP> \
  --location eastus \
  --sku Standard \
  --enable-auto-inflate true
```

---

## 2. Create Event Hub inside the Namespace

### Azure Portal

1. Open **nautilus-namespace**
2. Select **Data Explorer → + Event Hub**
3. Configure:

   * **Name:** `nautilus-hub`
   * Leave other settings as default
4. Click **Create**

---

### Azure CLI (optional)

```bash
az eventhubs eventhub create \
  --resource-group <RESOURCE_GROUP> \
  --namespace-name nautilus-namespace \
  --name nautilus-hub
```

---

## 3. Configure Event Hub Access for the VM

1. In **nautilus-namespace → settings→ Shared access policies**
2. Select **RootManageSharedAccessKey** (or create a new policy)
3. Copy the **Primary Connection String**

⚠️ The `send_logs.py` script typically requires:

* Event Hub connection string
* Event Hub name

These are commonly provided via **environment variables**.

Example:

```bash
export EVENT_HUB_CONNECTION_STRING="<connection-string>"
export EVENT_HUB_NAME="nautilus-hub"
```

(Adjust based on how `send_logs.py` is written.)

---

## 4. Verify Virtual Machine & Execute Script

1. Connect to the VM:

```bash
ssh azureuser@<VM_PUBLIC_IP>
```

2. Navigate to the script location:

```bash
cd /home/azureuser
cat send_logs.py
```
# paste the connection string or export as environment variables


3. Run the script **multiple times**:

```bash
python3 send_logs.py
python3 send_logs.py
python3 send_logs.py
```

If the script executes without errors, logs are being sent.

---

## 5. Verify Logs in Azure Event Hubs

### Check Metrics in Azure Portal

1. Go to **nautilus-namespace → nautilus-hub**
2. Open **Metrics**
3. Add metrics such as:

   * **Incoming Messages**
   * **Incoming Bytes**
4. Set **Time range:** Last 30 minutes

✅ You should see metric values increase each time `send_logs.py` is executed.

---

## 6. Success Criteria Checklist

✔ Event Hubs namespace `nautilus-namespace` created in **East US**
✔ Pricing tier **Standard** with **Auto-inflate enabled**
✔ Event Hub `nautilus-hub` created
✔ `send_logs.py` executed multiple times on `nautilus-vm`
✔ Event Hub metrics show incoming messages

---

If you want, I can also:

* Review or troubleshoot `send_logs.py`
* Help configure **Azure Monitor / Log Analytics**
* Add **diagnostic settings** for long-term log storage

### ☸️ **Q10: Azure Kubernetes Service (AKS) Setup and Management**

> *Set up a production-ready AKS cluster with autoscaling and integrated ACR for image pulling. Deploy a multi-container app using Helm or YAML manifests, and secure it with ingress controller, TLS, and Azure AD Pod Identity. How do you enable observability with Prometheus/Grafana and handle secret injection securely in the cluster?*

**Level 4**

### 🛠️ **Q1: VM Setup and Configuration for Azure API Gateway**

> **Scenario:**
> You need to host a backend REST API on an Azure VM and expose it securely through **Azure API Management (APIM)** to external clients.
> **Question:**
> Set up an Azure Linux or Windows VM to host the REST API. Configure Azure API Management to act as a gateway in front of the VM. Implement rate limiting and IP whitelisting in APIM.
> How would you:

* Secure API access using subscription keys or OAuth2?
* Route traffic via a custom domain with HTTPS?
* Protect the VM with NSGs and restrict public access to only the APIM instance?

### 🔄 **Q2: EventHub to Blob Storage Integration Setup**

> **Scenario:**
> Your application pushes real-time sensor data to Azure Event Hub. You are required to archive this data automatically into Azure Blob Storage for analytics.
> **Question:**
> Configure Azure Event Hub Capture to store data directly into Blob Storage in AVRO format.
> How would you:

* Set up the storage container and policy securely?
* Ensure the Event Hub is partitioned for performance?
* Process AVRO data later using Azure Data Factory or Synapse?

### 🧭 **Q3: SQL Database Migration and Setup**

> **Scenario:**
> You’re tasked with migrating a large on-premises SQL Server database to **Azure SQL Database** with minimal downtime.
> **Question:**
> Plan and implement the migration using **Data Migration Assistant (DMA)** or **Azure Database Migration Service (DMS)**.
> How would you:

* Assess compatibility and resolve issues?
* Ensure replication for near-zero downtime cutover?
* Implement firewall and VNet rules to restrict access to the new database?

### 📦 **Q4: VM and ACR Integration for Storage**

> **Scenario:**
> Your organization uses Docker to package applications. You need to run these containers on Azure VMs and store the images in **Azure Container Registry (ACR)**.
> **Question:**
> Deploy a Linux VM with Docker installed and connect it to ACR securely.
> How would you:

* Authenticate the VM using a service principal or managed identity?
* Pull and run an image on VM startup using a custom script?
* Ensure ACR access logs and image scanning are enabled?

### 🌐 **Q5: VM Setup with Web Storage Integration**

> **Scenario:**
> You’re deploying a web application on a VM that stores user-uploaded files in **Azure Blob Storage**.
> **Question:**
> Provision the VM, install the web app, and configure it to store all uploads in Blob Storage using a storage account key or SAS.
> How would you:

* Secure the storage connection (Key Vault vs environment variables)?
* Scale storage access using a private endpoint or VNet service endpoint?
* Handle failures when Blob Storage is unreachable?
