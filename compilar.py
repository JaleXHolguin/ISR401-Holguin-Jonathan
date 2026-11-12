import argparse
import os
from pathlib import Path
import platform
import subprocess
import tempfile
from urllib.request import urlretrieve
from zipfile import BadZipFile, ZipFile


VERSION = "0.17.0"
URL = (
    "https://github.com/tectonic-typesetting/tectonic/releases/download/"
    f"tectonic%40{VERSION}/tectonic-{VERSION}-x86_64-pc-windows-msvc.zip"
)


def preparar_tectonic():
    carpeta = Path(os.environ["LOCALAPPDATA"]) / "Tectonic" / VERSION
    ejecutable = carpeta / "tectonic.exe"
    if ejecutable.is_file():
        return ejecutable

    print(f"Descargando Tectonic {VERSION}...", flush=True)
    carpeta.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=carpeta) as temporal:
        archivo = Path(temporal) / "tectonic.zip"
        urlretrieve(URL, archivo)
        with ZipFile(archivo) as zip_tectonic:
            extraido = Path(zip_tectonic.extract("tectonic.exe", temporal))
        extraido.replace(ejecutable)
    return ejecutable


def main():
    informe = Path(__file__).resolve().parent / "FORM-PC-01"
    parser = argparse.ArgumentParser(description="Compila FORM-PC-01/main.tex.")
    parser.add_argument(
        "--salida",
        type=Path,
        default=informe,
        help="Carpeta donde se genera main.pdf (por defecto, FORM-PC-01).",
    )
    opciones = parser.parse_args()

    if platform.system() != "Windows" or platform.machine().upper() not in {"AMD64", "X86_64"}:
        parser.error("Este script requiere Windows x64.")
    if not (informe / "main.tex").is_file():
        parser.error("No se encontró FORM-PC-01/main.tex.")

    try:
        print("Comprobando Tectonic...", flush=True)
        tectonic = preparar_tectonic()
        subprocess.run([tectonic, "--version"], check=True)
        salida = opciones.salida.resolve()
        salida.mkdir(parents=True, exist_ok=True)
        resultado = subprocess.run(
            [tectonic, "--outdir", salida, "main.tex"], cwd=informe
        )
    except (OSError, BadZipFile, subprocess.CalledProcessError) as error:
        parser.exit(1, f"No se pudo compilar el informe: {error}\n")

    return resultado.returncode


if __name__ == "__main__":
    raise SystemExit(main())
