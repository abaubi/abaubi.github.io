# Planificació del Simulador de Sala de Pintura Multivariable (SCADA)

Aquest document detalla la planificació i el full de ruta acordat per transformar el simulador de la centrifugadora en un simulador de control multivariable per a una **Sala de Pintura de Cotxes** amb control acoblat de **Temperatura** i **Humitat**.

---

## 1. Descripció del Nou Sistema (Planta Física)

El sistema simula una cambra o sala de pintura on s'han de mantenir de forma precisa dues variables ambientals acoblades:
1. **Temperatura ($T$)**: S'utilitza un calefactor elèctric (sortida de control $U_T$: 0-100%) que injecta aire calent.
   * **Rang físic**: 0 ºC a 100 ºC.
   * **Equivalència industrial**: Sonda de temperatura amb senyal de **0-10 V** (on 0 V = 0 ºC i 10 V = 100 ºC).
2. **Humitat ($H$)**: S'utilitza una vàlvula d'injecció de vapor d'aigua humit (sortida de control $U_H$: 0-100%).
   * **Rang físic**: 0% a 100% d'Humitat Relativa (HR).
   * **Equivalència industrial**: Sonda d'humitat amb senyal de **0-10 V** (on 0 V = 0% i 10 V = 100%).

### Efectes d'Acoblament Encreuat (Planta Multivariable)
* **Calefactor ($U_T$)**: Augmenta la temperatura i **disminueix** la humitat de l'ambient (en assecar l'aire).
* **Vàlvula de Vapor ($U_H$)**: Augmenta la humitat i **augmenta** la temperatura (ja que el vapor injectat és calent).

---

## 2. Nova Secció de Càlculs i Equacions

S'inclourà un panell detallat on es descriuran les equacions de la planta i els efectes de l'acoblament:
* **Representació en Tensions**: A l'apartat de càlculs es farà tota la formulació en format **0-10 V** (per facilitar l'aprenentatge de regulació industrial).
* **Gràfiques i Visors**: Mostraran els valors en **unitats físiques** (ºC i % HR) per a una lectura clara de l'estat.
* **Sliders d'Acoblament**:
  * Guany d'acoblament de la Temperatura sobre la Humitat ($K_{TH}$): Defineix quant baixa la humitat per cada volt d'actuació del calefactor.
  * Guany d'acoblament de la Humitat sobre la Temperatura ($K_{HT}$): Defineix quant puja la temperatura per cada volt d'actuació del vapor.

---

## 3. Desacoblament Multivariable (Dues Opcions)

S'implementarà un selector per triar el mètode de desacoblament perquè els alumnes puguin experimentar amb ambdues opcions:
* **Opció A: Desacoblament per Matriu de Guany Directe (Feedforward Decoupling)**:
  * S'utilitzen xarxes de desacoblament creuat on les senyals de control calculades pels PIDs es corregeixen abans d'enviar-se a la planta en funció dels guanys d'acoblament.
* **Opció B: Desacoblament Interactiu Simplificat**:
  * Compensacions directes i intuïtives sumant/restant directament una fracció de l'actuació d'un llaç sobre l'altre.

---

## 4. Millores en Interfície i Control de Simulació

* **Interrupció d'Anti-Windup (AW)**:
  * S'afegiran dos interruptors visuals ràpids per activar/desactivar de manera independent l'Anti-Windup de Temperatura i l'Anti-Windup d'Humitat.
* **Fases del Procés de Pintura**:
  * Reanomenarem les fases per indicar la durada de cadascuna.
  * Cada fase tindrà assignades de manera predefinida les seves consignes ($SP$) de temperatura i humitat, simulant un cicle de treball real de la sala de pintura (ex. Fase 1: Aplicació, Fase 2: Assecat, Fase 3: Refredament).
* **Control de Velocitat de la Simulació**:
  * Botons per accelerar o desaccelerar la velocitat del temps del simulador (x1, x2, x4, x8, x10). Això permetrà veure les corbes tèrmiques i d'humitat (que són més lentes de forma natural) d'una manera molt més ràpida i eficient per a les pràctiques d'aula.
* **Presets de Sintonia PID**:
  * Es determinaran tres configuracions (Estable, Només P, Inestable) de forma interna, adaptades al comportament dinàmic de la nova planta tèrmica/humitat simulada.

---

## 5. Integració MQTT i SCADA Bi-direccional

* **Tòpic Base**: `iesebre/salapintura/`
* **Publicació (Telemetria)**: `iesebre/salapintura/telemetria`
* **Subscripció (Comandes de Control Extern)**: `iesebre/salapintura/cmd`
* **Menús d'Ajuda i Telemetria**: Completament adaptats per fer referència als registres de temperatura (ºC), humitat (%), tensions de consigna/mesura (0-10V) i el funcionament multivariable de la sala de pintura.

---

## 6. Full de Ruta d'Implementació (Properes Passes)

1. **Creació de `planificacio.md`**: *(Completat)*
2. **Confirmació del docent**: Esperar que l'usuari validi aquesta planificació amb la frase `"Endavant, apliquem les millores"`.
3. **Refactorització del fitxer únic `index.html`**:
   * Substituir completament el motor físic de la centrifugadora pel model d'equacions diferencials d'una sala de pintura multivariable.
   * Redissenyar la visualització 2D del Canvas (representació d'un cotxe, aspersió de pintura, escalfador de calor en vermell, vapor en blau).
   * Actualitzar els sliders de configuració, gràfiques de temps real (Temperatura i Humitat), logs, comandes MQTT i configuracions de presets.
4. **Verificació de Compilació i Linter**: Comprovar que el fitxer està lliure d'errors sintàctics i que el servidor arrenca correctament.
