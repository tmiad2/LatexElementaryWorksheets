import random
import math

def remap(x, x1, x2, y1, y2):
    return (x - x1) / (x2 - x1) * (y2 - y1) + y1


def inverse_cdf(x):
    assert x >= 0
    assert x <= 1
    num_sets = [(0.1,0, 9), (3,10, 99), (5,100, 999), (3,1000, 9999), (3,10000, 99999)]
    total_weight = 0.0
    for (weight,_,_) in num_sets:
        total_weight = total_weight+ weight
    for (weight,begin,end) in num_sets:
        q = weight/total_weight
        if x < q:
            return round(remap(x, 0, q, begin, end))
        else:
            x = x - q
    return 1324


def output_preamble():
    print(r"\documentclass[letter]{article}")
    print(r"\usepackage[hmargin=0.5cm,vmargin=1.0cm,bindingoffset=0.0cm]{geometry}")
    print(r"\usepackage{amssymb}")
    print(r"\usepackage{amsmath}")
    print(r"\usepackage[letterspace=150]{microtype}")
    print(r"\usepackage{array}")
    print(r"\usepackage{wrapfig,lipsum,graphicx}")
    print(r"""\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}""")
    print(r"\pagestyle{empty}")
    print(r"\parskip = 1.0 cm")
    print(r"\parindent = 0.0 cm")
    print(r"""
\newcommand\blank{\underline{\hspace{2cm}}} % Gives a blank 
\newcounter{prob} % A new counter for current problem number
\setcounter{prob}{1} % Start the counter at the value 1
\newcommand\itm{
\fbox{\textbf{\theprob}} \refstepcounter{prob}
} % Calls problem number
\newcommand{\problem}[1]{\makebox[0.5cm]{\itm}   
  \begin{minipage}[t]{\textwidth-0.5cm} #1 \end{minipage} 
}
\newcommand\divi[2]{
#2 \: \begin{array}{|l}
\hline #1
\end{array}
}

\newcommand\mult[2]{
$\begin{array}{rr} 
 & #1 \\ 
 \times & #2 \\ \hline 
 \end{array}$}
 
\newcommand\addi[2]{
  $\begin{array}{rr} 
   &  #1 \\ 
    + & #2 \\ \hline 
  \end{array}$}

\newcommand\subt[2]{
  $\begin{array}{rr}
    & #1 \\ 
    - & #2 \\ \hline
  \end{array}$}""")
    print(r"\begin{document}")
    print(
        r"""\setlength{\extrarowheight}{0.12cm}
\renewcommand\addi[2]{
\hspace*{5mm}\begin{tabular}{rr} \vspace{-2mm}
 & #1 \\
 $ + $ & #2 \\ \hline \vspace*{4.0mm}
 \end{tabular}}
\renewcommand\subt[2]{
\hspace*{5mm}\begin{tabular}{rr} \vspace{-2mm}
 & #1 \\
 $ - $ & #2 \\ \hline \vspace*{4.0mm}
 \end{tabular}}
\renewcommand\mult[2]{
\hspace*{5mm}\begin{tabular}{rr} \vspace{-2mm}
 & #1 \\
 $ \times $ & #2 \\ \hline \vspace*{4.0mm}
 \end{tabular}}

 
"""
    )


def output_title(title):
    print(
        r"""\begin{center} 
  \textsc{""",
        end="",
    )
    print(title, end="")
    print(
        r"""}
\end{center} """
    )
    print(
        r"""

\begin{wrapfigure}[8]{c}{2cm}
  \centering
  \includegraphics[width=\linewidth]{Ryan.jpg}
\end{wrapfigure}

        \begin{Huge}
Date:\underline{\hspace*{6cm}} \hfill
Name:\underline{\hspace*{6cm}}
\lsstyle
"""
    )


def output_directions(directions):
    print(
        r"""\textit{Directions}

\problem{""",
        end="",
    )
    print(directions, end="")
    print("}\n")


def output_array_start(columns):
    print(
        r"""

$$
\begin{array}{""",end='')
    for i in range(0, columns):
        print("c", end="")
    print(r"""}""")


def output_var(x):
    print(r"{", end="")
    print(x, end="")
    print(r"}", end="")


def output_array(rows, columns):
    output_array_start(columns)
    for i in range(0, rows):
        for j in range(0, columns):
            r = random.random()
            if r < 0.3:
                version = "subt"
            elif r <0.6:
                version = "addi"
            elif r <0.8:
                version = "mult"
            else:
                version = "divi"
            x = inverse_cdf(random.random())
            y = inverse_cdf(random.random())
            if version == "subt":
                if x < y:
                    temp = x
                    x = y
                    y = temp
            elif version == "mult":
                x = random.randint(0,12)
                y = random.randint(0,12)
            elif version == "divi":
                x = random.randint(1,144)
                y = random.randint(1,int(math.ceil(x/2)))
            print("\\", end="")
            print(version, end="")
            output_var(x)
            output_var(y)
            if j != columns - 1:
                print(" & ",end='')
            else:
                print(r"\\")

    output_array_end()


def output_array_end():
    print(
        r"""\end{array}
$$
\end{Huge}"""
    )


def output_post():
    print(r"\end{document}")


output_preamble()
output_title("Arithmetic Worksheet")
#output_directions("Perform the addition or subtraction indicated.")
output_array(5,4)
output_post()
