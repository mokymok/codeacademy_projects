 select*from transactions limit 10;
 select sum(money_in)from transactions;
 select sum(money_out)from transactions;
 select count(money_in)from transactions;
 select count(money_in)from transactions where currency="BIT";
 select max(money_in),max(money_out)from transactions;
 select avg(money_in)from transactions where currency='ETH';
 select date,avg(money_in),avg(money_out)from transactions group by date;
 select date,round(avg(money_in),2)as'Average Buy',round(avg(money_out),2)as'Average Sell'from transactions group by date;
