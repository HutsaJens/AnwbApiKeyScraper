# API Key Scraper

This is a simple Python script that extracts API keys from a JavaScript file using regular expressions. It is specifically designed to scrape API keys from a certain URL containing routing information.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Requirements](#requirements)
- [Installation](#installation)

## Introduction

This script utilizes the `requests` library to retrieve the content of a JavaScript file from a given URL and then employs regular expressions to extract API keys for both production and development environments.

## Usage

1. Clone this repository to your local machine or download the script file directly.

2. Open the script file `api_key_scraper.py` in a Python-compatible code editor or IDE.

3. Modify the `url` variable to point to the target JavaScript file containing the API keys you want to scrape.

4. Run the script using the following command:

   ```bash
   python api_key_scraper.py

5. The script will attempt to extract the API keys from the JavaScript file and display them on the console if successful. Otherwise, an error message will be shown.

## Requirements
* Python 3.x
* requests library (Install using pip install requests)

## Installation
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/api-key-scraper.git
Or download the script file api_key_scraper.py directly.

2. Install the required requests library using pip:
    ```bash
    pip install requests
    
3. Open the script file in your favorite code editor and customize the url variable to the target URL.

4. Run the script as described in the Usage section.
