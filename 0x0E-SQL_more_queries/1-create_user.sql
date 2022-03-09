-- create a server user called user_0d_1
-- with all privileges and with a passwrd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd'; -- name
GRANT ALL PRIVILEGES
ON *.*
TO user_0d_1@localhost;
