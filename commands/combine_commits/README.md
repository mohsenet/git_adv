## combine the three commits into a single commit

### 1
```bash
git rebase -i HEAD~3
    pick commit_1
    squash commit_2
    squash commit_3
git push --force
```

### If you set the wrong 'pick' and 'squash', use the following command:
```bash
git rebase --edit-todo
git rebase --continue
```
