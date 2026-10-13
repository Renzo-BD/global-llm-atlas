# Global LLM Atlas — revisión de candidatos y cambios (2026-10-13)

Este informe es una **cola de curación**, no una afirmación de verificación independiente ni una actualización automática de `data/llms.json`. La base canónica v0.3.0 mantiene 65 puntos de acceso y 33 asociaciones geográficas hasta completar las comprobaciones.

## Candidatos nuevos por país

| País | Servicio | Web declarada | Tipo por comprobar | Estado de curación |
|---|---|---|---|---|
| Pakistán | PakBot | https://www.pakbot.online/ | Asistente; modelo subyacente desconocido | UNVERIFIED |
| Pakistán | Warisha AI | https://warishaai.com/ | Asistente; modelo subyacente desconocido | UNVERIFIED |
| Bangladés | Moyna AI | https://moyna.ai/en | Plataforma multimodelo | UNVERIFIED |
| Bangladés | Assistant.bd | https://assistant.bd/ | Plataforma basada en terceros; beta | UNVERIFIED |
| Camboya | AngkorAI | https://www.angkorai.ai/ | Asistente; límite gratuito contradictorio (30/100 mensajes diarios) | UNVERIFIED |
| Nepal | GuffGPT | https://guffgpt.com/ | Asistente; modelo subyacente desconocido | UNVERIFIED |
| Nepal | Shree AI | https://ai.meetshree.com/ | Asistente; modelo subyacente desconocido | UNVERIFIED |
| Sri Lanka | Cladik | https://cladik.com/ | Asistente; modelo subyacente desconocido | UNVERIFIED |

**Antes de promover a ACTIVE:** comprobar dominio oficial, interacción web real, gratuidad sostenida (no solo prueba temporal), inglés/español, país de desarrollo y operador, dependencia de terceros, restricciones regionales y fecha/evidencia de comprobación.

## Revisión de registros existentes

- **Estados Unidos — ChatGPT, Claude, Gemini:** mantener sus registros existentes. Verificar cambios recientes en modelos disponibles y condiciones del nivel gratuito; no inferir que una versión de modelo constituye una nueva plataforma.
- **Francia — Le Chat / Mistral:** mantener el acceso conversacional existente. Registrar versiones nuevas de modelos API en una capa de novedades, no como un segundo chatbot gratuito.
- **Arabia Saudita — HUMAIN Chat:** revisar acceso internacional y limitaciones geográficas antes de modificar ACTIVE.
- **Uganda — Sunbird AI / Sunflower:** candidato de seguimiento de modelos lingüísticos; falta comprobar interfaz conversacional pública en inglés/español y nivel gratuito.
- **Estados Unidos — Reflection AI / Beam:** candidato de seguimiento de modelo/API, no promover sin chat web gratuito verificado.
- **Perú — Jeimy AI:** candidato pendiente de verificar país/operador, interfaz pública, gratuidad, modelos propios frente a orquestación de terceros, y enlaces oficiales. No atribuir pesos propios sin pruebas.

## Resultado

- 8 candidatos nuevos en 5 países, todos pendientes de verificación semántica.
- 0 bajas definitivas documentadas en esta revisión.
- 0 cambios automáticos de estado en la base canónica.
- No se modifica `data/android.json` sin comprobación específica de distribución Android.

## Política de actualización

Las afirmaciones de resúmenes previos no sustituyen una comprobación actual. Registrar evidencia oficial por servicio, diferenciar `modelo propio`, `fine-tune` y `plataforma de terceros`, y preservar el historial de cambios. El atlas actual solo contiene una fracción de los países del mundo; **no** presentar esta revisión como auditoría exhaustiva mundial.
