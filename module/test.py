import ocwa
import os
import sys
import json

def connection():
    query = {
        "query": '''
        {
            pages {
                list {
                    contentType
                    createdAt
                    description
                    id
                    isPrivate
                    isPublished
                    locale
                    path
                    privateNS
                    tags
                    title
                    updatedAt
                } 
            }
        }
    '''
    }

    wrapper = ocwa.Wrapper()
    response = wrapper.sendQuery(query)
    if('errors' in response.keys()):
        print("---")
        print("Connection failed, for the following reasons:")
        
        for error in response['errors']:
            print(">", error['message'])
        print("---")
    else:
        print("---")
        print("Connection success.")
        print("---")

def createPage():

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

def slack():

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

def token():
    query = {
        "query": '''
        {
            pages {
                single(id: 20) {
                    authorEmail
                    authorId
                    authorName
                    content
                    contentType
                    createdAt
                    creatorEmail
                    creatorId
                    creatorName
                    description
                    editor
                    id
                    isPublished
                    isPrivate
                    path
                    privateNS
                    publishEndDate
                    publishStartDate
                    render
                    tags {
                        createdAt
                        id
                        tag
                        title
                        updatedAt
                    }
                    title
                    updatedAt
                } 
            }
        }
    '''
    }

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
    response = wrapper.sendQuery(query)
    if('errors' in response.keys()):
        print("---")
        print("Connection failed, for the following reasons:")
        
        for error in response['errors']:
            print(">", error['message'])
        print("---")
    else:
        print("---")
        print("Connection success.")
        print("---")

def createContent():
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
        

    



