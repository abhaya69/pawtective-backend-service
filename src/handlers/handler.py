import json
from models import model
from components import premium_calculator,verification,payment_gateway
from fastapi.responses import HTMLResponse
import config

async def getTotalPremium(requestData : model.InputPremiumInfo) -> model.PremiumDetails:
    premiumDetails = await premium_calculator.calculateTotalPremium(requestData)
    return premiumDetails

async def verifyCKYC(requestData : model.InputCKYCVerification) -> model.OutputCKYCVerification:
    ckycResult = await verification.verifyCkyc(requestData)
    return ckycResult

async def generatePaymentLink(requestData : model.InputPaymentDetails) -> model.OutputPaymentDetails:
    url = config.BASE_API_URL+"/api/makePayment?pet_parent_first_name={}&pet_parent_last_name={}&pet_parent_mobile={}&pet_parent_email={}&final_premium={}".format(
                    requestData.pet_parent_first_name,
                    requestData.pet_parent_last_name,
                    requestData.pet_parent_mobile,
                    requestData.pet_parent_email,
                    str(requestData.final_premium)
                )
    return {
        "url":url
    }

async def generatePaymentPage(
    pet_parent_first_name : str,
    pet_parent_last_name : str,
    pet_parent_mobile : str,
    pet_parent_email : str,
    final_premium : str
):
    paymentPage = await payment_gateway.generatePaymentPage(
        pet_parent_first_name,
        pet_parent_last_name,
        pet_parent_mobile,
        pet_parent_email,
        final_premium
    )
    return paymentPage

# async def handlePaymentResponse(requestBody):
    
