import instaloader
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
import openpyxl
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl

options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
driver.maximize_window()


driver.get('https://www.instagram.com/')
def scrollComments():
    while True:
        try:

            # Get the height of the comment section
            height = driver.execute_script("return arguments[0].scrollHeight", comment_section)
            # Scroll to the bottom of the comment section
            #print(height)
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", comment_section)
            sleep(1) # Wait for the page to load
            wait = WebDriverWait(driver, 5)
            # load_more_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button"
            load_more_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[2]/div/div/ul/li/div/button"

            #/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/li/div/button
            load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, load_more_xpath)))
            load_more_button.click()
            
        except:
            driver.execute_script("arguments[0].scrollTo(0, 0)", comment_section)
            break



username_input = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password_input = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))

username_input.send_keys('shakirjani2024')
password_input.send_keys('hamid2')

login_button = driver.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()
try:
    Homebutton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div/a/div")))
    Homebutton.click()
except:
        print("\nLogin failed for this account. Maybe it is banned!\n")
sleep(2)
driver.get('https://www.instagram.com/p/CrUpD8TKirf/')

try:
    wait55 = WebDriverWait(driver, 10)
    comment_section = wait55.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[2]/div/div/ul')))
    scrollComments()
    comxpath = f"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[2]/div/div/ul/ul"

    comments = wait55.until(EC.presence_of_all_elements_located((By.XPATH, comxpath)))
except:
    cross=WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div")))
    cross.click()
    

wait = WebDriverWait(driver, 50)
i=0
for comment in comments:
    i+=1
    com= comment.find_element(By.TAG_NAME,"span").text
    username = comment.find_element(By.TAG_NAME,"h3").text
    print("#",i,"username: ",username," Comment: ",com)


#likes
# /html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[3]/section/div/div/span/a/span
# likesButton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[3]/section/div/div/span/a/span")))
# likesButton.click()
# countl=0
# print("Liker names: \n")
# for i in range(5000):
#     countl+=1
#     i+=1
#     liker = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[{}]/div/div/div/div[2]/div/div/span[1]/span/div/a/div/span/div".format(i))))
#     print("#",countl,": ",liker.text)

#/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[5]/div/div/div/div[2]/div/div/span[1]/span/div/a/div/span/div