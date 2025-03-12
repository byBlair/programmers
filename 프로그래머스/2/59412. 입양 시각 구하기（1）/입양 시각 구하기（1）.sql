-- 코드를 입력하세요
SELECT hour(DATETIME) as HOUR, count(*) as count
from ANIMAL_OUTS
where hour(DATETIME) between '09:00' and '19:59'
group by hour 
Order by HOUR 