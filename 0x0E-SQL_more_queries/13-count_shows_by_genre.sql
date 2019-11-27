-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT
-- First column must be called genre
tv_genres.name AS genre,
-- Second column must be called number_of_shows
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres, tv_show_genres, tv_shows
-- Don’t display a genre that doesn’t have any shows linked
WHERE
tv_genres.id = tv_show_genres.genre_id
AND
tv_shows.id = tv_show_genres.show_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
