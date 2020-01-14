from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_elements_by_id("login_field")
username_box[0].send_keys("venu.babu80@gmail.com")

password_box = browser.find_elements_by_id("password")
password_box[0].send_keys("Venubabu%12345")

password_box[0].submit()

assert "oletivenu" in browser.page_source

signout_link = browser.find_elements_by_class_name("dropdown-signout")

signout_link[0].submit()

browser.quit()
