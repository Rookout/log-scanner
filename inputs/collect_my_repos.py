# The following script is separated from the rest of the scanner, and is being run manually only.
# The script automatically generates a list of repositories, which is later used for the Rookout Logs Report.
# The list will include all of the user's repositories, according to the supplied token. including repos of organizions the user is belong to.

import os
from urllib.request import Request, urlopen
import json
import subprocess
import sys

if len(sys.argv) > 1:
    GITHUB_TOKEN = sys.argv[1]
elif os.environ.get("GITHUB_TOKEN") is not None:
    GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
else:
    print("no Github token supplied")
    quit()

supported_languages = ["C#", "Python", "JavaScript", "Java"]
status = True
base_url = 'https://api.github.com/user/repos'
page = 1
urls = []
while status:
    url = base_url + f"?page={page}"
    req = Request(url)
    req.add_header("Authorization", f"token {GITHUB_TOKEN}")
    response = urlopen(req)
    if response.status != 200:
        print("request failed.. check your github token or try manually")
    repos = json.loads(response.read())
    urls += [item['html_url'] for item in repos if item["language"] in supported_languages]

    page += 1
    if len(repos) < 30:
        status = False

os.remove(os.path.join("inputs", "repositories.txt"))
with open(os.path.join("inputs", "repositories.txt"), 'w') as file_content:
    for url in urls:
        file_content.write(f"{url}\n")

print("finished")
try:
    subprocess.call(["open", os.path.join("inputs", "repositories.txt")])
except:
    quit()
