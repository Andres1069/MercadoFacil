-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-08-2025 a las 19:08:22
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mercado_digital`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

CREATE TABLE `carrito` (
  `Cod_Carrito` int(11) NOT NULL,
  `Fecha_creacion` datetime NOT NULL,
  `Fecha_modificacion` datetime NOT NULL,
  `Cantidad_articulos` int(11) NOT NULL,
  `Total` int(11) NOT NULL,
  `Id_usuario` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito`
--

INSERT INTO `carrito` (`Cod_Carrito`, `Fecha_creacion`, `Fecha_modificacion`, `Cantidad_articulos`, `Total`, `Id_usuario`) VALUES
(1, '2025-06-20 10:00:00', '2025-06-20 10:05:00', 3, 12500, 1),
(2, '2025-06-20 11:00:00', '2025-06-20 11:05:00', 2, 7500, 2),
(3, '2025-06-20 12:00:00', '2025-06-20 12:05:00', 4, 18000, 3),
(4, '2025-06-20 13:00:00', '2025-06-20 13:05:00', 1, 55000, 4),
(5, '2025-06-20 14:00:00', '2025-06-20 14:05:00', 5, 30000, 5),
(6, '2025-06-20 15:00:00', '2025-06-20 15:05:00', 2, 9000, 6),
(7, '2025-06-20 16:00:00', '2025-06-20 16:05:00', 3, 16000, 7),
(8, '2025-06-20 17:00:00', '2025-06-20 17:05:00', 4, 21000, 8),
(9, '2025-06-20 18:00:00', '2025-06-20 18:05:00', 1, 12000, 9),
(10, '2025-06-20 19:00:00', '2025-06-20 19:05:00', 2, 10500, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito_item`
--

CREATE TABLE `carrito_item` (
  `Id_carrito_item` int(11) NOT NULL,
  `Cod_carrito` int(11) NOT NULL,
  `Cod_producto` int(11) NOT NULL,
  `Cantidad` int(20) NOT NULL,
  `Precio` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito_item`
--

INSERT INTO `carrito_item` (`Id_carrito_item`, `Cod_carrito`, `Cod_producto`, `Cantidad`, `Precio`) VALUES
(1, 1, 1, 2, 8000),
(2, 1, 3, 1, 4200),
(3, 2, 2, 1, 5500),
(4, 2, 4, 1, 2800),
(5, 3, 6, 2, 6000),
(6, 3, 9, 2, 5000),
(7, 4, 8, 1, 55000),
(8, 5, 5, 3, 10500),
(9, 6, 7, 1, 12000),
(10, 7, 10, 2, 3600);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito_pedido`
--

CREATE TABLE `carrito_pedido` (
  `Cod_carrito` int(11) NOT NULL,
  `Cod_pedido` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito_pedido`
--

INSERT INTO `carrito_pedido` (`Cod_carrito`, `Cod_pedido`) VALUES
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
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `Cod_Categoria` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`Cod_Categoria`, `Nombre`) VALUES
(1, 'Alimentos'),
(2, 'Lácteos'),
(3, 'Aseo Personal'),
(4, 'Bebidas'),
(5, 'Panadería'),
(6, 'Frutas y Verduras'),
(7, 'Carnes'),
(8, 'Granos'),
(9, 'Licores'),
(10, 'Snacks');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `domicilio`
--

CREATE TABLE `domicilio` (
  `Cod_Domicilio` int(11) NOT NULL,
  `Fecha` datetime NOT NULL,
  `Estado` varchar(30) NOT NULL,
  `Cod_genera` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `domicilio`
--

INSERT INTO `domicilio` (`Cod_Domicilio`, `Fecha`, `Estado`, `Cod_genera`) VALUES
(1, '2025-06-21 08:00:00', 'Pendiente', 1),
(2, '2025-06-21 09:00:00', 'En camino', 2),
(3, '2025-06-21 10:00:00', 'Entregado', 3),
(4, '2025-06-21 11:00:00', 'Cancelado', 4),
(5, '2025-06-21 12:00:00', 'Pendiente', 5),
(6, '2025-06-21 13:00:00', 'En camino', 6),
(7, '2025-06-21 14:00:00', 'Entregado', 7),
(8, '2025-06-21 15:00:00', 'Cancelado', 8),
(9, '2025-06-21 16:00:00', 'Pendiente', 9),
(10, '2025-06-21 17:00:00', 'En camino', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pago`
--

CREATE TABLE `pago` (
  `Cod_Pago` int(11) NOT NULL,
  `Metodo_Pago` varchar(50) NOT NULL,
  `Fecha_Pago` datetime NOT NULL,
  `Monto_Pago` int(11) NOT NULL,
  `Cod_pedido` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pago`
--

INSERT INTO `pago` (`Cod_Pago`, `Metodo_Pago`, `Fecha_Pago`, `Monto_Pago`, `Cod_pedido`) VALUES
(1, 'Tarjeta Crédito', '2025-06-20 10:45:00', 12500, 1),
(2, 'PSE', '2025-06-20 11:45:00', 7500, 2),
(3, 'Efectivo', '2025-06-20 12:45:00', 18000, 3),
(4, 'Tarjeta Débito', '2025-06-20 13:45:00', 55000, 4),
(5, 'Transferencia', '2025-06-20 14:45:00', 30000, 5),
(6, 'Nequi', '2025-06-20 15:45:00', 9000, 6),
(7, 'Daviplata', '2025-06-20 16:45:00', 16000, 7),
(8, 'Efectivo', '2025-06-20 17:45:00', 21000, 8),
(9, 'Tarjeta Crédito', '2025-06-20 18:45:00', 12000, 9),
(10, 'PSE', '2025-06-20 19:45:00', 10500, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE `pedido` (
  `Cod_Pedido` int(11) NOT NULL,
  `Fecha_Pedido` datetime NOT NULL,
  `Estado_Pedido` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedido`
--

INSERT INTO `pedido` (`Cod_Pedido`, `Fecha_Pedido`, `Estado_Pedido`) VALUES
(1, '2025-06-20 10:30:00', 'Pendiente'),
(2, '2025-06-20 11:30:00', 'En proceso'),
(3, '2025-06-20 12:30:00', 'Enviado'),
(4, '2025-06-20 13:30:00', 'Entregado'),
(5, '2025-06-20 14:30:00', 'Cancelado'),
(6, '2025-06-20 15:30:00', 'Pendiente'),
(7, '2025-06-20 16:30:00', 'En proceso'),
(8, '2025-06-20 17:30:00', 'Enviado'),
(9, '2025-06-20 18:30:00', 'Entregado'),
(10, '2025-06-20 19:30:00', 'Cancelado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `Cod_Producto` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Precio` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL,
  `Fecha_vencimiento` datetime NOT NULL,
  `Descripcion` varchar(255) NOT NULL,
  `imagen_url` varchar(255) DEFAULT NULL,
  `Cod_categoria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`Cod_Producto`, `Nombre`, `Precio`, `Cantidad`, `Fecha_vencimiento`, `Descripcion`, `imagen_url`, `Cod_categoria`) VALUES
(1, 'Leche Alpina 1L', 4000, 20, '2025-12-31 00:00:00', 'Leche entera Alpina', NULL, 2),
(2, 'Pan Bimbo Tradicional', 5500, 30, '2025-07-15 00:00:00', 'Pan de caja para desayunos', NULL, 5),
(3, 'Arroz Diana 1kg', 4200, 50, '2026-01-10 00:00:00', 'Arroz blanco', NULL, 8),
(4, 'Jabón Rexona', 2800, 25, '2026-03-20 00:00:00', 'Jabón corporal', NULL, 3),
(5, 'Jugó Hit Mango 1L', 3500, 40, '2026-05-10 00:00:00', 'Jugo de fruta', NULL, 4),
(6, 'Manzanas Rojas', 3000, 60, '2025-07-05 00:00:00', 'Manzanas frescas por libra', NULL, 6),
(7, 'Pechuga de Pollo', 12000, 15, '2025-07-02 00:00:00', 'Carne fresca de pollo', NULL, 7),
(8, 'Ron Medellín 750ml', 55000, 10, '2026-12-31 00:00:00', 'Licor nacional', NULL, 9),
(9, 'Papas Margarita BBQ 150g', 2500, 100, '2026-02-28 00:00:00', 'Papas sabor BBQ', NULL, 10),
(10, 'Yogurt Alpina Fresa', 1800, 35, '2025-08-15 00:00:00', 'Yogurt sabor fresa', NULL, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `Id` int(11) NOT NULL,
  `Num_Doc` varchar(20) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `Contraseña` varchar(50) NOT NULL,
  `Telefono` varchar(20) NOT NULL,
  `Correo` varchar(100) NOT NULL,
  `Barrio` varchar(100) NOT NULL,
  `Direccion` varchar(100) NOT NULL,
  `Rol` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`Id`, `Num_Doc`, `Nombre`, `Apellido`, `Contraseña`, `Telefono`, `Correo`, `Barrio`, `Direccion`, `Rol`) VALUES
(1, '1001001001', 'Carlos', 'García', '3001112233', 'Chicalá', 'carlos@ejemplo.com', 'Calle 10 #20-30', 'Cliente', 'Administrador'),
(2, '1001001002', 'Ana', 'Martínez', 'anaPass2025', '3012233445', 'ana@ejemplo.com', 'Chicalá', 'Carrera 45 #12-50', 'Cliente'),
(3, '1001001003', 'Luis', 'Rodríguez', 'luis7890', '3023344556', 'luis@ejemplo.com', 'Chicalá', 'Transversal 76 #30-90', 'Cliente'),
(4, '1001001004', 'Marta', 'Pérez', 'martita22', '3034455667', 'marta@ejemplo.com', 'Chicalá', 'Diagonal 33 #15-60', 'Cliente'),
(5, '1001001005', 'Juan', 'Mejía', '321', '3045566778', 'admin', 'Chicalá', 'Calle 8 #25-40', 'Administrador'),
(6, '1001001006', 'Sofía', 'Herrera', 'sofia2025', '3056677889', 'sofia@ejemplo.com', 'Chicalá', 'Carrera 78 #50-15', 'Cliente'),
(7, '1001001007', 'Daniel', 'Ramírez', 'dani2025', '3067788990', 'daniel@ejemplo.com', 'Chicalá', 'Calle 65 #72-20', 'Cliente'),
(8, '1001001008', 'Camila', 'Restrepo', 'camila123', '3078899001', 'camila@ejemplo.com', 'Chicalá', 'Carrera 37 #48-90', 'Cliente'),
(9, '1001001009', 'Pedro', 'Suárez', 'pedrito2025', '3089900112', 'pedro@ejemplo.com', 'Chicalá', 'Calle 80 #60-10', 'Cliente'),
(10, '1001001010', 'Laura', 'Morales', 'lauraPass', '3091011121', 'laura@ejemplo.com', 'Chicalá', 'Carrera 50 #20-25', 'Cliente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_pedido`
--

CREATE TABLE `usuario_pedido` (
  `Cod_Genera` int(11) NOT NULL,
  `Id_Usuario` int(11) NOT NULL,
  `Cod_pedido` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario_pedido`
--

INSERT INTO `usuario_pedido` (`Cod_Genera`, `Id_Usuario`, `Cod_pedido`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD PRIMARY KEY (`Cod_Carrito`),
  ADD KEY `Id_usuario` (`Id_usuario`);

--
-- Indices de la tabla `carrito_item`
--
ALTER TABLE `carrito_item`
  ADD PRIMARY KEY (`Id_carrito_item`),
  ADD KEY `Cod_carrito` (`Cod_carrito`),
  ADD KEY `Cod_producto` (`Cod_producto`);

--
-- Indices de la tabla `carrito_pedido`
--
ALTER TABLE `carrito_pedido`
  ADD KEY `Cod_carrito` (`Cod_carrito`),
  ADD KEY `Cod_pedido` (`Cod_pedido`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`Cod_Categoria`);

--
-- Indices de la tabla `domicilio`
--
ALTER TABLE `domicilio`
  ADD PRIMARY KEY (`Cod_Domicilio`),
  ADD KEY `Cod_genera` (`Cod_genera`);

--
-- Indices de la tabla `pago`
--
ALTER TABLE `pago`
  ADD PRIMARY KEY (`Cod_Pago`),
  ADD KEY `Cod_pedido` (`Cod_pedido`);

--
-- Indices de la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`Cod_Pedido`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`Cod_Producto`),
  ADD KEY `Cod_categoria` (`Cod_categoria`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `Num_Doc` (`Num_Doc`);

--
-- Indices de la tabla `usuario_pedido`
--
ALTER TABLE `usuario_pedido`
  ADD PRIMARY KEY (`Cod_Genera`),
  ADD KEY `Id_Usuario` (`Id_Usuario`),
  ADD KEY `Cod_pedido` (`Cod_pedido`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carrito`
--
ALTER TABLE `carrito`
  MODIFY `Cod_Carrito` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `carrito_item`
--
ALTER TABLE `carrito_item`
  MODIFY `Id_carrito_item` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `Cod_Categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `domicilio`
--
ALTER TABLE `domicilio`
  MODIFY `Cod_Domicilio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `pago`
--
ALTER TABLE `pago`
  MODIFY `Cod_Pago` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `pedido`
--
ALTER TABLE `pedido`
  MODIFY `Cod_Pedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `Cod_Producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `usuario_pedido`
--
ALTER TABLE `usuario_pedido`
  MODIFY `Cod_Genera` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD CONSTRAINT `fk_carrito_usuario` FOREIGN KEY (`Id_usuario`) REFERENCES `usuario` (`Id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `carrito_item`
--
ALTER TABLE `carrito_item`
  ADD CONSTRAINT `fk_carritoitem_carrito` FOREIGN KEY (`Cod_carrito`) REFERENCES `carrito` (`Cod_Carrito`),
  ADD CONSTRAINT `fk_carritoitem_producto` FOREIGN KEY (`Cod_producto`) REFERENCES `producto` (`Cod_Producto`);

--
-- Filtros para la tabla `carrito_pedido`
--
ALTER TABLE `carrito_pedido`
  ADD CONSTRAINT `fk_carritopedido_carrito` FOREIGN KEY (`Cod_carrito`) REFERENCES `carrito` (`Cod_Carrito`),
  ADD CONSTRAINT `fk_carritopedido_pedido` FOREIGN KEY (`Cod_pedido`) REFERENCES `pedido` (`Cod_Pedido`);

--
-- Filtros para la tabla `domicilio`
--
ALTER TABLE `domicilio`
  ADD CONSTRAINT `fk_domicilio_usuariopedido` FOREIGN KEY (`Cod_genera`) REFERENCES `usuario_pedido` (`Cod_Genera`);

--
-- Filtros para la tabla `pago`
--
ALTER TABLE `pago`
  ADD CONSTRAINT `fk_pago_pedido` FOREIGN KEY (`Cod_pedido`) REFERENCES `pedido` (`Cod_Pedido`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `fk_producto_categoria` FOREIGN KEY (`Cod_categoria`) REFERENCES `categoria` (`Cod_Categoria`);

--
-- Filtros para la tabla `usuario_pedido`
--
ALTER TABLE `usuario_pedido`
  ADD CONSTRAINT `fk_usuariopedido_pedido` FOREIGN KEY (`Cod_pedido`) REFERENCES `pedido` (`Cod_Pedido`),
  ADD CONSTRAINT `fk_usuariopedido_usuario` FOREIGN KEY (`Id_Usuario`) REFERENCES `usuario` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
