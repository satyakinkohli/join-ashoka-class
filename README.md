# Join-Ashoka-Class

Have a class at the devilish time of 8:30 AM? Perhaps a late lunch means your class at 2:50 PM is a bit of a pain-in-the-ass? Or, simply, is going to online classes just not your thing? There is something that could help.

## Working Explained

A ***<ins>combination of CRONTAB and python scripts</ins>*** allow you to automatically join your class at Ashoka University (duh, you got to be enrolled at the Univeristy!).
- The *CRONTAB script* executes the following function:
  1. run the python script every Monday to Friday at 8:26 AM, 10:06 AM, 11:46 AM, 2:46 PM, 4:26 PM any 6:06 PM (i.e. 4 minutes before any class starts).

- The *python script* executes the following functions:
  1. log in to [AMS](http://ams.ashoka.edu.in/Contents/StudentDashboard.aspx) through your Google account
  2. open the timetable and select the class which begins in the next 5 minutes that day of the week
  3. alert the user if no class is scheduled and exits the program, or, open the gmeet or zoom link of the upcoming class
  4. close the camera and mic (you don't wanna not do this :p) and join the meeting

## Setup

1. Make a file named `config.py` in the same directory as `main.py`. This file would only contain your Google account's credentials in the following format:
```
username = '<ashoka-email-id>'
password = '<password>'
```
2. Make a [CRONTAB file](https://www.jcchouinard.com/python-automation-with-cron-on-mac/) which contains the following text:
```
Eventually
```
