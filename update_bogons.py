#!/usr/bin/env python3
import logging
import os
import sys
import urllib.request


# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    stream=sys.stdout
)


def download_file(url: str, filename: str) -> bool:
    '''
    Download a file from a URL and save it locally
    :param url: URL to download from
    :param filename: Local filename to save as
    '''
    try:
        logging.info(f'Downloading {url} to {filename}')
        urllib.request.urlretrieve(url, filename)
        return True
    except Exception as e:
        logging.error(f'Failed to download {url}: {str(e)}')
        return False


def main() -> None:
    '''Main entry point for the script'''
    sources = {
        'bogons_ipv4.txt': 'https://team-cymru.org/Services/Bogons/fullbogons-ipv4.txt',
        'bogons_ipv6.txt': 'https://team-cymru.org/Services/Bogons/fullbogons-ipv6.txt'
    }

    success = True
    for filename, url in sources.items():
        if not download_file(url, filename):
            success = False

    if not success:
        sys.exit(1)


if __name__ == '__main__':
    main() 