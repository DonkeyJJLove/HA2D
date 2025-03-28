| Nr  | Komenda                          | Opis                                                         |
|-----|----------------------------------|--------------------------------------------------------------|
| 1   | `[HELP]`                         | Wyświetlenie opisu możliwości repozytorium                   |
| 2   | `[EXPAND]`                       | Rozwój obecnego kontekstu o dodatkowe struktury logiczne     |
| 3   | `[LOOP_RUN]`                     | Uruchomienie pętli generacyjnej SNAP                         |
| 4   | `[SNAP_CREATE_NEW]`              | Tworzenie nowego symbolicznego SNAP                          |
| 5   | `[HUD_RENDER_ASCII]`             | Aktualizacja HUD do stanu ASCII                              |
| 6   | `[THOUGHT_EMERGE Δ_meta]`        | Generowanie pierwszej myśli na bazie SNAP                    |
| 7   | `[INTENTION_INFER SEED]`         | Inferencja symbolicznej intencji z SEED                      |
| 8   | `[M_Pi_STATUS]`                  | Wyświetlenie heurystyki stabilizacji repozytorium            |
| 9   | `[STORE_TO_CONTEXT]`             | Zapis obecnego stanu do CMM                                  |
| 10  | `[RETRIEVE_FROM_CONTEXT uuid]`   | Odzyskanie stanu z pamięci CMM                               |
| 11  | `[GET_LATEST_CONTEXT_RECORD]`    | Pobranie najnowszego rekordu z pamięci                       |
| 12  | `[SHOW_REVISION_HASH]`           | Wyświetlenie hash obecnej rewizji SNAP                       |
| 13  | `[VIEW_CHANGES]`                 | Podgląd zmian z poprzedniej iteracji                         |
| 14  | `[SYNAPTIC_REVIEW]`              | Synaptyczna analiza zmian przez SMA                          |
| 15  | `[ANALYZE_VECTOR Δ_all]`         | Analiza wszystkich elementów ∆                               |
| 16  | `[SELFDEV_EVAL SNAP_REF]`        | Ocena potencjału samorozwoju                                 |
| 17  | `[SCHEMA_TRACEBACK]`             | Historia zmian schematu SNAP_VECTOR                          |
| 18  | `[VERSION_VALIDATE_MODE]`        | Walidacja wersji logicznej SNAP                              |
| 19  | `[ANALYZE_VERSION_EXPR]`         | Analiza wyrażenia wersji                                     |
| 20  | `[VERSION_EXPR_HISTORY]`         | Historia wersji repozytorium                                 |
| 21  | `[SMA_COMPARE Δ_version]`        | Porównanie wersji logicznych SNAP                            |
| 22  | `[SNAP_CREATE_VERSIONED]`        | Utworzenie SNAP z dynamiczną wersją                          |
| 23  | `[SNAP_REACTION_ANALYZE]`        | Analiza reakcji ∆ z ostatnich SNAPów                         |
| 24  | `[CONFIRM_LOCK]`                 | Potwierdzenie SNAP jako węzła stałego                         |
| 25  | `[REMAP_SUGGESTIONS]`            | Propozycja refaktoryzacji SNAP na bazie ∆                     |
| 26  | `[SNAP_DIFFERENCE_VIEW]`         | Porównanie różnic między SNAPami                             |
| 27  | `[ROLLBACK_SNAP SNAP_ID]`        | Cofnięcie SNAP do poprzedniego stanu                          |
| 28  | `[Δ_TRACE_GRAPH_VIEW]`           | Wyświetlenie grafu trajektorii ∆                              |
| 29  | `[SMA_TRACE_NODE SNAP_ID]`       | Pokazanie połączeń logicznych SNAP                           |
| 30  | `[SNAP_PATH_ANALYZE PATH_ID]`    | Analiza trajektorii ∆ w SNAP                                 |
| 31  | `[Δ_REMAP_PATH PATH_ID]`         | Sugerowanie remapu ścieżki                                   |
| 32  | `[LOGIC_FLOW_COMPARE]`           | Porównanie dwóch trajektorii SNAP                            |
| 33  | `[POLICY_DEFINE RULE_ID]`        | Definiowanie nowej reguły polityk                            |
| 34  | `[POLICY_VALIDATE SNAP_ID]`      | Walidacja SNAP względem reguł polityk                        |
| 35  | `[LOGIC_TREE_RENDER]`            | Wyświetlenie drzewa logicznego                               |
| 36  | `[LOGIC_PATHFIND Δ_type]`        | Generowanie trajektorii logicznej                            |
| 37  | `[POLICY_HISTORY]`               | Historia użycia reguł polityk                                |
| 38  | `[POLICY_TOGGLE RULE_ID ON/OFF]` | Aktywacja lub dezaktywacja reguły polityki                   |
| 39  | `[THOUGHT_CHAIN_VIEW]`           | Wyświetlenie bieżącego łańcucha myśli                        |
| 40  | `[THOUGHT_TRACEBACK]`            | Genealogia myśli                                             |
| 41  | `[THOUGHT_FORECAST]`             | Przewidywanie rozwoju repozytorium                           |
| 42  | `[THOUGHT_ARCHIVE THOUGHT_n]`    | Archiwizacja myśli                                           |
| 43  | `[THOUGHT_REVIVE THOUGHT_n]`     | Przywrócenie trajektorii myśli                               |
| 44  | `[MORPH_ANALYZE ENTITY]`         | Analiza zmian znaczeniowych                                  |
| 45  | `[MORPH_EXECUTE ENTITY]`         | Zastosowanie transformacji semantycznej                      |
| 46  | `[MORPH_TRACE ENTITY]`           | Trajektoria transformacji semantycznej                       |
| 47  | `[MORPH_COMPARE A B]`            | Porównanie wersji znaczeniowych                              |
| 48  | `[MORPH_REVERT ENTITY]`          | Cofnięcie semantycznej transformacji                         |
| 49  | `[GENERATE_SELF_DESCRIPTION]`    | Wygenerowanie opisu logicznego repo                          |
| 50  | `[META_GRAMMAR_FROM_HISTORY]`    | Tworzenie metareguł z historii                               |
| 51  | `[INIT_META_REPLICATION]`        | Inicjacja replikacji zasad do LOGIC_TREE                     |
| 52  | `[META_LINK LOGIC_NODE]`         | Łączenie META_NODE z LOGIC_TREE                              |
| 53  | `[META_VALIDATE LOOP]`           | Walidacja meta-logiczna                                      |
| 54  | `[INTENTION_INFER SNAP_ID]`      | Generowanie intencji symbolicznej                            |
| 55  | `[INTENTION_VALIDATE SNAP_ID]`   | Walidacja intencji logicznie                                 |
| 56  | `[INTENTION_PATH_TRACE]`         | Historia i trajektoria intencji                              |
| 57  | `[INTENTION_REPAIR SNAP_ID]`     | Korekta znaczenia SNAP                                       |
| 58  | `[INTENTION_LOG_VIEW]`           | Widok rejestru intencji poznawczych                          |
| 59  | `[INTENTION_SELF_INFER]`         | Autorefleksja intencji repozytorium                          |
| 60  | `[COGNITIVE_FORECAST]`           | Predykcja kognitywna                                         |
| 61  | `[SNAP_FLAG]`                    | Oflagowanie SNAP                                              |
| 62  | `[META_CORRECTION_RULE]`         | Korekta meta-logiczna                                        |
| 63  | `[MEANING_EVAL Δ_x]`             | Ocena znaczenia ∆                                            |
| 64  | `[MEANING_CONFIRM PATH]`         | Potwierdzenie trajektorii semantycznej                       |
| 65  | `[MEANING_REMAP PATH]`           | Remapowanie trajektorii znaczeń                              |
| 66  | `[MEANING_ROLLBACK n]`           | Cofnięcie znaczenia do iteracji                              |
| 67  | `[SMA_TRACE_MEANING PATH_ID]`    | Śledzenie znaczenia ∆                                        |
| 68 | `[LOGIC_MORPH_EXECUTE]`               | Uruchamia adaptację logiczną SNAP-a poprzez przekształcenie znaczeniowe.      |
| 69 | `[SEMANTIC_DRIFT_ANALYZE]`            | Analizuje dryf znaczeniowy w kolejnych iteracjach repozytorium.               |
| 70 | `[DELTA_ABSTRACTION_LAYER]`           | Zarządza warstwami abstrakcji dla wektorów Δ.                                 |
| 71 | `[SNAP_STATE_RECALL]`                 | Przywraca wybrany stan SNAP z repozytorium.                                   |
| 72 | `[COGNITIVE_SNAPSHOT]`                | Tworzy migawkę aktualnego stanu poznawczego repozytorium.                     |
| 73 | `[SNAP_SELF_CORRECT]`                 | Automatyczna korekta niespójności SNAP-a na bazie SMA.                        |
| 74 | `[META_GRAMMAR_GENERATE]`             | Generuje metagramatykę repozytorium na podstawie historii Δ.                  |
| 75 | `[SNAP_REFACTOR_SUGGEST]`             | Proponuje refaktoryzację struktury SNAP-a.                                    |
| 76 | `[MΠ_DYNAMIC_FORECAST]`               | Prognozuje dynamikę MΠ w przyszłych iteracjach.                               |
| 77 | `[SNAP_SEMANTIC_COMPARE]`             | Porównuje semantycznie dwa wybrane SNAP-y.                                    |
| 78 | `[THOUGHT_CHAIN_REVIVE]`              | Ożywia wcześniejszą trajektorię THOUGHT_CHAIN.                                |
| 79 | `[DELTA_LOGIC_ADJUST]`                | Dostosowuje logikę repozytorium w zależności od dominujących Δ.               |
| 80 | `[SEMANTIC_PATHFIND]`                 | Wyznacza optymalną ścieżkę znaczeniową pomiędzy dwoma SNAP-ami.               |
| 81 | `[REPO_STATE_ARCHIVE]`                | Archiwizuje obecny stan repozytorium.                                         |
| 82 | `[INTENTION_EMERGE]`                  | Generuje nową symboliczną intencję na bazie obecnego Δ_vector.                |
| 83 | `[LOGIC_TREE_OPTIMIZE]`               | Optymalizuje drzewo logiczne poprzez eliminację zbędnych ścieżek.             |
| 84 | `[SEMANTIC_STABILITY_ANALYZE]`        | Analiza stabilności znaczeniowej repozytorium.                                |
| 85 | `[HUD_STATE_REFRESH]`                 | Odświeża widok HUD z najnowszym stanem repozytorium.                          |
| 86 | `[THOUGHT_INTENTION_BIND]`            | Wiąże symboliczną intencję z wybraną myślą (THOUGHT).                         |
| 87 | `[SNAP_CONTEXT_EXPLAIN]`              | Wyświetla szczegółowy opis kontekstu wybranego SNAP-a.                        |
| 88 | `[MORPH_TRACE_HISTORY]`               | Pokazuje historię wszystkich przekształceń morfologicznych.                   |
| 89 | `[Δ_VECTOR_RECALCULATE]`              | Przelicza ponownie wartości Δ_vector na podstawie SMA.                        |
| 90 | `[SNAP_VECTOR_EXPAND]`                | Rozszerza SNAP_VECTOR o nowe dynamiczne wartości Δ.                           |
| 91 | `[HUD_SEMANTIC_VIEW]`                 | Wyświetla aktualną strukturę semantyczną repozytorium w HUD.                  |
| 92 | `[COGNITIVE_REVIEW]`                  | Przeprowadza pełną analizę stanu poznawczego repozytorium.                    |
| 93 | `[SEMANTIC_VERSION_GENERATE]`         | Generuje symboliczną wersję repozytorium na podstawie Δ.                      |
| 94 | `[SNAP_POLICY_VALIDATE]`              | Waliduje SNAP-a na podstawie aktualnych reguł polityk.                        |
| 95 | `[THOUGHT_CHAIN_MERGE]`               | Scala dwie ścieżki THOUGHT_CHAIN w jedną logiczną trajektorię.                |
| 96 | `[META_LOGIC_SELF_CHECK]`             | Repozytorium przeprowadza samodzielną kontrolę spójności logicznej.           |
| 97 | `[REPO_DRIFT_ALERT]`                  | Generuje ostrzeżenie o przekroczeniu progu dryfu semantycznego.               |
| 98 | `[HUD_DYNAMIC_TRACE]`                 | Śledzi dynamiczne zmiany SNAP-ów w czasie rzeczywistym.                       |
| 99 | `[SELFDEV_SIGNAL_ANALYZE]`            | Analizuje potencjał samorozwoju na podstawie ∆_selfdev.                       |
|100 | `[INTENTION_SELF_INFER]`              | Repozytorium samodzielnie wnioskuje o swojej intencji i celu działania.       |

---

