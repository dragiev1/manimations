from manim import *

class BraceAnnotation(Scene):
  def construct(self):
    numberplane = NumberPlane()
    origin_text = Text('0, 0').next_to(dot, DOWN)
    tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)

    dot1 = Dot([-2, 3, 0])
    dot2 = Dot([-5, -1, 0])
    line = Line(dot1.get_center(), dot2.get_center()).set_color(PURPLE)
    b1 = Brace(line)
    b1Text = b1.get_text("Horizontal distance")
    b2 = Brace(line, direction = line.copy().rotate(PI / 2).get_unit_vector())
    b2Text = b2.get_tex("x-x_1")

    picture = VGroup(line, dot1, dot2, b1, b2, b1Text, b2Text)
    picture.move_to(ORIGIN)
    self.add(picture)


class VectorArrow(Scene):
  def construct(self):
    dot = Dot(ORIGIN)
    arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
    numberplane = NumberPlane().set_color(PURPLE)
    origin_text = Text('0, 0').next_to(dot, DOWN)
    tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
    self.add(numberplane, dot, arrow, origin_text, tip_text)


class BooleanOperations(Scene):
  def ellipse_construct(self):
      ellipse1 = Ellipse(
        width = 5.0, height = 5.0, fill_opacity = 0.5, color = BLUE, stroke_width = 10 
      ).move_to(LEFT)

      ellipse2 = ellipse1.copy().set_color(color = RED).move_to(RIGHT)
      
      bool_ops_text = MarkupText("<u>Boolean Operations</u>").next_to(ellipse1, UP * 3)

      ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)

      self.play(FadeIn(ellipse_group))

    
      i = Intersection(ellipse1, ellipse2, color = GREEN, fill_opacity=0.5)
      self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
      i_text = Text("Intersection", font_size = 23).next_to(i, UP)
      self.play(FadeIn(i_text))

      u = Union(ellipse1, ellipse2, color = ORANGE, fill_opacity = 0.5)
      u_text = Text("Union", font_size = 23)
      self.play(u.animate.scale(0.3).next_to(i, DOWN, buff = u_text.height * 3))
      u_text.next_to(u, UP)
      self.play(FadeIn(u_text))

      e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
      exclusion_text = Text("Exclusion", font_size=23)
      self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5))
      exclusion_text.next_to(e, UP)
      self.play(FadeIn(exclusion_text))

      d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
      difference_text = Text("Difference", font_size=23)
      self.play(d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5))
      difference_text.next_to(d, UP)
      self.play(FadeIn(difference_text))

  def construct(self):
    self.ellipse_construct()



class PointMovingOnShapes(Scene):
  def construct(self):
    circle = Circle(radius = 1, color = BLUE)
    dot = Dot()
    dot2 = dot.copy().shift(RIGHT)
    self.add(dot)

    line = Line([3, 0, 0], [5, 4, 0])
    self.add(line)

    self.play(GrowFromCenter(circle))
    self.play(Transform(dot, dot2))
    self.play(MoveAlongPath(dot, circle), run_time = 2, rate_func = linear)
    self.play(Rotating(dot, about_point = [2, 0, 0]), run_time=1.5)
    self.wait()