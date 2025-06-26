-- Liste les villes de l'État California sans utiliser JOIN, triées par id croissant
SELECT *
FROM cities
WHERE state_id = (SELECT id
FROM states
WHERE name = 'California')
ORDER BY id ASC;
