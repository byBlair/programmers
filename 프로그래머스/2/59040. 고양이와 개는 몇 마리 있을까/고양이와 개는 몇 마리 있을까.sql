select ANIMAL_TYPE, count(*) as count
from ANIMAL_INS
where ANIMAL_TYPE in ("Cat","Dog")
group by ANIMAL_TYPE
    order by case ANIMAL_TYPE
    when 'Cat' then 1
    when 'Dog' then 2
end;