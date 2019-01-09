#!usr/bin/env python2

import webbrowser
#import commands
import time
from selenium import webdriver                 #Selenium automates and controls browsers and it’s activity
from getpass import getpass                    #For hiding password to be seen on the window
#import selenium
#import getpass

usrname= raw_input("Enter email id : ")
passwd= getpass("Enter password : ")          #taking credentials from the user

driver = webdriver.Firefox()                  #to open a new tab on browser
print "Opened facebook"
driver.get('https://www.facebook.com/')       #to open a url
time.sleep(1)                                 #so that browser does not sense automation

username_box = driver.find_element_by_id('email')       #to get the id of the email box from html page
username_box.send_keys(usrname)                         #to send data on that id
#print "Email entered"

passwd_box = driver.find_element_by_id('pass')
passwd_box.send_keys(passwd)
#print "Password entered"

login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 

print "Done"
raw_input('Press enter to close')
driver.quit()

execfile('menu.py')
