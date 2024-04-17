-- This script prepares MySQL server

CREATE DATABASE if NOT EXISTS hbnb_test_db;
CREATE USER if NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

FLUSH PRIVILEGES;
