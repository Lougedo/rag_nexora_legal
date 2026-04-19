# Corpus NEXORA Legal Compliance — Diseño y justificación

## Por qué la opción 3 (corpus curado mixto) y por qué ampliado

### El problema con las opciones descartadas

**Opción 1 — Privacy Law Corpus (1.043 leyes, 183 jurisdicciones)** se descartó porque:

- La mayoría de documentos están en inglés o son traducciones automáticas de calidad irregular.
- Incluye leyes de jurisdicciones irrelevantes para una empresa española (ley de privacidad de Nigeria, regulación de protección de datos de Tailandia...). Cuando el alumno pregunte al RAG, recibirá chunks de jurisdicciones aleatorias mezclados con lo relevante — esto ensucia las respuestas y dificulta entender el valor real del sistema.
- No incluye guías prácticas ni documentación de interpretación, solo textos legales puros. Un departamento legal real no trabaja solo con la ley; trabaja con la ley *más* la guía de la autoridad de control que explica cómo aplicarla.
- El volumen bruto impresiona (1.043 PDFs) pero no aporta calidad de respuesta para el caso NEXORA.

**Opción 2 — Solo textos oficiales BOE/EUR-Lex** se descartó porque:

- Son pocos documentos (5-8), muy densos pero insuficientes para demostrar el potencial de escala.
- Sin las guías de interpretación de la AEPD, el RAG responde citando artículos legales crudos que un perfil no jurídico no entiende.
- No refleja cómo trabaja un equipo de compliance real: siempre se consultan las guías prácticas junto con la norma.

### Por qué la opción 3 ampliada es la correcta

La opción 3 replica **exactamente** lo que haría un equipo de compliance real al montar un RAG para su empresa:

1. **Textos legales primarios** — las normas que te obligan (RGPD, LOPDGDD, AI Act, NIS2...).
2. **Guías de interpretación oficiales** — cómo la autoridad competente (AEPD, EDPB, Comisión Europea) dice que debes aplicar esa norma.
3. **Documentación sectorial y técnica** — informes, frameworks y estándares que orientan la implementación.
4. **Documentación interna de la empresa** — protocolos, políticas de proveedores, registros de tratamiento.

Este enfoque por capas tiene valor pedagógico directo: cuando un alumno pregunte *"¿Necesito hacer una evaluación de impacto para el sistema de cribado de CVs?"*, el RAG podrá responder combinando el artículo 35 del RGPD (capa 1), la guía de la AEPD sobre evaluaciones de impacto (capa 2), y el protocolo interno de NEXORA que dice que sí, que ya está en marcha (capa 4). Eso es un RAG útil, no un buscador de PDFs.

**¿Y por qué ampliar el volumen?** Porque el coste de descargar 100 PDFs en vez de 10 es idéntico con un script automatizado, y el efecto en clase es muy distinto: cuando ven que el ChromaDB tiene **150+ documentos y más de 8.000 páginas indexadas**, entienden que esto escala. Con 5 PDFs parece un juguete. Con 150 parece una herramienta real.

Además, un corpus más grande genera respuestas más ricas y con más matices. El RAG puede cruzar información entre una guía de la AEPD sobre transferencias internacionales y la política de proveedores de NEXORA que lista los proveedores con datos fuera de la UE. Eso no pasa con 5 documentos.

---

## Inventario del corpus

### Capa 1 — Legislación primaria (UE + España)

Fuentes: EUR-Lex (PDF en español), BOE (PDF consolidado).

| # | Documento | Fuente | Págs aprox | Idioma |
|---|---|---|---|---|
| 1 | **Reglamento (UE) 2016/679 — RGPD** | EUR-Lex | 88 | ES |
| 2 | **Reglamento (UE) 2024/1689 — AI Act** | EUR-Lex | 144 | ES |
| 3 | **Directiva (UE) 2022/2555 — NIS2** (ciberseguridad) | EUR-Lex | 73 | ES |
| 4 | **Reglamento (UE) 2019/881 — Cybersecurity Act** | EUR-Lex | 45 | ES |
| 5 | **Reglamento (UE) 2024/2847 — Cyber Resilience Act** | EUR-Lex | 120 | ES |
| 6 | **Directiva (UE) 2016/680** — protección de datos en ámbito penal | EUR-Lex | 43 | ES |
| 7 | **Reglamento (UE) 2018/1725** — protección de datos en instituciones UE | EUR-Lex | 60 | ES |
| 8 | **Reglamento (UE) 2022/868 — Data Governance Act** | EUR-Lex | 47 | ES |
| 9 | **Reglamento (UE) 2023/2854 — Data Act** | EUR-Lex | 72 | ES |
| 10 | **Directiva (UE) 2019/1024 — Open Data** | EUR-Lex | 26 | ES |
| 11 | **Reglamento (UE) 2022/2065 — Digital Services Act (DSA)** | EUR-Lex | 100 | ES |
| 12 | **Reglamento (UE) 2022/1925 — Digital Markets Act (DMA)** | EUR-Lex | 68 | ES |
| 13 | **Reglamento (UE) 2023/1114 — MiCA** (criptoactivos) | EUR-Lex | 149 | ES |
| 14 | **Directiva 2002/58/CE — ePrivacy** (comunicaciones electrónicas) | EUR-Lex | 18 | ES |
| 15 | **Reglamento (UE) 910/2014 — eIDAS** (identificación electrónica) | EUR-Lex | 42 | ES |
| 16 | **LO 3/2018 — LOPDGDD** | BOE | 70 | ES |
| 17 | **LO 7/2021** — protección datos ámbito penal (transposición DIR 2016/680) | BOE | 40 | ES |
| 18 | **Ley 34/2002 — LSSI-CE** (servicios sociedad información) | BOE | 30 | ES |
| 19 | **Ley 2/2023** — canal de denuncias (whistleblowing) | BOE | 35 | ES |
| 20 | **RD 311/2022 — Esquema Nacional de Seguridad (ENS)** | BOE | 55 | ES |
| 21 | **Ley 11/2022 — Ley General de Telecomunicaciones** | BOE | 90 | ES |
| 22 | **Código electrónico BOE: Protección de Datos de Carácter Personal** | BOE | ~300 | ES |

**Subtotal Capa 1: ~22 documentos, ~1.700 páginas estimadas**

---

### Capa 2 — Guías de interpretación y orientaciones oficiales

Fuentes: AEPD (aepd.es/guias), EDPB/CEPD, Comisión Europea, ENISA, AESIA.

**Guías AEPD (descarga directa PDF desde aepd.es):**

| # | Documento | Págs aprox |
|---|---|---|
| 23 | Guía para el cumplimiento del deber de informar | 30 |
| 24 | Guía para responsables de tratamiento | 45 |
| 25 | Directrices para la elaboración de contratos entre responsables y encargados | 25 |
| 26 | Guía práctica de análisis de riesgos en tratamientos de datos personales | 55 |
| 27 | Guía práctica para las evaluaciones de impacto (EIPD) | 50 |
| 28 | Guía de protección de datos por defecto | 50 |
| 29 | Guía de protección de datos desde el diseño | 40 |
| 30 | Listado de tipos de tratamientos que requieren EIPD (art. 35.4) | 8 |
| 31 | Guía sobre el uso de cookies | 35 |
| 32 | Guía sobre transferencias internacionales de datos | 40 |
| 33 | Guía del Delegado de Protección de Datos | 35 |
| 34 | Guía para la gestión y notificación de brechas de seguridad | 45 |
| 35 | Guía sobre legitimación del interés legítimo | 30 |
| 36 | Guía de privacidad y seguridad en Internet (AEPD + INCIBE) | 55 |
| 37 | Guía para el ciudadano sobre protección de datos | 20 |
| 38 | Orientaciones sobre cookies y analítica en portales de AAPP | 15 |
| 39 | Orientaciones sobre tratamientos entre AAPP (comunicación de datos) | 20 |
| 40 | Orientaciones EIPD en desarrollo normativo | 15 |
| 41 | Adecuación al RGPD de tratamientos que incorporan IA | 40 |
| 42 | Requisitos para auditorías de tratamientos que incluyen IA | 30 |
| 43 | IA agéntica desde la perspectiva de la protección de datos (2025) | 25 |
| 44 | Informe sobre aprendizaje federado | 20 |
| 45 | Guía de protección de datos en relaciones laborales | 50 |
| 46 | Guía sobre videovigilancia | 35 |
| 47 | Guía sobre protección de datos de menores | 30 |
| 48 | K-anonimidad y protección de datos | 15 |
| 49 | Introducción al hash como técnica de pseudonimización | 10 |
| 50 | Guía de compra segura en Internet (AEPD + INCIBE + Aecosan) | 20 |

**Guías EDPB/CEPD (disponibles en edpb.europa.eu, en español):**

| # | Documento | Págs aprox |
|---|---|---|
| 51 | Directrices sobre DPO (Delegado de Protección de Datos) WP243 rev.01 | 30 |
| 52 | Directrices sobre consentimiento WP259 rev.01 | 35 |
| 53 | Directrices sobre transparencia WP260 rev.01 | 40 |
| 54 | Directrices sobre portabilidad de datos WP242 rev.01 | 20 |
| 55 | Directrices sobre evaluaciones de impacto WP248 rev.01 | 25 |
| 56 | Directrices sobre notificación de brechas de seguridad WP250 rev.01 | 35 |
| 57 | Directrices sobre transferencias internacionales de datos — post-Schrems II | 30 |
| 58 | Directrices sobre videovigilancia | 25 |
| 59 | Directrices sobre derecho de acceso (1/2022) | 45 |
| 60 | Directrices sobre dark patterns en interfaces de redes sociales (3/2022) | 40 |

**Documentación sobre AI Act (Comisión Europea y otros):**

| # | Documento | Págs aprox |
|---|---|---|
| 61 | AI Act — Guidelines on prohibited AI practices (Comisión, jul 2025) | 50 |
| 62 | AI Act — Guidelines on GPAI models (Comisión, jul 2025) | 40 |
| 63 | AI Act — Code of Practice for GPAI (Comisión, 2025) | 60 |
| 64 | AI Act — Guidelines on high-risk classification (Comisión) | 35 |
| 65 | ALTAI — Assessment List for Trustworthy AI (High-Level Expert Group) | 40 |
| 66 | Ethics Guidelines for Trustworthy AI (HLEG, 2019) | 40 |
| 67 | Algorithmic discrimination under AI Act and GDPR (EPRS, 2025) | 15 |

**Documentación ENISA / Ciberseguridad:**

| # | Documento | Págs aprox |
|---|---|---|
| 68 | ENISA Threat Landscape 2025 (resumen ejecutivo) | 30 |
| 69 | ENISA Guidelines for SMEs on cybersecurity | 25 |
| 70 | ENISA Cloud Security Guide | 35 |

**Subtotal Capa 2: ~48 documentos, ~1.700 páginas estimadas**

---

### Capa 3 — Documentación sectorial y frameworks

Fuentes: ISO (resúmenes públicos), NIST, estándares de industria.

| # | Documento | Fuente | Págs aprox |
|---|---|---|---|
| 71 | ISO/IEC 27001:2022 — Overview and vocabulary (público) | ISO | 15 |
| 72 | ISO/IEC 27701:2019 — Privacy management (resumen público) | ISO | 10 |
| 73 | NIST AI Risk Management Framework (AI RMF 1.0) | NIST | 50 |
| 74 | NIST Cybersecurity Framework 2.0 | NIST | 30 |
| 75 | OECD AI Principles (actualización 2024) | OECD | 20 |
| 76 | UNESCO Recommendation on AI Ethics | UNESCO | 25 |
| 77 | WEF — The Future of AI-Enabled Health: Leading the Way (2025) | WEF | 40 |
| 78 | AI Literacy Framework (AILit) — Comisión Europea + OECD (2026) | CE/OECD | 30 |

**Subtotal Capa 3: ~8 documentos, ~220 páginas estimadas**

---

### Capa 4 — Documentación interna NEXORA (ya generada)

| # | Documento | Págs |
|---|---|---|
| 79 | Protocolo Interno de Cumplimiento Normativo v3.2 | 6 |
| 80 | Resumen ejecutivo AI Act | 3 |
| 81 | RGPD — Derechos del interesado (extracto práctico) | 3 |
| 82 | Política de Proveedores y Subcontratación v2.1 | 3 |

**Subtotal Capa 4: 4 documentos, 15 páginas**

---

### Totales del corpus

| Capa | Documentos | Páginas estimadas | Fuente |
|---|---|---|---|
| 1 — Legislación primaria | 22 | ~1.700 | EUR-Lex, BOE |
| 2 — Guías de interpretación | 48 | ~1.700 | AEPD, EDPB, CE, ENISA |
| 3 — Frameworks y estándares | 8 | ~220 | NIST, OECD, UNESCO, WEF |
| 4 — Documentación interna NEXORA | 4 | 15 | Generados |
| **TOTAL** | **82** | **~3.635** | |

Con los documentos que no requieren descarga manual y están disponibles directamente como PDF público, podemos llegar cómodamente a **80-100 documentos y 4.000-5.000 páginas**.

Si queremos estirar, las guías de la AEPD suman fácilmente otros 20 documentos más (hay un catálogo extensísimo de blogs, infografías y documentos sectoriales). Y el EDPB tiene decenas de directrices adicionales en español. Llegar a **120-150 documentos y 5.000-6.000 páginas** es perfectamente viable sin forzar nada.

---

## Diseño del script de descarga

### Arquitectura propuesta

```
descargar_corpus_nexora.py
│
├── Descarga automática (URLs directas a PDF públicos)
│   ├── EUR-Lex: /download/es/TXT/PDF/?uri=CELEX:32016R0679
│   ├── BOE: /biblioteca_juridica/abrir_pdf.php?fich=...
│   ├── AEPD: /sites/default/files/...
│   ├── EDPB: /sites/default/files/...
│   └── NIST/OECD/UNESCO: URLs directas
│
├── Copia de docs NEXORA internos (ya generados)
│
├── Inventario final
│   └── corpus_inventario.csv (nombre, fuente, URL, páginas, capa)
│
└── Output: ~/nexora_legal_corpus/ con todos los PDFs
```

### Consideraciones técnicas

- **Todas las fuentes son públicas y gratuitas.** EUR-Lex publica bajo licencia abierta. BOE publica bajo reutilización autorizada. AEPD publica sus guías para distribución libre. NIST es gobierno de EEUU (dominio público).
- **Los PDFs de EUR-Lex en español** se descargan con URL predecible: `https://eur-lex.europa.eu/legal-content/ES/TXT/PDF/?uri=CELEX:{celex_number}`.
- **Los PDFs del BOE** se descargan desde: `https://www.boe.es/buscar/pdf/{year}/BOE-A-{year}-{number}-consolidado.pdf`.
- **Las guías de la AEPD** se descargan desde: `https://www.aepd.es/sites/default/files/{year}-{month}/{filename}.pdf` o desde `https://www.aepd.es/guias/{slug}.pdf`.
- **Timeout y retry:** algunas fuentes (EUR-Lex, BOE) pueden ser lentas. El script incluirá retry con backoff.
- **Verificación post-descarga:** comprobar que cada PDF tiene más de 10KB (descartar errores 404 silenciosos).

### Estimación de indexación en ChromaDB

Con chunks de 1.000 caracteres y overlap de 200:
- ~5.000 páginas × ~2.000 caracteres/página = ~10M caracteres
- ~10M / 800 (chunk efectivo descontando overlap) = **~12.500 chunks**
- Con OpenAI `text-embedding-3-small`: ~12.500 × 0.02$/1M tokens ≈ **$0.05** de coste total
- Con Ollama `nomic-embed-text`: **$0** de coste, ~15-30 min de procesamiento local
- ChromaDB en disco: ~50-100 MB

**Para la demo en clase:** la indexación se hace antes de clase. Si quieres mostrar el proceso en vivo, indexas 5-10 PDFs en directo y cargas el ChromaDB completo pre-indexado como backup.

---

## Valor pedagógico del corpus ampliado

### Para la demo del RAG (S5)

Un corpus de 80-150 documentos permite preguntas que son imposibles con 5 PDFs:

**Preguntas intra-capa (dentro de una sola fuente):**
- *"¿Qué dice el artículo 35 del RGPD sobre evaluaciones de impacto?"* → responde del texto legal.
- *"¿Cómo recomienda la AEPD documentar un interés legítimo?"* → responde de la guía AEPD.

**Preguntas cross-capa (el RAG cruza fuentes automáticamente):**
- *"¿Nuestro sistema de cribado de CV necesita una evaluación de impacto?"* → el RAG combina:
  - El AI Act (alto riesgo en empleo, art. 6 Anexo III)
  - El RGPD art. 35 (EIPD obligatoria para alto riesgo)
  - La guía de la AEPD sobre EIPD (cómo hacerla paso a paso)
  - El protocolo NEXORA (dice que la EIPD ya está en marcha)
  - Esto es exactamente lo que un abogado junior tardaria 2 horas en compilar.

**Preguntas de contraste normativo:**
- *"¿Qué diferencias hay entre las obligaciones de transparencia del RGPD y las del AI Act?"*
- *"¿El ENS y la NIS2 se solapan? ¿Cuál prevalece?"*

**Preguntas de aplicabilidad empresarial:**
- *"¿Qué proveedores de NEXORA podrían verse afectados por el Data Act?"*
- *"Si NEXORA empieza a operar en el sector salud, ¿qué normativa adicional aplica?"*

### Para el mensaje de escalado

Cuando el alumno ve que el mismo RAG que empezó con 4 PDFs ahora maneja 100+ documentos y sigue respondiendo en 3-5 segundos, entiende tres cosas:

1. **La arquitectura escala.** No es un juguete que funciona con 5 documentos y rompe con 500. ChromaDB maneja millones de vectores.

2. **El coste marginal de añadir documentación es prácticamente cero.** Descargar, trocear e indexar un PDF nuevo cuesta céntimos y minutos. La inteligencia del LLM ya está pagada.

3. **El valor crece con el corpus.** Un RAG con 5 documentos es un FAQ. Un RAG con 150 documentos es un **asistente de compliance** que ahorra horas de trabajo real. La diferencia no es técnica — es de corpus.

---

## Siguiente paso

Con tu confirmación, genero el script `descargar_corpus_nexora.py` que:
1. Descarga todos los PDFs públicos del inventario (EUR-Lex, BOE, AEPD, EDPB, NIST...).
2. Copia los 4 PDFs internos de NEXORA ya generados.
3. Genera un `corpus_inventario.csv` con el listado completo.
4. Informa del resultado: documentos descargados, páginas totales, fallos.

También puedo generar el script de indexación adaptado (`indexar_corpus_nexora.py`) que procese todo el corpus en ChromaDB con batches apropiados para el volumen.

---

**FIN DEL DOCUMENTO**
