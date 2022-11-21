# Callow

[![Callow](logo.svg "Callow")](https://callow.now.sh/)

Callow is a simple brute-force script for website login pages. It is meant to be a toy project, and is not intended for use in any serious capacity.

## Requirements

1. Python 3.10+
2. Google chrome
3. [ChromeDriver](https://chromedriver.chromium.org/)

**Note:** Use the ChromeDriver version corresponding to your Chrome version.

## Installation

- Clone the repo

```sh
git clone github.com/maximousblk/callow.git
```

- Install dependencies:

```sh
pip3 install -r requirements.txt
```

## Updating

If you want to get most recent updates for Callow, just pull the latest changes:

```sh
git pull
```

## Quick Start

If you are doing this first time, you can test this safely on the [sandbox](https://callow.now.sh/sandbox/)

Most important part for this to work is to get the selectors right.

1. Run `callow.py` in the installation directory
2. Enter the URL for the login
3. Go to the login page
4. Open developer tools using `Ctrl` + `Shift` + `I`
5. Enter the css selector for `<input>` tags for username and password field
6. Enter the username or email of the target
7. Enter the location of the password dictionary/list and hit Enter

![Wizard](docs/img/wiz.png "Wizard")

Check out my [blog post](https://maximousblk.me/posts/callow-bruteforce-tool) if you want a more elaborate guide.

## Arguments

You can also pass those options in the form of arguments.

You can see the options for Callow here.

| Option   | Function                         |
| -------- | -------------------------------- |
| `--site` | Target website (http/https only) |
| `--usel` | Username input selector          |
| `--psel` | Password input selector          |
| `--user` | Target username to attack        |
| `--pass` | Password dictionary              |

Here is an example of how to use the arguments:

![Arguments](docs/img/arg.png "Arguments")

## To Do

- [X] Port to Python 3.x
- [X] Cross platform compatibility
- [ ] Proxy/Tor support

For more, look into [issues](/issues/) and [projects](/projects/)...

## Disclaimer

> This project (Callow) and it's contributors do not support or take responsibility for any form of unethical acts. This software is purely for educational purposes and is not intended to cause any harm.

## License

Callow is available free of charge under the [GPL-3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html) and can be used for both, commercial and non-commercial purposes.
