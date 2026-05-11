# APT Sobre instituciones financieras

Este paper posiblemente se de una unica vez en mexico, se esta preparando la documentacion extensa sobre la informacion tecnica bajo /APT-V114/Paper/2027. 

# Nuevo giro

Nuevamente como sabras, el equipo trabaja en conjunto para una seleccion de tecnicas actualizadas para que la audiencia ademas de llevarse una tecnica tengan las capacidades de poder utilizarlas para sus pruebas propias
este giro a llevado al equipo a seleccionar nuevos expositores que puedan sumar a esta nueva vision que se mostrara es un placer a anunciarles a nuestros seguidores la sumatoria de "Cesar Ortega", talvez lo conoces y si no te recomiendo estar presente en el evento.

# Escenario

Este APT inicia desde un acceso fisico en el ATM, este acceso es obtenido gracias a una vulnerabilidad encontrada en su chapa electronica que permite acceso ala parte blanda del ATM posteriormente conectando un hardware en el dispositivo y volviendo a cerrar el ATM podremos realizar un acceso al ATM abriendo la posibilidad a una dispensacion pero lo que se hara sera utilizarlo como punto de apoyo para empezar a realizar reconocmiento en la red financiera,
con esto presente se utilizara una tecnica de evasion de telemetria por drivers, accediendo al kernel para desactivar el EDR y empezar a jugar con la red, teniendo la persstencia realizada encontramos un AD con una mala implementacion ya que al dumpear los LSASS podemos ver que el usuario de soporte tecnico tiene el mismo hash en todos los ATMs permitiendonos una conexion remota a otros dispositivos, pero esto no nos da nada, hasta que en la red encontramos un administrador central que tiene doble interfaz permitiendo asi llegar a otra seccion.
en esta parte hay proyectos y cosas que pueden hacer perder el tiempo a cualquier persona pero buscamos nuevamente persistencia o estabilidad en un equipo, asi que jugando con el AD podemos hacernos de este y agregar algunas reglas para comprometer datos financieros importantes, dentro de nuestro despliegue hemos infectado mucha infraestructura para tener control completo y poder iniciar con la fase de post explotacion.

# Tecnicas

- Ataque a chapa inteligente de BLE (apertura de ATM)
- Ataque DMA (persistencia y ejecucion de beacon)
- Contacto inicial - Persistencia/deshabilitacion de defensas
- Dump de lsass / Contacto con AD
- movimiento en AD - Compromiso a todos los ATMs
- Phishing corporativo para AD
- Piviting a red corporativa
- beacons/cargas - persistencia/estabilidad
- post-explotacion

# Agenda


| Hora           | Charla                                                                 | Ponente(s)                  |
|----------------|------------------------------------------------------------------------|-----------------------------|
| 9:50 - 10:20   | Iniciación de la Villa, apertura del escenario de ataque              | —                           |
| 10:20 - 11:10  | Hacking SmartLock for fun and profit                                  | Cesar Ortega                |
| 11:20 - 12:00  | DMA Attack en ATMs                                                    | Arnold Morales              |
| 12:10 - 1:40   | Hookchain with beacon                                                 | Diego Hernandez             |
| 12:10 - 1:40   | Persistencia con Driver vulnerables                                   | Adonai Diaz / Arnold Morales|
| 1:40 - 2:10    | Comida                                                                | —                           |
| 2:20 - 3:40    | DACL - La verdad sobre el enterprise / comprometiendo AD              | Tierno / Hokma / Sky blue   |
| 3:50 - 4:30    | BOF / PICs / UDRL SLEEPMASK - Cuales son tus mejores cartas?          | Bdragon / Hokma / Donuts    |
| 4:40 - 5:40    | El despliegue verdadero de un APT (no todo es lo que ves en reels)    |  Héctor Espino              |
| 5:40 - 6:00    | Dinámicas / Premios / Regalos / Cierre de la Villa                    | —                           |

(Los horarios pueden variar)

---

ESTA AGENDA ES PARA EL DIA MAS IMPORTANTE DEL EVENTO, SI SON DOS DIAS ACTUALIZAMOS AL PRIMER DIA MOSTRAR "WORKSHOPS"

los siguientes temas estaran presente en los workshops que tendran una duracion de 60-90 min, en los que se enseñara las bases de cualquier tecnica se explicara codigo y se compartira con la audiencia para sus futuras pruebas.

lista: 

- UDRL Sleepmasks for dummies
- Telemetria, Kernel y evasion
- Drivers vulnerables
- evasion de EDR con hookchain
- BOF develpment
- Active Directory 101
- My first Bootkit
- DMA avanzado
- Buscando deserializaciones
- My first EDR - hook
- Flipper Zero for dummies
- Hardware?, como diseñar mi ADDON..
- Kerberoasting
- Ing Social para red team
- My firts jammer BLE

Estos workshops se iran rotando, se hara encuesta en nuestro instagram para seleccionar los workshop del dia por evento se buscara dar minimo 5 workshop. 

**Si tienes un tema de investigacion que quieras compartir enviame mensaje**




Aqui existiran dinamicas para los que quieran participar en la villa, ademas de el codigo y aprendizaje se rifara un premio central

Los papers de cada workshop seran publicados en este repo.
