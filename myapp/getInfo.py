from urllib.request import urlopen
from bs4 import BeautifulSoup
#import subprocess
import dns.resolver
from dns.exception import DNSException
from dns.resolver import Resolver



def getinfo(url):
    info = []
    info.append("<p>")
    meta_info = get_data(url)
    if meta_info[0]:
        temp = "<div style = 'color: green;'>~ The META tag is present: ✔ </div>"
        info.append(temp)
        if meta_info[2]:
            info.append("<div style = 'color: orange;'>~ Meta title is:<i> " + str(meta_info[2]) + "</i></div>")
        if meta_info[1]:
            temp = "<b>~<u> with content for meta tag as:</u><br><i>&#34; " + str(meta_info[1] + " &#34;</b></i>")
            info.append(temp)
        else:
            info.append("<div style = 'color: red;'>~ Meta tag does not contain any content information! 😢</div>")
    else:
        info.append("<div style = 'color: red;'>~ Meta tag is not present. 😔 </div>")
    info.append("."*80 + "</p><p>")
    #Dns Look up
    ul = make_url(url)
    dns_info = dns_lookup(ul)
    info.append(ul)
    if dns_info[0]:
        temp = "<div style = 'color: green;'>~ DNS TXT file exists. 😊</div>"
        info.append(temp)
        info.append("<div style = 'color: purple;'>~ with TXT read as:</div> <i>")
        for i in dns_info[0]:
            info.append("> " + i.to_text() + "</i>")
    elif dns_info[1]:
        temp = "<div style = 'color: red;'>~ DNS TXT file not found. </div> 😥"
        info.append(temp)
        info.append(dns_info[1])
    else:
        info.append("~ DNS TXT file Not Found! ¯\_(ツ)_/¯")
    
    info.append("</p>")
    return info

def dns_lookup(input, timeout=5):
    res = [None, None]
    resolver = Resolver()
    resolver.timeout = float(timeout)
    resolver.lifetime = float(timeout)
    try:
        DNS_TXT = resolver.resolve(input, "TXT")
        res[0] = DNS_TXT
    except DNSException as e:
        res[1] = "e: " + str(e)
    return res

def get_data(url):
    url = str(url)
    try:
        webpage = urlopen(url)
    except:
        print("invalid URL")
        return [None, None]
    soup = BeautifulSoup(webpage, 'lxml')
    title = soup.find("meta")
    name = soup.find("meta", property="og:title")
    content = soup.find("meta", attrs={'name':'description'})
    title_ret = title
    name_ret = name["content"] if name else None
    content_ret = content["content"] if content else None
    return [title_ret, content_ret,name_ret]

def make_url(url):
    # https://swastiksadyal.github.io/   ===> this one is for example, cause this is my portfoliio website
    lis = url.split('/')
    if lis[0] == "https:" or lis[0] == "http:":
        ul = lis[2]
    else:
        ul = lis[0]
    ul = ul.split('.')
    print(ul)
    if ul[0] == 'www':
        ul = ul[1:]
    return '.'.join(ul)