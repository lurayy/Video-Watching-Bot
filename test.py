from webbot import Browser
import threading
import time
from connections.connections import Connection

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
        bot.go_to('https://raptor.rewards.lolesports.com/v1/missions/free?locale=en_US')
        


# class ShowProgress(threading.Thread):


if __name__ == "__main__":
    conn = Connection()
    bots = []
    accounts = conn.get_accounts(1)
    for n in range(len(accounts['username'])):
        urls = conn.get_urls(REGION)
        bot = Bot(accounts['username'][n],  accounts['password'][n], urls, conn)
        bots.append(bot)
        



