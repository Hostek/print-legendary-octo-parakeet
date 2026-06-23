import random

WORDS_POOL = [
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
]


def generate_latex():
    selected_words = random.sample(WORDS_POOL, 25)

    key_roles = (["A"] * 9) + (["B"] * 8) + ["N"] * 7 + ["X"]
    random.shuffle(key_roles)

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

    latex_template = f"""\\documentclass[11pt]{{article}}
\\usepackage{{geometry}}
\\usepackage{{tabularx}}
\\usepackage{{colortbl}}
\\usepackage{{xcolor}}

% Konfiguracja dla kompilatora XeLaTeX i czcionki Linux Libertine O
\\usepackage{{fontspec}}
\\setmainfont{{Linux Libertine O}}
\\usepackage[polish]{{babel}}

% Ustawienia szerokości kolumn dla tabeli słów
\\newcolumntype{{Y}}{{>{{\\centering\\arraybackslash}}m{{3.5cm}}}}
% Ustawienia szerokości kolumn dla kluczy
\\newcolumntype{{Z}}{{>{{\\centering\\arraybackslash}}m{{1.2cm}}}}

\\begin{{document}}
\\pagestyle{{empty}}

\\newgeometry{{landscape, margin=1cm}}

\\begin{{center}}
    {{\\Huge \\textbf{{TAJNIACY}} --- PLANSZA GŁÓWNA}}
    \\par\\vspace{{0.5cm}}
    
    \\renewcommand{{\\arraystretch}}{{4.0}}
    \\begin{{tabular}}{{|Y|Y|Y|Y|Y|}}
        \\hline
{grid_rows}    \\end{{tabular}}
\\end{{center}}

\\newpage
\\restoregeometry
\\newgeometry{{portrait, margin=1.5cm}}

\\begin{{center}}
    {{\\Large \\textbf{{KARTA KLUCZA --- KAPITAN 1}}}}
    \\par\\vspace{{0.2cm}}
    {{\\small Legenda: \\textbf{{A}} - Ciemnoszary (Zaczyna) | \\textbf{{B}} - Jasnoszary | \\textbf{{--}} - Neutralny | \\textbf{{X}} - Zabójca}}
    \\par\\vspace{{0.5cm}}

    \\renewcommand{{\\arraystretch}}{{2.2}}
    \\begin{{tabular}}{{|Z|Z|Z|Z|Z|}}
        \\hline
{key_table_code}
    \\end{{tabular}}
    
    \\par\\vspace{{1.5cm}}
    \\noindent\\centerline{{- - - - - - - - - - - - - - - - - - - - - - - -  TNIJ TUTAJ  - - - - - - - - - - - - - - - - - - - - - - - -}}
    \\par\\vspace{{1.5cm}}
    
    {{\\Large \\textbf{{KARTA KLUCZA --- KAPITAN 2 (KOPIA)}}}}
    \\par\\vspace{{0.2cm}}
    {{\\small Legenda: \\textbf{{A}} - Ciemnoszary (Zaczyna) | \\textbf{{B}} - Jasnoszary | \\textbf{{--}} - Neutralny | \\textbf{{X}} - Zabójca}}
    \\par\\vspace{{0.5cm}}

    \\renewcommand{{\\arraystretch}}{{2.2}}
    \\begin{{tabular}}{{|Z|Z|Z|Z|Z|}}
        \\hline
{key_table_code}
    \\end{{tabular}}
\\end{{center}}

\\end{{document}}"""

    return latex_template


if __name__ == "__main__":
    output_filename = "tajniacy_gra.tex"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(generate_latex())
    print(f"Pomyślnie wygenerowano plik: {output_filename}")
    print(
        "Pamiętaj, aby w swoim edytorze zmienić domyślny kompilator z pdfLaTeX na XeLaTeX."
    )
