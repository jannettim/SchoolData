import pandas
import re

class CleanData:

    def __init__(self, filename, dlm="\t", encoding="utf-8"):

        self.filename = filename
        self.df = pandas.DataFrame.from_csv(self.filename, sep=dlm, encoding=encoding)

    def split_geo(self):


        temp_geo = self.df["Geography"].tolist()
        sd = [re.split(r",\s(?=\w\w$)", t)[0] for t in temp_geo]
        state = [re.split(r",\s(?=\w\w$)", t)[1] for t in temp_geo]
        self.df["School_District"] = sd
        self.df["state"] = state

    def write_file(self, outfile, dlm="\t", encoding="utf-8"):

        self.df.to_csv(outfile, sep=dlm, encoding=encoding)


cd = CleanData("data\\all_school_districts.txt")
cd.split_geo()
cd.write_file("data\\all_school_districts2.txt")