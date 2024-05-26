from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class scrapWeb():

    def get_web():
        driver = webdriver.Chrome()

        try:

            driver.get("https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros")
            # driver.implicitly_wait(30)
            # html_content = driver.page_source

            wait = WebDriverWait(driver, 10)
            field_id = driver.find_element(By.ID, 'mat-input-1')
            field_id.send_keys('0968599020001')  # Reemplaza

            submit_button = driver.find_element(By.CLASS_NAME, 'boton-buscar')  # Reemplaza
            submit_button.click()
            wait = WebDriverWait(driver, 100)
            driver.implicitly_wait(30)

            # submit_button = driver.find_element(By.CLASS_NAME, 'causa-individual')  # Reemplaza
            # submit_button.click()
            # Esperar a que la siguiente página cargue, si es necesario
            wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            elements = driver.find_elements(By.CLASS_NAME, "detalle")
            for element in elements:
                print(str(element))

                # if not element.is_selected():
                #     element.click()
                #     WebDriverWait(driver, 30)
                #     print('si click')
                # else:
                #     print('no click')
                #     None
            html_content = driver.page_source
            # print(str(elements))
            return {html_content}

        finally:
            # Cerrar el navegador
            driver.quit()

    def dend_form():
        driver = webdriver.Chrome()

        try:
            # Navegar a la página
            driver.get('https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros')

            # Esperar a que el formulario esté presente
            # wait = WebDriverWait(driver, 10)
            form_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'form')))

            # Llenar los campos del formulario
            nombre_input = driver.find_element(By.NAME, 'nombre')  # Reemplaza 'nombre' con el nombre real del input
            nombre_input.send_keys('Juan Pérez')  # Reemplaza 'Juan Pérez' con el valor que deseas enviar

            email_input = driver.find_element(By.NAME, 'email')  # Reemplaza 'email' con el nombre real del input
            email_input.send_keys('juan.perez@example.com')  # Reemplaza 'juan.perez@example.com' con el valor que deseas enviar

            # Encontrar el botón de envío y hacer clic
            submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')  # Reemplaza 'button[type="submit"]' con el selector adecuado
            submit_button.click()

            # Esperar a que la siguiente página cargue, si es necesario
            wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            # Obtener el HTML de la nueva página
            html_content = driver.page_source
            print(html_content)

        finally:
            # Cerrar el navegador
            driver.quit()
