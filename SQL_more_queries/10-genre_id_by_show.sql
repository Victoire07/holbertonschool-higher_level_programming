-- Liste les titres de séries avec au moins un genre associé, triés par titre et id de genre
SELECT tv_shows, tv_show_genres
INNER JOIN genres ON tv_show_genres = genres.id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, genres.id;
ORDER BY cities.id ASC;
