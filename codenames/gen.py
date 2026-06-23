import argparse
import random
import json
import os
import sys

LANG_DIR = "./lang"


def bootstrap_languages():
    """Inicjalizuje strukturę folderu ./lang/."""
    if not os.path.exists(LANG_DIR):
        os.makedirs(LANG_DIR)


def list_languages():
    """Skanuje katalog ./lang/ i wypisuje wszystkie dostępne języki."""
    bootstrap_languages()
    files = [f for f in os.listdir(LANG_DIR) if f.endswith(".json")]

    if not files:
        print("No language configurations found in ./lang/")
        return

    print("Available languages in ./lang/:")
    for filename in sorted(files):
        lang_code = os.path.splitext(filename)[0]
        filepath = os.path.join(LANG_DIR, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                full_name = data.get("full_lang_name", "Unknown Language")
                print(f"  - {lang_code:6}: {full_name}")
        except Exception:
            print(f"  - {lang_code:6}: [Error reading file]")


def load_lang_config(lang_code):
    """Ładuje plik JSON dla konkretnego kodu językowego."""
    filepath = os.path.join(LANG_DIR, f"{lang_code}.json")
    if not os.path.exists(filepath):
        print(f"Error: Language file '{filepath}' does not exist.")
        print("Use --lang-list to view available languages.")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def load_custom_words_file(filepath):
    """Ładuje słowa z zewnętrznego pliku TXT (jedno słowo na linię) lub JSON."""
    if not os.path.exists(filepath):
        print(f"Error: Custom word file '{filepath}' not found.")
        sys.exit(1)

    if filepath.endswith(".json"):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print("Error: JSON word list must be a flat array of strings.")
                sys.exit(1)
    else:
        with open(filepath, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]


def generate_latex(words, translations, babel_lang):
    if len(words) < 25:
        print(
            f"Error: Word list only contains {len(words)} items. At least 25 are required."
        )
        sys.exit(1)

    selected_words = random.sample(words, 25)

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

\\usepackage[{babel_lang}]{{babel}}

\\newcolumntype{{Y}}{{>{{\\centering\\arraybackslash}}m{{3.5cm}}}}
\\newcolumntype{{Z}}{{>{{\\centering\\arraybackslash}}m{{2.0cm}}}}

\\begin{{document}}
\\pagestyle{{empty}}

\\newgeometry{{landscape, a4paper, margin=0.8cm}}

\\begin{{center}}
    {{\\Large \\textbf{{{translations['title']}}}}}
    \\par\\vspace{{0.3cm}}
    \\renewcommand{{\\arraystretch}}{{4.2}}
    \\begin{{tabular}}{{|Y|Y|Y|Y|Y|}}
        \\hline
{grid_rows}    \\end{{tabular}}
    
    \\vfill
    
    \\rotatebox{{180}}{{%
        \\begin{{minipage}}{{\\linewidth}}
            \\centering
            \\renewcommand{{\\arraystretch}}{{4.2}}
            \\begin{{tabular}}{{|Y|Y|Y|Y|Y|}}
                \\hline
{grid_rows}            \\end{{tabular}}
            \\par\\vspace{{0.3cm}}
            {{\\Large \\textbf{{{translations['title']}}}}}
        \\end{{minipage}}%
    }}
\\end{{center}}

\\newpage
\\restoregeometry
\\newgeometry{{portrait, a4paper, margin=1.5cm}}

\\begin{{center}}
    {{\\Large \\textbf{{{translations['key_title_1']}}}}}
    \\par\\vspace{{0.2cm}}
    {{\\small {translations['legend']}}}
    \\par\\vspace{{0.5cm}}

    \\renewcommand{{\\arraystretch}}{{2.8}}
    \\begin{{tabular}}{{|Z|Z|Z|Z|Z|}}
        \\hline
{key_table_code}
    \\end{{tabular}}
    
    \\par\\vspace{{1.2cm}}
    \\noindent\\centerline{{- - - - - - - - - - - - - - - - - - - - - - - -  {translations['cut_here']}  - - - - - - - - - - - - - - - - - - - - - - - -}}
    \\par\\vspace{{1.2cm}}
    
    {{\\Large \\textbf{{{translations['key_title_2']}}}}}
    \\par\\vspace{{0.2cm}}
    {{\\small {translations['legend']}}}
    \\par\\vspace{{0.5cm}}

    \\renewcommand{{\\arraystretch}}{{2.8}}
    \\begin{{tabular}}{{|Z|Z|Z|Z|Z|}}
        \\hline
{key_table_code}
    \\end{{tabular}}
\\end{{center}}

\\end{{document}}"""

    return latex_document


def main():
    bootstrap_languages()

    parser = argparse.ArgumentParser(
        description="LaTeX board and keycard generator for Codenames.",
        epilog="Remember to compile the output game.tex file using XeLaTeX.",
    )

    parser.add_argument(
        "--lang",
        type=str,
        default="en",
        help="Language code to use (looks for ./lang/[lang].json). Default is 'en'.",
    )

    parser.add_argument(
        "--words",
        type=str,
        default=None,
        help="Optional path to a custom word file (.txt with one word per line, or a flat JSON array).",
    )

    parser.add_argument(
        "--lang-list",
        action="store_true",
        help="List all available languages inside the './lang' directory and exit.",
    )

    args = parser.parse_args()

    if args.lang_list:
        list_languages()
        sys.exit(0)

    lang_config = load_lang_config(args.lang)
    translations = lang_config.get("translations", {})
    babel_lang = lang_config.get("babel_lang", "english")

    if args.words:
        words_pool = load_custom_words_file(args.words)
        print(f"Loaded {len(words_pool)} custom words from: {args.words}")
    else:
        words_pool = lang_config.get("words", [])
        print(
            f"Loaded {len(words_pool)} default words for language: '{args.lang}' ({lang_config.get('full_lang_name')})"
        )

    latex_content = generate_latex(words_pool, translations, babel_lang)
    output_filename = "game.tex"

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(latex_content)

    print(f"LaTeX template successfully saved as: {output_filename}")


if __name__ == "__main__":
    main()
