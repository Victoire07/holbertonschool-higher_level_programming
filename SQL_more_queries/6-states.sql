-- Crée la base hbtn_0d_usa et la table states avec id auto-incrémenté en clé primaire et name obligatoire

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
