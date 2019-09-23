import math
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, Union
from core.vector2d import Vector2d

PI = 3.1416

class BaseGeometryObject:
    pass

class ShapeInteractionDetector:

    @classmethod
    def get_intersection_data(cls, first_geometry_object: BaseGeometryObject, second_geometry_object: BaseGeometryObject) -> Optional[Tuple[Vector2d, float, float]]:
        """Returns an intersection point of the lines, t and u
        
        t, u represent where an intersection point falls (first and second segment) 0.0 ≤ t, u ≤ 1.0
        """

        function_to_call = 'get_inter_data_'
        function_to_call += type(first_geometry_object).__name__.lower()
        function_to_call += "_" + type(second_geometry_object).__name__.lower()

        func = getattr(cls, function_to_call)
        return func(cls, first_geometry_object, second_geometry_object)

    @classmethod
    def get_inter_data_line_line(cls, first_line: "Line", second_line: "Line") -> Optional[Tuple[Vector2d, float, float]]:

        coefficients = cls.get_penetr_line_line_coeff(first_line, second_line)
        if not coefficients:
            return None

        intersection_point = cls.get_lines_intersect_point(first_line, coefficients)
        
        return (intersection_point, coefficients[0], coefficients[1])

    @classmethod
    def get_inter_data_line_ray(cls, line: "Line", ray: "Ray") -> Optional[Tuple[Vector2d, float, float]]:
        coefficients = cls.get_penetr_line_ray_coeff(line, ray)
        if not coefficients:
            return None

        intersection_point = cls.get_lines_intersect_point(line, coefficients)
        
        return (intersection_point, coefficients[0], coefficients[1])

    @classmethod
    def get_inter_data_ray_line(cls, ray: "Ray", line: "Line") -> Optional[Tuple[Vector2d, float, float]]:
        data = cls.get_inter_data_line_ray(line, ray)
        if not data:
            return None

        changed_coefficient_order = (data[0], data[2], data[1])
        
        return changed_coefficient_order

    @classmethod
    def get_penetr_line_line_coeff(cls, first_line: "Line", second_line: "Line") -> Optional[Tuple[float, float]]:

        coefficients = cls.get_penetr_coeff(first_line, second_line)
        if not coefficients:
            return None

        t, u = coefficients
        if t > 1 or t < 0 or u > 1 or u < 0:
            return None

        return (t, u)

    @classmethod
    def get_penetr_line_ray_coeff(cls, line: "Line", ray: "Line") -> Optional[Tuple[float, float]]:

        coefficients = cls.get_penetr_coeff(line, ray)
        if not coefficients:
            return None

        t, u = coefficients
        if t > 1 or t < 0 or u < 0:
            return None

        return (t, u)

    @staticmethod
    def get_penetr_coeff(first_line: Union["Ray", "Line"], second_line: Union["Ray", "Line"]) -> Optional[Tuple[float, float]]:
        x1 = first_line.first_point.x
        x2 = first_line.second_point.x
        y1 = first_line.first_point.y
        y2 = first_line.second_point.y

        x3 = second_line.first_point.x
        x4 = second_line.second_point.x
        y3 = second_line.first_point.y
        y4 = second_line.second_point.y

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        
        if denominator == 0:
            return None

        t_numerator = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        u_numerator = (x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)

        t = t_numerator / denominator
        u = -u_numerator / denominator
        
        return (t, u)

    @staticmethod
    def get_lines_intersect_point(line: Union["Ray", "Line"], penetration_coefficients: Tuple[float, float]) -> Vector2d:
        t, u = penetration_coefficients

        intersection_point_x = line.first_point.x + t * (line.second_point.x - line.first_point.x) 
        intersection_point_y = line.first_point.y + t * (line.second_point.y - line.first_point.y)
        intersection_point = Vector2d(intersection_point_x, intersection_point_y)

        return intersection_point

    
    @classmethod
    def get_penetration_length(cls, first_geometry_object: BaseGeometryObject, second_geometry_object: BaseGeometryObject) -> Optional[float]:
        function_to_call = 'get_penetr_length_'
        function_to_call += type(first_geometry_object).__name__.lower()
        function_to_call += "_" + type(second_geometry_object).__name__.lower()

        func = getattr(cls, function_to_call)
        return func(cls, first_geometry_object, second_geometry_object)

    @classmethod
    def get_penetr_length_line_line(cls, first_line: "Line", second_line: "Line") -> Optional[float]:

        coefficients = cls.get_penetr_line_line_coeff(first_line, second_line)
        if not coefficients:
            return None

        length = first_line.get_length()     
        penetration_length = length - length * coefficients[0]

        return penetration_length

    @classmethod
    def get_penetr_length_line_ray(cls, line: "Line", ray: "Ray") -> Optional[float]:

        coefficients = cls.get_penetr_line_ray_coeff(line, ray)
        if not coefficients:
            return None

        length = line.get_length()        
        penetration_length = length - length * coefficients[0]

        return penetration_length

    @classmethod
    def get_penetr_length_ray_line(cls, ray: "Ray", line: "Line") -> Optional[float]:
        return cls.get_penetr_length_line_ray(line, ray)


class Line(BaseGeometryObject):

    def __init__(self, first_point: Vector2d, second_point: Vector2d):

        if first_point.get_squared_magnitude() > second_point.get_squared_magnitude():
            raise AttributeError("First point should be closer to the origin than second point")

        if first_point == second_point:
            raise AttributeError("First and second point can't have the same coordinates")

        self.first_point = first_point
        self.second_point = second_point

    def __len__(self) -> float:
        return self.get_length()

    def get_length(self) -> float:
        return (self.second_point - self.first_point).get_magnitude()

    def is_point_belongs(self, point) -> bool:
        slope = (self.second_point.y - self.first_point.y) / (self.second_point.x - self.first_point.x)
        b = self.first_point.y - self.first_point.x * slope

        if point.y == point.x * slope + b and point.x >= self.first_point.x and point.y <= self.second_point.x:
            return True

        return False

    def get_intersection_data(self, other_object: BaseGeometryObject) -> Optional[Tuple[Vector2d, float, float]]:
        return ShapeInteractionDetector().get_intersection_data(self, other_object)
   
    def get_penetration_length(self, other_object: BaseGeometryObject) -> Optional[float]:
        return ShapeInteractionDetector().get_penetration_length(self, other_object)


class Ray(Line):

    def get_length(self) -> float:
        """Ray don't have length, it's infinite"""
        return -1.0

    def is_point_belongs(self, point) -> bool:
        slope = (self.second_point.y - self.first_point.y) / (self.second_point.x - self.first_point.x)
        b = self.first_point.y - self.first_point.x * slope

        if point.y == point.x * slope + b:
            return True

        return False

    def get_intersection_data(self, other_object: BaseGeometryObject) -> Optional[Tuple[Vector2d, float, float]]:
        return ShapeInteractionDetector().get_intersection_data(self, other_object)
   
    def get_penetration_length(self, other_object: BaseGeometryObject) -> Optional[float]:
        return ShapeInteractionDetector().get_penetration_length(self, other_object)


class BaseShape(ABC, BaseGeometryObject):

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_height(self) -> float:
        """Returns the height of a shapes rectangle box"""

    @abstractmethod
    def get_width(self) -> float:
        """Returns the width of a shapes rectangle box"""

    @abstractmethod
    def is_point_belongs(self, point) -> bool:
        """Returns true if a point placed situated inside a shape"""

class Circle(BaseShape):
    """Represent circle shape that you can use to create object"""

    def __init__(self, center: Vector2d, radius: float) -> None:
        self.radius = radius
        self.center = center

    def get_area(self) -> float:
        return PI * self.radius * self.radius

    def get_height(self) -> float:
        return self.get_diameter()

    def get_width(self) -> float:
        return self.get_diameter()

    def get_diameter(self) -> float:
        return self.radius * 2


class Oval(BaseShape):

    def __init__(self, center: Vector2d, horizontal_radius: float, vertical_radius: float) -> None:
        self.horizontal_radius = horizontal_radius
        self.vertical_radius = vertical_radius
        self.center = center

    def get_area(self) -> float:
        return PI * self.horizontal_radius * self.vertical_radius

    def get_height(self) -> float:
        return self.vertical_radius * 2

    def get_width(self) -> float:
        return self.horizontal_radius * 2


class Rectangle(BaseShape):
    
    def __init__(self, left_upper_corner: Vector2d, width: float, height: float) -> None:
        self.left_upper_corner = left_upper_corner
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.height * self.width

    def get_height(self) -> float:
        return self.height

    def get_width(self) -> float:
        return self.width


class Particle(BaseShape):
    
    def __init__(self, position: Vector2d) -> None:
        self.position = position

    def get_area(self) -> float:
        return 0.0

    def get_height(self) -> float:
        return 0.0

    def get_width(self) -> float:
        return 0.0

class Polygon(BaseShape):
    """Represent arbitrary convex shape"""

    def __init__(self, points: List[Vector2d]) -> None:
        """Creates a polygon from a list of points. Should be specified at least 3 points

        points (List[Vector2d]): list of points that represent border of the shape
                                 should be specified in the order they connect to each other
        """

        if len(points) < 3:
            raise Exception(
                "Polygon should have at least 3 points, you specified: " + str(len(points)))

        self.points = points
        self.the_most_distant_points = self.get_the_most_distant_points()
        self.triangles = self.triangulate(points[0])

    def get_the_most_distant_points(self) -> Tuple[Vector2d, Vector2d, Vector2d, Vector2d]:
        """Return tuple of four the most distant points (x, y coordinates) starting from max x and by clockwise

        (max_x_point, max_y_point, min_x_point, min_y_point)
        """
        max_x = -math.inf
        min_x = math.inf
        max_y = -math.inf
        min_y = math.inf
        max_x_point, max_y_point, min_x_point, min_y_point = Vector2d(
            0, 0), Vector2d(
            0, 0), Vector2d(
            0, 0), Vector2d(
            0, 0)

        for point in self.points:
            if max_x < point.x:
                max_x = point.x
                max_x_point = point

            elif min_x > point.x:
                min_x = point.x
                min_x_point = point

            if max_y < point.y:
                max_y = point.y
                max_y_point = point

            elif min_y > point.y:
                min_y = point.y
                min_y_point = point

        return (max_x_point, max_y_point, min_x_point, min_y_point)

    def get_area(self) -> float:
        area = 0.0

        for triangle in self.triangles:
            area += triangle.get_area()
        
        return area

    def get_height(self) -> float:
        max_x_point, max_y_point, min_x_point, min_y_point = self.get_the_most_distant_points()

        return max_y_point.y - min_y_point.y

    def get_width(self) -> float:
        max_x_point, max_y_point, min_x_point, min_y_point = self.get_the_most_distant_points()

        return max_x_point.x - min_x_point.x

    def triangulate(self, point: Vector2d) -> List[Triangle]:
        vertex_index = self.get_vertex_index(point)
        triangles = []

        for i in range(len(self.points)):
            if vertex_index and (i == vertex_index or i == (vertex_index - 1) or i == (vertex_index + 1)):
                continue
            
            triangle_points = [point, self.points[i], self.points[i + 1]] 
            triangles.append(Triangle(triangle_points))

        return triangles

        

    def get_vertex_index(self, point: Vector2d) -> Optional[int]:
        """Searches the point in a polygon vertexes list
        and return index. If point does not one of vertexes return None
        """

        # is the given point one of the vertexes
        for i in range(len(self.points)):
            if self.points[i] is point:
                return i

        return None

class Triangle(Polygon):

    def __init__(self, points: List[Vector2d]) -> None:

        if len(points) != 3:
            raise AttributeError("Triangle should have exactly 3 points, you specified: " + str(len(points)))

        self.points = points

    def get_area(self) -> float:
        a, b, c = self.get_sides_magnitude()

        semi_perimeter = 0.5 * (a + b + c)
        area = 0.5 * math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))

        return area

    def get_sides_magnitude(self) -> Tuple[float, float, float]:
        first_point, second_point, third_point = self.points[0], self.points[1], self.points[2]

        first_side = (second_point - first_point).get_magnitude()
        second_side = (third_point - second_point).get_magnitude()
        third_side = (first_point - third_point).get_magnitude()

        return (first_side, second_side, third_side)

    def is_point_belongs(self, point) -> bool:
        pass