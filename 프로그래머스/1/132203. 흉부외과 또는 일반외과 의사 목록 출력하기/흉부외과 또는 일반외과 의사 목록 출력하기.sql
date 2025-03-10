select DR_NAME, DR_ID, MCDP_CD, date_format(Hire_ymd, '%Y-%m-%d') as HIRE_YMD
from doctor
where MCDP_CD in ("cs","gs")
order by HIRE_YMD desc, DR_NAME ASC;