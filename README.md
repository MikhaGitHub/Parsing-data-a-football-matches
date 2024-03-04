# Parsing-data-a-football-matches
This progect parses data from a football match website using the Selenium library.
Written on python.
Data written in exel file.
Downloand and testing!
Step one:
Download a webdiriver(ChromeDriver):
1.Go on website and download same as your browser version
refs on all OS:
platform":"win64","url":"https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/win64/chromedriver-win64.zip"
platform":"win32","url":"https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/win32/chromedriver-win32.zip"
platform":"mac-x64","url":"https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/mac-x64/chromedriver-mac-x64.zip"
platform":"mac-arm64","url":"https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/mac-arm64/chromedriver-mac-arm64.zip"
platform":"linux64","url":"https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chromedriver-linux64.zip"
Its is curently versions webdrivers, for details here: "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"
# How download a libriary for work with parcing:
1.In terminal in your IDE write: pip install selenium
2.We'll import the libraries later:
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

