import configparser

'''
Read in variables from config.ini file. Store them as global variables

Make sure to fill out your config.ini file!!!
'''
merchant_account = "AdyenRecruitment_SF1"
checkout_apikey = "AQEyhmfxLY3MaRVBw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFim1PUfJ3azpz0JSwoTTokD0QwV1bDb7kfNy1WIxIIkxgBw==-SUIUyEVq055RSiOgC88PEGIwU5WGvkhUakA39L9rpDM=-I?M;6BC<)~Zd[uvH"
client_key = "test_4M2YGRDFQFDIHLR3P23G5P45OYLRYX3Y"
supported_integrations = ['dropin']


def read_config():
    global merchant_account, checkout_apikey, client_key

    config = configparser.ConfigParser(interpolation=None)
    config.read('config.ini')

    merchant_account = config['DEFAULT']['merchant_account']
    checkout_apikey = config['DEFAULT']['checkout_apikey']
    #checkout_api labeled the wrong key in the SDK 
    client_key = config['DEFAULT']['client_key']

    # Check to make sure variables are set
    if not merchant_account or not checkout_apikey or not client_key:
        raise Exception("Please fill out information in config.ini file")
