import os

import csv
import pdfkit
from PyPDF2 import PdfFileMerger

with open('metadata.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';', quotechar='\'')
    rows = list(reader)

for row in rows:
    author, title, date, filename = row

    body = f"""
        <html>
          <head>
            <meta name="pdfkit-page-size" content="Letter"/>
            <meta name="pdfkit-orientation" content="Portrait"/>
            <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
          </head>
          <p>This is a file in the Digital Central Asian Archaeology (DCAA) project:</p>
          <p>{author}. ({date}). {title}</p>
          <p>
          The DCAA is part of the Ancient World Digital Library hosted by the <a href="http://isaw.nyu.edu/library">Institute for the Study of the Ancient World Library.</a><br/><br/>
          <img src="/Users/patrick/envs/fda-experiments/img/logo.png" />
          </p>
          <p>Rights statement etc.</p>
          </html>
        """

    pdfkit.from_string(body, f'out/{author}_{date}.pdf')

#
# pdfs = [file for file in os.listdir('out') if file.endswith('pdf')]
#


for row in rows[1:]:
    author, title, date, filename = row

    merger = PdfFileMerger()

    cover = f'out/{author}_{date}.pdf'
    pdf = f'pdfs/{filename}'
    print(f'Working on {pdf}')

    docs = [cover, pdf]
    for doc in docs:
        merger.append(open(doc, 'rb'))
    with open(f'merged/{filename}', 'wb') as f:
        merger.write(f)

# for pdf in pdfs:
#     merger.append(open(pdf, 'rb'))
#
# with open('result.pdf', 'wb') as fout:
#     merger.write(fout)
