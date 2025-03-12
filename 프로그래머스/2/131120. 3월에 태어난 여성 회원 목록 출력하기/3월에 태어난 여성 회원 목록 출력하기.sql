select MEMBER_ID,MEMBER_NAME,GENDER,date_format(DATE_OF_BIRTH,'19%y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where month(DATE_OF_BIRTH) = 03 and TLNO is not null and GENDER = 'W'
order by MEMBER_ID asc