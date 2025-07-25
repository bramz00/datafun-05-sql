SELECT author_id, COUNT(*) AS book_count
FROM books
GROUP BY author_id;

SELECT author_id, AVG(year) AS avg_year
FROM books
GROUP BY author_id;
