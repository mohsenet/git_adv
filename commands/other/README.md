### other git adventure


```bash
# If you add following lines in .gitignore :
#
# >>>>>    **/ = Match in any directory (recursive subdirectories).    <<<<<
# **/node_modules/                 ==> Directory
# **/node_modules  (No Trailing /) ==> Directory and Files
```

```bash
# Check if a path is ignored:
git check-ignore -v path/to/node_modules
```

#### push an existing repository from the command line
```bash
git remote add origin https://github.com/mohsenet/fastapi-next-demo.git
git branch -M main
git push -u origin main
```
