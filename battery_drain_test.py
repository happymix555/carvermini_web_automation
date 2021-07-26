import selenium
from selenium import webdriver
import os
import time
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
from lxml import etree
import requests
import csv
from datetime import datetime
from csv import writer

def find_button(path):
    global driver
    while True:
        try:
            return driver.find_element_by_xpath(path)
        except:
            pass

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', False)

driver = webdriver.Chrome('/home/happymix/hac/web_automation/carvermini_web_automation/chromedriver', options=options)

driver.get('https://mini.carver-amr.com/login/')

id_box = driver.find_element_by_id('input-18')
pwd_box = driver.find_element_by_id('input-22')
# login_button = driver.find_element_by_class_name('v-btn__content')
login_button = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div/div/form/div[2]/div[2]/div/div/button')
id_box.send_keys('carvermini3')
pwd_box.send_keys('iamcarver')
login_button.click()



# three_bars_menu = driver.find_element_by_xpath('//*[@id="inspire"]/div/header/div/div/button[1]/span/i')
three_bars_menu = find_button('//*[@id="inspire"]/div/header/div/div/button[1]/span/i')
time.sleep(1)
three_bars_menu.click()
# loaded_then_click(three_bars_menu)
# time.sleep(1)

manual_control_button = find_button('/html/body/div/div/div/div[2]/nav/div[1]/div/a/div[2]')
time.sleep(1)
manual_control_button.click()
time.sleep(1)

wait_for_change_speed = input('chage speed then enter something to terminal')

# joy_zone = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[2]/div/div[2]/div')
joy_zone = find_button('//*[@id="zone_joystick"]')
time.sleep(2)
joy_zone.click()
time.sleep(2)

joy_nipple = ActionChains(driver)
# joy_nipple.click_and_hold(driver.find_element_by_xpath('//*[@id="nipple_0_0"]/div[2]'))
# joy_nipple.move_by_offset(-99, 0)
# joy_nipple.perform()
# time.sleep(2)
# joy_nipple.release()
# joy_nipple.reset_actions()

# joy_nipple.click_and_hold(driver.find_element_by_xpath('//*[@id="nipple_0_0"]/div[2]'))
# joy_nipple.move_by_offset(0, 99)
# joy_nipple.perform()
# time.sleep(2)
# joy_nipple.release()
# joy_nipple.reset_actions()

# joy_nipple.click_and_hold(driver.find_element_by_xpath('//*[@id="nipple_0_0"]/div[2]'))
# joy_nipple.move_by_offset(99, 99)
# joy_nipple.perform()
# time.sleep(2)
# joy_nipple.release()
# joy_nipple.reset_actions()

wait_for_change_speed = input('chage speed then enter something to terminal')

page_source = driver.page_source
soup = bs(page_source, "html.parser")
dom = etree.HTML(str(soup))
print(dom.xpath('//*[@id="inspire"]/div/header/div/div/div[4]/div/span[5]/span')[0].text)

state = 1

state1_time_count = 2
state2_time_count = 10
state3_time_count = 2
state4_time_count = 50
print_state_time_count = 5

state1_time_update_flag = 0
state2_time_update_flag = 0
state3_time_update_flag = 0
state4_time_update_flag = 0
print_state_time_flag = 0

fifteen_min = 60 * 1
fifteen_flag = 0

csv_location = '/home/happymix/hac/web_automation/battery_record.csv'

page_source = driver.page_source
soup = bs(page_source, "html.parser")
dom = etree.HTML(str(soup))
battery_percent = dom.xpath('//*[@id="inspire"]/div[1]/header/div/div/div[4]/div/span[5]/span')[0].text
current_time = datetime.now().strftime("%H:%M:%S")
# print(battery_percent)
list = []
list.append(current_time)
list.append(battery_percent)
# open the file in the write mode
# f = open('/home/happymix/hac_for_upload/web_automation/battery_record.csv', 'w', newline='')
print(list)
with open(csv_location, 'a+', newline='') as write_obj:
    # Create a writer object from csv module
    csv_writer = writer(write_obj)
    # Add contents of list as last row in the csv file
    csv_writer.writerow(list)

while True:
    if fifteen_flag == 0:
        fifteen_time = time.time()
        fifteen_flag = 1
    if state == 1:
        if state1_time_update_flag == 0:
            in_state_time = time.time()
            state1_time_update_flag = 1
        joy_nipple.click_and_hold(driver.find_element_by_xpath('//*[@id="nipple_0_0"]/div[2]'))
        joy_nipple.move_by_offset(0, -99)
        joy_nipple.perform()
        if time.time() - in_state_time >= state1_time_count:
            joy_nipple.release()
            # joy_nipple.reset_actions()
            joy_nipple.perform()
            joy_nipple.reset_actions()
            joy_nipple.perform()
            state1_time_update_flag = 0
            time.sleep(3)
            state = 2
    if state == 2:
        if state2_time_update_flag == 0:
            in_state_time = time.time()
            state2_time_update_flag = 1
        joy_nipple.click_and_hold(driver.find_element_by_xpath('//*[@id="nipple_0_0"]/div[2]'))
        joy_nipple.move_by_offset(99, 0)
        joy_nipple.perform()
        if time.time() - in_state_time >= state2_time_count:
            joy_nipple.release()
            # joy_nipple.reset_actions()
            joy_nipple.perform()
            joy_nipple.reset_actions()
            joy_nipple.perform()
            state2_time_update_flag = 0
            time.sleep(3)
            state = 4
    if state == 30:
        if state3_time_update_flag == 0:
            in_state_time = time.time()
            state3_time_update_flag = 1
        joy_nipple.click_and_hold(driver.find_element_by_xpath('//*[@id="nipple_0_0"]/div[2]'))
        joy_nipple.move_by_offset(0, -79)
        joy_nipple.perform()
        if time.time() - in_state_time >= state3_time_count:
            joy_nipple.release()
            # joy_nipple.reset_actions()
            joy_nipple.perform()
            joy_nipple.reset_actions()
            joy_nipple.perform()
            state3_time_update_flag = 0
            time.sleep(3)
            state = 1
    if state == 4:
        if time.time() - fifteen_time >= fifteen_min:
            if state4_time_update_flag == 0:
                in_state_time = time.time()
                state4_time_update_flag = 1
                print("Performing battery recovery")
            if time.time() - in_state_time >= state4_time_count:
                state4_time_update_flag = 0
                page_source = driver.page_source
                soup = bs(page_source, "html.parser")
                dom = etree.HTML(str(soup))
                battery_percent = dom.xpath('//*[@id="inspire"]/div[1]/header/div/div/div[4]/div/span[5]/span')[0].text
                current_time = datetime.now().strftime("%H:%M:%S")
                # print(battery_percent)
                list = []
                list.append(current_time)
                list.append(battery_percent)
                # open the file in the write mode
                # f = open('/home/happymix/hac_for_upload/web_automation/battery_record.csv', 'w', newline='')
                print(list)
                with open(csv_location, 'a+', newline='') as write_obj:
                    # Create a writer object from csv module
                    csv_writer = writer(write_obj)
                    # Add contents of list as last row in the csv file
                    csv_writer.writerow(list)
                # writer = csv.writer(f)
                # write a row to the csv file
                
                # writer.writerow(list)
                
                # close the file
                # f.close()
                fifteen_flag = 0
                state = 1
                print("Battery recovery done")
        else:
            state = 1
    if state == 5:
        break
    if print_state_time_flag == 0:
        print_state_time = time.time()
        print_state_time_flag = 1
    if time.time() - print_state_time >= print_state_time_count and state4_time_update_flag == 0:
        print_state_time_flag = 0
        print("perform battery rocovery in : " + str(int(fifteen_min - (time.time() - fifteen_time))) + " s")



# # # driver = webdriver.Chrome('/home/happymix/hac/carver_mini/code/web_automation/chromedriver', options=options)
# joy_stick = TouchActions(driver)
# # # joy_stick.move(50, 50)
# # joy_stick.perform()
# # time.sleep(2)
# # joy_stick = TouchActions(driver)
# joy_stick.long_press(driver.find_element_by_xpath('//*[@id="nipple_0_0"]/div[2]'))
# # joy_stick.move(50, 50)
# joy_stick.perform()
# # time.sleep(3)

print('DONE')