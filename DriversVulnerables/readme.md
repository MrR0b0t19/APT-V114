# DRIVERS VULNERABLES

## ¿Qué es un driver?
En este caso un driver o un controlador en modo kernel, es un componente que nos permite la interacción con el hardware y memoria del equipo. 
Estos son usados cómo un traductor entre el hardware y el kernel, son usados principalmente para poder usar hardware cómo dispositivoas usb, para hardware como el stack de internet, etc.

## Pero... ¿por qué pueden ser vulnerables?
Al trabajar directamente a nivel kernel, los drivers tinene un nivel de privilegios "máxima", es decir trabajan a nivel NT-System. Si en algún driver existe algún error de desarrollo puede generar una vulnerabilidad y provocar que el atacante pueda escalar sus privilegios hasta ser NT-System

## Modo Usuario y Modo Kernel
Antes de dar a conocer drivers vulnerables, deseo explicar un poco sobre cómo funcionan y cómo es posible que sean vulnerables desde un punto de vista del desarrollo.

Existen dos modos en windows:
- Modo Usuario
- Modo Kernel

El modo usuario son todas aquellas aplicaciones con las cuales el usuario puede interactuar, estas tienen su propio espacio de memoria virtual con el cual trabajar y no afectan al sistema si alguna aplicación llega a fallar.

El modo kernel, los controladores, servicios y gestionamiento de recursos del equipo, funcionan solamente en kernel, y aquí hay una gran diferencia a las aplicaciones de modo usuario, estos comparten el mismo espacio y si existe algún error en la programación de algún componente en kernel, pueden generar un falla o el conocido "pantalla azul" (BSOD) y afectar al equipo.

## ¿Cómo se puede interactar entre Kernel y Espacio de Usuario?

En cierto punto, el usuario debe hacer uso del hardware ya sea para ingresar información o para poder hacer uso de este. Por ejemplo, ¿Cómo es que logramos ingresar información desde un teclado para que el usuario pueda escribir en pantalla? ¿Cómo es que podemos mover el cursor con nuestro mouse? ¿Incluso cómo es que nos llega los paquetes de internet por medio de nuestra tarjeta de red y sea direccionado a nuestro equipo para su respectiva aplicación en uso?

Para esto quiero explicar algo que se llama DeviceObjects. Estos son "Objetos" que usamos para comunicarnos a ciertos drivers por medio de "buffers" que pueden recibir.

Supongamos que tenemos nuestro driver:

>Este es código de un driver sencillo creado en el kit de desarrollo de windows de KMD en Visual Studio 2022. Dónde se puede compilar el código.


Este es el punto de entrada de nuestro driver, donde definiremos el objeto:

```Cpp 
// El punto de entrada del driver
extern "C"
NTSTATUS DriverEntry(PDRIVER_OBJECT  DriverObject, PUNICODE_STRING RegistryPath)
{

    ...

    return STATUS_SUCCESS; 
}
```

Primero asignamos rutinas al objeto del driver, en estre caso queda de la siguiente manera:

```Cpp
    DriverObject->MajorFunction[IRP_MJ_CREATE] =
        DriverObject->MajorFunction[IRP_MJ_CLOSE] = MySampleObjectCreateClose;

    DriverObject->MajorFunction[IRP_MJ_WRITE] = MySampleObjectWrite;
```

Donde se asigna una funcion de interrupción de creación y cierre, y por último uno de escritura. La rutina de escritura explicaremos más adelante cuál es su función.

Después creamos el objeto con la siguiente función ```IoCreateDevice``` que recibe ciertos parametros:
- El objeto del driver
- El nombre del objeto
- El tipo del obejto 
- El puntero al objeto

Nuestro código quedaría así:
```Cpp
    UNICODE_STRING devName = RTL_CONSTANT_STRING(L"\\Device\\MyDriver");

    PDEVICE_OBJECT DeviceObject;

    status = IoCreateDevice(
        DriverObject,
        0,
        &devName,
        FILE_DEVICE_UNKNOWN,
        0,
        FALSE,
        &DeviceObject
    );
```
Depués generamos el simbolo de enlace con el cual podremos comunicarnos desde un ejecutable:

```Cpp
    UNICODE_STRING symLink = RTL_CONSTANT_STRING(L"\\??\\MyDriver");

    status = IoCreateSymbolicLink(&symLink, &devName);
```


