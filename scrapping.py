from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def scraping_web():
    # Configuración de opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecuta Chrome en modo headless (sin interfaz gráfica)

    # Ruta al ChromeDriver
    chrome_service = Service('/usr/local/bin/chromedriver')  # Reemplaza con la ruta correcta

    # Inicializa el navegador
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # URL a scrapear
    url = 'https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros'
    driver.get(url)

    # Espera a que la página se cargue completamente
    driver.implicitly_wait(100)  # Puedes ajustar el tiempo según sea necesario

    # Obtiene el contenido HTML de la página
    html_content = driver.page_source

    # Cierra el navegador
    driver.quit()

    return {'html': html_content}

# Ejemplo de uso
if __name__ == "__main__":
    data = scraping_web()
    print(data['html'])
