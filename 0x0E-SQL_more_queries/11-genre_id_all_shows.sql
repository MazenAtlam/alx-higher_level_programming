-- A script that lists all shows contained in the database hbtn_0d_tvshows
SELECT s.title AS title, g.genre_id AS genre_id
FROM hbtn_0d_tvshows.tv_shows AS s
JOIN hbtn_0d_tvshows.tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
