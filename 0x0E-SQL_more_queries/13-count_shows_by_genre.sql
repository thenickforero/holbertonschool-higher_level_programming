-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT
-- First column must be called genre
tv_genres.name AS genre,
-- Second column must be called number_of_shows
COUNT(tv_show_genres) AS number_of_shows
FROM tv_show_genres
-- Don’t display a genre that doesn’t have any shows linked
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
-- Results must be sorted in descending order by the number of shows linked
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
