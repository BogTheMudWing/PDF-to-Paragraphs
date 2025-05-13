import fitz
import json

def extract_text_by_indent(pdf_path):
    doc = fitz.open(pdf_path)
    paragraphs: list[str] = []
    current_paragraph = []
    base_x = None
    indented_x = None

    current_page = 0

    for page in doc:
        blocks = page.get_text("blocks")
        blocks = sorted(blocks, key=lambda x: (x[1], x[0]))  # Top-to-bottom, then left-to-right

        for i, block in enumerate(blocks):
            text = block[4].strip()
            x0 = block[0]

            if text:
                is_new_paragraph = False
                set_base_x = False
                clear_base_x = False
                set_indented_x = False

                if base_x == None:
                    set_base_x = True
                    is_new_paragraph = False
                else:
                    if x0 - base_x < 0.1 and x0 - base_x > -0.1:
                        is_new_paragraph = False
                    else:
                        if indented_x is None:
                            if x0 - base_x > 0:
                                set_indented_x = True
                                clear_base_x = True
                                is_new_paragraph = True
                            else:
                                set_base_x = True
                                is_new_paragraph = False
                        else:
                            if x0 - indented_x < 0.1 and x0 - indented_x > -0.1:
                                is_new_paragraph = True
                            else:
                                if x0 - base_x > 0:
                                    set_indented_x = True
                                    clear_base_x = True
                                    is_new_paragraph = True
                                else:
                                    set_base_x = True
                                    is_new_paragraph = False

                # print("Page " + str(current_page) + " block " + str(i) + ": x0=" + str(x0) + ", base_x=" + str(base_x) + ", indented_x=" + str(indented_x) + ", new_paragraph=" + str(is_new_paragraph) + ": " + str(text))

                lines = text.split("\n")

                for line in lines:
                    print(line)

                if is_new_paragraph:
                    if current_paragraph:
                        paragraphs.append(" ".join(current_paragraph).strip())
                    for i, line in enumerate(lines):
                        if i == len(lines) - 1:
                            current_paragraph = [line]
                        else:
                            paragraphs.append("".join(line).strip())
                else:
                    current_paragraph.append(text)

                if set_base_x:
                    base_x = x0
                if clear_base_x:
                    base_x = None
                if set_indented_x:
                    indented_x = x0

        current_page = current_page + 1

    return paragraphs

def save_paragraphs_to_json(paragraphs, json_path):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(paragraphs, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    pdf_file = input("Enter the PDF file: ") # Input file
    json_file = "output.json" # Output file

    paragraphs = extract_text_by_indent(pdf_file)
    save_paragraphs_to_json(paragraphs, json_file)
    print(f"Extracted {len(paragraphs)} paragraphs and saved to {json_file}")
