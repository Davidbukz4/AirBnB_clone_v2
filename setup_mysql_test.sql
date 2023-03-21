-- prepares mysql database for a project --
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localholst' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db` TO 'hbnb_text'@'localhost';
GRANT SELECTION ON `performance_schema`.* TO 'hbnb_test'@'localholst';
