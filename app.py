from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_urls():
    # Initialize Edge WebDriver
    options = webdriver.EdgeOptions()
    options.add_argument("user-data-dir=/Users/krishnateja/Library/Application Support/Microsoft Edge/Profile 1")
    driver = webdriver.Edge(options=options)

    try:
        # Load the webpage
        driver.get("https://app.myloft.xyz/browse/favourite/all?tab=1")
        wait = input("wait")

        # Find all div elements containing the text "Applied Physics"
        subject = input("Enter Name Of Subject : ")
        divs = driver.find_elements(By.XPATH,'//h4[contains(text(), "'+ subject +'")]')

        # List to store the extracted URLs
        url_list = []

        # Iterate over each div
        for div in divs:
            # Click on the div
            div.click()

            # Wait until a new window is opened
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

            # Switch to the new window
            driver.switch_to.window(driver.window_handles[1])

            # Get the URL of the new window
            url = driver.current_url
            url_list.append(url)

            # Close the new window
            driver.close()

            # Switch back to the main window
            driver.switch_to.window(driver.window_handles[0])

        return url_list

    finally:
        # Close the WebDriver
        driver.quit()


def save_urls_to_file(url_list, file_name):
    with open(file_name, 'w') as file:
        for url in url_list:
            file.write(url + '\n')

# Call the function to save URLs to a file




# Call the function and print the list of URLs
urls = scrape_urls()

print(urls)
save_urls_to_file(urls, 'url_list.txt')
