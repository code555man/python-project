from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


def youtube_sub(mail_user,mail_passwd):

    # url = "https://accounts.google.com/v3/signin/identifier?dsh=S-503225026%3A1688735671324018&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AeDOFXg0TS5gnAu96r_eDKsUF1XbMhDTwNN3YKww6S-2eFBmBq4yI3VM6lpb2uPjNQeafL3QzGdjtw&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    url = "http://mail.google.com/"

    service = Service(executable_path="chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(service=service, options=options)

    browser.get(url)

    browser.find_element(By.ID, "identifierId").send_keys(mail_user)
    # email.clear()
    sleep(1)

    browser.find_element(By.ID, "identifierNext").click()
    sleep(1)

    browser.find_element(By.NAME, "Passwd").send_keys(mail_passwd)
    # passwd.clear()
    sleep(1)

    browser.find_element(By.ID, "passwordNext").click()
    sleep(3)


    browser.get('') # youtube channel         
    browser.find_element(By.CLASS_NAME,"style-scope ytd-subscribe-button-renderer").click()
    print("success")
    sleep(2)

    # browser.quit()



if __name__ == "__main__":

    with open("mail.txt","r") as f:

        for x in range(15):
            row = f.readline()
            cut_str = row.split(":")
            std = [line.rstrip('\n') for line in cut_str]

            youtube_sub(std[0],std[1])
            print(std[0],std[1])
            sleep(8)
