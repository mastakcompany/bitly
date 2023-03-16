# Bitly URL shortener

This is a Python program that uses the Bitly API to shorten URLs and count the number of clicks on Bitlinks.

# Prerequisites
Before running this program, you need to obtain a Bitly API token. You can do this by creating a Bitly account and following the instructions [here](https://dev.bitly.com/docs/getting-started/authentication/).

# How to install
Python3 should already be installed.
Then use `pip` to install the dependencies:

1. Clone this repository or download the script file.
2. Install the required Python packages using pip:

```
pip install requests
pip install python-dotenv
```

You can also install dependencies with the command:
```
pip install -r requirements.txt
```
# Environment Variables
To run the program, you need to set the following environment variables:

`BITLY_API_TOKEN`: This variable should contain your Bitly API token.

Once you have obtained your API token, you can set the BITLY_API_TOKEN environment variable by exporting it in your shell or by adding it to a .env file in the root directory of the bitly program.

For example, if you are using the Bash shell, you can export the BITLY_API_TOKEN variable like this:

```
export BITLY_API_TOKEN=your_api_token_here
```

If you prefer to use a .env file, create a file named .env in the root directory of the bitly program and add the following line:

```
BITLY_API_TOKEN=your_api_token_here
```
Replace your_api_token_here with your actual API token.

# Usage
To run the program, use the following command:
```
python link_shortener.py [URL]
```
Replace [URL] with the URL you want to shorten or check the number of clicks for. If no URL is provided, the program will prompt you to enter one.

If the URL provided is a Bitlink, the program will display the number of clicks on the link. If the URL is not a Bitlink, the program will shorten it and display the resulting Bitlink.

### Project purpose
The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/)
