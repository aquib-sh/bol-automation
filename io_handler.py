import pandas


class CSVReader:
    def __init__(self, input_file, columns):
        self.input_file = input_file
        self.data = self.__read()
        self.columns = columns

    def __read(self):
        return pandas.read_csv(self.input_file)

    def readrow(self):
        """Yields each row of dataframe one by one."""
        data_size = len(self.data[self.columns[0]])
        for i in range(0, data_size):
            row = self.data.iloc[i]
            yield {
                self.columns[0]: row[self.columns[0]],
                self.columns[1]: row[self.columns[1]],
                self.columns[2]: row[self.columns[2]],
                self.columns[3]: row[self.columns[3]],
            }
