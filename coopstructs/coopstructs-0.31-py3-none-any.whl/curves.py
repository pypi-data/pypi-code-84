from enum import Enum
from abc import ABC, abstractmethod
from coopstructs.vectors import Vector2
import math
from typing import List, Callable, Dict
from coopstructs.toggles import EnumToggleable
from coopstructs.geometry import Rectangle, Line
import numpy as np

class Orientation(Enum):
    UP_LEFT = 3
    UP_RIGHT = 4
    RIGHT_UP = 5
    RIGHT_DOWN = 6
    DOWN_RIGHT = 7
    DOWN_LEFT = 8
    LEFT_DOWN = 9
    LEFT_UP = 10
    UP = 11
    RIGHT = 12
    DOWN = 13
    LEFT = 14


class Curve(ABC):
    @classmethod
    @abstractmethod
    def from_points(cls, points: List[Vector2], naming_provider: Callable[[], str]) -> (List, List):
        pass

    def __init__(self, id: str, origin: Vector2):
        self.origin = origin
        self.id = id

    def __str__(self):
        return f"{type(self)} starting at {self.origin} and terminating at {self.end_point()} [{self.id}]"

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def _end_point(self):
        raise NotImplementedError()

    @property
    def end_point(self):
        return self.end_point()

    @property
    def control_points(self) -> List[Vector2]:
        return self._control_points()

    @abstractmethod
    def _control_points(self) -> List[Vector2]:
        raise NotImplementedError()

    @abstractmethod
    def line_representation(self) -> List[Line]:
        pass

    @abstractmethod
    def force_continuity(self, next_point: Vector2) -> Vector2:
        pass

    @classmethod
    def orientation(cls, origin, destination) -> List[Orientation]:
        orientation = None
        if origin.x == destination.x and origin.y > destination.y:
            orientation = [Orientation.UP]
        elif origin.x == destination.x and origin.y < destination.y:
            orientation = [Orientation.DOWN]
        elif origin.x < destination.x and origin.y == destination.y:
            orientation = [Orientation.RIGHT]
        elif origin.x > destination.x and origin.y == destination.y:
            orientation = [Orientation.LEFT]
        elif origin.x > destination.x and origin.y > destination.y:
            orientation = [Orientation.UP_LEFT, Orientation.LEFT_UP]
        elif origin.x > destination.x and origin.y < destination.y:
            orientation = [Orientation.DOWN_LEFT, Orientation.LEFT_DOWN]
        elif origin.x < destination.x and origin.y > destination.y:
            orientation = [Orientation.UP_RIGHT, Orientation.RIGHT_UP]
        elif origin.x < destination.x and origin.y < destination.y:
            orientation = [Orientation.DOWN_RIGHT, Orientation.RIGHT_DOWN]
        return orientation


class Arc(Curve):

    @classmethod
    def from_points(cls, points: List[Vector2], naming_provider: Callable[[], str]) -> (List, List):
        curves = []
        for ii in range(len(points) - 1):
            orientation = cls.orientation(points[ii], points[ii + 1])[0]
            if orientation in (Orientation.UP, Orientation.RIGHT, Orientation.DOWN, Orientation.LEFT):
                curves.append(LineCurve(naming_provider(), points[ii], points[ii + 1]))
            else:
                curves.append(Arc(naming_provider(), orientation, points[ii],
                                  Vector2(abs(points[ii + 1].x - points[ii].x) * 2,
                                          abs(points[ii + 1].y - points[ii].y) * 2))
                              )
        return curves, []

    @classmethod
    def from_arcbox(cls, id:str, orientation: Orientation, origin: Vector2, arc_box_size: Vector2):
        return Arc(id, orientation, origin, arc_box_size)

    @classmethod
    def from_origin_and_destination(cls, id:str, orientation: Orientation, origin: Vector2, destination: Vector2):
        return Arc(id, orientation, origin, Vector2(destination.x - origin.x, destination.y - origin.y) * 2)

    def __init__(self, id:str, orientation: Orientation, origin: Vector2, arc_box_size: Vector2):
        super().__init__(id, origin)
        self.orientation = orientation
        self.arc_box_size = arc_box_size
        self.arc_rad_start = None
        self.arc_rad_end = None
        self.define_arc_radian_start_end()
        self._arc_box = self.arc_box()
        self.mid_point = Vector2(self._arc_box[0] + self._arc_box[2] / 2.0, self._arc_box[1] + self._arc_box[3] / 2.0)

    def _control_points(self) -> List[Vector2]:
        return [self.origin, self.end_point]

    def line_representation(self):
        return self.compute_curve_lines()

    def define_arc_radian_start_end(self):
        if self.orientation == Orientation.DOWN_LEFT:
            self.arc_rad_start = 2 * math.pi
            self.arc_rad_end = 3 * math.pi / 2
        elif self.orientation == Orientation.DOWN_RIGHT:
            self.arc_rad_start = math.pi
            self.arc_rad_end = 3 * math.pi / 2
        elif self.orientation == Orientation.LEFT_DOWN:
            self.arc_rad_start = math.pi / 2
            self.arc_rad_end = math.pi
        elif self.orientation == Orientation.LEFT_UP:
            self.arc_rad_start = 3 * math.pi / 2
            self.arc_rad_end = math.pi
        elif self.orientation == Orientation.UP_LEFT:
            self.arc_rad_start = 0
            self.arc_rad_end = math.pi / 2
        elif self.orientation == Orientation.UP_RIGHT:
            self.arc_rad_start = math.pi
            self.arc_rad_end = math.pi / 2
        elif self.orientation == Orientation.RIGHT_DOWN:
            self.arc_rad_start = math.pi / 2
            self.arc_rad_end = 0
        elif self.orientation == Orientation.RIGHT_UP:
            self.arc_rad_start = 3 * math.pi / 2
            self.arc_rad_end = 2 * math.pi
        else:
            raise Exception(f"Invalid curve orientation: [{self.orientation}]")

    def _end_point(self):
        if self.orientation in (Orientation.DOWN_LEFT,  Orientation.LEFT_DOWN):
            return Vector2(int(self.origin.x - self.arc_box_size.x / 2), int(self.origin.y + self.arc_box_size.y / 2))
        elif self.orientation in (Orientation.LEFT_UP, Orientation.UP_LEFT):
            return Vector2(int(self.origin.x - self.arc_box_size.x / 2), int(self.origin.y - self.arc_box_size.y / 2))
        elif self.orientation in (Orientation.UP_RIGHT, Orientation.RIGHT_UP):
            return Vector2(int(self.origin.x + self.arc_box_size.x / 2), int(self.origin.y - self.arc_box_size.y / 2))
        elif self.orientation in (Orientation.RIGHT_DOWN, Orientation.DOWN_RIGHT):
            return Vector2(int(self.origin.x + self.arc_box_size.x / 2), int(self.origin.y + self.arc_box_size.y / 2))
        else:
            raise Exception("Incorrect Curve type with orientation")

    def compute_curve_lines(self) -> List[Line]:
        b_points = self.compute_curve_points()
        if b_points is None:
            return None

        ret = []
        for ii in range(0, len(b_points)):
            if ii == 0:
                continue
            else:
                start = Vector2(b_points[ii - 1].x, b_points[ii - 1].y)
                end = Vector2(b_points[ii].x, b_points[ii].y)
                ret.append(Line(start, end))
        return ret

    def compute_curve_points(self, numPoints=None) -> List[Vector2]:
        if numPoints is None:
            numPoints = 30
        if numPoints < 2:
            return None

        ret = []
        increment = (self.arc_rad_end - self.arc_rad_start) / (numPoints - 1)
        for ii in range(0, numPoints):
            next = self.point_along_arc(self.arc_rad_start + increment * ii, self.mid_point, self.arc_box_as_rectangle())
            ret.append(next)

        return ret

    def arc_box_as_rectangle(self) -> Rectangle:
        return Rectangle(x=self._arc_box[0], y=self._arc_box[1], width=self._arc_box[2], height=self._arc_box[3])

    def point_along_arc(self, radians: float, rotation_point: Vector2, arc_box: Rectangle):
        a = arc_box.width / 2
        b = arc_box.height / 2

        x = a * math.cos(radians)
        y = - b * math.sin(radians)

        return Vector2(int(x), int(y)) + rotation_point

    def arc_box(self):
        if self.orientation == Orientation.DOWN_LEFT:
            return [self.origin.x - self.arc_box_size.x, self.origin.y - self.arc_box_size.y / 2,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.orientation == Orientation.DOWN_RIGHT:
            return [self.origin.x, self.origin.y - self.arc_box_size.y / 2,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.orientation == Orientation.LEFT_DOWN:
            return [self.origin.x - self.arc_box_size.x / 2, self.origin.y,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.orientation == Orientation.LEFT_UP:
            return [self.origin.x - self.arc_box_size.x / 2, self.origin.y - self.arc_box_size.y,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.orientation == Orientation.UP_LEFT:
            return [self.origin.x - self.arc_box_size.x, self.origin.y - self.arc_box_size.y / 2,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.orientation == Orientation.UP_RIGHT:
            return [self.origin.x, self.origin.y - self.arc_box_size.y / 2,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.orientation == Orientation.RIGHT_UP:
            return [self.origin.x - self.arc_box_size.x / 2, self.origin.y - self.arc_box_size.y,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.orientation == Orientation.RIGHT_DOWN:
            return [self.origin.x - self.arc_box_size.x / 2, self.origin.y,
                    self.arc_box_size.x, self.arc_box_size.y]
        else:
            raise Exception("Incorrect Curve type with orientation")

    def length(self):
        return (self.arc_rad_end - self.arc_rad_start) * (self.origin - self.mid_point).length()

    def force_continuity(self, next_point: Vector2) -> Vector2:
        end_point = self.end_point()
        if self.orientation in (Orientation.UP_LEFT, Orientation.DOWN_LEFT) and next_point.x > end_point.x:
            return Vector2(end_point.x, next_point.y)
        elif self.orientation in (Orientation.UP_RIGHT, Orientation.DOWN_RIGHT) and next_point.x < end_point.x:
            return Vector2(end_point.x, next_point.y)
        elif self.orientation in (Orientation.RIGHT_UP, Orientation.LEFT_UP) and next_point.y > end_point.y:
            return Vector2(next_point.x, end_point.y)
        elif self.orientation in (Orientation.RIGHT_DOWN, Orientation.LEFT_DOWN) and next_point.y < end_point.y:
            return Vector2(next_point.x, end_point.y)
        else:
            return next_point



class LineCurve(Curve):
    @classmethod
    def from_points(self, points, naming_provider: Callable [[], str]) -> (List, List):
        lines = []
        for ii in range(len(points) - 1):
            lines.append(LineCurve(naming_provider(), points[ii], points[ii + 1]))
        return lines, []

    def __init__(self, id:str, origin: Vector2, destination: Vector2):
        super().__init__(id, origin)
        self.destination = destination
        self.length = self.length()

    def _control_points(self) -> List[Vector2]:
        return [self.origin, self.end_point]

    def line_representation(self):
        return [Line(self.origin, self.destination)]

    def _end_point(self):
        return self.destination

    def length(self):
        return Line(self.origin, self.destination).length()

    def force_continuity(self, next_point: Vector2) -> Vector2:
        return next_point

class CubicBezier(Curve):
    @classmethod
    def from_points(cls, points: List[Vector2], naming_provider: Callable [[], str]) -> (List, List):
        leftover_points = []
        leftover_count = (len(points) - 1) % 3 if len(points) >= 4 else len(points)
        leftover_points = points[-leftover_count:] if leftover_count != 0 else leftover_points
        used_points = points[:-leftover_count] if leftover_count != 0 else points

        curves = []

        if len(points) < 4:
            return curves, points

        # A Cubic Bezier requires 4 control points, so operate in blocks of 4 (re-using the last each time)
        for ii in range(0, len(used_points) - 3, 3):
            curves.append(CubicBezier(naming_provider(), points[ii:ii+4]))

        return curves, leftover_points

    def __init__(self, id:str, control_points: List[Vector2]):
        Curve.__init__(self, id, control_points[0])
        self._cps = control_points

    def line_representation(self):
        return self.compute_curve_lines()

    def _control_points(self) -> List[Vector2]:
        return self._cps

    def _end_point(self):
        return self.control_points[-1]

    def compute_curve_lines(self):
        b_points = self.compute_bezier_points([(x.x, x.y) for x in self.control_points])
        ret = []
        for ii in range(0, len(b_points)):
            if ii == 0:
                continue
            else:
                start = Vector2(b_points[ii - 1][0], b_points[ii - 1][1])
                end = Vector2(b_points[ii][0], b_points[ii][1])
                ret.append(LineCurve(self.id + f"_{ii}", start, end))
        return ret

    def compute_bezier_points(self, vertices, numPoints=None):
        if numPoints is None:
            numPoints = 30
        if numPoints < 2 or len(vertices) != 4:
            return []

        result = []

        b0x = vertices[0][0]
        b0y = vertices[0][1]
        b1x = vertices[1][0]
        b1y = vertices[1][1]
        b2x = vertices[2][0]
        b2y = vertices[2][1]
        b3x = vertices[3][0]
        b3y = vertices[3][1]

        # Compute polynomial coefficients from Bezier points
        ax = -b0x + 3 * b1x + -3 * b2x + b3x
        ay = -b0y + 3 * b1y + -3 * b2y + b3y

        bx = 3 * b0x + -6 * b1x + 3 * b2x
        by = 3 * b0y + -6 * b1y + 3 * b2y

        cx = -3 * b0x + 3 * b1x
        cy = -3 * b0y + 3 * b1y

        dx = b0x
        dy = b0y

        # Set up the number of steps and step size
        numSteps = numPoints - 1  # arbitrary choice
        h = 1.0 / numSteps  # compute our step size

        # Compute forward differences from Bezier points and "h"
        pointX = dx
        pointY = dy

        firstFDX = ax * (h * h * h) + bx * (h * h) + cx * h
        firstFDY = ay * (h * h * h) + by * (h * h) + cy * h

        secondFDX = 6 * ax * (h * h * h) + 2 * bx * (h * h)
        secondFDY = 6 * ay * (h * h * h) + 2 * by * (h * h)

        thirdFDX = 6 * ax * (h * h * h)
        thirdFDY = 6 * ay * (h * h * h)

        # Compute points at each step
        result.append((int(pointX), int(pointY)))

        for i in range(numSteps):
            pointX += firstFDX
            pointY += firstFDY

            firstFDX += secondFDX
            firstFDY += secondFDY

            secondFDX += thirdFDX
            secondFDY += thirdFDY

            result.append((int(pointX), int(pointY)))

        return result


    def force_continuity(self, next_point: Vector2) -> Vector2:
        return next_point.project_onto(self.control_points[-1], self.control_points[-2])

# class EasyInputCubicBezier(CubicBezier):
#     def __init__(self, id:str, control_points: List[Vector2]):
#         super().__init__()



class CatmullRom(Curve):

    @classmethod
    def from_points(cls, points: List[Vector2], naming_provider: Callable[[], str]) -> (List, List):
        leftover_points = []
        leftover_count = len(points) if len(points) < 4 else 0
        leftover_points = points if leftover_count != 0 else leftover_points
        used_points = points if leftover_count == 0 else []

        curves = []

        if len(used_points) < 4:
            return [], points

        # A Cubic Bezier requires 4 control points, so operate in blocks of 3 (re-using the last each time)
        curves.append(CatmullRom(naming_provider(), points))
        return curves, leftover_points


    def __init__(self, id:str, control_points: List[Vector2]):
        Curve.__init__(self, id, control_points[0])

        if len(control_points) < 4:
            raise ValueError(f"Invalid input for control points. Must have at least 4 values but list of length {len(control_points)} was provided: [{control_points}]")
        self._cps = control_points

    def _control_points(self) -> List[Vector2]:
        return self._cps

    def line_representation(self):
        return self.compute_curve_lines()

    def _end_point(self):
        return self.control_points[-1]

    def compute_curve_lines(self):
        b_points = self.compute_catmull_points([(x.x, x.y) for x in self.control_points])
        ret = []
        for ii in range(0, len(b_points)):
            if ii == 0:
                continue
            else:
                start = Vector2(b_points[ii - 1][0], b_points[ii - 1][1])
                end = Vector2(b_points[ii][0], b_points[ii][1])
                ret.append(Line(start, end))
        return ret

    def compute_catmull_points(self, vertices, numPoints=None):
        if numPoints is None:
            numPoints = 30
        if numPoints < 2 or len(vertices) < 4:
            return []

        ##### MODIFIED FROM: https://en.wikipedia.org/wiki/Centripetal_Catmull%E2%80%93Rom_spline

        # The curve c will contain an array of (x, y) points.
        c = []
        for ii in range(len(vertices) - 3):
            # Convert the points to numpy so that we can do array multiplication
            # P0, P1, P2, P3 = map(np.array, [(self.control_points[ii].x, self.control_points[ii].y),
            #                                 (self.control_points[ii + 1].x, self.control_points[ii + 1].y),
            #                                 (self.control_points[ii + 2].x, self.control_points[ii + 2].y),
            #                                 (self.control_points[ii + 3].x, self.control_points[ii + 3].y)])
            P0, P1, P2, P3 = map(np.array, [vertices[ii], vertices[ii + 1], vertices[ii + 2], vertices[ii + 3]])

            # Parametric constant: 0.5 for the centripetal spline, 0.0 for the uniform spline, 1.0 for the chordal spline.
            alpha = 0.5
            # Premultiplied power constant for the following tj() function.
            alpha = alpha / 2

            def tj(ti, Pi, Pj):
                xi, yi = Pi
                xj, yj = Pj
                return ((xj - xi) ** 2 + (yj - yi) ** 2) ** alpha + ti

            # Calculate t0 to t4
            t0 = 0
            t1 = tj(t0, P0, P1)
            t2 = tj(t1, P1, P2)
            t3 = tj(t2, P2, P3)

            # Only calculate points between P1 and P2
            t = np.linspace(t1, t2, numPoints)

            # Reshape so that we can multiply by the points P0 to P3
            # and get a point for each value of t.
            t = t.reshape(len(t), 1)
            # print(t)
            A1 = (t1 - t) / (t1 - t0) * P0 + (t - t0) / (t1 - t0) * P1
            A2 = (t2 - t) / (t2 - t1) * P1 + (t - t1) / (t2 - t1) * P2
            A3 = (t3 - t) / (t3 - t2) * P2 + (t - t2) / (t3 - t2) * P3
            # print(A1)
            # print(A2)
            # print(A3)
            B1 = (t2 - t) / (t2 - t0) * A1 + (t - t0) / (t2 - t0) * A2
            B2 = (t3 - t) / (t3 - t1) * A2 + (t - t1) / (t3 - t1) * A3

            C = (t2 - t) / (t2 - t1) * B1 + (t - t1) / (t2 - t1) * B2

            c.extend(C)


        return [Vector2(point[0], point[1]) for point in c]


    def force_continuity(self, next_point: Vector2) -> Vector2:
        return next_point

class CurveType(Enum):
    ARC = 1,
    CUBICBEZIER = 2,
    LINE = 3,
    CATMULLROM = 4

class CurveBuilder:

    def __init__(self, id_provider: Callable [[], str]):
        self.curves = {} # {id: curve}
        self.current_points = []
        self.current_curve_type = EnumToggleable(CurveType)
        self.current_orientation = EnumToggleable(Orientation)
        self.id_provider = id_provider

    def add_curves(self, curves: Dict[str, Curve]):
        self.curves = {**self.curves, **curves}

    def set_curve_type(self, curve_type: CurveType):
        self.current_curve_type.set_value(curve_type)

    def toggle_curve_type(self):
        self.current_curve_type.toggle()
        self.current_points = []

    def save_curve(self):
        new_curves, _ = self.curves_from_points(self.current_curve_type.value, self.current_points)
        for curve in new_curves:
            self.curves[self.id_provider()] = curve
        self.current_points = []

    def add_point(self, point: Vector2):
        self.current_points.append(point)

    def remove_point(self):
        if any(self.current_points):
            self.current_points.pop()

    # def orientation(self, origin, destination) -> List[Orientation]:
    #     orientation = None
    #     if origin.x == destination.x and origin.y > destination.y:
    #         orientation = [Orientation.UP]
    #     elif origin.x == destination.x and origin.y < destination.y:
    #         orientation = [Orientation.DOWN]
    #     elif origin.x < destination.x and origin.y == destination.y:
    #         orientation = [Orientation.RIGHT]
    #     elif origin.x > destination.x and origin.y == destination.y:
    #         orientation = [Orientation.LEFT]
    #     elif origin.x > destination.x and origin.y > destination.y:
    #         orientation = [Orientation.UP_LEFT, Orientation.LEFT_UP]
    #     elif origin.x > destination.x and origin.y < destination.y:
    #         orientation = [Orientation.DOWN_LEFT, Orientation.LEFT_DOWN]
    #     elif origin.x < destination.x and origin.y > destination.y:
    #         orientation = [Orientation.UP_RIGHT, Orientation.RIGHT_UP]
    #     elif origin.x < destination.x and origin.y < destination.y:
    #         orientation = [Orientation.DOWN_RIGHT, Orientation.RIGHT_DOWN]
    #     return orientation

    def curves_from_points(self, curve_type: CurveType, points: List[Vector2]) -> (List[Curve], List[Vector2]):
        # curves = []
        # leftover_points = []
        if len(points) <2:
            return [], points

        if curve_type == CurveType.LINE:
            # curves = self.lines_from_points(points)
            curves, leftover_points = LineCurve.from_points(points, self.id_provider)
        elif curve_type == CurveType.ARC:
            # curves = self.arcs_from_points(points)
            curves, leftover_points = Arc.from_points(points, self.id_provider)
        elif curve_type == CurveType.CUBICBEZIER:
            # leftover_count = (len(points) - 1) % 3 if len(points) >= 4 else len(points)
            # leftover_points = points[-leftover_count:] if leftover_count != 0 else leftover_points
            # used_points = points[:-leftover_count] if leftover_count != 0 else points
            # curves = self.cubicbeziers_from_points(used_points)
            curves, leftover_points = CubicBezier.from_points(points, self.id_provider)
        elif curve_type == CurveType.CATMULLROM:
            # leftover_count = len(points) if len(points) < 4 else 0
            # leftover_points = points if leftover_count != 0 else leftover_points
            # used_points = points if leftover_count == 0 else []
            # curves = self.catmullrom_from_points(used_points)
            curves, leftover_points = CatmullRom.from_points(points, self.id_provider)
        else:
            raise NotImplementedError(f"Curve type {curve_type} has not been implemented for generation from points")

        return curves, leftover_points

    # def lines_from_points(self, points):
    #     lines = []
    #     for ii in range(len(points) - 1):
    #         lines.append(LineCurve(self.id_provider(), points[ii], points[ii + 1]))
    #     return lines
    #
    # def arcs_from_points(self, points):
    #     curves = []
    #     for ii in range(len(points) - 1):
    #         orientation = self.orientation(points[ii], points[ii + 1])[0]
    #         if orientation in (Orientation.UP, Orientation.RIGHT, Orientation.DOWN, Orientation.LEFT):
    #             curves.append(LineCurve(self.id_provider(), points[ii], points[ii + 1]))
    #         else:
    #             curves.append(Arc(self.id_provider(), orientation, points[ii],
    #                         Vector2(abs(points[ii + 1].x - points[ii].x) * 2, abs(points[ii + 1].y - points[ii].y) * 2))
    #                           )
    #     return curves

    # def cubicbeziers_from_points(self, points):
    #     curves = []
    #
    #     if len(points) < 4:
    #         return curves
    #
    #     # A Cubic Bezier requires 4 control points, so operate in blocks of 4 (re-using the last each time)
    #     for ii in range(0, len(points) - 3, 3):
    #         curves.append(CubicBezier(self.id_provider(), points[ii:ii+4]))
    #
    #     # curves.append(CubicBezier(self.id_provider(), points))
    #     return curves

    # def catmullrom_from_points(self, points):
    #     curves = []
    #
    #     if len(points) < 4:
    #         return curves
    #
    #     # A Cubic Bezier requires 4 control points, so operate in blocks of 3 (re-using the last each time)
    #     curves.append(CatmullRom(self.id_provider(), points))
    #     return curves

    def curves_from_temp_next_points(self, next_points: List[Vector2]):
        all_points = self.current_points + next_points
        points = []
        for i in all_points:
            if i not in points or i == points[0]:
                points.append(i)

        curves, leftovers = self.curves_from_points(self.current_curve_type.value, points)
        return curves

    def force_continuity(self, next_point: Vector2):
        curves, leftovers = self.curves_from_points(self.current_curve_type.value, self.current_points)

        if curves is None or len(curves) == 0:
            return next_point

        # Dont need to force a continuity if we are in the middle of a Bezier
        if self.current_curve_type.value == CurveType.CUBICBEZIER and len(leftovers) != 0:
            return next_point
        else:
            return curves[-1].force_continuity(next_point)


if __name__ == "__main__":
    import random as rnd

    builder = CurveBuilder(lambda: "1")

    points = []

    rnd.seed(0)
    for ii in range(10):
        points.append(Vector2(rnd.randint(0, 100), rnd.randint(0, 100)))

    curves, leftover = builder.curves_from_points(curve_type=CurveType.CATMULLROM, points=points)

    curve = curves[0]
    catmullpoints = curve.compute_catmull_points([(x.x, x.y) for x in curve.control_points])
    print(catmullpoints)

