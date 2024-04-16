-- his script creates a MySQL server

CREATE DATABASE if NOT EXISTS hbnb_dev_db;
CREATE USER if NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
