import ocwa
import json

query = {
    "query": '''
    {
        pages {
            links(locale: "en") {
                title
                id
                links
            }
        }
    }
    '''
}

wrapper = ocwa.Wrapper('OCWA_TOKEN')
response = wrapper.sendQuery(query)
print(json.dumps(response, indent=2))