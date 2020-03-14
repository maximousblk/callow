# Callow

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmaximousblk%2Fcallow.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fmaximousblk%2Fcallow?ref=badge_shield)

Callow is a dead simple brute force tool for websites with simple structures.

> **Note:** _This project currentry only supports windows_

<sup>This project is basically a fork of
[metachar/Hatch](https://github.com/metachar/Hatch) but I wanted to develop it
independently. Being a fork of a parent project, Callow respects and inherits
the same license terms of Hatch.</sup>

## Requirements

- Python 3.x
- Google Chrome
- [Chromedriver](http://chromedriver.chromium.org/)

Callow currently ships with ChromeDriver 80.0.3987.106 and hence supports Chrome
80 and quite possibly any future versions of chrome. For older versions of
chrome, replace the `chromedriver.exe` with the version compatible with your
version of chrome.

## Installation

- Clone the repo

```txt
git clone https://github.com/maximousblk/callow.git
```

- Install dependencies

```txt
pip3 install -r requirements.txt
```

## Options

```txt
~\workspace\repos\maximousblk\callow (master -> origin)
λ callow.py -h
Usage: callow.py [options]

Options:
  -h, --help       show this help message and exit
  --site=WEBSITE   Target website (http/https only)
  --usel=USEL      Username input selector
  --psel=PSEL      Password input selector
  --lsel=LSEL      Submit button selector
  --user=USERNAME  Target username to attack
  --pass=PASSLIST  Password dictionary
```

dont worry if you run the tool without any options. You'll greeted with a
wizard!

## How to use

1. Find a website with a login page
2. Inspect element to find the Selector of the username and password input
   elements and the form submit button
3. choose a target username to attack
4. Choose a password list file
5. Let it run.

## To Do

- [x] Port to Python 3.x
- [ ] Cross platform compatibility

For more, look into [issues](/issues/) and [projects](/projects/)...

## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmaximousblk%2Fcallow.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fmaximousblk%2Fcallow?ref=badge_large)
