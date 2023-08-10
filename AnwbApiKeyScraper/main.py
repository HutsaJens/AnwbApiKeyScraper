import requests
import re as regex

url = "https://533.static.anwb.nl/assets/utils-anwb-071a536c.js"
routing_pattern = r"routing:\s*{([^}]+)}"
prod_pattern = r"prod:\s*\"([^\"]+)\""
dev_pattern = r"dev:\s*\"([^\"]+)\""


def main():
    prod_key, dev_key = scrapeApiKey()

    # Prod key should be used when making api requests
    if prod_key and dev_key:
        print("Prod Key:", prod_key)
        print("Dev Key:", dev_key)
    else:
        print("Failed to scrape API keys")


def scrapeApiKey():
    response = requests.get(url)

    if response.status_code != 200:
        return None, None

    script_text = response.text
    match_1 = regex.search(routing_pattern, script_text, regex.DOTALL)
    if not match_1:
        return None, None

    routing_obj = match_1.group(1)
    prod_match = regex.search(prod_pattern, routing_obj)
    dev_match = regex.search(dev_pattern, routing_obj)

    if not prod_match or not dev_match:
        return None, None

    prod_value = prod_match.group(1)
    dev_value = dev_match.group(1)

    return prod_value, dev_value


if __name__ == "__main__":
    main()
