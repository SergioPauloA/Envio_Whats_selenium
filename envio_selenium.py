from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Lista de números
numeros = ["numero1", "numero2", "numero3"]
mensagem = "Mensagem que deseja"

# Configuração do Edge
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

# Acessa o WhatsApp Web
driver.get("https://web.whatsapp.com/")
input("Após escanear o QR Code, pressione Enter...")  # Aguarda login manual

# Envia mensagens
for numero in numeros:
    driver.get(f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}")
    time.sleep(10)  # Tempo para a página carregar completamente

    try:
        # Aguarda a caixa de mensagem aparecer e envia a mensagem
        caixa_mensagem = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p")
        caixa_mensagem.send_keys(Keys.ENTER)
        print(f"Mensagem enviada para {numero}")
    except Exception as e:
        print(f"Erro ao enviar para {numero}: {e}")

    time.sleep(5)

driver.quit()