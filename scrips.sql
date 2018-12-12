create database mytestapp

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100),
  `email` int(100),
  `username` varchar(30),
  `password` varchar(100),
  `register_date` timestamp default current_timestamp,
  PRIMARY KEY (`id`)
)

show tables
describe users