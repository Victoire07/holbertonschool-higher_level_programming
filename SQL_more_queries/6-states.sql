-- Crée la base hbtn_0d_usa et la table states avec id auto-incrémenté en clé primaire et name obligatoire

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

