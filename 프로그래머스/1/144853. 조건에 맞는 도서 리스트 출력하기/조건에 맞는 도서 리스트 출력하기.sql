-- 코드를 입력하세요
SELECT BOOK_ID, date_format(PUBLISHED_DATE,'20%y-%m-%d') as PUBLISHED_DATE
from BOOK
where year(PUBLISHED_DATE) = 2021 and CATEGORY = "인문"