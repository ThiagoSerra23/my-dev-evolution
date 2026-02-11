SELECT o.Id, u.Username, o.Total 
FROM Orders o 
JOIN Users u ON o.UserId = u.Id 
WHERE o.Total > 100 
ORDER BY o.CreatedAt DESC;