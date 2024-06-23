-- A script that lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM hbtn_0d_tvshows.tv_genres AS g
INNER JOIN hbtn_0d_tvshows.tv_show_genres AS sg
ON g.id = sg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
