import requests
import json

def getCreds():
    creds = dict() # dictionary to hold everything
    creds['access_token'] = 'EAAHHaCP5zx0BAAp2Iv8GsRCmwchFHExO0GZBhCOZBk5svujnkT9vEBRk9UDeHcsHKMzkwz4nn3h0wQbXG2AHvwyZC8C0AUjA7P5bOAABZBP91XKBAu1KT5ZB7TuRBtcYCeovv4fX5WXDhFPfnXr6CJx962x1cXr6hLtLx7Dql2QZDZD'
    creds['client_id'] = '500725070810909' # client id from facebook app IG Graph API Test
    creds['client_secret'] = 'edfcda20c1d776ad7757555972ea2654' # client secret from facebook app
    creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
    creds['graph_version'] = 'v8.0' # version of the api we are hitting
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
    creds['debug'] = 'no' # debug mode for api call

    creds['page_id'] = '118580610011877' # users page id
    
    
    creds['instagram_account_id'] = '17841404636746484' # users instagram account id    # ig-user-id = instagram_account_id
    creds['ig_username'] = 'duonghoanvu1' # ig username
    
    return creds

def makeApiCall( url, endpointParams, debug = 'no' ):
    data = requests.get( url, endpointParams ) # make get request

    response = dict() # hold response info
    response['url'] = url # url we are hitting
    response['endpoint_params'] = endpointParams #parameters for the endpoint
    response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
    response['json_data'] = json.loads( data.content ) # response data from the api
    response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

    if ( 'yes' == debug ) : # display out response info
        displayApiCallData( response ) # display response

    return response # get and return content

def displayApiCallData( response ) :
    """ Print out to cli response from api call """

    print ("\nURL: ") # title
    print (response['url']) # display url hit
    
    print ("\nEndpoint Params: ") # title
    print (response['endpoint_params_pretty']) # display params passed to the endpoint
    
    print ("\nResponse: ") # title
    print (response['json_data_pretty']) # make look pretty for cli