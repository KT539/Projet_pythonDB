SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


DROP SCHEMA IF EXISTS `festival_PythonDB`;
CREATE SCHEMA IF NOT EXISTS `festival_PythonDB` DEFAULT CHARACTER SET utf8;
USE `festival_PythonDB`;

DROP TABLE IF EXISTS  `bands`;
CREATE TABLE if NOT EXISTS `bands`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(50) NOT NULL UNIQUE,
	`genre` VARCHAR(25) NOT NULL, 
	`origin` VARCHAR(25) NULL,
	`description` VARCHAR(100) NOT NULL,
	PRIMARY KEY (`id`))
ENGINE = INNODB;

DROP TABLE IF EXISTS  `visitors`;
CREATE TABLE if NOT EXISTS `visitors`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`first_name` VARCHAR(25) NOT NULL,
	`last_name` VARCHAR(25) NOT NULL, 
	`birthdate` DATE NULL,
	`email` VARCHAR(75) NOT NULL UNIQUE,
	`hash`VARCHAR(100) NOT NULL UNIQUE,
	`is_admin` BOOLEAN NOT NULL,
	PRIMARY KEY (`id`))
ENGINE = INNODB;

DROP TABLE IF EXISTS  `concerts`;
CREATE TABLE if NOT EXISTS `concerts`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(25) NOT NULL UNIQUE,
	`date` DATETIME NOT NULL, 
	`price` FLOAT NOT NULL,
	`scene_number`INT NOT NULL,
	`max_capacity` INT NOT NULL,
	`band_id` INT NOT NULL,
	PRIMARY KEY (`id`),
	INDEX `fk_concerts_bands_idx` (`band_id`),
	CONSTRAINT `fk_concerts_bands`
		FOREIGN KEY (`band_id`)
		REFERENCES `bands` (`id`)
		ON DELETE CASCADE
		ON UPDATE CASCADE)
ENGINE = INNODB;

DROP TABLE IF EXISTS  `reservations`;
CREATE TABLE if NOT EXISTS `reservations`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`date_reservation` DATE NOT NULL,
	`concert_id` INT NOT NULL, 
	`visitor_id` INT NOT NULL,
	PRIMARY KEY (`id`),
	INDEX `fk_reservations_concerts_idx` (`concert_id`),
  CONSTRAINT `fk_reservations_concerts`
  	FOREIGN KEY (`concert_id`)
  	REFERENCES `concerts` (`id`)
  	ON DELETE CASCADE
  	ON UPDATE CASCADE,
  INDEX `fk_reservations_visitors_idx` (`visitor_id`),
  CONSTRAINT `fk_reservations_visitors`
  	FOREIGN KEY (`visitor_id`)
  	REFERENCES `visitors` (`id`)
  	ON DELETE CASCADE
	ON UPDATE CASCADE)
ENGINE = InnoDB;