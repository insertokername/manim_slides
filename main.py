from manim import * 

from manim_slides import Slide

TITLE_SIZE = 75
SUB_SIZE = 40
APPEAR_SPEED = 1.2
DISAPPEAR_SPEED=0.5

def slide_1(slide):
    Title = Text("Standardul IEEE 754", font_size=TITLE_SIZE).shift(UP*0.5)
    Subtitle = Text("Reprezentarea numerelor rationale", font_size=SUB_SIZE,slant="ITALIC").shift(DOWN*0.5)
    Subtitle2 = Text("in memoria calculatorului", font_size=SUB_SIZE,slant="ITALIC").shift(DOWN*1)

    slide.play(Write(Title),Write(Subtitle),Write(Subtitle2),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))
    slide.next_slide()

    slide.play(Uncreate(Title),Uncreate(Subtitle),Uncreate(Subtitle2),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_2(slide):
    Title = Text("Fun fact", font_size=TITLE_SIZE).shift(UP*0.5)
    Subtitle = Text('Știați că numarul "0.3" nu există?', font_size=SUB_SIZE,slant="ITALIC").shift(DOWN*0.5)
    
    slide.play(Write(Title),Write(Subtitle),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))
    slide.next_slide()

    slide.play(Uncreate(Title),Uncreate(Subtitle),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_3(slide):

    Title1 = Text("Standardul IEEE-754 1982", font_size=TITLE_SIZE-27).shift(UP*0.5)
    Title = Text("pentru single-precision floating point", font_size=TITLE_SIZE-27).shift(DOWN*0.5)

    slide.play(Write(Title),Write(Title1),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))
    slide.next_slide()

    slide.play(Uncreate(Title),Uncreate(Title1),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_4(slide):

    Title = Text("Despre aceasta prezentare", font_size=TITLE_SIZE)
    
    slide.play(Write(Title),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))
    slide.next_slide()

    slide.play(Uncreate(Title),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

class BasicExample(Slide):
    def construct(self):
        self.camera.background_color = DARKER_GREY
        slide_1(self)
        slide_2(self)
        slide_3(self)
        slide_4(self)