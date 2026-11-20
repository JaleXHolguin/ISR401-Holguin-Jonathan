# Manifiesto de evidencias privadas

**Actividad:** GA-TL-02-FORM — Taller de entrevista estructurada y design thinking aplicados al PFC.

**Proyecto:** UteqFit-AI.

## Ubicación y acceso

**Enlace al archivo de audio en Drive:** [ensayo-entrevista.mp3](https://drive.google.com/file/d/1TBWic82GbG8VxHKJ1xuM99Cfca1e_DZw/view?usp=sharing).

**Acceso del docente:** PENDIENTE: confirmar que el archivo esté compartido con su correo institucional y mantenga el acceso restringido.

El audio se almacena en Drive y debe mantenerse con acceso restringido. Este repositorio contiene únicamente su registro de identificación y verificación.

## Registro del audio

| Campo | Valor |
| --- | --- |
| Identificador | AUD-01 |
| Archivo | `ensayo-entrevista.mp3` |
| Descripción | Audio del ensayo de la entrevista estructurada mediante juego de roles. |
| Fecha del ensayo | 20 de noviembre de 2026 |
| Duración | 00:07:45.672 (7 minutos y 45.672 segundos, según los metadatos del archivo). |
| Tamaño | 7 450 906 bytes |
| Algoritmo de verificación | SHA-256 |
| Huella SHA-256 | `5AF52C6F575D6702070A815A76CD870FDF87BC796D5F9084914D28A8DED9DED4` |
| Consentimiento | Se solicitó verbalmente antes de iniciar la entrevista mediante la pregunta reproducida a continuación. |

## Solicitud de consentimiento

Antes de la entrevista se formuló la siguiente solicitud:

> Puedes omitir cualquier pregunta o detener la entrevista cuando quieras. Si das algún ejemplo, evita mencionar nombres o datos que identifiquen a otras personas. ¿Estás de acuerdo en participar y en que grabemos únicamente el audio?

## Verificación del archivo

Para comprobar que el archivo privado coincide con el registrado, ejecutar en PowerShell desde la carpeta donde se encuentre el audio:

```powershell
Get-FileHash -LiteralPath '.\ensayo-entrevista.mp3' -Algorithm SHA256
```

El resultado debe coincidir con la huella indicada. Si el audio se edita o se vuelve a codificar, se debe calcular su nueva huella y actualizar este registro.
