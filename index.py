from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.viajesexito.com/")

paquetes = driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]/a/p')
paquetes.click()

time.sleep(2)

llegando = 'Punta Cana'
salida = driver.find_element(By.XPATH, '//*[@id="CityPredictiveTo_netactica_airhotel"]')
salida.click()

salida.send_keys(llegando)

time.sleep(2)

city = driver.find_element(By.XPATH, '/html/body/ul[21]/li/a/table/tbody/tr/td[2]')
city.click()

time.sleep(2)

exit = driver.find_element(By.XPATH, '//*[@id="DateFrom_netactica_airhotel"]')
exit.click()

time.sleep(2)

dia = driver.find_element(By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[3]/td[3]/a')
dia.click()

time.sleep(2)

dia2 = driver.find_element(By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[4]/td[4]/a')
dia2.click()

time.sleep(2)

habitacion = driver.find_element(By.XPATH, '//*[@id="txtNumPassengersPaquetesComplete"]')
habitacion.click()

time.sleep(2)

adulto = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/span[2]/button')
adulto.click()

time.sleep(2)

aplicar = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/header/button/span')
aplicar.click()

time.sleep(2)

buscar = driver.find_element(By.XPATH, '//*[@id="sbm_netactica_airhotel"]')
buscar.click()

time.sleep(25)

price1 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
print("------------PRIMER PRECIO POR PAQUETES------------------")
print(price1.text)

price2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
print("------------SEGUNDO PRECIO POR PAQUETES------------------")
print(price2.text)

price3 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[3]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
print("------------TERCERO PRECIO POR PAQUETES------------------")
print(price3.text)

price4 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[4]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
print("------------CUARTO PRECIO POR PAQUETES------------------")
print(price4.text)

price5 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[5]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
print("------------QUINTO PRECIO POR PAQUETES------------------")
print(price5.text)

price6 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[6]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
print("------------SEXTO PRECIO POR PAQUETES------------------")
print(price6.text)

price7 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[7]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
print("------------SEPTIMO PRECIO POR PAQUETES------------------")
print(price7.text)

price8 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[8]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
print("------------OCTAVO PRECIO POR PAQUETES------------------")
print(price8.text)

price9 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[9]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
print("------------NOVENO PRECIO POR PAQUETES------------------")
print(price9.text)

price10 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[10]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
print("------------DECIMO PRECIO POR PAQUETES------------------")
print(price10.text)

time.sleep(2)

vuelo = driver.find_element(By.XPATH, '//*[@id="txtAirlineCode"]')
vuelo.click()

aero = 'Copa Airlines'
time.sleep(2)

vuelo.send_keys(aero)

time.sleep(2)

vuelos = driver.find_element(By.XPATH, '/html/body/ul[3]/li/a')
vuelos.click()

time.sleep(2)

buscar2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
buscar2.click()

time.sleep(2)

driver.quit()