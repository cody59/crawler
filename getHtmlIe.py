from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import IEDriverManager

driver = webdriver.Ie(service=Service(IEDriverManager().install()))