import base64

import requests


class BolManager:
    def __init__(self, _id, secret):
        self.__token = self.__get_token(_id, secret)
        self.host = "https://api.bol.com"
        self.__header = {
            "Accept": "application/vnd.retailer.v6+json",
            "Content-Type": "N/A",
            "Authorization": f"Bearer {self.__token}",
        }

    def __get_token(self, _id, token) -> str:
        """Fetches access token from Bol API

        Parameters
        ----------
        _id:  str
            API_ID of Bol API

        token: str
            API_SECRET of Bol API

        Returns
        --------
        access_token: str
            A new access token to be used for accessing retailer API.
        """
        cred = _id + ":" + token
        cred_bytes = cred.encode("ascii")
        # encode the creds to base 64
        b64cred_bytes = base64.b64encode(cred_bytes)
        b64cred = b64cred_bytes.decode("ascii")

        header = {"Authorization": "Basic " + b64cred}
        link = "https://login.bol.com/token?grant_type=client_credentials"

        req = requests.post(link, headers=header)
        resp = eval(req.content.decode())

        return resp["access_token"]

    def search_term(self, term, period=2) -> dict:
        """Fetches insights for a search term excluding the related terms.

        Parameters
        ----------
        term: str
            Search term that you want to get insights for

        period: int (DEFAULT=2)
            Period back in terms of week which you want insights for.
            suppose you want sights for current week and previous week,
            so we will put period=2

        Returns
        -------
        results: dict
            fetched info on insights about the search term
        """
        path = f"/retailer/insights/search-terms?search-term={term}&period=WEEK&number-of-periods={period}&related-search-terms=false"
        req = requests.get(self.host + path, headers=self.__header)
        results = eval(req.content.decode())
        return (req.status_code, results)

    def search_term_wr(self, term, period=2) -> dict:
        """Fetches insights for a search term including the related terms.

        Parameters
        ----------
        term: str
            Search term that you want to get insights for

        period: int (DEFAULT=2)
            Period back in terms of week which you want insights for.
            suppose you want sights for current week and previous week,
            so we will put period=2

        Returns
        -------
        results: dict
            fetched info on insights about the search term
        """
        path = f"/retailer/insights/search-terms?search-term={term}&period=WEEK&number-of-periods={period}&related-search-terms=true"
        req = requests.get(self.host + path, headers=self.__header)
        results = eval(req.content.decode())
        return (req.status_code, results)

    def get_orders(self) -> str:
        """Fetch all the order details."""
        path = "https://api.bol.com/retailer/orders"
        req = requests.get(path, headers=self.__header)
        results = req.content.decode()
        return results
