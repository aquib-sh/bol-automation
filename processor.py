class BolDataProcessor:
    def __init__(self, logger):
        self.log = logger

    def set_data(self, data: dict):
        self.data = data

    def get_related_search_terms(self, data) -> list:
        """Returns a list of related seach terms from data."""
        related_terms = []
        related_search_term_data = data["searchTerms"]["relatedSearchTerms"]
        for term in related_search_term_data:
            related_terms.append(term["searchTerm"])
        return related_terms

    def filter_data_by_end_week(self, data, end_week, end_year, _dict=None) -> dict:
        """Filters data to get only up till the end of specified week of that year.

        Parameters
        ----------
        data: dict
            Dict from the returned JSON response of Bol API

        end_week: int
            Ending week till where data is to be extracted.

        end_year: int
            Year of that week.

        _dict: dict (OPTIONAL)
            Existing dictionary to add the new data

        Returns
        -------
        data: dict
            A dictionary of lists with keys ["search term", "NL total", "BE total", "week", "year"]
        """
        #self.log.debug(f"Filter data till {end_week}")
        if _dict == None:
            _dict = {
                "search term": [],
                "NL total": [],
                "BE total": [],
                "week": [],
                "year": [],
            }
        term = data["searchTerms"]["searchTerm"]
        for period in data["searchTerms"]["periods"]:
            week = int(period["period"]["week"])
            year = int(period["period"]["year"])

            NL_total = period["countries"][0]["value"]
            BE_total = period["countries"][1]["value"]

            _dict["search term"].append(term)
            _dict["NL total"].append(NL_total)
            _dict["BE total"].append(BE_total)
            _dict["week"].append(week)
            _dict["year"].append(year)

            #self.log.debug(f"Term {term}\t| Week {week}\t| Year {year}")
            # If we have reached the desired week of the year then break
            if week == end_week and year == end_year:
                #self.log.debug(f"Breaking out of filter at week {week}")
                break

        return _dict
