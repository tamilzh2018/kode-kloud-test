**Level 1**
# Q1 Set Up Git Repository on Storage Server
The Nautilus development team has provided requirements to the DevOps team for a new application development project, specifically requesting the establishment of a Git repository. Follow the instructions below to create the Git repository on the Storage server in the Stratos DC:

Utilize yum to install the git package on the Storage Server.

Create a bare repository named /opt/media.git (ensure exact name usage).

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

# Q2 Clone Git Repository on Storage Server
The DevOps team established a new Git repository last week, which remains unused at present. However, the Nautilus application development team now requires a copy of this repository on the Storage Server in the Stratos DC. Follow the provided details to clone the repository:

The repository to be cloned is located at /opt/news.git

Clone this Git repository to the /usr/src/kodekloudrepos directory. Perform this task using the natasha user, and ensure that no modifications are made to the repository or existing directories, such as changing permissions or making unauthorized alterations.

Ans:
Ensure the target directory exists (create it if needed), then clone the repository:

mkdir -p /usr/src/kodekloudrepos

cd /usr/src/kodekloudrepos
git clone /opt/news.git

# Q3 Fork a Git Repository
# Q4 Update Git Repository with Sample HTML File
# Q5 Delete Git Branch
**Level 2**
# Q1 Git Install and Create Repository
# Q2 Git Create Branches
# Q3 Git Merge Branches
# Q4 Git Manage Remotes
# Q5 Git Revert Some Changes
**Level 3**
# Q1 Git Cherry Pick
# Q2 Manage Git Pull Requests
# Q3 Git hard reset
# Q4 Git Clean
# Q5 Git Stash
**Level 4**
# Q1 Git Rebase
# Q2 Manage Git Repositories
# Q3 Resolve Git Merge Conflicts
# Q4 Git Hook
# Q5 Git Setup from Scratch