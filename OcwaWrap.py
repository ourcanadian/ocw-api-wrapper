import requests

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

    # def sendSingleQuery(self, id, attr):
    #     id = str(id)
    #     response = self.sendQuery({ 'query' : ' { pages { single(id: '+id+') { '+attr+' } } }' })
    #     if('errors' in response.keys()):
    #         for error in response['errors']:
    #             print("(id="+id+")", error['message'])
    #         return None
    #     return response['data']['pages']['single']

    # def log(self, msg):
    #     if(self.slack_url):
    #         command = os.popen('''curl -X POST -H 'Content-type: application/json' --data '{"text":"'''+msg+'''"}' '''+self.slack_url)
    #         print(command.read())
    #         print(command.close())
    #     else:
    #         print(msg)
