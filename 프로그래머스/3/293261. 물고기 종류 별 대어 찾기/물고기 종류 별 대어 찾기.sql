select a.ID, b.FISH_NAME, a.LENGTH
from FISH_INFO a join FISH_NAME_INFO b
on a.FISH_TYPE = b.FISH_TYPE
where (a.FISH_TYPE, a.length) in (
    select FISH_TYPE, max(length)
    from FISH_INFO
    group by FISH_TYPE
)
order by a.id asc

# 각 물고기 종류별 가장 긴 길이가 뭔지 알려줘
# 가장 큰 길이를 찾는다 서브쿼리
# 그 길이를 가진 실제 행을 찾는다