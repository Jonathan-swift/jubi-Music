import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "26515107"))
    API_HASH = os.environ.get("API_HASH", "71c39ddb9da42a66087c3b4cf57e21c3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5658850018:AAEakf_LvYodlptYAlBTWlh_YK8hVz5fxe8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHwBu4vVddP9tw-tTxnJHJY9IdxTMGOS3kZJY1YmwBQAwDM2clP6BYKcFW3bOwe9S_hj35_aOdp6_qqcbwVarHMkBVt9i6pRE3pJWDoAUecV1UAdo6j_KG2MzsM_96atc-7N82ojXA03X9Mdd7PJvWllbuF5_VGEH7zgJXT0ZFF6qc54ezcV6tR2FJCYIvR9MY8GTW5TE5KzdAiV0kHRJ7nVRmAkjt1dVgA2QM70LRXQHQPVCUdITwXPYE4481prD95lzBSrC1HRVyJhg886Rwr9sTN13ZX4jqQWsdK2q_JnVozQnHzS_EZ745sN8dQhfdh8rEfc5uh2mt2njp8jZ7YU1EA=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("Jubismusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "jubistalk") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Jonathaan_swift") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("5519737346")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
