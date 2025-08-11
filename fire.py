#!/data/data/com.termux/files/usr/bin/python
import platform,os
import requests
import bs4
import faker
import fake_email
#####
os.system("git pull")

bit = platform.architecture()[0]
if bit == '64bit':
    import newwww
elif bit == '32bit':
    import newwww
