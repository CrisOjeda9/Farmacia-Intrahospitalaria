use bd_hospital_210467;

SHOW PROCEDURE STATUS WHERE Db = 'bd_hospital_210467';

-- limpiar la base de datos
CALL sp_limpia_bd('farmacmd');
-- poblar la base
 CALL sp_poblar_bd();
-- estatus de la basede datos
CALL sp_estatus_bd('farmacmd');

-- PRUEBAS de FUNCIONES, usadas en los procedimeintos 
SELECT GenerarDescripcionLote();
SELECT GenerarFechaSolicitud();
SELECT GenerarCantidad();
SELECT GenerarCodigoLote();

-- PROCEDIMEINTO PARA LA INSERCION DE LAS TABLAS LOTES_MEDICAMENTOS Y DETALLE_LOTES
CALL sp_insertar_lotes(50);
select*from lotes_medicamentos;
select*from detalle_lotes;

-- El id de la receta, lo deje null, ya que no puedo hacer un registro de prueba en receta, 
-- porque la tabla contiene citaId y no existe. POR ESE CASO EL ATRIBUTO RECETA_ID SE LE QUITO NN
-- Lo que corresponde al total aun falta, estoy ocupando por el momento cantidades aleatorias, usando la fn genera_cantidad aplicado en sp_lotes...
-- CALL sp_insertar_dispensacion_medicamentos(1,8); -- INSERTA EN DISPENSACION_MEDICAMENTOS
-- SELECT sp_insertar_dispensacion(2); aun no funciona 

-- PROCEDIMEINTO PARA LLENAR LA TABLA CITAS, RECETA_MEDICA Y RECETA_MEDICA_DETALLES, para poder ocupar dispensacion
CALL InsertarCitaYReceta(50);
select*from citas;
select*from receta_medica;
select*from receta_medica_detalle;

-- PROCEDIMIENTO PARA LA INSERCION DE LA TABLA DE DISPENSACION MEDICAMNETOS
CALL sp_insertar_dispensacion_medicamentos(2);
select*from dispensacion_medicamentos;

-- PROCEDIMIENTO PARA LA INSERCION DE LA TABLA DE DETALLES DISPENSACION
CALL sp_insertar_detalles_dispensacion(1);
select*from detalles_dispensacion;




-- PRUEBAS DE FUNCIONES PARA CALCULAR LA CANTIDAD DE MEDICAMNETOS 
-- A ENTREGAR EN CUANTO A LA DOSIS PREESCRITA EN DETALLES RECETA Y LA CANTIDAD QUE POSEE EL MEDICAMENTO POR UNIDAD
select fn_calcular_cantidad_por_unidad (2);

-- PRUEBAS DE LA FUNCION PARA CALCULAR EL PRECIO VENTA (precio unitario de detalles lotes)
-- EN BASE AL PRECIO COSTO(precio unitario en lotes medicamnetos)
-- SELECT calcular_precio_venta_por_lote(3) AS Precio_de_Venta;



