import argparse
import random
import json
import os
import sys

LANG_DIR = "./lang"
FALLBACK_DOMAIN = "github.com/Hostek/print-legendary-octo-parakeet"


def get_project_domain():
    """Reads the domain from the root config file or returns fallback."""
    possible_paths = ["../../PROJECT_CONFIG.json", "./PROJECT_CONFIG.json"]
    for path in possible_paths:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f).get("domain_url", FALLBACK_DOMAIN)
            except Exception:
                pass
    return FALLBACK_DOMAIN


def bootstrap_languages():
    """Initializes folder structure for ./lang/."""
    if not os.path.exists(LANG_DIR):
        os.makedirs(LANG_DIR)


def list_languages():
    """Scans ./lang/ folder and outputs all available languages."""
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
    """Loads JSON file and injects the project domain into the watermark."""
    filepath = os.path.join(LANG_DIR, f"{lang_code}.json")
    if not os.path.exists(filepath):
        print(f"Error: Language file '{filepath}' does not exist.")
        print("Use --lang-list to view available languages.")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    domain = get_project_domain()
    if "translations" in data and "watermark" in data["translations"]:
        data["translations"]["watermark"] = data["translations"]["watermark"].replace(
            "[DOMAIN_URL]", domain
        )

    return data


def load_custom_words_file(filepath):
    """Loads words from custom plain text or JSON file."""
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


def generate_latex(words, translations, babel_lang, layout_type):
    if len(words) < 25:
        print(
            f"Error: Word list only contains {len(words)} items. At least 25 are required."
        )
        sys.exit(1)

    selected_words = random.sample(words, 25)
    key_roles = (["A"] * 9) + (["B"] * 8) + ["N"] * 7 + ["X"]
    random.shuffle(key_roles)

    watermark_tex = rf"\vfill \centering \color{{gray}}{{\tiny {translations.get('watermark', '')}}}"

    grid_rows = ""
    for i in range(5):
        row_words = selected_words[i * 5 : (i + 1) * 5]
        grid_rows += (
            "        "
            + " & ".join([rf"\textbf{{\Large {w}}}" for w in row_words])
            + r" \\ \hline"
            + "\n"
        )

    if layout_type == 1:
        spymaster_rows = ""
        for i in range(5):
            row_words = selected_words[i * 5 : (i + 1) * 5]
            row_roles = key_roles[i * 5 : (i + 1) * 5]
            cells = []
            for w, r in zip(row_words, row_roles):
                color = "white"
                text_color = "black"
                label = r
                if r == "A":
                    color = "black!60"
                    text_color = "white"
                elif r == "B":
                    color = "black!20"
                    text_color = "black"
                elif r == "N":
                    color = "white"
                    text_color = "black"
                    label = "--"
                elif r == "X":
                    color = "black"
                    text_color = "white"

                cells.append(
                    rf"\cellcolor{{{color}}}\color{{{text_color}}}{{\small {label} \par \textbf{{\Large {w}}}}}"
                )
            spymaster_rows += "        " + " & ".join(cells) + r" \\ \hline" + "\n"

        page_2_code = f"""\\newgeometry{{landscape, a4paper, margin=0.8cm}}
\\begin{{center}}
    {{\\Large \\textbf{{{translations['key_title_1']}}}}} \\par\\vspace{{0.2cm}}
    {{\\small {translations['legend']}}} \\par\\vspace{{0.3cm}}
    \\renewcommand{{\\arraystretch}}{{3.8}}
    \\begin{{tabular}}{{|Y|Y|Y|Y|Y|}}
        \\hline
{spymaster_rows}    \\end{{tabular}}
    \\vfill
    \\rotatebox{{180}}{{%
        \\begin{{minipage}}{{\\linewidth}}
            \\centering
            \\renewcommand{{\\arraystretch}}{{3.8}}
            \\begin{{tabular}}{{|Y|Y|Y|Y|Y|}}
                \\hline
{spymaster_rows}            \\end{{tabular}}
            \\par\\vspace{{0.3cm}}
            {{\\Large \\textbf{{{translations['key_title_1']}}}}}
        \\end{{minipage}}%
    }}
    {watermark_tex}
\\end{{center}}"""
    else:

        def format_cell(role):
            if role == "A":
                return r"\cellcolor{black!60}\color{white}{\textbf{A}}"
            elif role == "B":
                return r"\cellcolor{black!20}\color{black}{\textbf{B}}"
            elif role == "N":
                return r"\cellcolor{white}\color{black}{\textbf{--}}"
            elif role == "X":
                return r"\cellcolor{black}\color{white}{\textbf{X}}"

        key_rows = []
        for i in range(5):
            row_roles = key_roles[i * 5 : (i + 1) * 5]
            key_rows.append(
                "        "
                + " & ".join([format_cell(r) for r in row_roles])
                + r" \\ \hline"
            )
        key_table_code = "\n".join(key_rows)

        page_2_code = f"""\\newgeometry{{portrait, a4paper, margin=1.5cm}}
\\begin{{center}}
    {{\\Large \\textbf{{{translations['key_title_1']}}}}} \\par\\vspace{{0.2cm}}
    {{\\small {translations['legend']}}} \\par\\vspace{{0.5cm}}
    \\renewcommand{{\\arraystretch}}{{2.8}}
    \\begin{{tabular}}{{|Z|Z|Z|Z|Z|}}
        \\hline
{key_table_code}
    \\end{{tabular}}
    \\par\\vspace{{1.2cm}}
    \\noindent\\centerline{{- - - - - - - -  {translations['cut_here']}  - - - - - - - -}}
    \\par\\vspace{{1.2cm}}
    {{\\Large \\textbf{{{translations['key_title_2']}}}}} \\par\\vspace{{0.5cm}}
    \\begin{{tabular}}{{|Z|Z|Z|Z|Z|}}
        \\hline
{key_table_code}
    \\end{{tabular}}
    {watermark_tex}
\\end{{center}}"""

    return f"""\\documentclass[11pt, a4paper]{{article}}
\\usepackage[a4paper]{{geometry}}
\\usepackage{{tabularx, colortbl, xcolor, graphicx, fontspec}}
\\usepackage[{babel_lang}]{{babel}}

\\IfFontExistsTF{{Linux Libertine O}}{{\\setmainfont{{Linux Libertine O}}}}{{
  \\IfFontExistsTF{{Liberation Serif}}{{\\setmainfont{{Liberation Serif}}}}{{\\IfFontExistsTF{{Times New Roman}}{{\\setmainfont{{Times New Roman}}}}{{}}}}
}}

\\newcolumntype{{Y}}{{>{{\\centering\\arraybackslash}}m{{3.5cm}}}}
\\newcolumntype{{Z}}{{>{{\\centering\\arraybackslash}}m{{2.0cm}}}}

\\begin{{document}}
\\pagestyle{{empty}}
\\newgeometry{{landscape, a4paper, margin=0.8cm}}
\\begin{{center}}
    {{\\Large \\textbf{{{translations['title']}}}}} \\par\\vspace{{0.3cm}}
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
    {watermark_tex}
\\end{{center}}
\\newpage
\\restoregeometry
{page_2_code}
\\end{{document}}"""


def main():
    bootstrap_languages()
    parser = argparse.ArgumentParser(description="Codenames LaTeX Generator")
    parser.add_argument("--lang", type=str, default="en", help="Language code.")
    parser.add_argument("--words", type=str, default=None, help="Path to custom words.")
    parser.add_argument(
        "--lang-list", action="store_true", help="List languages and exit."
    )
    parser.add_argument("--seed", type=str, default=None, help="RNG seed.")
    parser.add_argument(
        "--type", type=int, choices=[1, 2], default=1, help="Layout type."
    )
    args = parser.parse_args()

    if args.lang_list:
        list_languages()
        sys.exit(0)

    if args.seed:
        random.seed(args.seed)
        print(f"Seed set: {args.seed}")

    lang_config = load_lang_config(args.lang)

    if args.words:
        words_pool = load_custom_words_file(args.words)
    else:
        words_pool = lang_config.get("words", [])

    latex_content = generate_latex(
        words_pool, lang_config["translations"], lang_config["babel_lang"], args.type
    )

    with open("game.tex", "w", encoding="utf-8") as f:
        f.write(latex_content)
    print("Success: game.tex generated.")


if __name__ == "__main__":
    main()
