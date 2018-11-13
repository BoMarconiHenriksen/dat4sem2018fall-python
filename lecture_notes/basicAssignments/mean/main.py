""" 
The url to run this program use this url:
https://raw.githubusercontent.com/rmlassesen/dataset/master/p_pladser.csv
"""
import downloader as download
import convert_csv as convert_csv
import mean as mean

if __name__ == '__main__':
    global file_name
    data_income_file = download.download_file()

data = convert_csv.convert_csv_to_dataframe(data_income_file)

mean.mean_find(data)
