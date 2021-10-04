1)install mysql in a container 
$docker run --name=test-mysql  --env="MYSQL_ROOT_PASSWORD=mypassword" mysql:5.7

2)$docker inspect test-mysql
/*get the ip address*/
172.17.0.2

->OPEN A NEW TERMINAL AND EXECUTE THE FOLLOWING COMMANDS IN THAT..
3)
download mysql-client in the host machine
$sudo apt-get install mysql-client
4)to access mysql in a container.
$mysql -uroot -p -h 172.17.0.2 -P 3306

5)FOR TESTING CREATE SOME DATABSE THE HOST.
$mysql -uroot -p -h 172.17.0.2 -P 3306
mysql>create database db1;

AND CHECK WHETHER THE SAME DATABASE IS PRESENT IN THE CONTAINER 
$docker exec -it test-mysql mysql -u root -p
mysql>show databases;
..
..
..

6)TO RUN MYSQLSLAP
/*the container containing mysql should be running prior executing the below command*/
 mysqlslap -uroot -p -h 172.17.0.2 -P 3306 --concurrency=1 --iterations=1 --auto-generate-sql --verbose --number-int-cols=5 --number-char-cols=5 --number-of-queries=100 --no-drop

/*on executing the above command open the container*/
$docker exec -it test-mysql mysql -uroot -p
mysql>show databases;
/*mysqlslap database should be present in the databases set*/ 

7)TO RUN SQLMAP
/*installing sqlmap*/
$git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
$cd sqlmap-dev
$python sqlmap.py
 
/*install pyMySQL on ubuntu*/
->install pip
$sudo apt-get install python-pip
->installing PyMySQL
$pip install PyMySQL

/*before running sqlmap
download the employees database(https://github.com/datacharmer/test_db) and extract everything then open a terminal and 
create the employees database. "THE MYSQL CONTAINER SHOULD BE RUNNING PRIOR EXECUTING THE  BELOW COMMAND."*/
$mysql -uroot -p -h 172.17.0.2 -P 3306 -t < employees.sql

/*TO VERIFY*/
$docker exec -it test-mysql mysql -uroot -p
mysql>show databases;
..
..
mysql>use employee;
mysql>select * from employee;
/*you should be able to see all the contents in the employee table WITH OUT ANY ERRORS*/

/**RUNNING MYSQMAP ON THE EMPLOYEES DATABSE OF THE CONTAINER**/
$cd sqlmap-dev
/*python sqlmap.py -d "mysql://user:password@ip_address:port/database" -f --banner --dbs --users*/
$python sqlmap.py -d "mysql://root:123@172.17.0.2:3306/employees" -f --banner --dbs --users

7)TO OPEN A NEW TERMIANL
/*to open a new terminal and move the control to the new termianl*/
$gnome-terminal disown.
 
8)TO TRACE SYSTEM CALLS 
$strace -f -p PID -tt

9)TO RUN SHELL SCRIPT

/*https://stackoverflow.com/questions/22656359/bash-shell-script-opening-multiple-terminals-and-executing-distinct-commands*/
/*https://unix.stackexchange.com/questions/31414/how-can-i-pass-a-command-line-argument-into-a-shell-script*/
/*https://www.lifewire.com/multitasking-background-foreground-process-2180219*/


/*shell.sh*/
xterm -title "App 1" -e "mycommand; mysecondcommand" 

/*shell script to run the process in the background*/
xterm -title "App 1" -e "mycommand &"
/*to run the script*/
$chmod 700 shell.sh
$./shell.sh