#  data retrieval
import urllib3
from urllib3 import request
import requests
import json
import time
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
"""
Credenciales
El usuario:delfino
Password:Delfino*2021
Email:delfino.sanchez@bsmexico.com.mx
"""
#vk=requests.get("https://kit.voximplant.com/Editor/out/26817", auth=('delfino', 'Delfino*2021'))
#print(vk.json())
values={"domain":"https://kit.voximplant.com",
'access_token':"f28784281734213565c2adbd32f786a685fd8d1c8abc32d153e9bc4efe6c230e",
'scenario_id':'26818',
'phone_number_id':'2857',
'phone':'525534452621',
'variables': "[{'client_name':'ian'})]"
}
#vvk=requests.post("https://kit.voximplant.com/", auth=('delfino', 'Delfino*2021'), json=values)
#print(vvk)

class Deal:
    """
    This class will allow us to model Deals, by name, product owner and follower
    """
    def __init__(self, deal_name, product_owner, follower,date, org_name, notes):
        self.deal_name=deal_name
        self.product_owner=product_owner
        self.follower=follower
        self.date=date
        self.org_name=org_name
        self.notes=notes

    def get_deal_name(self):
        return self.deal_name

    def get_product_owner(self):
        return self.product_owner

    def get_follower(self):
        return self.follower

    def get_date(self):
        return self.date

    def get_org_name(self):
        return self.org_name

    def get_notes(self):
        return self.notes

    def __str__(self):
        return "Title:"+self.deal_name+", PO: "+self.product_owner+ " follower:"+self.follower+" date: "+self.date

class PipeDrive_api:
    """
    A class to receive the respective data from 
    from pipedrive/persons in deals
    """

    def __init__(self, pipedrive_url, api_token,route='/v1/deals'):
        """
        Pipedrive api initializator
        PARAMS:
            pipedrive_url:str -> url to connect with yourcompany.pipedrive.com
            api_token:str -> token for api
            route:str -> To observe the posibble json(api call ) to get, get from
                         link: https://developers.pipedrive.com/docs/api/v1/Persons#getPersons
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
        deals=[]
        get_response = requests.get(self.pipedrive_url+self.route+'?limit=500&api_token=' + self.api_token)
        get_content=json.loads(get_response.content)
        #print(get_content)
        for x in get_content['data']:
            #print(str(x['title']),x['pipeline_id'])#Nombre del trato
            #print(str(x['person_name']))#Product Owner
            #x['owner_name']#follower
            #print(str(x['update_time']))#fecha
            #print(str(x['update_time']))#hora
            #print(str(x['org_name']))#nombre de la empresa
            #print(x['notes_count'])
            #print(x['next_activity_note'])#Incluye notas teléfono y nombre
            #print(x['pipeline_id'])
            deals.append(Deal(x['title'], x['person_name'], x['owner_name'], x['update_time'], x['org_name'], x['next_activity_note']))
            #for y in x:
                #print(y + " : \n")
                #print(x[y])
        #for d in deals:
            #print(str(d))
        print(len(deals))
        return deals
        """
        for x in get_content['data']:
            print(x['name'],x['phone'][0]['value'])
            self.persons[x['name']]=x['phone'][0]['value']
        print(self.persons)
        self.called_has_been_called=True
        """
        #print(get_content['data'][0]['name'],get_content['data'][0]['phone'][0]['value'])

    def get_persons_to_call(self):
        """
        Check if there exists persons in dict persons 
        and return the dict
        """
        if not self.called_has_been_called:
            return "It's not possible to call, due to caller inactivated"
        return self.persons

class Monday:
#import requests
#import json
    def __init__(self, MONDAY_API_KEY, MONDAY_API_URL ):
        self.apiKey=MONDAY_API_KEY#"eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2NzQxODc2MywidWlkIjozMTYyMzI2NSwiaWFkIjoiMjAyMi0wNi0yN1QwMDo1Nzo1NS44MzZaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTI2MDkxNTUsInJnbiI6InVzZTEifQ.9Eq1QGJMfaerjKwulkPUmkPRhDSdsBYsALj6jNHcZX0"
        self.apiUrl =MONDAY_API_URL# "https://api.monday.com/v2"
        self.headers = {"Authorization" : self.apiKey}
        self.deals_from_monday=[]
        """
        self.query5 = 'mutation ($myItemName: String!, $columnVals: JSON!) { create_item (board_id:YOUR_BOARD_ID, item_name:$myItemName, column_values:$columnVals) { id } }'
        vars = {
        'myItemName' : 'Hello everyone!',
        'columnVals' : json.dumps({
        'status' : {'label' : 'Done'},
        'date4' : {'date' : '1993-08-27'}
         }) 
        }
        #self.query3='mutation{ create_item (board_id:2859016879, item_name:"WHAT IS UP MY FRIENDS!") { id } }'
        #self.query2 = '{ boards (limit:10) {Trato} }'
        self.data = {'query' : self.query3}
        """
    
    def posting(self, deal_name, product_owner,follower,date, org_name, notes):
        self.query5 = 'mutation($myItemName: String!, $columnVals: JSON!){create_item (board_id:2905311888, item_name:$myItemName, column_values:$columnVals){id}}'
        vars = {
        'myItemName' : deal_name,
        'columnVals' : json.dumps({
        'status' : {'label' : 'En Proceso', 'color':'#FDAB3D'},
        'date' : {'date' : date},
        'texto':  product_owner,
        'texto5':follower,# date '1993-08-27'
        'texto8':org_name,
        'texto0':notes

         }) 
        }
        self.query3='mutation{ create_item (board_id:2859016879, item_name:'"WHAT IS UP MY FRIENDS!2"') { id } }'
        #self.query2 = '{ boards (limit:10) {Trato} }'
        self.data = {'query' : self.query5, 'variables' : vars}
        r = requests.post(url=self.apiUrl, json=self.data, headers=self.headers)
        print(r)

    def get(self):
        """
        Get deal names from Monday Board
        """
        #import requests import json
        #apiKey = "YOUR_API_KEY_HERE"
        #apiUrl = "https://api.monday.com/v2"
        #headers = {"Authorization" : apiKey}
        query2 = '{boards(limit:1) { name id description items { name column_values{title id type text } } } }'
        data = {'query' : query2}
        r = requests.post(url=self.apiUrl, json=data, headers=self.headers) # make request
        board=r.json()
        x=board['data']['boards']
        for y in x:
            for m in (y['items']):
                deal_name=m['name']
                if not deal_name in self.deals_from_monday:
                    self.deals_from_monday.append(m['name'])
        return self.deals_from_monday



#from voximplant.apiclient import VoximplantAPI, VoximplantException
class Voximplant_api:
    """
    Voximplant class api to call 
    A class to connect with Voximplant Platform
    """

    def __init__(self,name_json, my_number):
        """
        Builder of Voximplant_api
        name_json : str -> Json file of credentials api
        my_number:str -> origin number
        """
        self.api = VoximplantAPI(name_json)
        self.my_number = my_number


    def send_message_number(self,ext,number,sms):
        """
        For test we'll be sending messages
        PARAMS:
            ext:str -> Extension (country's lada) phone number
            number: str -> Number to call
            sms:str -> Message to sent
        """
        destination=number
        try:
            res=self.api.send_sms_message(self.my_number, ext+destination, sms)
            print(res,"Succesfully sent")
        except VoximplantException as e:
            print("Error:{}".format(e.message))

    def call_list_of_numbers(self,contacts,sms):
        """
        contacts : dict -> Iterable dict of contacts, format {"name":"phone_number"}
        sms : str -> Message to sent 
        """
        for c in contacts:
            self.send_message_number("521",contacts[c],"Hola "+c+"\n"+sms)
"""
voximplant= Voximplant_api("b3288643-f855-4006-8662-c1e7da7325a0_private.json", 15623407185)
voximplant.call_list_of_numbers(pipedrive.get_persons_to_call(),"Este es un mensaje de prueba, saludos.")
"""

#get_response = requests.get(PIPEDRIVE_API_URL+route+'?api_token=' + api_token)
"""
pipedrive= PipeDrive_api(PIPEDRIVE_API_URL, api_token, route)
deals_to_send=pipedrive.caller()
m=Monday()
for deal in deals_to_send:
    print(str(deal))
    comprobator=deal.get_deal_name().split("-")[len(deal.get_deal_name().split("-")) -1]
    if deal not in processed and comprobator=="c":
        print("Enviando")
        processed.append(deal)
        m.posting(deal.get_deal_name(), deal.get_product_owner(), deal.get_follower(), deal.get_date().split()[0])
"""
class Perpetuor:
    """
    Perpetuor allow us to simulate a machine with an stop of code to get the data,
    analyze it and finally decide whether it would be sent to the crm(Monday)
    """
    def __init__(self, PIPEDRIVE_API_URL, route, api_token,  MONDAY_API_KEY, MONDAY_API_URL):
        self.PIPEDRIVE_API_URL=PIPEDRIVE_API_URL
        self.route=route
        self.api_token=api_token
        self.pipedrive=PipeDrive_api(PIPEDRIVE_API_URL, api_token, route)
        self.m=Monday(MONDAY_API_KEY, MONDAY_API_URL)
        self.processed=[]
        try:
            open("proccesed.txt","x")
        except:
            print("file previously created")

    def perpet(self):
        """
        Keeps the function alive to send and receive message from Pipedrive to Monda, from Monday
        and finally decides if post it or not
        """
        local_list_from_get_monday = []
        while True:
            try:
                file=open("proccesed.txt","r")
                self.processed=file.read().split("\n")
                file.close()
                for block in self.m.get():
                    if not block in local_list_from_get_monday:
                        local_list_from_get_monday.append(block)
                print(local_list_from_get_monday)
                deals_to_send=self.pipedrive.caller()
                for deal in deals_to_send:
                    print(str(deal))
                    #comprobator=deal.get_deal_name().split()[len(deal.get_deal_name().split())-1]
                    #
                    comprobator=deal.get_deal_name().split("-")[len(deal.get_deal_name().split("-")) -1]
                    #print(comprobator)
                    if not deal.get_deal_name() in self.processed and not deal.get_deal_name() in local_list_from_get_monday and comprobator=="c":
                        print("Enviando")
                        print(deal.get_deal_name(), comprobator)
                        self.processed.append(deal.get_deal_name())
                        self.m.posting(deal.get_deal_name(), deal.get_product_owner(), deal.get_follower(), deal.get_date().split()[0], deal.get_org_name(), deal.get_notes())
                file_f=open("proccesed.txt","w")
                for m in self.processed:
                    file_f.write(m+"\n")
                file_f.close()
            except:
                self.m.posting("ERROR[PERPET]", "None", "None", "None", "None", "None" )
            print("In sleep")
            time.sleep(10)

PIPEDRIVE_API_URL = "https://bullishmx2.pipedrive.com/"#"https://bullishmx2.pipedrive.com"#"https://tovox.pipedrive.com/"#"https://api.pipedrive.com/v1/"
route = '/v1/pipelines/1/deals'#'/v1/deals'
api_token = 'fc39f5cc93a58b8711315038969f5e6c667f5dca'#bullish_api_pipedrive
MONDAY_API_KEY="eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2OTExNTg0MywidWlkIjoyMzQ3MDMzMywiaWFkIjoiMjAyMi0wNy0wNlQxOToxMzo1OC4xNjNaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MzcyNzEwMiwicmduIjoidXNlMSJ9.p8QMHUsgFMBtj19s-c56uudu5ajGSDo34ToWuzRpCis"
MONDAY_API_URL="https://api.monday.com/v2"
#pipedrive=PipeDrive_api(PIPEDRIVE_API_URL, api_token, route)
#pipedrive.caller()
p=Perpetuor(PIPEDRIVE_API_URL,route, api_token,MONDAY_API_KEY, MONDAY_API_URL)
p.perpet()
