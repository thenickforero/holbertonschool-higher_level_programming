-- Script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
