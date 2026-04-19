#!/usr/bin/env python3
"""
Genera los 4 PDFs del corpus NEXORA Legal Compliance para el RAG de la sesión S5 IASP.
"""

import argparse
import os
import sys

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.colors import HexColor
    from reportlab.lib.units import cm
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
        HRFlowable
    )
    from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
except ImportError:
    print("ERROR: falta reportlab. Instala con: pip install reportlab")
    sys.exit(1)

DEFAULT_OUTPUT_DIR = "./nexora_legal_interno"
OUTPUT_DIR = DEFAULT_OUTPUT_DIR

# ── Styles ──────────────────────────────────────────────────────────────────

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle', parent=styles['Title'],
    fontSize=20, spaceAfter=20, textColor=HexColor('#1a3c5e'),
    fontName='Helvetica-Bold'
)
subtitle_style = ParagraphStyle(
    'DocSubtitle', parent=styles['Normal'],
    fontSize=12, spaceAfter=30, textColor=HexColor('#555555'),
    fontName='Helvetica-Oblique', alignment=TA_CENTER
)
heading1_style = ParagraphStyle(
    'H1', parent=styles['Heading1'],
    fontSize=14, spaceBefore=20, spaceAfter=10,
    textColor=HexColor('#1a3c5e'), fontName='Helvetica-Bold'
)
heading2_style = ParagraphStyle(
    'H2', parent=styles['Heading2'],
    fontSize=12, spaceBefore=14, spaceAfter=8,
    textColor=HexColor('#2e6da4'), fontName='Helvetica-Bold'
)
body_style = ParagraphStyle(
    'BodyText2', parent=styles['Normal'],
    fontSize=10, leading=14, spaceAfter=8,
    alignment=TA_JUSTIFY, fontName='Helvetica'
)
bullet_style = ParagraphStyle(
    'Bullet', parent=body_style,
    leftIndent=20, bulletIndent=10, spaceAfter=4
)
footer_style = ParagraphStyle(
    'Footer', parent=styles['Normal'],
    fontSize=8, textColor=HexColor('#999999'),
    fontName='Helvetica-Oblique'
)


def build_doc(filename, title, subtitle, story_func):
    path = os.path.join(OUTPUT_DIR, filename)
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        topMargin=2*cm, bottomMargin=2*cm,
        leftMargin=2.5*cm, rightMargin=2.5*cm
    )
    story = []
    story.append(Paragraph(title, title_style))
    story.append(Paragraph(subtitle, subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor('#1a3c5e')))
    story.append(Spacer(1, 20))
    story_func(story)
    story.append(Spacer(1, 30))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor('#cccccc')))
    story.append(Spacer(1, 6))
    story.append(Paragraph("NEXORA S.L. — Documento interno — Confidencial", footer_style))
    doc.build(story)
    print(f"  ✓ {filename} ({os.path.getsize(path)//1024} KB)")


# ═══════════════════════════════════════════════════════════════════════════
# DOCUMENTO 1: Protocolo Interno de Cumplimiento Normativo NEXORA
# ═══════════════════════════════════════════════════════════════════════════

def doc1_protocolo(story):
    story.append(Paragraph("1. Objeto y alcance", heading1_style))
    story.append(Paragraph(
        "El presente protocolo establece las directrices internas de NEXORA S.L. para garantizar el cumplimiento "
        "de la normativa vigente en materia de proteccion de datos personales, inteligencia artificial, "
        "propiedad intelectual y contratacion mercantil. Es de obligado cumplimiento para todos los empleados, "
        "colaboradores externos y proveedores que traten datos o sistemas de IA en nombre de la empresa.",
        body_style
    ))
    story.append(Paragraph(
        "NEXORA S.L., con CIF B-12345678 y domicilio social en Madrid, opera en los sectores de consultoria "
        "tecnologica, desarrollo de software y servicios de datos. La empresa cuenta con 120 empleados "
        "distribuidos en las oficinas de Madrid (sede central), Barcelona (desarrollo) y Valencia (operaciones).",
        body_style
    ))

    story.append(Paragraph("2. Marco normativo de referencia", heading1_style))
    story.append(Paragraph(
        "NEXORA esta sujeta al cumplimiento de las siguientes normas principales:",
        body_style
    ))
    normas = [
        "Reglamento General de Proteccion de Datos (RGPD) — Reglamento (UE) 2016/679",
        "Ley Organica 3/2018 de Proteccion de Datos Personales y garantia de los derechos digitales (LOPDGDD)",
        "Reglamento Europeo de Inteligencia Artificial (AI Act) — Reglamento (UE) 2024/1689",
        "Directiva NIS2 — Directiva (UE) 2022/2555 sobre ciberseguridad",
        "Codigo de Comercio y Ley de Sociedades de Capital",
        "Ley 34/2002 de servicios de la sociedad de la informacion (LSSI-CE)",
        "Ley 2/2023 reguladora de la proteccion de las personas que informen sobre infracciones normativas (Canal de denuncias)"
    ]
    for n in normas:
        story.append(Paragraph(f"• {n}", bullet_style))

    story.append(Paragraph("3. Estructura organizativa de cumplimiento", heading1_style))
    story.append(Paragraph(
        "La funcion de cumplimiento en NEXORA se organiza en tres niveles:",
        body_style
    ))

    story.append(Paragraph("3.1. Comite de Cumplimiento", heading2_style))
    story.append(Paragraph(
        "Compuesto por el Director General, el Director Juridico, el Delegado de Proteccion de Datos (DPO), "
        "el CTO y el Director de Operaciones. Se reune trimestralmente y de forma extraordinaria ante "
        "cualquier cambio regulatorio significativo. Sus funciones incluyen: aprobar politicas de cumplimiento, "
        "evaluar riesgos normativos, supervisar auditorias internas y decidir medidas correctivas.",
        body_style
    ))

    story.append(Paragraph("3.2. Delegado de Proteccion de Datos (DPO)", heading2_style))
    story.append(Paragraph(
        "Designado conforme al articulo 37 del RGPD. En NEXORA, el DPO es Dra. Elena Martinez, con certificacion "
        "CIPP/E y experiencia de 8 anos en privacidad. Sus responsabilidades incluyen: supervisar el cumplimiento "
        "del RGPD y la LOPDGDD, gestionar las evaluaciones de impacto (EIPD), atender las solicitudes de ejercicio "
        "de derechos de los interesados, y actuar como punto de contacto con la Agencia Espanola de Proteccion "
        "de Datos (AEPD). El DPO reporta directamente al Comite de Cumplimiento y tiene acceso independiente "
        "a todos los registros de tratamiento.",
        body_style
    ))

    story.append(Paragraph("3.3. Responsables de area", heading2_style))
    story.append(Paragraph(
        "Cada director de departamento (Desarrollo, Comercial, RRHH, Operaciones, Marketing) es responsable "
        "de garantizar el cumplimiento normativo en su area. Deben reportar al DPO cualquier incidencia "
        "en un plazo maximo de 24 horas y participar en la formacion anual obligatoria sobre proteccion "
        "de datos e IA responsable.",
        body_style
    ))

    story.append(Paragraph("4. Politica de proteccion de datos", heading1_style))

    story.append(Paragraph("4.1. Principios de tratamiento", heading2_style))
    story.append(Paragraph(
        "Todo tratamiento de datos personales en NEXORA debe respetar los principios del articulo 5 del RGPD: "
        "licitud, lealtad y transparencia; limitacion de la finalidad; minimizacion de datos; exactitud; "
        "limitacion del plazo de conservacion; integridad y confidencialidad; y responsabilidad proactiva.",
        body_style
    ))

    story.append(Paragraph("4.2. Bases juridicas de tratamiento", heading2_style))
    story.append(Paragraph(
        "NEXORA utiliza las siguientes bases juridicas segun el tipo de tratamiento:",
        body_style
    ))
    bases = [
        "Ejecucion de contrato (art. 6.1.b RGPD): para la prestacion de servicios contratados por clientes.",
        "Consentimiento explicito (art. 6.1.a RGPD): para comunicaciones comerciales y marketing directo.",
        "Interes legitimo (art. 6.1.f RGPD): para prevencion de fraude y seguridad de la red. Documentado mediante test de ponderacion.",
        "Obligacion legal (art. 6.1.c RGPD): para obligaciones fiscales, laborales y de reporte regulatorio.",
        "Interes publico (art. 6.1.e RGPD): exclusivamente para proyectos con administraciones publicas."
    ]
    for b in bases:
        story.append(Paragraph(f"• {b}", bullet_style))

    story.append(Paragraph("4.3. Registro de actividades de tratamiento (RAT)", heading2_style))
    story.append(Paragraph(
        "NEXORA mantiene un Registro de Actividades de Tratamiento conforme al articulo 30 del RGPD. "
        "El registro se actualiza semestralmente e incluye 23 actividades de tratamiento documentadas. "
        "Las categorias principales de datos tratados son: datos identificativos de clientes y empleados, "
        "datos de contacto profesional, datos financieros (facturacion), datos de navegacion web (cookies), "
        "datos de uso de plataformas propias, y metadatos de sistemas de IA (logs de inferencia, prompts anonimizados).",
        body_style
    ))

    story.append(Paragraph("4.4. Plazos de conservacion", heading2_style))
    story.append(Paragraph(
        "Los datos personales se conservan durante los siguientes periodos maximos:",
        body_style
    ))
    plazos = [
        "Datos de clientes activos: durante la vigencia del contrato + 5 anos (prescripcion de obligaciones contractuales).",
        "Datos de empleados: durante la relacion laboral + 4 anos (prescripcion laboral y fiscal).",
        "Datos de candidatos no seleccionados: 12 meses desde la finalizacion del proceso de seleccion.",
        "Logs de sistemas de IA: 24 meses, anonimizados a los 6 meses.",
        "Datos de navegacion y cookies: 13 meses desde la obtencion del consentimiento.",
        "Facturas y documentacion fiscal: 6 anos (Codigo de Comercio) y 4 anos (Ley General Tributaria)."
    ]
    for p in plazos:
        story.append(Paragraph(f"• {p}", bullet_style))

    story.append(Paragraph("4.5. Derechos de los interesados", heading2_style))
    story.append(Paragraph(
        "NEXORA garantiza el ejercicio de los derechos de acceso, rectificacion, supresion, limitacion, "
        "portabilidad y oposicion. Las solicitudes se atienden en un plazo maximo de 30 dias naturales "
        "a traves del correo dpo@nexora.es. En 2025, NEXORA recibio 47 solicitudes de ejercicio de "
        "derechos: 31 de acceso, 8 de supresion, 5 de rectificacion y 3 de portabilidad. Todas fueron "
        "atendidas dentro del plazo legal.",
        body_style
    ))

    story.append(Paragraph("4.6. Transferencias internacionales", heading2_style))
    story.append(Paragraph(
        "NEXORA utiliza proveedores cloud con sede en Estados Unidos (AWS, Google Cloud, OpenAI). "
        "Las transferencias internacionales se amparan en: Clausulas Contractuales Tipo (CCT) aprobadas "
        "por la Comision Europea (Decision 2021/914), complementadas con medidas adicionales de cifrado "
        "y pseudonimizacion conforme a las Recomendaciones 01/2020 del EDPB. Para el uso de APIs de "
        "OpenAI, se aplica un Data Processing Addendum (DPA) especifico que prohíbe el uso de datos de "
        "clientes para entrenamiento de modelos.",
        body_style
    ))

    story.append(Paragraph("5. Politica de inteligencia artificial", heading1_style))

    story.append(Paragraph("5.1. Clasificacion de sistemas de IA", heading2_style))
    story.append(Paragraph(
        "NEXORA clasifica sus sistemas de IA conforme a la taxonomia de riesgo del AI Act europeo "
        "(Reglamento UE 2024/1689):",
        body_style
    ))
    clasificacion = [
        "Riesgo inaceptable (prohibidos): NEXORA no desarrolla ni utiliza sistemas de puntuacion social, "
        "manipulacion subliminal, explotacion de vulnerabilidades, ni vigilancia biometrica en tiempo real "
        "en espacios publicos.",
        "Alto riesgo: Sistemas de IA utilizados en procesos de seleccion de personal (modulo de cribado "
        "de CV automatizado — actualmente en fase piloto, sujeto a EIPD y supervision humana obligatoria). "
        "Sistemas de scoring crediticio ofrecidos como servicio a clientes del sector financiero.",
        "Riesgo limitado (obligacion de transparencia): Chatbots de atencion al cliente basados en LLMs "
        "que deben identificarse como sistemas automatizados. Sistemas de generacion de contenido que "
        "deben etiquetar el output como generado por IA.",
        "Riesgo minimo: Herramientas internas de productividad (asistentes de codigo, resumen de documentos, "
        "traduccion automatica). No requieren obligaciones adicionales pero se documentan igualmente."
    ]
    for c in clasificacion:
        story.append(Paragraph(f"• {c}", bullet_style))

    story.append(Paragraph("5.2. Obligaciones especificas para sistemas de alto riesgo", heading2_style))
    story.append(Paragraph(
        "Para los sistemas clasificados como alto riesgo, NEXORA aplica las siguientes medidas conforme "
        "al Titulo III del AI Act:",
        body_style
    ))
    obligaciones = [
        "Sistema de gestion de riesgos: evaluacion continua documentada, con revision semestral.",
        "Calidad de datos: auditoria de datasets de entrenamiento para detectar sesgos, con metricas "
        "de equidad (demographic parity, equalized odds) reportadas trimestralmente.",
        "Documentacion tecnica: ficha tecnica del sistema que incluye arquitectura, datos de entrenamiento, "
        "metricas de rendimiento, limitaciones conocidas y casos de uso previstos.",
        "Registro automatico (logging): todos los sistemas de alto riesgo registran cada inferencia "
        "con timestamp, input (anonimizado), output, y score de confianza. Retencion: 24 meses.",
        "Supervision humana: toda decision automatizada clasificada como alto riesgo requiere revision "
        "humana antes de producir efectos juridicos. El operador humano tiene capacidad de veto.",
        "Transparencia e informacion: los usuarios son informados de que interactuan con un sistema de IA, "
        "de la logica involucrada, y de su derecho a solicitar una revision humana.",
        "Precision, robustez y ciberseguridad: pruebas de adversarial testing anuales, pen testing "
        "trimestral, y plan de continuidad documentado."
    ]
    for o in obligaciones:
        story.append(Paragraph(f"• {o}", bullet_style))

    story.append(Paragraph("5.3. Evaluacion de Impacto de Derechos Fundamentales (EIDF)", heading2_style))
    story.append(Paragraph(
        "Conforme al articulo 27 del AI Act, NEXORA realiza una Evaluacion de Impacto de Derechos "
        "Fundamentales para cada sistema de IA de alto riesgo antes de su despliegue. La EIDF evalua: "
        "impacto en la privacidad, riesgo de discriminacion, efectos en la autonomia individual, "
        "impacto en grupos vulnerables, y medidas de mitigacion. La EIDF se revisa anualmente o "
        "ante cualquier cambio significativo en el sistema.",
        body_style
    ))

    story.append(Paragraph("6. Politica de gestion de contratos", heading1_style))

    story.append(Paragraph("6.1. Tipos de contratos gestionados", heading2_style))
    story.append(Paragraph(
        "NEXORA gestiona los siguientes tipos de contratos:",
        body_style
    ))
    contratos = [
        "Contratos de prestacion de servicios tecnologicos (SLA incluido): 87 contratos activos.",
        "Contratos de licencia de software: 34 contratos activos.",
        "Acuerdos de procesamiento de datos (DPA): 52 acuerdos vigentes.",
        "Contratos laborales: 120 contratos activos (indefinidos, temporales y becarios).",
        "Contratos con proveedores cloud y SaaS: 28 contratos activos.",
        "Acuerdos de confidencialidad (NDA): 156 NDAs vigentes.",
        "Contratos de I+D con universidades y centros de investigacion: 5 convenios activos."
    ]
    for c in contratos:
        story.append(Paragraph(f"• {c}", bullet_style))

    story.append(Paragraph("6.2. Clausulas obligatorias", heading2_style))
    story.append(Paragraph(
        "Todo contrato con clientes o proveedores debe incluir como minimo las siguientes clausulas: "
        "clausula de proteccion de datos (conforme al art. 28 RGPD para encargados de tratamiento), "
        "clausula de confidencialidad, clausula de propiedad intelectual, clausula de cumplimiento "
        "del AI Act (para contratos que involucren sistemas de IA), clausula de resolucion y penalizaciones, "
        "clausula de jurisdiccion y ley aplicable (por defecto: tribunales de Madrid, ley espanola).",
        body_style
    ))

    story.append(Paragraph("6.3. Proceso de revision ante cambio regulatorio", heading2_style))
    story.append(Paragraph(
        "Cuando entra en vigor una nueva regulacion o se modifica una existente, el proceso de revision "
        "contractual sigue estos pasos: (1) El equipo juridico identifica los contratos potencialmente "
        "afectados en un plazo maximo de 5 dias habiles. (2) Se clasifica el impacto como ALTO (requiere "
        "renegociacion o adenda), MEDIO (requiere comunicacion al cliente y ajuste de clausulas menores) "
        "o BAJO (no requiere accion, solo documentacion interna). (3) Para impacto ALTO, se inicia el "
        "proceso de renegociacion con el cliente en un plazo maximo de 30 dias. (4) El Comite de "
        "Cumplimiento revisa y aprueba las adendas antes de su firma.",
        body_style
    ))

    story.append(Paragraph("7. Politica de gestion de incidencias", heading1_style))

    story.append(Paragraph("7.1. Brechas de seguridad de datos personales", heading2_style))
    story.append(Paragraph(
        "Conforme al articulo 33 del RGPD, NEXORA notificara a la AEPD cualquier brecha de seguridad "
        "que suponga un riesgo para los derechos y libertades de las personas fisicas en un plazo maximo "
        "de 72 horas desde su deteccion. Si el riesgo es alto, se notificara tambien a los afectados "
        "(art. 34 RGPD). El DPO coordina la respuesta, que incluye: contencion, evaluacion del alcance, "
        "notificacion, documentacion y medidas correctivas. En 2025, NEXORA registro 2 incidencias menores "
        "(acceso no autorizado a carpeta compartida y envio de email con copia visible) que no requirieron "
        "notificacion a la AEPD tras evaluacion del riesgo.",
        body_style
    ))

    story.append(Paragraph("7.2. Incidencias de sistemas de IA", heading2_style))
    story.append(Paragraph(
        "Conforme al articulo 62 del AI Act, los incidentes graves relacionados con sistemas de IA de "
        "alto riesgo deben notificarse a la autoridad de vigilancia del mercado (en Espana, la AESIA) "
        "en un plazo de 15 dias. Se considera incidente grave: cualquier mal funcionamiento que cause o "
        "pueda causar dano a la salud, la seguridad o los derechos fundamentales de las personas. "
        "NEXORA mantiene un registro interno de todos los incidentes de IA, incluyendo los no graves, "
        "y los revisa trimestralmente en el Comite de Cumplimiento.",
        body_style
    ))

    story.append(Paragraph("8. Formacion y concienciacion", heading1_style))
    story.append(Paragraph(
        "Todos los empleados de NEXORA deben completar una formacion anual obligatoria que cubre: "
        "proteccion de datos personales (4 horas), uso responsable de IA (2 horas), ciberseguridad "
        "basica (2 horas), y canal de denuncias (1 hora). La formacion se imparte online a traves "
        "de la plataforma interna y se evalua mediante test. El porcentaje de completitud en 2025 "
        "fue del 94%. Los nuevos empleados reciben la formacion durante su primer mes.",
        body_style
    ))

    story.append(Paragraph("9. Auditoria y control", heading1_style))
    story.append(Paragraph(
        "NEXORA realiza una auditoria interna anual de cumplimiento y una auditoria externa bienal. "
        "La ultima auditoria externa (noviembre 2025, realizada por Deloitte) concluyo con 3 observaciones "
        "menores: (1) necesidad de actualizar el RAT con dos nuevos tratamientos identificados, "
        "(2) documentar formalmente el test de ponderacion de interes legitimo para un tratamiento de "
        "marketing, y (3) completar la EIDF del modulo de cribado de CV antes de su puesta en produccion. "
        "Las tres observaciones fueron resueltas antes de febrero de 2026.",
        body_style
    ))

    story.append(Paragraph("10. Revision y actualizacion del protocolo", heading1_style))
    story.append(Paragraph(
        "Este protocolo se revisa anualmente o de forma extraordinaria ante cambios regulatorios "
        "significativos. La presente version (v3.2) fue aprobada por el Comite de Cumplimiento "
        "el 15 de enero de 2026. La proxima revision ordinaria esta prevista para enero de 2027.",
        body_style
    ))

    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "<b>Aprobado por:</b> Comite de Cumplimiento de NEXORA S.L.<br/>"
        "<b>Fecha:</b> 15 de enero de 2026<br/>"
        "<b>Version:</b> 3.2<br/>"
        "<b>Clasificacion:</b> Uso interno — Confidencial",
        body_style
    ))


# ═══════════════════════════════════════════════════════════════════════════
# DOCUMENTO 2: Resumen Ejecutivo del AI Act
# ═══════════════════════════════════════════════════════════════════════════

def doc2_ai_act(story):
    story.append(Paragraph("Introduccion", heading1_style))
    story.append(Paragraph(
        "El Reglamento (UE) 2024/1689, conocido como AI Act o Reglamento Europeo de Inteligencia Artificial, "
        "fue publicado en el Diario Oficial de la Union Europea el 12 de julio de 2024. Es la primera "
        "regulacion integral sobre inteligencia artificial a nivel mundial. Su objetivo es garantizar "
        "que los sistemas de IA comercializados y utilizados en la UE sean seguros, respeten los derechos "
        "fundamentales y fomenten la innovacion.",
        body_style
    ))

    story.append(Paragraph("Calendario de aplicacion", heading1_style))
    story.append(Paragraph(
        "El AI Act se aplica de forma escalonada:",
        body_style
    ))
    calendario = [
        "2 de febrero de 2025: prohibicion de practicas de IA inaceptables (Titulo II).",
        "2 de agosto de 2025: obligaciones para modelos de IA de proposito general (GPAI) y gobernanza (Titulos V, XII).",
        "2 de agosto de 2026: aplicacion completa, incluyendo sistemas de alto riesgo (Titulo III). "
        "A partir de esta fecha, todos los sistemas de alto riesgo deben cumplir integramente.",
        "2 de agosto de 2027: obligaciones para sistemas de IA integrados en productos regulados (Anexo I)."
    ]
    for c in calendario:
        story.append(Paragraph(f"• {c}", bullet_style))

    story.append(Paragraph("Clasificacion por niveles de riesgo", heading1_style))

    story.append(Paragraph("Riesgo inaceptable (Articulo 5) — PROHIBIDO", heading2_style))
    story.append(Paragraph(
        "Se prohiben los siguientes usos de IA en la UE:",
        body_style
    ))
    prohibidos = [
        "Sistemas de puntuacion social (social scoring) por parte de autoridades publicas.",
        "Manipulacion subliminal o enganosa que cause dano significativo.",
        "Explotacion de vulnerabilidades por edad, discapacidad o situacion social.",
        "Identificacion biometrica en tiempo real en espacios publicos con fines policiales "
        "(salvo excepciones tasadas: busqueda de victimas, prevencion de amenazas terroristas, "
        "localizacion de sospechosos de delitos graves).",
        "Categorizacion biometrica para inferir raza, religion, orientacion sexual o afiliacion politica.",
        "Scraping no selectivo de imagenes faciales de Internet o CCTV para crear bases de datos de reconocimiento facial.",
        "Inferencia de emociones en el lugar de trabajo o en instituciones educativas (salvo razones medicas o de seguridad)."
    ]
    for p in prohibidos:
        story.append(Paragraph(f"• {p}", bullet_style))

    story.append(Paragraph("Alto riesgo (Titulo III, Anexo III) — REGULADO", heading2_style))
    story.append(Paragraph(
        "Se clasifican como alto riesgo los sistemas de IA utilizados en los siguientes ambitos:",
        body_style
    ))
    alto_riesgo = [
        "Identificacion y categorizacion biometrica remota.",
        "Gestion y operacion de infraestructuras criticas (energia, agua, transporte, telecomunicaciones).",
        "Educacion y formacion profesional: admision, evaluacion, deteccion de trampas.",
        "Empleo y gestion de trabajadores: contratacion, seleccion de CV, evaluacion de rendimiento, "
        "promociones, despidos, asignacion de tareas, monitorizacion.",
        "Acceso a servicios esenciales: evaluacion de credito, seguros de vida y salud, servicios publicos, "
        "asistencia social, clasificacion de llamadas de emergencia.",
        "Aplicacion de la ley: evaluacion de riesgo de reincidencia, poligrafo, evaluacion de pruebas.",
        "Gestion de migracion y control de fronteras: verificacion de documentos, evaluacion de solicitudes de asilo.",
        "Administracion de justicia y procesos democraticos."
    ]
    for a in alto_riesgo:
        story.append(Paragraph(f"• {a}", bullet_style))

    story.append(Paragraph("Obligaciones para sistemas de alto riesgo (Articulos 8-15)", heading2_style))
    story.append(Paragraph(
        "Los proveedores de sistemas de alto riesgo deben cumplir con:",
        body_style
    ))
    obligaciones_ar = [
        "Sistema de gestion de riesgos (art. 9): proceso iterativo y documentado durante todo el ciclo de vida.",
        "Gobernanza de datos (art. 10): datasets de entrenamiento, validacion y prueba relevantes, representativos, "
        "sin errores y completos. Atencion especifica a sesgos.",
        "Documentacion tecnica (art. 11): informacion detallada sobre el sistema, su desarrollo y su funcionamiento.",
        "Registro automatico (art. 12): logging de eventos durante el funcionamiento para trazabilidad.",
        "Transparencia (art. 13): instrucciones de uso claras para los desplegadores.",
        "Supervision humana (art. 14): disenar el sistema para que pueda ser supervisado por personas fisicas.",
        "Precision, robustez y ciberseguridad (art. 15): niveles adecuados de exactitud, robustez ante errores "
        "y ataques, y medidas de ciberseguridad."
    ]
    for o in obligaciones_ar:
        story.append(Paragraph(f"• {o}", bullet_style))

    story.append(Paragraph("Riesgo limitado (Titulo IV) — TRANSPARENCIA", heading2_style))
    story.append(Paragraph(
        "Los sistemas de riesgo limitado tienen obligaciones de transparencia: los chatbots deben informar "
        "al usuario de que esta interactuando con un sistema de IA; el contenido generado por IA (deepfakes, "
        "texto, imagenes, audio) debe etiquetarse como generado artificialmente; y los sistemas de deteccion "
        "de emociones o categorizacion biometrica deben informar a las personas expuestas.",
        body_style
    ))

    story.append(Paragraph("Riesgo minimo — SIN OBLIGACIONES ADICIONALES", heading2_style))
    story.append(Paragraph(
        "La gran mayoria de sistemas de IA (filtros de spam, videojuegos, asistentes de productividad) "
        "se clasifican como riesgo minimo y no tienen obligaciones regulatorias adicionales bajo el AI Act. "
        "Se fomenta la adopcion voluntaria de codigos de conducta.",
        body_style
    ))

    story.append(Paragraph("Modelos de IA de proposito general (GPAI)", heading1_style))
    story.append(Paragraph(
        "El AI Act introduce obligaciones especificas para los proveedores de modelos de IA de proposito "
        "general (como GPT-4, Claude, Gemini, Llama). Las obligaciones basicas incluyen: documentacion "
        "tecnica, politica de cumplimiento de derechos de autor, y resumen del contenido de entrenamiento. "
        "Los modelos con riesgo sistemico (umbral: 10^25 FLOP de entrenamiento) tienen obligaciones "
        "adicionales: evaluacion de modelos, mitigacion de riesgos sistemicos, notificacion de incidentes "
        "graves, y pruebas de adversarial testing.",
        body_style
    ))

    story.append(Paragraph("Regimen sancionador", heading1_style))
    story.append(Paragraph(
        "Las infracciones del AI Act se sancionan con multas proporcionales y disuasorias:",
        body_style
    ))
    sanciones = [
        "Practicas prohibidas (art. 5): hasta 35 millones de euros o el 7% de la facturacion anual global.",
        "Incumplimiento de obligaciones de alto riesgo: hasta 15 millones de euros o el 3% de la facturacion.",
        "Suministro de informacion incorrecta: hasta 7,5 millones de euros o el 1% de la facturacion.",
        "Para PYMEs y startups, las multas se ajustan proporcionalmente al tamano de la empresa."
    ]
    for s in sanciones:
        story.append(Paragraph(f"• {s}", bullet_style))

    story.append(Paragraph("Gobernanza y supervision", heading1_style))
    story.append(Paragraph(
        "Cada Estado miembro designa al menos una autoridad nacional competente. En Espana, la Agencia "
        "Espanola de Supervision de la Inteligencia Artificial (AESIA), con sede en A Coruna, actuara como "
        "autoridad de vigilancia del mercado. A nivel europeo, se establece la Oficina Europea de IA (AI Office) "
        "dentro de la Comision Europea, responsable de supervisar los modelos GPAI y coordinar la aplicacion "
        "armonizada del reglamento. Tambien se crea un Comite Europeo de Inteligencia Artificial con "
        "representantes de los Estados miembros.",
        body_style
    ))

    story.append(Paragraph("Sandboxes regulatorios", heading1_style))
    story.append(Paragraph(
        "El AI Act obliga a los Estados miembros a establecer al menos un sandbox regulatorio de IA antes "
        "del 2 de agosto de 2026. Los sandboxes permiten desarrollar, probar y validar sistemas de IA "
        "innovadores en un entorno controlado y supervisado antes de su comercializacion. Las PYMEs y "
        "startups tienen acceso prioritario. Espana ya ha puesto en marcha su sandbox piloto a traves "
        "de la AESIA.",
        body_style
    ))


# ═══════════════════════════════════════════════════════════════════════════
# DOCUMENTO 3: Extracto del RGPD — Derechos del interesado
# ═══════════════════════════════════════════════════════════════════════════

def doc3_rgpd(story):
    story.append(Paragraph("Capitulo III del RGPD — Derechos del interesado", heading1_style))
    story.append(Paragraph(
        "El presente documento recoge un extracto y explicacion practica de los articulos 12 a 23 del "
        "Reglamento General de Proteccion de Datos (RGPD), relativos a los derechos de los interesados. "
        "Adaptado al contexto operativo de NEXORA S.L.",
        body_style
    ))

    story.append(Paragraph("Articulo 12 — Transparencia de la informacion", heading2_style))
    story.append(Paragraph(
        "El responsable del tratamiento debe proporcionar toda informacion relativa al tratamiento de forma "
        "concisa, transparente, inteligible y facilmente accesible, con un lenguaje claro y sencillo. "
        "La informacion se facilitara por escrito, incluyendo por medios electronicos. En NEXORA, las "
        "clausulas informativas se revisan semestralmente para verificar su claridad. Las solicitudes de "
        "ejercicio de derechos se atienden de forma gratuita, salvo que sean manifiestamente infundadas "
        "o excesivas, en cuyo caso puede cobrarse un canon razonable o denegarse la solicitud.",
        body_style
    ))

    story.append(Paragraph("Articulos 13-14 — Informacion en la recogida de datos", heading2_style))
    story.append(Paragraph(
        "Cuando se recojan datos directamente del interesado (art. 13), se debe informar de: identidad "
        "del responsable, datos del DPO, finalidades del tratamiento, base juridica, destinatarios, "
        "transferencias internacionales, plazo de conservacion, existencia de derechos, derecho a retirar "
        "el consentimiento, derecho a reclamar ante la AEPD, y si existe toma de decisiones automatizada "
        "(incluida la elaboracion de perfiles). Cuando los datos no se obtienen directamente del interesado "
        "(art. 14), ademas hay que informar del origen de los datos y las categorias de datos tratados.",
        body_style
    ))

    story.append(Paragraph("Articulo 15 — Derecho de acceso", heading2_style))
    story.append(Paragraph(
        "El interesado tiene derecho a obtener confirmacion de si se estan tratando sus datos personales "
        "y, en caso afirmativo, acceso a: los datos, las finalidades, las categorias de datos, los "
        "destinatarios, el plazo de conservacion, la existencia de decisiones automatizadas (incluida "
        "la elaboracion de perfiles), y la informacion significativa sobre la logica aplicada, asi como "
        "la importancia y consecuencias de dicho tratamiento. En NEXORA, el plazo de respuesta es de "
        "30 dias naturales. El DPO coordina la recopilacion de informacion de todos los sistemas.",
        body_style
    ))

    story.append(Paragraph("Articulo 16 — Derecho de rectificacion", heading2_style))
    story.append(Paragraph(
        "El interesado tiene derecho a obtener la rectificacion de datos personales inexactos que le "
        "conciernan. Tambien puede completar datos incompletos mediante una declaracion adicional. "
        "En NEXORA, las rectificaciones se propagan a todos los sistemas que contengan los datos "
        "afectados en un plazo maximo de 48 horas.",
        body_style
    ))

    story.append(Paragraph("Articulo 17 — Derecho de supresion (derecho al olvido)", heading2_style))
    story.append(Paragraph(
        "El interesado tiene derecho a obtener la supresion de sus datos personales cuando: los datos "
        "ya no sean necesarios para la finalidad original; retire el consentimiento y no exista otra "
        "base juridica; se oponga al tratamiento y no prevalezcan motivos legitimos; los datos se hayan "
        "tratado ilicitamente; o deba cumplirse una obligacion legal. La supresion no procede cuando "
        "el tratamiento sea necesario para el ejercicio de la libertad de expresion, el cumplimiento "
        "de una obligacion legal, razones de interes publico en el ambito de la salud publica, "
        "fines de archivo en interes publico o investigacion, o la formulacion de reclamaciones.",
        body_style
    ))

    story.append(Paragraph("Articulo 18 — Derecho a la limitacion del tratamiento", heading2_style))
    story.append(Paragraph(
        "El interesado puede solicitar la limitacion del tratamiento cuando: impugne la exactitud de "
        "los datos (durante la verificacion), el tratamiento sea ilicito pero no desee la supresion, "
        "el responsable ya no necesite los datos pero el interesado los necesite para reclamaciones, "
        "o se haya ejercido el derecho de oposicion (mientras se verifica). En NEXORA, los datos "
        "limitados se marcan tecnicamente y solo se tratan con consentimiento del interesado, para "
        "reclamaciones o por razones de interes publico.",
        body_style
    ))

    story.append(Paragraph("Articulo 20 — Derecho a la portabilidad", heading2_style))
    story.append(Paragraph(
        "El interesado tiene derecho a recibir sus datos personales en un formato estructurado, de uso "
        "comun y lectura mecanica, y a transmitirlos a otro responsable sin impedimentos, cuando: el "
        "tratamiento se base en consentimiento o contrato, y se efectue por medios automatizados. "
        "En NEXORA, los datos se exportan en formato CSV o JSON dentro de los 30 dias siguientes "
        "a la solicitud.",
        body_style
    ))

    story.append(Paragraph("Articulo 21 — Derecho de oposicion", heading2_style))
    story.append(Paragraph(
        "El interesado puede oponerse al tratamiento basado en interes publico o interes legitimo, "
        "incluida la elaboracion de perfiles. El responsable dejara de tratar los datos salvo que "
        "acredite motivos imperiosos que prevalezcan sobre los intereses del interesado. Para marketing "
        "directo, el derecho de oposicion es absoluto: si el interesado se opone, los datos dejan de "
        "tratarse para esa finalidad sin excepciones.",
        body_style
    ))

    story.append(Paragraph("Articulo 22 — Decisiones automatizadas y elaboracion de perfiles", heading2_style))
    story.append(Paragraph(
        "El interesado tiene derecho a no ser objeto de una decision basada unicamente en el tratamiento "
        "automatizado, incluida la elaboracion de perfiles, que produzca efectos juridicos o le afecte "
        "significativamente. Las excepciones son: que sea necesario para un contrato, que este autorizado "
        "por el Derecho de la Union o del Estado miembro, o que se base en consentimiento explicito. "
        "En todos los casos, el responsable debe aplicar medidas adecuadas para proteger los derechos "
        "del interesado, como minimo el derecho a obtener intervencion humana, a expresar su punto de "
        "vista y a impugnar la decision.",
        body_style
    ))
    story.append(Paragraph(
        "En NEXORA, el articulo 22 es especialmente relevante para los sistemas de scoring crediticio "
        "y el modulo de cribado de CV. Ambos sistemas estan disenados con supervision humana obligatoria "
        "(human-in-the-loop) y los interesados son informados del uso de IA y de su derecho a solicitar "
        "revision humana.",
        body_style
    ))

    story.append(Paragraph("Procedimiento interno NEXORA para el ejercicio de derechos", heading1_style))
    story.append(Paragraph(
        "1. El interesado envia su solicitud a dpo@nexora.es, identificandose y especificando el derecho "
        "que desea ejercer. 2. El DPO acusa recibo en un plazo maximo de 3 dias habiles. 3. El DPO "
        "verifica la identidad del solicitante. 4. Se recopila la informacion necesaria de los sistemas "
        "involucrados. 5. Se responde al interesado en un plazo maximo de 30 dias naturales (prorrogable "
        "2 meses en casos complejos, previa notificacion). 6. Se documenta la solicitud y la respuesta "
        "en el registro interno de ejercicio de derechos.",
        body_style
    ))


# ═══════════════════════════════════════════════════════════════════════════
# DOCUMENTO 4: Politica de Proveedores y Subcontratacion
# ═══════════════════════════════════════════════════════════════════════════

def doc4_proveedores(story):
    story.append(Paragraph("1. Objeto", heading1_style))
    story.append(Paragraph(
        "La presente politica establece los criterios y procedimientos de NEXORA S.L. para la seleccion, "
        "contratacion y supervision de proveedores y subcontratistas que accedan a datos personales o "
        "intervengan en el desarrollo, despliegue o mantenimiento de sistemas de inteligencia artificial.",
        body_style
    ))

    story.append(Paragraph("2. Ambito de aplicacion", heading1_style))
    story.append(Paragraph(
        "Aplica a todos los proveedores que cumplan al menos uno de los siguientes criterios: "
        "accedan a datos personales de clientes, empleados o usuarios de NEXORA; proporcionen "
        "infraestructura cloud o servicios SaaS; participen en el desarrollo o mantenimiento de "
        "sistemas de IA; proporcionen servicios de consultoria con acceso a informacion confidencial; "
        "o presten servicios de soporte tecnico con acceso a sistemas de produccion.",
        body_style
    ))

    story.append(Paragraph("3. Evaluacion previa de proveedores (due diligence)", heading1_style))
    story.append(Paragraph(
        "Antes de contratar a un nuevo proveedor, NEXORA realiza una evaluacion que incluye:",
        body_style
    ))
    due_diligence = [
        "Verificacion de certificaciones relevantes: ISO 27001 (seguridad de la informacion), "
        "SOC 2 Type II (controles de servicio), ISO 27701 (gestion de privacidad), ENS (Esquema Nacional de Seguridad).",
        "Revision de la politica de privacidad y condiciones de tratamiento de datos del proveedor.",
        "Evaluacion de la ubicacion geografica de los centros de datos y las implicaciones para "
        "transferencias internacionales.",
        "Verificacion de la capacidad del proveedor para cumplir con los requisitos del RGPD (art. 28) "
        "y del AI Act (cuando aplique).",
        "Evaluacion financiera basica (solvencia, continuidad de negocio).",
        "Revision de incidentes de seguridad previos reportados publicamente."
    ]
    for d in due_diligence:
        story.append(Paragraph(f"• {d}", bullet_style))

    story.append(Paragraph("4. Registro de proveedores activos", heading1_style))
    story.append(Paragraph(
        "NEXORA mantiene un registro actualizado de todos los proveedores con acceso a datos personales "
        "o sistemas de IA. A fecha de enero de 2026, los principales proveedores son:",
        body_style
    ))

    # Tabla de proveedores
    data = [
        ['Proveedor', 'Servicio', 'Datos accedidos', 'Ubicacion datos', 'DPA vigente'],
        ['Amazon Web Services', 'Infraestructura cloud (EC2, S3, RDS)', 'Todos (cifrados en transito y reposo)', 'eu-west-1 (Irlanda)', 'Si — CCT + medidas adicionales'],
        ['Google Workspace', 'Correo, documentos, calendario', 'Datos de contacto, documentos internos', 'UE (configurado)', 'Si — CCT'],
        ['OpenAI', 'API GPT-4o para asistente de productividad', 'Prompts anonimizados, sin datos personales directos', 'EEUU', 'Si — DPA + zero retention policy'],
        ['Anthropic', 'API Claude para analisis de documentos', 'Documentos de negocio (sin datos personales directos)', 'EEUU', 'Si — DPA + CCT'],
        ['HubSpot', 'CRM y marketing automation', 'Datos de contacto de leads y clientes', 'EEUU (UE para EU customers)', 'Si — CCT'],
        ['Personio', 'Gestion de RRHH', 'Datos de empleados (nominas, contratos, ausencias)', 'Alemania (UE)', 'Si — art. 28 RGPD'],
        ['Slack (Salesforce)', 'Comunicacion interna', 'Mensajes internos, archivos compartidos', 'EEUU', 'Si — CCT + cifrado'],
        ['ChromaDB (self-hosted)', 'Base de datos vectorial para RAGs', 'Embeddings de documentos internos', 'On-premise (Madrid)', 'N/A — infraestructura propia'],
        ['Ollama (self-hosted)', 'Runtime de LLMs locales', 'Documentos procesados localmente', 'On-premise (Madrid)', 'N/A — infraestructura propia'],
    ]

    table = Table(data, colWidths=[80, 100, 105, 80, 95])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#1a3c5e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#ffffff')),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#ffffff'), HexColor('#f5f5f5')]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(table)

    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "Nota: los proveedores self-hosted (ChromaDB, Ollama) se ejecutan en la infraestructura propia "
        "de NEXORA en el data center de Madrid. No requieren DPA externo ya que no implican transferencia "
        "de datos a terceros. Sin embargo, se documentan igualmente en el registro por transparencia.",
        body_style
    ))

    story.append(Paragraph("5. Requisitos contractuales obligatorios", heading1_style))
    story.append(Paragraph(
        "Todo contrato con proveedores que accedan a datos personales debe incluir un Acuerdo de "
        "Procesamiento de Datos (DPA) conforme al articulo 28 del RGPD, que contenga como minimo:",
        body_style
    ))
    requisitos = [
        "Objeto y duracion del tratamiento, naturaleza y finalidad, tipo de datos y categorias de interesados.",
        "Obligacion de tratar los datos unicamente siguiendo instrucciones documentadas del responsable.",
        "Garantia de confidencialidad del personal con acceso a los datos.",
        "Medidas tecnicas y organizativas de seguridad adecuadas al riesgo.",
        "Condiciones para la subcontratacion (autorizacion previa general o especifica).",
        "Asistencia al responsable en la atencion de solicitudes de ejercicio de derechos.",
        "Asistencia en el cumplimiento de las obligaciones de seguridad, notificacion de brechas, EIPD y consulta previa.",
        "Supresion o devolucion de los datos al finalizar la prestacion del servicio.",
        "Puesta a disposicion de toda la informacion necesaria para demostrar el cumplimiento y facilitar auditorias."
    ]
    for r in requisitos:
        story.append(Paragraph(f"• {r}", bullet_style))

    story.append(Paragraph("6. Supervision continua", heading1_style))
    story.append(Paragraph(
        "NEXORA realiza una revision anual de todos los proveedores criticos (aquellos con acceso a datos "
        "especialmente protegidos o que soporten servicios esenciales). La revision incluye: verificacion "
        "de vigencia de certificaciones, revision de cambios en las politicas de privacidad del proveedor, "
        "revision de incidentes de seguridad reportados, y verificacion de que el DPA sigue siendo adecuado. "
        "Adicionalmente, NEXORA se reserva el derecho de auditar a cualquier proveedor con un preaviso "
        "minimo de 30 dias.",
        body_style
    ))

    story.append(Paragraph("7. Proveedores de IA — Requisitos adicionales", heading1_style))
    story.append(Paragraph(
        "Para proveedores de sistemas o servicios de IA, NEXORA exige adicionalmente:",
        body_style
    ))
    ia_requisitos = [
        "Declaracion de conformidad con el AI Act para sistemas de alto riesgo desplegados en la UE.",
        "Compromiso de no utilizar los datos de NEXORA o sus clientes para entrenar o mejorar modelos propios "
        "(zero data retention o clausula equivalente).",
        "Transparencia sobre el modelo utilizado, su version y sus limitaciones conocidas.",
        "Informacion sobre la ubicacion geografica del procesamiento de inferencia.",
        "Compromiso de notificacion en caso de cambio significativo en el modelo o sus condiciones de servicio.",
        "Para LLMs: confirmacion de que no se inyectan outputs publicitarios o de terceros en las respuestas."
    ]
    for i in ia_requisitos:
        story.append(Paragraph(f"• {i}", bullet_style))

    story.append(Paragraph("8. Procedimiento ante incumplimiento", heading1_style))
    story.append(Paragraph(
        "Si se detecta un incumplimiento por parte de un proveedor: (1) Se notifica formalmente al proveedor "
        "requiriendo la subsanacion en un plazo de 15 dias habiles. (2) Si no se subsana, se suspende el acceso "
        "a datos de forma inmediata. (3) Se evalua la viabilidad de migrar a un proveedor alternativo. "
        "(4) Se documenta el incumplimiento y se comunica al Comite de Cumplimiento. (5) Si el incumplimiento "
        "afecta a datos personales, se evalua la necesidad de notificacion a la AEPD conforme al articulo 33 RGPD.",
        body_style
    ))

    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "<b>Aprobado por:</b> Direccion Juridica y DPO de NEXORA S.L.<br/>"
        "<b>Fecha:</b> 1 de febrero de 2026<br/>"
        "<b>Version:</b> 2.1<br/>"
        "<b>Proxima revision:</b> Febrero de 2027",
        body_style
    ))


# ═══════════════════════════════════════════════════════════════════════════
# MAIN — Generar los 4 PDFs
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Genera los 4 PDFs internos de NEXORA para el corpus RAG"
    )
    parser.add_argument(
        "--output-dir", default=DEFAULT_OUTPUT_DIR,
        help=f"Carpeta destino (por defecto: {DEFAULT_OUTPUT_DIR})"
    )
    args = parser.parse_args()

    OUTPUT_DIR = args.output_dir
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Generando corpus NEXORA Legal Compliance en {OUTPUT_DIR}/...\n")

    build_doc(
        "01_NEXORA_Protocolo_Cumplimiento_Normativo_v3.2.pdf",
        "Protocolo Interno de Cumplimiento Normativo",
        "NEXORA S.L. — Version 3.2 — Enero 2026",
        doc1_protocolo
    )

    build_doc(
        "02_AI_Act_Resumen_Ejecutivo.pdf",
        "Reglamento Europeo de Inteligencia Artificial (AI Act)",
        "Resumen ejecutivo — Reglamento (UE) 2024/1689 — Actualizado a 2026",
        doc2_ai_act
    )

    build_doc(
        "03_RGPD_Derechos_Interesado_Extracto.pdf",
        "Derechos del Interesado — RGPD",
        "Extracto practico del Capitulo III del Reglamento (UE) 2016/679 — Adaptado a NEXORA S.L.",
        doc3_rgpd
    )

    build_doc(
        "04_NEXORA_Politica_Proveedores_Subcontratacion.pdf",
        "Politica de Proveedores y Subcontratacion",
        "NEXORA S.L. — Version 2.1 — Febrero 2026",
        doc4_proveedores
    )

    print(f"\n✓ 4 documentos generados en {OUTPUT_DIR}/")
    print("  Listos para indexar en ChromaDB con el script de indexacion.")
