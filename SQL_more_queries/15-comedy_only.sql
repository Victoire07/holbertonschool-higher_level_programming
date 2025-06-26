-- Script qui affiche tous les titres des séries de genre "Comedy" dans la base hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_showstv_shows
WHERE name in TABLE tv_genres = 'Comedy'
ORDER BY tv_shows.title DESC;
