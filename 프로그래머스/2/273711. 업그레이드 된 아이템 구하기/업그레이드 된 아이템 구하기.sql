-- 코드를 작성해주세요
select a.ITEM_ID,a.ITEM_NAME,a.RARITY
from ITEM_INFO a
join ITEM_TREE b
on a.ITEM_ID = b.ITEM_ID
join ITEM_INFO c
on b.PARENT_ITEM_ID = c.ITEM_ID
WHERE c.RARITY = 'RARE'
order by a.ITEM_ID desc

