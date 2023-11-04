import numpy as np


data = np.load('FILENAME.npy')
caption = "ENTER CAPTION HERE"
label = "ADD LABEL HERE"

rows = data.shape[0]
cols = data.shape[1]

colsConfig = 'c'*(cols+1)

headings = "Heading & "*(cols)
headings = "\t\t "+headings+"Heading\\\\\n"

header = "\\begin{table}\n\t\centering\n\t\\scriptsize\n\t\\renewcommand{\\arraystretch}{1.5}\n\t\\setlength\\tabcolsep{1.5pt}\n\t\\caption{"+f"{caption}"+"}\n\t\\begin{tabular}\{"+f"{colsConfig}"+"}\n\t\t\\toprule\n"		
footer = "\\bottomrule\n\t\\end{tabular}\n\t\\label{"+f"{label}"+"}\n\\end{table}"  

content = "\t\t"

for i in range(rows):
    for j in range(cols):
        content += " & "f'{data[i][j]:.4f}'
    content += "\n\t\t"

 
with open('res.txt','w') as f:
    f.write(header+headings+content+footer)


