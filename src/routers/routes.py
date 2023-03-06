import asyncio
import time
from uuid import uuid4

from fastapi import FastAPI,Request,Header,Response
from fastapi.responses import HTMLResponse

from fastapi import APIRouter,BackgroundTasks

from handlers import handler
from models import exceptions
from models import model
from utils import util

from uuid import uuid4
import traceback
import hashlib



router=APIRouter()


@router.post("/webhook")
async def webhook():
    pass

@router.post("/getTotalPremium")
async def getTotalPremium(requestData : model.InputPremiumInfo):
    try:
        print("Input",requestData.dict())        
        responseData = await handler.getTotalPremium(requestData)
        responseData = await util.convertToString(responseData.dict())
        print("Output",responseData)
        return {
            "data":responseData,
            "success":True,
            "error":None
        }
    except exceptions.HandledExceptions as e:
        print(traceback.format_exc())
        print("Error in getTotalPremium : "+str(e))
        return {
            "data":None,
            "success":False,
            "error":e.message,
        }
    except Exception as e:
        print(traceback.format_exc())
        print("Error in getTotalPremium : "+str(e))
        return {
            "data":None,
            "success":False,
            "error":"Internal Server Error"
        }

@router.post("/verifyCKYC")
async def verifyCKYC(requestData : model.InputCKYCVerification):
    try:
        print("Input",requestData.dict())         
        responseData = await handler.verifyCKYC(requestData)
        print("Output",responseData)
        return {
            "data":responseData,
            "success":True,
            "error":None
        }
    except exceptions.HandledExceptions as e:
        print("Error in verifyCkyc : "+str(e))
        print(traceback.format_exc())
        return {
            "data":None,
            "success":False,
            "error":e.message,
        }
    except Exception as e:
        print("Error in verifyCkyc : "+str(e))
        print(traceback.format_exc())
        return {
            "data":None,
            "success":False,
            "error":"Internal Server Error"
        }

@router.post("/getPaymentLink")
async def getPaymentLink(requestData : model.InputPaymentDetails):
    try:
        print("Input",requestData.dict())         
        responseData = await handler.generatePaymentLink(requestData)
        print("Output",responseData)
        return {
            "data":responseData,
            "success":True,
            "error":None
        }
    except exceptions.HandledExceptions as e:
        print("Error in getPaymentLink : "+str(e))
        print(traceback.format_exc())
        return {
            "data":None,
            "success":False,
            "error":e.message,
        }
    except Exception as e:
        print("Error in getPaymentLink : "+str(e))
        print(traceback.format_exc())
        return {
            "data":None,
            "success":False,
            "error":"Internal Server Error"
        }

@router.get("/makePayment", response_class=HTMLResponse)
async def makePayment(
    pet_parent_first_name : str,
    pet_parent_last_name : str,
    pet_parent_mobile : str,
    pet_parent_email : str,
    final_premium : str
):
    try:
        print("Input: ",pet_parent_first_name,pet_parent_last_name,pet_parent_mobile,pet_parent_email,final_premium)        
        responseData = await handler.generatePaymentPage(
            pet_parent_first_name,
            pet_parent_last_name,
            pet_parent_mobile,
            pet_parent_email,
            final_premium
        )
        print("Output",responseData)
        return responseData
    except exceptions.HandledExceptions as e:
        print("Error in generatePaymentPage : "+str(e))
        print(traceback.format_exc())
        return "<h1>Internal Server Error</h1>"
    except Exception as e:
        print("Error in generatePaymentPage : "+str(e))
        print(traceback.format_exc())
        return "<h1>Internal Server Error</h1>"
    
# @router.get("/paymentResponse")
# async def paymentResponse(
#     WS_P_ID : str,
#     TID : str,
#     PGID : str,
#     Premium : str,
#     Response : str
# ):
#     try:        
#         responseData = await handler.generatePaymentLink(requestData)

#         return {
#             "data":responseData,
#             "success":True,
#             "error":None
#         }
#     except exceptions.HandledExceptions as e:
#         print("Error in getPaymentLink : "+str(e))
#         return {
#             "data":None,
#             "success":False,
#             "error":e.message,
#         }
#     except Exception as e:
#         print("Error in getPaymentLink : "+str(e))
#         return {
#             "data":None,
#             "success":False,
#             "error":"Internal Server Error"
#         }


