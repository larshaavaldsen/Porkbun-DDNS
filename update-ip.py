import requests

# open IP file and check for changes 

file = open("ip.txt", 'w+')

ip = file.read().strip()

new_ip = requests.get('http://checkip.amazonaws.com').text.strip()

# logic for new ip
if ip != new_ip:
    print("new IP detected")

    # update ip.txt
    file.write(new_ip)
    
    # update DNS record
    json = {
            "secretapikey": "secretapikey",
            "apikey": "apikey",
            "content": new_ip,
            "ttl": "600"
        }
    
    update = requests.post('https://api.porkbun.com/api/json/v3/dns/editByNameType/DOMAIN/RECORDTYPE/SUBDOMAIN', json=json)

    print(update.status_code)
