import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "26515107"))
    API_HASH = os.environ.get("API_HASH", "71c39ddb9da42a66087c3b4cf57e21c3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5658850018:AAEakf_LvYodlptYAlBTWlh_YK8hVz5fxe8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHwBuw7PaUudHaup_FaZdjZaC58CHodKHmralXg_JLJWMR212JoEVC7WflMvNPU_SM4HPXPxn_OQpLOFBDorEOeEnj1NDQk27s8qiw5pjjGgmVdWbxa3fD94UFASRckh1TncLAZSRLBhJWrsjVYjdXMZd0BJvpspZyXzPUF2-7d-NPTmLSGXT8l2bOrlv0CVCOqkOe5tEPM8OV17VfQCIVEMoccYM5iKVMEtlCFCxJIEn7ymTWjAfCEorDlm4xjOjGTbVK3de_YARBFkkO7pGMRCYS_1OddSLDsNJVSsRi5WxZYEtJHNU1MwSbv18jZG36KNMkLgBmWL1i1DlhXNhifiZgY=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("Jubismusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "jubistalk") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Jonathaan_swift") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("5519737346")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
