drop database if exists Videostore;
drop database if exists cars;

create database cars;



use cars;

create table User(
	user_id varchar(20) NOT NULL,
	email_id varchar(30) NOT NULL,
	username varchar(20) NOT NULL,
	password varchar(20) NOT NULL,
	DOB date,
	primary key(user_id), 
	UNIQUE(email_id)
);

create table Account(
	user_id varchar(20) NOT NULL,
	number_cars integer default 0 check (number_channels <= 2000),
	primary key (user_id,number_cars),
	foreign key (user_id) references User(user_id) on delete cascade
);





