def get_list_of_urls_from_dict(key: str, url_dict: dict) ->list:

    # returns key
    return url_dict.get(key, [])

# Example dictionary
url_dict = {
    "search": ["https://google.com", "https://bing.com"],
    "social": ["https://facebook.com", "https://twitter.com"],
    "news": ["https://cnn.com", "https://bbc.com"]
}

# Key exists in the dictionary
print(get_list_of_urls_from_dict("social", url_dict))
# Output: ['https://facebook.com', 'https://twitter.com']

# Key does not exist in the dictionary
print(get_list_of_urls_from_dict("shopping", url_dict))
# Output: []