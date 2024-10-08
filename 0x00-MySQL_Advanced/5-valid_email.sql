-- Validate user email on update
DELIMITER $$
CREATE TRIGGER valid_email_reset
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
IF OLD.email <> NEW.email
THEN
SET NEW.valid_email = 0;
END IF;
END$$
DELIMITER ;
