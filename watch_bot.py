from webbot import Browser
import threading
import time
from connections.connections import Connection
import json

REGION = "EUW"


class Bot(threading.Thread):
    
    def setup(self,username,password,urls, conn):
        self.username = username
        self.password = password
        self.login_url = urls['login_url']
        self.conn = conn
        self.watch_url = urls['watch_url']

    def run(self):
        bot = Browser(showWindow = True)
        bot.go_to(self.login_url)
        print("went to home page")
        print("checking for login")
        bot.maximize_window()
        # if(bot.exists(text="LOGIN")):
        #     bot.click("LOGIN")
        # else:
        #     print("didn't find login")
        #     bot.click("EUW")
        bot.click("EUW")
        bot.click("LOGIN")
        print("click login")
        time.sleep(5)
        bot.type(self.username, into="Username")
        bot.type(self.password, into = "Password")
        bot.click("SIGN IN")
        print("clicked sign in")
        time.sleep(5)
        print("signed in")
        bot.go_to(self.watch_url)
        time.sleep(10)
        self.mission_confirmation(bot)
        bot.quit()

    def mission_confirmation(self,bot):
        bot.go_to('https://raptor.rewards.lolesports.com/v1/missions/free?locale=en_US')
        pre = bot.driver.find_element_by_tag_name("pre").text
        data = json.loads(pre)
        try:
            if( data['completed'][0]['isComplete']):
                self.conn.post_mission_status(self.username, True)
        except:
            self.conn.post_mission_status(self.username, False)
# class ShowProgress(threading.Thread):


if __name__ == "__main__":
    conn = Connection()
    bots = []
    accounts = conn.get_accounts(1)
    for n in range(len(accounts['username'])):
        urls = conn.get_urls(REGION)
        print(accounts['username'][n],  accounts['password'][n], urls, conn)
        bot = Bot()
        bot.setup(accounts['username'][n],  accounts['password'][n], urls, conn)
        bot.start()
        bots.append(bot)
        



