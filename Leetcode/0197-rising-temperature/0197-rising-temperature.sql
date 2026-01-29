# Write your MySQL query statement below
select w1.id 
from Weather as w1, Weather as w2
where 
    w1.temperature > w2.temperature
    AND DATEDIFF(W1.recordDate, W2.recordDate) = 1