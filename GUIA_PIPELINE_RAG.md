# Guía del pipeline RAG — NEXORA Legal

Resumen operativo del pipeline completo: descarga del corpus → generación de
documentos internos → indexación en ChromaDB (local o Cloud) → consumo desde
Flowise en clase.

---

## Arquitectura

```
  corpus_inventario.csv  ─┐
                          │
  PDFs públicos (web) ────┼──> descargar_corpus.py ──┐
                          │                           │
  generar_corpus_nexora_  │                           ├──> nexora_legal_corpus/
  legal.py ──> nexora_    │                           │    (66 PDFs + inventario)
  legal_interno/ ─────────┘                           │
                                                      │
                                                      ▼
                                        indexar_corpus.py
                                        (chunk + embed paralelo)
                                                      │
                         ┌────────────────────────────┴─────────────────────────┐
                         ▼                                                        ▼
             ChromaDB local                                        Chroma Cloud (SaaS)
             ./chroma_db/                                          api.trychroma.com
                         │                                                        │
                         └────────────────────┬───────────────────────────────────┘
                                              ▼
                                      Flowise (RAG + chat)
                                      → consumido por alumnos
```

## Ficheros del proyecto

| Fichero | Rol |
|---|---|
| [corpus_inventario.csv](corpus_inventario.csv) | Inventario maestro con URLs, metadatos y tipo de descarga de cada documento |
| [descargar_corpus.py](descargar_corpus.py) | Descarga los PDFs web y copia los locales al destino |
| [generar_corpus_nexora_legal.py](generar_corpus_nexora_legal.py) | Genera los 4 PDFs internos ficticios de NEXORA (reportlab) |
| [indexar_corpus.py](indexar_corpus.py) | Trocea, embebe en paralelo (OpenAI + Ollama) e indexa en ChromaDB |
| [nexora_legal_corpus/](nexora_legal_corpus/) | Corpus final: 98 PDFs + `corpus_resultados.csv` |
| [nexora_legal_interno/](nexora_legal_interno/) | Fuente de los 4 PDFs internos (reutilizable en re-ejecuciones) |

---

## Setup inicial (una vez)

### 1. Dependencias Python

```powershell
pip install requests tqdm reportlab
pip install langchain langchain-community langchain-text-splitters langchain-openai langchain-ollama langchain-chroma chromadb pypdf
```

### 2. Ollama con modelo de embeddings

```powershell
ollama pull nomic-embed-text
# ollama serve ya corre como servicio por defecto
```

### 3. Variables de entorno

En PowerShell, para la sesión actual:

```powershell
$env:OPENAI_API_KEY  = "sk-..."
$env:CHROMA_API_KEY  = "ck-..."        # solo para modo cloud
$env:CHROMA_DATABASE = "nexora-legal"  # solo para modo cloud
```

Persistentes (toda nueva terminal las verá):

```powershell
setx OPENAI_API_KEY "sk-..."
setx CHROMA_API_KEY "ck-..."
setx CHROMA_DATABASE "nexora-legal"
```

---

## Flujo completo

### Paso 1 — Generar los 4 PDFs internos

```powershell
python .\generar_corpus_nexora_legal.py
```

Salida por defecto: `./nexora_legal_interno/` con:
- `01_NEXORA_Protocolo_Cumplimiento_Normativo_v3.2.pdf`
- `02_AI_Act_Resumen_Ejecutivo.pdf`
- `03_RGPD_Derechos_Interesado_Extracto.pdf`
- `04_NEXORA_Politica_Proveedores_Subcontratacion.pdf`

Idempotente: sobrescribe si se vuelve a lanzar.

### Paso 2 — Descargar el corpus público + copiar los internos

```powershell
python .\descargar_corpus.py --skip-existing --local-docs-dir .\nexora_legal_interno
```

- `--skip-existing`: no re-descarga lo que ya está.
- `--local-docs-dir`: dónde buscar los PDFs tipo `local` del inventario.

Genera `./nexora_legal_corpus/` con todos los PDFs numerados + `corpus_resultados.csv`.

### Paso 3 — Indexar (local, para desarrollo)

```powershell
python .\indexar_corpus.py
```

Salida en `./chroma_db/` con dos colecciones:
- `nexora_legal_openai` (text-embedding-3-small, 1536 dim)
- `nexora_legal_ollama` (nomic-embed-text, 768 dim)

Metadatos por chunk: `source_file`, `page`, `chunk_index`, `chunk_id`,
`id`, `titulo`, `capa`, `categoria`, `fuente`. Suficiente para citas precisas
y filtros por capa legal en Flowise.

Flags útiles:

```powershell
python .\indexar_corpus.py --only ollama              # solo uno
python .\indexar_corpus.py --openai-model large       # 3-large en vez de small
python .\indexar_corpus.py --reset                    # borra colecciones antes
python .\indexar_corpus.py --chunk-size 1500 --chunk-overlap 300
```

### Paso 4 — Indexar en Chroma Cloud (para la clase)

```powershell
python .\indexar_corpus.py --mode cloud
```

Requiere `CHROMA_API_KEY` y (opcional) `CHROMA_TENANT` + `CHROMA_DATABASE`
en el entorno. El preflight falla rápido si la auth está mal, sin gastar
créditos.

### Paso 5 — Conectar Flowise

En el nodo **Chroma** de Flowise:

| Campo | Valor local | Valor cloud |
|---|---|---|
| Collection Name | `nexora_legal_openai` o `nexora_legal_ollama` | igual |
| Chroma URL | `http://localhost:8000` (requiere `chroma run`) | `https://api.trychroma.com` |
| Chroma API Key | — | `ck-...` |
| Tenant | — | tu tenant UUID |
| Database | — | `nexora-legal` |

Para queries: usar el mismo modelo de embeddings que se usó al indexar
(la colección `_openai` con `text-embedding-3-small`, la `_ollama` con
`nomic-embed-text`). Mezclar rompe la búsqueda.

---

## Decisión de deploy: Chroma Cloud

Evaluadas 6 opciones. Elegida **Chroma Cloud Starter**:

- **Coste real**: <$0.50 para todo el ciclo (indexado + ~300 queries de clase).
  Cubierto por los $5 de crédito gratuitos al registrarse.
- **Setup**: 5 min (signup + copiar API key).
- **Mantenimiento**: cero.
- **Compatibilidad**: `chromadb.CloudClient` + `langchain-chroma` nativo.
  Flowise usa el mismo patrón.
- **BYOE**: acepta embeddings OpenAI y Ollama sin reconversión.

**Gotchas asumidos**:

1. Solo región us-east-1 (Virginia). ~100 ms RTT desde España. Para <300
   queries en 2 h es irrelevante.
2. No hay import directo del `./chroma_db/` local; hay que reindexar remoto.
   Coste del write inicial: ~$0.38.
3. Docs aún "alpha" en algunos detalles del SDK.

**Alternativa descartada**: Railway self-hosted ($5/mes, region EU). Gana
en latencia pero pierde en coste y mantenimiento. Solo compensaría si la
residencia EU de datos fuera un requisito.

---

## Estado del corpus (a 2026-04-20)

- **98 PDFs** en `./nexora_legal_corpus/` tras las correcciones.
- **12 fallos originales corregidos**:
  - 4 NEXORA renombrados (nombres cortos en `nexora_legal_corpus/`, prefijo
    `01_`–`04_` en `nexora_legal_interno/`).
  - UNESCO con doble extensión corregido.
  - 5 placeholders de descargas HTML borrados (IDs 23, 48, 49, 50, 73).
  - 7 URLs actualizadas en `corpus_inventario.csv` con fallbacks:
    23 (BOE), 48/49/50 (EDPB WP260/242/248), 73 (APDCAT mirrors),
    78 (RD 817/2023), 92 (BSI ISO 42001).
- **Documento ID 73 (APDCAT)**: la versión castellana ya no está en el
  portal oficial — usamos mirrors no institucionales. Valorar sustituir
  por la guía AEPD equivalente (IDs 28/45) si la procedencia preocupa.

---

## Cheatsheet

```powershell
# Regenerar PDFs NEXORA
python .\generar_corpus_nexora_legal.py

# Completar descargas pendientes
python .\descargar_corpus.py --skip-existing --local-docs-dir .\nexora_legal_interno

# Indexar en local (desarrollo)
python .\indexar_corpus.py

# Indexar en Chroma Cloud (clase)
python .\indexar_corpus.py --mode cloud

# Reindexar desde cero (local o cloud)
python .\indexar_corpus.py --mode cloud --reset

# Solo un proveedor de embeddings
python .\indexar_corpus.py --only ollama
python .\indexar_corpus.py --only openai --openai-model large
```

---

## Troubleshooting

| Síntoma | Causa probable | Fix |
|---|---|---|
| `pip .\script.py` → ERROR unknown command | `pip` instala paquetes, no ejecuta | Usar `python .\script.py` |
| Descarga marca `FAIL` con archivo de pocos KB | URL devolvió HTML de error | Borrar el archivo y actualizar URL en `corpus_inventario.csv` |
| `OPENAI_API_KEY no está definida` | Env var no exportada en la shell actual | `$env:OPENAI_API_KEY = "sk-..."` o `--only ollama` |
| Preflight Ollama falla | Ollama no corre o falta el modelo | `ollama pull nomic-embed-text` |
| Chroma Cloud 401 | API key inválida o expirada | Regenerar en dashboard y reexportar `CHROMA_API_KEY` |
| Flowise no encuentra documentos | Usando embeddings distintos a los de indexación | Alinear modelo de embeddings del nodo con la colección (`_openai` ↔ 3-small, `_ollama` ↔ nomic) |

---

## Próximos pasos

1. Lanzar indexación local y validar conteo de chunks.
2. Registrarse en Chroma Cloud, crear database `nexora-legal`, copiar API key.
3. Reindexar con `--mode cloud`.
4. Montar el flujo en Flowise apuntando a la colección cloud.
5. Compartir con los alumnos: URL de Flowise + (si aplica) API key read-only
   de Chroma Cloud.
