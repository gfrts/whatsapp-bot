import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


#links e xpaths
WPP_LINK = "https://web.whatsapp.com/"
SEND_BUTTON = '//*[@id="main"]/footer/div[1]/div[3]'
START_CHAT = '//*[@id="action-button"]'
USE_WEB_WPP = '//*[@id="fallback_block"]/div/div/a'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(WPP_LINK) #abre o whatsapp. necessita autenticacao via QRCode

def send_message(numero, msg):
    #chama a api para enviar mensagem a um numero
    url = "https://api.whatsapp.com/send?phone={}&text={}"
    driver.get(url.format(numero, msg))
    sleep(3)
    
    #clica no botao 'Iniciar conversa'
    start_chat = driver.find_element_by_xpath(START_CHAT)
    start_chat.click()
    sleep(3)
    
    #clica no botao 'Usar Whatsapp Web"
    use_web_wpp = driver.find_element_by_xpath(USE_WEB_WPP)
    use_web_wpp.click()
    sleep(10)
    
    #clica no botao de enviar mensagem
    send_button = driver.find_element_by_xpath(SEND_BUTTON)
    send_button.click()
    sleep(3)
    
df = pd.read_excel('lista_contatos_bot_wpp.xlsx')
numeros = df['Telefone'].values.tolist()
nomes = df['Nome'].values.tolist()
#defina abaixo a mensagem que quer enviar
mensagem = "Ola {}, sou um bot te enviando uma mensagem!"

for numero, nome in zip(numeros, nomes):
    send_message(numero, mensagem.format(nome))
