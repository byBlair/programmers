-- 코드를 입력하세요
SELECT a.BOOK_ID, b.AUTHOR_NAME, a.PUBLISHED_DATE
FROM BOOK a 
join AUTHOR b
on a.AUTHOR_ID = b.AUTHOR_ID
where a.CATEGORY = "경제" 
order by a.PUBLISHED_DATE asc