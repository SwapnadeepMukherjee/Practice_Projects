# Input -> comes any url in any forms
# logic -> processs/mask the url and shorten it -> we will need to mask the url 
# logically ->

# how will we validate the uniques of the url such that it doesn't coincide with the other person's URL?

# Recursively validate the UUID before sharing the short-URL:

# original_url = ""
# list = [UUID, orig_url, short_url]

def post_long_url(self, original_url, list):
    original_url = ""
    list = [[UUID, orig_url, short_url]]

    for original_url in list[orig_url]:
        if original_url == list[orig_url]:
            return list[short_url]
        else:
            reuturn 0
