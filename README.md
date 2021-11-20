<h1> Join-Ashoka-Class </h1>

Have a class at the devilish time of 8:30 AM? Perhaps a late lunch means your class at 2:50 PM is a bit of a pain-in-the-ass? Or, simply, going to online classes is just not your thing? There is something that could help.

The CRON + python scripts allow you to join your class at Ashoka University (duh, you got to be enrolled at the Univeristy!) automatically.
The CRON script does the following job:
1. run the python script every Monday to Friday at 8:26 AM, 10:06 AM, 11:46 AM, 2:46 PM, 4:26 PM, 6:06 PM (i.e. 4 minutes before each class @ AU starts)
The python script executes the following functions:
2. logs in to AMS (http://ams.ashoka.edu.in/Contents/StudentDashboard.aspx) through your Google account
3. opens the timetable and selects the class which begins in the next 5 minutes that day of the week
4. alerts the user if no class is scheduled and exits the program, or, opens the gmeet or zoom link of the upcoming class
5. closes the camera and mic (you don't wanna not do this :p) and joins the meeting
