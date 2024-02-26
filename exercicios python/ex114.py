import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print ('\033[31mDeu erro!\033[m')
else:
    print ('Tudo ok!')