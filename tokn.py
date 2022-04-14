import json


class TokenRetriever:
    def __init__(self, token_file):
        self.token_file = token_file
        self.__api_id = None
        self.__api_secret = None
        self.__retrieve()

    def __retrieve(self):
        fp = open(self.token_file, "r")
        data = json.loads(fp.read())
        self.__api_id = data["API_ID"]
        self.__api_secret = data["API_SECRET"]

    def get_api_id(self):
        return self.__api_id

    def get_api_secret(self):
        return self.__api_secret
