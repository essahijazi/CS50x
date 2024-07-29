SELECT p.name
FROM people p
JOIN stars star1 ON p.id = star1.person_id
JOIN stars star2 ON star1.movie_id = star2.movie_id AND star1.person_id != star2.person_id
JOIN people kb_actor ON star2.person_id = kb_actor.id
WHERE kb_actor.name = 'Kevin Bacon' AND kb_actor.birth = 1958
  AND p.name != 'Kevin Bacon'
GROUP BY p.name;
