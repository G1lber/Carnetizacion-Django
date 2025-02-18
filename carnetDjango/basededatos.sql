-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         11.7.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para carnetmoi
CREATE DATABASE IF NOT EXISTS `carnetmoi` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci */;
USE `carnetmoi`;

-- Volcando estructura para tabla carnetmoi.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.auth_group: ~0 rows (aproximadamente)

-- Volcando estructura para tabla carnetmoi.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.auth_group_permissions: ~0 rows (aproximadamente)

-- Volcando estructura para tabla carnetmoi.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.auth_permission: ~40 rows (aproximadamente)
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add ficha', 7, 'add_ficha'),
	(26, 'Can change ficha', 7, 'change_ficha'),
	(27, 'Can delete ficha', 7, 'delete_ficha'),
	(28, 'Can view ficha', 7, 'view_ficha'),
	(29, 'Can add rh', 8, 'add_rh'),
	(30, 'Can change rh', 8, 'change_rh'),
	(31, 'Can delete rh', 8, 'delete_rh'),
	(32, 'Can view rh', 8, 'view_rh'),
	(33, 'Can add rol', 9, 'add_rol'),
	(34, 'Can change rol', 9, 'change_rol'),
	(35, 'Can delete rol', 9, 'delete_rol'),
	(36, 'Can view rol', 9, 'view_rol'),
	(37, 'Can add tipo_doc', 10, 'add_tipo_doc'),
	(38, 'Can change tipo_doc', 10, 'change_tipo_doc'),
	(39, 'Can delete tipo_doc', 10, 'delete_tipo_doc'),
	(40, 'Can view tipo_doc', 10, 'view_tipo_doc');

-- Volcando estructura para tabla carnetmoi.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.auth_user: ~1 rows (aproximadamente)
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$870000$244UKKuBv9ZpVPoNlO7zhk$5nUl5pUTseuMNVzhHpxQY3/7CTeoTf967o2gRVpWk9k=', '2025-02-18 04:36:51.018753', 1, 'adso', '', '', 'adso@gmail.com', 1, 1, '2025-02-18 04:23:03.106375');

-- Volcando estructura para tabla carnetmoi.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.auth_user_groups: ~0 rows (aproximadamente)

-- Volcando estructura para tabla carnetmoi.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.auth_user_user_permissions: ~0 rows (aproximadamente)

-- Volcando estructura para tabla carnetmoi.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.django_admin_log: ~0 rows (aproximadamente)

-- Volcando estructura para tabla carnetmoi.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.django_content_type: ~6 rows (aproximadamente)
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(7, 'mainapp', 'ficha'),
	(8, 'mainapp', 'rh'),
	(9, 'mainapp', 'rol'),
	(10, 'mainapp', 'tipo_doc'),
	(6, 'sessions', 'session');

-- Volcando estructura para tabla carnetmoi.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.django_migrations: ~19 rows (aproximadamente)
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2025-02-17 22:01:40.502925'),
	(2, 'auth', '0001_initial', '2025-02-17 22:01:40.713841'),
	(3, 'admin', '0001_initial', '2025-02-17 22:01:40.761932'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2025-02-17 22:01:40.767026'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-02-17 22:01:40.771027'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2025-02-17 22:01:40.822395'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2025-02-17 22:01:40.861405'),
	(8, 'auth', '0003_alter_user_email_max_length', '2025-02-17 22:01:40.876028'),
	(9, 'auth', '0004_alter_user_username_opts', '2025-02-17 22:01:40.880634'),
	(10, 'auth', '0005_alter_user_last_login_null', '2025-02-17 22:01:40.900678'),
	(11, 'auth', '0006_require_contenttypes_0002', '2025-02-17 22:01:40.901638'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2025-02-17 22:01:40.906390'),
	(13, 'auth', '0008_alter_user_username_max_length', '2025-02-17 22:01:40.919971'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2025-02-17 22:01:40.933954'),
	(15, 'auth', '0010_alter_group_name_max_length', '2025-02-17 22:01:40.950362'),
	(16, 'auth', '0011_update_proxy_permissions', '2025-02-17 22:01:40.955364'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2025-02-17 22:01:40.968496'),
	(18, 'sessions', '0001_initial', '2025-02-17 22:01:40.989253'),
	(19, 'mainapp', '0001_initial', '2025-02-18 23:03:44.300506');

-- Volcando estructura para tabla carnetmoi.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.django_session: ~2 rows (aproximadamente)
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('jgukwdr5tpproqdsylmhbs1ddo05kc24', '.eJxVjMEOwiAQRP-FsyELC7b16N1vIMsu2KqBpLQn47_bJj3ocea9mbcKtC5jWFuawyTqoow6_XaR-JnKDuRB5V4117LMU9S7og_a9K1Kel0P9-9gpDZua0cgfQQQsExwlmgyCJFnw4xb8hEFO_ZI2bshY7JDbx0mHCxwl0h9vv7gOGU:1tkFLn:hIuuFnoWkYwl2a6qszeCftwa7lGd17Z0Bm5lR6KrIfc', '2025-03-04 04:36:51.029762'),
	('u3h7qoz3dfn7fhjzifz67yl0nusbsav2', 'e30:1tkEkM:H6HFYWMI4elKjmP4oTqf_dPJLFExbBAtWrciBeVK4so', '2025-03-04 03:58:10.579941');

-- Volcando estructura para tabla carnetmoi.mainapp_ficha
CREATE TABLE IF NOT EXISTS `mainapp_ficha` (
  `num_ficha` int(11) NOT NULL,
  `fecha_inicio` datetime(6) DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  PRIMARY KEY (`num_ficha`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.mainapp_ficha: ~0 rows (aproximadamente)

-- Volcando estructura para tabla carnetmoi.mainapp_rh
CREATE TABLE IF NOT EXISTS `mainapp_rh` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre_tipo` varchar(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.mainapp_rh: ~0 rows (aproximadamente)

-- Volcando estructura para tabla carnetmoi.mainapp_rol
CREATE TABLE IF NOT EXISTS `mainapp_rol` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.mainapp_rol: ~0 rows (aproximadamente)

-- Volcando estructura para tabla carnetmoi.mainapp_tipo_doc
CREATE TABLE IF NOT EXISTS `mainapp_tipo_doc` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre_doc` varchar(18) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.mainapp_tipo_doc: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
