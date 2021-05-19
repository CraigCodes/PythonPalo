import requests
import getpass
import re



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


def clearDHCPLeases(interface):

    apirequest = "https://192.168.169.101/api/?type=op&cmd=<clear><dhcp><lease><interface><entry name='" + interface + "'/></interface></lease></dhcp></clear>&key=" + key

    response = requests.get(apirequest, verify=False)
    response = response.content.decode('UTF-8')

    print(response)

if __name__ == '__main__':

    #Get username and password
    Username = input("Username: ")
    Password = getpass.getpass("Password: ")
    interface = "ethernet1/1"
    key = getAPIKey(Username, Password)
    print(key)

    getSystemInfo(key)
    clearDHCPLeases(interface)
