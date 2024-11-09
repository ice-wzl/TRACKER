DROP DATABASE IF EXISTS TRACKER;

CREATE DATABASE IF NOT EXISTS TRACKER;
-- Context switch
USE TRACKER;

/* CAMPAIGN Table */
/* 
Primary Key: id
Super Key: {id}
Candidate Key: id
*/
DROP TABLE IF EXISTS CAMPAIGN;
CREATE TABLE IF NOT EXISTS CAMPAIGN (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

/* Target Table */
/* 
Primary Key: id
Super Key: {id}
Candidate Key: id
Foreign Key: campaign_id, references CAMPAIGN
*/
DROP TABLE IF EXISTS TARGET;
CREATE TABLE IF NOT EXISTS TARGET (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    ip_address VARCHAR(50) NOT NULL,
    campaign_id INT,
    FOREIGN KEY (campaign_id) REFERENCES CAMPAIGN(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

/* ImplantType Table */
/* 
Primary Key: id
Super Key: {id, implant_name}, {id, version}
Candidate Key: id OR {implant_name, version}
*/
DROP TABLE IF EXISTS IMPLANTTYPE;
CREATE TABLE IF NOT EXISTS IMPLANTTYPE (
    id INT AUTO_INCREMENT PRIMARY KEY,
    implant_name VARCHAR(50) NOT NULL,
    implant_version VARCHAR(50) NOT NULL,
    implant_type VARCHAR(100) NOT NULL,
    CHECK (implant_type IN ('knock', 'beacon', 'both'))
);

/* Location Table */
/* 
Primary Key: id
Super Key: {id, State}, {id, Country}
Candidate Key: id
*/
DROP TABLE IF EXISTS LOCATION;
CREATE TABLE IF NOT EXISTS LOCATION (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    country VARCHAR(100)
);

/* Deployment Table */
/* 
Primary Key: id
Super Key: {id, install_date}, {id, point_of_contact} 
Candidate Key: id
Foreign Keys: location_id references LOCATION,
              implant_type_id references IMPLANTTYPE
*/
DROP TABLE IF EXISTS DEPLOYMENT;
CREATE TABLE IF NOT EXISTS DEPLOYMENT (
    id INT AUTO_INCREMENT PRIMARY KEY,
    install_date DATE,
    kill_date DATE,
    persistant BOOLEAN,
    point_of_contact VARCHAR(100),
    ip_address VARCHAR(50) NOT NULL,
    implant_port INT NOT NULL,
    target_id INT NOT NULL,
    campaign_id INT NOT NULL,
    location_id INT,
    implant_type_id INT,
    FOREIGN KEY (target_id) REFERENCES TARGET(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (campaign_id) REFERENCES CAMPAIGN(id)
		ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (implant_type_id) REFERENCES IMPLANTTYPE(id) 
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (location_id) REFERENCES LOCATION(id) 
        ON DELETE CASCADE ON UPDATE CASCADE
);


DROP TABLE IF EXISTS TARGETNOTES;
CREATE TABLE IF NOT EXISTS TARGETNOTES (
    id INT AUTO_INCREMENT PRIMARY KEY,
    target_id INT,
    campaign_id INT,
    date_of_note DATE,
    note LONGTEXT,
    FOREIGN KEY (target_id) REFERENCES TARGET(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (campaign_id) REFERENCES CAMPAIGN(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
