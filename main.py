import requests, time, random, string, json

url = 'https://api.sharpspring.com/pubapi/v1/'

def gera_nome():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(10))

firstName = gera_nome()

def gera_email():
    first_name = gera_nome()
    domain = gera_nome() + ".com"
    return f"{first_name}@{domain}"

emailAddress = gera_email()

headers = {
    "id": "123",
    "Content-Type": "application/json",
}

query_params = {
    'accountID': '7CB1260E01C728EA9A185A3CED2C68D8',
    'secretKey': '03E5065CBFF46E2931B62E5A132FACE6'
}

body = {
    "method": "createLeads",
    "params": {
        "objects": [
            {
                "firstName": json.dumps(firstName),
                "lastName": json.dumps(firstName),
                "emailAddress": json.dumps(emailAddress)
            }
        ]
    },
    "id": "123"
}

def criar_lead(firstName, emailAddress):
    response = requests.post(url, params=query_params, headers=headers, json=body)
    print(response.status_code)
    print(response.text)
    print(firstName + " " + emailAddress)
    
count = 0
while count < 5:
    firstName = gera_nome()
    emailAddress = gera_email()
    time.sleep(2)
    criar_lead(firstName = firstName, emailAddress=emailAddress)
    time.sleep(10)
    count += 1