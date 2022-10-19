import openpyxl as openpyxl
from openpyxl.workbook import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
from email.message import EmailMessage
from datetime import datetime

# from Excel_function import exl_function, date

# Scraping the data from Amazon Website
driver = webdriver.Chrome(executable_path="C:\\Users\\Vikas Ahuja\\Downloads\\chromedriver.exe")
# webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in")
driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys("Samsung phones")
driver.find_element(By.XPATH, "//input[@id = 'nav-search-submit-button']").click()
phone_names = driver.find_elements(By.XPATH, "//span[contains(@class,'a-color-base a-text-normal')]")
# print("total Count:", len(phone_names))
prices = driver.find_elements(By.XPATH, "//span[contains(@class,'price-whole')]")
# exl_function('Samsung Data', 'Name', 'Price')
# # This Code will append data into the empty list
my_phone = []
my_price = []

for phone in phone_names:
    # print(phone.text)
    my_phone.append(phone.text)

print("------------------")

for price in prices:
    # print(price.text)
    my_price.append(price.text)

final_list = zip(my_phone, my_price)

# for data in list(final_list):
#   print(data)

# Appending the web scraping data into excel sheet
date = datetime.now().strftime("%Y_%m_%d-%I:%M")


def excel_function(titles, col1, col2):
    wb = Workbook()
    wb['Sheet'].title = titles
    sh1 = wb.active
    sh1.append([col1, col2])
    for data1 in list(final_list):
        sh1.append(data1)
    wb.save('FinalData' + date + '.xlsx')


excel_function('Samsung Data', 'Name', 'Price')

# Sending the Excel through Email
msg = EmailMessage()
msg['Subject'] = 'Webscraping Samsung Mobile data from Amazon Website into Excel Sheet'
msg['From'] = 'vikas.ahuja8343@gmail.com'
msg['To'] = 'ruchikaahuja.asm@gmail.com'

with open('EmailTemplate.txt') as my_file:
    data = my_file.read()
    msg.set_content(data)

with open('FinalData' + date + '.xlsx', "rb") as f:
    file_data = f.read()
    print("File data in binary", file_data)
    file_name = f.name
    print("File name is", file_name)
    msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login("vikas.ahuja8343@gmail.com", "rdgavgavctxzrdpu")
    server.send_message(msg)

print("Email sent !!!")
