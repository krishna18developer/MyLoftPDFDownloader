import os
import requests

def download_files_from_file(file_name, folder_name):
    # Create a folder named "Applied Physics" if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Read URLs from the file
    with open(file_name, 'r') as file:
        url_list = file.readlines()

    # Download each file and save it in the folder
    for i, url in enumerate(url_list):
        url = url.strip()  # Remove leading/trailing whitespace and newline characters
        file_name = os.path.join(folder_name, f"{folder_name}_file_{i+1}.pdf")  # Naming the files as folder_name_file_1.pdf, folder_name_file_2.pdf, ...
        response = requests.get(url)
        with open(file_name, 'wb') as file:
            file.write(response.content)
            print(f"Downloaded {file_name}")

# File name containing URLs
file_name = 'url_list.txt'

# Folder name
folder_name = "Subjects/" + input("Subject Name : ")


# Call the function to download files
download_files_from_file(file_name, folder_name)