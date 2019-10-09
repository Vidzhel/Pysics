import math
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

from core.math.vector2d import Vector2d

PI = 3.1416


class BaseGeometryObject(ABC):

	@abstractmethod
	def is_point_belongs(self, point) -> bool:
		pass


class Particle(BaseGeometryObject):

	def __init__(self, position: Vector2d) -> None:
		self.position = position

	def is_point_belongs(self, point) -> bool:
		if point == self.position:
			return True

		return False


class Ray(BaseGeometryObject):
	"""Represents a line that starts at first_point and goes through the second_point into the
	infinity"""

	def __init__(self, first_point: Vector2d, second_point: Vector2d):

		if first_point == second_point:
			raise AttributeError("First and second point can't have the same coordinates")

		self.first_point = first_point
		self.second_point = second_point

	def get_direction(self) -> Vector2d:
		return (self.second_point - self.first_point).normalize()

	def get_vector(self) -> Vector2d:
		return self.second_point - self.first_point

	def is_vertical(self):
		return self.second_point.x - self.first_point.x == 0

	def is_horizontal(self):
		return self.second_point.y - self.first_point.y == 0

	def get_slope(self) -> float:
		numerator = self.second_point.y - self.first_point.y
		dominator = self.second_point.x - self.first_point.x

		if dominator == 0:
			return 100000

		return numerator / dominator

	def get_y_intercept(self, slope: float) -> float:
		return self.first_point.y - self.first_point.x * slope

	def is_point_belongs(self, point) -> bool:
		slope = self.get_slope()
		b = self.get_y_intercept(slope)

		# The point should lay on the line and have the same direction as a ray
		ray_direction = self.get_direction()
		from_first_to_point_direction = (point - self.first_point).normalize()

		if math.isclose(point.y, point.x * slope + b,
		                abs_tol=0.01) and ray_direction == from_first_to_point_direction:
			return True

		return False

	def get_distance_to_point(self, point: Vector2d) -> float:
		closest_point = self.get_closest_point(point)
		distance = (point - closest_point).get_magnitude()

		return distance

	def get_closest_point(self, point: Vector2d) -> Vector2d:
		# Get a point by projecting the segment from the first point to the given onto a Line
		# it it does not belong to the Ray than it placed behind the first point
		from_first_point_to_point = point - self.first_point
		this_line = self.first_point - self.second_point

		closest_point = self.first_point + from_first_point_to_point.project_on(this_line)

		if self.is_point_belongs(closest_point):
			return closest_point

		return self.first_point

	def get_perpendicular(self) -> "Ray":
		return Ray(self.first_point.get_perpendicular_vector(),
		           self.second_point.get_perpendicular_vector())

	def get_cos_of_angle(self, other: "Ray"):
		this_vector = self.second_point - self.first_point
		other_vector = other.second_point - other.first_point

		return this_vector.get_cos_of_angle(other_vector)

	def get_angle(self, other: "Ray"):
		this_vector = self.first_point - self.second_point
		other_vector = other.second_point - other.first_point

		return this_vector.get_angle(other_vector)


class Line(Ray):
	"""Represents an infinity line that goes through first and second points"""

	def is_point_belongs(self, point) -> bool:
		slope = self.get_slope()
		b = self.get_y_intercept(slope)

		if math.isclose(point.y, point.x * slope + b, abs_tol=0.01):
			return True

		return False

	def get_closest_point(self, point: Vector2d) -> Vector2d:
		from_first_point_to_point = point - self.first_point
		this_line = self.first_point - self.second_point

		closest_point = self.first_point + from_first_point_to_point.project_on(this_line)
		return closest_point

	def get_perpendicular(self) -> "Line":
		return Line(self.first_point.get_perpendicular_vector(),
		            self.second_point.get_perpendicular_vector())


class Segment(Line):
	"""Represents a line that is placed between the first and the second points"""

	def __len__(self) -> float:
		return self.get_length()

	def get_length(self) -> float:
		return (self.second_point - self.first_point).get_magnitude()

	def is_point_belongs(self, point: Vector2d) -> bool:
		slope = self.get_slope()
		b = self.get_y_intercept(slope)
		min_x = min(self.first_point.x, self.second_point.x)
		max_x = max(self.first_point.x, self.second_point.x)
		min_y = min(self.first_point.y, self.second_point.y)
		max_y = max(self.first_point.y, self.second_point.y)

		if math.isclose(point.y, point.x * slope + b, abs_tol=0.01) and min_x <= point.x <= \
				max_x and min_y <= point.y <= max_y:
			return True

		return False

	def get_closest_point(self, point: Vector2d) -> Vector2d:
		from_first_point_to_point = point - self.first_point
		this_line = self.first_point - self.second_point
		closest_point = self.first_point + from_first_point_to_point.project_on(this_line)

		if self.is_point_belongs(closest_point):
			return closest_point

		from_second_point_to_point = point - self.second_point

		distance_from_start = from_first_point_to_point.get_magnitude()
		distance_from_end = from_second_point_to_point.get_magnitude()
		if distance_from_start > distance_from_end:
			return self.second_point

		return self.first_point

	def get_middle_point(self) -> Vector2d:
		x = self.first_point.x / 2 + self.second_point.x / 2
		y = self.first_point.y / 2 + self.second_point.y / 2

		return Vector2d(x, y)

	def get_perpendicular(self) -> "Segment":
		return Segment(self.first_point.get_perpendicular_vector(),
		               self.second_point.get_perpendicular_vector())


class BaseShape(BaseGeometryObject):

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
	def get_support_point(self, direction: Vector2d):
		"""Gets a point with the biggest dot product on the direction vector"""


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

	def is_point_belongs(self, point) -> bool:
		distance_to_center = (self.center - point).get_magnitude()

		if math.isclose(distance_to_center, self.radius,
		                abs_tol=0.01) or distance_to_center <= self.radius:
			return True

		return False

	def get_support_point(self, direction: Vector2d):
		direction = direction.normalize()
		direction = direction.scale(self.radius)
		point = self.center + direction

		return point


class Ellipse(BaseShape):

	def __init__(self, center: Vector2d, horizontal_radius: float, vertical_radius: float) -> None:
		self.horizontal_radius = horizontal_radius
		self.vertical_radius = vertical_radius
		self.center = center

	def get_max_radius(self) -> float:
		return max(self.horizontal_radius, self.vertical_radius)

	def get_min_radius(self) -> float:
		return min(self.horizontal_radius, self.vertical_radius)

	def get_area(self) -> float:
		return PI * self.horizontal_radius * self.vertical_radius

	def get_height(self) -> float:
		return self.vertical_radius * 2

	def get_width(self) -> float:
		return self.horizontal_radius * 2

	def is_point_belongs(self, point) -> bool:
		# Use equation of ellipse to determinate either the point belongs to the ellipse
		left = point.x ** 2 / self.horizontal_radius ** 2
		right = point.y ** 2 / self.vertical_radius ** 2
		res = left + right

		if math.isclose(res, 1, abs_tol=0.01) or res < 1:
			return True

		return False


class BasePolygon(BaseShape, ABC):

	def __init__(self, points: List[Vector2d]) -> None:
		"""Creates a polygon from a list of points. Should be specified at least 3 points

		points (List[Vector2d]): list of points that represent border of the shape
								 should be specified in the order they connect to each other
		"""

		if len(points) < 3:
			raise Exception(
				"ConvexPolygon should have at least 3 points, you specified: " + str(len(points)))

		self.points = points
		self.points_count = len(self.points)

		self.the_most_distant_points = self.get_the_most_distant_points()

		self.triangles = self.triangulate(points[0])

		self.sides = self.get_sides()
		self.sides_count = len(self.sides)

		self.centroid = self.get_centroid()

		self.diagonals = self.get_diagonals()

	def get_the_most_distant_points(self) -> Tuple[Vector2d, Vector2d, Vector2d, Vector2d]:
		"""Return tuple of four the most distant points (x, y coordinates) starting from max x
		and by clockwise

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

		return max_x_point, max_y_point, min_x_point, min_y_point

	def triangulate(self, point: Vector2d) -> List['Triangle']:
		vertex_index = self.get_vertex_index(point)
		triangles = []

		for i in range(self.points_count):
			is_this_vertex = i == vertex_index

			previous_index = (vertex_index - 1)
			if previous_index < 0:
				previous_index = self.points_count - 1
			is_previous_vertex = i == previous_index

			next_index = (vertex_index + 1)
			if previous_index > self.points_count - 1:
				next_index = 0
			is_next_vertex = i == next_index
			if vertex_index is not None and (is_this_vertex or is_previous_vertex or is_next_vertex):
				continue

			triangle_points = [point, self.points[i], self.points[i + 1]]
			triangles.append(Triangle(triangle_points))

		return triangles

	def get_sides(self) -> List[Segment]:
		sides: List[Segment] = []

		for i in range(self.points_count):
			if i == self.points_count - 1:
				side = Segment(self.points[i], self.points[0])
			else:
				side = Segment(self.points[i], self.points[i + 1])

			sides.append(side)

		return sides

	def get_centroid(self) -> Vector2d:
		# https://en.wikipedia.org/wiki/Polygon
		centroid = Vector2d(0, 0)
		signed_area = 0.0

		for i in range(self.points_count - 1):
			x0 = self.points[i].x
			y0 = self.points[i].y
			x1 = self.points[i + 1].x
			y1 = self.points[i + 1].y

			temp_area = x0 * y1 - x1 * y0
			signed_area += temp_area
			centroid.x += (x0 + x1) * temp_area
			centroid.y += (y0 + y1) * temp_area

		x0 = self.points[self.points_count - 1].x
		y0 = self.points[self.points_count - 1].y
		x1 = self.points[0].x
		y1 = self.points[0].y
		temp_area = x0 * y1 - x1 * y0
		signed_area += temp_area
		centroid.x += (x0 + x1) * temp_area
		centroid.y += (y0 + y1) * temp_area

		signed_area *= 0.5
		centroid.x /= (6.0 * signed_area)
		centroid.y /= (6.0 * signed_area)

		return centroid

	def get_diagonals(self) -> List[Segment]:
		diagonals: List[Segment] = []

		for point in self.points:
			diagonals.append(Segment(self.centroid, point))

		return diagonals

	def get_area_triangles(self) -> float:
		area = 0.0

		for triangle in self.triangles:
			area += triangle.get_area()

		return area

	def get_area(self) -> float:
		# To get an area of a polygon you need to get array of points in counterclockwise order
		# and multiply x of each point on y of the next point, then do the same with y and x
		# get the sum and divide on 2

		res = 0
		reversed_sides = self.sides[::-1]

		for side in reversed_sides:
			res += side.second_point.x * side.first_point.y

		for side in reversed_sides:
			res += side.second_point.y * side.first_point.x

		return 0.5 * res

	def get_height(self) -> float:
		max_x_point, max_y_point, min_x_point, min_y_point = self.the_most_distant_points

		return max_y_point.y - min_y_point.y

	def get_width(self) -> float:
		max_x_point, max_y_point, min_x_point, min_y_point = self.the_most_distant_points

		return max_x_point.x - min_x_point.x

	def get_vertex_index(self, point: Vector2d) -> Optional[int]:
		"""Searches the point in a polygon vertexes list
		and return index. If point does not one of vertexes return None
		"""

		# is the given point one of the vertexes
		for i in range(self.points_count):
			if self.points[i] is point:
				return i

		return None

	def is_point_belongs(self, point) -> bool:
		# Draw a horizontal ray that starts the point, if count of times the ray intersects with
		# a polygon sides is even than the point located inside the polygon

		hor_line = Ray(point, point.x + 1)
		data = hor_line.get_intersection_data(self)
		if not data:
			return False

		inter_points = data[0]

		if len(inter_points) % 2 == 1:
			return True

		return False

	def is_concave(self):
		"""To determinate ether a polygon is concave we will calculate
		cross product for each pair of vectors and if all the results are
		greater or all are smaller than zero than it will be convex poly
		"""

		cross_products = []

		for i in range(self.sides_count - 1):
			first_vector = self.sides[i].get_vector()
			second_vector = self.sides[i + 1].get_vector()

			cross_products.append(first_vector.cross(second_vector))

		sign = cross_products[0]

		for cp in cross_products:
			if cp * sign < 0:
				return True

		return False

	def get_side_with_point(self, point: Vector2d) -> List[Line]:
		sides_with_point = []
		for side in self.sides:
			if side.first_point == point or side.second_point == point:
				sides_with_point.append(side)

		return sides_with_point

	def get_support_point(self, direction: Vector2d) -> Vector2d:
		support_point = None
		max_product = -1

		for point in self.points:
			product = direction.dot_product(point)

			if product > max_product:
				max_product = product
				support_point = point

		return support_point


class ConvexPolygon(BasePolygon):

	def __init__(self, points: List[Vector2d]):
		super().__init__(points)

		if self.is_concave():
			raise AttributeError("Convex polygon can't have interior angles > 180 degrees")


class ConcavePolygon(BasePolygon):

	def __init__(self, points: List[Vector2d]):
		super().__init__(points)

		if not self.is_concave():
			raise AttributeError("Concave polygon should have at least one interior angle > 180 degrees")

		self.check_self_inter_poly()

	def check_self_inter_poly(self):

		for i in range(self.sides_count - 1):
			is_inter = self.sides[i].get_intersection_data(self.sides[i + 1])
			if is_inter:
				raise AttributeError("Self-intersecting polygons are disallowed")

		is_inter = self.sides[0].get_intersection_data(self.sides[self.sides_count - 1])
		if is_inter:
			raise AttributeError("Self-intersecting polygons are disallowed")

	def triangulate(self, point: Vector2d) -> List['Triangle']:
		pass


class Rectangle(ConvexPolygon):

	def __init__(self, left_upper_corner: Vector2d, width: float, height: float) -> None:
		self.left_upper_corner = left_upper_corner
		self.width = width
		self.height = height

		points = self.get_corners()
		super().__init__(list(points))

	def get_corners(self) -> Tuple[Vector2d, Vector2d, Vector2d, Vector2d]:
		left_lower_corner = self.left_upper_corner.copy()
		left_lower_corner.y -= self.height

		right_upper_corner = self.left_upper_corner.copy()
		right_upper_corner.x += self.width

		right_lower_corner = right_upper_corner.copy()
		right_lower_corner.y -= self.height

		return self.left_upper_corner, right_upper_corner, right_lower_corner, left_lower_corner

	def get_area(self) -> float:
		return self.height * self.width

	def get_height(self) -> float:
		return self.height

	def get_width(self) -> float:
		return self.width


class Triangle(ConvexPolygon):

	def __init__(self, points: List[Vector2d]) -> None:

		if len(points) != 3:
			raise AttributeError(
				"Triangle should have exactly 3 points, you specified: " + str(len(points)))

		super().__init__(points)

	def get_area(self) -> float:
		a, b, c = self.get_sides_magnitude()

		semi_perimeter = 0.5 * (a + b + c)
		area = 0.5 * math.sqrt(
			semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))

		return area

	def get_sides_magnitude(self) -> Tuple[float, float, float]:
		first_point, second_point, third_point = self.points[0], self.points[1], self.points[2]

		first_side = (second_point - first_point).get_magnitude()
		second_side = (third_point - second_point).get_magnitude()
		third_side = (first_point - third_point).get_magnitude()

		return first_side, second_side, third_side
