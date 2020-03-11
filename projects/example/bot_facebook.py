import facebook

from key_loader import GENERAL_ACCESS_TOKEN as TKN

graph = facebook.GraphAPI(access_token=TKN.FACEBOOK.value)
fb_response = graph.put_object(
    parent_object='me',
    connection_name='feed',
    message="Hello world!")
print(fb_response)