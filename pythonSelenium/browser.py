from selenium import webdriver

# browser exposes an executable file
# through selenium test we need to invoke an executable file which will then invoke actual browser
# driver = webdriver.Chrome(executable_path=r"c:\\seleniumWebdrivers\chromedriver.exe")
# driver = webdriver.Firefox(executable_path=r"c:\\seleniumWebdrivers\geckodriver.exe")
driver = webdriver.Edge(executable_path=r"c:\\seleniumWebdrivers\msedgedriver.exe")

driver.maximize_window()
driver.get("https://www.coconutsoftware.com/")

print(driver.title)
print(driver.current_url)
driver.get("https://www.coconutsoftware.com/banks-and-credit-unions/")
driver.minimize_window()
driver.back()
driver.refresh()

driver.close()
