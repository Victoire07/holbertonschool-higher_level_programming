-- Crée la table force_name avec une contrainte NOT NULL sur la colonne name
CREATE TABLE IF NOT EXISTS force_name
(
    int INT,
    name VARCHAR(256) NOT  NULL,
);
