-- Affiche score et nom des enregistrements avec nom non vide, triés par score décroissant

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
