#just write behave in terminal
from selenium.webdriver import Chrome


def before_all(context):
    path = 'C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe'
    context.driver = Chrome(executable_path=path)  # through context you can use driver object anywhere in this page like global

def after_all(context):
    context.driver.close()

def before_feature(context,feature):
    path = 'C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe'
    context.driver = Chrome(executable_path=path)  # through context you can use driver object anywhere in this page like global

def after_feature(context,feature):
    context.driver.close()

def before_scenario(context,scenario):
    path = 'C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe'
    context.driver = Chrome(executable_path=path)  # through context you can use driver object anywhere in this page like global

def after_scenario(context,scenario):
    context.driver.close()

def before_tag(context,tag):
    path = 'C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe'
    context.driver = Chrome(executable_path=path)  # through context you can use driver object anywhere in this page like global

def after_tag(context,tag):
    context.driver.close()

def before_step(context,step):
    path = 'C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe'
    context.driver = Chrome(executable_path=path)  # through context you can use driver object anywhere in this page like global

def after_step(context,step):
    context.driver.close()