-- Liste des villes avec leur État, triées par id de la table cities
USE hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities
JOIN cities.state_id ON states.id = cities.state_id
ORDER BY cities.id ASC;
