# XeLaTeX: Instalacja i kompilacja lokalna

XeLaTeX to nowoczesny silnik systemu LaTeX, który pozwala na łatwe korzystanie z czcionek systemowych (np. Arial, Times New Roman) oraz pełne wsparcie dla kodowania UTF-8.

---

## 1. Instalacja XeLaTeX

Aby móc korzystać z XeLaTeX na komputerze, musisz zainstalować dystrybucję systemu TeX.

### Windows

Polecanym i prostym w instalacji środowiskiem jest **MiKTeX**.

1. Wejdź na stronę [miktex.org/download](https://miktex.org/download) i pobierz instalator dla systemu Windows.
2. Uruchom instalator i postępuj zgodnie z instrukcjami. Przy instalacji możesz wybrać opcję automatycznego doinstalowywania brakujących pakietów (_"Install missing packages on-the-fly"_ -> ustaw na _Yes_).

### macOS

Dla użytkowników systemu macOS standardem jest pakiet **MacTeX**.

1. Wejdź na stronę [tug.org/mactex](https://tug.org/mactex/) i pobierz pełny instalator MacTeX (plik jest dość duży).
2. Uruchom instalator `.pkg` i przejdź proces instalacji.

### Linux (Ubuntu/Debian)

Zainstaluj pełny pakiet TeX Live za pomocą menedżera pakietów:

```bash
sudo apt update
sudo apt install texlive-xetex texlive-lang-polish
```

---

## 2. Jak skompilować dokument XeLaTeX

### Krok 1: Przygotowanie dokumentu

1. Utwórz plik tekstowy o nazwie `dokument.tex`.
2. Wklej do niego poniższy, przykładowy kod:

   ```latex
   \documentclass{article}
   \usepackage{fontspec} % Wymagane dla XeLaTeX do obsługi czcionek
   \setmainfont{Arial}    % Możesz zmienić na inną czcionkę systemową
   \usepackage[polish]{babel}

   \begin{document}
   Hello World! To jest dokument skompilowany przy użyciu silnika XeLaTeX.
   Polskie znaki: zażółć gęślą jaźń.
   \end{document}
   ```

### Krok 2: Kompilacja za pomocą linii komend (Windows, macOS, Linux)

1. Otwórz konsolę (Wiersz polecenia na Windows / Terminal na macOS i Linux).
2. Przejdź do katalogu, w którym znajduje się plik `dokument.tex`, na przykład:
   ```bash
   cd Desktop
   ```
3. Uruchom kompilator XeLaTeX wpisując:
   ```bash
   xelatex dokument.tex
   ```
4. Po zakończeniu kompilacji w tym samym folderze powstanie gotowy plik PDF o nazwie `dokument.pdf`.

---

[← Powrót do Poradnika dla początkujących](README.md)
