from zipfile import ZipFile
import pandas as pd
file_path = r"C:\Users\Bhupendra\Desktop\DataCenter\EDA\COVID-19 Dataset.zip"
with ZipFile(file_path,'r') as zipp:
    zipp.printdir()
