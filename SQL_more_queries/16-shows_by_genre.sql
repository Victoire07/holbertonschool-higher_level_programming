-- Script SQL qui affiche tous les shows, et pour chacun : le ou les genres associés ou NULL s’il n’a aucun genre !
SELECT tv_shows.title AS title, tv_genres.name AS  name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
