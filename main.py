from manim import * 

from manim_slides import Slide

TITLE_SIZE = 60
SUB_SIZE = 30
APPEAR_SPEED = 1.3
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
    
    slide.play(DrawBorderThenFill(Title),DrawBorderThenFill(Subtitle),run_time=APPEAR_SPEED)
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
    
    slide.play(DrawBorderThenFill(Title),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))

    slide.next_slide()
    dec_maths =Text("123 = 100+20+3", font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(RIGHT*1.7).shift(UP*1)
    slide.play(Write(dec_maths),run_time=APPEAR_SPEED,)

    slide.next_slide()
    dec_table = VGroup(Table(
        [["100", "10","1"],
        ["1", "2", "3"]]).to_edge(RIGHT).shift(UP*0.9).shift(LEFT*1.74)).scale(0.8)
    slide.play(DrawBorderThenFill(dec_table),run_time=APPEAR_SPEED)

    slide.next_slide()
    bin_maths =Text("101= 4+0+1  (5)",font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(RIGHT*1.7).shift(DOWN*1.85)
#    sub_bin_maths =Text("(5)",font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(DOWN*2.5).shift(RIGHT*1.3)
    slide.play(Write(bin_maths),run_time=APPEAR_SPEED)

    slide.next_slide()
    bin_table = VGroup(Table(
        [["4", "2","1"],
        ["1", "0", "1"]]).to_edge(RIGHT).shift(DOWN*2).shift(LEFT*2.3)).scale(0.8)
    slide.play(DrawBorderThenFill(bin_table),run_time = APPEAR_SPEED)

    slide.next_slide()
    group = VGroup(Title,dec_maths,bin_maths,dec_maths,bin_table,dec_table)
    other_group = VGroup(
        Text("Mai multe exemple:", font_size=TITLE_SIZE*0.95).shift(TOP_POS),
        Text("1101= 8+4+0+1",font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(RIGHT*1.6),
        Text("(adica 13)",font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(DOWN*0.67).shift(RIGHT*0.89).shift(RIGHT*1.6),
        VGroup(Table(
            [["8","4", "2","1"],
            ["1", "1", "0", "1"]]).to_edge(RIGHT).shift(LEFT*1.24)).scale(0.8)
    ).shift(DOWN*0.3).scale(0.8)
    slide.play(Transform(group,other_group))

    slide.next_slide()
    other_group = VGroup(
        Text("Mai multe exemple:", font_size=TITLE_SIZE*0.95).shift(TOP_POS),
        Text("111001= 32+16+8+0+0+1",font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(LEFT*0.6),
        Text("(adica 57)",font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(DOWN*0.67).shift(RIGHT*1.6),
        VGroup(Table(
            [["32","16","8","4","2","1"],
            ["1","1","1","0","0","1"]]).to_edge(RIGHT).shift(RIGHT*1.66)).scale(0.8)
    ).shift(DOWN*0.3).scale(0.8)
    slide.play(Transform(group,other_group))

    slide.next_slide()
    group = VGroup(Title,dec_maths,bin_maths,dec_maths,bin_table,dec_table)
    other_group = VGroup(
        Text("Mai multe exemple:", font_size=TITLE_SIZE*0.95).shift(TOP_POS),
        Text("11.01= 2+1+0+0.25",font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(RIGHT*1.1),
        Text("(adica 3.25)",font_size=SUB_SIZE,slant="ITALIC").to_edge(LEFT).shift(DOWN*0.67).shift(RIGHT*1.59),
        VGroup(Table(
            [["2","1","0.5","0.25"],
            ["1","1","0","1"]]).to_edge(RIGHT).shift(LEFT*0.49)).scale(0.8)
    ).shift(DOWN*0.3).scale(0.8)
    slide.play(Transform(group,other_group))
    
    slide.next_slide()
    slide.play(Unwrite(group),run_time=DISAPPEAR_SPEED)
    #slide.play(Uncreate(sub_bin_maths),Uncreate(Title),Uncreate(bin_maths),Uncreate(dec_maths),Uncreate(bin_table),Uncreate(dec_table),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_8(slide):
    group = VGroup(
        Text("Memoria fizica:", font_size=TITLE_SIZE*0.95).shift(TOP_POS),
        Text("00000000 00000000 00000000 00000000")
    ).shift(DOWN*0.3).scale(0.8)
    
    slide.play(DrawBorderThenFill(group))
    
    slide.next_slide()
    other_group = VGroup(
        Text("De exemplu:", font_size=TITLE_SIZE*0.95).shift(TOP_POS),
        Text("00000000 00000000 00000101 10010011\n=1427")
    ).shift(DOWN*0.3).scale(0.8)
    slide.play(Transform(group,other_group),run_time=APPEAR_SPEED)

    slide.next_slide()
    slide.play(Uncreate(group),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_9(slide):
    group = VGroup(
        Text("Reprezentarea numerlor rationale:", font_size=TITLE_SIZE)
    ).shift(DOWN*0.3).scale(0.8)
    slide.play(Write(group,run_time=APPEAR_SPEED))


    slide.next_slide()
    other_group = VGroup(
        Text("O solutie simpla:", font_size=TITLE_SIZE*0.95).shift(TOP_POS),
        Text("00000000 00000000.00000000 00000000")
    ).shift(DOWN*0.3).scale(0.8)
    slide.play(Transform(group,other_group,run_time=APPEAR_SPEED))

    slide.next_slide()
    other_group = VGroup(
        Text("De exemplu:", font_size=TITLE_SIZE*0.95).shift(TOP_POS),
        Text("00000000 00000011.10000000 00000000\n=3.5"),
    ).shift(DOWN*0.3).scale(0.8)
    slide.play(Transform(group,other_group,run_time=APPEAR_SPEED))

    slide.next_slide()
    other_group = VGroup(
        Text("Capacitatea maxima:", font_size=TITLE_SIZE*0.95).shift(TOP_POS),
        Text("11111111 11111111.11111111 11111111\n=~65536.999985"),
    ).shift(DOWN*0.3).scale(0.8)
    slide.play(Transform(group,other_group,run_time=APPEAR_SPEED))

    slide.next_slide()
    slide.play(Uncreate(group),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_10(slide):
    Title = Text("Un compromis", font_size=TITLE_SIZE).shift(UP*0.5)
    Subtitle = Text("marime > precizie", font_size=SUB_SIZE,slant="ITALIC").shift(DOWN*0.5)

    slide.play(Write(Title),Write(Subtitle),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))
    slide.next_slide()

    slide.play(Uncreate(Title),Uncreate(Subtitle),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_11(slide):
        
    text = Text("Notatia stiintifica a unui numar:", font_size=TITLE_SIZE).shift(TOP_POS)
    slide.play(Write(text))
    
    slide.next_slide()
    group = VGroup(
        MathTex(r"1000 = 1*10^{3}")
    ).shift(DOWN*0.3).scale(1.7)
    
    slide.play(DrawBorderThenFill(group))
    
    slide.next_slide()
    other_group = VGroup(
        MathTex(r"2249 = 2.249*10^{3}")
    ).shift(DOWN*0.3).scale(1.7)
    slide.play(Transform(group,other_group,run_time=APPEAR_SPEED))

    slide.next_slide()
    slide.play(Unwrite(group),Unwrite(text),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_12(slide):
        
    text = Text("Notatia stiintifica binara:", font_size=TITLE_SIZE).shift(TOP_POS)
    slide.play(Write(text))
    
    slide.next_slide()
    group = VGroup(
        MathTex(r"1011 = 1.011*2^{3}"),
        Text("\n(11)",font_size=SUB_SIZE).shift(DOWN*0.6).shift(LEFT*1.4)
    ).shift(DOWN*0.3).scale(1.7)
    
    slide.play(DrawBorderThenFill(group))
    
    slide.next_slide()
    other_group = VGroup(
        MathTex(r"11.001 = 1.1001*2^{1}"),
        Text("\n(3.125)",font_size=SUB_SIZE).shift(DOWN*0.6).shift(LEFT*1.4)
    ).shift(DOWN*0.3).scale(1.7)
    slide.play(Transform(group,other_group,run_time=APPEAR_SPEED))

    slide.next_slide()
    slide.play(Unwrite(group),Unwrite(text),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_13(slide):
    text = VGroup(Text("Notatia stiintifica", font_size=TITLE_SIZE).shift(TOP_POS),
                  Text("in memoria calculatorului:",font_size=TITLE_SIZE).shift(TOP_POS*0.75))
    slide.play(DrawBorderThenFill(text),run_time=APPEAR_SPEED)
    
    slide.next_slide()
    sign=Text("0",font_size=SUB_SIZE*1.4).shift(LEFT*6.2)
    expo=Text("00000000",font_size=SUB_SIZE*1.4).shift(LEFT*3.9)
    mantissa=Text("00000000000000000000000",font_size=SUB_SIZE*1.4).shift(RIGHT*2.2)

    eq = MathTex(r"x*2",font_size=TITLE_SIZE).shift(DOWN*1.5)
    pow = MathTex(r"^{y}",font_size=TITLE_SIZE).shift(DOWN*1.3).shift(RIGHT*0.87)

    
    #shift(DOWN*0.3).scale(0.8)
    slide.play(Write(eq),Write(pow),DrawBorderThenFill(sign),DrawBorderThenFill(expo),DrawBorderThenFill(mantissa),run_time=APPEAR_SPEED)

    slide.next_slide()
    slide.play(Indicate(sign),run_time=3)

    slide.next_slide()
    slide.play(Indicate(expo),Indicate(pow),run_time=3)

    slide.next_slide()
    slide.play(Indicate(mantissa),Indicate(eq),run_time=3)

    slide.next_slide()
    slide.play(Unwrite(eq),Unwrite(pow),Unwrite(sign),Unwrite(expo),Unwrite(mantissa),Unwrite(text),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_14(slide):
    text = Text("Exponentul:", font_size=TITLE_SIZE).shift(TOP_POS*0.8)
    slide.play(Write(text))
    
    slide.next_slide()
    group = VGroup(
        Text("00000000").shift(LEFT*2.5),
        Text("=  -127").shift(RIGHT*1.4)
    ).shift(RIGHT*0.7).scale(0.8)
    slide.play(DrawBorderThenFill(group))
        
    slide.next_slide()
    other_group = VGroup(
        Text("01111111").shift(LEFT*2.5),
        Text("=  0").shift(RIGHT*1.4)
    ).shift(RIGHT*0.7).scale(0.8)
    slide.play(Transform(group,other_group,run_time=APPEAR_SPEED))

    slide.next_slide()
    other_group = VGroup(
        Text("11111111").shift(LEFT*2.5),
        Text("=  128").shift(RIGHT*1.4)
    ).shift(RIGHT*0.7).scale(0.8)
    slide.play(Transform(group,other_group,run_time=APPEAR_SPEED))

    slide.next_slide()
    slide.play(Unwrite(group),Unwrite(text),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))
    

def slide_15(slide):
    text = Text("Mantisa:", font_size=TITLE_SIZE).shift(TOP_POS*0.8)
    slide.play(Write(text))
    
    slide.next_slide()
    # group = VGroup(
    #     #Text("1.",fill_opacity=0.5).shift(LEFT*5.4),
    #     Text("00000000000000000000000").shift(LEFT*0.55)
    # ).shift(RIGHT*0.7).scale(0.8)
    # slide.play(Write(group))

    # slide.next_slide()
    #slide.play(FadeOut(group),run_time=APPEAR_SPEED)
    group = VGroup(
        Text("1.",fill_opacity=0.5).shift(LEFT*5.4),
        Text("00000000000000000000000").shift(LEFT*0.55)
    ).shift(RIGHT*0.7).scale(0.8)
    slide.play(Write(group))

    #lide.play(FadeIn(group),run_time=APPEAR_SPEED)    
    #slide.play(TransformMatchingShapes(group,other_group,run_time=APPEAR_SPEED))
    
    slide.next_slide()
    slide.play(Unwrite(group),Unwrite(text),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_16(slide):    
    text = VGroup(Text("Exemple:", font_size=TITLE_SIZE).shift(TOP_POS))
                  #Text("in memoria calculatorului:",font_size=TITLE_SIZE).shift(TOP_POS*0.75))
 
    sign=Text("0",font_size=SUB_SIZE*1.4).shift(LEFT*6.2)
    expo=Text("10000000",font_size=SUB_SIZE*1.4).shift(LEFT*3.9)
    mantissa=VGroup(
        Text("1.",fill_opacity=0.5).shift(LEFT*3.5),
        Text("00000000000000000000001").shift(RIGHT*1.45)
    ).shift(RIGHT*0.7).scale(0.8)

    eq = MathTex(r"1.1*2^{1} = 3",font_size=TITLE_SIZE).shift(DOWN*1.5)
    
    
    slide.play(DrawBorderThenFill(text),Write(eq),DrawBorderThenFill(sign),DrawBorderThenFill(expo),DrawBorderThenFill(mantissa),run_time=APPEAR_SPEED*0.5)

    slide.next_slide()
    slide.play(Unwrite(eq),Unwrite(sign),Unwrite(expo),Unwrite(mantissa),Unwrite(text),run_time=DISAPPEAR_SPEED*0.5)
    slide.play(Wait(0.15))

def slide_17(slide):    
    text = VGroup(Text("Exemple:", font_size=TITLE_SIZE).shift(TOP_POS))
                  #Text("in memoria calculatorului:",font_size=TITLE_SIZE).shift(TOP_POS*0.75))
 
    sign=Text("0",font_size=SUB_SIZE*1.4).shift(LEFT*6.2)
    expo=Text("10000101",font_size=SUB_SIZE*1.4).shift(LEFT*3.9)
    mantissa=VGroup(
        Text("1.",fill_opacity=0.5).shift(LEFT*3.5),
        Text("00000000000000000000001").shift(RIGHT*1.45)
    ).shift(RIGHT*0.7).scale(0.8)
    eq = MathTex(r"1.0*2^{6} = 64",font_size=TITLE_SIZE).shift(DOWN*1.5)
    
    
    slide.play(DrawBorderThenFill(text),Write(eq),DrawBorderThenFill(sign),DrawBorderThenFill(expo),DrawBorderThenFill(mantissa),run_time=APPEAR_SPEED*0.5)

    slide.next_slide()
    slide.play(Unwrite(eq),Unwrite(sign),Unwrite(expo),Unwrite(mantissa),Unwrite(text),run_time=DISAPPEAR_SPEED*0.5)
    slide.play(Wait(0.15))

def slide_18(slide):

    Title = Text("Cazuri speciale", font_size=TITLE_SIZE)
    
    slide.play(Write(Title),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))

    slide.next_slide()
    slide.play(Uncreate(Title),run_time=DISAPPEAR_SPEED)
    slide.play(Wait(0.15))

def slide_19(slide):    
    text = VGroup(Text("Subnormale:", font_size=TITLE_SIZE).shift(TOP_POS))
                  #Text("in memoria calculatorului:",font_size=TITLE_SIZE).shift(TOP_POS*0.75))
 
    sign=Text("0",font_size=SUB_SIZE*1.4).shift(LEFT*6.2)
    expo=Text("00000000",font_size=SUB_SIZE*1.4).shift(LEFT*3.9)
    mantissa= VGroup(
        Text("0.",fill_opacity=0.5).shift(LEFT*3.5),
        Text("00000000000000000000001").shift(RIGHT*1.45)
    ).shift(RIGHT*0.7).scale(0.8)


    eq = MathTex(r"1.4*10^{-45}",font_size=TITLE_SIZE).shift(DOWN*1.5)
    
    
    slide.play(DrawBorderThenFill(text),Write(eq),DrawBorderThenFill(sign),DrawBorderThenFill(expo),DrawBorderThenFill(mantissa),run_time=APPEAR_SPEED*0.5)

    slide.next_slide()
    slide.play(Unwrite(eq),Unwrite(sign),Unwrite(expo),Unwrite(mantissa),Unwrite(text),run_time=DISAPPEAR_SPEED*0.5)
    slide.play(Wait(0.15))

def slide_20(slide):    
    text = VGroup(Text("Infinitati:", font_size=TITLE_SIZE).shift(TOP_POS))
                  #Text("in memoria calculatorului:",font_size=TITLE_SIZE).shift(TOP_POS*0.75))
 
    sign=Text("0",font_size=SUB_SIZE*1.4).shift(LEFT*6.2)
    expo=Text("11111111",font_size=SUB_SIZE*1.4).shift(LEFT*3.9)
    mantissa=Text("00000000000000000000000",font_size=SUB_SIZE*1.4).shift(RIGHT*2.2)

    eq = MathTex(r"\infty",font_size=TITLE_SIZE).shift(DOWN*1.5)
    
    
    slide.play(DrawBorderThenFill(text),Write(eq),DrawBorderThenFill(sign),DrawBorderThenFill(expo),DrawBorderThenFill(mantissa),run_time=APPEAR_SPEED*0.5)

    slide.next_slide()
    slide.play(Unwrite(eq),Unwrite(sign),Unwrite(expo),Unwrite(mantissa),Unwrite(text),run_time=DISAPPEAR_SPEED*0.5)
    slide.play(Wait(0.15))

def slide_21(slide):    
    text = VGroup(Text("Infinitati:", font_size=TITLE_SIZE).shift(TOP_POS))
                  #Text("in memoria calculatorului:",font_size=TITLE_SIZE).shift(TOP_POS*0.75))
 
    sign=Text("1",font_size=SUB_SIZE*1.4).shift(LEFT*6.2)
    expo=Text("11111111",font_size=SUB_SIZE*1.4).shift(LEFT*3.9)
    mantissa=Text("00000000000000000000000",font_size=SUB_SIZE*1.4).shift(RIGHT*2.2)

    eq = MathTex(r"-\infty",font_size=TITLE_SIZE).shift(DOWN*1.5)
    
    
    slide.play(DrawBorderThenFill(text),Write(eq),DrawBorderThenFill(sign),DrawBorderThenFill(expo),DrawBorderThenFill(mantissa),run_time=APPEAR_SPEED*0.5)

    slide.next_slide()
    slide.play(Unwrite(eq),Unwrite(sign),Unwrite(expo),Unwrite(mantissa),Unwrite(text),run_time=DISAPPEAR_SPEED*0.5)
    slide.play(Wait(0.15))

def slide_22(slide):    
    text = VGroup(Text("NaN:", font_size=TITLE_SIZE).shift(TOP_POS))
                  #Text("in memoria calculatorului:",font_size=TITLE_SIZE).shift(TOP_POS*0.75))
 
    sign=Text("1",font_size=SUB_SIZE*1.4).shift(LEFT*6.2)
    expo=Text("11111111",font_size=SUB_SIZE*1.4).shift(LEFT*3.9)
    mantissa=Text("00000000000000000000001>=",font_size=SUB_SIZE*1.4).shift(RIGHT*2.4)

    eq = MathTex(r"NaN",font_size=TITLE_SIZE).shift(DOWN*1.5)
    
    
    slide.play(DrawBorderThenFill(text),Write(eq),DrawBorderThenFill(sign),DrawBorderThenFill(expo),DrawBorderThenFill(mantissa),run_time=APPEAR_SPEED*0.5)

    slide.next_slide()
    slide.play(Unwrite(eq),Unwrite(sign),Unwrite(expo),Unwrite(mantissa),Unwrite(text),run_time=DISAPPEAR_SPEED*0.5)
    slide.play(Wait(0.15))

def slide_23(slide):

    Title = Text("Va multumesc!", font_size=TITLE_SIZE)
    
    slide.play(Write(Title),run_time=APPEAR_SPEED)
    slide.play(Wait(0.1))

    slide.next_slide()
    slide.play(Uncreate(Title),run_time=DISAPPEAR_SPEED)
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
        slide_8(self)
        slide_9(self)
        slide_10(self)
        slide_11(self)
        slide_12(self)
        slide_13(self)
        slide_14(self)
        slide_15(self)
        slide_16(self)
        slide_17(self)
        slide_18(self)
        slide_19(self)
        slide_20(self)
        slide_21(self)
        slide_22(self)
        slide_23(self)
