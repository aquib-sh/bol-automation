import config
from bol import BolManager
from datetime_util import DatetimeOperator
from io_handler import CSVReader
from tokn import TokenRetriever


class BolApp:
    def __init__(self):
        rtr = TokenRetriever(config.TOKEN_PATH)
        self.manager = BolManager(rtr.get_api_id(), rtr.get_api_secret())
        self.reader = CSVReader(config.INPUT_PATH, config.COLUMNS)
        self.dop = DatetimeOperator()

    def run(self):
        for row in self.reader.readrow():
            term = row[config.COLUMNS[0]]
            week_start = row[config.COLUMNS[1]]
            week_end = row[config.COLUMNS[2]]
            year = row[config.COLUMNS[3]]

            # absolute week start
            abs_week_start = self.dop.week(week_start, year)

            # get all the data for that search term
            data = self.manager.search_term_wr(term, abs_week_start)


if __name__ == "__main__":
    app = BolApp()
