from manim import * 

from manim_slides import Slide

TITLE_SIZE = 75
SUB_SIZE = 40
APPEAR_SPEED = 1.25
DISAPPEAR_SPEED=0.5

TOP_POS = UP*2.8

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
    Title = Text('Știați că numarul "0.3"', font_size=TITLE_SIZE).shift(UP*0.5)
    Subtitle = Text('nu există?', font_size=TITLE_SIZE).shift(DOWN*0.5)
    
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

    Title = Text("Despre aceasta prezentare", font_size=TITLE_SIZE*0.8)
    
    slide.play(Write(Title),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))
    slide.next_slide()

    slide.play(Uncreate(Title),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_5(slide):

    Title = Text("S-o luam cu inceputul", font_size=TITLE_SIZE)
    
    slide.play(Write(Title),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))

    slide.next_slide()
    slide.play(Uncreate(Title),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_6(slide):

    Title = Text("Sistemul binar", font_size=TITLE_SIZE)
    
    slide.play(Write(Title),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))

    slide.next_slide()
    slide.play(Uncreate(Title),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_7(slide):

    Title = Text("Cum functioneaza?", font_size=TITLE_SIZE*0.95).shift(TOP_POS)
    
    slide.play(Write(Title),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))

    slide.next_slide()
    dec_maths =Text("123 = 100+20+3", font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(UP*1)
    slide.play(Write(dec_maths),run_time=APPEAR_SPEED,)

    slide.next_slide()
    dec_table = Table(
        [["100", "10","1"],
        ["1", "2", "3"]]).to_edge(RIGHT).shift(UP*0.9).shift(LEFT*0.74)
    slide.play(DrawBorderThenFill(dec_table),run_time=APPEAR_SPEED)

    slide.next_slide()
    bin_maths =Text("1101= 8+4+0+1",font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(DOWN*1.85)
    sub_bin_maths =Text("(adica 13)",font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(DOWN*2.5).shift(RIGHT*0.89)
    slide.play(Write(sub_bin_maths),Write(bin_maths),run_time=APPEAR_SPEED)

    slide.next_slide()
    bin_table = Table(
        [["8","4", "2","1"],
        ["1", "1", "0", "1"]]).to_edge(RIGHT).shift(DOWN*2).shift(LEFT*0.24)
    slide.play(DrawBorderThenFill(bin_table),run_time = APPEAR_SPEED)

    slide.next_slide()
    slide.play(Uncreate(sub_bin_maths),Uncreate(Title),Uncreate(bin_maths),Uncreate(dec_maths),Uncreate(bin_table),Uncreate(dec_table),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

class IEEPresentation(Slide):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        slide_1(self)
        slide_2(self)
        slide_3(self)
        slide_4(self)
        slide_5(self)
        slide_6(self)
        slide_7(self)