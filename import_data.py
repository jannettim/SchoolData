import pandas
import os

def read_all_data(filepath, output_file, dlm="\t", encoding="utf-8"):

    f_path = filepath
    f_list = os.listdir(f_path)

    all_df = []
    count = 0
    for f in f_list:
        if count == 0:
            all_df = pandas.read_excel(os.path.join(f_path, f), "Export",
                                       names=["Geo_Id", "Geography", "Total_Est", "Total_MOE", "White_est", "White_MOE",
                                              "Black_Est", "Black_MOE", "AI_AN_EST", "AI_AN_MOE", "Asian_Est",
                                              "Asian_MOE", "PI_Est", "PI_MOE", "Other_Est", "Other_MOE", "Two_Est",
                                              "Two_MOE", "Two_Other_Est", "Two_Other_MOE", "Three_Est", "Three_MOE"],
                                       skiprows=10, header=None)
            count += 1
        else:
            df = pandas.read_excel(os.path.join(f_path, f), "Export",
                                   names=["Geo_Id", "Geography", "Total_Est", "Total_MOE", "White_est", "White_MOE",
                                          "Black_Est", "Black_MOE", "AI_AN_EST", "AI_AN_MOE", "Asian_Est", "Asian_MOE",
                                          "PI_Est", "PI_MOE", "Other_Est", "Other_MOE", "Two_Est", "Two_MOE",
                                          "Two_Other_Est", "Two_Other_MOE", "Three_Est", "Three_MOE"], skiprows=10,
                                   header=None)

            all_df = pandas.concat([all_df, df])

    all_df.reset_index(inplace=True)
    all_df.drop("index", inplace=True, axis=1)
    all_df.to_csv(output_file, sep=dlm, encoding=encoding)
    return all_df

read_all_data("data_download", "data\\all_school_districts.txt")