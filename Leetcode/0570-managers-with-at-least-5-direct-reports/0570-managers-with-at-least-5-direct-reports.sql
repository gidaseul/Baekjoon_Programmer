SELECT e.name AS name
FROM Employee AS e
JOIN Employee AS r
  ON e.id = r.managerId          -- e = 매니저, r = 직속 부하
GROUP BY e.id, e.name
HAVING COUNT(*) >= 5;             -- 직속 부하가 5명 이상
