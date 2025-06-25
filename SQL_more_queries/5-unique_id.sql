-- Table unique_id avec un id unique par défaut à 1 et une colonne name
CREATE TABLE IF NOT EXISTS unique_id
(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
