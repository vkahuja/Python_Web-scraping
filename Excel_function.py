# This Code will append data into the empty list
from datetime import datetime

from openpyxl.workbook import Workbook

from webScraping_amazon_excel_using_Selenium import phone_names, prices

my_phone = []
my_price = []

for phone in phone_names:
    my_phone.append(phone.text)

print("------------------")

for price in prices:
    my_price.append(price.text)

final_list = zip(my_phone, my_price)

# Appending the web scraping data into excel sheet
date = datetime.now().strftime("%Y_%m_%d-%I:%M")


def exl_function(titles, col1, col2):
    wb = Workbook()
    wb['Sheet'].title = titles
    sh1 = wb.active
    sh1.append([col1, col2])
    for data1 in list(final_list):
        sh1.append(data1)
        wb.save('FinalData' + date + '.xlsx')