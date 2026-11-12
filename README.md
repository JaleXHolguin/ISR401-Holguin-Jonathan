# ISR401-Holguin-Jonathan

## Compilar FORM-PC-01

Requisito: Python 3 instalado en Windows x64.

Abrir una terminal en la carpeta raíz del repositorio, donde está `compilar.py`, y ejecutar:

```powershell
py compilar.py
```

El script comprueba si Tectonic 0.17.0 está disponible y lo descarga si hace falta. La primera compilación requiere conexión a internet para descargar el compilador y los paquetes de LaTeX. Después compila `FORM-PC-01/main.tex` y guarda el PDF en `FORM-PC-01/main.pdf`.

Para generar el PDF en otra carpeta, **usar** `--salida`.

```powershell
py compilar.py --salida revision
```
