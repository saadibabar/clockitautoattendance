from selenium import webdriver
import yaml

conf = yaml.load(open('logindata.yml'))
myKtmEmail = conf['ktm_user']['email']
myKtmPassword = conf['ktm_user']['password']

driver = webdriver.Chrome()

def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.find_element_by_class_name(usernameId).send_keys(username)
   driver.find_element_by_class_name(passwordId).send_keys(password)
   driver.find_element_by_class_name(submit_buttonId).click()
   

login("https://clockit.me/index.php/auth/login", "login-userpin", myKtmEmail, "login-password", myKtmPassword, "login-btn")