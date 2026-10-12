# Fuentes personales — archivo local, no publicar

Se descargaron seis paquetes ZIP reales el 2026-10-12. No se modificó HTML, no se convirtieron las fuentes, no se realizó commit ni publicación. Los ZIP y archivos extraídos conservan sus bytes originales, nombres y licencias incluidas. Las páginas de procedencia se guardan como evidencia, no para ejecutarlas.

## Archivos

| Fuente | Original | ZIP | Español básico probado | OS/2 fsType |
|---|---|---|---|---|
| Hello Farmer | [hello farmer.otf](<hello-farmer-2/original/hello farmer.otf>) | [ZIP](<hello-farmer-2/hello-farmer-2.zip>) | Completo | 0: instalable |
| Baby Angella | [BabyAngella-Regular.ttf](<baby-angella/original/BabyAngella-Regular.ttf>) | [ZIP](<baby-angella/baby-angella.zip>) | Falta ¿ | 8: editable |
| Roklin | [Roklin.ttf](<roklin/original/Roklin.ttf>) | [ZIP](<roklin/roklin.zip>) | Completo | 4: previsualización/impresión |
| Homesweet | [Homesweet.otf](<homesweet/original/Homesweet.otf>) | [ZIP](<homesweet/homesweet.zip>) | Completo | 0: instalable |
| Richard Samuels | [Richard Samuels.otf](<richard-samuels/original/Richard Samuels.otf>) | [ZIP](<richard-samuels/richard_samuels.zip>) | Completo | 0: instalable |
| Super Cedar | [Super Cedar Personal Use.ttf](<super-cedar/original/Super Cedar Personal Use.ttf>) | [ZIP](<super-cedar/super-cedar.zip>) | Completo | 4: previsualización/impresión |

El [catálogo JSON](<catalog.json>) y el [catálogo JavaScript](<catalog.js>) contienen los mismos seis registros; el segundo define `window.LOCAL_FONT_CATALOG` para carga por script desde `file://`. Incluyen URL relativas a la raíz del proyecto (espacios codificados), weight=400, style=normal, procedencia, etiquetas de licencia, hashes SHA-256, cobertura, `missingSpanish` como array y restricciones. Respetar `embedding.integrationAllowed`: **Roklin está bloqueada**. Las otras cinco se habilitan por solicitud exclusivamente para uso local personal (`integrationScope: local-personal-only`), sin atribuir permiso de publicación o redistribución. El estado web sigue sin confirmar. Super Cedar permite técnicamente solo previsualización/impresión: no incrustar en documentos editables.

## Licencias y embedding

- **Hello Farmer**: demo exclusivamente personal; [nota del autor](<hello-farmer-2/source-text.txt>). El ZIP no incluye licencia separada.
- **Baby Angella**: demo exclusivamente personal, también indicado dentro del binario; [nota del autor](<baby-angella/source-text.txt>). No incluye licencia separada. El sitio violatype.com no resolvió durante la consulta.
- **Roklin**: [licencia original](<roklin/original/Note of the author.txt>) personal/demo. Las [condiciones del autor archivadas](<roklin/author-license.txt>), consultadas en [Sign Studio](https://www.signstd.com/licenses/), distinguen licencia Webfont para `@font-face` y Server para creación de diseños por usuarios; prohíben redistribución, modificación de bits de embedding y ciertos embeddings en software abierto. **No integrar esta demo en el generador.** Solicitar autorización/licencia adecuada al autor.
- **Homesweet**: [nota del autor](<homesweet/source-text.txt>) personal únicamente; prohíbe también promoción y uso comercial sin licencia y contacto previo. No incluye licencia separada.
- **Richard Samuels**: [ficha FontRiver archivada](<richard-samuels/source-text.txt>) indica uso personal. No incluye licencia separada; el binario reserva todos los derechos. La [página de licencias del autor](https://www.letterena.com/license) no expuso condiciones legibles en la respuesta HTML archivada; no se considera una autorización.
- **Super Cedar**: [README original](<super-cedar/original/README, PLEASE.txt>) permite solo uso personal. **Advertencia:** el dominio comercial allsuperfont.com del README devolvió contenido de apuestas durante la inspección. Se conserva el documento original, pero no se recomienda usar ese enlace para comprar una licencia.

`fsType` es una señal técnica de embedding en documentos, **no** sustituye la licencia, ni autoriza por sí solo webfonts, redistribución o integración en aplicaciones. Ningún binario tiene el bit Restricted License (0x0002), pero Roklin y Super Cedar limitan técnicamente embedding a previsualización/impresión. En las otras cinco no se encontró una prohibición web expresa en las notas disponibles, pero tampoco permiso web expreso: estado `not-confirmed`, no “prohibido” ni “autorizado”. No publicar, subir al repositorio, distribuir ni servir públicamente estos archivos; uso comercial o promocional requiere permisos adicionales.

## Verificación reproducible

El [informe técnico](<inspection.json>) conserva los campos de nombres/licencias, peso, fsType y cobertura extraídos. El [inspector](<inspect_fonts.py>) usa solo Python estándar y se ejecuta desde la raíz del proyecto:

```sh
python3 fonts/inspect_fonts.py
```

Cobertura: tablas Unicode `cmap` formatos 4/12, identificadores de glifo no nulos para `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÉÍÓÚÜÑáéíóúüñ¿¡`. Esto verifica presencia, no calidad visual, diacríticos combinantes ni corrección del contorno. Todos declaran variante Regular y peso 400; no se generan variantes sintéticas.

Cada entrada incluye el SHA-256 del binario y del ZIP; los archivos extraídos se compararon byte a byte con el ZIP. Se preservó toda la documentación incluida: solo los paquetes Roklin y Super Cedar traían notas externas. En cada subcarpeta se guarda `source.html` original y `source-text.txt` como transcripción auxiliar; las condiciones originales prevalecen sobre este resumen.
