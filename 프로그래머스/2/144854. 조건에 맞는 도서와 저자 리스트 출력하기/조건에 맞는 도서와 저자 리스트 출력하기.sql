select a.BOOK_ID, b.AUTHOR_NAME, date_format(a.PUBLISHED_DATE,'20%y-%m-%d') as PUBLISHED_DATE
from BOOK a
left join AUTHOR b
on a.AUTHOR_ID = b.AUTHOR_ID
where a.CATEGORY = '경제'
order by PUBLISHED_DATE asc