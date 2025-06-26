-- Liste les villes de l'État California sans utiliser JOIN, triées par id croissant
SELECT cities.id, cities.name FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;
