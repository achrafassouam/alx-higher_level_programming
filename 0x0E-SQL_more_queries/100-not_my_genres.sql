-- a script that lists all shows, and all genres linked to that show
-- from the database hbtn_0d_tvshows

SELECT name
FROM tv_genres
WHERE name
NOT IN (SELECT a.name FROM tv_genres a
	RIGHT JOIN tv_show_genres b
	ON a.id = b.genre_id 
	RIGHT JOIN tv_shows c
	ON b.show_id = c.id 
	WHERE c.title = 'Dexter')
ORDER BY 1 ASC;
