use bd_hospital_farmacia;

SHOW PROCEDURE STATUS WHERE Db = 'bd_hospital_farmacia';


CALL sp_limpia_bd('farmacmd');
CALL sp_estatus_bd('farmacmd');
-- CALL sp_poblar_bd();

SELECT GenerarDescripcionLote();
SELECT GenerarFechaSolicitud();
-- select fn_numero_aleatorio_rangos(6,9);
SELECT GenerarCantidad();
SELECT GenerarCodigoLote();

-- SP PARA INSERTAR LOTES_MEDICAMENTOS Y DETALLE_LOTES
CALL sp_insertar_lotes(10);

-- El id de la receta, lo deje null, ya que no puedo hacer un registro de prueba en receta, 
-- porque la tabla contiene citaId y no existe. POR ESE CASO EL ATRIBUTO RECETA_ID SE LE QUITO NN
-- Lo que corresponde al total aun falta, estoy ocupando por el momento cantidades aleatorias, usando la fn genera_cantidad aplicado en sp_lotes...
CALL sp_insertar_dispensacion_medicamentos(4); -- INSERTA EN DISPENSACION_MEDICAMENTOS
-- SELECT sp_insertar_dispensacion(2); aun no funciona 


select*from dispensacion_medicamentos;
select*from lotes_medicamentos;
select*from detalle_lotes;



-- SP, TRIGGERS DE LOTES, SP Y TRIGGERS DE LA TABLA DISPENSACION_MEDICAMENTOS


