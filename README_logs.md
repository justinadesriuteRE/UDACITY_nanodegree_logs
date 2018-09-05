## About

A large database with over a million rows is explored by writing  SQL queries to draw conclusions about the data. The project imitates building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

## To Run

### Requirements

- Python3
- Vagrant
- VirtualBox

### Setup
1. Install Vagrant And VirtualBox
2. Clone this repository

### To Run

Launch Vagrant VM by running `vagrant up` in the project's directory and log in with `vagrant ssh` command.

To access shared files in the directory run `cd /vagrant`.

To load the data, use the command `psql -d news -f newsdata.sql`.  Command connects you to a database and runs the SQL statements.

To execute the main program, run `python3 newsdata.py` from the command line.

Program's goal is to give answers to 3 questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
