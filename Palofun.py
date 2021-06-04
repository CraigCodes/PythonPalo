import requests
import getpass
import re
import wawa


if __name__ == '__main__':

    #Get username and password
    Username = "admin"
    Password = "Palotest1"
    interface = "ethernet1/1"
    listname = "TestFilter"
    key = wawa.getAPIKey(Username, Password)
    print(key)

    #wawa.getSystemInfo(key)
    #wawa.clearDHCPLeases(interface, key)
    FQDNList = 'craigslist.com', 'Apple.com', 'Google.com'
    wawa.writeURLList(listname, FQDNList, key)