## Create Branch

### Create branch, work on your task, push it, and create a pull request on github web ui
```bash
# Clone the entire repository
git clone https://github.com/mohsenet/your-project.git
cd your-project

# Make sure you have the latest changes from the main branch
git checkout main
git pull origin main

# Create a new branch for your specific task
git checkout -b feature/user-authentication

# Work on your files and make commits as needed
# ... Make your code changes ...
git add path/to/changed/files
git commit -m "Implement user authentication form"

# ... Make more changes ...
git add path/to/more/changed/files
git commit -m "Add password validation"

# Push your feature branch to the remote repository
git push -u origin feature/user-authentication

# When done, go to your Git hosting platform (GitHub, GitLab, etc.)
# and create a pull request from your feature branch to the main branch
```


### reviewers can check out your branch locally
```bash
git fetch origin
git checkout feature/user-authentication
```

