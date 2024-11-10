USE TRACKER;

-- ------------------------------
DROP FUNCTION IF EXISTS GetCampaignName;
DELIMITER $$

CREATE FUNCTION GetCampaignName(p_campaign_id INT)
RETURNS VARCHAR(100)
DETERMINISTIC
BEGIN
    DECLARE campaign_name VARCHAR(100) DEFAULT 'Campaign not found';

    SELECT name INTO campaign_name
    FROM CAMPAIGN
    WHERE id = p_campaign_id;

    RETURN campaign_name;
END $$

DELIMITER ;
-- ------------------------------
DROP FUNCTION IF EXISTS GetCampaignId;
DELIMITER $$

CREATE FUNCTION GetCampaignId(p_campaign_name VARCHAR(100))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE campaign_id INT DEFAULT NULL;

    SELECT id into campaign_id

    FROM CAMPAIGN
    WHERE name = p_campaign_name;

    return campaign_id;
END $$

DELIMITER ;

-- ------------------------------
DROP FUNCTION IF EXISTS GetTargetId;
DELIMITER $$

CREATE FUNCTION GetTargetId(p_target_name VARCHAR(100))
RETURNS INT
DETERMINISTIC
BEGIN 
    DECLARE target_id INT DEFAULT NULL;

    SELECT id INTO target_id
    FROM TARGET
    WHERE name = p_target_name;
    
    RETURN target_id;
END $$

DELIMITER ;

-- ------------------------------

DROP FUNCTION IF EXISTS GetTargetName;
DELIMITER $$

CREATE FUNCTION GetTargetName(p_target_id INT)
RETURNS VARCHAR(100)
DETERMINISTIC
BEGIN 
    DECLARE target_name VARCHAR(100) DEFAULT 'Target not found';

    SELECT name INTO target_name
    FROM TARGET
    WHERE id = p_target_id;

    RETURN target_name;
END $$

DELIMITER ;
-- ------------------------------
DELIMITER $$
DROP PROCEDURE IF EXISTS GetTargetNormalized$$

CREATE PROCEDURE GetTargetNormalized()
BEGIN 
    SELECT
        T.id,
        T.name,
        T.ip_address,
        T.mac_address,
        GetCampaignName(T.campaign_id) as campaign_name
    FROM 
        TARGET T;
END$$

DELIMITER ;

-- ------------------------------

DELIMITER $$
DROP PROCEDURE IF EXISTS GetDeploymentDetails$$

CREATE PROCEDURE GetDeploymentDetails()
BEGIN
    SELECT 
		D.id,
        D.install_date, 
        D.kill_date,
        D.ip_address,
        D.implant_port,
        GetTargetName(D.target_id) AS target_name,
        L.State AS location,
        L.Country AS country,
        IT.implant_name,
        IT.implant_version as implant_version
    FROM
        DEPLOYMENT D
    JOIN 
        LOCATION L ON D.location_id = L.id
    JOIN
        TARGET T ON D.target_id = T.id
    JOIN
        IMPLANTTYPE IT ON D.implant_type_id = IT.id;

END$$

DELIMITER ;
-- ------------------------------

DELIMITER $$

DROP PROCEDURE IF EXISTS AddDeployment$$

CREATE PROCEDURE AddDeployment(
    IN p_install_date DATE,
    IN p_kill_date DATE,
    IN p_persistant BOOLEAN,
    IN p_point_of_contact VARCHAR(100),
    IN p_ip_address VARCHAR(100),
    IN p_implant_port INT,
    IN p_target_id INT,
    IN p_campaign_id INT,
    IN p_location_id INT,
    IN p_implant_type_id INT
)
BEGIN
    INSERT INTO DEPLOYMENT (
        install_date, 
        kill_date, 
        persistant, 
        point_of_contact, 
        ip_address,
        implant_port,
        target_id,
        campaign_id,
        location_id, 
        implant_type_id
    ) 
    VALUES (
        p_install_date, 
        p_kill_date, 
        p_persistant, 
        p_point_of_contact, 
        p_ip_address,
        p_implant_port,
        p_target_id,
        p_campaign_id,
        p_location_id, 
        p_implant_type_id
    );
END$$

DELIMITER ;
-- ------------------------------
DELIMITER $$

DROP PROCEDURE IF EXISTS AddLocation$$

CREATE PROCEDURE AddLocation(
	IN p_state VARCHAR(100),
    IN p_country VARCHAR(100)
)
BEGIN
	INSERT INTO LOCATION (
		state,
        country
    )
	VALUES (
		p_state,
        p_country
	);
END$$

DELIMITER ;

-- ------------------------------
DELIMITER $$

DROP PROCEDURE IF EXISTS AddImplant$$

CREATE PROCEDURE AddImplant(
	IN p_implant_name VARCHAR(100),
    IN p_implant_version VARCHAR(100),
    IN p_implant_type VARCHAR(100)
)
BEGIN
	INSERT INTO IMPLANTTYPE (
		implant_name,
        implant_version,
        implant_type
    )
	VALUES (
		p_implant_name,
        p_implant_version,
        p_implant_type
	);
END$$

DELIMITER ;


-- ------------------------------
DELIMITER $$

DROP PROCEDURE IF EXISTS AddCampaign$$

CREATE PROCEDURE AddCampaign(
	IN p_name VARCHAR(100)
)
BEGIN
	INSERT INTO CAMPAIGN (
		name
    )
	VALUES (
		p_name
	);
END$$

DELIMITER ;

-- ------------------------------
DELIMITER $$

DROP PROCEDURE IF EXISTS AddTarget$$

CREATE PROCEDURE AddTarget(
	IN p_name VARCHAR(100),
    IN p_ip_address VARCHAR(100),
    IN p_mac_address VARCHAR(100),
    IN p_campaign_id INT
)
BEGIN
	INSERT INTO TARGET (
		name,
        ip_address,
        mac_address,
        campaign_id
    )
	VALUES (
		p_name,
        p_ip_address,
        p_mac_address,
        p_campaign_id
	);
END$$

DELIMITER ;
