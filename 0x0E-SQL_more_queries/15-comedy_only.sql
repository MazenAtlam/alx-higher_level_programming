-- A script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT s.title AS title FROM hbtn_0d_tvshows.tv_shows AS s
INNER JOIN hbtn_0d_tvshows.tv_show_genres AS sg ON s.id = sg.show_id
INNER JOIN hbtn_0d_tvshows.tv_genres AS g ON g.id = sg.genre_id
WHERE g.name = 'Comedy'
ORDER BY s.title;
