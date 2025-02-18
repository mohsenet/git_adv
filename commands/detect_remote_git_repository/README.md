## Detect Remote Git Repository

### Method 1

For detect remote git repository, we can use following command.
```bash
git remote -v
```

### Method 2

You can also find it in 'config' file in the '[remote "origin"]' section.
```bash
[remote "origin"]
    url = https://github.com/username/repository.git
    fetch = +refs/heads/*:refs/remotes/origin/*
```

