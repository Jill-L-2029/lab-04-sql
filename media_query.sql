SELECT users.username, users.email, posts.title, posts.content
FROM users
JOIN posts
    ON users.user_id = posts.user_id
WHERE users.username = 'cody';