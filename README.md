# Join-Ashoka-Class

Have a class at the devilish time of 8:30 AM? Perhaps a late lunch means your class at 2:50 PM is a bit of a pain-in-the-ass? Or, simply, is going to online classes just not your thing? There is something that could help.

<a href="https://youtu.be/0baaP0oFj84" rel="noreferrer noopener" target="_blank"><img src="https://github.com/satyakinkohli/join-ashoka-class/blob/main/JAC-play-button.png" alt="Youtube link for project video" width="100%" height="100%" border="10" /></a>

## Working Explained

A ***<ins>combination of CRONTAB and python scripts</ins>*** allows you to automatically join your class at Ashoka University (duh, you got to be enrolled at the Univeristy!).
- The *CRONTAB script* executes the following function:
  1. run the python script every day-of-week from Monday through Friday at 8:26 AM, 10:06 AM, 11:46 AM, 2:46 PM, 4:26 PM and 6:06 PM (i.e. 4 minutes before every class slot).

- The *python script* executes the following functions:
  1. log in to [AMS](http://ams.ashoka.edu.in/Contents/StudentDashboard.aspx) through your Google account
  2. open the timetable and select the class slot which begins in the next 5 minutes that day of the week
  3. alert the user if no class is scheduled and exits the program, or, open the gmeet or zoom link of the upcoming class
  4. close the camera and mic (you don't wanna not do this :p) and join the meeting

## Setup

1. In `main.py`, change the location of the chromedriver as per your requirements:
```
driver = webdriver.Chrome(service=Service("<location-of-chromedriver>"), options=chrome_options)
```
2. Make a file named `config.py` in the same directory as `main.py`. This file would contain your Google account's credentials, in the following format:
```
username = '<ashoka-email-id>'
password = '<ashoka-email-password>'
```
3. Configure Zoom settings (required specifically for Zoom classes)
  - Go to Options and enable 'Open at Login'
  - In the Zoom app, go to Settings > Video and check ( &#x2611; &nbsp;) `Stop my video when joining a meeting`
  - In the Zoom app, go to Settings > Audio and check ( &#x2611; &nbsp;) `Automatically join computer audio when joinnig a meeting`
  - In the Zoom app, go to Settings > Audio and check ( &#x2611; &nbsp;) `Mute my mic when joining meeting`
4. Schedule your computer to wake up automatically atleast 12-15 minutes before the beginning of every class slot. Instructions for this can be found here: [MAC](https://support.apple.com/guide/mac-help/schedule-mac-desktop-computer-turn-mchlp2266/mac#:~:text=On%20your%20Mac%2C%20choose%20Apple,Energy%20Saver%20%2C%20then%20click%20Schedule.&text=Select%20the%20options%20you%20want,a%20time%2C%20then%20click%20Apply.) and [WINDOWS](https://www.howtogeek.com/119028/how-to-make-your-pc-wake-from-sleep-automatically/#:~:text=To%20do%20so%2C%20head%20to,it's%20set%20to%20%E2%80%9CEnable.%E2%80%9D)
5. Make a [Crontab file](https://www.jcchouinard.com/python-automation-with-cron-on-mac/) (for MAC) which contains the following text:
```
PYTHONPATH=<location-of-modules-imported-in-main.py>
26 8,16 * * 1-5 <location-of-python3> <location-of-main.py> > <location-of-log-file-1-which-will-be-created> 2>&1
6 10,18 * * 1-5 <location-of-python3> <location-of-main.py> > <location-of-log-file-2-which-will-be-created> 2>&1
46 11,14 * * 1-5 <location-of-python3> <location-of-main.py> > <location-of-log-file-3-which-will-be-created> 2>&1
```
This is what this looked like for me:
```
PYTHONPATH=/Users/satyakinkohli/PycharmProjects/Join-AshokaClass/venv/lib/python3.9/site-packages
26 8,16 * * 1-5 /usr/bin/python3 /Users/satyakinkohli/PycharmProjects/Join-AshokaClass/main.py > /Users/satyakinkohli/PycharmProjects/Join-AshokaClass/log1.txt 2>&1
6 10,18 * * 1-5 /usr/bin/python3 /Users/satyakinkohli/PycharmProjects/Join-AshokaClass/main.py > /Users/satyakinkohli/PycharmProjects/Join-AshokaClass/log2.txt 2>&1
46 11,14 * * 1-5 /usr/bin/python3 /Users/satyakinkohli/PycharmProjects/Join-AshokaClass/main.py > /Users/satyakinkohli/PycharmProjects/Join-AshokaClass/log3.txt 2>&1
```
More details on how to write Cron schedule expressions can be found [here](https://crontab.guru).
