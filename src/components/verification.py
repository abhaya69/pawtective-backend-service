from models import model
import requests
from uuid import uuid4
import json

async def verifyCkyc(requestData : model.InputCKYCVerification) -> model.OutputCKYCVerification:
    data = {
        "req_id":str(uuid4()),
        "customer_type":"I",
        "id_type":"PAN",
        "id_num":requestData.pan_number,
        "full_name":requestData.pet_parent_name,
        "gender":requestData.pet_parent_gender,
        "dob":requestData.pet_parent_dob.replace("/",'-'),
        "url_type":"P"
    }
    url="https://fglpg001.futuregenerali.in/NLCKYC/API/CKYC/CreateCKYC"
    resp=requests.post(url,json=data)
    if resp.status_code == 200:
        ckycVerificationResponse = model.CKYCVerificationResponse(**json.loads(resp.text))
        ckycVerificationResponse.status_code=200
    else:
        print(resp.status_code,resp.text)
        raise Exception("HTTP Request Error")

    output = model.OutputCKYCVerification()
    output.first_name=ckycVerificationResponse.result.first_name
    output.middle_name=ckycVerificationResponse.result.middle_name
    output.last_name=ckycVerificationResponse.result.last_name
    output.dob=ckycVerificationResponse.result.dob
    output.email=ckycVerificationResponse.result.email.lower()
    output.ckyc_number=ckycVerificationResponse.result.ckyc_number
    output.pincode=ckycVerificationResponse.result.pincode
    output.customer_address=ckycVerificationResponse.result.customer_address
    output.customer_permanant_address=ckycVerificationResponse.result.customer_permanant_address

    return output

