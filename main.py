import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='The link-shortener tool'
    )
    parser.add_argument(
        'url',
        nargs='?'
    )
    return parser


def shorten_link(token, url):
    api_endpoint = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {
        "long_url": url
    }
    response = requests.post(
        url=api_endpoint,
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    bitlink = response.json().get("link")
    return bitlink


def count_clicks(token, bitlink):
    api_endpoint = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(
        url=api_endpoint,
        headers=headers
    )
    response.raise_for_status()
    click_count = response.json().get("total_clicks")
    return click_count


def is_bitlink(url, token):
    api_endpoint = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(
        url=api_endpoint,
        headers=headers
    )
    return response.ok


def main():
    load_dotenv()
    token = os.environ["BITLY_API_TOKEN"]
    parser = create_parser()
    args = parser.parse_args()
    try:
        parsed_url = urlparse(args.url)
        normalized_url = f"{parsed_url.netloc}{parsed_url.path}"
        if is_bitlink(normalized_url, token):
            print("По вашей ссылке перешли:",
                  count_clicks(token, normalized_url),
                  "раз(а)")
        else:
            print("Битлинк:", shorten_link(token, args.url))
    except requests.exceptions.HTTPError:
        print("Вы ввели неправильную ссылку или неверный токен.")


if __name__ == '__main__':
    main()
