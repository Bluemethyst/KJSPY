
try:
    import kubepy
except ImportError:
    print("This module (KubePY Create) relies on the KubePY module, please install it with pip install kubepy")
    
class Recipes():
    def __init__(self, instance_path):
        self.instance_path = instance_path
        self.recipes_list = {"recipes": {"create": []}}
        
    def pressing(self, output, input):
        self.recipes_list["recipes"]["create"].append({"type": "shapeless", "output": output, "input": input})