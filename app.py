from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests

subject = input("Enter Name Of Subject : ")

def scrape_urls():
    
    options = webdriver.EdgeOptions()
    options.add_argument("user-data-dir=/Users/krishnateja/Library/Application Support/Microsoft Edge/Profile 1")
    driver = webdriver.Edge(options=options)

    try:
        driver.get("https://app.myloft.xyz/browse/favourite/all?tab=1")
        
        input("Start?")
        
        divs = driver.find_elements(By.XPATH,'//h4[contains(text(), "'+ subject +'")]')

        url_list = []

        for div in divs:
            
            div.click()

            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

            driver.switch_to.window(driver.window_handles[1])
            
            url = driver.current_url
            url_list.append(url)

            
            driver.close()

            driver.switch_to.window(driver.window_handles[0])
        return url_list

    finally:
        driver.quit()


def save_urls_to_file(url_list, file_name):
    with open(file_name, 'w') as file:
        for url in url_list:
            file.write(url + '\n')
            
def download_files_from_file(file_name, folder_name):
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    
    with open(file_name, 'r') as file:
        url_list = file.readlines()

    
    for i, url in enumerate(url_list):
        url = url.strip()  
        file_name = os.path.join(folder_name, f"{subject}_file_{i+1}.pdf")  
        response = requests.get(url)
        with open(file_name, 'wb') as file:
            file.write(response.content)
            print(f"Downloaded {file_name}")




urls = scrape_urls()
save_urls_to_file(urls, 'url_list.txt')

file_name = 'url_list.txt'
folder_name = "Subjects/" + subject

download_files_from_file(file_name, folder_name)