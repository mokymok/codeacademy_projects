 select*from met limit 10;
 select count(*)from met;
 select count(*)from met where category like'%celery%';
 select title,medium,date from met order by date desc limit 10;
 select country,count(country) from met where country is not null group by country order by 2 desc limit 10;
 select category from met group by 1 having count(*)>100;
 select medium,count(medium)from met where medium like '%gold%'or medium like '%silver%' group by medium order by 1 desc;
