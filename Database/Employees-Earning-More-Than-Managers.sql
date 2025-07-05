SELECT 
    e.name AS Employee
FROM Employee AS e
JOIN Employee As m ON e.managerId = m.id
WHERE e.salary > m.salary 