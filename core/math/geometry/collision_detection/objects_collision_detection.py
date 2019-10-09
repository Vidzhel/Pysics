from .lines.lines_collision_detection import *
from .lines.is_lines_intersect import *
from .lines.lines_distance import *

from .line_ellipse.line_ellipse_collision_detection import *
from .line_ellipse.is_line_ellipse_intersect import *
from .line_ellipse.line_ellipse_distance import *

from .line_polygon.line_polygon_collision_detection import *
from .line_polygon.is_line_polygon_intersect import *
from .line_polygon.line_polygon_distance import *

from .ellipses.ellipses_collision_detection import *
from .ellipses.ellipses_distance import *
from .ellipses.is_ellipses_intersect import *

from .ellipse_polygon.ellipse_polygon_collision_detection import *
from .ellipse_polygon.ellipse_polygon_distance import *
from .ellipse_polygon.is_ellipse_polygon_intersect import *

from .polygons.concave_polygons_collision_detection import *
from .polygons.convex_polygons_collision_detection import *
from .polygons.concave_convex_collision_detection import *
from .polygons.is_convex_polygons_intersect import *
from .polygons.is_concave_polygons_intersect import *
from .polygons.is_concave_convex_intersect import *
from .polygons.concave_polygons_distance import *
from .polygons.convex_polygons_distance import *
from .polygons.concave_convex_distance import *

from core.math.vector2d import Vector2d
from .collision_data import CollisionData

from typing import List, Optional, Tuple

class CollisionDetection:

    @classmethod
    def get_intersection_data(cls, first_geometry_object: "BaseGeometryObject",
                              second_geometry_object: "BaseGeometryObject") -> CollisionData:
        """Returns an intersection point of the lines, t and u

        t, u represent where an intersection point falls (first and second segment) 0.0 ≤ t, u ≤ 1.0
        """

        function_to_call = 'get_inter_data_'
        class_name1 = type(first_geometry_object).__name__.lower()
        class_name2 = type(second_geometry_object).__name__.lower()

        function_to_call += class_name1 + "_" + class_name2
        try:
            func = globals()[function_to_call]
        except KeyError:
            raise TypeError(
                "Function that gets intersection data of " + class_name1 + ' and ' + class_name2 + ' could not be found')

        return func(first_geometry_object, second_geometry_object)

    @classmethod
    def get_distance_length(cls, first_geometry_object: "BaseGeometryObject",
                               second_geometry_object: "BaseGeometryObject") -> Optional[float]:
        function_to_call = 'get_distance_'
        function_to_call += type(first_geometry_object).__name__.lower()
        function_to_call += "_" + type(second_geometry_object).__name__.lower()

        func = getattr(cls, function_to_call)
        return func(cls, first_geometry_object, second_geometry_object)
