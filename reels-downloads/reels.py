#  Python Version 3.10.x
#  Selenium 4.22.0

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import subprocess, csv, os
from time import sleep

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe") 
options = webdriver.ChromeOptions()
# options.add_argument('--headless') # ซ่อนหน้าจอ chrome driver
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

# args = python reels.py chanel url || python reels.py "<chanel_name>" "<channel_reel_url>"
with open('page-reels.txt') as f:
    for line in f:
        line = line.rstrip()
        channel = line.split('=')[1]
        channel = channel.split('&')[0]
        url = line.split(' ')[0]
        with open('reels.txt', 'a') as reels:
            reels.write(channel+ ' downloads successful.' + '\n')
        
        sleep(3)
        driver.get(url)

        sleep(3)
        element = driver.find_element(By.XPATH, "//div[@aria-label='Close']")
        element.click()

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:

            # Scroll down to the bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for page to load
            sleep(6)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            
            last_height = new_height
            
        sleep(5)

        # Extract reel urls
        a_elements = driver.find_elements(By.TAG_NAME, 'a')

        directory_path = r'C:\Users\User\OneDrive\Documents\Work\script\reels-downloads\output\videos{}'.format(channel)
        os.makedirs(directory_path, exist_ok=True)

        with open(f"output/videos{channel}.csv", "w") as f:
            writer = csv.writer(f)
            for element in a_elements:
                href = element.get_attribute('href')
                if href and '/reel/' in href:
                    writer.writerow([href.split('/?s=')[0]])
                    
        f.close()
        driver.quit()

        # download reels with yt-dlp
        args = ["yt-dlp", "-f", "best", "-a", f"output/videos{channel}.csv", "--output", f"output/videos{channel}/%(id)s.%(ext)s"]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in iter(lambda: process.stdout.readline(), b''):
            print(line.decode("utf-8"))

        process.wait()
