import requests
import csv
import json
import xml.etree.ElementTree as ET
from io import StringIO

def download_data(api_url):
    response = requests.get(api_url)
    downloaded_data = {}
    
    if response.status_code == 200:
        data = response.content
        if 'json' in response.headers.get('Content-Type'):
            data = json.loads(data)
        elif 'xml' in response.headers.get('Content-Type'):
            root = ET.fromstring(data)
            data = [{elem.tag: elem.text for elem in child} for child in root]
        downloaded_data[api_url] = data
        print("Data downloaded successfully from", api_url)
    else:
        print("Failed to download data from", api_url)
        print("Status code:", response.status_code)
    
    return downloaded_data

def save_data_to_csv(downloaded_data, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for url, data in downloaded_data.items():
            for item in data:
                writer.writerow(item.values())

if __name__ == "__main__":
    group2_url = "http://35.174.107.106:3000/agreement"
    group4_url = "http://13.48.42.106:8000/request-details/"
    group3_offers_urls = [
        "http://ec2-54-147-16-17.compute-1.amazonaws.com:4000/users/offers?provider=A",
        "http://ec2-54-147-16-17.compute-1.amazonaws.com:4000/users/offers?provider=B",
        "http://ec2-54-147-16-17.compute-1.amazonaws.com:4000/users/offers?provider=C",
        "http://ec2-54-147-16-17.compute-1.amazonaws.com:4000/users/offers?provider=D"
    ]
    group3_agreement_bids_urls = [
        "http://ec2-54-147-16-17.compute-1.amazonaws.com:4000/users/Agreementbids?provider=A",
        "http://ec2-54-147-16-17.compute-1.amazonaws.com:4000/users/Agreementbids?provider=B",
        "http://ec2-54-147-16-17.compute-1.amazonaws.com:4000/users/Agreementbids?provider=C",
        "http://ec2-54-147-16-17.compute-1.amazonaws.com:4000/users/Agreementbids?provider=D"
    ]
    
    downloaded_data = {}
    
    # Download data from Group 2 API
    downloaded_data.update(download_data(group2_url))
    
    # Download data from Group 4 API
    downloaded_data.update(download_data(group4_url))
    
    # Download data from Group 3 APIs for offers
    for url in group3_offers_urls:
        downloaded_data.update(download_data(url))
    
    # Download data from Group 3 APIs for agreement bids
    for url in group3_agreement_bids_urls:
        downloaded_data.update(download_data(url))
    
    # Save the downloaded data to a CSV file
    save_data_to_csv(downloaded_data, "Final_data.csv")
