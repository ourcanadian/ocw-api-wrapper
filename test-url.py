import OcwaWrap as ocwa
import json
import os
import sys

def main():

    if(len(sys.argv) > 1 and sys.argv[1] in os.environ.keys()):
        API_TOKEN = os.environ[sys.argv[1]]
    elif('OCWA_TOKEN' in os.environ.keys()):
        API_TOKEN = os.environ['OCWA_TOKEN']
    else:
        print("---")
        print("Token missing from enviroment variables.")
        print("Please ensure the variable is named:")
        print("OCWA_TOKEN or enter another name as an arguement:")
        print("```python3 test-token.py VAR_NAME```")
        print("---")
        return

    wrapper = ocwa.Wrapper(API_TOKEN)
    content = wrapper.createContent(2)

    content.getContent()
    content.getDescription()
    content.getId()
    content.getPath()
    content.getTitle()

    expected_url = "https://madeinca.ca/"
    url = content.getUrl()

    if(url == expected_url):
        print("---")
        print("Connection success.")
        print("---")
    else:
        print("---")
        print("Error in url.")
        print("Found: "+str(url))
        print("Expected: "+expected_url)
        print("---")

if __name__ == "__main__":
    main()