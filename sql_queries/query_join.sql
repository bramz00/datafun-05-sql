SELECT b.title, b.year, a.first, a.last
FROM books b
INNER JOIN authors a ON b.author_id = a.author_id;

SELECT a.first, a.last, b.title
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id;