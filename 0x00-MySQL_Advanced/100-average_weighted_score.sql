-- Compute a user's weighted average score


DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
DECLARE w_average_score FLOAT;
SET w_average_score=(SELECT SUM(score * weight) / SUM(weight)
FROM users
JOIN corrections ON users.id=corrections.user_id
JOIN projects ON corrections.project_id=projects.id
WHERE id=user_id);
UPDATE users SET average_score = w_average_score
WHERE id=user_id
END$$
DELIMITER ;
