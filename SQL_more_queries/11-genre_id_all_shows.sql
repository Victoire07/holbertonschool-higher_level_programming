-- Liste toutes les séries avec leurs identifiants de genre s’ils existent, sinon NULL, triées par titre et genre_id
USE hbtn_0d_tvshows;
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
