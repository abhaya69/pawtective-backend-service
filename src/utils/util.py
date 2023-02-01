from uuid import uuid4
import hashlib
import config

async def generate_checksum(
    pet_parent_mobile : str,
    final_premium : float,
    pet_parent_first_name : str,
    pet_parent_last_name : str,
    pet_parent_email : str
):
    # TransactionID|PaymentOption|ResponseURL|ProposalNumber|PremiumAmount|UserIdentifier|UserId| FirstName|LastName|Mobile|Email|
    cvfutureTransactionID = str(uuid4())
    cvfuturePaymentOption = "3"
    cvfutureResponseURL = config.BASE_API_URL+"/api/paymentResponse"
    cvfutureProposalNumber = pet_parent_mobile
    cvfuturePremiumAmount = final_premium
    cvfutureUserIdentifier = pet_parent_mobile
    cvfutureUserId = pet_parent_mobile
    cvfutureFirstName = pet_parent_first_name
    cvfutureLastName = pet_parent_last_name
    cvfutureMobile = pet_parent_mobile
    cvfutureEmail = pet_parent_email

    _text=cvfutureTransactionID+'|'+ \
        cvfuturePaymentOption+'|'+ \
            cvfutureResponseURL+'|'+ \
                cvfutureProposalNumber+'|'+ \
                    cvfuturePremiumAmount+'|'+ \
                        cvfutureUserIdentifier+'|'+ \
                            cvfutureUserId+'|'+ \
                                cvfutureFirstName+'|'+ \
                                    cvfutureLastName+'|'+ \
                                        cvfutureMobile+'|'+ \
                                            cvfutureEmail+'|'
    print("Payload "+_text)
    checksum = hashlib.sha256(_text.encode('utf-8')).hexdigest()
    print("Checksum "+checksum)
    return checksum