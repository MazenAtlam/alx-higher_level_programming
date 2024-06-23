-- A script that lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows
SELECT s.title AS title, g.name As name
FROM hbtn_0d_tvshows.tv_shows AS s
LEFT JOIN hbtn_0d_tvshows.tv_show_genres As sg ON s.id = sg.show_id
LEFT JOIN hbtn_0d_tvshows.tv_genres AS g ON g.id = sg.genre_id
ORDER BY s.title, g.name;
