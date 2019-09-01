from core.force_generators import force_generators

class DrugForce(force_generators.StaticForceGenerator):
    """Apply drug force on all non static objects"""

    def __init__(self, name: str, force: Vector2d, targeted_objects: List[BaseObject]) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        targeted_objects (List[BaseObject]): objects on which the force will be applied
        all static objects will be omitted
        """

        super().__init__(name, force, targeted_objects)

        