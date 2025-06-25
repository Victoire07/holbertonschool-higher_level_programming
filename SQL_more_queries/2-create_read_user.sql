-- Crée la base hbtn_0d_2 et l’utilisateur user_0d_2 avec droit de lecture uniquement
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
