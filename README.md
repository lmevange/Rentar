# Rentar

Rent Rater website
The idea of this project is to create a reliable source of information for renters to learn about the history of their prospective apartment and landlord. Landlords tend to have the upperhand so this is suppsoed to be a tool that renters can use to help even the playing field.

Look up history of apartments and Landords and how users of the site rate the apartments and landlords


To acsess our website go to http://www.rentarater.com/

The first step is to create a User and this can be done by clicking the Log in button on the right of our navigation bar.
After creating a user you can finally use all the features of Rentar. 

You can rate apartments by clicking the Add apartment button

![alt tag](https://github.com/lmevange/Rentar/blob/readmepics/assets/Images/Screen%20Shot%202016-12-08%20at%206.53.35%20PM.png)



After clicking that you will be brought to a page and will click on the Adress info button

![alt tag](https://github.com/lmevange/Rentar/blob/readmepics/assets/Images/Screen%20Shot%202016-12-08%20at%207.12.46%20PM.png)

Upon clicking a popup will apear and you can fillout the information for the aparemnt you wish to rate

You can contact us at the About Us button


![alt tag](https://github.com/lmevange/Rentar/blob/readmepics/assets/Images/Screen%20Shot%202016-12-10%20at%202.18.11%20PM.png)







###### Deploying Rentar: 
======

  _for deployment on a linux server_ 

  * We first create a droplet at digital ocean to get an IP and server. Log in and change root

    password. Make user. Add user to sudo group. Log in as new user. Make home directory rwx.

  * On that droplet update and upgrade, make sure python3 and git is installed with apt-get python3 and apt-get pip.

  * Do all install commands with sudo.

  * Install pip3 with package ‘apt-get python3-pip3’ update pip3 with ‘pip3 install –upgrade pip’

  * Install Django and crispy forms packages ‘pip3 install django’ ‘pip3 install django-crispy- forms’

    ‘pip3 install Django-mathfilters’

  * Clone repository ‘git clone https://github.com/lmevange/Rentar’

  * Inside Rentar/server run ‘python3 manage.py runserver’ to run local. ‘python3 manage.py

    runserver 0.0.0.0:8000’ to run on remote IP.

  * Add ip address and or hostname of server in server/settings.py under allowed_hosts[]
