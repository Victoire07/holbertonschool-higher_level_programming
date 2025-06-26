-- Liste tous les genres associés à la série "Dexter", triés par ordre alphabétique du nom du genre
SELECT tv_genres.name AS genre
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
