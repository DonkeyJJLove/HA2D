# 📊 revision_viewer.md – Evolution Revision Viewer

## 📌 Cel

**Evolution Revision Viewer** to komponent systemu HA2D odpowiedzialny za śledzenie zmian w strukturze logicznej repozytorium. Jego głównym zadaniem jest umożliwienie analizy i porównania kolejnych iteracji kodu oraz stanu logicznego repozytorium.

Dzięki temu narzędziu użytkownik może:

- **Porównać stan repozytorium** pomiędzy poszczególnymi iteracjami.
- **Nadać każdej rewizji unikalny hash** (SHA256) zapewniający integralność oraz jednoznaczną identyfikację zmian.
- **Wizualizować różnice** pomiędzy iteracjami w formacie podobnym do IDE (linie, różnice, komentarze).

---

## 📎 Widok HUD (ASCII)

Interfejs Revision Viewer jest integralną częścią interfejsu ASCII HUD, zapewniając użytkownikowi intuicyjną obsługę:

```ascii
===============================================================================
| 🔍 REWIZJE KODU – EVOLUTION_REVISION_VIEWER                                  |
|------------------------------------------------------------------------------|
| [ VIEW_CHANGES ]           → Podgląd zmian z poprzedniej iteracji            |
| [ SHOW_REVISION_HASH ]     → Hash rewizji obecnego stanu                     |
| [ SYNAPTIC_REVIEW ]        → Analiza zmian przez SMA (_neuro)               |
===============================================================================
```

---

## 🎛️ Dostępne funkcjonalności

| Funkcja                 | Opis funkcjonalności                             | Wynik działania                              |
|-------------------------|--------------------------------------------------|----------------------------------------------|
| `VIEW_CHANGES`          | Wyświetlenie szczegółowych zmian względem poprzedniej iteracji | Widok różnic linii kodu (± diff)             |
| `SHOW_REVISION_HASH`    | Wygenerowanie i wyświetlenie unikalnego hasha SHA256 dla aktualnej rewizji | Hash rewizji: SHA256                         |
| `SYNAPTIC_REVIEW`       | Synaptyczna analiza zmian dokonywana przez SMA (_neuro) | Raport synaptycznej analizy zmian            |

---

## 📑 Przykładowa reprezentacja zmian kodu (VIEW_CHANGES)

Widok prezentowany użytkownikowi przedstawia różnice linii kodu pomiędzy iteracjami, analogicznie jak w IDE:

```diff
12 │  {
13 │    "Δ_corr": "EVAL(SMA_TRACE(INIT))",
-14 │    "Δ_structure": "MCV_DIFF(NULL_STATE)",
+14 │    "Δ_structure": "MCV_DIFF(NEW_BASELINE_STATE)",
15 │    "Δ_model": "MODEL_DELTA(INIT)",
+16 │    "Δ_meta": "NLP_SEMANTIC_EVAL(SNAPSHOT)",
17 │    "Δ_behavior": "NO_ACTIVITY_YET"
18 │  }
```

- `-` oznacza linie usunięte.
- `+` oznacza linie dodane lub zmienione.

---

## 🗝️ Hashowanie rewizji (SHA256)

Każdy stan repozytorium jest identyfikowany unikalnym hashem SHA256:

```pseudo
current_state_payload := {
    "SNAP_VECTOR_SCHEMA": {...},
    "HUD_STATE": {...},
    "M_Pi": {...}
}

revision_hash := SHA256(current_state_payload)

// przykładowy wynik:
revision_hash = "a4f8c719e7bf17c2b1fabc145d7369e04a1a6d8d59a9c1e3d3b5f66f3e6e9f1a"
```

Ten hash jest prezentowany użytkownikowi po wybraniu funkcji `[SHOW_REVISION_HASH]`.

---

## 🧠 Synaptyczna analiza rewizji (SYNAPTIC_REVIEW)

Każda zmiana jest również analizowana synaptycznie przez SMA (_neuro):

```ascii
╭─────────────────────────────────────────────────────────────╮
│ 📡 SYNAPTIC REVIEW                                          │
├─────────────────────────────────────────────────────────────┤
│ Dominująca zmiana      : Δ_structure                        │
│ Potencjalny dryf       : Niski (adaptacja semantyczna)      │
│ Zalecana akcja         : Potwierdzenie nowego baseline'u    │
│ Stabilność poznawcza   : Wysoka (M_Π stabilne)              │
│ Ocena SMA (_neuro)     : ✅ POZYTYWNA                        │
╰─────────────────────────────────────────────────────────────╯
```

Raport ten pozwala użytkownikowi szybko ocenić semantyczną i logiczną jakość dokonanych zmian.

---

## 🔄 Cykl pracy z Evolution Revision Viewer

Cykl typowego użycia narzędzia:

1. Repozytorium generuje nową iterację.
2. Użytkownik wybiera `[VIEW_CHANGES]`, aby zobaczyć szczegóły dokonanych zmian.
3. Użytkownik generuje `[SHOW_REVISION_HASH]` jako podpis wersji.
4. Użytkownik wykonuje `[SYNAPTIC_REVIEW]` w celu walidacji semantycznej zmian.
5. Po analizie użytkownik potwierdza rewizję, a hash jest zapisywany w pamięci CMM.

---

## 📋 Licencja

MIT / CC-BY 4.0 – Otwarte zastosowanie do celów naukowych, edukacyjnych oraz rozwojowych.

---

## ✍️ Autor i inspiracje

- Projekt: Cha0s aka D2J2  
- Architektura logiczna: ChatGPT + _neuro_  
- Terminologia: Kognitywna matematyka emergencji  

---