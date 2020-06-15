import requests
import os

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
