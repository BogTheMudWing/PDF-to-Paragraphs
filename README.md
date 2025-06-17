# PDF to Paragraphs

A Python script that converts a PDF ebook into a JSON list of paragraphs.

## About

I created this script to create computer-friendly index of paragraphs so that I could quickly find paragraph numbers using [BogTheMudWing/Paragraph-Finder](https://github.com/BogTheMudWing/Paragraph-Finder).

Unfortunately, PDFs are not very computer-friendly, and so the paragraphs must be detected by the presence of an indent (a change in position for a block of text). This is an imperfect solution and will usually leave lots to clean up, but it handles most of the tedious work of converting the file.

## Use

Once you have downloaded the script, you'll need to install pymupdf using your package manager. This depends on your operating system, so do some searching for instructions on how to do this.

After that, open a terminal and run the script. It will ask you for the PDF file. It is easiest to have the PDF in the same folder as the script. Then, just type the name into the prompt (including the .pdf file extension), and it will create or overwrite output.json.

---

[![BogTheMudWing](https://nextcloud.macver.org/apps/files_sharing/publicpreview/jyWLnm4i724mxXg?file=/&fileId=61792&x=3390&y=1906&a=true&etag=c43260166526abc326861afd5244df8e)](https://blog.macver.org/about-me)
