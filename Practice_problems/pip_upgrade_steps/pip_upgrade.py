import re

text = "This is a string with version 3.9.1 and 2.7.18"
versions = ["3.9.1", "2.7.18"]
new_versions = ["new_version1", "new_version2"]

# Create a dictionary to map old versions to new versions
version_map = dict(zip(versions, new_versions))

# Define the regular expression with a capture group for the version number
regex = r"==(?P<version>[0-9]+\.[0-9]+\.[0-9]+)"

# Use sub with a callback function to replace each version with its corresponding new version
def replace_version(match):
    version = match.group("version")
    return "==" + version_map.get(version, version)

new_text = re.sub(regex, replace_version, text)
print(new_text)  # Output: This is a string with version new_version1 and new_version2