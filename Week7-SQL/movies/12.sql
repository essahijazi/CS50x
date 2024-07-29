select title
from movies
join stars on stars.movie_id = movies.id
join people on stars.person_id = people.id
where name in ('Bradley Cooper', 'Jennifer Lawrence')
group by title
having count(distinct name) = 2;
