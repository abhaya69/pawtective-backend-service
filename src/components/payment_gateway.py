from models import model
from utils import util
from uuid import uuid4
import config

async def generatePaymentPage(
    pet_parent_first_name : str,
    pet_parent_last_name : str,
    pet_parent_mobile : str,
    pet_parent_email : str,
    final_premium : str
):
    checksum = await util.generate_checksum(
        pet_parent_mobile = pet_parent_mobile,
        final_premium = final_premium,
        pet_parent_first_name = pet_parent_first_name,
        pet_parent_last_name = pet_parent_last_name,
        pet_parent_email = pet_parent_email
    )

    cvfutureTransactionID = str(uuid4())
    cvfuturePaymentOption = '3'
    cvfutureResponseURL = "https://webhook.site/ca5f5322-1786-478e-935d-a51b824c7280"
    # cvfutureResponseURL = config.BASE_API_URL+"/api/paymentResponse"
    cvfutureProposalNumber = pet_parent_mobile
    cvfuturePremiumAmount = final_premium
    cvfutureUserIdentifier = pet_parent_mobile
    cvfutureUserId = pet_parent_mobile
    cvfutureFirstName = pet_parent_first_name
    cvfutureLastName = pet_parent_last_name
    cvfutureMobile = pet_parent_mobile
    cvfutureEmail = pet_parent_email

    return """
    <html>
    <body onload="document.forms['cvfuturePaymentForm'].submit()">
    <form name="cvfuturePaymentForm" action="http://fglpg001.futuregenerali.in/Ecom_NL/WEBAPPLN/UI/Common/WebAggPayNew.aspx" method="post">
        <input type="hidden" id="cvfutureTransactionID" name="TransactionID" value="{}">
        <input type="hidden" id="cvfuturePaymentOption" name="PaymentOption" value="{}">
        <input type="hidden" id="cvfutureResponseURL" name="ResponseURL" value="{}">
        <input type="hidden" id="cvfutureProposalNumber" name="ProposalNumber" value="{}">
        <input type="hidden" id="cvfuturePremiumAmount" name="PremiumAmount" value="{}">
        <input type="hidden" id="cvfutureUserIdentifier" name="UserIdentifier" value="{}">
        <input type="hidden" id="cvfutureUserId" name="UserId" value="{}">
        <input type="hidden" id="cvfutureFirstName" name="FirstName" value="{}">
        <input type="hidden" id="cvfutureLastName" name="LastName" value="{}">
        <input type="hidden" id="cvfutureMobile" name="Mobile" value="{}">
        <!--input type="hidden" name="Vendor" value="webagg"-->
        <input type="hidden" id="cvfutureEmail" name="Email" value="{}">
        <input type="hidden" name="CheckSum" value="{}">
    </form>
    </body>
    </html>
    """.format(
        cvfutureTransactionID ,
        cvfuturePaymentOption ,
        cvfutureResponseURL ,
        cvfutureProposalNumber ,
        cvfuturePremiumAmount,
        cvfutureUserIdentifier,
        cvfutureUserId ,
        cvfutureFirstName ,
        cvfutureLastName,
        cvfutureMobile,
        cvfutureEmail ,
        checksum
    )