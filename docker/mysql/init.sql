-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: healthcare_api
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `access_logs`
--

CREATE DATABASE IF NOT EXISTS healthcare_api
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE healthcare_api;

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `access_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `access_logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `ip_address` varchar(45) DEFAULT NULL,
  `user_agent` varchar(255) DEFAULT NULL,
  `action` varchar(100) DEFAULT NULL,
  `resource` varchar(100) DEFAULT NULL,
  `details` text DEFAULT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_access_user` (`user_id`),
  CONSTRAINT `fk_access_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=165 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `access_logs`
--

LOCK TABLES `access_logs` WRITE;
/*!40000 ALTER TABLE `access_logs` DISABLE KEYS */;
INSERT INTO `access_logs` VALUES (1,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/apidocs/',NULL,'2026-01-22 03:02:04','2026-01-22 03:02:04','2026-01-22 03:02:04'),(2,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/swagger-ui.css',NULL,'2026-01-22 03:02:05','2026-01-22 03:02:05','2026-01-22 03:02:05'),(3,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/swagger-ui-bundle.js',NULL,'2026-01-22 03:02:05','2026-01-22 03:02:05','2026-01-22 03:02:05'),(4,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/swagger-ui-standalone-preset.js',NULL,'2026-01-22 03:02:05','2026-01-22 03:02:05','2026-01-22 03:02:05'),(5,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/lib/jquery.min.js',NULL,'2026-01-22 03:02:05','2026-01-22 03:02:05','2026-01-22 03:02:05'),(6,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/favicon-32x32.png',NULL,'2026-01-22 03:02:06','2026-01-22 03:02:06','2026-01-22 03:02:06'),(7,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/apispec_1.json',NULL,'2026-01-22 03:02:07','2026-01-22 03:02:07','2026-01-22 03:02:07'),(8,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/people/',NULL,'2026-01-22 03:03:23','2026-01-22 03:03:23','2026-01-22 03:03:23'),(9,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/users/',NULL,'2026-01-22 03:04:19','2026-01-22 03:04:19','2026-01-22 03:04:19'),(10,NULL,'127.0.0.1','Thunder Client (https://www.thunderclient.com)','POST','/auth/login',NULL,'2026-01-22 03:07:28','2026-01-22 03:07:28','2026-01-22 03:07:28'),(11,NULL,'127.0.0.1','Thunder Client (https://www.thunderclient.com)','POST','/auth/login',NULL,'2026-01-22 03:09:34','2026-01-22 03:09:34','2026-01-22 03:09:34'),(12,1,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/professionals/',NULL,'2026-01-22 03:09:49','2026-01-22 03:09:49','2026-01-22 03:09:49'),(13,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/people/',NULL,'2026-01-22 03:15:16','2026-01-22 03:15:16','2026-01-22 03:15:16'),(14,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/people/',NULL,'2026-01-22 03:15:37','2026-01-22 03:15:37','2026-01-22 03:15:37'),(15,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/people/',NULL,'2026-01-22 03:15:52','2026-01-22 03:15:52','2026-01-22 03:15:52'),(16,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/people/',NULL,'2026-01-22 03:16:01','2026-01-22 03:16:01','2026-01-22 03:16:01'),(17,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/professionals/',NULL,'2026-01-22 03:17:22','2026-01-22 03:17:22','2026-01-22 03:17:22'),(18,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/professionals/',NULL,'2026-01-22 03:17:33','2026-01-22 03:17:33','2026-01-22 03:17:33'),(19,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/professionals/',NULL,'2026-01-22 03:17:40','2026-01-22 03:17:40','2026-01-22 03:17:40'),(20,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/professionals/',NULL,'2026-01-22 03:17:45','2026-01-22 03:17:45','2026-01-22 03:17:45'),(21,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/professionals/',NULL,'2026-01-22 03:17:54','2026-01-22 03:17:54','2026-01-22 03:17:54'),(22,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/units/',NULL,'2026-01-22 03:18:32','2026-01-22 03:18:32','2026-01-22 03:18:32'),(23,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/units/',NULL,'2026-01-22 03:18:38','2026-01-22 03:18:38','2026-01-22 03:18:38'),(24,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/units/',NULL,'2026-01-22 03:18:41','2026-01-22 03:18:41','2026-01-22 03:18:41'),(25,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/units/',NULL,'2026-01-22 03:18:48','2026-01-22 03:18:48','2026-01-22 03:18:48'),(26,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/units/',NULL,'2026-01-22 03:18:55','2026-01-22 03:18:55','2026-01-22 03:18:55'),(27,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/episodes/',NULL,'2026-01-22 03:20:08','2026-01-22 03:20:08','2026-01-22 03:20:08'),(28,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/episodes/',NULL,'2026-01-22 03:20:15','2026-01-22 03:20:15','2026-01-22 03:20:15'),(29,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/episodes/',NULL,'2026-01-22 03:20:23','2026-01-22 03:20:23','2026-01-22 03:20:23'),(30,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/episodes/',NULL,'2026-01-22 03:20:28','2026-01-22 03:20:28','2026-01-22 03:20:28'),(31,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/episodes/',NULL,'2026-01-22 03:20:34','2026-01-22 03:20:34','2026-01-22 03:20:34'),(32,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/orders/',NULL,'2026-01-22 03:21:46','2026-01-22 03:21:46','2026-01-22 03:21:46'),(33,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/orders/',NULL,'2026-01-22 03:22:19','2026-01-22 03:22:19','2026-01-22 03:22:19'),(34,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/orders/',NULL,'2026-01-22 03:22:28','2026-01-22 03:22:28','2026-01-22 03:22:28'),(35,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/orders/',NULL,'2026-01-22 03:22:35','2026-01-22 03:22:35','2026-01-22 03:22:35'),(36,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/orders/',NULL,'2026-01-22 03:22:44','2026-01-22 03:22:44','2026-01-22 03:22:44'),(37,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/notes/',NULL,'2026-01-22 03:23:25','2026-01-22 03:23:25','2026-01-22 03:23:25'),(38,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/notes/',NULL,'2026-01-22 03:23:32','2026-01-22 03:23:32','2026-01-22 03:23:32'),(39,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/notes/',NULL,'2026-01-22 03:23:40','2026-01-22 03:23:40','2026-01-22 03:23:40'),(40,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/notes/',NULL,'2026-01-22 03:23:46','2026-01-22 03:23:46','2026-01-22 03:23:46'),(41,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/notes/',NULL,'2026-01-22 03:23:53','2026-01-22 03:23:53','2026-01-22 03:23:53'),(42,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/agenda/',NULL,'2026-01-22 03:25:49','2026-01-22 03:25:49','2026-01-22 03:25:49'),(43,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/agenda/',NULL,'2026-01-22 03:25:59','2026-01-22 03:25:59','2026-01-22 03:25:59'),(44,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/agenda/',NULL,'2026-01-22 03:26:06','2026-01-22 03:26:06','2026-01-22 03:26:06'),(45,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/agenda/',NULL,'2026-01-22 03:26:21','2026-01-22 03:26:21','2026-01-22 03:26:21'),(46,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/agenda/',NULL,'2026-01-22 03:26:28','2026-01-22 03:26:28','2026-01-22 03:26:28'),(47,NULL,'127.0.0.1','Thunder Client (https://www.thunderclient.com)','POST','/auth/login',NULL,'2026-01-22 03:27:37','2026-01-22 03:27:37','2026-01-22 03:27:37'),(48,1,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/appointments/',NULL,'2026-01-22 03:27:53','2026-01-22 03:27:53','2026-01-22 03:27:53'),(49,1,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/appointments/',NULL,'2026-01-22 03:28:02','2026-01-22 03:28:02','2026-01-22 03:28:02'),(50,1,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/appointments/',NULL,'2026-01-22 03:28:07','2026-01-22 03:28:07','2026-01-22 03:28:07'),(51,1,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/appointments/',NULL,'2026-01-22 03:28:13','2026-01-22 03:28:13','2026-01-22 03:28:13'),(52,1,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/appointments/',NULL,'2026-01-22 03:28:19','2026-01-22 03:28:19','2026-01-22 03:28:19'),(53,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/consents/',NULL,'2026-01-22 03:29:01','2026-01-22 03:29:01','2026-01-22 03:29:01'),(54,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/consents/',NULL,'2026-01-22 03:29:08','2026-01-22 03:29:08','2026-01-22 03:29:08'),(55,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/consents/',NULL,'2026-01-22 03:31:08','2026-01-22 03:31:08','2026-01-22 03:31:08'),(56,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/consents/',NULL,'2026-01-22 03:32:42','2026-01-22 03:32:42','2026-01-22 03:32:42'),(57,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/consents/',NULL,'2026-01-22 03:33:02','2026-01-22 03:33:02','2026-01-22 03:33:02'),(58,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/diagnoses/',NULL,'2026-01-22 03:33:40','2026-01-22 03:33:40','2026-01-22 03:33:40'),(59,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/diagnoses/',NULL,'2026-01-22 03:33:55','2026-01-22 03:33:55','2026-01-22 03:33:55'),(60,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/diagnoses/',NULL,'2026-01-22 03:34:18','2026-01-22 03:34:18','2026-01-22 03:34:18'),(61,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/diagnoses/',NULL,'2026-01-22 03:34:28','2026-01-22 03:34:28','2026-01-22 03:34:28'),(62,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/diagnoses/',NULL,'2026-01-22 03:34:47','2026-01-22 03:34:47','2026-01-22 03:34:47'),(63,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/apidocs/',NULL,'2026-01-22 03:43:46','2026-01-22 03:43:46','2026-01-22 03:43:46'),(64,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/swagger-ui-bundle.js',NULL,'2026-01-22 03:43:47','2026-01-22 03:43:47','2026-01-22 03:43:47'),(65,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/swagger-ui.css',NULL,'2026-01-22 03:43:47','2026-01-22 03:43:47','2026-01-22 03:43:47'),(66,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/swagger-ui-standalone-preset.js',NULL,'2026-01-22 03:43:47','2026-01-22 03:43:47','2026-01-22 03:43:47'),(67,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/lib/jquery.min.js',NULL,'2026-01-22 03:43:47','2026-01-22 03:43:47','2026-01-22 03:43:47'),(68,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/favicon-32x32.png',NULL,'2026-01-22 03:43:48','2026-01-22 03:43:48','2026-01-22 03:43:48'),(69,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/apispec_1.json',NULL,'2026-01-22 03:43:49','2026-01-22 03:43:49','2026-01-22 03:43:49'),(70,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/insurers/',NULL,'2026-01-22 03:44:02','2026-01-22 03:44:02','2026-01-22 03:44:02'),(71,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/insurers/',NULL,'2026-01-22 03:44:29','2026-01-22 03:44:29','2026-01-22 03:44:29'),(72,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/insurers/',NULL,'2026-01-22 03:44:37','2026-01-22 03:44:37','2026-01-22 03:44:37'),(73,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/insurers/',NULL,'2026-01-22 03:44:42','2026-01-22 03:44:42','2026-01-22 03:44:42'),(74,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/insurers/',NULL,'2026-01-22 03:44:48','2026-01-22 03:44:48','2026-01-22 03:44:48'),(75,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/insurers/',NULL,'2026-01-22 03:44:53','2026-01-22 03:44:53','2026-01-22 03:44:53'),(76,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/prestations/',NULL,'2026-01-22 03:54:57','2026-01-22 03:54:57','2026-01-22 03:54:57'),(77,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/prestations/',NULL,'2026-01-22 03:55:04','2026-01-22 03:55:04','2026-01-22 03:55:04'),(78,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/prestations/',NULL,'2026-01-22 03:55:08','2026-01-22 03:55:08','2026-01-22 03:55:08'),(79,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/prestations/',NULL,'2026-01-22 03:55:13','2026-01-22 03:55:13','2026-01-22 03:55:13'),(80,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/prestations/',NULL,'2026-01-22 03:55:18','2026-01-22 03:55:18','2026-01-22 03:55:18'),(81,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/invoices/',NULL,'2026-01-22 03:55:34','2026-01-22 03:55:34','2026-01-22 03:55:34'),(82,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/invoices/',NULL,'2026-01-22 03:55:41','2026-01-22 03:55:41','2026-01-22 03:55:41'),(83,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/invoices/',NULL,'2026-01-22 03:55:47','2026-01-22 03:55:47','2026-01-22 03:55:47'),(84,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/invoices/',NULL,'2026-01-22 03:55:52','2026-01-22 03:55:52','2026-01-22 03:55:52'),(85,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/invoice_items/',NULL,'2026-01-22 03:56:01','2026-01-22 03:56:01','2026-01-22 03:56:01'),(86,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/episodes/',NULL,'2026-01-22 03:56:31','2026-01-22 03:56:31','2026-01-22 03:56:31'),(87,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/orders/',NULL,'2026-01-22 03:56:53','2026-01-22 03:56:53','2026-01-22 03:56:53'),(88,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/order-details/',NULL,'2026-01-22 03:56:59','2026-01-22 03:56:59','2026-01-22 03:56:59'),(89,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/payments/',NULL,'2026-01-22 03:57:37','2026-01-22 03:57:37','2026-01-22 03:57:37'),(90,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/payments/',NULL,'2026-01-22 03:57:52','2026-01-22 03:57:52','2026-01-22 03:57:52'),(91,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/payments/',NULL,'2026-01-22 03:58:10','2026-01-22 03:58:10','2026-01-22 03:58:10'),(92,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/payments/',NULL,'2026-01-22 03:58:20','2026-01-22 03:58:20','2026-01-22 03:58:20'),(93,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/notifications/',NULL,'2026-01-22 04:02:54','2026-01-22 04:02:54','2026-01-22 04:02:54'),(94,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/notifications/',NULL,'2026-01-22 04:03:23','2026-01-22 04:03:23','2026-01-22 04:03:23'),(95,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/notifications/',NULL,'2026-01-22 04:03:26','2026-01-22 04:03:26','2026-01-22 04:03:26'),(96,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/notifications/',NULL,'2026-01-22 04:03:27','2026-01-22 04:03:27','2026-01-22 04:03:27'),(97,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/episodes/',NULL,'2026-01-22 04:03:46','2026-01-22 04:03:46','2026-01-22 04:03:46'),(98,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/consents/',NULL,'2026-01-22 04:04:04','2026-01-22 04:04:04','2026-01-22 04:04:04'),(99,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/diagnoses/',NULL,'2026-01-22 04:04:13','2026-01-22 04:04:13','2026-01-22 04:04:13'),(100,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/plans/',NULL,'2026-01-22 04:05:53','2026-01-22 04:05:53','2026-01-22 04:05:53'),(101,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/plans/',NULL,'2026-01-22 04:06:12','2026-01-22 04:06:12','2026-01-22 04:06:12'),(102,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/plans/',NULL,'2026-01-22 04:06:18','2026-01-22 04:06:18','2026-01-22 04:06:18'),(103,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/plans/',NULL,'2026-01-22 04:06:25','2026-01-22 04:06:25','2026-01-22 04:06:25'),(104,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/plans/',NULL,'2026-01-22 04:06:31','2026-01-22 04:06:31','2026-01-22 04:06:31'),(105,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/plans/',NULL,'2026-01-22 04:06:37','2026-01-22 04:06:37','2026-01-22 04:06:37'),(106,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/affiliations/',NULL,'2026-01-22 04:08:25','2026-01-22 04:08:25','2026-01-22 04:08:25'),(107,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/affiliations/',NULL,'2026-01-22 04:08:48','2026-01-22 04:08:48','2026-01-22 04:08:48'),(108,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/affiliations/',NULL,'2026-01-22 04:08:54','2026-01-22 04:08:54','2026-01-22 04:08:54'),(109,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/affiliations/',NULL,'2026-01-22 04:08:59','2026-01-22 04:08:59','2026-01-22 04:08:59'),(110,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/affiliations/',NULL,'2026-01-22 04:09:06','2026-01-22 04:09:06','2026-01-22 04:09:06'),(111,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/appointments/',NULL,'2026-01-22 04:09:16','2026-01-22 04:09:16','2026-01-22 04:09:16'),(112,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/authorizations/',NULL,'2026-01-22 04:11:11','2026-01-22 04:11:11','2026-01-22 04:11:11'),(113,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/authorizations/',NULL,'2026-01-22 04:11:21','2026-01-22 04:11:21','2026-01-22 04:11:21'),(114,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/authorizations/',NULL,'2026-01-22 04:11:26','2026-01-22 04:11:26','2026-01-22 04:11:26'),(115,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/authorizations/',NULL,'2026-01-22 04:11:31','2026-01-22 04:11:31','2026-01-22 04:11:31'),(116,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/authorizations/',NULL,'2026-01-22 04:11:36','2026-01-22 04:11:36','2026-01-22 04:11:36'),(117,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/notes/',NULL,'2026-01-22 04:12:36','2026-01-22 04:12:36','2026-01-22 04:12:36'),(118,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/prescriptions/',NULL,'2026-01-22 04:13:01','2026-01-22 04:13:01','2026-01-22 04:13:01'),(119,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/prescriptions/',NULL,'2026-01-22 04:13:36','2026-01-22 04:13:36','2026-01-22 04:13:36'),(120,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/prescriptions/',NULL,'2026-01-22 04:13:47','2026-01-22 04:13:47','2026-01-22 04:13:47'),(121,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/prescriptions/',NULL,'2026-01-22 04:13:57','2026-01-22 04:13:57','2026-01-22 04:13:57'),(122,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/prescriptions/',NULL,'2026-01-22 04:14:07','2026-01-22 04:14:07','2026-01-22 04:14:07'),(123,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/prescriptions/',NULL,'2026-01-22 04:14:16','2026-01-22 04:14:16','2026-01-22 04:14:16'),(124,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/prescription-items/',NULL,'2026-01-22 04:14:22','2026-01-22 04:14:22','2026-01-22 04:14:22'),(125,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/prestations/',NULL,'2026-01-22 04:14:32','2026-01-22 04:14:32','2026-01-22 04:14:32'),(126,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/prestations/',NULL,'2026-01-22 04:14:32','2026-01-22 04:14:32','2026-01-22 04:14:32'),(127,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/results/',NULL,'2026-01-22 04:14:39','2026-01-22 04:14:39','2026-01-22 04:14:39'),(128,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/results/',NULL,'2026-01-22 04:15:05','2026-01-22 04:15:05','2026-01-22 04:15:05'),(129,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/results/',NULL,'2026-01-22 04:15:12','2026-01-22 04:15:12','2026-01-22 04:15:12'),(130,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/results/',NULL,'2026-01-22 04:15:19','2026-01-22 04:15:19','2026-01-22 04:15:19'),(131,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/tariffs/',NULL,'2026-01-22 04:15:27','2026-01-22 04:15:27','2026-01-22 04:15:27'),(132,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/units/',NULL,'2026-01-22 04:15:49','2026-01-22 04:15:49','2026-01-22 04:15:49'),(133,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/tariffs/',NULL,'2026-01-22 04:16:02','2026-01-22 04:16:02','2026-01-22 04:16:02'),(134,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/tariffs/',NULL,'2026-01-22 04:16:08','2026-01-22 04:16:08','2026-01-22 04:16:08'),(135,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/tariffs/',NULL,'2026-01-22 04:16:14','2026-01-22 04:16:14','2026-01-22 04:16:14'),(136,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/tariffs/',NULL,'2026-01-22 04:16:19','2026-01-22 04:16:19','2026-01-22 04:16:19'),(137,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','POST','/tariffs/',NULL,'2026-01-22 04:16:25','2026-01-22 04:16:25','2026-01-22 04:16:25'),(138,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/apidocs/',NULL,'2026-01-22 04:27:42','2026-01-22 04:27:42','2026-01-22 04:27:42'),(139,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/lib/jquery.min.js',NULL,'2026-01-22 04:27:43','2026-01-22 04:27:43','2026-01-22 04:27:43'),(140,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/swagger-ui.css',NULL,'2026-01-22 04:27:43','2026-01-22 04:27:43','2026-01-22 04:27:43'),(141,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/swagger-ui-standalone-preset.js',NULL,'2026-01-22 04:27:43','2026-01-22 04:27:43','2026-01-22 04:27:43'),(142,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/swagger-ui-bundle.js',NULL,'2026-01-22 04:27:43','2026-01-22 04:27:43','2026-01-22 04:27:43'),(143,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/flasgger_static/favicon-32x32.png',NULL,'2026-01-22 04:27:44','2026-01-22 04:27:44','2026-01-22 04:27:44'),(144,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/apispec_1.json',NULL,'2026-01-22 04:27:45','2026-01-22 04:27:45','2026-01-22 04:27:45'),(145,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/affiliations/',NULL,'2026-01-22 04:27:57','2026-01-22 04:27:57','2026-01-22 04:27:57'),(146,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/appointments/',NULL,'2026-01-22 04:30:57','2026-01-22 04:30:57','2026-01-22 04:30:57'),(147,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/agenda/',NULL,'2026-01-22 04:33:08','2026-01-22 04:33:08','2026-01-22 04:33:08'),(148,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/authorizations/',NULL,'2026-01-22 04:35:02','2026-01-22 04:35:02','2026-01-22 04:35:02'),(149,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/consents/',NULL,'2026-01-22 04:36:05','2026-01-22 04:36:05','2026-01-22 04:36:05'),(150,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/credit-debit-notes/',NULL,'2026-01-22 04:36:53','2026-01-22 04:36:53','2026-01-22 04:36:53'),(151,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/diagnoses/',NULL,'2026-01-22 04:38:10','2026-01-22 04:38:10','2026-01-22 04:38:10'),(152,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/episodes/',NULL,'2026-01-22 04:39:18','2026-01-22 04:39:18','2026-01-22 04:39:18'),(153,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/insurers/',NULL,'2026-01-22 04:40:05','2026-01-22 04:40:05','2026-01-22 04:40:05'),(154,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/invoices/',NULL,'2026-01-22 04:40:56','2026-01-22 04:40:56','2026-01-22 04:40:56'),(155,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/notes/',NULL,'2026-01-22 04:42:42','2026-01-22 04:42:42','2026-01-22 04:42:42'),(156,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/orders/',NULL,'2026-01-22 04:44:08','2026-01-22 04:44:08','2026-01-22 04:44:08'),(157,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/payments/',NULL,'2026-01-22 04:45:01','2026-01-22 04:45:01','2026-01-22 04:45:01'),(158,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/people/',NULL,'2026-01-22 04:50:42','2026-01-22 04:50:42','2026-01-22 04:50:42'),(159,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/plans/',NULL,'2026-01-22 04:52:14','2026-01-22 04:52:14','2026-01-22 04:52:14'),(160,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/prescriptions/',NULL,'2026-01-22 04:53:03','2026-01-22 04:53:03','2026-01-22 04:53:03'),(161,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/prestations/',NULL,'2026-01-22 04:54:35','2026-01-22 04:54:35','2026-01-22 04:54:35'),(162,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/results/',NULL,'2026-01-22 04:56:11','2026-01-22 04:56:11','2026-01-22 04:56:11'),(163,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/tariffs/',NULL,'2026-01-22 04:57:17','2026-01-22 04:57:17','2026-01-22 04:57:17'),(164,NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','GET','/units/',NULL,'2026-01-22 04:58:16','2026-01-22 04:58:16','2026-01-22 04:58:16');
/*!40000 ALTER TABLE `access_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `affiliations`
--

DROP TABLE IF EXISTS `affiliations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `affiliations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `payer_id` int(11) NOT NULL,
  `plan_id` int(11) NOT NULL,
  `policy_number` varchar(50) NOT NULL,
  `card_number` varchar(100) NOT NULL,
  `valid_from` date DEFAULT NULL,
  `valid_to` date DEFAULT NULL,
  `copayment` decimal(10,2) NOT NULL DEFAULT 0.00,
  `coinsurance` decimal(10,2) NOT NULL DEFAULT 0.00,
  `status` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_aff_person` (`person_id`),
  KEY `fk_aff_payer` (`payer_id`),
  KEY `fk_aff_plan` (`plan_id`),
  CONSTRAINT `fk_aff_payer` FOREIGN KEY (`payer_id`) REFERENCES `payers` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_aff_person` FOREIGN KEY (`person_id`) REFERENCES `people` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_aff_plan` FOREIGN KEY (`plan_id`) REFERENCES `plans` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `affiliations`
--

LOCK TABLES `affiliations` WRITE;
/*!40000 ALTER TABLE `affiliations` DISABLE KEYS */;
INSERT INTO `affiliations` VALUES (1,1,1,2,'POL-789456','CARD-123456','2024-01-01','2024-12-31',10.00,5.00,1,'2026-01-22 04:08:25','2026-01-22 04:08:25'),(2,2,2,3,'POL-456123','CARD-654321','2024-02-01','2024-12-31',15.00,8.00,1,'2026-01-22 04:08:48','2026-01-22 04:08:48'),(3,3,3,1,'POL-123789','CARD-987654','2024-03-01','2024-12-31',20.00,10.00,1,'2026-01-22 04:08:54','2026-01-22 04:08:54'),(4,4,4,4,'POL-321654','CARD-321987','2024-04-01','2024-12-31',12.00,7.00,1,'2026-01-22 04:08:59','2026-01-22 04:08:59'),(5,5,5,5,'POL-654987','CARD-456789','2024-05-01','2024-12-31',10.00,6.00,1,'2026-01-22 04:09:06','2026-01-22 04:09:06');
/*!40000 ALTER TABLE `affiliations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `agenda_blocks`
--

DROP TABLE IF EXISTS `agenda_blocks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agenda_blocks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `professional_id` int(11) NOT NULL,
  `unit_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `state` enum('AVAILABLE','BLOCKED','OCCUPIED') DEFAULT 'AVAILABLE',
  `type` enum('CONSULTATION','PROCEDURE','INTERCONSULTATION') DEFAULT 'CONSULTATION',
  `capacity` int(11) DEFAULT 1,
  `notes` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_agenda_unit` (`unit_id`),
  KEY `idx_agenda_prof_date` (`professional_id`,`date`),
  CONSTRAINT `fk_agenda_prof` FOREIGN KEY (`professional_id`) REFERENCES `professionals` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_agenda_unit` FOREIGN KEY (`unit_id`) REFERENCES `units` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agenda_blocks`
--

LOCK TABLES `agenda_blocks` WRITE;
/*!40000 ALTER TABLE `agenda_blocks` DISABLE KEYS */;
INSERT INTO `agenda_blocks` VALUES (1,1,1,'2026-01-25','09:00:00','10:00:00','AVAILABLE','CONSULTATION',1,'Consulta de control para Luis Daza','2026-01-22 03:25:49','2026-01-22 03:25:49'),(2,1,1,'2026-01-25','10:30:00','11:30:00','AVAILABLE','CONSULTATION',1,'Segunda consulta de control para Luis Daza','2026-01-22 03:25:58','2026-01-22 03:25:58'),(3,2,2,'2026-01-26','08:00:00','09:00:00','AVAILABLE','CONSULTATION',1,'Consulta de control para María Gómez','2026-01-22 03:26:06','2026-01-22 03:26:06'),(4,3,3,'2026-01-26','09:30:00','10:30:00','AVAILABLE','CONSULTATION',1,'Consulta de seguimiento para Juan Pérez','2026-01-22 03:26:20','2026-01-22 03:26:20'),(5,4,4,'2026-01-27','11:00:00','12:00:00','AVAILABLE','CONSULTATION',1,'Consulta de control para Ana Rodríguez','2026-01-22 03:26:28','2026-01-22 03:26:28');
/*!40000 ALTER TABLE `agenda_blocks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointment_history`
--

DROP TABLE IF EXISTS `appointment_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appointment_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `appointment_id` int(11) NOT NULL,
  `old_state` varchar(20) DEFAULT NULL,
  `new_state` varchar(20) DEFAULT NULL,
  `changed_at` datetime DEFAULT current_timestamp(),
  `changed_by` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `appointment_id` (`appointment_id`),
  CONSTRAINT `appointment_history_ibfk_1` FOREIGN KEY (`appointment_id`) REFERENCES `appointments` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment_history`
--

LOCK TABLES `appointment_history` WRITE;
/*!40000 ALTER TABLE `appointment_history` DISABLE KEYS */;
INSERT INTO `appointment_history` VALUES (1,1,NULL,'SOLICITADA','2026-01-22 03:27:53',1),(2,2,NULL,'SOLICITADA','2026-01-22 03:28:02',1),(3,3,NULL,'SOLICITADA','2026-01-22 03:28:07',1),(4,4,NULL,'SOLICITADA','2026-01-22 03:28:12',1),(5,5,NULL,'SOLICITADA','2026-01-22 03:28:19',1);
/*!40000 ALTER TABLE `appointment_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appointments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `professional_id` int(11) NOT NULL,
  `unit_id` int(11) NOT NULL,
  `start` datetime NOT NULL,
  `end` datetime NOT NULL,
  `duration_minutes` int(11) DEFAULT NULL,
  `motivo` text NOT NULL,
  `canal` enum('PRESENCIAL','VIRTUAL') NOT NULL,
  `observations` text DEFAULT NULL,
  `status` enum('SOLICITADA','CONFIRMADA','CUMPLIDA','CANCELADA','NO_ASISTIDA') NOT NULL DEFAULT 'SOLICITADA',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_appointments_professional` (`professional_id`),
  KEY `fk_appointments_unit` (`unit_id`),
  KEY `fk_appointments_person_id` (`person_id`),
  CONSTRAINT `fk_appointments_person_id` FOREIGN KEY (`person_id`) REFERENCES `people` (`id`),
  CONSTRAINT `fk_appointments_professional` FOREIGN KEY (`professional_id`) REFERENCES `professionals` (`id`),
  CONSTRAINT `fk_appointments_unit` FOREIGN KEY (`unit_id`) REFERENCES `units` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES (1,1,1,1,'2026-01-25 09:00:00','2026-01-25 10:00:00',60,'Consulta general','PRESENCIAL','Paciente solicita ser atendido temprano','SOLICITADA','2026-01-22 03:27:52','2026-01-22 03:27:52'),(2,1,1,1,'2026-01-25 10:30:00','2026-01-25 11:30:00',60,'Consulta de seguimiento','PRESENCIAL','Paciente sigue con síntomas leves','SOLICITADA','2026-01-22 03:28:01','2026-01-22 03:28:01'),(3,2,2,2,'2026-01-26 08:00:00','2026-01-26 08:45:00',45,'Consulta pediátrica','VIRTUAL','Padres solicitan revisión de crecimiento','SOLICITADA','2026-01-22 03:28:07','2026-01-22 03:28:07'),(4,3,3,3,'2026-01-26 09:30:00','2026-01-26 10:00:00',30,'Control de presión arterial','PRESENCIAL','Paciente con historial de hipertensión','SOLICITADA','2026-01-22 03:28:12','2026-01-22 03:28:12'),(5,4,4,4,'2026-01-27 11:00:00','2026-01-27 12:00:00',60,'Revisión dermatológica','PRESENCIAL','Paciente presenta sarpullido en brazos','SOLICITADA','2026-01-22 03:28:19','2026-01-22 03:28:19');
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authorizations`
--

DROP TABLE IF EXISTS `authorizations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authorizations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `procedure_code` varchar(50) DEFAULT NULL,
  `plan_id` int(11) NOT NULL,
  `status` enum('REQUESTED','APPROVED','DENIED') NOT NULL DEFAULT 'REQUESTED',
  `request_date` datetime NOT NULL DEFAULT current_timestamp(),
  `response_date` datetime DEFAULT NULL,
  `authorization_number` varchar(100) DEFAULT NULL,
  `observations` text DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `idx_authorizations_order` (`order_id`),
  KEY `idx_authorizations_plan` (`plan_id`),
  CONSTRAINT `fk_authorizations_order` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_authorizations_plan` FOREIGN KEY (`plan_id`) REFERENCES `plans` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authorizations`
--

LOCK TABLES `authorizations` WRITE;
/*!40000 ALTER TABLE `authorizations` DISABLE KEYS */;
INSERT INTO `authorizations` VALUES (1,1,'PROC123',2,'REQUESTED','2026-01-22 04:11:11','2026-01-05 15:00:00','AUTH-12345','Initial request for procedure','2026-01-22 04:11:11','2026-01-22 04:11:11'),(2,2,'PROC124',3,'APPROVED','2026-01-22 04:11:21','2026-01-06 10:30:00','AUTH-12346','Follow-up request for lab test','2026-01-22 04:11:21','2026-01-22 04:11:21'),(3,3,'PROC125',1,'REQUESTED','2026-01-22 04:11:26','2026-01-07 14:00:00','AUTH-12347','Request for imaging study','2026-01-22 04:11:26','2026-01-22 04:11:26'),(4,4,'PROC126',4,'DENIED','2026-01-22 04:11:31','2026-01-08 09:45:00','AUTH-12348','Request for surgical procedure','2026-01-22 04:11:31','2026-01-22 04:11:31'),(5,5,'PROC127',5,'APPROVED','2026-01-22 04:11:36','2026-01-09 11:15:00','AUTH-12349','Request for specialist consultation','2026-01-22 04:11:36','2026-01-22 04:11:36');
/*!40000 ALTER TABLE `authorizations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clinical_notes`
--

DROP TABLE IF EXISTS `clinical_notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clinical_notes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `episode_id` int(11) NOT NULL,
  `professional_id` int(11) DEFAULT NULL,
  `subjective` text DEFAULT NULL,
  `objective` text DEFAULT NULL,
  `assessment` text DEFAULT NULL,
  `plan` text DEFAULT NULL,
  `attachments` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`attachments`)),
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_note_episode` (`episode_id`),
  KEY `fk_note_prof` (`professional_id`),
  CONSTRAINT `fk_note_episode` FOREIGN KEY (`episode_id`) REFERENCES `episodes` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_note_prof` FOREIGN KEY (`professional_id`) REFERENCES `professionals` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clinical_notes`
--

LOCK TABLES `clinical_notes` WRITE;
/*!40000 ALTER TABLE `clinical_notes` DISABLE KEYS */;
INSERT INTO `clinical_notes` VALUES (1,1,1,'Patient reports abdominal pain for 3 days','BP 120/80, HR 78, tenderness in lower right quadrant','Suspected appendicitis','Request abdominal ultrasound and lab tests','[\"file1.pdf\", \"image1.png\"]','2026-01-22 03:23:24','2026-01-22 03:23:24'),(2,2,4,'Patient reports vomiting and diarrhea for 2 days','BP 110/70, HR 90, dry mucous membranes','Mild dehydration','Administer IV fluids and monitor electrolytes','[\"file2.pdf\"]','2026-01-22 03:23:31','2026-01-22 03:23:31'),(3,3,3,'Patient reports feeling well, no complaints','Weight and height within normal range, vitals stable','Routine pediatric check-up, no abnormalities','Continue regular diet and vaccinations','[]','2026-01-22 03:23:40','2026-01-22 03:23:40'),(4,4,2,'Patient reports itchy rash after eating peanuts','Mild rash on arms, vitals normal','Allergic reaction, mild','Administer antihistamines and monitor','[\"image2.png\"]','2026-01-22 03:23:46','2026-01-22 03:23:46'),(5,5,5,'Patient reports mild pain during movement','Sutures intact, minimal swelling, ROM improving','Post-surgery follow-up, knee replacement','Continue physiotherapy, schedule next follow-up in 2 weeks','[\"file3.pdf\", \"image3.png\"]','2026-01-22 03:23:52','2026-01-22 03:23:52');
/*!40000 ALTER TABLE `clinical_notes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clinical_versions`
--

DROP TABLE IF EXISTS `clinical_versions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clinical_versions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entity_type` varchar(100) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `content_snapshot` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`content_snapshot`)),
  `version_number` int(11) NOT NULL DEFAULT 1,
  `user_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_clinical_versions_user` (`user_id`),
  CONSTRAINT `fk_clinical_versions_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clinical_versions`
--

LOCK TABLES `clinical_versions` WRITE;
/*!40000 ALTER TABLE `clinical_versions` DISABLE KEYS */;
/*!40000 ALTER TABLE `clinical_versions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consents`
--

DROP TABLE IF EXISTS `consents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `consents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `process_type` varchar(50) NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `method` enum('DIGITAL_SIGNATURE','VERBAL_WITH_RECORD') NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `file_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_person` (`person_id`),
  CONSTRAINT `fk_person` FOREIGN KEY (`person_id`) REFERENCES `people` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consents`
--

LOCK TABLES `consents` WRITE;
/*!40000 ALTER TABLE `consents` DISABLE KEYS */;
INSERT INTO `consents` VALUES (1,1,'data_processing','2026-01-22 03:29:01','DIGITAL_SIGNATURE','2026-01-22 03:29:01','2026-01-21 23:32:18','FILE001'),(2,2,'medical_treatment','2026-01-22 03:29:08','DIGITAL_SIGNATURE','2026-01-22 03:29:08','2026-01-21 23:32:18','file002'),(3,3,'data_processing','2026-01-22 03:31:08','VERBAL_WITH_RECORD','2026-01-22 03:31:08','2026-01-22 03:31:08',NULL),(4,4,'medical_treatment','2026-01-22 03:32:42','DIGITAL_SIGNATURE','2026-01-22 03:32:42','2026-01-22 03:32:42','file_20260122033242_4.pdf'),(5,5,'research_participation','2026-01-22 03:33:02','VERBAL_WITH_RECORD','2026-01-22 03:33:02','2026-01-22 03:33:02',NULL);
/*!40000 ALTER TABLE `consents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credit_debit_notes`
--

DROP TABLE IF EXISTS `credit_debit_notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credit_debit_notes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `factura_id` int(11) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_credit_debit_invoice` (`factura_id`),
  CONSTRAINT `fk_credit_debit_invoice` FOREIGN KEY (`factura_id`) REFERENCES `invoices` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_debit_notes`
--

LOCK TABLES `credit_debit_notes` WRITE;
/*!40000 ALTER TABLE `credit_debit_notes` DISABLE KEYS */;
/*!40000 ALTER TABLE `credit_debit_notes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagnoses`
--

DROP TABLE IF EXISTS `diagnoses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diagnoses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `episode_id` int(11) NOT NULL,
  `code` varchar(20) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `type_diagnoses` enum('PRESUMPTIVE','DEFINITIVE') NOT NULL,
  `main` tinyint(1) DEFAULT 0,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_episode` (`episode_id`),
  CONSTRAINT `fk_episode` FOREIGN KEY (`episode_id`) REFERENCES `episodes` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnoses`
--

LOCK TABLES `diagnoses` WRITE;
/*!40000 ALTER TABLE `diagnoses` DISABLE KEYS */;
INSERT INTO `diagnoses` VALUES (1,1,'J45.9','Asthma, unspecified','PRESUMPTIVE',1,'2026-01-22 03:33:40','2026-01-22 03:33:40'),(2,2,'I10','Essential (primary) hypertension','DEFINITIVE',1,'2026-01-22 03:33:54','2026-01-22 03:33:54'),(3,3,'Z00.00','General adult medical examination','PRESUMPTIVE',1,'2026-01-22 03:34:18','2026-01-22 03:34:18'),(4,4,'L27.0','Generalized skin rash due to food','PRESUMPTIVE',1,'2026-01-22 03:34:28','2026-01-22 03:34:28'),(5,5,'Z48.81','Encounter for surgical aftercare following surgery on the musculoskeletal system','DEFINITIVE',1,'2026-01-22 03:34:47','2026-01-22 03:34:47');
/*!40000 ALTER TABLE `diagnoses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `episodes`
--

DROP TABLE IF EXISTS `episodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `episodes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `professional_id` int(11) DEFAULT NULL,
  `unit_id` int(11) DEFAULT NULL,
  `motivo` varchar(255) DEFAULT NULL,
  `type_episode` enum('CONSULTATION','PROCEDURE','CONTROL','AMBULATORY_EMERGENCY') NOT NULL,
  `started_at` datetime DEFAULT current_timestamp(),
  `closed_at` datetime DEFAULT NULL,
  `status` enum('OPEN','CLOSED') NOT NULL DEFAULT 'OPEN',
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_episode_prof` (`professional_id`),
  KEY `fk_episode_unit` (`unit_id`),
  KEY `idx_episodes_person` (`person_id`),
  CONSTRAINT `fk_episode_person` FOREIGN KEY (`person_id`) REFERENCES `people` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_episode_prof` FOREIGN KEY (`professional_id`) REFERENCES `professionals` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_episode_unit` FOREIGN KEY (`unit_id`) REFERENCES `units` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `episodes`
--

LOCK TABLES `episodes` WRITE;
/*!40000 ALTER TABLE `episodes` DISABLE KEYS */;
INSERT INTO `episodes` VALUES (1,1,1,3,'Patient presents with abdominal pain','CONSULTATION','2026-01-22 03:20:08',NULL,'OPEN','2026-01-22 03:20:08','2026-01-22 03:20:08'),(2,2,4,2,'Follow-up for hypertension management','CONSULTATION','2026-01-22 03:20:15',NULL,'OPEN','2026-01-22 03:20:15','2026-01-22 03:20:15'),(3,3,3,1,'Routine pediatric check-up','CONSULTATION','2026-01-22 03:20:23',NULL,'OPEN','2026-01-22 03:20:23','2026-01-22 03:20:23'),(4,4,2,5,'Patient presents with skin rash and itching','CONSULTATION','2026-01-22 03:20:28',NULL,'OPEN','2026-01-22 03:20:28','2026-01-22 03:20:28'),(5,5,5,4,'Post-surgery follow-up for knee replacement','CONSULTATION','2026-01-22 03:20:34',NULL,'OPEN','2026-01-22 03:20:34','2026-01-22 03:20:34');
/*!40000 ALTER TABLE `episodes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insurers`
--

DROP TABLE IF EXISTS `insurers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `insurers` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `tax_id` varchar(50) NOT NULL,
  `contact` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `tax_id` (`tax_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insurers`
--

LOCK TABLES `insurers` WRITE;
/*!40000 ALTER TABLE `insurers` DISABLE KEYS */;
INSERT INTO `insurers` VALUES (1,'Seguros La Vida','J123456789','+584123456789',1,'2026-01-22 07:44:29','2026-01-22 07:44:29'),(2,'Salud Total','J987654321','+584129876543',1,'2026-01-22 07:44:36','2026-01-22 07:44:36'),(3,'Protección Médica','J456789123','+584126789012',1,'2026-01-22 07:44:42','2026-01-22 07:44:42'),(4,'Vida y Salud','J321654987','+584127654321',1,'2026-01-22 07:44:47','2026-01-22 07:44:47'),(5,'Salud Integral','J654987321','+584128765432',1,'2026-01-22 07:44:53','2026-01-22 07:44:53');
/*!40000 ALTER TABLE `insurers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice_items`
--

DROP TABLE IF EXISTS `invoice_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invoice_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `invoice_id` int(11) NOT NULL,
  `prestation_id` int(11) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `quantity` decimal(10,2) NOT NULL,
  `unit_price` decimal(12,2) DEFAULT 0.00,
  `total_price` decimal(12,2) NOT NULL,
  `tax_amount` decimal(12,2) NOT NULL DEFAULT 0.00,
  PRIMARY KEY (`id`),
  KEY `fk_item_prestation` (`prestation_id`),
  KEY `idx_invoice_items_invoice` (`invoice_id`),
  CONSTRAINT `fk_item_invoice` FOREIGN KEY (`invoice_id`) REFERENCES `invoices` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_item_prestation` FOREIGN KEY (`prestation_id`) REFERENCES `prestations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice_items`
--

LOCK TABLES `invoice_items` WRITE;
/*!40000 ALTER TABLE `invoice_items` DISABLE KEYS */;
INSERT INTO `invoice_items` VALUES (1,2,1,'Consulta médica general',1.00,50.00,55.00,5.00),(2,3,2,'Examen de laboratorio',1.00,30.00,40.00,10.00),(3,4,3,'Consulta pediátrica',1.00,40.00,45.00,5.00),(4,5,4,'Consulta dermatológica',1.00,45.00,50.00,5.00);
/*!40000 ALTER TABLE `invoice_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoices`
--

DROP TABLE IF EXISTS `invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invoices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) DEFAULT NULL,
  `total` decimal(12,2) DEFAULT 0.00,
  `status` enum('PENDING','ISSUED','PAID','CANCELLED') NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `invoice_number` varchar(50) NOT NULL,
  `issue_date` date NOT NULL,
  `currency` char(3) NOT NULL DEFAULT 'USD',
  `insurer_id` int(10) unsigned DEFAULT NULL,
  `subtotal` decimal(12,2) NOT NULL DEFAULT 0.00,
  PRIMARY KEY (`id`),
  KEY `fk_invoice_patient` (`patient_id`),
  KEY `fk_invoices_insurer` (`insurer_id`),
  CONSTRAINT `fk_invoice_patient` FOREIGN KEY (`patient_id`) REFERENCES `people` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_invoices_insurer` FOREIGN KEY (`insurer_id`) REFERENCES `insurers` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoices`
--

LOCK TABLES `invoices` WRITE;
/*!40000 ALTER TABLE `invoices` DISABLE KEYS */;
INSERT INTO `invoices` VALUES (2,1,55.00,'PENDING','2026-01-21 23:55:33','2026-01-21 23:55:33','FAC-000101','2026-01-10','USD',NULL,50.00),(3,NULL,40.00,'PENDING','2026-01-21 23:55:40','2026-01-21 23:55:41','FAC-000102','2026-01-11','USD',2,30.00),(4,3,45.00,'PENDING','2026-01-21 23:55:47','2026-01-21 23:55:47','FAC-000103','2026-01-12','USD',NULL,40.00),(5,NULL,50.00,'PENDING','2026-01-21 23:55:52','2026-01-21 23:55:52','FAC-000104','2026-01-13','USD',4,45.00);
/*!40000 ALTER TABLE `invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification_logs`
--

DROP TABLE IF EXISTS `notification_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notification_logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `notification_id` int(11) NOT NULL,
  `status` enum('SENT','ERROR','RETRY') DEFAULT 'SENT',
  `detail` text DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_notif_log` (`notification_id`),
  CONSTRAINT `fk_notif_log` FOREIGN KEY (`notification_id`) REFERENCES `notifications` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification_logs`
--

LOCK TABLES `notification_logs` WRITE;
/*!40000 ALTER TABLE `notification_logs` DISABLE KEYS */;
/*!40000 ALTER TABLE `notification_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notifications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recipient` varchar(255) NOT NULL,
  `payload` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`payload`)),
  `type` varchar(50) NOT NULL,
  `template` varchar(100) NOT NULL,
  `status` enum('PENDING','SENT','FAILED','RETRYING') NOT NULL DEFAULT 'PENDING',
  `timestamp` datetime DEFAULT current_timestamp(),
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
INSERT INTO `notifications` VALUES (1,'john.doe@example.com','{\"name\": \"John\"}','EMAIL','welcome_email','FAILED','2026-01-22 04:02:54','2026-01-22 04:02:53','2026-01-22 04:02:54'),(2,'maria.gomez@example.com','{\"name\": \"Maria\"}','EMAIL','appointment_reminder','FAILED','2026-01-22 04:03:26','2026-01-22 04:03:01','2026-01-22 04:03:26'),(3,'maria.gomez@example.com','{\"name\": \"Maria\"}','EMAIL','appointment_reminder','FAILED','2026-01-22 04:03:23','2026-01-22 04:03:22','2026-01-22 04:03:23'),(4,'luis.daza@example.com','{\"name\": \"Luis\", \"appointment_date\": \"2026-01-25\"}','EMAIL','appointment_reminder','FAILED','2026-01-22 04:03:27','2026-01-22 04:03:26','2026-01-22 04:03:27');
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_details`
--

DROP TABLE IF EXISTS `order_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `code` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `indications` text DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_order_details_order` (`order_id`),
  CONSTRAINT `fk_order_details_order` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_details`
--

LOCK TABLES `order_details` WRITE;
/*!40000 ALTER TABLE `order_details` DISABLE KEYS */;
INSERT INTO `order_details` VALUES (1,1,'LAB001','Complete Blood Count','Fasting required','2026-01-22 03:21:46','2026-01-22 03:21:46'),(2,2,'LAB002','Basic Metabolic Panel','No fasting required','2026-01-22 03:22:19','2026-01-22 03:22:19'),(3,3,'LAB003','Lipid Profile','Fasting required','2026-01-22 03:22:27','2026-01-22 03:22:27'),(4,4,'LAB004','Liver Function Test','No fasting required','2026-01-22 03:22:35','2026-01-22 03:22:35'),(5,5,'LAB005','Urinalysis','Morning sample preferred','2026-01-22 03:22:43','2026-01-22 03:22:43');
/*!40000 ALTER TABLE `order_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `episode_id` int(11) NOT NULL,
  `professional_id` int(11) DEFAULT NULL,
  `type` enum('LABORATORY','IMAGING','PROCEDURE','MEDICATION','OTHER') DEFAULT 'LABORATORY',
  `priority` enum('normal','urgent') NOT NULL DEFAULT 'normal',
  `status` enum('issued','authorized','in_progress','completed','canceled') NOT NULL DEFAULT 'issued',
  `requires_authorization` tinyint(1) DEFAULT 0,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_order_prof` (`professional_id`),
  KEY `idx_orders_episode` (`episode_id`),
  CONSTRAINT `fk_order_episode` FOREIGN KEY (`episode_id`) REFERENCES `episodes` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_order_prof` FOREIGN KEY (`professional_id`) REFERENCES `professionals` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,1,'LABORATORY','normal','issued',0,'2026-01-22 03:21:46','2026-01-22 03:21:46'),(2,2,4,'LABORATORY','urgent','issued',1,'2026-01-22 03:22:19','2026-01-22 03:22:19'),(3,3,3,'LABORATORY','normal','issued',0,'2026-01-22 03:22:27','2026-01-22 03:22:27'),(4,4,2,'LABORATORY','urgent','issued',1,'2026-01-22 03:22:35','2026-01-22 03:22:35'),(5,5,5,'LABORATORY','normal','issued',0,'2026-01-22 03:22:43','2026-01-22 03:22:43');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payers`
--

DROP TABLE IF EXISTS `payers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `tax_id` varchar(100) DEFAULT NULL,
  `contact_email` varchar(255) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payers`
--

LOCK TABLES `payers` WRITE;
/*!40000 ALTER TABLE `payers` DISABLE KEYS */;
INSERT INTO `payers` VALUES (1,'Juan Pérez','J123456789','juan.perez@example.com','+584121234567','2026-01-22 00:08:09'),(2,'María López','J987654321','maria.lopez@example.com','+584129876543','2026-01-22 00:08:09'),(3,'Seguros La Vida','J112233445','contacto@seguroslavida.com','+584123456780','2026-01-22 00:08:09'),(4,'Inversiones XYZ','J556677889','info@inversionesxyz.com','+584123450987','2026-01-22 00:08:09'),(5,'Carlos Gómez','V12345678','carlos.gomez@example.com','+584126789012','2026-01-22 00:08:09');
/*!40000 ALTER TABLE `payers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `invoice_id` int(11) NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `payment_method` enum('CASH','CARD','TRANSFER') DEFAULT 'CASH',
  `reference` varchar(255) DEFAULT NULL,
  `paid_at` datetime DEFAULT current_timestamp(),
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `idx_payments_invoice` (`invoice_id`),
  CONSTRAINT `fk_payment_invoice` FOREIGN KEY (`invoice_id`) REFERENCES `invoices` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_payments_invoice` FOREIGN KEY (`invoice_id`) REFERENCES `invoices` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,2,150.50,'CARD','TRX123456789','2026-01-06 14:30:00','2026-01-22 03:57:37','2026-01-22 03:57:37'),(2,2,75.00,'CASH','TRX987654321','2026-01-07 10:00:00','2026-01-22 03:57:51','2026-01-22 03:57:51'),(3,4,200.00,'TRANSFER','TRX321654987','2026-01-09 11:45:00','2026-01-22 03:58:10','2026-01-22 03:58:10'),(4,5,50.00,'CASH','TRX654987321','2026-01-10 15:20:00','2026-01-22 03:58:20','2026-01-22 03:58:20');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_number` varchar(50) DEFAULT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `gender` enum('M','F','OTHER') DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `active` tinyint(1) DEFAULT 1,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `emergency_contact` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people`
--

LOCK TABLES `people` WRITE;
/*!40000 ALTER TABLE `people` DISABLE KEYS */;
INSERT INTO `people` VALUES (1,'V30485744','Luis','Daza','M','2004-09-23','ldaza2394@gmail.com','+584126702309','Quíbor, Venezuela',1,'2026-01-22 03:03:23','2026-01-22 03:03:23','+584120551810'),(2,'V30123456','María','Gómez','F','2003-05-14','maria.gomez@gmail.com','+584129876543','Barquisimeto, Venezuela',1,'2026-01-22 03:15:16','2026-01-22 03:15:16','+584121234567'),(3,'V30567890','Juan','Pérez','M','2005-11-02','juan.perez@gmail.com','+584128765432','Valencia, Venezuela',1,'2026-01-22 03:15:37','2026-01-22 03:15:37','+584121112233'),(4,'V30234567','Ana','Rodríguez','F','2002-07-19','ana.rodriguez@gmail.com','+584127654321','Caracas, Venezuela',1,'2026-01-22 03:15:52','2026-01-22 03:15:52','+584123334455'),(5,'V30456789','Carlos','Martínez','M','2004-03-28','carlos.martinez@gmail.com','+584123456789','Maracay, Venezuela',1,'2026-01-22 03:16:01','2026-01-22 03:16:01','+584126789012');
/*!40000 ALTER TABLE `people` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions`
--

DROP TABLE IF EXISTS `permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions`
--

LOCK TABLES `permissions` WRITE;
/*!40000 ALTER TABLE `permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plan_tariffs`
--

DROP TABLE IF EXISTS `plan_tariffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plan_tariffs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plan_id` int(11) DEFAULT NULL,
  `prestation_code` varchar(20) NOT NULL,
  `price` decimal(12,2) NOT NULL,
  `valid_from` date DEFAULT NULL,
  `valid_until` date DEFAULT NULL,
  `taxes` decimal(10,2) NOT NULL DEFAULT 0.00,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_tariff_plan` (`plan_id`),
  CONSTRAINT `fk_tariff_plan` FOREIGN KEY (`plan_id`) REFERENCES `plans` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan_tariffs`
--

LOCK TABLES `plan_tariffs` WRITE;
/*!40000 ALTER TABLE `plan_tariffs` DISABLE KEYS */;
INSERT INTO `plan_tariffs` VALUES (1,1,'SRV001',150.00,'2026-01-08','2026-12-31',15.00,'2026-01-22 04:16:02','2026-01-22 04:16:02'),(2,2,'SRV002',200.00,'2026-02-01','2026-12-31',20.00,'2026-01-22 04:16:07','2026-01-22 04:16:07'),(3,3,'SRV003',120.00,'2026-03-01','2026-12-31',12.00,'2026-01-22 04:16:13','2026-01-22 04:16:13'),(4,4,'SRV004',180.00,'2026-04-01','2026-12-31',18.00,'2026-01-22 04:16:19','2026-01-22 04:16:19'),(5,5,'SRV005',250.00,'2026-05-01','2026-12-31',25.00,'2026-01-22 04:16:25','2026-01-22 04:16:25');
/*!40000 ALTER TABLE `plan_tariffs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plans`
--

DROP TABLE IF EXISTS `plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plans` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `insurer_id` int(10) unsigned DEFAULT NULL,
  `name` varchar(200) NOT NULL,
  `general_conditions` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `insurer_idx` (`insurer_id`),
  KEY `idx_insurer_id` (`insurer_id`),
  CONSTRAINT `fk_plan_insurer` FOREIGN KEY (`insurer_id`) REFERENCES `insurers` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plans`
--

LOCK TABLES `plans` WRITE;
/*!40000 ALTER TABLE `plans` DISABLE KEYS */;
INSERT INTO `plans` VALUES (1,3,'Basic Plan','Covers general consultations','2026-01-22 04:06:12','2026-01-22 04:06:12'),(2,2,'Standard Plan','Covers consultations and lab tests','2026-01-22 04:06:18','2026-01-22 04:06:18'),(3,3,'Premium Plan','Covers consultations, lab tests, and specialist visits','2026-01-22 04:06:25','2026-01-22 04:06:25'),(4,4,'Comprehensive Plan','Covers all consultations, lab tests, and surgical procedures','2026-01-22 04:06:31','2026-01-22 04:06:31'),(5,5,'Emergency Plan','Covers emergency care and general consultations','2026-01-22 04:06:36','2026-01-22 04:06:36');
/*!40000 ALTER TABLE `plans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prescription_items`
--

DROP TABLE IF EXISTS `prescription_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prescription_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `prescription_id` int(11) NOT NULL,
  `medicine_code` varchar(50) NOT NULL,
  `name` varchar(200) NOT NULL,
  `dosage` varchar(50) DEFAULT NULL,
  `route` varchar(50) DEFAULT NULL,
  `frequency` varchar(50) DEFAULT NULL,
  `duration` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_prescription` (`prescription_id`),
  CONSTRAINT `fk_prescription` FOREIGN KEY (`prescription_id`) REFERENCES `prescriptions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prescription_items`
--

LOCK TABLES `prescription_items` WRITE;
/*!40000 ALTER TABLE `prescription_items` DISABLE KEYS */;
INSERT INTO `prescription_items` VALUES (1,1,'MED123','Paracetamol','500mg','oral','TID','5 days','2026-01-22 04:13:36','2026-01-22 04:13:36'),(2,2,'MED124','Amoxicillin','250mg','oral','BID','7 days','2026-01-22 04:13:47','2026-01-22 04:13:47'),(3,3,'MED125','Loratadine','10mg','oral','QD','3 days','2026-01-22 04:13:57','2026-01-22 04:13:57'),(4,4,'MED126','Omeprazole','20mg','oral','BID','5 days','2026-01-22 04:14:07','2026-01-22 04:14:07'),(5,5,'MED127','Ibuprofen','100mg','oral','TID','10 days','2026-01-22 04:14:16','2026-01-22 04:14:16');
/*!40000 ALTER TABLE `prescription_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prescriptions`
--

DROP TABLE IF EXISTS `prescriptions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prescriptions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `episode_id` int(11) NOT NULL,
  `observations` text DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `episode_id` (`episode_id`),
  CONSTRAINT `prescriptions_ibfk_1` FOREIGN KEY (`episode_id`) REFERENCES `episodes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prescriptions`
--

LOCK TABLES `prescriptions` WRITE;
/*!40000 ALTER TABLE `prescriptions` DISABLE KEYS */;
INSERT INTO `prescriptions` VALUES (1,1,'Take after meals','2026-01-22 04:13:36','2026-01-22 04:13:36'),(2,2,'Take with water','2026-01-22 04:13:47','2026-01-22 04:13:47'),(3,3,'Take in the morning','2026-01-22 04:13:57','2026-01-22 04:13:57'),(4,4,'Take before meals','2026-01-22 04:14:07','2026-01-22 04:14:07'),(5,5,'Take after meals','2026-01-22 04:14:16','2026-01-22 04:14:16');
/*!40000 ALTER TABLE `prescriptions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestations`
--

DROP TABLE IF EXISTS `prestations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prestations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(100) NOT NULL,
  `name` varchar(200) NOT NULL,
  `group_name` varchar(100) DEFAULT NULL,
  `requirements` varchar(255) DEFAULT NULL,
  `estimated_time` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `active` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestations`
--

LOCK TABLES `prestations` WRITE;
/*!40000 ALTER TABLE `prestations` DISABLE KEYS */;
INSERT INTO `prestations` VALUES (1,'LAB001','Blood Test','Laboratory','Fasting 8 hours',30,'2026-01-22 03:54:57','2026-01-22 03:54:57',1),(2,'LAB002','Urine Test','Laboratory','Morning sample preferred',45,'2026-01-22 03:55:03','2026-01-22 03:55:03',1),(3,'CONS001','General Consultation','Consultation','Bring previous medical records',60,'2026-01-22 03:55:08','2026-01-22 03:55:08',1),(4,'CONS002','Pediatric Consultation','Consultation','Child vaccination card required',45,'2026-01-22 03:55:13','2026-01-22 03:55:13',1),(5,'LAB003','Lipid Profile','Laboratory','Fasting 12 hours',60,'2026-01-22 03:55:17','2026-01-22 03:55:17',1);
/*!40000 ALTER TABLE `prestations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professionals`
--

DROP TABLE IF EXISTS `professionals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `professionals` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `professional_registry` varchar(100) NOT NULL,
  `specialty` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `schedule_enabled` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professionals`
--

LOCK TABLES `professionals` WRITE;
/*!40000 ALTER TABLE `professionals` DISABLE KEYS */;
INSERT INTO `professionals` VALUES (1,'Ana','Rodríguez','REG-1023','Pediatría','ana.rodriguez@example.com','+584129876543','ACTIVE',1,1,'2026-01-22 03:17:21','2026-01-22 03:17:21'),(2,'Juan','Pérez','REG-2045','Neurología','juan.perez@example.com','+584128765432','ACTIVE',1,1,'2026-01-22 03:17:32','2026-01-22 03:17:32'),(3,'María','Gómez','REG-3098','Dermatología','maria.gomez@example.com','+584127654321','ACTIVE',1,1,'2026-01-22 03:17:40','2026-01-22 03:17:40'),(4,'Carlos','Martínez','REG-4076','Ortopedia','carlos.martinez@example.com','+584123456789','ACTIVE',1,1,'2026-01-22 03:17:45','2026-01-22 03:17:45'),(5,'Sofía','López','REG-5120','Ginecología','sofia.lopez@example.com','+584126789012','ACTIVE',1,1,'2026-01-22 03:17:54','2026-01-22 03:17:54');
/*!40000 ALTER TABLE `professionals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `results` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `summary` text NOT NULL,
  `file_id` varchar(255) DEFAULT NULL,
  `version` int(11) NOT NULL DEFAULT 1,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `date` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `idx_results_order_id` (`order_id`),
  CONSTRAINT `fk_results_order` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` VALUES (1,1,'Patient lab results normal','file_12345.pdf',1,'2026-01-22 04:15:05','2026-01-22 04:15:05','2026-01-05 00:00:00'),(2,2,'Elevated blood sugar levels','file_12346.pdf',1,'2026-01-22 04:15:12','2026-01-22 04:15:12','2026-01-06 00:00:00'),(3,3,'Cholesterol levels within normal range','file_12347.pdf',1,'2026-01-22 04:15:19','2026-01-22 04:15:19','2026-01-07 00:00:00');
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_permissions`
--

DROP TABLE IF EXISTS `role_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_permissions` (
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`role_id`,`permission_id`),
  KEY `fk_rp_perm` (`permission_id`),
  CONSTRAINT `fk_rp_perm` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_rp_role` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_permissions`
--

LOCK TABLES `role_permissions` WRITE;
/*!40000 ALTER TABLE `role_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `role_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'admin','admin','2026-01-21 23:06:25','2026-01-21 23:06:25');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_settings`
--

DROP TABLE IF EXISTS `system_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_settings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key_name` varchar(100) NOT NULL,
  `value_text` text DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `key_name` (`key_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_settings`
--

LOCK TABLES `system_settings` WRITE;
/*!40000 ALTER TABLE `system_settings` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `units`
--

DROP TABLE IF EXISTS `units`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `units` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(140) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `type` enum('SEDE','CONSULTORIO','SERVICIO') NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `phone` varchar(45) DEFAULT NULL,
  `schedule_reference` varchar(140) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `units`
--

LOCK TABLES `units` WRITE;
/*!40000 ALTER TABLE `units` DISABLE KEYS */;
INSERT INTO `units` VALUES (1,'Consultorio 201','Consultorio especializado en pediatría','CONSULTORIO','Av. Bolívar, Torre Médica, Piso 2',1,'2026-01-22 03:18:32','2026-01-22 03:18:32','+1 555-234-5678','Lunes a Viernes 9:00 AM - 5:00 PM'),(2,'Consultorio 301','Consultorio equipado para cardiología','CONSULTORIO','Calle Libertad, Edificio Salud Integral, Piso 3',1,'2026-01-22 03:18:38','2026-01-22 03:18:38','+1 555-345-6789','Lunes a Viernes 8:00 AM - 3:00 PM'),(3,'Consultorio 102','Consultorio para dermatología y estética','CONSULTORIO','Av. Central, Centro Médico, Piso 1',1,'2026-01-22 03:18:41','2026-01-22 03:18:41','+1 555-456-7890','Lunes a Viernes 10:00 AM - 6:00 PM'),(4,'Consultorio 401','Consultorio de neurología con equipamiento avanzado','CONSULTORIO','Calle 23, Edificio Salud Total, Piso 4',1,'2026-01-22 03:18:48','2026-01-22 03:18:48','+1 555-567-8901','Lunes a Viernes 7:30 AM - 2:30 PM'),(5,'Consultorio 501','Consultorio para ginecología y obstetricia','CONSULTORIO','Av. Los Pinos, Torre Salud, Piso 5',1,'2026-01-22 03:18:55','2026-01-22 03:18:55','+1 555-678-9012','Lunes a Viernes 8:00 AM - 4:00 PM');
/*!40000 ALTER TABLE `units` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_roles`
--

DROP TABLE IF EXISTS `user_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_roles` (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`role_id`),
  KEY `fk_ur_role` (`role_id`),
  CONSTRAINT `fk_ur_role` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_ur_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_roles`
--

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;
INSERT INTO `user_roles` VALUES (1,1);
/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `fk_user_person` (`person_id`),
  CONSTRAINT `fk_user_person` FOREIGN KEY (`person_id`) REFERENCES `people` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,1,'Ldaza','$2b$12$rDF9jvHppil91kwQPsHjXeyB2XxnDJvfZg4J2df6KPZaTkV7jkEva','ldaza2394@gmail.com',1,'2026-01-22 03:04:19','2026-01-22 03:04:19');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

SET FOREIGN_KEY_CHECKS=1;

--
-- Dumping routines for database 'healthcare_api'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-22 10:09:43
