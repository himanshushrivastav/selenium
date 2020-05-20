from utility.services import *
from repositories.locators import home_page as hp

class Home(fun):
    def __init__(self):
        super(fun, self).__init__()

    def NavBar_links(self):
        self.click(hp.get('Home'))
        print('clicked')
        self.click(locator=hp.get('store'))
        print('done')
        self.click(hp.get('browse All'))



a = Home()
a.setup()
a.NavBar_links()