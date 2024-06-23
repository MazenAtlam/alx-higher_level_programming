-- A script that lists all shows contained in hbtn_0d_tvshows that
-- have at least one genre linked
SELECT s.title AS title, g.genre_id AS genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
