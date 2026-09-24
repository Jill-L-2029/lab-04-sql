-- Create users table
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    created_at DATETIME
);

-- Create posts table
CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    title VARCHAR(100),
    content TEXT,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert 10 users
INSERT INTO users (user_id, username, email, created_at)
VALUES (1, 'cody', 'cody@gmail.com', '2026-09-01 09:00:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (2, 'charlie', 'charlie@gmail.com', '2026-09-01 10:00:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (3, 'stuart', 'stuart@gmail.com', '2026-09-02 09:30:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (4, 'ashley', 'ashley@gmail.com', '2026-09-02 11:00:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (5, 'katie', 'katie@gmail.com', '2026-09-03 08:45:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (6, 'bob', 'bob@gmail.com', '2026-09-03 12:00:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (7, 'emma', 'emma@gmail.com', '2026-09-04 09:15:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (8, 'henry', 'henry@gmail.com', '2026-09-04 14:30:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (9, 'justin', 'justin@gmail.com', '2026-09-05 10:20:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (10, 'brooke', 'brooke@gmail.com', '2026-09-05 16:00:00');

-- Insert 10 posts
INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (1, 1, 'My First Post', 'Hello everyone!', '2026-09-06 09:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (2, 2, 'Learning SQL', 'Today I learned about SQL.', '2026-09-06 10:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (3, 3, 'Data Science', 'I am learning about data science.', '2026-09-07 09:30:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (4, 4, 'Weekend Plans', 'Looking forward to the weekend.', '2026-09-07 11:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (5, 5, 'Python', 'Python is one of my favorite programming languages.', '2026-09-08 08:45:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (6, 6, 'Sunny', 'It is a sunny day today.', '2026-09-08 12:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (7, 7, 'Databases', 'Relational databases use tables and relationships.', '2026-09-09 09:15:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (8, 8, 'GitHub', 'GitHub makes collaboration easier.', '2026-09-09 14:30:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (9, 9, 'Virginia', 'I enjoy living in Virginia.', '2026-09-10 08:20:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (10, 10, 'SQL Scripts', 'SQL scripts let us run many commands at once.', '2026-09-10 16:00:00');