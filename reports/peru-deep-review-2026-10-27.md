# Perú — búsqueda profunda y decisiones de curación

Fecha: **27 de octubre de 2026**. Actualización del Atlas: **v0.7.0**.

## Resultado

- **Un candidato nuevo en el directorio:** [Theus](https://theus.pe/), plataforma peruana que orquesta modelos de terceros. Estado **UNVERIFIED** hasta probar una conversación.
- **Nueve registros nuevos de seguimiento**, que elevan a doce la lista de investigación: SipánGPT, KUNTUR, ChasquiAyuda, PeruMedQA, IA-UPCH, OPTIMACO-UNMSM, integración LLM–LMS de UTP, Rosettia y LaCima.
- **Cambio verificable de acceso:** CatIA y el Catálogo IA Perú muestran una restricción temporal para personas autorizadas.
- No se confirmó un nuevo modelo fundacional peruano de propósito general, entrenado desde cero, con chat público operativo. Sí hay artefactos de adaptación, investigación y datos que justifican un seguimiento mucho más concreto.
- Totales del directorio: **93 puntos de acceso, 92 servicios únicos, 43 asociaciones de país, 29 UNVERIFIED**. Android nativo/regional permanece en **38**. La lista de investigación se cuenta por separado.

La novedad es respecto del seguimiento anterior del Atlas; varios proyectos se publicaron antes de esta búsqueda.

## Modelos y adaptaciones con evidencia concreta

| Proyecto | Evidencia | Clasificación y acceso |
|---|---|---|
| **SipánGPT** | [Modelo Llama v0.5](https://huggingface.co/ussipan/Llama-3.2-SipanGPT-v0.5-GGUF), [LoRA](https://huggingface.co/ussipan/Llama-3.2-SipanGPT-v0.5-lora), [dataset V2](https://huggingface.co/datasets/ussipan/sipangpt-V2). El publicador ussipan se identifica con la Universidad Señor de Sipán y acredita a Jhan Gómez P. | Adaptación de Llama 3.2 1B para información universitaria. Hay pesos y formatos locales; no se verificó un chat web público ni un aval institucional independiente del perfil del publicador. |
| **KUNTUR** | [Modelo](https://huggingface.co/somosnlp/kuntur-peru-legal-es-gemma-2b-it-merged), [presentación SomosNLP 2024](https://somosnlp.org/blog/proyectos-hackathon-2024), [demo](https://huggingface.co/spaces/somosnlp/KUNTUR). | Ajuste de Gemma-2B-IT con LoRA/QLoRA sobre preguntas de la Constitución peruana. El publicador identifica a Alonso Quispe. Pesos publicados; demo con **RUNTIME_ERROR**, corroborado en la API del proveedor. No se agrega como chat operativo. |
| **ChasquiAyuda** | [Adaptador público](https://huggingface.co/somosnlp-hackathon-2026/chaskiayuda-model-dpo), con archivos adapter_model.safetensors y adapter_config.json. | Postentrenamiento DPO + QLoRA de Qwen2.5-7B-Instruct para respuesta humanitaria en español enfocada en Perú. Proyecto de hackathon; ciudadanía/afiliación de autores no corroborada. [Demo](https://huggingface.co/spaces/somosnlp-hackathon-2026/chaskiayuda-demo) y API devolvieron **401**. |
| **PeruMedQA** | [Artículo publicado el 18-03-2026](https://link.springer.com/article/10.1007/s40670-026-02692-w) y [repositorio de autores](https://github.com/rodrigo-carrillo/PeruMedQA). | Benchmark de 8.380 preguntas médicas peruanas y adaptación PEFT/LoRA de MedGemma-4B. Colaboración internacional con afiliación de Manuel Castillo-Cara a la Universidad de Lima. Código/datos/resultados publicados; pesos adaptados descargables y chat público no establecidos. |
| **Rosettia** | [Adaptador NLLB](https://huggingface.co/somosnlp-hackathon-2026/rosettia-quy-gspo-nllb13b-lora), [rama Qwen](https://huggingface.co/Thermostatic/rosettia-chanka-4b-base). | Traducción español → quechua chanka/ayacuchano mediante adaptación de modelos existentes. Enfoque lingüístico peruano, sin inferir nacionalidad de los autores ni universidad propietaria. No es un nuevo asistente general. |

### SipánGPT: la actualización de 2026 sí merece seguimiento

La API pública del Hub muestra el modelo Llama v0.5 modificado por última vez el **23-12-2024**. El dataset V2 fue modificado el **19-09-2026** y declara **350 ejemplos de entrenamiento y 50 de prueba**.

También existe [sipangpt-gemma-4-e2b-it-gguf](https://huggingface.co/ussipan/sipangpt-gemma-4-e2b-it-gguf), modificado el **20-09-2026**, con archivos GGUF y proyector multimodal. Su ficha describe una conversión de formato: **el nombre del repositorio y los archivos no bastan para afirmar que hubo un nuevo ajuste fino**.

No se descargaron ni ejecutaron los pesos. Los 304.000 diálogos de la versión antigua son una afirmación del publicador, distinta de los 400 ejemplos declarados en V2.

### Límites de las afirmaciones técnicas

En ChasquiAyuda, las cantidades de la tabla de fuentes no cuadran con el total de pares anunciado, y un ejemplo de carga apunta a un adaptador con nombre distinto del repositorio DPO. Sus métricas de recompensa son reportadas por el equipo; no equivalen a exactitud verificada de orientación durante emergencias.

Rosettia declara que no hizo evaluación con hablantes nativos y que sus pruebas son de investigación. PeruMedQA evalúa exámenes: sus resultados no establecen validación clínica. KUNTUR usa un corpus constitucional delimitado: no se asume cobertura vigente de todo el derecho peruano.

## Universidades: proyectos, capacidad y límites de evidencia

| Institución | Evidencia relevante | Qué permite concluir |
|---|---|---|
| **Cayetano Heredia** | [IA-UPCH](https://ciencias.cayetano.edu.pe/noticias/laboratorio-de-inteligencia-artificial/), anuncio del 22-09-2025: investigación con modelos fundacionales, LLM, variantes GPT/abiertas y multimodalidad en salud; infraestructura de entrenamiento/despliegue. Coordinación: Moises Meza Rodriguez. | Hallazgo más sólido que la referencia anterior a un curso. Confirma capacidad y líneas de trabajo; no acredita un modelo fundacional institucional liberado. |
| **UNMSM** | [OPTIMACO](https://vrip.unmsm.edu.pe/grupo_investigacion/optimaco/) registra el proyecto **B251412668e** sobre grafos de conocimiento para entrenamiento de LLM. | Proyecto identificable, con código verificable. La ficha no establece arquitectura, corpus, pesos liberados ni un chat. |
| **UTP** | [Registro oficial 2025-2, página 22](https://www.utp.edu.pe/web/sites/default/files/2026-01/Registro-de-proyectos-de-investigacion-Transparencia-2025-2.pdf): **P-2025-LIM-09**, integración de LLM con LMS universitarios. Investigador principal: **Adolfo Jorge Prado Ventocilla**; sede Ate. | Investigación aplicada por integración modular/APIs; producto esperado: prototipo LMS. El registro consigna abril 2025–abril 2026 y “en ejecución” en su corte: no se infiere el estado actual. Sus metas de reducción de carga docente no son resultados medidos. |
| **Universidad de Lima** | Afiliación institucional en el artículo publicado de PeruMedQA. | Evidencia de participación en adaptación/evaluación concreta; no propiedad exclusiva del modelo ni cómputo íntegramente realizado en Perú. |
| **Universidad Señor de Sipán** | Perfil ussipan, modelo Llama, datasets y artefacto GGUF reciente. | Asociación institucional declarada por el publicador. Falta confirmar aval formal universitario y despliegue vigente. |
| **PUCP** | [URB-LLM](https://cris.pucp.edu.pe/es/projects/la-producci%C3%B3n-y-consolidaci%C3%B3n-del-espacio-urbano-informal-a-trav%C3%A9/) y [Encuentro ICI 2026 sobre lenguas originarias](https://encuentroici.pucp.edu.pe/event/lenguas-originarias-del-peru-y-tecnologias-computacionales/). | Aplicación de LLM y desarrollo de recursos lingüísticos. No confundir documentación lingüística, reconocimiento o un proyecto aplicado con un modelo generativo propio liberado. Evidencia institucional indexada; no reproducción técnica. |
| **Universidad del Pacífico** | [Proyecto de comprensión lectora](https://ia.up.edu.pe/proyecto/ampliando-la-comprension-lectora-a-traves-de-un-sistema-inteligente-basado-en-la-arquitectura-gpt/) y [presentación de la colaboración con PUC-Rio](https://ia.up.edu.pe/estudiantes-de-ingenieria-de-la-informacion-desarrollan-proyecto-para-ampliar-la-comprension-lectora-con-ayuda-de-un-chatbot/). | Trabajo de adaptación/aplicación educativa. No nuevo chat general ni modelo fundacional confirmado. |
| **UNI / INICTEL-UNI** | [Nueva carrera](https://portal.uni.edu.pe/index.php/rss/item/8469-uni-aprueba-carrera-ingenieria-inteligencia-artificial-fiis-amplia-oferta-academica), [coloquio sudamericano](https://www.gob.pe/institucion/uni/noticias/1389926-uni-realizo-coloquio-internacional-sobre-inteligencia-artificial-y-perspectivas-de-desarrollo-en-america-del-sur) y [LABIAR](https://www.fiis.uni.edu.pe/laboratorios/labiar). Se mantiene la referencia previa al uso de LLM abierto en INICTEL. | Formación, infraestructura y aplicaciones. El anuncio de un instituto, una carrera o un coloquio no demuestra por sí solo pesos propios o chat de un LLM institucional. |
| **UNAP / Puno** | [LaCima FINESI](https://lacima.edu.pe/es/investigacion) entrega página HTTP 200 con línea de modelos de lenguaje, RAG verificable, quechua y aimara. | Nueva pista de laboratorio, sustentada en su propia identificación institucional. No modelo específico liberado confirmado. |
| **UTEC** | [Registro académico sobre pruebas unitarias con LLM abiertos](https://alicia.concytec.gob.pe/vufind/Record/UTEC_79250301398ee374615a1e68b717ffd8/Details). | Investigación sobre modelos existentes. Se excluyeron resultados de UTEC Uruguay y El Salvador para evitar atribuciones erróneas a Perú. |
| **USMP** | [Registro de tesis sobre asistente para capacitación empresarial](https://alicia.concytec.gob.pe/vufind/Record/USMP_4c3ca1bf45e4b44f6887449492cf5eb8), además de divulgación sobre agentes. | Pista aplicada; el resumen no establece un nuevo modelo fundacional ni servicio público. |
| **UNSA / UCSP / UPC / UNSAAC** | Búsquedas dirigidas a sus dominios recuperaron formación, uso/evaluación de modelos y trabajos aplicados. | No se verificó en este pase un nuevo modelo fundacional institucional con pesos y chat público. Esto no demuestra que no existan proyectos no indexados o en desarrollo. |

## Gobierno

**CatIA cambió de accesibilidad.** Tanto [el catálogo](https://catalogoia.servicios.gob.pe/) como [la ruta CatIA](https://catalogoia.servicios.gob.pe/catia) redirigen a un formulario que anuncia disponibilidad temporal solo para personas autorizadas. Se reprodujo por GET directo, con HTTP 200 en la página restringida. La ficha antigua indexada no demuestra acceso conversacional actual. Se añade esta evidencia al registro existente, sin inferir cierre definitivo ni cambiar automáticamente su estado.

El [documento ENIA 2026–2030 de PCM](https://www.gob.pe/institucion/pcm/informes-publicaciones/8408055-estrategia-nacional-de-inteligencia-artificial-2026-2030) y [la publicación oficial de su aprobación](https://busquedas.elperuano.pe/dispositivo/NL/2511535-1) sustentan una estrategia y un catálogo; no son evidencia de que ya se haya liberado un LLM nacional operativo. La página Gob.pe del documento devolvió 418 en esta consulta; se distingue la ficha indexada de una lectura completa de su anexo.

La [cooperación Perú–Chile](https://www.gob.pe/institucion/pcm/noticias/1294929-peru-y-chile-impulsan-alianza-estrategica-para-desarrollar-inteligencia-artificial-propia-en-la-region) corresponde al proyecto **regional** LatamGPT. No se crea un segundo modelo peruano por participación o nacionalidad de investigadores. Copuchat conserva su asociación y registro existentes.

## Independientes y empresas

### Theus — incorporación como candidato

Fuentes: [producto](https://theus.pe/), [precios](https://theus.pe/precios/), [compañía](https://theus.pe/nosotros/), [chat](https://theus.pe/chat-theus/) y [Astratech](https://astratech.pe/).

El publicador identifica a Marketrix S.A.C. / Astratech y a Mariano Suquilanda Gallo como fundador; describe diseño y operación desde Lima. La portada ofrece un cuadro de conversación sin cuenta y el plan Free tiene uso limitado con ventanas de cinco horas/siete días, sin tarjeta. El producto utiliza modelos de terceros, con selección/orquestación TITAN; el nombre comercial o la opción de afinar modelos no demuestra un modelo fundacional peruano.

GET a la portada devolvió 200; https://chat.theus.pe/ redirigió a /chat/ y devolvió una pantalla de carga de cuenta. No se envió una pregunta, no se creó cuenta y no se ejecutaron instaladores. Se agrega **pe-theus**, con enlace a la portada que ofrece la prueba pública, registro opcional y estado UNVERIFIED.

### Jeimy y otras pistas

Jeimy conserva el resultado previo de presentación alcanzable y conversación no verificada. En esta profundización, /modelos y docs.jeimy.ai/api/modelos devolvieron **403**. Se preserva la incertidumbre sobre procedencia técnica; los nombres Colibrí/Águila/Apu no se atribuyen a modelos entrenados desde cero.

Yachay SLM y QuBERT continúan en el seguimiento previo, sin duplicación. Monolith-1.0 conserva la exclusión documentada: no se rehabilita por una mención ambigua a “Monolito”.

La noticia de TVPerú sobre DOX.AI es una pista periodística con acceso 403 en este pase. No se estableció una URL atribuible del operador ni un chat con condiciones verificadas, por lo que no se agrega.

## Android

No se añadió ninguna aplicación nativa. Se revisaron fuentes de producto y búsquedas específicas para Theus, SipánGPT y Jeimy. La coincidencia de un desarrollador llamado Astratech en Google Play no prueba que una app pertenezca a Theus. Las descargas Windows/macOS, un CLI, GGUF o un navegador móvil no equivalen a un APK oficial.

## Método y verificaciones

Revisión de fuentes institucionales, fichas de modelos, metadatos públicos del Hub, artículos originales y repositorios de autores. Los metadatos confirman presencia de artefactos y fechas, sin reproducir entrenamiento ni evaluar calidad. No se sortearon restricciones de acceso.

Los hallazgos se guardan en data/research-peru.json y en este informe. Las entradas antiguas conservan sus fuentes y fechas; los nuevos registros llevan revisión individual. JSON/CSV del directorio se sincronizan, se preservan capacidades desconocidas y se ejecuta el validador del repositorio antes de publicar.
