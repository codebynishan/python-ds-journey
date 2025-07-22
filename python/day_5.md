# Learn about github
## Create Github Account
Visit [github](https://github.com) and create account.
- Create New Repo
---
# Local setup
## Install
Open Terminal
- brew install git (macOS)
- git --version
---
### Using SSH setup
```bash
ssh-keygen -C "your.email@example.com"
```
This will save key into default location `~/.ssh/your_user`

### Copy the SSH Public key
```bash
cat `~/.ssh/id_ed25519.pub`
```

### Add the SSH Key to GitHub
1. Go to GitHub Settings → SSH and GPG Keys.
2. Click New SSH Key.
3. Give it a title (e.g., "My Laptop").
4. Paste the copied public key (id_ed25519.pub) into the "Key" field.
5. Click Add SSH Key.

### Test the SSH Connection
```bash
ssh -T git@github.com
```




## Config Git
Open Terminal
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
## Init local repo
```bash
mkdir example-dir
cd example-dir
git init
```
## Add and commit files
```bash
git add .
git commit -m "message on commit"
```

## Add Remote url
```bash
git remote add origin <remote_url>
```
## Push Changes to Github
```bash
git push -u origin main 
```

# Cloning the repo
```bash
git clone <repo_url>
```

## Creating new Branch 
```bash
git branch -M branch_name
```
## Push new Branch
```bash
git push -u origin branch_name
```





hello worldhello world....
 This is from file handling