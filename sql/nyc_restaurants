select*from nomnom;
select distinct neighborhood from nomnom;
select distinct cuisine from nomnom;
select*from nomnom where cuisine='Chinese';
select*from nomnom where review>=4.0;
select*from nomnom where cuisine='Italian'and price='$$$';
select*from nomnom where name like'%meatball%';
select*from nomnom where neighborhood='Midtown'or neighborhood='Downtown'or neighborhood='Chinatown';
select*from nomnom where health is null;
select*from nomnom order by review desc limit 10;
select name,
 case
  when review>4.5 then'extraordinary'
  when review>4 then'excellent'
  when review>3 then'good'
  when review>2 then'fair'
  else'poor'
 end as'review'
from nomnom;
