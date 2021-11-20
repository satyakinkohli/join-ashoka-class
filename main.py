from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import config


def chunks(arr, n):
    lst = []
    for k in range(0, len(arr), n):
        lst.append(arr[k: k + n])
    return lst


def execute():
    login()
    classes = extracting_timetable()
    returnDict = selecting_correct_class_time(classes)
    if not returnDict['classExist']:
        return
    opening_class_link(classes, returnDict['timeRow'], returnDict['dayRow'])


def login():
    # URL of college website
    URL = 'https://ams.ashoka.edu.in/Contents/StudentDashboard.aspx'
    driver.get(URL)

    # username and password
    username = config.username
    password = config.password

    # entering google username
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    # entering google password
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()


def extracting_timetable():
    # opening timetable page
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="divMainTilesList"]/div[1]/a[2]')))
    timetableURL = 'https://ams.ashoka.edu.in/Contents/TimeTable/TimeTableView_Student.aspx'
    driver.get(timetableURL)

    # extracting html table including header and grid of what classes at what time
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="divData"]/table/tbody')))
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")

    timetableHead = soup.find_all("thead")
    tdHead = timetableHead[0].find_all("td")
    headings = [tr.text for tr in tdHead]
    headings = [(heading[:heading.find('y') + 1] + " " + heading[heading.find('y') + 1:]).lstrip() for heading in
                headings]  # this adds a space between the day and date as the scraping doesn't do that automatically

    timetable = soup.find_all("tbody")
    td = timetable[0].find_all("td")
    classes = [tr.text.rstrip() for tr in td]
    classes[0:0] = headings
    classes = chunks(classes, 8)

    return classes


def selecting_correct_class_time(classes):
    # finding nearest possible class match according to the current time

    # # automatic -------------------
    # now = datetime.now()
    # # automatic -------------------
    # # manual -------------------
    now1 = datetime.strptime('17-Nov-2021', '%d-%b-%Y')
    now = now1.replace(hour=16, minute=28)
    # # manual -------------------

    # # automatic -------------------
    # day = now.strftime("%A %d-%b-%Y")
    # dayRow = 8 if (day.split())[0] == "Sunday" else int(now.strftime("%w")) + 1
    # # automatic -------------------
    # # manual -------------------
    dayRow = 4
    # # manual -------------------

    time = now.strftime("%I:%M %p")

    timeDifference_arr = [None]
    for element in range(1, len(classes)):
        start, end = classes[element][0].split("-")
        timeDifference = datetime.strptime(time, "%I:%M %p") - datetime.strptime(start.rstrip(), "%I:%M %p")
        if timeDifference.days == -1:
            timeDifference_arr.append(86400 - timeDifference.seconds)
        else:
            timeDifference_arr.append(-1)
    try:
        timeRow = timeDifference_arr.index(min(x for x in timeDifference_arr if x is not None if x > 0))
    except ValueError:
        timeRow = 0

    if timeRow == 0 or timeDifference_arr[timeRow] > 300:
        print("Sorry!\nThere is no upcoming class for today, or your next class doesn't begin in the next 5 minutes.")
        return {'classExist': False}
    return {'classExist': True, 'timeRow': timeRow, 'dayRow': dayRow}


def opening_class_link(classes, timeRow, dayRow):
    if classes[timeRow][dayRow - 1] == "":
        return

    # # automatic -------------------
    # driver.find_element(By.XPATH, f'//*[@id="divData"]/table/tbody/tr[{timeRow}]/td[{dayRow}]/div/p[4]/a').click()
    # window_after = driver.window_handles[1]
    # driver.switch_to.window(window_after)
    # # automatic -------------------
    # # manual -------------------
    URL1 = 'https://meet.google.com/afd-vkqo-sqf'
    driver.get(URL1)
    # # manual -------------------

    if driver.current_url[0:4] == "zoom" or driver.current_url[8:12] == "zoom":
        zoom()
    elif driver.current_url[8:12] == "meet":
        meet()
    else:
        print("Error\nNo clue what happened though!")


def meet():
    # mute yourself
    driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    # close your camera
    driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    # join the meeting
    driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()

    return


def zoom():
    return


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.headless = False
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--incognito")
    # the add_experimental_option does not work, that is why the below method to allow camera and mic access has
    # been used
    chrome_options.add_argument("use-fake-ui-for-media-stream")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    execute()
