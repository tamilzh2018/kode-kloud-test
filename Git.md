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
There is a Git server utilized by the Nautilus project teams. Recently, a new developer named Jon joined the team and needs to begin working on a project. To begin, he must fork an existing Git repository. Follow the steps below:

Click on the Gitea UI button located on the top bar to access the Gitea page.

Login to Gitea server using username jon and password Jon_pass123.

Once logged in, locate the Git repository named sarah/story-blog and fork it under the jon user.

Note: For tasks requiring web UI changes, screenshots are necessary for review purposes. Additionally, consider utilizing screen recording software such as loom.com to record and share your task completion process.
Ans:
login and choose specific repo and fork
# Q4 Update Git Repository with Sample HTML File
The Nautilus development team has initiated a new project development, establishing various Git repositories to manage each project's source code. Recently, a repository named /opt/media.git was created. The team has provided a sample index.html file located on the jump host under the /tmp directory. This repository has been cloned to /usr/src/kodekloudrepos on the storage server in the Stratos DC.

Copy the sample index.html file from the jump host to the storage server placing it within the cloned repository at /usr/src/kodekloudrepos/media.

Add and commit the file to the repository.

Push the changes to the master branch.
Ans:

**Secure Copy from Jump to to Storage Server**
     scp /tmp/index.html storage_user@storage_server:/usr/src/kodekloudrepos/media/
     git status
     git add index.html 
     git commit -m "index.html added"
     git branch
     git push origin master
# Q5 Delete Git Branch
The Nautilus developers are engaged in active development on one of the project repositories located at /usr/src/kodekloudrepos/cluster. During testing, several test branches were created, and now they require cleanup. Here are the requirements provided to the DevOps team:

On the Storage server in Stratos DC, delete a branch named xfusioncorp_cluster from the /usr/src/kodekloudrepos/cluster Git repository.
Ans:
**local branch**: git branch -d xfusioncorp_cluster
**If the branch hasn't been merged and you still want to delete it**: git branch -D xfusioncorp_cluster
**Deleting a remote branch**: git push origin --delete xfusioncorp_cluster

**Level 2**
# Q1 Git Install and Create Repository
To fulfill the request for setting up a Git repository on the Storage server in Stratos DC, follow these steps:

### 🛠️ Step 1: Install Git using `yum`
Log into the Storage server and run:

sudo yum install git -y

This installs Git and its dependencies.

### 📁 Step 2: Create and Initialize the Git Repository
Now, create the directory and initialize the Git repository:

sudo mkdir -p /opt/cluster.git
cd /opt/cluster.git
sudo git init

> ⚠️ **Important:** Do **not** use `git init --bare` — this must be a standard (non-bare) repository.

### ✅ Verification
To confirm the repository was initialized correctly, run:

git status

# Q2 Git Create Branches
Nautilus developers are actively working on one of the project repositories, /usr/src/kodekloudrepos/news. Recently, they decided to implement some new features in the application, and they want to maintain those new changes in a separate branch. Below are the requirements that have been shared with the DevOps team:

On Storage server in Stratos DC create a new branch xfusioncorp_news from master branch in /usr/src/kodekloudrepos/news git repo.

Please do not try to make any changes in the code.
Ans:
To create a new branch named `xfusioncorp_news` from the `master` branch in the `/usr/src/kodekloudrepos/news` Git repository on the Storage server in Stratos DC, follow these steps:

1. **SSH into the Storage server** (assuming you have access):
   
   ssh <your-user>@<storage-server-ip>
   
2. **Navigate to the repository directory**:
   
   cd /usr/src/kodekloudrepos/news
   
3. **Ensure you're on the `master` branch and it's up to date**:
   
   git checkout master
   git pull origin master
   
4. **Create the new branch `xfusioncorp_news` from `master`**:
   
   git checkout -b xfusioncorp_news
   
5. **Push the new branch to the remote repository**:
   
   git push origin xfusioncorp_news
   
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