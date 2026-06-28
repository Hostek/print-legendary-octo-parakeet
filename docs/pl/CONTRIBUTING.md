# Wytyczne dla Współtwórców

Witaj! Ten dokument opisuje standardy i zasady projektowania obowiązujące w naszym repozytorium. Przestrzeganie tych reguł pozwala utrzymać generatory w czystości, dba o ich niezawodność i sprawia, że są łatwo dostępne dla każdego.

## Spis treści

- [Wytyczne dla Współtwórców](#wytyczne-dla-współtwórców)
  - [Spis treści](#spis-treści)
  - [1. Zasada Spójności Generatorów ("Unity")](#1-zasada-spójności-generatorów-unity)
    - [A. Nazwa pliku wyjściowego](#a-nazwa-pliku-wyjściowego)
    - [B. Obowiązkowe argumenty linii komend](#b-obowiązkowe-argumenty-linii-komend)
    - [C. Opcjonalne argumenty standardowe](#c-opcjonalne-argumenty-standardowe)
  - [2. Dodawanie Nowej Gry](#2-dodawanie-nowej-gry)
    - [Kroki do zgłoszenia zmian (Pull Request):](#kroki-do-zgłoszenia-zmian-pull-request)
  - [3. Dodawanie Nowego Języka do Istniejącej Gry](#3-dodawanie-nowego-języka-do-istniejącej-gry)
  - [4. Aktualizacja i Poprawianie Tłumaczeń](#4-aktualizacja-i-poprawianie-tłumaczeń)

---

## 1. Zasada Spójności Generatorów ("Unity")

Każdy skrypt generujący grę musi przestrzegać ścisłej umowy dotyczącej parametrów linii komend (CLI). Ta spójność gwarantuje, że jakiekolwiek automatyczne narzędzia, zewnętrzne skrypty opakowujące lub początkujący użytkownicy mogą wchodzić w interakcję z każdą grą w repozytorium przy użyciu dokładnie tego samego wzorca poleceń.

Wszystkie skrypty generujące muszą spełniać następujące zasady architektoniczne:

### A. Nazwa pliku wyjściowego

- Skrypt **musi** zapisywać wyjściowy plik źródłowy LaTeX pod identyczną nazwą: `game.tex`.
- Wygenerowany plik **musi** być przystosowany do kompilacji przy użyciu silnika `xelatex`.

### B. Obowiązkowe argumenty linii komend

Każdy skrypt musi obsługiwać przynajmniej poniższe argumenty za pomocą biblioteki `argparse`:

- `--lang [KOD]`: Określa słownik językowy.
  - _Domyślnie_: Parametr ten musi przyjmować wartość `"en"`.
  - _Ograniczenie_: Kod języka musi być zgodny z globalnym rejestrem w pliku [docs/LANGUAGES.md](../LANGUAGES.md).
- `--seed [WARTOSC]`: Inicjuje generator liczb pseudolosowych.
  - _Wymóg_: Użycie tego samego seedu musi zawsze owocować całkowicie identycznym, deterministycznym układem planszy.
- `--lang-list`: Skanuje lokalny katalog `./lang`, wyświetla listę dostępnych języków wraz z ich pełnymi nazwami i natychmiast kończy działanie programu.

### C. Opcjonalne argumenty standardowe

- `--words [SCIEZKA]`: Jeśli dotyczy danej gry, pozwala na przekazanie własnej listy słów.
- `--type [INT]`: Opcje układu graficznego. Wartość `1` powinna być zawsze domyślnym/standardowym layoutem.

---

## 2. Dodawanie Nowej Gry

Wprowadzając nową grę print-and-play, zachowaj następującą strukturę katalogów:

```text
games/
└── [nazwa-gry]/
    ├── gen.py               # Skrypt generatora w języku Python
    ├── README.md            # Wybór języka / Przekierowanie
    ├── docs/
    │   ├── en/
    │   │   └── README.md    # Instrukcja generowania i zasady gry (Angielski)
    │   └── pl/
    │       └── README.md    # Instrukcja generowania i zasady gry (Polski)
    └── lang/
        ├── en.json          # Domyślny angielski słownik i konfiguracja
        └── pl.json          # Polski słownik i konfiguracja
```

### Kroki do zgłoszenia zmian (Pull Request):

1. Utwórz folder gry wewnątrz katalogu `games/`.
2. Napisz skrypt `gen.py` według [Zasady Spójności](#1-zasada-spójności-generatorów-unity).
3. Dodaj plik językowy `lang/en.json` oraz inne wymagane słowniki.
4. Przygotuj czytelne opisy przygotowania gry i zasad rozgrywki w lokalnych dokumentach `README.md`.
5. Zaktualizuj główny plik `README.md` w korzeniu repozytorium, dodając odnośnik do nowej gry.

---

## 3. Dodawanie Nowego Języka do Istniejącej Gry

Aby dodać obsługę nowego języka do danej gry (na przykład niemieckiego `de`):

1. Upewnij się, że kod języka jest zarejestrowany w pliku [docs/LANGUAGES.md](../LANGUAGES.md). Jeśli nie, najpierw go zarejestruj.
2. Wejdź do katalogu `games/[nazwa-gry]/lang/`.
3. Utwórz nowy plik JSON o nazwie `[kod].json` (np. `de.json`).
4. Skopiuj strukturę kluczy z pliku `en.json` i przetłumacz wartości (takie jak elementy interfejsu, etykiety i listy słów).
5. Upewnij się, że wartość `babel_lang` odpowiada poprawnej nazwie pakietu obsługi języka w systemie LaTeX (pakiet `babel`).

---

## 4. Aktualizacja i Poprawianie Tłumaczeń

Jeśli zauważysz literówkę lub chcesz rozbudować słownictwo danej gry:

1. Znajdź odpowiedni plik językowy w `games/[nazwa-gry]/lang/[kod].json`.
2. Zmodyfikuj wartości w pliku JSON. Nie zmieniaj samych kluczy, ponieważ spowoduje to błędy odczytu w skrypcie `gen.py`.
3. Przetestuj swoje zmiany lokalnie, generując i kompilując plik PDF:
   ```bash
   python gen.py --lang [kod]
   xelatex game.tex
   ```

---

[← Powrót do głównej strony współtwórców](../../CONTRIBUTING.md) | [← Powrót do głównego pliku README](../../../README.md)
