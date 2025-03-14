-- 코드를 입력하세요
SELECT distinct(a.CAR_ID)
from CAR_RENTAL_COMPANY_CAR a
join CAR_RENTAL_COMPANY_RENTAL_HISTORY b
on a.CAR_ID = b.CAR_ID
where a.CAR_TYPE like '%세단%' and DATE_FORMAT(b.START_DATE, '%Y-%m') = '2022-10' 
order by CAR_ID desc