#!/usr/bin/env python
# coding: utf-8

# # Azure Cognitive Search with Translate Servces
# Using Azure Cognitive Search with Translate Servoces

import os
import requests 
import uuid, json
from dotenv import load_dotenv

#Translation endpoints
service_endpoint = "https://ul-translation-service.cognitiveservices.azure.com/" # for doc translation


key = os.getenv("AZURE_API_KEY")
path = "translator/text/batch/v1.1/batches"

#params = '&from=en&to=de&to=es&to=zh-Hans'
    
constructed_url = service_endpoint + path
print("url", constructed_url)

blob_sas_in = os.getenv("BLOB_SAS_IN")
blob_sas_out = os.getenv("BLOB_SAS_OUT")

body= {
    "inputs": [
        {
            "source": {
                "sourceUrl": blob_sas_in,
                "storageSource": "AzureBlob",
                "language": "en"   
            },
            "targets": [
                {
                    "targetUrl": blob_sas_out,
                    "storageSource": "AzureBlob",
                    "category": "general",
                    #"language": "es" # spanish
                    "language": "zh-Hans" # chinese simplified
                    #"language": "pt"      # portuguese brazil
                    #"language": "ja",      # japanese
                    #"language": "de"      # german
                    #"language": "de"      # german
                         
                }
            ]
        }

    ]
}
headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": 'application/json'
}

response = requests.post(constructed_url, headers=headers, json=body)
print("response:", response)
response_headers = response.headers
print(f'response status code: response.status_code)\nresponse status: {response.reason}\nresponse headers:\n') 

for key, value in response_headers.items():
    print(key, ":", value)




