from utils.utility import print_normal

class Gripper:
    """Gripper is part of the BaseRobot, because every robot has a gripper
    """
    def __init__(self, name, weight = 2, closing_speed = 150) -> None:
        self._name = name
        self._weight = weight
        self._closing_speed = closing_speed
        self._enable = False
        self._object_held = None
        
    def __str__(self) -> str:
        return f"Gripper = {self._name}"
    
    @property
    def enable(self):
        """Returns the activate state of the girpper

        Returns:
            bool: True or False
        """
        return self._enable
    
    @property
    def object_held(self):
        """Object held by the gripper

        Returns:
            Any: It returns the object held which can be part or tray
        """
        return self._object_held
    
    @object_held.setter
    def object_held(self, some_object):
        self._object_held = some_object
    
    def activate_gripper(self):
        """Activates the gripper
        """
        print_normal(f"activate {self._name}\n")
        self._enable = True
    
    def deactivate_gripper(self):
        """Deactivates the gripper
        """
        print_normal(f"deactivate {self._name}\n")
        self._enable = False
        
    def is_gripper_empty(self):
        """Tells if gripper is holding any object or not

        Returns:
            Any: It can contain either a Tray or a Part
        """
        return self._object_held is None