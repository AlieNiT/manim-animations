from math import cos, sin
from manim import *


class Scene0(Scene):
    def construct(self):
        # event_image = 
        event_image = ImageMobject("event-image.png").scale(0.7).shift(LEFT * 0.2)
        event_image2 = ImageMobject("event-image.png").scale(0.2).shift(LEFT * 6.25 + DOWN * 3.1)
        # self.add(event_image)
        self.play(GrowFromCenter(event_image))
        self.wait(2)
        self.play(Transform(event_image, event_image2))
        self.wait(1)

class Scene1(Scene):
    def construct(self):
        c1 = Circle(2, WHITE).shift(2 * RIGHT)
        vt = ValueTracker(0.00001)
        time_text =  MathTex("Time: ").scale(1.5).shift(LEFT * 4.5 + UP * 2.5)
        t_value_text = always_redraw(
            lambda: MathTex('%.1f'%vt.get_value()).scale(1.5).next_to(time_text, RIGHT, buff=0.1)
        )
        T = 4
        times = VGroup()
        time1 = MathTex(str(1 * T) + ".0").next_to(t_value_text, DOWN, 0.3).set_color(GREEN).scale(1.5)
        time2 = MathTex(str(2 * T) + ".0").next_to(time1, DOWN, 0.3).set_color(YELLOW).scale(1.5)
        time3 = MathTex(str(3 * T) + ".0").next_to(time2, DOWN, 0.3).set_color(GOLD).scale(1.5)
        time4 = MathTex(str(4 * T) + ".0").next_to(time3, DOWN, 0.3).set_color(RED).scale(1.5)
        time5 = MathTex(str(5 * T) + ".0").next_to(time4, DOWN, 0.3).set_color(MAROON).scale(1.5)
        time6 = MathTex(str(6 * T) + ".0").next_to(time5, DOWN, 0.3).set_color(PURPLE).scale(1.5)

        times.add(time1, time2, time3, time4, time5, time6)
        car = always_redraw(
            lambda : SVGMobject("car.svg")
            .set_color(GREEN if vt.get_value() < T else 
                        (YELLOW if vt.get_value() < 2 * T else 
                          (GOLD if vt.get_value() < 3 * T else 
                            (RED if vt.get_value() < 4 * T else 
                              (MAROON if vt.get_value() < 5 * T else 
                                PURPLE
                              )
                            )
                          )
                        )
                      )
            .set(width=0.3)
            .scale(5)
            .next_to(c1, UP, 0)
            .rotate(vt.get_value() * 2 * PI / T, about_point= c1.get_center())
        )
        event_image = ImageMobject("event-image.png").scale(0.2).shift(LEFT * 6.25 + DOWN * 3.1)
        self.add(event_image)
        self.wait(1)
        self.play(Create(c1), run_time = 0.7)
        self.play(Create(car), run_time = 0.7)
        self.play(Write(time_text), run_time = 0.6)
        self.play(Write(t_value_text), run_time = 0.6)
        self.wait(1)

        self.play(vt.animate.set_value(1 * T), rate_func = linear, run_time = T * 9/8)
        self.play(Transform(t_value_text, time1), Create(time1), vt.animate.set_value(T + 0.2), rate_func = linear, run_time = 0.2* 9/8)
        self.play(vt.animate.set_value(2 * T), rate_func = linear, run_time = 9/8 * (T - 0.2))
        self.play(Transform(t_value_text, time2), Create(time2), vt.animate.set_value(2 * T + 0.2), rate_func = linear, run_time = 0.2* 9/8)
        self.play(vt.animate.set_value(3 * T), rate_func = linear, run_time = 9/8 * (T - 0.2))
        self.play(Transform(t_value_text, time3), Create(time3), vt.animate.set_value(3 * T + 0.2), rate_func = linear, run_time = 0.2* 9/8)
        self.play(vt.animate.set_value(4 * T), rate_func = linear, run_time = 9/8 * (T - 0.2))
        self.play(Transform(t_value_text, time4), Create(time4), vt.animate.set_value(4 * T + 0.2), rate_func = linear, run_time = 0.2* 9/8)
        self.play(vt.animate.set_value(5 * T), rate_func = linear, run_time = 9/8 * (T - 0.2))
        self.play(Transform(t_value_text, time5), Create(time5), vt.animate.set_value(5 * T + 0.2), rate_func = linear, run_time = 0.2* 9/8)
        self.play(vt.animate.set_value(6 * T), rate_func = linear, run_time = 9/8 * (T - 0.2))
        self.play(Transform(t_value_text, time6), Create(time6), run_time = 0.2)
        self.wait(1.5)
        self.play(FadeOut(car, scale=1.5), FadeOut(c1, scale=1.5),
                  FadeOut(time_text, scale=1.5), FadeOut(t_value_text, scale=1.5), FadeOut(times), run_time = 1)
        self.wait(1.5)
class tmp(Scene):
    def construct(self):
        car = always_redraw(
            lambda : SVGMobject("car.svg")
        )
        self.play(Create(car))
        self.wait()
        self.play(Flash(car))
        self.wait()

class Scene11WITHQ(Scene):
    def construct(self):
        T = MathTex("T").scale(9).shift(LEFT * 3)
        f = MathTex("f").scale(9).shift(RIGHT * 3)
        question_mark = MathTex("\\mathord{?}").scale(9).shift()
        event_image = ImageMobject("event-image.png").scale(0.2).shift(LEFT * 6.25 + DOWN * 3.1)
        self.add(event_image)
        self.play(Write(T), run_time = 1)
        self.play(Write(f), run_time = 1)
        self.wait(1)
        self.play(Write(question_mark), run_time = 1)
        self.wait(1)
        self.play(FadeOut(T, shift = LEFT * 3), FadeOut(f, shift = RIGHT * 3))
        self.wait(0.8)


class PendulumScene(Scene):
    def construct(self):
        vt = ValueTracker(1)
        pnd_origin = UP + RIGHT * 3
        omega = 4
        theta0 = PI / 10
        l = 4
        R = 0.2
        pnd = VGroup()
        line = always_redraw(
            lambda : Line(pnd_origin, pnd_origin + DOWN * l * cos(theta0 * sin(omega* vt.get_value())) + RIGHT * l * sin(theta0 * sin(omega* vt.get_value())))
        )
        pnd.add(line)
        mass = always_redraw(
            lambda : Circle(R, YELLOW, fill_opacity = 1).move_to(pnd_origin + DOWN * l * cos(theta0 * sin(omega* vt.get_value())) + RIGHT * l * sin(theta0 * sin(omega* vt.get_value()))).set_fill(YELLOW)
        ) 
        pnd.add(mass)

        vertical_line = always_redraw(
            lambda : Line(pnd_origin, pnd_origin + DOWN * l).set_stroke(width = 1, opacity = 0.6)
        )
        pnd.add(vertical_line)

        angle = always_redraw (
            lambda : Angle(vertical_line , line, 1.5, other_angle = sin(omega* vt.get_value()) < 0).set_color(RED)
        )
        pnd.add(angle)
        
        # pnd_origin += UP

        spring_mass = VGroup()

        r_i = 0.03
        r_e = 0.4
        mass_spring_omega = 4
        mass_spring_amp = 0.5
        graph = always_redraw(lambda : 
        ParametricFunction(lambda u : np.array([(r_i * u + r_e / 2 * -cos(u)) * (1 + mass_spring_amp / (r_i * (10 * 2 * PI + PI) + r_e * -cos(10 * 2 * PI + PI)) * sin(mass_spring_omega * vt.get_value()))  , r_i + r_e * sin(u), 0]),
        color = BLUE, t_range = [0, 10 * 2 * PI + PI]).shift(LEFT * (4 + (r_i * (10 * 2 * PI + PI) + r_e / 2 * -cos(10 * 2 * PI + PI)) * (mass_spring_amp / (r_i * (10 * 2 * PI + PI) + r_e * -cos(10 * 2 * PI + PI)) * sin(mass_spring_omega * vt.get_value()))))
        )
        spring_mass.add(graph)
        
        end_line = always_redraw(
            lambda : Line(graph.get_end(), graph.get_end() + RIGHT * 0.2)
        )
        start_line = always_redraw(
            lambda : Line(graph.get_start(), graph.get_start() + LEFT * 0.2)
        )
        s_mass = always_redraw(
            lambda : Square(0.8).next_to(start_line, LEFT, buff = 0).set_fill(YELLOW, 1)
        )
        wall_line = Line(end_line.get_end() + DOWN * 0.4, end_line.get_end() + UP * 0.4)

        spring_mass.add(end_line, start_line, s_mass, wall_line)

        self.add(spring_mass)
        self.play(Create(pnd))
        self.wait(1)
        self.play(vt.animate.set_value(10),rate_func = linear, run_time = 10)
        self.wait()



class Scene2(Scene):
    def construct(self):
        vt = ValueTracker(0)
        
        c1 = Circle(1.6, RED).shift(2.5 * LEFT + 0.5 * UP)
        c2 = Circle(1.6, BLUE).shift(2.5 * RIGHT + 0.5 * UP)

        time_text =  MathTex("Time: ").shift(UP * 2.8 + LEFT * 0.5)
        t_value_text = always_redraw(
            lambda: MathTex('%.1f'%vt.get_value() + "s").next_to(time_text, RIGHT, buff=0.1)
        )

        t1 = 2
        t2 = 4
        
        t_value_text1 = MathTex(str(t1) + ".0s").next_to(time_text, RIGHT, buff=0.1)
        t_value_text2 = MathTex(str(t2) + ".0s").next_to(time_text, RIGHT, buff=0.1)

        car1 = always_redraw(
            lambda : SVGMobject("car.svg")
            .set_color(RED_A)
            .set(width=0.3)
            .scale(4)
            .next_to(c1, UP, 0)
            .rotate(0 if (vt.get_value() / t2) > 1 else vt.get_value() * 2 * PI / t2, about_point = c1.get_center())
        )

        car2 = always_redraw(
            lambda : SVGMobject("car.svg")
            .set_color(BLUE_A)
            .set(width=0.3)
            .scale(4)
            .next_to(c2, UP, 0)
            .rotate(0 if (vt.get_value() / t1) > 1 else vt.get_value() * 2 * PI / t1, about_point= c2.get_center())
        )        

        T1_text = MathTex("T = ").next_to(c1, DOWN, 1).shift(0.2 * LEFT).set_color(RED_A)
        T2_text = MathTex("T = ").next_to(c2, DOWN, 1).shift(0.2 * LEFT).set_color(BLUE_A)
 
        T1_value = MathTex(str(t2) + "s").next_to(T1_text, RIGHT, buff = 0.1).set_color(RED_A)
        T2_value = MathTex(str(t1) + "s").next_to(T2_text, RIGHT, buff = 0.1).set_color(BLUE_A)
        event_image = ImageMobject("event-image.png").scale(0.2).shift(LEFT * 6.25 + DOWN * 3.1)
        self.add(event_image)
        self.play(Create(time_text), Create(t_value_text), run_time = 0.5)
        self.wait(0.5)
        self.play(Create(c1), Create(car1), run_time = 1.4)
        self.play(Write(T1_text), run_time = 0.4)
        self.wait(0.5)
        self.play(Create(c2), Create(car2), run_time = 1.4)
        self.play(Write(T2_text), run_time = 0.4)
        self.wait(5.1)

        self.play(vt.animate.set_value(t1), rate_func = linear, run_time = t1)
        self.add(t_value_text1)
        self.play(Transform(t_value_text1, T2_value), run_time = 1)
        self.wait(0.2)
        self.play(vt.animate.set_value(t2), rate_func = linear, run_time = t2 - t1)
        self.wait()
        self.add(t_value_text2)
        self.play(Transform(t_value_text2, T1_value), run_time = 1)
        self.wait(1.3)
        self.play(FadeOut(time_text), FadeOut(t_value_text))
        self.play(FadeOut(car1), FadeOut(c1), FadeOut(T1_text), FadeOut(t_value_text2), run_time = 0.25)
        self.play(FadeOut(car2), FadeOut(c2), FadeOut(T2_text), FadeOut(t_value_text1), run_time = 0.25)
        self.wait(1)

class SceneF(Scene):
    def construct(self):
        f = MathTex("f").scale(9)
        event_image = ImageMobject("event-image.png").scale(0.2).shift(LEFT * 6.25 + DOWN * 3.1)
        self.add(event_image)

        self.play(Write(f), run_time = 1.5)
        self.wait(3.5)
        self.play(FadeOut(f), run_time = 0.5)
        self.wait(1)



class Scene3NEW(Scene):
    def construct(self):
        c1 = Circle(2, RED).shift(2 * RIGHT)
        vt = ValueTracker(0.00001)
        time_text =  MathTex("Time: ").scale(1.5).shift(LEFT * 4.5 + UP * 2.5)
        t_value_text = always_redraw(
            lambda: MathTex('%.1f'%vt.get_value()+"s").scale(1.5).next_to(time_text, RIGHT, buff=0.1)
        )
        
        t1 = 3
   
        t_value_text1 = MathTex(str(1) + ".0s").scale(1.5).next_to(time_text, RIGHT, buff=0.1).set_color(RED_A)
        

        car1 = always_redraw(
            lambda : SVGMobject("car.svg")
            .set_color(RED_A)
            .set(width=0.3)
            .scale(4)
            .next_to(c1, UP, 0)
            .rotate(0 if (vt.get_value() / t1) > 1 else vt.get_value() * 2 * PI / t1, about_point = c1.get_center())
        )
     
        c1_lines = VGroup()
       
        for i in range(t1):
            c1_lines.add(Line(c1.get_center(), c1.get_center() + 2 * (LEFT * sin(2 * i * PI / t1) + UP * cos(2 * i * PI / t1))).set_color(RED_A))

        F1_value = MathTex("\\frac{1}{3}").move_to(c1.get_center()).shift(0.8 * (LEFT * sin(PI / t1) + UP * cos(PI / t1))).set_color(RED_A).shift(UP * 0.1)
       
        F1_text = MathTex("f = ").next_to(c1, DOWN, 1).set_color(RED_A)
       
        F1_value_in_place = MathTex("\\frac{\\frac{1}{3}}{1s}").next_to(F1_text, RIGHT, buff = 0.2).set_color(RED_A)
        divison_line1 = Line(F1_text.get_right(), F1_text.get_right() + 0.5 * RIGHT).shift(0.1 * RIGHT).set_color(RED_A)
       
        F1_final_value = MathTex("\\frac{1}{3}\\frac{1}{s}").move_to(F1_value_in_place.get_center()).set_color(RED_A)
    
        self.play(Create(time_text), Create(t_value_text), run_time = 1)
        self.wait(0.3)
        self.play(Create(c1), run_time = 1)
        self.wait(0.2)
        self.play(Create(car1), run_time = 1)
        self.wait(0.2)
        self.play(Create(F1_text),run_time = 0.3)
        self.wait(2)

        self.play(vt.animate.set_value(1), rate_func = linear, run_time = 1.3)
        self.wait(0.6)
        self.play(Create(c1_lines), run_time = 1)
        self.wait(0.5)
        self.play(Create(F1_value), run_time = 0.3)
        self.wait(1.4)
        self.add(t_value_text1)
        self.play(Create(divison_line1), 
                  F1_value.animate.move_to(divison_line1.get_center() + 0.3 * UP), t_value_text1.animate.move_to(divison_line1.get_center() + 0.3 * DOWN)
                 , run_time = 1)
        self.play(F1_value.animate.scale(0.5), t_value_text1.animate.scale(0.3333), run_time = 0.6)
        self.wait(1)        
        
        self.play(Transform(F1_value, F1_final_value), Transform(t_value_text1, F1_final_value), Transform(divison_line1, F1_final_value)
                 , run_time = 0.7)
        self.wait(4.5)
        self.play(FadeOut(time_text), FadeOut(t_value_text), run_time = 0.5)
        self.play(FadeOut(c1_lines), FadeOut(F1_text), FadeOut(car1), FadeOut(c1), FadeOut(t_value_text1), FadeOut(F1_value),FadeOut(divison_line1), run_time = 0.5)
        self.wait(0.5)

class SumSineScene(Scene):
    def construct(self):

        axes1 = Axes(x_range=[0, 6*PI + 0.0001, PI + 0.001], y_range=[-1.2, 1.2, 4], x_length= 3.5*PI, y_length= 2.4, y_axis_config = {"include_tip" : False}).scale(0.8).to_edge(LEFT, buff = 1.5).shift(UP * 3)
        axes2 = Axes(x_range=[0, 6*PI + 0.0001, PI + 0.001], y_range=[-1.2, 1.2, 4], x_length= 3.5*PI, y_length= 2.4, y_axis_config = {"include_tip" : False}).scale(0.8).next_to(axes1, DOWN, 0.4)
        axes3 = Axes(x_range=[0, 6*PI + 0.0001, PI + 0.001], y_range=[-2.1, 2.1, 4], x_length= 3.5*PI, y_length= 4.2, y_axis_config = {"include_tip" : False}).scale(0.8).next_to(axes2, DOWN, 0.4)
        
        A_text = MathTex("A").scale(1.5).next_to(axes1, RIGHT, 1.4)
        A_text1 = MathTex("A").scale(1.5).next_to(axes1, RIGHT, 1.4)
        B_text = MathTex("B").scale(1.5).next_to(axes2, RIGHT, 1.4)
        B_text1 = MathTex("B").scale(1.5).next_to(axes2, RIGHT, 1.4)
        AB_text = MathTex("A+B").scale(1.5).next_to(axes3, RIGHT, 0.74)

        graph1 = axes1.get_graph(lambda x : np.sin(x), color = BLUE, x_range = [0, 6 * PI])
        graph11 = axes1.get_graph(lambda x : np.sin(x), color = BLUE, x_range = [0, 6 * PI])
        graph2 = axes2.get_graph(lambda x : np.sin(1.5 * x), color = RED, x_range = [0, 6 * PI])
        graph21 = axes2.get_graph(lambda x : np.sin(1.5 * x), color = RED, x_range = [0, 6 * PI])
        graph3 = axes3.get_graph(lambda x : np.sin(x) + np.sin(1.5 * x), color = MAROON, x_range = [0, 6 * PI])


        # self.play(Zoo)
        self.wait(3.7)
        self.play(Create(axes1), Create(axes2), Create(axes3), run_time = 1)
        self.wait(1.4)
        self.play(Create(graph1), Create(graph11), Create(A_text), Create(A_text1), run_time = 1)
        self.wait(2.2)
        self.play(Create(graph2), Create(graph21), Create(B_text), Create(B_text1), run_time = 1)          
        self.wait(5.5)
        self.play(Transform(graph1, graph3), Transform(graph2, graph3), Transform(A_text1, AB_text), Transform(B_text1, AB_text))    
        self.wait(5.8)    

class FourierScene(Scene):
    def construct(self):
        t = ValueTracker(0.0001)        
        
        omega0 = -1
        amp_muliplier = 2
        origin = LEFT * 4
        fourier_circles = VGroup()
        fourier_circles.get_family()
        c1 = always_redraw( 
            lambda : Circle(amp_muliplier * sawtooth_amp(1), RED).move_to(origin).set_opacity(0.5).set_fill(BLACK, 0)
        )
        l1 = always_redraw(
            lambda : Line(origin, origin + c1.get_radius() * (RIGHT * cos(omega0 * t.get_value()) + UP * sin(omega0 * t.get_value())))
        )
        # c2 = always_redraw(
        #     lambda : Circle(amp_muliplier * sawtooth_amp(2), RED).move_to(l1.get_end()).set_opacity(0.5).set_fill(BLACK, 0)
        # )
        # l2 = always_redraw(
        #     lambda : Line(c2.get_center(), c2.get_center() + c2.get_radius() * (RIGHT * cos(omega0 * 3 * t.get_value()) + UP * sin(omega0 * 3 * t.get_value())))
        # ) 

        # c3 = always_redraw(
        #     lambda : Circle(amp_muliplier * sawtooth_amp(3), RED).move_to(l2.get_end()).set_opacity(0.5).set_fill(BLACK, 0)
        # )
        # l3 = always_redraw(
        #     lambda : Line(c3.get_center(), c3.get_center() + c3.get_radius() * (RIGHT * cos(omega0 * 3 * t.get_value()) + UP * sin(omega0 * 3 * t.get_value())))
        # ) 

        # c4 = always_redraw(
        #     lambda : Circle(amp_muliplier * sawtooth_amp(4), RED, ).move_to(l3.get_end()).set_opacity(0.5).set_fill(BLACK, 0)
        # )
        # l4 = always_redraw(
        #     lambda : Line(c4.get_center(), c4.get_center() + c4.get_radius() * (RIGHT * cos(omega0 * 4 * t.get_value()) + UP * sin(omega0 * 4 * t.get_value())))
        # ) 
        


        axes =  Axes(
            x_range = [0, 2 * PI, 1],
            y_range = [-1.5, 1.5, 1],
            x_length = 8,
            y_length = 6
        ).next_to(c1.get_right(), buff = 1.5)

        graph = always_redraw(
            lambda : axes.get_graph(
            lambda x: sawtooth_amp(1) * sin((-x + t.get_value()) * omega0 * 1),
            x_range = [0, min(2 * PI, t.get_value())]
        )
        )
        connector = always_redraw(
            lambda : DashedLine(start = l1.get_end(), end = graph.get_start())
            # lambda : Line(l4.get_end(), graph.get_start())
        )
        shape = always_redraw(
            lambda : ParametricFunction(lambda u : np.array([
            2 * (sawtooth_amp(1) * cos((-u + t.get_value()) * omega0 * 1)), 
            2 * (sawtooth_amp(1) * sin((-u + t.get_value()) * omega0 * 1)),
            0]),
        color = BLUE, t_range = [0, t.get_value()]
        ).shift(LEFT * 4)
        )
        dot = always_redraw(
            lambda : Dot(l1.get_end(), radius = 0.1, color = BLUE)
        )
        fourier_circles.add(c1, l1)
        # fourier_circles
        # self.play()
        self.play(Create(axes), Create(graph))
        self.wait(0.1)
        self.play(Create(fourier_circles), Create(shape), Create(connector), Create(dot)) 
        self.wait(0.1)
        # self.play()
        self.play(t.animate.set_value(10), rate_func = linear,run_time = 10)
        self.wait(1)



def sawtooth_amp(n):
    return -2 * pow(-1, n) / (PI * n)

def sawtooth(x,t,n, omega0):
    res = 0
    for i in range(n):
        res += sawtooth_amp(i + 1) * sin((-x + t) * omega0 * (i + 1))
    
    return res    

def sawtooth_cos(x,t,n, omega0):
    res = 0
    for i in range(n):
        res += sawtooth_amp(i + 1) * cos((-x + t) * omega0 * (i + 1))

    return res 