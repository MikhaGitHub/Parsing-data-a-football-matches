from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd




custom_options = Options()
custom_options.add_argument("--start-maximized")
path_driver = Service(r"E:\Python\Devman\Parcing Dev\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=path_driver, options=custom_options)
ref = "https://www.flashscore.com.ua/"
driver.get(ref)

driver_m = driver.find_elements(By.CLASS_NAME,"event__match.event__match--twoLine")

results = []


for match in driver_m:
    result = match.text.splitlines()
    results.append(result)

list_matches = ["Status", "Team_1", "Team_2", "g_1", "g_2", "first_time_1", "first_time_2", "sl_1", "sl_2"]

df = pd.DataFrame(results, columns=list_matches)

drop_columns_list = ["sl_1", "sl_2"]
df = df.drop(drop_columns_list,axis=1)
df = df.loc[df['first_time_2'] < '(2)']
name = "file_test.xlsx"
df.to_excel(name, index=False)
print(df)

driver.quit()




