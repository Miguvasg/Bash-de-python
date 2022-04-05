## Ejecutar fichero de Python

Al usar "#!/usr/bin/python" en la primera línea del script, el fichero hello.py ahora se puede ejecutar con "./hello.py", sin tener que escribir "python hello.py", esto nos ayudará para crear el comando bash con mayor facilidad.

## Crear un bash para el script

Debes copiar el fichero en una ubicación que se desee siempre que esta se encuentre dentro de los directorios de PATH, este comando mostrará las rutas donde se puede copiar el script para que se pueda ejecutar desde cualquier directorio. Al escribir un comando bash, linux buscará dentro de los directorios que están en PATH, por este motivo es que vamos a copiar el fichero en alguno de estos directorios.

```bash
echo $PATH
sudo cp hello.py /usr/local/bin/
```

NOTA: normalmente los script propios se guardan en "/usr/local/bin".

Después debes crear el link simbólico, con esto al usar el comando "prueba", se ejecutará el script hello.py. Ten cuidado con colocar el formato "./hello.py" para que el fichero se ejecute sin usar el comando "python".

```bash
sudo ln -s /usr/local/bin/./hello.py /usr/local/bin/prueba
```

## Eliminar links simbólicos

Si ya no requieres este link lo puedes eliminar de la siguiente manera:

```bash
sudo unlink /usr/local/bin/prueba
```

NOTA: no olvides eliminar el fichero "hello.py" si ya no lo necesitas.