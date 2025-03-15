-- 코드를 입력하세요
SELECT a.ANIMAL_ID, b.name
From ANIMAL_INS a
join ANIMAL_OUTS b
on a.ANIMAL_ID = b.ANIMAL_ID
order by DATEDIFF(b.DATETIME, a.DATETIME) DESC
limit 2
