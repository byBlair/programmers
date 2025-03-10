-- 코드를 입력하세요
SELECT a.FLAVOR
From FIRST_HALF a
join ICECREAM_INFO b on b.FLAVOR = a.FLAVOR
where 3000 < a.TOTAL_ORDER and INGREDIENT_TYPE = 'fruit_based'
order by a.TOTAL_ORDER desc