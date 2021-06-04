import requests
import getpass
import re
import urllib3



def getAPIKey(Username, Password):

    apirequest = 'https://192.168.169.101/api/?type=keygen&user=' + str(Username) + '&password=' + str(Password)

    response = requests.get(apirequest,verify=False)
    response = response.content.decode('UTF-8')
    Call = re.compile("<key>.*<\/key>")
    key = Call.findall(response)
    key = ''.join(key)
    key = re.sub(r"<key>" , '', key)
    key = re.sub(r"</key>", '', key)

    return key

def getSystemInfo(key):

    apirequest = 'https://192.168.169.101/api/?type=op&cmd=<show><system><info></info></system></show>&key=' + key

    response = requests.get(apirequest, verify=False)
    response = response.content.decode('UTF-8')

    print(response)


def clearDHCPLeases(interface, key):

    apirequest = "https://192.168.169.101/api/?type=op&cmd=<clear><dhcp><lease><interface><entry name='" + interface + "'/></interface></lease></dhcp></clear>&key=" + key

    response = requests.get(apirequest, verify=False)
    response = response.content.decode('UTF-8')

    print(response)

def addToURLList(listname, url, key):

    apirequest = 'https://192.168.169.101/api/?type=config&action=set&key=' + key + '&xpath=/config/devices/entry/vsys/entry[@name=\'vsys1\']/profiles/custom-url-category/entry[@name=\'' + listname + '\']/list&element=<list><member>' + url + '</member><member>apple.com</member></list><type>URL List</type>'
    response = requests.put(apirequest, verify=False)
    response = response.content.decode('UTF-8')

    print(response)

def writeURLList(listname, FQDNList, key):

    urllist = ''
    
    for i in FQDNList:
        urllist= urllist + '<member>' + i + '</member>'


    apirequest = 'https://192.168.169.101/api/?type=config&action=set&key=' + key + '&xpath=/config/devices/entry/vsys/entry[@name=\'vsys1\']/profiles/custom-url-category/entry[@name=\'' + listname + '\']/list&element=<list>'+ urllist + '</list><type>URL List</type>'
    response = requests.put(apirequest, verify=False)
    response = response.content.decode('UTF-8')

    print(response)

def getURLList(listname, key):
    
    apirequest = 'https://192.168.169.101/api/?type=config&action=get&key=' + key + '&xpath=/config/devices/entry/vsys/entry[@name=\'vsys1\']/profiles/custom-url-category/entry[@name=\'' + listname + '\']'
    response = requests.get(apirequest, verify=False)
    response = response.content.decode('UTF-8')

    print(response)


