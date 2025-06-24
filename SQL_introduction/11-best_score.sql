-- Récupère les enregistrements avec un score >= 10 de 'second_table', triés par score décroissant

SELECT score, name
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;
