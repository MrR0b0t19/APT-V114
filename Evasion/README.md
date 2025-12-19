# Documentacion & Scripts

Para la evasion utilizaremos un loader personalizado escrito en C, el cual carga una shellcode encriptada con XOR y la carga en memoria, como estamos utilizando una shellcode, podemos usar (pero no se limita) a un implante de Sliver, por ejemplo. Tambien podemos hacer uso de donut (https://github.com/TheWover/donut) para convertir un ejecutable como Rubeus en formato de shellcode y ejecutarlo con el mismo loader. En caso de que nuestro loader empiece a ser detectado por el AV (eventualmente lo será) tendremos que aplicar tecnicas de ofuscacion en el codigo fuente para evadir las firmas estaticas.

### MITRE ATT&CK

-T1055 Process Injection

-T1620 Reflective Code Loading

-T1027 Obfuscated Files or Information

-T1140 Deobfuscate/Decode Files or Information

-T1059 Command and Scripting Interpreter

-T1106 Native API
