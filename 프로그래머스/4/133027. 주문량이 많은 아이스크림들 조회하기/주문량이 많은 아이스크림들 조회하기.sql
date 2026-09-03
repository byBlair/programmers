-- 코드를 입력하세요
SELECT a.FLAVOR
FROM FIRST_HALF a 
join JULY b
    on a.FLAVOR = b.FLAVOR
Group by a.FLAVOR, a.TOTAL_ORDER
order by a.TOTAL_ORDER + sum(b.Total_order) desc
Limit 3