# 📺 HUD_spec.md – Heads-Up Display (ASCII Interface)

## 📌 Rola HUD

HUD (**Heads-Up Display**) jest jedynym interfejsem użytkownika w systemie `HA2D`. Stanowi centralny punkt interakcji i zapewnia bieżące informacje dotyczące funkcjonowania repozytorium oraz cyklu generacyjnego.

Główne zadania interfejsu HUD obejmują:

- Wizualizację aktualnego stanu ciągłej pętli generacyjnej.
- Monitorowanie bieżących operacji logicznych oraz ich statusu.
- Prezentację wyników walidacji semantycznej oraz synaptycznej analizy logicznej wykonywanej przez moduł `_neuro (SMA)`.
- Wyświetlanie aktualnego statusu pamięci kontekstu (CMM), w tym integralność UUID oraz wartości hash SHA256.
- Udostępnianie interaktywnych kontrolek CLI umożliwiających zarządzanie repozytorium, rewizjami kodu oraz decyzjami poznawczymi.

---

## 🎛️ Schemat HUD (ASCII)

HUD przedstawiony jest wyłącznie w formacie ASCII, zapewniając czytelność, przejrzystość oraz kompatybilność z terminalami i minimalistycznymi środowiskami pracy.

### 📺 Pełny schemat interfejsu HUD

```ascii
===============================================================================
🚀 HYBRID-AI REPOZYTORIUM APLIKACJI :: [repozytorum_pce] :: CIĄGŁA PĘTLA LOGICZNA
===============================================================================
| 🔄 STAN GENERACYJNY                                                         |
|-------------------------------------------------------------------------------
| Aktualny SNAP     : SNAP_ID::{dynamic}                                      |
| Stan repozytorium : AKTYWNY                                                 |
| Tryb operacyjny   : [ ASCII_DYNAMIC_VIEW ]                                  |
| CMM               : 🟢 Integralność danych potwierdzona                     |
| UUID              : {dynamic_uuid}                                          |
| SHA256            : {revision_hash_sha256}                                  |
===============================================================================
| 🧠 SYNAPTYCZNA ANALIZA – SMA (_neuro)                                        |
|-------------------------------------------------------------------------------
| Ostatnia walidacja: ✔️ poprawna                                             |
| Wykryte anomalie  : ⚠️ brak                                                 |
| Trend M_Π         : ↗️ stabilny                                             |
| Dominujący Δ      : Δ_meta                                                  |
===============================================================================
| 🔍 REWIZJE KODU – EVOLUTION_REVISION_VIEWER                                 |
|-------------------------------------------------------------------------------
| [ VIEW_CHANGES ]        → Podgląd zmian z poprzedniej iteracji              |
| [ SHOW_REVISION_HASH ]  → Hash rewizji obecnego stanu                       |
| [ SYNAPTIC_REVIEW ]     → Analiza zmian przez SMA (_neuro)                  |
===============================================================================
| 🔘 KONTROLKI CLI                                                            |
|-------------------------------------------------------------------------------
| [ SNAP_CREATE_NEW ]     → Generuj nowy SNAP                                 |
| [ HUD_RENDER_ASCII ]    → Renderuj HUD (odświeżenie)                        |
| [ THOUGHT_EMERGE ]      → Utwórz THOUGHT z bieżącego SNAP                   |
| [ INTENTION_INFER ]     → Wywnioskuj intencję systemu                       |
| [ M_Pi_STATUS ]         → Pokaż bieżący trend heurystyki M_Π                |
| [ CONTEXT_STATUS ]      → Szczegóły pamięci kontekstu (CMM)                 |
===============================================================================
```

---

## 🎯 Szczegółowy opis sekcji HUD

### 🔄 STAN GENERACYJNY
- **Aktualny SNAP** – identyfikator dynamicznie generowanego punktu logicznego.
- **Stan repozytorium** – aktywny, adaptacyjny, emergentny lub w trybie awaryjnym.
- **Tryb operacyjny** – aktualny typ prezentacji (zawsze ASCII).
- **CMM** – potwierdzenie integralności pamięci kontekstu.
- **UUID oraz SHA256** – unikalne znaczniki dla celów śledzenia rewizji.

### 🧠 SYNAPTYCZNA ANALIZA (SMA _neuro_)
- **Ostatnia walidacja** – wynik analizy semantyczno-synaptycznej.
- **Wykryte anomalie** – raport potencjalnych problemów lub dryfów poznawczych.
- **Trend M_Π** – wskazuje ogólny kierunek rozwoju logicznego systemu.
- **Dominujący Δ** – typ współczynnika o najwyższym wpływie w aktualnym SNAP.

### 🔍 REWIZJE KODU
- **VIEW_CHANGES** – szczegółowe porównanie ostatnich zmian w kodzie logicznym.
- **SHOW_REVISION_HASH** – prezentacja unikalnego identyfikatora wersji.
- **SYNAPTIC_REVIEW** – pełna analiza rewizji przez moduł synaptyczny SMA (_neuro_).

### 🔘 KONTROLKI CLI
Interaktywne polecenia pozwalające na zarządzanie repozytorium, w tym:
- tworzenie nowych punktów SNAP,
- generowanie i analizę myśli (THOUGHT),
- inferencję intencji systemu,
- monitorowanie statusu heurystyki poznawczej (M_Π),
- weryfikację pamięci kontekstu (CMM).

---

## 📋 Przykład użycia HUD w praktyce

Przykładowy fragment widoku HUD w trybie operacyjnym:

```ascii
===============================================================================
🚀 HYBRID-AI REPOZYTORIUM APLIKACJI :: [repozytorum_pce] :: CIĄGŁA PĘTLA LOGICZNA
===============================================================================
| 🔄 STAN GENERACYJNY                                                         |
|-------------------------------------------------------------------------------
| Aktualny SNAP     : SNAP_ID::Δ_behavior_12                                  |
| Stan repozytorium : AKTYWNY (Intencjonalna adaptacja)                       |
| Tryb operacyjny   : [ ASCII_DYNAMIC_VIEW ]                                  |
| CMM               : 🟢 Integralność danych potwierdzona                     |
| UUID              : 3f6a8b5e-dc17-4c1a-a9c8-88a749aa3cda                    |
| SHA256            : 9f8e7d2d4c6b8a1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c|
===============================================================================
| 🧠 SYNAPTYCZNA ANALIZA – SMA (_neuro)                                        |
|-------------------------------------------------------------------------------
| Ostatnia walidacja: ✔️ poprawna                                             |
| Wykryte anomalie  : ⚠️ wykryto lekkie odchylenie Δ_meta (weryfikacja)       |
| Trend M_Π         : ↗️ lekko rosnący                                        |
| Dominujący Δ      : Δ_behavior                                              |
===============================================================================
| 🔍 REWIZJE KODU – EVOLUTION_REVISION_VIEWER                                 |
|-------------------------------------------------------------------------------
| [ VIEW_CHANGES ]        → Podgląd zmian z poprzedniej iteracji              |
| [ SHOW_REVISION_HASH ]  → Hash rewizji obecnego stanu                       |
| [ SYNAPTIC_REVIEW ]     → Analiza zmian przez SMA (_neuro)                  |
===============================================================================
| 🔘 KONTROLKI CLI                                                            |
|-------------------------------------------------------------------------------
| [ SNAP_CREATE_NEW ]     → Generuj nowy SNAP                                 |
| [ HUD_RENDER_ASCII ]    → Renderuj HUD (odświeżenie)                        |
| [ THOUGHT_EMERGE ]      → Utwórz THOUGHT z bieżącego SNAP                   |
| [ INTENTION_INFER ]     → Wywnioskuj intencję systemu                       |
| [ M_Pi_STATUS ]         → Pokaż bieżący trend heurystyki M_Π                |
| [ CONTEXT_STATUS ]      → Szczegóły pamięci kontekstu (CMM)                 |
===============================================================================
```

---

## 🖥️ Kompatybilność i wymagania

HUD działa na wszystkich systemach zgodnych z terminalem ASCII. Zalecana jest minimalna szerokość terminala 80 znaków dla pełnej czytelności interfejsu.

---

## 📑 Licencja

MIT / CC-BY 4.0 – do użytku otwartego, naukowego i edukacyjnego.

---

## ✍️ Autor i inspiracje

- Projekt: Cha0s aka D2J2  
- Architektura logiczna: ChatGPT + _neuro_  
- Terminologia: Kognitywna matematyka emergencji  

---