-- Active: 1718884359506@@127.0.0.1@3306@gestor_contrasena
CREATE DATABASE IF NOT EXISTS gestor_contrasena;

USE gestor_contrasena;

CREATE TABLE `baul` (
 `id_baul` int NOT NULL AUTO_INCREMENT,
 `Plataforma` varchar(80) NOT NULL,
 `usuario` varchar(80) NOT NULL,
 `clave` varchar(80) NOT NULL,
 PRIMARY KEY (`id_baul`),
 UNIQUE KEY `Plataforma` (`Plataforma`,`usuario`)
) 
ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4;


