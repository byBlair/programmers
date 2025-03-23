-- 코드를 입력하세요
SELECT CAR_ID,
        case
        when exists (
            select 1
            from CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
            where h.CAR_ID = c.CAR_ID
            and date '2022-10-16' between h.start_date and h.end_date)
            then '대여중'
            else '대여 가능'
            end as AVAILABILITY
From (
        select distinct CAR_ID
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY) as c
order by CAR_ID desc