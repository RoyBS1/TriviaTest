import time
from telnetlib import EC
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Generating driver\browser and open the game
exe_path = ("D:\chromedriver.exe")
browser = webdriver.Chrome(exe_path)
browser.get('https://********.**.**/trivia')

#Setting the network connection to be slow so it would be possible to catch CSS changes for the correct answer
browser.set_network_conditions(
    offline=False,
    latency=5,  # additional latency (ms)
    download_throughput=200 * 1024,  # maximal throughput
    upload_throughput=200 * 1024)  # maximal throughput

#Initialize the data list and starting the game session
repository = {}
repository['repos1'] = []
#repos = set(repository)
for games in range (10):
    browser.find_element_by_id("play-button").click()
    time.sleep(2)

    for count in range (10):
        question = browser.find_element_by_class_name("trivia-question").text
        answer1 = browser.find_element_by_id("ans_1").text
        answer2 = browser.find_element_by_id("ans_2").text
        answer3 = browser.find_element_by_id("ans_3").text
        answer4 = browser.find_element_by_id("ans_4").text

        browser.find_element_by_id("ans_3").click()
        time.sleep(1)
        try:
            correctAnswer = browser.find_element_by_class_name("correct_answer").text
        except:
            selenium.common.exceptions.NoSuchElementException
        finally:
            time.sleep(1)

        #Check if value already exist
        if(question in repository.values()):
            print("Question already exists")
        else:
            #Pushing the value to the list
            repository['repos1'].append({
                'Question': question,
                'Answer1': answer1,
                'Answer2': answer2,
                'Answer3': answer3,
                'Answer1': answer4,
                'Correct answer': correctAnswer
            })
        time.sleep(4)

    #Finish game and start a new one
    print("Game finished successfully")
    browser.get('https://********.**.**/trivia')
    time.sleep(4)

#Writing to a json file and encode to HE
with open('data.json', 'w', encoding='utf8') as outfile:
    json.dump(repository, outfile, ensure_ascii=False)
