import argparse
import random
import json
import os

DEFAULT_WORD_BANKS = {
    "pl": [
        "Czekolada",
        "Kaktus",
        "Zamek",
        "Pirat",
        "Klucz",
        "Mysz",
        "Gwiazda",
        "Telefon",
        "Oko",
        "Lustro",
        "Krowa",
        "Rower",
        "Szkoła",
        "Banan",
        "Chmura",
        "Statek",
        "Pies",
        "Słońce",
        "Książka",
        "Ryba",
        "Dinozaur",
        "Kawa",
        "Poduszka",
        "Balon",
        "Drzewo",
        "Zegarek",
        "Samolot",
        "Kapelusz",
        "Pudełko",
        "Karta",
        "Ogórek",
        "Szarlotka",
        "Kot",
        "Wulkan",
        "Puszcza",
        "Księżyc",
        "Złoto",
        "Woda",
        "Ogień",
        "Ziemniak",
        "Bilet",
        "Czapka",
        "Dach",
        "Ekran",
        "Fotel",
        "Gitara",
        "Igła",
        "Jabłko",
        "Komin",
        "Lampa",
        "Most",
        "Namiot",
        "Ołówek",
        "Płyta",
        "Radio",
        "Serce",
        "Torba",
        "Ucho",
        "Wózek",
        "Ząb",
    ],
    "en": [
        "Chocolate",
        "Cactus",
        "Castle",
        "Pirate",
        "Key",
        "Mouse",
        "Star",
        "Phone",
        "Eye",
        "Mirror",
        "Cow",
        "Bicycle",
        "School",
        "Banana",
        "Cloud",
        "Ship",
        "Dog",
        "Sun",
        "Book",
        "Fish",
        "Dinosaur",
        "Coffee",
        "Pillow",
        "Balloon",
        "Tree",
        "Watch",
        "Plane",
        "Hat",
        "Box",
        "Card",
        "Cucumber",
        "Apple Pie",
        "Cat",
        "Volcano",
        "Forest",
        "Moon",
        "Gold",
        "Water",
        "Fire",
        "Potato",
        "Ticket",
        "Cap",
        "Roof",
        "Screen",
        "Armchair",
        "Guitar",
        "Needle",
        "Apple",
        "Chimney",
        "Lamp",
        "Bridge",
        "Tent",
        "Pencil",
        "Disc",
        "Radio",
        "Heart",
        "Bag",
        "Ear",
        "Cart",
        "Tooth",
    ],
}

TRANSLATIONS = {
    "pl": {
        "title": "TAJNIACY --- PLANSZA GŁÓWNA",
        "key_title_1": "KARTA KLUCZA --- KAPITAN 1",
        "key_title_2": "KARTA KLUCZA --- KAPITAN 2 (KOPIA)",
        "legend": "Legenda: \\textbf{A} - Ciemnoszary (Zaczyna) | \\textbf{B} - Jasnoszary | \\textbf{--} - Neutralny | \\textbf{X} - Zabójca",
        "cut_here": "TNIJ TUTAJ",
    },
    "en": {
        "title": "CODENAMES --- MAIN BOARD",
        "key_title_1": "KEY CARD --- SPYMASTER 1",
        "key_title_2": "KEY CARD --- SPYMASTER 2 (COPY)",
        "legend": "Legend: \\textbf{A} - Dark Gray (Starts) | \\textbf{B} - Light Gray | \\textbf{--} - Neutral | \\textbf{X} - Assassin",
        "cut_here": "CUT HERE",
    },
}


def load_custom_words(filepath, lang):
    """Ładuje słowa z zewnętrznego pliku TXT lub JSON."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Nie znaleziono pliku: {filepath}")

    if filepath.endswith(".json"):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict) and lang in data:
                return data[lang]
            elif isinstance(data, list):
                return data
            else:
                raise ValueError("Niepoprawny format pliku JSON ze słowami.")
    else:
        with open(filepath, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        return words


def generate_latex(words, lang):
    if len(words) < 25:
        raise ValueError(
            f"Wybrana baza słów ma tylko {len(words)} wyrazów. Wymagane jest minimum 25."
        )
    selected_words = random.sample(words, 25)

    key_roles = (["A"] * 9) + (["B"] * 8) + ["N"] * 7 + ["X"]
    random.shuffle(key_roles)

    trans = TRANSLATIONS.get(lang, TRANSLATIONS["en"])

    grid_rows = ""
    for i in range(5):
        row_words = selected_words[i * 5 : (i + 1) * 5]
        grid_rows += (
            "        "
            + " & ".join([rf"\textbf{{\Large {w}}}" for w in row_words])
            + r" \\ \hline"
            + "\n"
        )

    def format_cell(role):
        if role == "A":
            return r"\cellcolor{black!60}\textcolor{white}{\textbf{A}}"
        elif role == "B":
            return r"\cellcolor{black!20}\textcolor{black}{\textbf{B}}"
        elif role == "N":
            return r"\cellcolor{white}\textcolor{black}{\textbf{--}}"
        elif role == "X":
            return r"\cellcolor{black}\textcolor{white}{\textbf{X}}"

    key_rows = []
    for i in range(5):
        row_roles = key_roles[i * 5 : (i + 1) * 5]
        key_rows.append(
            "        " + " & ".join([format_cell(r) for r in row_roles]) + r" \\ \hline"
        )
    key_table_code = "\n".join(key_rows)

    latex_document = f"""\\documentclass[11pt, a4paper]{{article}}
\\usepackage[a4paper]{{geometry}}
\\usepackage{{tabularx}}
\\usepackage{{colortbl}}
\\usepackage{{xcolor}}
\\usepackage{{graphicx}}

\\usepackage{{fontspec}}
\\IfFontExistsTF{{Linux Libertine O}}{{
  \\setmainfont{{Linux Libertine O}}
}}{{
  \\IfFontExistsTF{{Liberation Serif}}{{
    \\setmainfont{{Liberation Serif}}
  }}{{
    \\IfFontExistsTF{{Times New Roman}}{{
      \\setmainfont{{Times New Roman}}
    }}{{
    }}
  }}
}}

\\usepackage[{'polish' if lang == 'pl' else 'english'}]{{babel}}

\\newcolumntype{{Y}}{{>{{\\centering\\arraybackslash}}m{{3.5cm}}}}
\\newcolumntype{{Z}}{{>{{\\centering\\arraybackslash}}m{{2.0cm}}}}

\\begin{{document}}
\\pagestyle{{empty}}

\\newgeometry{{landscape, a4paper, margin=1.0cm}}

\\begin{{center}}
    {{\\Large \\textbf{{{trans['title']}}}}}
    \\par\\vspace{{0.3cm}}
    \\renewcommand{{\\arraystretch}}{{1.8}}
    \\begin{{tabular}}{{|Y|Y|Y|Y|Y|}}
        \\hline
{grid_rows}    \\end{{tabular}}
    
    \\vfill
    
    \\rotatebox{{180}}{{%
        \\begin{{minipage}}{{\\linewidth}}
            \\centering
            \\renewcommand{{\\arraystretch}}{{1.8}}
            \\begin{{tabular}}{{|Y|Y|Y|Y|Y|}}
                \\hline
{grid_rows}            \\end{{tabular}}
            \\par\\vspace{{0.3cm}}
            {{\\Large \\textbf{{{trans['title']}}}}}
        \\end{{minipage}}%
    }}
\\end{{center}}

\\newpage
\\restoregeometry
\\newgeometry{{portrait, a4paper, margin=1.5cm}}

\\begin{{center}}
    {{\\Large \\textbf{{{trans['key_title_1']}}}}}
    \\par\\vspace{{0.2cm}}
    {{\\small {trans['legend']}}}
    \\par\\vspace{{0.5cm}}

    \\renewcommand{{\\arraystretch}}{{2.8}} % Większe wiersze klucza
    \\begin{{tabular}}{{|Z|Z|Z|Z|Z|}}
        \\hline
{key_table_code}
    \\end{{tabular}}
    
    \\par\\vspace{{1.2cm}}
    \\noindent\\centerline{{- - - - - - - - - - - - - - - - - - - - - - - -  {trans['cut_here']}  - - - - - - - - - - - - - - - - - - - - - - - -}}
    \\par\\vspace{{1.2cm}}
    
    {{\\Large \\textbf{{{trans['key_title_2']}}}}}
    \\par\\vspace{{0.2cm}}
    {{\\small {trans['legend']}}}
    \\par\\vspace{{0.5cm}}

    \\renewcommand{{\\arraystretch}}{{2.8}} % Większe wiersze klucza
    \\begin{{tabular}}{{|Z|Z|Z|Z|Z|}}
        \\hline
{key_table_code}
    \\end{{tabular}}
\\end{{center}}

\\end{{document}}"""

    return latex_document


def main():
    parser = argparse.ArgumentParser(
        description="Generator gry planszowej Tajniacy (Codenames) do formatu LaTeX."
    )
    parser.add_argument(
        "--lang",
        choices=["pl", "en"],
        default="en",
        help="Wybór języka gry (pl/en). Domyślnie: en.",
    )
    parser.add_argument(
        "--words",
        type=str,
        default=None,
        help="Opcjonalna ścieżka do własnego pliku ze słowami (.txt lub .json).",
    )

    args = parser.parse_args()

    if args.words:
        try:
            word_bank = load_custom_words(args.words, args.lang)
            print(
                f"Załadowano własną bazę słów z pliku: {args.words} (Liczba słów: {len(word_bank)})"
            )
        except Exception as e:
            print(f"Błąd podczas ładowania pliku ze słowami: {e}")
            return
    else:
        word_bank = DEFAULT_WORD_BANKS[args.lang]
        print(
            f"Używam domyślnej bazy słów dla języka: '{args.lang}' (Liczba słów: {len(word_bank)})"
        )

    try:
        latex_content = generate_latex(word_bank, args.lang)
        output_file = "game.tex"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(latex_content)
        print(f"Plik wyjściowy został pomyślnie zapisany jako: {output_file}")
    except ValueError as e:
        print(f"Błąd generowania: {e}")


if __name__ == "__main__":
    main()
