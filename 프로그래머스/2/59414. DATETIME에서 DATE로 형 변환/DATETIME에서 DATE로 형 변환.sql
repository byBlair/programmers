-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, date_format(DATETIME,'20%y-%m-%d') as DATE
from ANIMAL_INS
order by ANIMAL_ID