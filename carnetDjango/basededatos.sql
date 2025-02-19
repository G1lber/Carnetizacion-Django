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
	(13, 'Can add content type', 4, 'add_contenttype'),
	(14, 'Can change content type', 4, 'change_contenttype'),
	(15, 'Can delete content type', 4, 'delete_contenttype'),
	(16, 'Can view content type', 4, 'view_contenttype'),
	(17, 'Can add session', 5, 'add_session'),
	(18, 'Can change session', 5, 'change_session'),
	(19, 'Can delete session', 5, 'delete_session'),
	(20, 'Can view session', 5, 'view_session'),
	(21, 'Can add ficha', 6, 'add_ficha'),
	(22, 'Can change ficha', 6, 'change_ficha'),
	(23, 'Can delete ficha', 6, 'delete_ficha'),
	(24, 'Can view ficha', 6, 'view_ficha'),
	(25, 'Can add rh', 7, 'add_rh'),
	(26, 'Can change rh', 7, 'change_rh'),
	(27, 'Can delete rh', 7, 'delete_rh'),
	(28, 'Can view rh', 7, 'view_rh'),
	(29, 'Can add rol', 8, 'add_rol'),
	(30, 'Can change rol', 8, 'change_rol'),
	(31, 'Can delete rol', 8, 'delete_rol'),
	(32, 'Can view rol', 8, 'view_rol'),
	(33, 'Can add tipo_doc', 9, 'add_tipo_doc'),
	(34, 'Can change tipo_doc', 9, 'change_tipo_doc'),
	(35, 'Can delete tipo_doc', 9, 'delete_tipo_doc'),
	(36, 'Can view tipo_doc', 9, 'view_tipo_doc'),
	(37, 'Can add user', 10, 'add_usuariopersonalizado'),
	(38, 'Can change user', 10, 'change_usuariopersonalizado'),
	(39, 'Can delete user', 10, 'delete_usuariopersonalizado'),
	(40, 'Can view user', 10, 'view_usuariopersonalizado');

-- Volcando estructura para tabla carnetmoi.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_mainapp_u` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_mainapp_u` FOREIGN KEY (`user_id`) REFERENCES `mainapp_usuariopersonalizado` (`id`)
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

-- Volcando datos para la tabla carnetmoi.django_content_type: ~10 rows (aproximadamente)
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'contenttypes', 'contenttype'),
	(6, 'mainapp', 'ficha'),
	(7, 'mainapp', 'rh'),
	(8, 'mainapp', 'rol'),
	(9, 'mainapp', 'tipo_doc'),
	(10, 'mainapp', 'usuariopersonalizado'),
	(5, 'sessions', 'session');

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
	(1, 'contenttypes', '0001_initial', '2025-02-19 00:46:00.896470'),
	(2, 'contenttypes', '0002_remove_content_type_name', '2025-02-19 00:46:00.921786'),
	(3, 'auth', '0001_initial', '2025-02-19 00:46:01.018710'),
	(4, 'auth', '0002_alter_permission_name_max_length', '2025-02-19 00:46:01.037933'),
	(5, 'auth', '0003_alter_user_email_max_length', '2025-02-19 00:46:01.041375'),
	(6, 'auth', '0004_alter_user_username_opts', '2025-02-19 00:46:01.045293'),
	(7, 'auth', '0005_alter_user_last_login_null', '2025-02-19 00:46:01.048573'),
	(8, 'auth', '0006_require_contenttypes_0002', '2025-02-19 00:46:01.049574'),
	(9, 'auth', '0007_alter_validators_add_error_messages', '2025-02-19 00:46:01.054575'),
	(10, 'auth', '0008_alter_user_username_max_length', '2025-02-19 00:46:01.057576'),
	(11, 'auth', '0009_alter_user_last_name_max_length', '2025-02-19 00:46:01.073179'),
	(12, 'auth', '0010_alter_group_name_max_length', '2025-02-19 00:46:01.083867'),
	(13, 'auth', '0011_update_proxy_permissions', '2025-02-19 00:46:01.086925'),
	(14, 'auth', '0012_alter_user_first_name_max_length', '2025-02-19 00:46:01.089926'),
	(15, 'mainapp', '0001_initial', '2025-02-19 00:46:01.286201'),
	(16, 'admin', '0001_initial', '2025-02-19 00:46:01.339075'),
	(17, 'admin', '0002_logentry_remove_auto_add', '2025-02-19 00:46:01.345170'),
	(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-02-19 00:46:01.350932'),
	(19, 'sessions', '0001_initial', '2025-02-19 00:46:01.369111');

-- Volcando estructura para tabla carnetmoi.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.django_session: ~0 rows (aproximadamente)

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

-- Volcando estructura para tabla carnetmoi.mainapp_usuariopersonalizado
CREATE TABLE IF NOT EXISTS `mainapp_usuariopersonalizado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  `ficha_id` int(11) DEFAULT NULL,
  `rh_id` bigint(20) DEFAULT NULL,
  `rol_id` bigint(20) DEFAULT NULL,
  `tipo_doc_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `mainapp_usuarioperso_ficha_id_b60ecd41_fk_mainapp_f` (`ficha_id`),
  KEY `mainapp_usuariopersonalizado_rh_id_96e3e53d_fk_mainapp_rh_id` (`rh_id`),
  KEY `mainapp_usuariopersonalizado_rol_id_d6766d97_fk_mainapp_rol_id` (`rol_id`),
  KEY `mainapp_usuarioperso_tipo_doc_id_3725b6f4_fk_mainapp_t` (`tipo_doc_id`),
  CONSTRAINT `mainapp_usuarioperso_ficha_id_b60ecd41_fk_mainapp_f` FOREIGN KEY (`ficha_id`) REFERENCES `mainapp_ficha` (`num_ficha`),
  CONSTRAINT `mainapp_usuarioperso_tipo_doc_id_3725b6f4_fk_mainapp_t` FOREIGN KEY (`tipo_doc_id`) REFERENCES `mainapp_tipo_doc` (`id`),
  CONSTRAINT `mainapp_usuariopersonalizado_rh_id_96e3e53d_fk_mainapp_rh_id` FOREIGN KEY (`rh_id`) REFERENCES `mainapp_rh` (`id`),
  CONSTRAINT `mainapp_usuariopersonalizado_rol_id_d6766d97_fk_mainapp_rol_id` FOREIGN KEY (`rol_id`) REFERENCES `mainapp_rol` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.mainapp_usuariopersonalizado: ~1 rows (aproximadamente)
INSERT INTO `mainapp_usuariopersonalizado` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `ficha_id`, `rh_id`, `rol_id`, `tipo_doc_id`) VALUES
	(1, 'pbkdf2_sha256$870000$FjWy6iSsEHP38oZqmnTJ4a$abIjUMg+JvigF9qW9zhUNK6FPyXgY13LHRVvr3hWb3s=', NULL, 1, 'adso', '', '', 'adso@gmail.com', 1, 1, '2025-02-19 00:47:43.065560', NULL, NULL, NULL, NULL);

-- Volcando estructura para tabla carnetmoi.mainapp_usuariopersonalizado_groups
CREATE TABLE IF NOT EXISTS `mainapp_usuariopersonalizado_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usuariopersonalizado_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mainapp_usuariopersonali_usuariopersonalizado_id__d8b78d5a_uniq` (`usuariopersonalizado_id`,`group_id`),
  KEY `mainapp_usuarioperso_group_id_8d06d6de_fk_auth_grou` (`group_id`),
  CONSTRAINT `mainapp_usuarioperso_group_id_8d06d6de_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `mainapp_usuarioperso_usuariopersonalizado_13e39940_fk_mainapp_u` FOREIGN KEY (`usuariopersonalizado_id`) REFERENCES `mainapp_usuariopersonalizado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.mainapp_usuariopersonalizado_groups: ~0 rows (aproximadamente)

-- Volcando estructura para tabla carnetmoi.mainapp_usuariopersonalizado_user_permissions
CREATE TABLE IF NOT EXISTS `mainapp_usuariopersonalizado_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usuariopersonalizado_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mainapp_usuariopersonali_usuariopersonalizado_id__1c7e8999_uniq` (`usuariopersonalizado_id`,`permission_id`),
  KEY `mainapp_usuarioperso_permission_id_bf212e81_fk_auth_perm` (`permission_id`),
  CONSTRAINT `mainapp_usuarioperso_permission_id_bf212e81_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `mainapp_usuarioperso_usuariopersonalizado_eef02172_fk_mainapp_u` FOREIGN KEY (`usuariopersonalizado_id`) REFERENCES `mainapp_usuariopersonalizado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- Volcando datos para la tabla carnetmoi.mainapp_usuariopersonalizado_user_permissions: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
