def get_inter_data_line_particle(line: Union["Segment", "Line"], particle: "Particle") -> Optional[
	Tuple[Vector2d, float]]:
	if line.is_point_belongs(particle.position):
		return particle.position, 1

	return None


def get_inter_data_particle_line(particle: "Particle", line: "Segment") -> Optional[
	Tuple[Vector2d, float]]:
	return get_inter_data_line_particle(line, particle)


def get_inter_data_ray_particle(ray: "Line", particle: "Particle") -> Optional[
	Tuple[List[Vector2d], float]]:
	return get_inter_data_line_particle(ray, particle)


def get_inter_data_particle_ray(particle: "Particle", ray: "Line") -> Optional[
	Tuple[List[Vector2d], float]]:
	return get_inter_data_ray_particle(ray, particle)


def is_particle_belong_to_shape(particle: "Particle", shape: "BaseShape"):
	return shape.is_point_belongs(particle.position)


def get_inter_data_circle_particle(circle: "Circle", particle: "Particle") -> Optional[
	Tuple[Vector2d, float, float]]:
	if is_particle_belong_to_shape(particle, circle):
		pass


def get_inter_data_particle_circle(particle: "Particle", circle: "Circle") -> Optional[
	Tuple[Vector2d, float, float]]:
	pass


def get_inter_data_ellipse_particle(ellipse: "Ellipse", particle: "Particle") -> Optional[
	Tuple[Vector2d, float, float]]:
	pass


def get_inter_data_particle_ellipse(particle: "Particle", ellipse: "Ellipse") -> Optional[
	Tuple[Vector2d, float, float]]:
	pass


def get_inter_data_particle_particle(first_particle: "Particle", second_particle: "Particle") -> \
		Optional[Tuple[Vector2d, float, float]]:
	pass


def get_inter_data_particle_rectangle(particle: "Particle", rect: "Rectangle") -> Optional[
	Tuple[Vector2d, float, float]]:
	pass


def get_inter_data_rectangle_particle(rect: "Rectangle", particle: "Particle") -> Optional[
	Tuple[Vector2d, float, float]]:
	pass


def get_inter_data_particle_polygon(particle: "Particle", poly: "ConvexPolygon") -> Optional[
	Tuple[Vector2d, float, float]]:
	pass


def get_inter_data_polygon_particle(poly: "ConvexPolygon", particle: "Particle") -> Optional[
	Tuple[Vector2d, float, float]]:
	pass


def get_inter_data_particle_triangle(particle: "Particle", triangle: "Triangle") -> Optional[
	Tuple[Vector2d, float, float]]:
	pass


def get_inter_data_triangle_particle(triangle: "Triangle", particle: "Particle") -> Optional[
	Tuple[Vector2d, float, float]]:
	pass
