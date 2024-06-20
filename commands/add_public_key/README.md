## How to generate public key and add it to github or gitlab.

### Step 1

Default ssh key path
```bash
cd ~/.ssh/
```

### Step 2

After run following command you can find public key (id_ed25519.pub) in the above path
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

### Step 3

After that add your public key on your github or gitlab

### Step 4

Update your Git repository to use SSH instead of HTTPS
```bash
git remote set-url origin git@github.com:mohsenet/my_git_adventures.git
```

### Step 5

Enter the following command for the first time
```bash
git push -u origin main
```

### Step 6

Next time, the following command is enough
```bash
git push
```

Now you can uset it passwordless to connect and push to server
