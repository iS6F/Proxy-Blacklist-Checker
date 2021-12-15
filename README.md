# Proxy Blacklist Checker
Minimal script thats checks if multiple proxys are blacklisted from websites via "www.xmyip.com" with the power of bs4 and requests in under 35 lines
the program in the current state is slow due to the "www.xmyip.com" website but i might update it in the future and add multi-poccessing and maybe change the source website

using it is pretty simple, you need a config folder within it 3 files
```
[ips.txt, whitelisted.txt, blacklisted.txt]
```
after adding the folder and the files, (or make the python file do it), simply add the proxys in a ``ip:port`` style within a list, simply run the file after that and if you are unhappy with the blacklist accuracy change the if argument to fit the accuracy you want like shown here :
```py
    if nl < 50: #change the 50 to a higher number, 54 is 100% accuracy
        print(f'{cw}[{cp}{ip}{cw}] {cw}[{cr}Blacklisted{cw}]')
        with open(f'{path}\\config\\blacklisted.txt', 'a') as bl:
            bl.write(f'{ipport}\n')
    elif nl >= 50: # also change it here
        print(f'{cw}[{cp}{ip}{cw}] {cw}[{cg}Whitelisted{cw}]')
        with open(f'{path}\\config\\whitelisted.txt', 'a') as wl:
            wl.write(f'{ipport}\n')
```
you can remove colors to make it more minimal or even add multi-poccesing yourself do whatever you like :)
