-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID, date_format(START_DATE,'20%y-%m-%d') as START_DATE, date_format(END_DATE,'20%y-%m-%d') as END_DATE ,IF(DATEDIFF(END_DATE, START_DATE) + 1 >= 30, '장기 대여', '단기 대여') AS RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where DATE_FORMAT(START_DATE, '%Y-%m') = '2022-09'
order by HISTORY_ID desc
