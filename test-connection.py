import OcwaWrap as ocwa
import json

def main():
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


if __name__ == "__main__":
    main()