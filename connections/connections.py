import requests 
import json
import random 

class Connection: 

    def __init__(self):
        with open('urls.json') as json_file:
            data = json.load(json_file)
            self.login_urls = data['login_urls']
            self.vods_urls = data['vods_urls']
            self.get_account_detail_url = 'http://localhost:8000/api/get_users'
            self.post_mission_status_url = 'http://localhost:8000/api/post_mission_status'
            print("URLS Loaded")

    def get_accounts(self,number = 10):        
        request_json =  {'quantity':number}
        r = requests.post(url = self.get_account_detail_url, data =json.dumps(request_json))
        return (json.loads(r.text))
        
    def post_mission_status(self,username,status):
        request_json =  {'username':username, 'is_worlds_completed':status}
        r = requests.post(url = self.post_mission_status_url, data =json.dumps(request_json))
        response_json = json.loads(r.text)
        return response_json['done']

    def get_urls(self, region):
        watch_url = self.vods_urls[random.randint(0,len(self.vods_urls))]
        login_url = self.login_urls[str(region).upper()]
        response = {
            'watch_url':watch_url,
            'login_url':login_url
        }
        return response