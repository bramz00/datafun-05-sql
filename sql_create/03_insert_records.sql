INSERT INTO authors (author_id, first, last) VALUES
('1', 'Isaac', 'Asimov'),
('2', 'Mary', 'Shelley'),
('3', 'Mark', 'Twain'),
('4', 'Leo', 'Tolstoy'),
('5', 'Virginia', 'Woolf'),
('6', 'Ernest', 'Hemingway'),
('7', 'Gabriel', 'Garcia Marquez'),
('8', 'Herman', 'Melville'),
('9', 'Kurt', 'Vonnegut'),
('10', 'Toni', 'Morrison');

-- Insert books
INSERT INTO books (book_id, title, year, author_id) VALUES
('1', 'Foundation', 1951, '1'),
('2', 'Frankenstein', 1818, '2'),
('3', 'Adventures of Huckleberry Finn', 1884, '3'),
('4', 'War and Peace', 1869, '4'),
('5', 'Mrs. Dalloway', 1925, '5'),
('6', 'The Old Man and the Sea', 1952, '6'),
('7', 'One Hundred Years of Solitude', 1967, '7'),
('8', 'Moby-Dick', 1851, '8'),
('9', 'Slaughterhouse-Five', 1969, '9'),
('10', 'Beloved', 1987, '10');
