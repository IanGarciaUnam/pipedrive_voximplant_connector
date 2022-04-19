#  data retrieval
import urllib3
from urllib3 import request
# json data
import requests
import json
"""
PIPEDRIVE_API_URL = "https://tovox.pipedrive.com/"#"https://api.pipedrive.com/v1/"
route = '/v1/persons'
api_token = 'fdd6d9b99b3ce395ce9bba99521cfbe0a3890cdd'
get_response = requests.get(PIPEDRIVE_API_URL+route+'?api_token=' + api_token)
print(get_response)
get_content=json.loads(get_response.content)
print(get_content)
print("=================")
print(get_content['data'][0]['name'],get_content['data'][0]['phone'][0]['value'])
#print(get_content)
"""
class PipeDrive_api:
    """
    A class to receive the respective data from 
    from pipedrive/persons in deals
    """

    def __init__(self, pipedrive_url, api_token,route='/v1/persons'):
        """
        Pipedrive api initializator
        """
        self.pipedrive_url=pipedrive_url
        self.called_has_been_called=False
        self.route=route
        self.api_token=api_token
        self.persons={}

    def caller(self):
        """
        begin the call and add each person to dict persons by
        name and phone number
        """
        get_response = requests.get(self.pipedrive_url+self.route+'?api_token=' + self.api_token)
        get_content=json.loads(get_response.content)
        for x in get_content['data']:
            print(x['name'],x['phone'][0]['value'])
            self.persons[x['name']]=x['phone'][0]['value']
        print(self.persons)
        self.called_has_been_called=True
        #print(get_content['data'][0]['name'],get_content['data'][0]['phone'][0]['value'])

    def get_persons_to_call(self):
        """
        Check if there exists persons in dict persons 
        and return the dict
        """
        if not self.called_has_been_called:
            return "It's not possible to call, due to caller inactivated"
        return self.persons

from voximplant.apiclient import VoximplantAPI, VoximplantException
class Voximplant_api:

    def __init__(self,name_json, number):
        self.api = VoximplantAPI(name_json)
        self.my_number = number


    def call_number(self,number):
        """
        For test we'll be sending messages
        """
        destination=number
        sms="MENSAJE DE PRUEBA 001"
        try:
            res=self.api.send_sms_message(self.my_number, destination, sms)
            print(res)
        except VoximplantException as e:
            print("Error:{}".format(e.message))

    def call_list_of_numbers(self,contacts):
        for c in contacts:
            self.call_number(contacts[c])


PIPEDRIVE_API_URL = "https://tovox.pipedrive.com/"#"https://api.pipedrive.com/v1/"
route = '/v1/persons'
api_token = 'fdd6d9b99b3ce395ce9bba99521cfbe0a3890cdd'
get_response = requests.get(PIPEDRIVE_API_URL+route+'?api_token=' + api_token)
x = PipeDrive_api(PIPEDRIVE_API_URL, api_token, route)
x.caller()

voximplant= Voximplant_api("077bcfa5-e653-48c8-b8df-b4bb82e007cd_private.json", 19292240694)
voximplant.call_list_of_numbers(x.get_persons_to_call())