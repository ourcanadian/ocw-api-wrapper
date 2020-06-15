import OcwaWrap as ocwa
import os
import sys

def main():

    if(len(sys.argv) > 1 and sys.argv[1] in os.environ.keys()):
        SLACK_URL = os.environ[sys.argv[1]]
    elif('SLACK_URL' in os.environ.keys()):
        SLACK_URL = os.environ['SLACK_URL']
    else:
        print("---")
        print("Slack url missing from enviroment variables.")
        print("Please ensure the variable is named:")
        print("SLACK_URL or enter another name as an arguement:")
        print("```python3 test-slack.py VAR_NAME```")
        print("---")
        return

    wrapper = ocwa.Wrapper(slack_url=SLACK_URL)
    response = wrapper.slack("Hello World")

    print("---")
    print("Connection success.")
    print("---")


if __name__ == "__main__":
    main()