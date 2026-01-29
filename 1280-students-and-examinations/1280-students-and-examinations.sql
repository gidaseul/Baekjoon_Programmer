# Write your MySQL query statement below
select
    s.student_id, 
    s.student_name, 
    sub.subject_name,
    COUNT(e.student_id) AS attended_exams
from
    Students AS s
cross join     
    Subjects AS sub
left join
    Examinations as e 

on 
    s.student_id = e.student_id and sub.subject_name = e.subject_name

Group by     
    s.student_id,
    s.student_name,
    sub.subject_name
order by
    s.student_id,
    sub.subject_name;
