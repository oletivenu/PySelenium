from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("venu.babu80@gmail.com")

password_box = browser.find_element_by_id("password")
password_box.send_keys("Venubabu%12345")

password_box.submit()

assert "oletivenu" in browser.page_source

signout_link = browser.find_element_by_class_name("dropdown-signout")

signout_link.submit()

browser.quit()
