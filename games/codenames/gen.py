import argparse
import random
import json
import os
import sys

LANG_DIR = "./lang"
THEMES_DIR = "./themes"
FALLBACK_DOMAIN = "github.com/Hostek/print-legendary-octo-parakeet"


def get_project_domain():
    possible_paths = ["../../PROJECT_CONFIG.json", "./PROJECT_CONFIG.json"]
    for path in possible_paths:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f).get("domain_url", FALLBACK_DOMAIN)
            except Exception:
                pass
    return FALLBACK_DOMAIN


def bootstrap_folders():
    if not os.path.exists(LANG_DIR):
        os.makedirs(LANG_DIR)
    if not os.path.exists(THEMES_DIR):
        os.makedirs(THEMES_DIR)


def list_languages():
    bootstrap_folders()
    files = [f for f in os.listdir(LANG_DIR) if f.endswith(".json")]
    if not files:
        print("No languages found.")
        return
    print("Available languages:")
    for filename in sorted(files):
        lang_code = os.path.splitext(filename)[0]
        try:
            with open(os.path.join(LANG_DIR, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                print(f"  - {lang_code:6}: {data.get('full_lang_name')}")
        except:
            pass


def load_lang_config(lang_code):
    filepath = os.path.join(LANG_DIR, f"{lang_code}.json")
    if not os.path.exists(filepath):
        print(f"Error: Language '{lang_code}' not found.")
        sys.exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    domain = get_project_domain()
    if "translations" in data and "watermark" in data["translations"]:
        data["translations"]["watermark"] = data["translations"]["watermark"].replace(
            "[DOMAIN_URL]", domain
        )
    return data


def load_words(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    if filepath.endswith(".json"):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def generate_latex(words, translations, babel_lang, layout_type):
    if len(words) < 25:
        print(f"Error: Word list too short ({len(words)}/25).")
        sys.exit(1)

    selected_words = random.sample(words, 25)
    key_roles = (["A"] * 9) + (["B"] * 8) + ["N"] * 7 + ["X"]
    random.shuffle(key_roles)
    watermark_tex = rf"\vfill \centering \color{{gray}}{{\tiny {translations.get('watermark', '')}}}"

    grid_rows = ""
    for i in range(5):
        row = selected_words[i * 5 : (i + 1) * 5]
        grid_rows += (
            "        "
            + " & ".join([rf"\textbf{{\Large {w}}}" for w in row])
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
    \\renewcommand{{\\arraystretch}}{{3.8}}\\begin{{tabular}}{{|Y|Y|Y|Y|Y|}}\\hline {spymaster_rows} \\end{{tabular}}
    \\vfill \\rotatebox{{180}}{{\\begin{{minipage}}{{\\linewidth}}\\centering
    \\renewcommand{{\\arraystretch}}{{3.8}}\\begin{{tabular}}{{|Y|Y|Y|Y|Y|}}\\hline {spymaster_rows} \\end{{tabular}}
    \\par\\vspace{{0.3cm}}{{\\Large \\textbf{{{translations['key_title_1']}}}}}\\end{{minipage}}}}
    {watermark_tex}
\\end{{center}}"""
    else:

        def fmt(r):
            if r == "A":
                return r"\cellcolor{black!60}\color{white}{\textbf{A}}"
            if r == "B":
                return r"\cellcolor{black!20}\color{black}{\textbf{B}}"
            if r == "N":
                return r"\cellcolor{white}\color{black}{\textbf{--}}"
            return r"\cellcolor{black}\color{white}{\textbf{X}}"

        k_rows = [
            " & ".join([fmt(r) for r in key_roles[i * 5 : (i + 1) * 5]]) + r" \\ \hline"
            for i in range(5)
        ]
        kt = "\n        ".join(k_rows)
        page_2_code = f"""\\newgeometry{{portrait, a4paper, margin=1.5cm}}
\\begin{{center}}
    {{\\Large \\textbf{{{translations['key_title_1']}}}}} \\par\\vspace{{0.5cm}}
    \\renewcommand{{\\arraystretch}}{{2.8}}\\begin{{tabular}}{{|Z|Z|Z|Z|Z|}}\\hline {kt} \\end{{tabular}}
    \\par\\vspace{{1.2cm}} \\noindent\\centerline{{- - - - {translations['cut_here']} - - - -}}
    \\par\\vspace{{1.2cm}} {{\\Large \\textbf{{{translations['key_title_2']}}}}} \\par\\vspace{{0.5cm}}
    \\begin{{tabular}}{{|Z|Z|Z|Z|Z|}}\\hline {kt} \\end{{tabular}}
    {watermark_tex}
\\end{{center}}"""

    return f"""\\documentclass[11pt, a4paper]{{article}}
\\usepackage[a4paper]{{geometry}}
\\usepackage{{tabularx, colortbl, xcolor, graphicx, fontspec}}
\\usepackage[{babel_lang}]{{babel}}
\\IfFontExistsTF{{Linux Libertine O}}{{\\setmainfont{{Linux Libertine O}}}}{{\\IfFontExistsTF{{Liberation Serif}}{{\\setmainfont{{Liberation Serif}}}}{{\\IfFontExistsTF{{Times New Roman}}{{\\setmainfont{{Times New Roman}}}}{{}}}}}}
\\newcolumntype{{Y}}{{>{{\\centering\\arraybackslash}}m{{3.5cm}}}}\\newcolumntype{{Z}}{{>{{\\centering\\arraybackslash}}m{{2.0cm}}}}
\\begin{{document}}
\\pagestyle{{empty}}\\newgeometry{{landscape, a4paper, margin=0.8cm}}
\\begin{{center}}
    {{\\Large \\textbf{{{translations['title']}}}}} \\par\\vspace{{0.3cm}}
    \\renewcommand{{\\arraystretch}}{{4.2}}\\begin{{tabular}}{{|Y|Y|Y|Y|Y|}}\\hline {grid_rows} \\end{{tabular}}
    \\vfill \\rotatebox{{180}}{{\\begin{{minipage}}{{\\linewidth}}\\centering
    \\renewcommand{{\\arraystretch}}{{4.2}}\\begin{{tabular}}{{|Y|Y|Y|Y|Y|}}\\hline {grid_rows} \\end{{tabular}}
    \\par\\vspace{{0.3cm}}{{\\Large \\textbf{{{translations['title']}}}}}\\end{{minipage}}}}
    {watermark_tex}
\\end{{center}}
\\newpage\\restoregeometry {page_2_code}
\\end{{document}}"""


def main():
    bootstrap_folders()
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", type=str, default="en")
    parser.add_argument("--words", type=str, default=None)
    parser.add_argument("--theme", type=str, default=None)
    parser.add_argument("--lang-list", action="store_true")
    parser.add_argument("--seed", type=str, default=None)
    parser.add_argument("--type", type=int, choices=[1, 2], default=1)
    args = parser.parse_args()

    if args.lang_list:
        list_languages()
        return
    if args.seed:
        random.seed(args.seed)

    config = load_lang_config(args.lang)

    if args.theme:
        word_file = f"./themes/{args.lang}/{args.theme}.txt"
        print(f"Loading theme: {args.theme} ({args.lang})")
        words_pool = load_words(word_file)
    elif args.words:
        words_pool = load_words(args.words)
    else:
        words_pool = config.get("words", [])

    latex = generate_latex(
        words_pool, config["translations"], config["babel_lang"], args.type
    )
    with open("game.tex", "w", encoding="utf-8") as f:
        f.write(latex)
    print("Success: game.tex generated.")


if __name__ == "__main__":
    main()
