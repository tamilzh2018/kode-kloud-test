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
The Nautilus application development team has been working on a project repository /opt/news.git. This repo is cloned at /usr/src/kodekloudrepos on storage server in Stratos DC. They recently shared the following requirements with DevOps team:

Create a new branch datacenter in /usr/src/kodekloudrepos/news repo from master and copy the /tmp/index.html file (present on storage server itself) into the repo. Further, add/commit this file in the new branch and merge back that branch into master branch. Finally, push the changes to the origin for both of the branches.
Ans:
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
# Q4 Git Manage Remotes
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
# Q5 Git Revert Some Changes
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
**Level 3**
# Q1 Git Cherry Pick
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
# Q2 Manage Git Pull Requests
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

# Q3 Git hard reset
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
# Q4 Git Clean
The Nautilus application development team was working on a git repository /usr/src/kodekloudrepos/blog present on Storage server in Stratos DC. One of the developers mistakenly created a couple of files under this repository, but now they want to clean this repository without adding/pushing any new files. Find below more details:

Clean the /usr/src/kodekloudrepos/blog git repository without adding/pushing any new files, make sure git status is clean.
Ans:
Let's go step-by-step so you can **clean the Git repository** at `/usr/src/kodekloudrepos/blog` and make sure `git status` shows a **clean working tree** (no changes, untracked files, or pending commits).

---

### 🧭 Step 1: Navigate to the repository

```bash
cd /usr/src/kodekloudrepos/blog
```

---

### 🧹 Step 2: Check the current status

```bash
git status
```

This will show you:

* Untracked files (not yet added to git)
* Modified files (already tracked but changed)
* Anything staged for commit

You’ll probably see something like:

```
Untracked files:
  (use "git add <file>..." to include in what will be committed)
    file1.txt
    file2.log
```

---

### 🗑️ Step 3: Remove **untracked files and directories**

You can safely clean out all files that are not tracked by git (i.e., those that were mistakenly created):

```bash
git clean -fd
```

Explanation:

* `-f` = force (required for safety)
* `-d` = also remove untracked directories

This will **delete all untracked files and folders**.

> ⚠️ **Warning:** This permanently deletes those files from disk (not to trash). Only run this if you’re sure they’re not needed.

---

### 🔁 Step 4: Discard any changes to tracked files

If the developer also modified existing tracked files, revert them to their last committed version:

```bash
git restore .
```

or the older equivalent:

```bash
git checkout -- .
```

---

### ✅ Step 5: Confirm the repository is clean

Finally, verify that the working tree is clean:

```bash
git status
```

You should now see:

```
On branch main
nothing to commit, working tree clean
```

# Q5 Git Stash
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
**Level 4**
# Q1 Git Rebase
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

# Q2 Manage Git Repositories
A new developer just joined the Nautilus development team and has been assigned a new project for which he needs to create a new repository under his account on Gitea server. Additionally, there is some existing data that need to be added to the repo. Below you can find more details about the task:

Click on the Gitea UI button on the top bar. You should be able to access the Gitea UI. Login to Gitea server using username max and password Max_pass123.

a. Create a new git repository story_ecommerce under max user.

b. SSH into storage server using user max and password Max_pass123 and clone this newly created repository under user max home directory i.e /home/max.

c. Copy all files from location /usr/itadmin to the repository and commit/push your changes to the master branch. The commit message must be "add stories" (must be done in single commit).

d. Create a new branch max_games from master.

e. Copy a file story-index-max.txt from location /tmp/stories/ to the repository. This file has a typo, which you can fix by changing the word Mooose to Mouse. Commit and push the changes to the newly created branch. Commit message must be "typo fixed for Mooose" (must be done in single commit).

Note: For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.

Ans:
Here's a step-by-step guide to help the new developer complete the task successfully:

---

### 🧩 Step-by-Step Instructions

#### 1️⃣ Create a New Repository in Gitea
- Go to the Gitea UI by clicking the **Gitea** button on the top bar.
- Log in with:
  - **Username:** `max`
  - **Password:** `Max_pass123`
- Click **New Repository**.
- Fill in the details:
  - **Repository Name:** `story_ecommerce`
  - **Owner:** `max`
  - Leave other settings as default (public/private as needed).
- Click **Create Repository**.

#### 2️⃣ SSH into the Storage Server and Clone the Repo
- Open a terminal and SSH into the storage server:
  ```bash
  ssh max@<storage-server-ip>
  ```
  - Use password: `Max_pass123`
- Navigate to the home directory:
  ```bash
  cd /home/max
  ```
- Clone the newly created repository:
  ```bash
  git clone git@<gitea-server>:max/story_ecommerce.git
  ```

---

#### 3️⃣ Copy Existing Data and Commit to Master
- Copy all files from `/usr/itadmin`:
  ```bash
  cp -r /usr/itadmin/* /home/max/story_ecommerce/
  cd /home/max/story_ecommerce
  ```
- Stage and commit the changes:
  ```bash
  git config --global user.name "max"
  git config --global user.email "max@stratos.xfusioncorp.com"
  git add .
  git commit -m "add stories"
  git branch --set-upstream-to=origin/master master
  git push origin master
  ```

---

#### 4️⃣ Create a New Branch `max_games`
- From the repo directory:
  ```bash
  Create new branch on remote repo and then locally pull that
  git checkout -b max_games
  git push origin max_games
  ```

---

#### 5️⃣ Fix Typo in `story-index-max.txt` and Commit to `max_games`
- Copy the file:
  ```bash
  cp /tmp/stories/story-index-max.txt /home/max/story_ecommerce/
  ```
- Fix the typo using `sed`:
  ```bash
  sed -i 's/Mooose/Mouse/g' story-index-max.txt
  ```
- Stage and commit:
  ```bash
  git add story-index-max.txt
  git commit -m "typo fixed for Mooose"
  git push origin max_games
  ```
# Q3 Resolve Git Merge Conflicts
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
# Q4 Git Hook
The Nautilus application development team was working on a git repository /opt/beta.git which is cloned under /usr/src/kodekloudrepos directory present on Storage server in Stratos DC. The team want to setup a hook on this repository, please find below more details:

Merge the feature branch into the master branch`, but before pushing your changes complete below point.

Create a post-update hook in this git repository so that whenever any changes are pushed to the master branch, it creates a release tag with name release-2023-06-15, where 2023-06-15 is supposed to be the current date. For example if today is 20th June, 2023 then the release tag must be release-2023-06-20. Make sure you test the hook at least once and create a release tag for today's release.

Finally remember to push your changes.
Note: Perform this task using the natasha user, and ensure the repository or existing directory permissions are not altered.

Ans:
To complete this task as the `natasha` user on the Storage server in Stratos DC, follow these steps carefully:

---

### ✅ Step-by-Step Instructions

#### 1. **Switch to the `natasha` user**
```bash
sudo su - natasha
```

#### 2. **Navigate to the cloned repository**
```bash
cd /usr/src/kodekloudrepos
```

#### 3. **Merge the feature branch into master**
Assuming the feature branch is named `feature`:
```bash
git checkout master
git merge feature
```

#### 4. **Create the `post-update` hook**
Git hooks are stored in `.git/hooks`. Create a `post-update` hook that tags the latest commit on `master` with today’s date.

```bash
 vi /opt/beta.git/hooks/post-update
 #!/bin/bash
BRANCH=$(git for-each-ref --format='%(refname:short)' refs/heads/master)
if [ "$BRANCH" = "master" ]; then
  DATE=$(date +%F)
  TAG="release-$DATE"
  git tag "$TAG" master
  echo "Created tag: $TAG"
fi

chmod +x /opt/beta.git/hooks/post-update

```

#### 5. **Test the hook**
Push the merged changes to trigger the hook:
```bash
cd /usr/src/kodekloudrepos
git push origin master

```

Then verify the tag was created:
```bash
cd /opt/beta.git
git tag

```

You should see a tag like:
```
release-2025-10-31
```

# Q5 Git Setup from Scratch

**Certification Test**
# Q1:
A developer was in the process of creating repositories on the Gitea server. Unfortunately, one repository was mistakenly created and now needs to be deleted. Below are further details regarding this issue.


The repository name is story-blog-t1q1 and is located under the sarah user on the Gitea server. The Gitea login credentials are as follows:

Username: sarah
Password: S3cure321
Ans:

### 🧾 Steps to Delete the Repository via Gitea Web Interface

1. **Log in to Gitea**:
   - Open your Gitea server in a browser.
   - Use the credentials:
     - **Username**: `sarah`
     - **Password**: `S3cure321`

2. **Navigate to the Repository**:
   - Go to: `https://http://git.stratos.xfusioncorp.com/sarah/story-blog-t1q1`
  
3. **Open Repository Settings**:
   - Click the **Settings** tab at the top of the repository page.

4. **Scroll to Danger Zone**:
   - At the bottom of the settings page, find the **Danger Zone** section.

5. **Delete the Repository**:
   - Click **Delete this repository**.
   - Confirm the deletion by typing the repository name when prompted.

# Q2:
Recently a bare repository was created by one of the developers. Now, they were planning to add some content in this repository so this needs to be cloned somewhere so that one of the developers can start adding data in it. Below you can find more details.


Clone the repository /opt/story-blog-t1q11.git under sarah user's home on storage server.

Use below credentials to SSH into the storage server and to complete this task.

Username: sarah
Password: S3cure321
Ans:
### 🛠️ Steps to Clone the Repository

1. **SSH into the Storage Server**:
   Open a terminal and run:
   
   ssh sarah@<storage-server-ip>
   
   When prompted, enter the password: `S3cure321`

2. **Navigate to Home Directory**:
   Once logged in:
   
   cd ~
   

3. **Clone the Bare Repository**:
   Run the following command:
   
   git clone /opt/story-blog-t1q11.git story-blog-t1q11
   
   This will create a working copy of the repository named `story-blog-t1q11` in the home directory.

4. **Verify the Clone**:
   Check the contents:
   
   cd story-blog-t1q11
   ls -la
   
# Q3:
Commit the change of file lion-and-mouse-t1q6.txt which is placed under /home/sarah/story-blog-t1q6 repository on Storage server, file is already staged. A commit records the change in the repository compared to its previous state. But before that we must configure the git user who will be the owner of the commit.


Set git username as sarah and user email as sarah@example.com using the below commands.

git config user.email sarah@example.com
git config user.name sarah

Use below credentials to SSH into the storage server and to complete this task.

Username: sarah
Password: S3cure321
Ans:

### 🛠️ Step-by-Step Instructions

1. **SSH into the Storage Server**:
   
   ssh sarah@<storage-server-ip>
   
   Enter the password: `S3cure321`

2. **Navigate to the Repository**:
   
   cd /home/sarah/story-blog-t1q6
   

3. **Configure Git User Info**:
   
   git config user.name "sarah"
   git config user.email "sarah@example.com"
# incase if wrongly mentioned email or username
   git config --global --unset user.email

   

4. **Commit the Staged File**:
   Since the file is already staged, run:
   
   git commit -m "Add lion-and-mouse-t1q6.txt"
   

5. **Verify the Commit**:
   
   git log --oneline
   
   This will show the latest commit confirming the change was recorded.

# Q4: 
A new repository named /usr/src/kodekloudrepos/media-t2q5 was created recently and some data was added in it. Now one of the developers wanted to use this repository further to add/update some data.

Checkout the master branch under repo /usr/src/kodekloudrepos/media-t2q5.

Use below credentials to SSH into the storage server and to complete this task.

Username: sarah
Password: S3cure321
Ans:
### 🛠️ Step-by-Step Instructions

1. **SSH into the Storage Server**:
   
   ssh sarah@<storage-server-ip>
   
   Enter the password: `S3cure321`

2. **Navigate to the Repository**:
   
   cd /usr/src/kodekloudrepos/media-t2q5
   

3. **Check Out the Master Branch**:
   
   git checkout master
   

4. **Verify the Branch**:
   Confirm you're on `master`:
   
   git branch
   
   The current branch will be marked with an asterisk (`*`).

# Q5
The Nautilus application development team has been working on a project repository /opt/media-t2q3.git. This repo is cloned at /usr/src/kodekloudrepos/media-t2q3 on storage server in Stratos DC. They recently shared the following requirements with DevOps team:


Create a new branch devops-t2q3 in /usr/src/kodekloudrepos/media-t2q3 repo from master and copy the /tmp/index-t2q3.html file (present on storage server itself) into the repo. Further, add/commit this file in the new branch and merge back that branch into master branch. Finally, push the changes to the origin for both of the branches.

Use below credentials to SSH into the storage server and to complete this task.

Username: sarah
Password: S3cure321

Ans:
### 🛠️ Task Summary
- Create a new branch `devops-t2q3` from `master`
- Copy `/tmp/index-t2q3.html` into the repo
- Add and commit the file in the new branch
- Merge `devops-t2q3` into `master`
- Push both branches to origin

### 📋 Step-by-Step Instructions

1. **SSH into the Storage Server**:
   
   ssh sarah@<storage-server-ip>
   
   Enter password: `S3cure321`

2. **Navigate to the Repository**:
   
   cd /usr/src/kodekloudrepos/media-t2q3
   

3. **Ensure You're on Master Branch**:
   
   git checkout master
   

4. **Create and Switch to New Branch**:
   
   git checkout -b devops-t2q3
   

5. **Copy the HTML File into the Repo**:
   
   cp /tmp/index-t2q3.html .
   

6. **Add and Commit the File**:
   
   git add index-t2q3.html
   git commit -m "Add index-t2q3.html to devops-t2q3 branch"
   

7. **Switch Back to Master and Merge**:
   
   git checkout master
   git merge devops-t2q3
   

8. **Push Both Branches to Origin**:
   
   git push origin master
   git push origin devops-t2q3
   

