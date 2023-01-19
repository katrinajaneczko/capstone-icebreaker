# ICS File Generator
## Mary, Katrina, Nathaniel, Christine, Harrison

This project allows a user to keep track of deadlines for a specific class. By accessing the web application, the user can select a course and see future and past events with the date and a description of the event. They can also download a .ics file (iCalendar) to import all important events into their Google or Outlook calendar.

**Instructions For Use**

One must first have the following libraries installed on their machine:
- ics
- api
- flask

To install, use the following terminal command:

pip3 install [name]

Clone the repository and first run api.py. Then run web.py, and access http://127.0.0.1:5000 on your web browser. You now have access to the Syllabus Explorer.

From the homepage, you can select the course for which you want to see due dates. Once you've selected the course, you'll see a page with the current date and time, as well as past and future events in the course. Scrolling through the tables will allow you to see all events in the semester.

At the top of the course page, you'll see three links.

1. Download ICS
   
   By clicking this link, a .ics will be downloaded to your machine. This file is compatible with both Google and Outlook calendar apps.
2. Google Calendar
   
   By clicking this link, you will be redirected to Google Calendar, where you can import the .ics file to automatically be added to your calendar.
3. Outlook Calendar
   
   By clicking this link, you will be redirected to Microsoft Calendar, where you can import the .ics file to automatically be added to your calendar.
   
**Adding ics file to Google Calendar**
1. To add the ics file to your Google Calendar, after clicking the link, select the plus sign next to "Other Calendars" on the lower left side of the page.

![image](https://user-images.githubusercontent.com/65423598/213352264-2f0c2af9-aef2-42ef-9e18-80ab0294984c.png)

2. Next, select the "import" option from the dropdown menu.
 
 ![image](https://user-images.githubusercontent.com/65423598/213352399-ec2ee19d-cbba-4701-9694-f3d95c833d3a.png)
 
3. Select the .ics file from the appropriate location on your computer, and select import. Your calendar should now populate with the events from the file!


**Adding ics file to Outlook Calendar**
1. To add the ics file to your Outlook Calendar, after clicking the link, select the "Add Calendar" button on the lower left side of the page.

![image](https://user-images.githubusercontent.com/65423598/213353236-dc7a438b-4a29-4516-9426-051f5209bb4c.png)

2. Next, select the "Upload from file" option in the pop up window.

![image](https://user-images.githubusercontent.com/65423598/213353362-edce9a75-2c06-4f15-9dcc-61866458c28e.png)

3. Select browse, and choose the .ics file from the appropriate location on your computer. Select import, and your calendar will now be populated with the events from the file.
