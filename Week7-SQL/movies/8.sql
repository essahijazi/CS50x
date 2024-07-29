select name
from people
where id in (
    select person_id
    from stars
    where movie_id = (
        select id
        from movies
        where title = 'Toy Story'
    )
);


-- select name
-- from people
-- join stars on stars.person_id = people.id
-- join movies on stars.movie_id = movies.id
-- where title = 'Toy Story';
