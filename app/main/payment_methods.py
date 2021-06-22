import app.main.config as config
import Adyen
import json

'''
Retrieve available payment methods by calling /paymentMethods

Request only needs to include merchantAccount, but you can include more information to get a more refined response

Should have a payment state on your server from which you can fetch information like amount and shopperReference
'''


def adyen_payment_methods():
    adyen = Adyen.Adyen()
    adyen.client.platform = 'test'
    adyen.client.xapikey = config.checkout_apikey

    print(">>>>>>>> CONFIG")
    print(config.checkout_apikey)
    print(config.merchant_account)
    print(">>>>>>>> CONFIG")


    payment_methods_request = {
        'merchantAccount': config.merchant_account,
        'reference': 'Fusion paymentMethods call',
        'shopperReference': 'Cassies Checkout Shopper',
        'channel': 'Web',
    }
    
    print("/paymentMethods request:\n" + str(payment_methods_request))

    payment_methods_response = adyen.checkout.payment_methods(payment_methods_request)
    formatted_response = json.dumps((json.loads(payment_methods_response.raw_response)))
    
    print("/paymentMethods response:\n" + formatted_response)
    return formatted_response

def filter_unsupported_methods(adyen_result):
    pm_dict = json.loads(adyen_result.raw_response)
    pm_dict["paymentMethods"] = [value for value in pm_dict["paymentMethods"] if value["type"] in config.supported_integrations or value["type"] == "scheme"]
    new_string = json.dumps(pm_dict)
    return new_string