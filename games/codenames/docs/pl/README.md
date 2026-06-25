# Tajniacy (Codenames): Generowanie PDF & Instrukcja gry

Witaj w dokumentacji print-and-play gry **Tajniacy** (Codenames). Ten przewodnik wyjaśni, jak skonfigurować i wygenerować elementy gry oraz jak grać po ich wydrukowaniu.

---

## 1. Jak wygenerować plik PDF z grą

Proces składa się z uruchomienia skryptu Python, który tworzy plik LaTeX, a następnie skompilowania go do formatu PDF.

### Wymagania
1.  **Python 3** (W razie potrzeby zobacz [Instrukcję Pythona](../../../../docs/pl/python.md)).
2.  **XeLaTeX** (Zobacz [Instrukcję lokalną XeLaTeX](../../../../docs/pl/latex.md) lub [Instrukcję Overleaf](../../../../docs/pl/overleaf.md)).

### Krok 1: Uruchomienie skryptu Python
Otwórz konsolę (terminal), przejdź do katalogu `games/codenames/` i wpisz:

```bash
python gen.py
```

Spowoduje to wygenerowanie pliku `game.tex`.

### Parametry konfiguracyjne (Argumenty linii komend)
Możesz dostosować proces generowania za pomocą następujących argumentów:

*   `--lang KOD`: Wybiera plik językowy z katalogu `./lang/` (np. `pl` lub `en`).
    ```bash
    python gen.py --lang pl
    ```
*   `--words SCIEZKA`: Używa własnego pliku słów `.txt` (jedno słowo na linię) lub tablicy `.json`:
    ```bash
    python gen.py --words moje_slowa.txt
    ```
*   `--seed WARTOSC`: Pozwala określić stałą wartość generatora losowości. Ten sam seed wygeneruje identyczny układ planszy i kluczy:
    ```bash
    python gen.py --seed "moj_seed_1"
    ```
*   `--type [1|2]`:
    *   `1` (**Domyślny**): Generuje pełnowymiarowy, poziomy arkusz Kapitana, na którym słowa są bezpośrednio pokolorowane. Kapitanowie nie muszą niczego wycinać; posługują się kopią planszy głównej, gdzie każde słowo ma tło w odpowiednim kolorze (Ciemnoszary dla drużyny A, Jasnoszary dla drużyny B, Biały dla Neutralnych, Czarny dla Zabójcy).
    *   `2`: Generuje arkusz pionowy z dwoma mniejszymi siatkami 5x5 oznaczonymi literami **A**, **B**, **--** oraz **X**. Należy przeciąć arkusz wzdłuż linii przerywanej, aby dać każdemu z Kapitanów mniejszą kartę klucza.

### Krok 2: Kompilacja do PDF
Skompiluj plik `game.tex` za pomocą programu XeLaTeX:

```bash
xelatex game.tex
```

W rezultacie powstanie plik `game.pdf`. Wydrukuj stronę 1 (plansza graczy) oraz stronę 2 (karta Kapitanów).

---

## 2. Zasady gry (Instrukcja)

Tajniacy to gra słowna dla dwóch zespołów.

### Cel gry
Drużyna, która jako pierwsza poprawnie wskaże wszystkie swoje słowa (agentów) na planszy, wygrywa grę.

### Role i przygotowanie
1.  **Podział na drużyny**: Gracze dzielą się na dwa zespoły: **Drużynę A (Ciemnoszara)** oraz **Drużynę B (Jasnoszara)**.
2.  **Wybór Kapitanów**: Każda drużyna wybiera jednego Szefa Wywiadu (Kapitana). Kapitanowie siadają po przeciwnej stronie stołu niż ich agenci (**Operorzy**).
3.  **Plansza główna**: Wydrukowaną Planszę Główną (Strona 1) kładziemy na środku stołu.
    *   *Uwaga: Plansza zawiera zduplikowane słowa obrócone o 180 stopni, aby gracze po obu stronach stołu mogli je łatwo odczytać.*
4.  **Ściągawka Kapitanów**: Przekaż Kapitanom Arkusz Klucza (Strona 2).
    *   **W przypadku typu 1 (Domyślny)**: Kapitanowie patrzą na identyczną planszę jak gracze, ale z kolorowym podkładem wskazującym tożsamość każdego słowa.
    *   **W przypadku typu 2**: Przetnij stronę wzdłuż przerywanej linii. Każdy Kapitan otrzymuje miniaturową kartę klucza.

### Tożsamości pól na planszy
25 słów na planszy dzieli się na cztery grupy:
*   **Drużyna A (Ciemnoszary / 9 słów)**: Ta drużyna zaczyna grę i ma do odnalezienia 9 słów.
*   **Drużyna B (Jasnoszary / 8 słów)**: Ta drużyna wykonuje ruch jako druga i ma do odnalezienia 8 słów.
*   **Neutralni (Biały / 7 słów)**: Przypadkowi przechodnie. Wskazanie takiego słowa kończy turę drużyny.
*   **Zabójca (Czarny / 1 słowo)**: Śmiertelna pułapka. Wskazanie tego słowa oznacza natychmiastową przegraną.

---

### Przebieg rozgrywki
Gra toczy się w turach, rozpoczynając od **Drużyny A**.

#### Krok A: Podpowiedź Kapitana
W swojej turze Kapitan podaje swoim Operorom wskazówkę składającą się dokładnie z **jednego słowa** i **jednej liczby** (np. *"Ocean: 3"*).
*   **Słowo** powinno kojarzyć się ze słowami własnej drużyny na planszy.
*   **Liczba** informuje, ile słów na planszy wiąże się z podanym skojarzeniem.
*   **Zasady podpowiadania**: Kapitanowi nie wolno wypowiadać żadnej części słów widocznych na planszy, tłumaczyć słów na inne języki, ani wykonywać żadnych gestów.

#### Krok B: Odgadywanie Operorów
Operorzy wspólnie dyskutują i próbują wskazać słowa.
1.  Aby zgadnąć słowo, jeden z Operorów musi fizycznie dotknąć słowa na wydrukowanej planszy.
2.  **Rozstrzygnięcie strzału**:
    *   **Trafienie słowa własnej drużyny**: Sukces. Mogą zgadywać dalej (maksymalnie tyle razy, ile wynosiła podana liczba + 1 dodatkowy bonusowy strzał na wypadek wcześniejszych niedokończonych podpowiedzi).
    *   **Trafienie słowa przeciwnika**: Tura kończy się natychmiast, a punkt wędruje na konto drugiej drużyny.
    *   **Trafienie pola Neutralnego**: Tura kończy się natychmiast.
    *   **Trafienie Zabójcy**: Gra kończy się natychmiastową przegraną drużyny zgadującej.
3.  Operorzy mogą zdecydować o zakończeniu swojej tury w dowolnym momencie.

### Wygrana
Gra kończy się natychmiast, gdy:
*   Któraś z drużyn odnajdzie wszystkie swoje słowa. **Ta drużyna wygrywa.**
*   Dowolna drużyna wskaże słowo Zabójcy. **Ta drużyna przegrywa natychmiast.**

---
[← Powrót do strony głównej Tajniaków](../../README.md) | [← Powrót do głównego pliku README](../../../README.md)