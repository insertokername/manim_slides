This is a presentation i made for a school project about the IEE 754 standard

the presentation is very bare bones and it only serves as a visual aid to the actual explanations

# dependecies
ffmpeg `choco install ffmpeg`

latex for manim `choco install manim-latex` or follow [the manim docs](https://docs.manim.community/en/stable/installation/windows.html)

python version **BELOW OR EQUAL TO 3.11** as of writing since manim-slides is not functional in >=python3.12
also:
`pip install -r requirements.txt`

# rendering:
just run one of the script (present_render is for higher resolution and fps) and then open the output html file with your browser or run it with `manim-slides present IEEPresentation` 
