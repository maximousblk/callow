<p align="center">
<a href="//callow.now.sh/"><img src="logo.svg" alt="CALLOW" /></a>
<br>
<br>
</p>

# Callow

A dead simple login brute-force tool

> **Note:** _This project currentry only supports windows_

<sup>This project is basically a fork of [metachar/Hatch](https://github.com/metachar/Hatch) but I wanted to develop it independently. Being a fork of a parent project, Callow respects and inherits the same license terms of Hatch.</sup>

## Requirements

1.  Python 3.5+
2.  Google chrome 80+
3.  [ChromeDriver](//chromedriver.chromium.org/)

Callow includes ChromeDriver 80 which supports Chrome 80 and probably any future versions of chrome. For older versions, replace the `chromedriver.exe` with the version compatible with your version of chrome.

## Installation

- Clone the repo :

```
git clone github.com/maximousblk/callow.git
```

<small>or download from <a href="//github.com/maximousblk/callow/releases">releases</a></small>

- Install dependencies:

```
pip3 install -r requirements.txt
```

## Updating

If you want to get most recent updates for Callow, just pull the repository using

```
git pull origin master
```

Or, you can download the latest version from [releases page](//github.com/maximousblk/callow/releases) on Github.

## Getting Started

If you are doing this first time, you can test this safely on our [sandbox](//callow.now.sh/sandbox/) so that no one gets harmed

Most important part for this to work is to get the selectors right. To do that:

1.  Run `callow.py` in the installation directory
2.  Go to the page that has the login page
3.  Open developer tools using `Ctrl` + `Shift` + `I`
4.  Enter the css selector for `<input>` tags for username and password field
5.  Enter the username or email of the target
6.  Enter the location of the password dictionary/list
7.  Let it run and wait for eternity

## Arguments

```txt
~\workspace\repos\maximousblk\callow (master -> origin)
λ callow.py -h
Usage: callow.py [options]

Options:
  -h, --help       show this help message and exit
  --site=WEBSITE   Target website (http/https only)
  --usel=USEL      Username input selector
  --passsel=passsel      Password input selector
  --user=USERNAME  Target username to attack
  --pass=PASSLIST  Password dictionary
```

If you run it without passing any arguments, you'll greeted with a wizard!

## To Do

- [x] Port to Python 3.x
- [ ] Cross platform compatibility
- [ ] Proxy/Tor support

For more, look into [issues](/issues/) and [projects](/projects/)...

## Disclaimer

> This project (Callow) and it's contributors do not support or take responsibility for any form of unethical acts.    
> This software is purely for educational purposes and is not intended to cause harm.
