Contributors:

Harshit Srivastava                                                   
Aayush Sanjay Agarwal                           
Akhil Chandra Panchumarthi                      
                               
Salient Features:

1. Login and SignUp page for login and registration respectively. The login uses Google API for Captcha verification. SignUp has Password strength feature.

2. Page for the list of Professors. This also has a search bar using Javascript, to filter the list.

3. Has a dashboard for the professor to login and update his details.On the first login, it directly takes the user to the page to enter the personal information. One can also upload one’s profile picture.

4. There is also an option to take data from the previous website which was made using Beautiful Soup library of Python (using the format of Deka Sir’s website only). It will ask for the page link on the personal information form, and the link button on the homepage, adds the information.  Linking this way using web scraping to collect details from the given url.

5. The dashboard has a homepage that has a notification panel that gets updated everytime user logs in. Once the user confirms the notification it automatically gets updated in the database as well as the professor’s page and is removed from the notification panel. The user can also post about the updates on facebook and linkedin.

6. The homepage also has a panel for displaying the personal information, with number of publications, number of courses etc.

7. There is an about me dropdown where he can change his personal information, his education details and work experience etc.

8. There are seperate forms for the publications, students, projects, teachings, recognitions etc. where the user can add new information, edit existing information or delete them.

9. The is a view page tab on the dashboard panel that takes user to the dynamic page generated for everyone to see.

10. The page generated has multiple segments, each for the different parts, like personal information, teachings, publications, students, recognitions etc.

11. For web scraping, we are using a python script to extract information from text file which will serve as mail (for simplicity, the text files are already present in the project).


S/W Tools :

1. HTML
2. CSS
3. Javascript
4. Python
5. Django Web Framework
6. Beautiful Soup for web scraping
7. Google Api




