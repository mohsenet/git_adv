## How to generate public key and it to github or gitlab.


~/.ssh/
After run following command you can find public key (id_ed25519.pub) in the above path
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

After that add your public key on github or gitlab

Update your Git repository to use SSH instead of HTTPS
```bash
git remote set-url origin git@github.com:mohsenet/my_git_adventures.git
```

Enter the following command the first time
```bash
git push -u origin main
```

Next time, the following command is enough
```bash
git push
```

Now you can uset it passwordless to connect and push to server
