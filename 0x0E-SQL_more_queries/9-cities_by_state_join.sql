-- A script that lists all cities contained in the database hbtn_0d_usa\
SELECT c.id AS id, c.name AS name, s.name AS name
FROM hbtn_0d_usa.cities AS c
LEFT JOIN hbtn_0d_usa.states AS s
ON c.state_id = s.id
ORDER BY c.id;