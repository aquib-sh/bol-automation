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
        data_size = len(self.data[self.cols[0]])
        for i in range(0, data_size):
            row = self.data.iloc[i]
            yield {
                self.cols[0]: row[self.cols[0]], 
                self.cols[1]: row[self.cols[1]],
                self.cols[2]: row[self.cols[2]],
                self.cols[3]: row[self.cols[3]]
            }

           