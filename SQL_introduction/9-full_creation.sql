-- Créer une nouvelle table appelée second_table dans la base hbtn_0c_0 avec 3 colonnes !
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);

-- Insérer dans cette table plusieurs lignes
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
