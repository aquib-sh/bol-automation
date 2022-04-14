class BolDataProcessor:
    def __init__(self, data:dict):
        self.data = data

    def set_data(self, data:dict):
        self.data = data

    def get_related_search_terms(self) -> list:
        """Returns a list of related seach terms from data."""
        related_terms = []
        related_search_term_data = data['searchTerms']['relatedSearchTerms']
        for term in related_search_term_data:
            related_terms.append(term['searchTerm'])
        return related_terms
    
    def filter_data_by_end_week(self,  end_week, end_year) -> dict:
        """Filters data to get only up till the end of specified week of that year.

        Parameters
        ----------
        end_week: int
            Ending week till where data is to be extracted.

        end_year: int
            Year of that week.

        Returns
        -------
        data: dict
            A dictionary of lists with keys ["search term", "NL total", "BE total", "week", "year"]
        """
        _dict = {
            "search term" : [],
            "NL total" : [],
            "BE total" : [],
            "week" : [],
            "year" : []
        }
        term = search_results['searchTerms']['searchTerm']
        for period in search_results['searchTerms']['periods']:
            week = period['period']['week']
            year = period['period']['year']

            NL_total = period['countries'][0]['value']
            BE_total = period['countries'][1]['value']

            _dict['search term'].append(term)
            _dict['NL total'].append(NL_total)
            _dict['BE total'].append(BE_total)
            _dict['week'].append(week)
            _dict['year'].append(year)

            # If we have reached the desired week of the year then break
            if (week == end_week and year == end_year):
                break

        return _dict
