from pydantic import BaseModel
from typing import List

class Addons(BaseModel):
    tp_cover : str = None
    lost_stolen_cover : str = None
    vet_cosultation_cover : str = None
    emergency_miniding_cover : str = None

class InputPremiumInfo(BaseModel):
    pet_age : str = None
    pet_breed_category : str = None
    sum_insured : int = None
    addons : Addons = None

class PremiumDetails(BaseModel):
    sum_insured : float = 0
    premium_amount : float = 0
    gst_details : float = 0
    tp_cover : float = 0
    lost_stolen_cover : float = 0
    vet_cosultation_cover : float = 0
    emergency_miniding_cover : float = 0
    gross_total : float = 0
    final_premium : float = 0

class InputCKYCVerification(BaseModel):
    pan_number : str = None
    pet_parent_dob : str = None
    pet_parent_gender : str = None
    pet_parent_name : str = None

class CKYCResult(BaseModel):
    customer_name : str = None
    first_name : str = None
    middle_name : str = None
    prefix : str = None
    last_name : str = None
    dob : str = None
    ckyc_number : str = None
    email : str = None
    pan : str = None
    customer_address : str = None
    customer_permanant_address : str = None
    kyc_date : str = None
    updated_date : str = None
    kyc_verify_agency_name : str = None
    cin : str = None
    doi : str = None
    pincode : str = None
    kyc_status : str = None
    id_num : str = None
    id_type : str = None

class CKYCVerificationResponse(BaseModel):
    req_id : str = None
    success : bool = False
    Final_Status : str = None
    error_message : str = None
    ckyc_remarks : str = None
    result : CKYCResult = None
    proposal_id : str = None
    customer_type : str = None
    url : str = None
    url_expiry : str = None
    status_code : str = None

class OutputCKYCVerification(BaseModel):
    first_name : str = None
    middle_name : str = None
    last_name : str = None
    dob : str = None
    email : str = None
    ckyc_number : str = None
    pincode : str = None
    customer_address : str = None
    customer_permanant_address : str = None

class InputPaymentDetails(BaseModel):
    metadata : dict = {}
    pet_parent_first_name : str = None
    pet_parent_last_name : str = None
    pet_parent_mobile : str = None
    pet_parent_email : str = None
    final_premium : float = 0

class OutputPaymentDetails(BaseModel):
    payment_link : str = None