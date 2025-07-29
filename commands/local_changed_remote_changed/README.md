## How to merge that when local and remote changed?

Pull and merge the remote changes
```bash
git pull origin main --no-rebase
```

Commit
```bash
# If there's a merge conflict:
#   - Edit the conflicting files, resolve them
#   - Then run:
git add .
git commit -m "Merge remote changes into local branch"
```

Now push your combined changes
```bash
git push origin main
```
