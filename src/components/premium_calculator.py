from models import model
from config import PREMIUM_CONFIG
from models import exceptions



async def calculateTotalPremium(requestData : model.InputPremiumInfo) -> model.PremiumDetails:
    premiumDetails = model.PremiumDetails()

    if requestData.pet_breed_category not in PREMIUM_CONFIG:
        raise exceptions.InvalidInput('Invalid Category Provided')

    ageGroupData = PREMIUM_CONFIG[requestData.pet_breed_category]
    amountData=None
    for item in ageGroupData.keys():
        age = int(requestData.pet_age.split('Months')[0].split('-')[1])
        if age>=int(item.split('-')[0]) and age<=int(item.split('-')[1]):
            amountData = ageGroupData[item]
            break
    
    if not amountData:
        raise exceptions.InvalidInput('Invalid Age Provided for the Category')
    
    sum_insured = int(requestData.sum_insured.lower().replace('₹','').replace(' ','').replace('lakh','00000'))

    premiumDetails.sum_insured = sum_insured
    premiumDetails.premium_amount = sum_insured*amountData['bc'] + \
                                    sum_insured*amountData['b1'] + amountData['b2'] + amountData['b3']

    if requestData.addons:
        if requestData.addons.tp_cover=='Add':
            premiumDetails.tp_cover = sum_insured*amountData['tpa']
        if requestData.addons.lost_stolen_cover=='Add':
            premiumDetails.lost_stolen_cover = sum_insured*amountData['las']
        if requestData.addons.vet_cosultation_cover=='Add':
            premiumDetails.vet_cosultation_cover = amountData['vv']
        if requestData.addons.emergency_miniding_cover=='Add':
            premiumDetails.emergency_miniding_cover = amountData['em']

    premiumDetails.gross_total = premiumDetails.premium_amount+premiumDetails.tp_cover+ \
                                    premiumDetails.lost_stolen_cover+premiumDetails.vet_cosultation_cover+\
                                        premiumDetails.emergency_miniding_cover

    premiumDetails.gst_details = premiumDetails.gross_total*0.18
    premiumDetails.final_premium = premiumDetails.gross_total+premiumDetails.gst_details

    return premiumDetails