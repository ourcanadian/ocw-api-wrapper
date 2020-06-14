import requests

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

class OcwaWrap:

    url = 'https://wiki.ourcanadian.ca/graphql'
    headers = None

    def __init__(self, api_token=None, slack_url=None):
        if(api_token):
            self.headers = {'Authorization': 'Bearer %s' % api_token}
        self.slack_url = slack_url

    def hello_world(self):
        return "Hello World"

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

    # def log(self, msg):
    #     if(self.slack_url):
    #         command = os.popen('''curl -X POST -H 'Content-type: application/json' --data '{"text":"'''+msg+'''"}' '''+self.slack_url)
    #         print(command.read())
    #         print(command.close())
    #     else:
    #         print(msg)
