-- 코드를 입력하세요
SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT
where (price,CATEGORY) in (
                select max(PRICE),CATEGORY
                from FOOD_PRODUCT
                WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY CATEGORY
    )
order by PRICE desc 
