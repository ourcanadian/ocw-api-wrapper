import requests
import os
import re
import sys

SINGLE_ATTRS = [
    "authorEmail",
    "authorId",
    "authorName",
    "content",
    "contentType",
    "createdAt",
    "creatorEmail",
    "creatorId",
    "creatorName",
    "description",
    "editor",
    "id",
    "isPublished",
    "isPrivate",
    "path",
    "privateNS",
    "publishEndDate",
    "publishStartDate",
    "render",
    "title",
    "updatedAt"
]

class Wrapper:

    url = 'https://wiki.ourcanadian.ca/graphql'
    headers = None

    def __init__(self, api_token=None, slack_url=None):
        if(api_token):
            self.headers = {'Authorization': 'Bearer %s' % api_token}
        self.slack_url = slack_url

    def sendQuery(self, query):
        if(self.headers):
            return requests.post(url=self.url, json=query, headers=self.headers).json()
        else:
            return requests.post(url=self.url, json=query).json()

    def sendSingleQuery(self, id, called_attrs):
        attributes = ""
        for attr in called_attrs:
            if attr in SINGLE_ATTRS:
                attributes += attr+" "
            else:
                raise Exception("Invalid attribute: "+attr)

        response = self.sendQuery({ 'query' : ' { pages { single(id: '+str(id)+') { '+attributes+'} } }' })
        return response

    def createPage(self, id, called_attrs=SINGLE_ATTRS):
        response = self.sendSingleQuery(id, called_attrs)
        if('data' in response.keys()):
            if('pages' in response['data'].keys() and 'single' in response['data']['pages'].keys()):
                return Page(response['data']['pages']['single'])
            else:
                raise Exception("Issue accessing page data.")
        elif('errors' in response.keys() and len(response['errors']) > 0 and 'message' in response['errors'][0].keys()):
            raise Exception(response['errors'][0]['message']) 
        else:
            raise Exception("Unkown error")

    def createContent(self, id):
        attrs = [
            'content',
            'description',
            'id',
            'path',
            'title',
        ]
        response = self.sendSingleQuery(id, attrs)
        if('data' in response.keys()):
            if('pages' in response['data'].keys() and 'single' in response['data']['pages'].keys()):
                return Content(response['data']['pages']['single'])
            else:
                raise Exception("Issue accessing page data.")
        elif('errors' in response.keys() and len(response['errors']) > 0 and 'message' in response['errors'][0].keys()):
            raise Exception(response['errors'][0]['message']) 
        else:
            raise Exception("Unkown error")

    def slack(self, msg):
        if(self.slack_url):
            command = os.popen('''curl -X POST -H 'Content-type: application/json' --data '{"text":"'''+msg+'''"}' '''+self.slack_url)
            print(command.read())
            print(command.close())
        else:
            raise Exception("No access to slack messaging, must have SLACK_URL")

class Page:

    def __init__(self, pageObject):
        self.attr = pageObject

    def get(self, key):
        if(key in self.attr.keys()):
            return self.attr[key]
        else:
            raise Exception("You did not request access to "+key)

    def getAuthorEmail(self):
        return self.get("authorEmail")

    def getAuthorId(self):
        return self.get("authorId")

    def getAuthorName(self):
        return self.get("authorName")

    def getContent(self):
        return self.get("content")

    def getContentType(self):
        return self.get("contentType")

    def getCreatedAt(self):
        return self.get("createdAt")

    def getCreatorEmail(self):
        return self.get("creatorEmail")

    def getCreatorId(self):
        return self.get("creatorId")

    def getCreatorName(self):
        return self.get("creatorName")

    def getDescription(self):
        return self.get("description")

    def getEditor(self):
        return self.get("editor")
        
    def getId(self):
        return self.get("id")

    def getIsPublished(self):
        return self.get("isPublished")

    def getIsPrivate(self):
        return self.get("isPrivate")

    def getPath(self):
        return self.get("path")

    def getPrivateNS(self):
        return self.get("privateNS")

    def getPublishEndDate(self):
        return self.get("publishEndDate")

    def getPublishStartDate(self):
        return self.get("publishStartDate")

    def getRender(self):
        return self.get("render")

    def getTitle(self):
        return self.get("title")

    def getUpdatedAt(self):
        return self.get("updatedAt")

class Content:

    url = None

    def __init__(self, pageObject):
        self.content = pageObject['content']
        self.description = pageObject['description']
        self.id = pageObject['id']
        self.path = pageObject['path']
        self.title = pageObject['title']

    def getContent(self):
        return self.content

    def getDescription(self):
        return self.description

    def getId(self):
        return self.id

    def getPath(self):
        return self.path

    def getTitle(self):
        return self.title

    def getUrl(self):
        if(not self.url):
            match = re.match('> (.*)\s', self.content)
            if(match):
                self.url = match.groups(1)[0]

        return self.url

def test_connection():
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

    wrapper = Wrapper()
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

def test_slack(urlName='SLACK_URL', urlValue=None):

    if(urlValue):
        SLACK_URL = urlValue
    elif(urlName in os.environ.keys()):
        SLACK_URL = os.environ[urlName]
    else:
        print("---")
        print("Slack url missing from enviroment variables.")
        print("Please ensure the variable is named", urlName)
        print("Or enter the value as a parameter: test_slack(urlValue='HOOK_URL')")
        print("---")
        return

    wrapper = Wrapper(slack_url=SLACK_URL)
    response = wrapper.slack("Hello World")

    print("---")
    print("Connection success.")
    print("---")

def test_token(tokenName='OCWA_TOKEN', tokenValue=None):
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

    if(tokenValue):
        API_TOKEN = tokenValue
    elif(tokenName in os.environ.keys()):
        API_TOKEN = os.environ[tokenName]
    else:
        print("---")
        print("Token missing from enviroment variables.")
        print("Please ensure the variable is named", tokenName)
        print("Or enter the value as a parameter: test_token(tokenValue='TOKEN_VALUE')")
        print("---")
        return

    wrapper = Wrapper(API_TOKEN)
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

def test_createPage():

    print("Under construction . . .")
    return

    wrapper = Wrapper(API_TOKEN)
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


def test_createContent():

    print("Under construction . . .")
    return

    wrapper = Wrapper(API_TOKEN)
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

def tests(setting=0):
    if(setting == 1):
        print("1) ocwa.test_connection()")
        print()
        print("\tNo parameters.")
    elif(setting == 2):
        print("2) ocwa.test_token()")
        print()
        print("| tokenName  | 'OCWA_TOKEN' |")
        print("| tokenValue |     None     |")
        print()
        print("e.g. ocwa.test_token(tokenName='WIKIJS_ACCESS_TOKEN')")
        print("e.g. ocwa.test_token(tokenValue='efp2uru435tc67432o2c')")
    elif(setting == 3):
        print("3) ocwa.test_slack()")
        print()
        print("| urlName  | 'SLACK_URL' |")
        print("| urlValue |    None     |")
        print()
        print("e.g. ocwa.test_slack(urlName='REDDIT_BOT_SLACK_URL')")
        print("e.g. ocwa.test_slack(urlValue='https://hooks.slack.com/services/vrehbverb/berlvhbery')")
    else:
        print("1) ocwa.test_connection()")
        print("2) ocwa.test_token()")
        print("3) ocwa.test_slack()")
