import requests
import json
from flask import Flask, request

app = Flask(__name__)
hdr = { 'Content-Type': 'application/json' }

@app.route('/status', methods=['POST'])
def returnstatus():
    try:
        reqjson = json.loads(request.data)
        urn = reqjson["urn"]
    except:
        return("Invalid Request")
    resp = requests.post('https://www.fdmerchantservices.com/MerchantOnBoarding/inquiryService', headers=hdr, json={"urn": urn})
    return(resp.content)

if __name__ == '__main__':
    app.run(debug=True)
