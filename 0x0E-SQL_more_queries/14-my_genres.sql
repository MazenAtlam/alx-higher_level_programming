-- A script that uses the hbtn_0d_tvshows database
-- to lists all genres of the show Dexter
SELECT g.name AS name FROM hbtn_0d_tvshows.tv_genres AS g
INNER JOIN hbtn_0d_tvshows.tv_show_genres AS sg ON g.id = sg.genre_id
INNER JOIN hbtn_0d_tvshows.tv_shows AS s ON s.id = sg.show_id
WHERE s.title = 'Dexter'
ORDER BY name;
