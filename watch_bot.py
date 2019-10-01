from webbot import Browser
import threading
import time

class Bot(threading.Thread):
    
    def setup(self,username,password):
        self.username = username
        self.password = password
        self.login_url = "https://euw.leagueoflegends.com/en/"
        #going to change url later
        self.watch_url = "https://watch.lolesports.com/vods/worlds/world_championship_2019"

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
        time.sleep(5)
        bot.quit()

if __name__ == "__main__":
    bot1 = Bot()
    bot1.setup("Eimavekisha","9VnO9XB6dkmBtoE3") 
    bot1.start()   


