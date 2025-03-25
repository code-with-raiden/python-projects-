import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from JSON file
creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\SAGAR\\Desktop\\DJD-E1\\project\\axiomatic-array-454709-t1-65337db2aa02.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet (replace with your actual sheet name)
sheet = client.open("demo").sheet1  # Access first sheet

# Get all data from a specific column (e.g., Column A)
column_data = sheet.col_values(2)  # Column index starts from 1

print(column_data)  # Output will be a list


import webbrowser as web
from time import sleep
import pyautogui


def sendwhatsmsg(phone_no, message):
    Message = message
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(15)
    pyautogui.press('enter')




for i in column_data:
    sendwhatsmsg(i,"hello this a demo project")
    print("msg sent ")
print("done")



