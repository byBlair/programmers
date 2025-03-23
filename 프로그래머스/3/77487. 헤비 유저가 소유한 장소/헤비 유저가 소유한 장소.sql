-- 코드를 입력하세요
SELECT ID, name, HOST_ID
from PLACES a
where HOST_ID in (
        select HOST_ID
        from places
        group by HOST_ID
        having count(HOST_ID) >= 2)
order by ID 