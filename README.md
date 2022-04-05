## Ejecutar fichero de Python

El fichero hello.py ahora se puede ejecutar con "./hello.py", sin tener que escribir "python hello.py"

## Crear un bash para el script

Copiar el ficher en una ubicación que se desee, pero que esté dentro de PATH, este comando mostrará las rutas
donde se puede copiar el script y este se ejecutará desde cualquier directorio.

```bash
echo $PATH
sudo cp hello.py /usr/local/bin/
```

NOTA: normalmente los script propios se guardan en "/usr/local/bin".

Después crer el link simbólico, con esto al usar el comando prueba, se ejecutará el script hello.py. Ojo con
colocar el formato "./hello.py" para que el fichero se ejecute sin usar el comando "python".

```bash
sudo ln -s /usr/local/bin/./hello.py /usr/local/bin/prueba
```

## Eliminar links simbólicos

Para eliminar el link:

```bash
sudo unlink /usr/local/bin/prueba
```

No olvides eliminar el ficher "hello.py" si ya no lo necesitas.