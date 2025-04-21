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