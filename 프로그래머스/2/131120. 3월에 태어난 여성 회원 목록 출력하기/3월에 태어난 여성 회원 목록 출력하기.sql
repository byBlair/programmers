-- 코드를 입력하세요
SELECT member_id, member_name, gender, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from member_profile
where month(date_of_birth) = 3 and TLNO is not null and GENDER = 'W'
order by member_id asc
