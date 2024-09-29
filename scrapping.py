from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"profile.managed_default_content_settings.stylesheets": 2,
        "profile.default_content_setting_values.notifications": 2,
        "profile.managed_default_content_settings.javascript": 1,
        }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--deny-permission-prompts")
    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = init_driver()

driver.get("https://www.ntu.edu.pk/index.php")

element = driver.find_element(By.XPATH, '//a[contains(text(), "ADMISSIONS")]')

action = ActionChains(driver)
action.move_to_element(element).perform()

tabs = driver.find_elements(By.XPATH, '//li/a[@href and @class="nav-link__list px-0" and not (contains(text(), "Download"))]')

tabs_urls = [x.get_attribute("href") for x in tabs]

i = 1

text_str = ""

for tab_url in tabs_urls:
    time.sleep(0.5)
    print("Total: ", i)
    i += 1
    driver.get(tab_url)

    sub_tabs = driver.find_elements(By.XPATH, '//li[@class="nav-item"]/a[not (contains(text(), "CONTACT"))]')
    # print(len(sub_tabs))
    # sub_tabs_urls = [x.get_attribute("href") for x in sub_tabs]
    j = 1
    # for sub_tab_url in sub_tabs_urls:
    #     driver.get(sub_tab_url)
    for sub_tab in sub_tabs:
        sub_tab.click()
        time.sleep(0.5)
        # print(j)
        j += 1
        if j == 2:
            try:
                element_case_0 = driver.find_element(By.XPATH, '//h2/span')
                text_element_case_0 = element_case_0.text
                print(text_element_case_0)
                text_str += text_element_case_0 + '\n'
            except:
                pass

        try:
            element_case_1 = driver.find_elements(By.XPATH, '//div[@class="tab-content"]/div/ul/li')
            text_element_case_1 = [x.text for x in element_case_1 if x.text != ""]
            text_element_case_1 = "\n".join(text_element_case_1)
            print(text_element_case_1)
            text_str += text_element_case_1 + '\n'
        except:
            print("Case 1 failed")
        try:
            element_case_2 = driver.find_elements(By.XPATH, '//div[@class="tab-content"]/div/ol/li')
            text_element_case_2 = [x.text for x in element_case_2 if x.text != ""]
            text_element_case_2 = "\n".join(text_element_case_2)
            print(text_element_case_2)
            text_str += text_element_case_2 + '\n'
        except:
            print("Case 2 failed")

        try:
            element_case_3 = driver.find_elements(By.XPATH, '//div[@class="tab-content"]/div/p')
            text_element_case_3 = [x.text for x in element_case_3 if x.text != ""]
            text_element_case_3 = "\n".join(text_element_case_3)
            print(text_element_case_3)
            text_str += text_element_case_3 + '\n'
        except:
            print("Case 3 failed")

        try:
            element_case_4 = driver.find_elements(By.XPATH, '//div[@class="tab-content"]/div/table/tbody/tr/td')
            text_element_case_4 = [x.text for x in element_case_4 if x.text != ""]
            text_element_case_4 = "\n".join(text_element_case_4)
            print(text_element_case_4)
            text_str += text_element_case_4 + '\n'
        except:
            print("Case 4 failed")

        try:
            element_case_5 = driver.find_elements(By.XPATH, '//div[@class="tab-content"]/div/table/tbody/tr/td/p')
            text_element_case_5 = [x.text for x in element_case_5 if x.text != ""]
            text_element_case_5 = "\n".join(text_element_case_5)
            print(text_element_case_5)
            text_str += text_element_case_5 + '\n'
        except:
            print("Case 5 failed")

        try:
            element_case_6 = driver.find_elements(By.XPATH, '//div[@class="tab-content"]/div/div/div/p')
            text_element_case_6 = [x.text for x in element_case_6 if x.text != ""]
            text_element_case_6 = "\n".join(text_element_case_6)
            print(text_element_case_6)
            text_str += text_element_case_6 + '\n'
        except:
            print("Case 6 failed")

        try:
            element_case_7 = driver.find_elements(By.XPATH, '//div[@id="intro"]/div')
            text_element_case_7 = [x.text for x in element_case_7 if x.text != ""]
            text_element_case_7 = "\n".join(text_element_case_7)
            print(text_element_case_7)
            text_str += text_element_case_7 + '\n'
        except:
            print("Case 7 failed")

text_str = text_str.replace('travesti marjinaltrv travestiler izmit ve kocaeli travesti escortlar marjinal travest', '')
text_str = text_str.replace('Click Here to Apply', '')
with open('output.txt', 'w') as file:
    file.write(text_str)

print("Successful!")

driver.quit()