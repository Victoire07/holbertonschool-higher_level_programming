-- Crée la table id_not_null avec deux colonnes : id (valeur par défaut 1) et name
CREATE TABLE IF NOT EXISTS id_not_null
(
    id INT DEFAULT 1,
    name VARCHARD(256),
);
