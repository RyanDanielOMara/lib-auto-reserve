from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import datetime
import time

reserve_date = (datetime.date.today() + datetime.timedelta(days=3))
reserve_day  = int(reserve_date.strftime('%d'))
room_number  = "14"
people = [
	["10:00am", "11:00am", "12:00pm", "Ali",      "Ahmed",     "atahmed@buffalo.edu"],
	["12:00pm", "1:00pm",  "2:00pm",  "Barry",    "Lee",       "bclee@buffalo.edu"],
	["2:00pm",  "3:00pm",  "4:00pm",  "Brian",    "De Guzman", "bsdeguzm@buffalo.edu"],
	["4:00pm",  "5:00pm",  "6:00pm",  "Joseph",   "Lebold",    "jlebold@buffalo.edu"],
	["6:00pm",  "7:00pm",  "8:00pm",  "Ryan",     "O'Mara",    "rdomara@buffalo.edu"],
	["8:00pm",  "9:00pm",  "10:00pm", "Tyler",    "Lynch",     "tjlynch@buffalo.edu"],
	["10:00pm", "11:00pm", "11:59pm", "Valencia", "Kaplinsky", "vakaplin@buffalo.edu"],
]

# PEOPLE FOR DEMO
people = [
	["12:00am", "1:00am",  "2:00am",  "Barry",    "Lee",       "bclee@buffalo.edu"],
	["2:00am",  "3:00am",  "4:00am",  "Brian",    "De Guzman", "bsdeguzm@buffalo.edu"],
	["4:00am",  "5:00am",  "6:00am",  "Joseph",   "Lebold",    "jlebold@buffalo.edu"],
	["6:00am",  "7:00am",  "8:00am",  "Ryan",     "O'Mara",    "rdomara@buffalo.edu"],
	["8:00am",  "9:00am",  "10:00am", "Tyler",    "Lynch",     "tjlynch@buffalo.edu"],
	["10:00am", "11:00am", "12:00pm", "Valencia", "Kaplinsky", "vakaplin@buffalo.edu"],
]


def main():
	print(reserve_date.strftime('Making reservations for %m/%d/%y...'))

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	driver = webdriver.Chrome(chrome_options=options)
	driver.get('http://booking.lib.buffalo.edu/booking/silverman')


	print("Loading library website...")

	for person in people:
		driver.refresh();
		time.sleep(0.5)

		selectDay(driver)
		time.sleep(2.5)
		
		reserveRoom(driver, person)
		time.sleep(1.5)

def selectDay(driver):
	if 1 <= reserve_day <= 3:
		selectNextMonth(driver)

	xpath_to_date = "//table[@class='ui-datepicker-calendar']//tbody//tr//td//a[text()='" + str(reserve_day) + "']"
	elem = driver.find_element_by_xpath(xpath_to_date)
	elem.click()

def selectNextMonth(driver):
	next_path = "//a[contains(@class, 'ui-datepicker-next')]"
	next_month_button = driver.find_element_by_xpath(next_path)
	next_month_button.click()

def reserveRoom(driver, person):
	(time1_start, time2_start, time2_end, first_name, last_name, email) = person

	print("Reserving room " + room_number + " from " + time1_start + " to " + time2_end + " for " + first_name + " " + last_name + "...")

	xpath_to_reserve_table = "//*[contains(@title, 'Room " + room_number + ", " + time2_start + " to " + time2_end + "')]"
	reservation_table = driver.find_element_by_xpath(xpath_to_reserve_table)
	reservation_table.click()

	xpath_to_reserve_table = "//*[contains(@title, 'Room " + room_number + ", " + time1_start + " to " + time2_start + "')]"
	reservation_table = driver.find_element_by_xpath(xpath_to_reserve_table)
	reservation_table.click()

	time.sleep(0.2)

	confirm_button = driver.find_element_by_id('rm_tc_cont')
	confirm_button.click()

	active_elem = driver.switch_to.active_element
	active_elem.send_keys(first_name)
	active_elem.send_keys(Keys.TAB)

	active_elem = driver.switch_to.active_element
	active_elem.send_keys(last_name)
	active_elem.send_keys(Keys.TAB)

	active_elem = driver.switch_to.active_element
	active_elem.send_keys(email)
	active_elem.send_keys(Keys.TAB)

	active_elem = driver.switch_to.active_element
	active_elem.click()

if __name__ == "__main__":
    main()
    print("Finished reservations.")
    time.sleep(3)