-- Liste des villes avec leur État, triées par id de la table cities
SELECT cities.id, cities.name, states.name
INNER JOIN cities.state_id = states.id
ORDER BY cities.id ASC;

