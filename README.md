# Bitly URL shortener

This is a Python program that uses the Bitly API to shorten URLs and count the number of clicks on Bitlinks.

# Prerequisites
Before running this program, you need to obtain a Bitly API token. You can do this by creating a Bitly account and following the instructions [here](https://dev.bitly.com/docs/getting-started/authentication/).

# How to install
Python3 should already be installed.
Then use 'pip' to install the dependencies:

1. Clone this repository or download the script file.
2. Install the required Python packages using pip:

```
pip install requests
pip install python-dotenv
```

You can also install dependencies with the command:
```angular2html
pip install -r requirements.txt
```

# Usage
To run the program, use the following command:
```
python link_shortener.py [URL]
```
Replace [URL] with the URL you want to shorten or check the number of clicks for. If no URL is provided, the program will prompt you to enter one.

If the URL provided is a Bitlink, the program will display the number of clicks on the link. If the URL is not a Bitlink, the program will shorten it and display the resulting Bitlink.

### Project purpose
The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/)
