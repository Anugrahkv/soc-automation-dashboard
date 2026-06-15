import requests
import os

def query_abuseipdb(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'
    headers = {
        'Accept': 'application/json',
        'Key': os.getenv('ABUSEIPDB_API_KEY')
    }
    params = {'ipAddress': ip, 'maxAgeInDays': 90}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'type': 'ip', # Added this identifier
            'ip': data['data']['ipAddress'],
            'score': data['data']['abuseConfidenceScore'],
            'country': data['data']['countryCode']
        }
    return None

def query_virustotal(file_hash):
    url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
    headers = {
        'accept': 'application/json',
        'x-apikey': os.getenv('VIRUSTOTAL_API_KEY')
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        # Navigate the JSON tree to get to the analysis stats
        stats = data['data']['attributes']['last_analysis_stats']
        
        return {
            'type': 'hash', # Identifier for the frontend
            'malicious': stats.get('malicious', 0),
            'suspicious': stats.get('suspicious', 0),
            'undetected': stats.get('undetected', 0),
            'file_type': data['data']['attributes'].get('type_description', 'Unknown')
        }
    return None