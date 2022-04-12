from token import TokenRetriever

from bol import BolManager


class BolApp:
    def __init__(self):
        rtr = TokenRetriever()
        self.manager = BolManager(rtr.get_api_id(), rtr.get_api_secret())
