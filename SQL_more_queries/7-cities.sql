-- Crée la table cities dans hbtn_0d_usa avec une clé étrangère vers la table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    state_id INT  NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
