-- 코드를 작성해주세요
select a.ITEM_ID, ITEM_NAME
from ITEM_INFO a
left outer join ITEM_TREE b
on a.ITEM_ID = b.ITEM_ID
where PARENT_ITEM_ID is null
order by b.ITEM_ID asc