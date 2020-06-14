from OcwaWrap import OcwaWrap
import json
import os
import sys

def main():
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

    wrapper = OcwaWrap(API_TOKEN)
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

if __name__ == "__main__":
    main()