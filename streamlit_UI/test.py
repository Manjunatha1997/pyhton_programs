import os


from datetime import date
import pandas as pd
from csv import writer



def create_csv():
    today_date = date.today()
    today_date = str(today_date)
    today_date_csv_file = today_date+'.csv'

    if not os.path.exists(today_date_csv_file):
        with open(today_date_csv_file, 'w') as f:
            f.write('inference_images,status,reason')



def add_data(inference_images,status,reason):
    today_date = date.today()
    today_date = str(today_date)
    today_date_csv_file = today_date+'.csv'

    with open(today_date_csv_file, 'a', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow([inference_images,status,reason])  
        # Close the file object
        f_object.close()


data = pd.read_csv(r'D:\python_programs\streamlit_UI\reports\2022-05-18.csv')



