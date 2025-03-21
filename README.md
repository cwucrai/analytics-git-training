# analytics-git-training

A repository for practicing Git and GitHub workflows within our team.

## Git Workflow Guide

### 1. Clone the Repository using SSH

```bash
git clone git@github.com:YourOrganization/analytics-git-training.git
cd analytics-git-training
```

### 2. Create a Local Branch

Option 1: Create a branch and stay on your current branch
```bash
git branch my-feature-branch
```

Option 2: Create a branch and switch to it in one command
```bash
git checkout -b my-feature-branch
```

### 3. Publish Your Branch to GitHub

After making and committing your changes locally, push your branch to GitHub:

```bash
git push -u origin my-feature-branch
```

The `-u` (or `--set-upstream`) flag sets up tracking, so next time you can simply use `git push`.

### 4. Fetch and Checkout Someone Else's Branch

First, fetch all remote branches:
```bash
git fetch origin
```

Then checkout their branch:
```bash
git checkout origin/their-branch-name
```

If you want to make changes to their branch, create a local tracking branch:
```bash
git checkout -b their-branch-name origin/their-branch-name
```

## Additional Tips

- Always pull the latest changes before starting new work: `git pull origin main`
- Create descriptive branch names (e.g., `feature/add-login`, `bugfix/fix-header`)
- Use meaningful commit messages that explain the why, not just the what