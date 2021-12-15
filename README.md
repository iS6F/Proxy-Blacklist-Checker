# Proxy-Blacklist-Checker
Minimal script thats checks if multiple proxys are blacklisted from websites via "www.xmyip.com" with the power of bs4 and requests in under 35 lines
the program in the current state is slow due to the "www.xmyip.com" website but i might update it in the future and add multi-poccessing and maybe change the source website

using it is pretty simple, you need a config folder within it 3 files
```
[ips.txt, whitelisted.txt, blacklisted.txt]
```
after adding the folder and the files, (or make the python file do it), simply add the proxys in a ``ip:port`` style within a list, simply run the file after that and if you are unhappy with the blacklist accuracy change the if argument to fit the accuracy you want like shown here :
