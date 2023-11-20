import warnings
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

import requests


import os
import sys
__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])
warnings.filterwarnings("ignore")


import dependencias
from dependencias.WebDriverLocal import start_browser


def selenium(browser,downloadpath):
    '''

    [Descripcion]

    [Creación]

        1. Autor:  Wilber Lopez Mucia
        2. Dia de Creación: 15/08/2023
        3. Incident: Descarga graficas de diferentes paises en torno a los casos confirmados y las muertes confirmadas, desde el año 2020 hasta la fecha actual

            
    [Funciones]

        chance= cambiar de nombre los archivos descargados para death y confirmed,  y ubicarlos en sus respectivar carpetas 
                    
   

    ''' 

    #------------------------------------
    # FUNCIONES
    #------------------------------------
    
    def chance(downloadpath, downloadcases):

        #remplazar el nombre para confirmed deaths
        os.replace(os.path.join(downloadpath, "coronavirus-data-explorer.png"), os.path.join(downloadpath, "Confirmed_deaths_Fecha_Actual.png"))

        #remplazar el nombre para confirmed confirmed cases
        os.replace(os.path.join(downloadpath, "coronavirus-data-explorer(1).png"), os.path.join(downloadcases, "Confirmed_cases_Fecha_Actual.png"))
        

    #------------------------------------
    # MAIN
    #------------------------------------

    #------------------------------------
    # VARIABLES DE CONFIGURACION
    #----------------------------------------------------------------------------------------------------------------------------
    url='https://ourworldindata.org'
    final_path=os.path.join(path, "Final_path")
    #browser.get(url)
    
    

    ########################################################
    # verificar que la pagina este online
    ########################################################
    try:
        status_genereport=requests.get(url).status_code
    except:
        status_genereport=None
    if status_genereport!=200:
        raise ValueError('La página esta caida')
    else:
        browser.get(url)


    

    #realizar la busqueda de coronavirus
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, 'SiteSearchNavigation__mobile-toggle'))).click()
    
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/div[2]/div/div/div[3]/div[1]/input'))).clear()
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/div[2]/div/div/div[3]/div[1]/input'))).send_keys('coronavirus')

    #seleccionar la primera opción de la busqueda de coronavirus
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="postResults"]/ul/li[1]/a'))).click()

    #seleccionar data explorer
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, 'wp-block-owid-card'))).click()
    
    
    #seleccionar la opción de confirmed deaths
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'react-select-2-input'))).send_keys('Confirmed deaths')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'react-select-2-input'))).send_keys(Keys.RETURN)
    

    #seleccionar semanal como intervalo
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/form/div[2]/div[2]/div/div[1]/div'))).click()
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/form/div[2]/div[2]/div/div[1]/div[5]'))).click()       
    
    ##limpiar el campo de los paises 
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'button'))).click()   
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ClearSelectionButton'))).click()
    
    #seleccionar los paises de interes
    
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-field'))).send_keys('Brazil')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'name'))).click()

    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-field'))).send_keys('Colombia')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'name'))).click()

    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-field'))).send_keys('United Kingdom')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'name'))).click()
    
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-field'))).send_keys('United States')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'name'))).click()

    #opción log 
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[3]/div/div[2]/div/ul/li[1]/span/span[2]"))).click()
    #seleccionar por ciudad o por región
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="FacetStrategyDropdown"]/div[1]'))).click()    
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="FacetStrategyFloat"]/div[2]'))).click()

    #Download
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '//nav[@class="tabs"]/ul/li[5]'))).click()
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'grouped-menu-icon'))).click()

    #---------------------Confirmed Cases---------------------------------------------------------------------
    #reload  pargina para seleccionar la segunda parte del ejercicio
    browser.refresh()

    #seleccionar la opción de confirmed cases
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'react-select-2-input'))).send_keys('Confirmed cases')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'react-select-2-input'))).send_keys(Keys.RETURN)     
     

    ##limpiar el campo de los paises 
    
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ClearSelectionButton'))).click()
    
    #seleccionar los paises de interes
    
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-field'))).send_keys('Argentina')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'name'))).click()

    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-field'))).send_keys('Brazil')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'name'))).click()

    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-field'))).send_keys('Chile')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'name'))).click()
    
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-field'))).send_keys('Colombia')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'name'))).click()

    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-field'))).send_keys('Ecuador')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'name'))).click()

    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-field'))).send_keys('Peru')
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'name'))).click()

    #seleccionar cumulativo como intervalo
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/form/div[2]/div[2]/div/div[1]/div'))).click()
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/form/div[2]/div[2]/div/div[1]/div[2]'))).click()
    
    
    #Download
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '//nav[@class="tabs"]/ul/li[5]'))).click()
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'grouped-menu-icon'))).click()

    return chance

  
        # ----------------------------------------------------------------------------------------------------------------------------
    


if __name__ == '__main__':
    downloadpath = os.path.join(path, "Confirmed Deaths")
    nombre_carpeta = "Confirmed Cases"
    # Crear la carpeta si no existe
    if not os.path.exists(nombre_carpeta):
        os.mkdir(nombre_carpeta)
    mozilla_bin = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = start_browser(downloadpath, mozilla_bin)
    chance_func = selenium(browser, downloadpath)
    chance_func(downloadpath, ".\Confirmed Cases")
    
