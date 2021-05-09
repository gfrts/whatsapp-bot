import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


#links e xpaths
WPP_LINK = "https://web.whatsapp.com/"
NEW_MSG_BUTTON = '//*[@id="side"]/header/div[2]/div/span/div[2]/div/span'
SEARCH_CONTACT_FIELD = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]'
FIRST_CONTACT = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[2]'
TYPE_MSG = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
SEND_BUTTON = '//*[@id="main"]/footer/div[1]/div[3]'
START_CHAT = '//*[@id="action-button"]'
USE_WEB_WPP = '//*[@id="fallback_block"]/div/div/a'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(WPP_LINK)

def send_message(contact_name, msg):
    
   ##ENVIANDO MSG PROCURANDO CONTATO## 
    
    new_msg_button = driver.find_element_by_xpath(NEW_MSG_BUTTON)
    new_msg_button.click()
    sleep(1)
    
    search_contact_field = driver.find_element_by_xpath(SEARCH_CONTACT_FIELD)
    search_contact_field.click()
    search_contact_field.send_keys(contact_name)
    sleep(2)
    
    first_contact = driver.find_element_by_xpath(FIRST_CONTACT)
    first_contact.click()
    sleep(1)
    
    type_msg = driver.find_element_by_xpath(TYPE_MSG)
    type_msg.click()
    type_msg.send_keys(msg)
    
   ##ENVIANDO MSG USANDO URL##
    
   # url = "https://api.whatsapp.com/send?phone={}&text={}"
   # driver.get(url.format(contact_name, msg))
   # sleep(2)
    
   # start_chat = driver.find_element_by_xpath(START_CHAT)
   # start_chat.click()
   # sleep(2)
    
   # use_web_wpp = driver.find_element_by_xpath(USE_WEB_WPP)
   # use_web_wpp.click()
   # sleep(2)
    
   # send_button = driver.find_element_by_xpath(SEND_BUTTON)
   # send_button.click()
   # sleep(1)
    
df = pd.read_excel('lista_contatos_bot_wpp.xlsx', sheet_name = 'Página1')
contatos = df['Lista de contatos'].values.tolist()
mensagem = "Ola {}, sou um bot te enviando uma mensagem!"

for contato in contatos:
    send_message(contato, mensagem.format(contato))
