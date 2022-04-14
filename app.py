import pandas

import config
from bol import BolManager
from datetime_util import DatetimeOperator
from io_handler import CSVReader
from log import Logger
from processor import BolDataProcessor
from tokn import TokenRetriever


class BolApp:
    def __init__(self):
        self.log = Logger()

        self.log.info('Initializing...')
        rtr = TokenRetriever(config.TOKEN_PATH)
        self.manager = BolManager(rtr.get_api_id(), rtr.get_api_secret())
        self.reader = CSVReader(config.INPUT_PATH, config.COLUMNS)
        self.log.info(f"Loaded {config.INPUT_PATH}")

        self.dop = DatetimeOperator()
        self.processor = BolDataProcessor(self.log) # init with empty data
        self.__dict = {
            "search term": [],
            "NL total": [],
            "BE total": [],
            "week": [],
            "year": [],
        }
        self.__dict_keys = list(self.__dict.keys())
        
    def __export_data(self, filename):
        pandas.DataFrame(self.__dict).to_csv(filename, index=False)

    def run(self):
        for row in self.reader.readrow():
            term = row[config.COLUMNS[0]]
            week_start = row[config.COLUMNS[1]]
            week_end = row[config.COLUMNS[2]]
            year = row[config.COLUMNS[3]]

            # absolute week start
            abs_week_start = self.dop.week_difference(week_start, year)

            # get all the data for that search term
            status, data = self.manager.search_term_wr(term, abs_week_start)
            if (status == 200):
                self.log.info(f"Fetched data for {term}")
            else:
                self.log.error(f"Unable to fetch data for {term}, returned with {status}")
                continue

            # get info with filtered data uptil week_end
            self.processor.filter_data_by_end_week(data, week_end, year, self.__dict)

            # extract related terms from the data 
            related_terms = self.processor.get_related_search_terms(data)

            # get individual data for each term and concat it to previous info
            for term in related_terms:
                status, data = self.manager.search_term(term, abs_week_start)
                if (status == 200):
                    self.log.info(f"Fetched data for {term}")
                else:
                    self.log.error(f"Unable to fetch data for {term}")
                    continue

                # Add the filtered data to final dict
                self.processor.filter_data_by_end_week(data, week_end, year, self.__dict)

            self.log.debug(f"SizeOf final_info list {len(self.__dict[self.__dict_keys[0]])}")

        output_file = "results" + self.dop.get_timestamp_str() + ".csv"
        self.__export_data(output_file)
        self.log.info(f"Sucessfully exported the results to {output_file}")


if __name__ == "__main__":
    app = BolApp()
    app.run()
