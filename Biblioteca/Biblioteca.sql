-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: mysql_db
-- Tiempo de generación: 05-03-2025 a las 11:36:59
-- Versión del servidor: 8.0.40
-- Versión de PHP: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Biblioteca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autores`
--

CREATE TABLE `autores` (
  `id` int NOT NULL,
  `nombre` varchar(255) COLLATE utf8mb4_spanish_ci NOT NULL,
  `apellido` varchar(255) COLLATE utf8mb4_spanish_ci NOT NULL,
  `nacionalidad` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `autores`
--

INSERT INTO `autores` (`id`, `nombre`, `apellido`, `nacionalidad`) VALUES
(1, 'Gabriel', 'García Márquez', 'Colombiana'),
(2, 'Isabel', 'Allende', 'Chilena'),
(3, 'J.K.', 'Rowling', 'Británica'),
(4, 'George', 'Orwell', 'Británica'),
(5, 'Mario', 'Vargas Llosa', 'Peruana'),
(6, 'Julio', 'Cortázar', 'Argentino'),
(7, 'Haruki', 'Murakami', 'Japonesa'),
(8, 'Jane', 'Austen', 'Británica'),
(9, 'Mark', 'Twain', 'Americana'),
(10, 'Virginia', 'Woolf', 'Británica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor_libro`
--

CREATE TABLE `autor_libro` (
  `id_autor` int NOT NULL,
  `id_libro` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `autor_libro`
--

INSERT INTO `autor_libro` (`id_autor`, `id_libro`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `editoriales`
--

CREATE TABLE `editoriales` (
  `id` int NOT NULL,
  `nombre` varchar(255) COLLATE utf8mb4_spanish_ci NOT NULL,
  `direccion` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `telefono` varchar(9) COLLATE utf8mb4_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `editoriales`
--

INSERT INTO `editoriales` (`id`, `nombre`, `direccion`, `telefono`) VALUES
(1, 'Editorial Planeta', 'cervantes 6 3D', '687254159'),
(2, 'Grupo Santillana', NULL, NULL),
(3, 'Penguin Random House', NULL, NULL),
(4, 'Ediciones Akal', NULL, NULL),
(5, 'Editorial Anagrama', NULL, NULL),
(6, 'RBA Libros', NULL, NULL),
(7, 'Editorial Espasa', NULL, NULL),
(8, 'Alianza Editorial', NULL, NULL),
(9, 'Ediciones B', NULL, NULL),
(10, 'Tusquets Editores', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `id` int NOT NULL,
  `titulo` varchar(255) COLLATE utf8mb4_spanish_ci NOT NULL,
  `anio` date DEFAULT NULL,
  `id_editorial` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`id`, `titulo`, `anio`, `id_editorial`) VALUES
(1, 'Cien años de soledad', '1967-01-01', 1),
(2, 'La casa de los espíritus', '1982-01-01', 2),
(3, 'Harry Potter y la piedra filosofal', '1997-01-01', 3),
(4, '1984', '1949-01-01', 4),
(5, 'La ciudad y los perros', '1963-01-01', 5),
(6, 'Rayuela', '1963-01-01', 6),
(7, 'Kafka en la orilla', '2002-01-01', 7),
(8, 'Orgullo y prejuicio', '1813-01-01', 8),
(9, 'Las aventuras de Tom Sawyer', '1876-01-01', 9),
(10, 'Al faro', '1927-01-01', 10),
(11, 'El amor en los tiempos del cólera', '1985-01-01', 1),
(12, 'Crónica de una muerte anunciada', '1981-01-01', 1),
(13, 'El túnel', '1948-01-01', 2),
(14, 'Ficciones', '1944-01-01', 2),
(15, 'Cumbres borrascosas', '1847-01-01', 3),
(16, 'El gran Gatsby', '1925-01-01', 4),
(17, 'Moby Dick', '1851-01-01', 5),
(18, 'Don Quijote de la Mancha', '1605-01-01', 6),
(19, 'En busca del tiempo perdido', '1913-01-01', 7),
(20, 'La metamorfosis', '1915-01-01', 8),
(21, 'Las uvas de la ira', '1939-01-01', 9),
(22, 'El retrato de Dorian Gray', '1890-01-01', 10),
(23, 'La sombra del viento', '2001-01-01', 1),
(24, 'El viejo y el mar', '1952-01-01', 2),
(25, 'Cuentos de la selva', '1918-01-01', 3),
(26, 'Los miserables', '1862-01-01', 4),
(27, 'El principito', '1943-01-01', 5),
(28, 'El nombre de la rosa', '1980-01-01', 6);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `autor_libro`
--
ALTER TABLE `autor_libro`
  ADD PRIMARY KEY (`id_autor`,`id_libro`),
  ADD KEY `id_libro` (`id_libro`);

--
-- Indices de la tabla `editoriales`
--
ALTER TABLE `editoriales`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_editorial` (`id_editorial`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autores`
--
ALTER TABLE `autores`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `editoriales`
--
ALTER TABLE `editoriales`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `libros`
--
ALTER TABLE `libros`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `autor_libro`
--
ALTER TABLE `autor_libro`
  ADD CONSTRAINT `autor_libro_ibfk_1` FOREIGN KEY (`id_autor`) REFERENCES `autores` (`id`),
  ADD CONSTRAINT `autor_libro_ibfk_2` FOREIGN KEY (`id_libro`) REFERENCES `libros` (`id`);

--
-- Filtros para la tabla `libros`
--
ALTER TABLE `libros`
  ADD CONSTRAINT `libros_ibfk_1` FOREIGN KEY (`id_editorial`) REFERENCES `editoriales` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
