<h1> Join-Ashoka-Class </h1>

Have a class at the devilish time of 8:30 AM? Perhaps a late lunch means your class at 2:50 PM is a bit of a pain-in-the-ass? Or, simply, going to online classes is just not your thing? There is something that could help.

A  ***<ins>combination of CRON and python scripts</ins>*** allow you to automatically join your class at Ashoka University (duh, you got to be enrolled at the Univeristy!).
- The *CRON script* does the following function:
  1. run the python script every Monday to Friday at 8:26 AM, 10:06 AM, 11:46 AM, 2:46 PM, 4:26 PM any 6:06 PM (i.e. 4 minutes before any class starts).

- The *python script* executes the following functions:
  1. log in to AMS (http://ams.ashoka.edu.in/Contents/StudentDashboard.aspx) through your Google account
  2. open the timetable and select the class which begins in the next 5 minutes that day of the week
  3. alert the user if no class is scheduled and exits the program, or, open the gmeet or zoom link of the upcoming class
  4. close the camera and mic (you don't wanna not do this :p) and join the meeting
