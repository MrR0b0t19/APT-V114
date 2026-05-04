# APT Sobre instituciones financieras

Este paper posiblemente se de una unica vez en mexico, se esta preparando la documentacion extensa sobre la informacion tecnica bajo /APT-V114/Paper/2027. 

# Nuevo giro

Nuevamente como sabras, el equipo trabaja en conjunto para una seleccion de tecnicas actualizadas para que la audiencia ademas de llevarse una tecnica tengan las capacidades de poder utilizarlas para sus pruebas propias
este giro a llevado al equipo a seleccionar nuevos expositores que puedan sumar a esta nueva vision que se mostrara es un placer a anunciarles a nuestros seguidores la sumatoria de "Cesar Ortega", talvez lo conoces y si no te recomiendo estar presente en el evento.

# Escenario

Este APT inicia desde un acceso fisico en el ATM, este acceso es obtenido gracias a una vulnerabilidad encontrada en su chapa electronica que permite acceso ala parte blanda del ATM posteriormente conectando un hardware en el dispositivo y volviendo a cerrar el ATM podremos realizar un acceso al ATM abriendo la posibilidad a una dispensacion pero lo que se hara sera utilizarlo como punto de apoyo para empezar a realizar reconocmiento en la red financiera,
con esto presente se utilizara una tecnica de evasion de telemetria por drivers, accediendo al kernel para desactivar el EDR y empezar a jugar con la red, teniendo la persstencia realizada encontramos un AD con una mala implementacion ya que al dumpear los LSASS podemos ver que el usuario de soporte tecnico tiene el mismo hash en todos los ATMs permitiendonos una conexion remota a otros dispositivos, pero esto no nos da nada, hasta que en la red encontramos un administrador central que tiene doble interfaz permitiendo asi llegar a otra seccion.
en esta parte hay proyectos y cosas que pueden hacer perder el tiempo a cualquier persona pero buscamos nuevamente persistencia o estabilidad en un equipo, asi que jugando con el AD podemos hacernos de este y agregar algunas reglas para comprometer datos financieros importantes, dentro de nuestro despliegue hemos infectado mucha infraestructura para tener control completo y poder iniciar con la fase de post explotacion.

......

