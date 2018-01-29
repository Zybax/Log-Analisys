# Log-Analisys
3rd Project of Fullstack Nanodegree 

## Prerequisites:
```
    Python2
    Vagrant
    VirtualBox
```
## Getting Started

Install Vagrant And VirtualBox

Clone this repository

Open a terminal and go to the project's folder

Launch  the vagrant machine by running ``` vagrant up ``` 
then log in by running ``` vagrant ssh```

Go to the vagrant machine folder by running ``` cd /vagrant```
then use the command ```psql -d news -f newsdata.sql ``` to load the data to postgres.

Now you can execute the program by running ```python news.py ```from the command line.

## database tables:
```
    Authors 
    Articles 
    Log 
```
