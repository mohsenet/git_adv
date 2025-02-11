## Use_SSH_over_HTTPS_port.

### Step 1

Configure SSH to connect over port 443
```bash
touch ~/.ssh/config
vi ~/.ssh/config
```

### Step 2

Add following config
```bash
Host github.com
Hostname ssh.github.com
Port 443
```

### Step 3

Debug the SSH connection with following command
```bash
ssh -vT git@github.com
```

### Step 4

Now you can use SSH over HTTPS port
```bash
git clone git@github.com:mohsenet/your_repo.git
```

