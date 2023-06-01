-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: garcia_mathias_iinfo1b_magasin_164_2023.sql

-- Destruction de la BD si elle existe.
-- Pour être certain d'avoir la dernière version des données

DROP DATABASE IF EXISTS garcia_mathias_iinfo1b_magasin_164_2023;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS garcia_mathias_iinfo1b_magasin_164_2023;

-- Utilisation de cette base de donnée

USE garcia_mathias_iinfo1b_magasin_164_2023;
-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour garcia_mathias_iinfo1b_magasin_164_2023
CREATE DATABASE IF NOT EXISTS `garcia_mathias_iinfo1b_magasin_164_2023` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `garcia_mathias_iinfo1b_magasin_164_2023`;

-- Listage de la structure de table garcia_mathias_iinfo1b_magasin_164_2023. t_categorie
CREATE TABLE IF NOT EXISTS `t_categorie` (
  `id_categorie` int NOT NULL,
  `nom_categorie` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_categorie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table garcia_mathias_iinfo1b_magasin_164_2023.t_categorie : ~0 rows (environ)
INSERT INTO `t_categorie` (`id_categorie`, `nom_categorie`) VALUES
	(1, 'T shirt'),
	(2, 'SweetShirt'),
	(3, 'Pantalon');

-- Listage de la structure de table garcia_mathias_iinfo1b_magasin_164_2023. t_catégories_avoir_produits
CREATE TABLE IF NOT EXISTS `t_catégories_avoir_produits` (
  `id_catégories_avoir_produits` int NOT NULL AUTO_INCREMENT,
  `fk_catégories` int DEFAULT NULL,
  `fk_produits_1` int DEFAULT NULL,
  PRIMARY KEY (`id_catégories_avoir_produits`),
  KEY `fk_produits_1` (`fk_produits_1`),
  KEY `fk_catégories` (`fk_catégories`),
  CONSTRAINT `fk_catégories` FOREIGN KEY (`fk_catégories`) REFERENCES `t_catégories` (`id_catégorie`),
  CONSTRAINT `fk_produits_1` FOREIGN KEY (`fk_produits_1`) REFERENCES `t_produits` (`id_produits`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Listage des données de la table garcia_mathias_iinfo1b_magasin_164_2023.t_catégories_avoir_produits : ~0 rows (environ)

-- Listage de la structure de table garcia_mathias_iinfo1b_magasin_164_2023. t_clients
CREATE TABLE IF NOT EXISTS `t_clients` (
  `id_clients` int NOT NULL AUTO_INCREMENT,
  `prénom_clients` varchar(50) NOT NULL DEFAULT '0',
  `nom_clients` varchar(50) NOT NULL DEFAULT '0',
  `téléphone_clients` varchar(50) NOT NULL DEFAULT '0',
  `mail_clients` varchar(50) NOT NULL DEFAULT '0',
  `rue_clients` varchar(50) NOT NULL DEFAULT '0',
  `npa_clients` varchar(50) NOT NULL DEFAULT '0',
  `ville_clients` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_clients`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Listage des données de la table garcia_mathias_iinfo1b_magasin_164_2023.t_clients : ~5 rows (environ)
INSERT INTO `t_clients` (`id_clients`, `prénom_clients`, `nom_clients`, `téléphone_clients`, `mail_clients`, `rue_clients`, `npa_clients`, `ville_clients`) VALUES
	(1, 'Mathias', 'Garcia', '0792050074', 'mathias.damota@eduvaud.ch', 'chemin de primerose 35', '1007', 'Lausanne'),
	(2, 'Olivier', 'Maccaud', '0786754563', 'olivier.maccaud@eduvaud.ch', 'chemin du flon 12', '1005', 'Lausanne'),
	(3, 'Sam ', 'Gerard', '0765431289', 'sam.gerard@eduvaud.ch', 'avenue fédérale 12', '1020', 'Renens'),
	(4, 'Tobi', 'Graud', '0778905653', 'tobi.graud@eduvaud.ch', 'route du champ 56', '1022', 'Chavannes-près-renens'),
	(5, 'Renaud', 'Dell', '0754534545', 'renaud.dell@eduvaud.ch', 'rue de ta mere 7', '1053', 'Romanel-sur-Lausanne');

-- Listage de la structure de table garcia_mathias_iinfo1b_magasin_164_2023. t_clients_avoir_commandes
CREATE TABLE IF NOT EXISTS `t_clients_avoir_commandes` (
  `id_clients_avoir_commandes` int NOT NULL AUTO_INCREMENT,
  `fk_clients` int DEFAULT NULL,
  `fk_commandes` int DEFAULT NULL,
  PRIMARY KEY (`id_clients_avoir_commandes`),
  KEY `fk_clients` (`fk_clients`),
  KEY `fk_commandes` (`fk_commandes`),
  CONSTRAINT `fk_clients` FOREIGN KEY (`fk_clients`) REFERENCES `t_clients` (`id_clients`),
  CONSTRAINT `fk_commandes` FOREIGN KEY (`fk_commandes`) REFERENCES `t_commandes` (`id_commandes`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Listage des données de la table garcia_mathias_iinfo1b_magasin_164_2023.t_clients_avoir_commandes : ~2 rows (environ)
INSERT INTO `t_clients_avoir_commandes` (`id_clients_avoir_commandes`, `fk_clients`, `fk_commandes`) VALUES
	(1, 1, 1),
	(2, 2, 2);

-- Listage de la structure de table garcia_mathias_iinfo1b_magasin_164_2023. t_commandes
CREATE TABLE IF NOT EXISTS `t_commandes` (
  `id_commandes` int NOT NULL AUTO_INCREMENT,
  `date_commandes` date NOT NULL,
  `date_expeditions_commandes` date NOT NULL,
  `montant_commandes` varchar(50) NOT NULL,
  PRIMARY KEY (`id_commandes`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Listage des données de la table garcia_mathias_iinfo1b_magasin_164_2023.t_commandes : ~2 rows (environ)
INSERT INTO `t_commandes` (`id_commandes`, `date_commandes`, `date_expeditions_commandes`, `montant_commandes`) VALUES
	(1, '2018-08-10', '2018-08-13', '45.50'),
	(2, '2019-04-20', '2019-04-23', '97.90');

-- Listage de la structure de table garcia_mathias_iinfo1b_magasin_164_2023. t_produits
CREATE TABLE IF NOT EXISTS `t_produits` (
  `id_produits` int NOT NULL DEFAULT '0',
  `référence_produits` varchar(50) DEFAULT NULL,
  `couleur_produits` varchar(50) DEFAULT NULL,
  `type_produits` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_produits`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Listage des données de la table garcia_mathias_iinfo1b_magasin_164_2023.t_produits : ~8 rows (environ)
INSERT INTO `t_produits` (`id_produits`, `référence_produits`, `couleur_produits`, `type_produits`) VALUES
	(1, '12345', 'Blanc', 'Tshirt'),
	(2, '42343', 'Noir', 'Pantalon'),
	(3, '234242', 'Bleu', 'Pantalon'),
	(4, '24234', 'Violet', 'SweetShirt'),
	(5, '97643', 'Blanc', 'SweetShirt'),
	(6, '87669', 'Vert', 'Pantalon'),
	(7, '87616', 'Noir', 'Tshirt'),
	(8, '56913', 'Orange', 'Tshirt');

-- Listage de la structure de table garcia_mathias_iinfo1b_magasin_164_2023. t_produits_avoir_commandes
CREATE TABLE IF NOT EXISTS `t_produits_avoir_commandes` (
  `id_produits_avoir_commandes` int NOT NULL AUTO_INCREMENT,
  `fk_produits` int DEFAULT NULL,
  `fk_commandes_1` int DEFAULT NULL,
  PRIMARY KEY (`id_produits_avoir_commandes`),
  KEY `fk_produits` (`fk_produits`),
  KEY `fk_commandes_1` (`fk_commandes_1`),
  CONSTRAINT `fk_commandes_1` FOREIGN KEY (`fk_commandes_1`) REFERENCES `t_commandes` (`id_commandes`),
  CONSTRAINT `fk_produits` FOREIGN KEY (`fk_produits`) REFERENCES `t_produits` (`id_produits`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Listage des données de la table garcia_mathias_iinfo1b_magasin_164_2023.t_produits_avoir_commandes : ~0 rows (environ)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
