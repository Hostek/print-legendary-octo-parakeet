# Python: Instalacja i uruchamianie

Python to popularny i przyjazny dla początkujących język programowania. Poniżej znajdziesz instrukcję, jak go zainstalować oraz jak uruchomić swój pierwszy skrypt.

---

## 1. Instalacja Pythona

### Windows
1. Wejdź na oficjalną stronę: [python.org/downloads](https://www.python.org/downloads/).
2. Kliknij żółty przycisk **Download Python [wersja]**.
3. Uruchom pobrany plik instalacyjny `.exe`.
4. **Ważne:** Na samym dole okna instalatora zaznacz pole **"Add python.exe to PATH"** (Dodaj Pythona do zmiennej PATH). Jeśli tego nie zrobisz, system nie będzie wiedział, jak uruchomić Pythona z konsoli.
5. Kliknij **Install Now** i poczekaj na zakończenie procesu.

### macOS
1. Najprostszym sposobem dla początkujących jest pobranie instalatora ze strony [python.org/downloads](https://www.python.org/downloads/).
2. Pobierz instalator dla macOS (plik `.pkg`) i uruchom go, postępując zgodnie z instrukcjami na ekranie.
3. *Alternatywa dla użytkowników Homebrew:* Jeśli korzystasz z terminala i masz zainstalowane narzędzie Homebrew, wpisz:
   ```bash
   brew install python
   ```

### Linux (Ubuntu/Debian)
W większości dystrybucji Linux Python jest już zainstalowany. Aby upewnić się, że masz najnowszą wersję, otwórz terminal i wpisz:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## 2. Jak uruchomić skrypt Python

Aby sprawdzić, czy Python działa, stwórzmy prosty program "Hello World".

### Krok 1: Przygotowanie pliku
1. Otwórz zwykły edytor tekstu (np. Notatnik w systemie Windows, TextEdit na macOS lub Gedit na Linuxie).
2. Wpisz następujący kod:
   ```python
   print("Witaj w świecie Python!")
   ```
3. Zapisz plik pod nazwą `skrypt.py` (upewnij się, że rozszerzenie to `.py`, a nie `.txt`). Zapisz go np. na Pulpicie.

### Krok 2: Uruchomienie skryptu

#### Windows (Konsola CMD lub PowerShell)
1. Otwórz menu Start, wpisz `cmd` i uruchom **Wiersz polecenia**.
2. Przejdź do folderu, w którym zapisałeś plik (np. na Pulpit). Wpisz:
   ```cmd
   cd Desktop
   ```
3. Uruchom skrypt wpisując:
   ```cmd
   python skrypt.py
   ```
4. Na ekranie powinien pojawić się napis: `Witaj w świecie Python!`.

#### macOS i Linux (Terminal)
1. Otwórz **Terminal**.
2. Przejdź do folderu z plikiem (np. Desktop):
   ```bash
   cd Desktop
   ```
3. Uruchom skrypt wpisując (w systemach Unix często używa się komendy `python3` zamiast `python`):
   ```bash
   python3 skrypt.py
   ```
