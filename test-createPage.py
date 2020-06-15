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
    page = wrapper.createPage(2)

    page.getAuthorEmail()
    page.getAuthorId()
    page.getAuthorName()
    page.getContent()
    page.getContentType()
    page.getCreatedAt()
    page.getCreatorEmail()
    page.getCreatorId()
    page.getCreatorName()
    page.getDescription()
    page.getEditor()
    page.getId()
    page.getIsPublished()
    page.getIsPrivate()
    page.getPath()
    page.getPrivateNS()
    page.getPublishEndDate()
    page.getPublishStartDate()
    page.getRender()
    page.getTitle()
    page.getUpdatedAt()

    print("---")
    print("Connection success.")
    print("---")

if __name__ == "__main__":
    main()