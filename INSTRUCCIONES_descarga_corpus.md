# Instrucciones para ejecutar la descarga del corpus NEXORA Legal

## Contexto

Este script descarga ~66 documentos legales públicos (legislación UE y española, guías de la AEPD, directrices del EDPB, frameworks internacionales) más 4 documentos internos ficticios de NEXORA que ya generamos previamente. El corpus alimentará un RAG montado en Flowise para la sesión S5 del máster IASP (UNIR).

## Pre-requisitos

```bash
pip install requests tqdm
```

## Pasos

### 1. Asegúrate de que los 4 PDFs internos de NEXORA están accesibles

Los PDFs generados previamente deben estar en el directorio desde el que ejecutes el script (o en `~/nexora_legal_corpus/`):

```
01_NEXORA_Protocolo_Cumplimiento_Normativo_v3.2.pdf
02_AI_Act_Resumen_Ejecutivo.pdf
03_RGPD_Derechos_Interesado_Extracto.pdf
04_NEXORA_Politica_Proveedores_Subcontratacion.pdf
```

Si no los tienes, el script los reportará como `NOT_FOUND` y puedes generarlos después con el script `generar_corpus_nexora_legal.py`.

### 2. Ejecutar la descarga

```bash
python descargar_corpus_nexora.py --output-dir ./nexora_legal_corpus
```

**Opciones útiles:**

```bash
# Si se interrumpe y quieres continuar sin re-descargar:
python descargar_corpus_nexora.py --output-dir ./nexora_legal_corpus --skip-existing

# Si los docs NEXORA están en otro directorio:
python descargar_corpus_nexora.py --nexora-docs-dir ~/Desktop/nexora_docs
```

**Duración estimada:** 5-15 minutos dependiendo de la velocidad de conexión. EUR-Lex y BOE pueden ser lentos.

### 3. Revisar el resultado

El script genera un `corpus_inventario.csv` con el estado de cada descarga. Revisa los `FAIL` — algunas URLs pueden haber cambiado y necesitarán descarga manual.

### 4. Si hay fallos

Es normal que 5-10 URLs fallen (redirecciones, cambios de servidor). Para cada fallo:
- Busca el documento en Google: `"nombre del documento" filetype:pdf`
- Descárgalo manualmente y ponlo en `./nexora_legal_corpus/` con el nombre que indica el inventario.

### 5. Siguiente paso: indexación en ChromaDB

Una vez descargado el corpus, indexarlo con el script de indexación:

```bash
# Con OpenAI (más rápido, ~$0.05 de coste):
python indexar_corpus_nexora.py --provider openai --corpus-dir ./nexora_legal_corpus

# Con Ollama (gratis, 15-30 min):
python indexar_corpus_nexora.py --provider ollama --corpus-dir ./nexora_legal_corpus
```

*(El script de indexación se genera como paso siguiente)*

## Notas sobre URLs

- **EUR-Lex** usa el patrón: `https://eur-lex.europa.eu/legal-content/ES/TXT/PDF/?uri=CELEX:{numero}`
- **BOE** usa: `https://www.boe.es/buscar/pdf/{year}/BOE-A-{year}-{number}-consolidado.pdf`
- **AEPD** usa: `https://www.aepd.es/guias/{slug}.pdf`
- **EDPB** tiene URLs menos predecibles — algunas van a `ec.europa.eu/newsroom/`, otras a `edpb.europa.eu/sites/default/files/`

Si alguna URL de EUR-Lex falla, prueba a ir a `eur-lex.europa.eu`, buscar el número CELEX y descargar el PDF en español manualmente. Son documentos públicos siempre accesibles, solo cambian las URLs de vez en cuando.

## Estructura final esperada

```
nexora_legal_corpus/
├── 01_RGPD_Reglamento_UE_2016_679.pdf
├── 02_AI_Act_Reglamento_UE_2024_1689.pdf
├── ...
├── 62_WEF_Future_AI_Enabled_Health_2025.pdf
├── 63_NEXORA_Protocolo_Cumplimiento_Normativo_v3.2.pdf
├── 64_NEXORA_AI_Act_Resumen_Ejecutivo.pdf
├── 65_NEXORA_RGPD_Derechos_Interesado.pdf
├── 66_NEXORA_Politica_Proveedores_v2.1.pdf
└── corpus_inventario.csv
```
