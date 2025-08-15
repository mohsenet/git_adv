## How to generate public key and add it to github or gitlab.

### Quick Step
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### Step 1

Default ssh key path
```bash
cd ~/.ssh/
```

### Step 2

After run following command you can find public key (id_ed25519.pub) in the above path.
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

### Step 3

After that add your public key on your github or gitlab.
```bash
sudo apt install xclip
```
`xclip -sel clip file_name`
```bash
xclip -sel clip ~/.ssh/id_ed25519.pub
```

### Step 4

Update your Git repository to use SSH instead of HTTPS.
```bash
git remote set-url origin git@github.com:mohsenet/my_git_adventures.git
```

### Step 5

Enter the following command for the first time.
```bash
git push -u origin main
```

### Step 6

Next time, the following command will be enough.
```bash
git push
```

Now you can use it passwordless to connect and push to the server.
