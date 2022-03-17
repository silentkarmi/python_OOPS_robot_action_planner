class Gripper:
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
        return self._enable
    
    @property
    def object_held(self):
        return self._object_held
    
    @object_held.setter
    def object_held(self, some_object):
        self._object_held = some_object
    
    def activate_gripper(self):
        self._enable = True
    
    def deactivate_gripper(self):
        self._enable = False
        
    def is_gripper_empty(self):
        return self._object_held is None