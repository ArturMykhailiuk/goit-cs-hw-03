select * from tasks where user_id = 2;

select * from tasks where status_id = (select id from status where name = 'new');

update tasks set status_id = 2 where id = 3

select * from users where id not in (select user_id from tasks)

insert into tasks(title,description,status_id,user_id) values('start', 'start new tasks', 1, 5)

select * from tasks where status_id not in (select id from status where name = 'completed')

delete from tasks where id = 11

select * from users where email like '%.com'

update users set fullname = 'Artur Mykhailiuk' where id = 4

select status_id , count(id) from tasks group by status_id 

select t.*, u.email from tasks t 
inner join users u on u.id = t.user_id and u.email like '%@example.com'

select * from tasks where description is null or description = ''

select u.fullname, t.title, t.description, s.name  from tasks t
inner join users u on u.id = t.user_id 
inner join status s on s.id = t.status_id and s.name = 'in progress'
order by u.fullname

select u.fullname, count(t.id) from tasks t
inner join users u on u.id = t.user_id 
group by (u.fullname)