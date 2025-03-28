# 🗂️ context_protocol.md – Context Memory Manager (CMM)

## 📌 Czym jest CMM?

**Context Memory Manager (CMM)** jest mechanizmem zapewniającym trwałe przechowywanie oraz efektywną wymianę danych pomiędzy różnymi instancjami i iteracjami systemu HA2D.

CMM umożliwia repozytorium utrzymywanie ciągłości logicznej i semantycznej, gwarantując integralność oraz spójność przechowywanych informacji pomiędzy kolejnymi iteracjami pętli generacyjnej.

---

## 📑 Struktura przykładowego rekordu pamięci

Każdy rekord pamięci w CMM posiada następującą strukturę:

```json
{
  "uuid": "GENEROWANY_UUID",
  "timestamp": "2025-03-28T10:22:00Z",
  "payload": {
    "repozytorum_pce": {
        "SNAP_VECTOR_SCHEMA": {
            "Δ_corr": "EVAL(SMA_TRACE(INIT))",
            "Δ_structure": "MCV_DIFF(NULL_STATE)",
            "Δ_model": "MODEL_DELTA(INIT)",
            "Δ_meta": "NLP_SEMANTIC_EVAL(∅)",
            "Δ_behavior": "NO_ACTIVITY_YET"
        },
        "M_Pi": "FUNC_M_Pi(Δ_all)",
        "STATUS": "SEED_INITIATED",
        "HUD_MODE": "ASCII_DYNAMIC_VIEW"
    },
    "zmienna_synaptyczna": "Stan startowy"
  },
  "sha256": "SUMA_SHA256"
}
```

**Wyjaśnienie pól:**

- `uuid`: Unikalny identyfikator rekordu generowany automatycznie przez CMM.
- `timestamp`: Znacznik czasu wskazujący moment utworzenia rekordu (format ISO8601 UTC).
- `payload`: Rzeczywisty zapisany stan danych kontekstowych:
  - `repozytorum_pce`: Stan strukturalny repozytorium w danej iteracji.
  - `zmienna_synaptyczna`: Przykładowa dodatkowa zmienna kontekstowa (np. stan początkowy, decyzja, parametr).
- `sha256`: Wartość skrótu kryptograficznego (SHA256) całego payloadu dla zapewnienia integralności danych.

---

## 📜 Dostępne operacje w CMM

System CMM oferuje podstawowy zestaw operacji pozwalających na interakcję z pamięcią kontekstu:

| Operacja                          | Opis operacji                                  | Parametry wejściowe    | Zwracany wynik                 |
|-----------------------------------|-----------------------------------------------|------------------------|--------------------------------|
| `STORE_TO_CONTEXT(payload)`       | Zapisuje nowy rekord kontekstowy               | `payload` (JSON)       | `uuid`, `timestamp`, `sha256` |
| `RETRIEVE_FROM_CONTEXT(uuid)`     | Odczytuje rekord kontekstowy na podstawie UUID | `uuid`                 | Rekord danych (JSON)          |
| `GET_LATEST_CONTEXT_RECORD()`     | Pobiera najnowszy dostępny rekord kontekstowy  | brak                   | Najnowszy rekord danych (JSON)|

---

## 🛠️ Przykłady użycia operacji CMM

### 🔸 Zapisanie nowego kontekstu (`STORE_TO_CONTEXT`)

```pseudo
payload := {
    "repozytorum_pce": {...},
    "zmienna_synaptyczna": "Aktualizacja wartości logicznych"
}

response := CMM.STORE_TO_CONTEXT(payload)

// response zawiera:
{
  "uuid": "8b2e1a04-7f24-4c12-9fd8-a497c3e6a25e",
  "timestamp": "2025-03-28T12:30:00Z",
  "sha256": "a4f8c71...6e9f1a"
}
```

### 🔸 Odczytanie istniejącego kontekstu (`RETRIEVE_FROM_CONTEXT`)

```pseudo
uuid := "8b2e1a04-7f24-4c12-9fd8-a497c3e6a25e"

context_data := CMM.RETRIEVE_FROM_CONTEXT(uuid)

// context_data zawiera pełny rekord:
{
  "uuid": "8b2e1a04-7f24-4c12-9fd8-a497c3e6a25e",
  "timestamp": "2025-03-28T12:30:00Z",
  "payload": {
    "repozytorum_pce": {...},
    "zmienna_synaptyczna": "Aktualizacja wartości logicznych"
  },
  "sha256": "a4f8c71...6e9f1a"
}
```

### 🔸 Pobranie najnowszego rekordu kontekstu (`GET_LATEST_CONTEXT_RECORD`)

```pseudo
latest_context := CMM.GET_LATEST_CONTEXT_RECORD()

// latest_context zawiera najświeższe dane zapisane w CMM
```

---

## 🔐 Weryfikacja integralności danych (SHA256)

Każdy rekord posiada hash SHA256, który pozwala zweryfikować, czy dane kontekstowe nie zostały zmienione lub uszkodzone podczas przesyłu:

```pseudo
hash_check := SHA256(context_data.payload)

IF hash_check == context_data.sha256:
    → integralność potwierdzona ✅
ELSE:
    → wykryto naruszenie integralności ❌
```

---

## 🔄 Rola CMM w cyklu logicznym repozytorium

- **Zapewnienie ciągłości logicznej:**  
  CMM umożliwia zapisanie wszystkich kluczowych stanów logicznych repozytorium oraz ich ponowne przywołanie podczas kolejnych iteracji.

- **Integracja z SMA (_neuro):**  
  Analiza synaptyczna korzysta z rekordów zapisanych w CMM, umożliwiając analizę zmian strukturalnych oraz identyfikację dryfów logicznych i semantycznych.

- **Kontrola wersji (rewizje):**  
  Dzięki mechanizmowi hashowania SHA256, CMM pełni funkcję podstawowego mechanizmu kontroli wersji danych, gwarantując śledzenie zmian między iteracjami.

---

## 📋 Licencja

MIT / CC-BY 4.0 – Otwarte zastosowanie do celów naukowych, edukacyjnych oraz rozwojowych.

---

## ✍️ Autor i inspiracje

- Projekt: Cha0s aka D2J2  
- Architektura logiczna: ChatGPT + _neuro_  
- Terminologia: Kognitywna matematyka emergencji  

---
