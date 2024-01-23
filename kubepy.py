import json

class Recipes():
    def __init__(self, instance_path):
        self.instance_path = instance_path
        self.recipes_list = {"recipes": []}
        
    def shapeless(self, output, input):
        self.recipes_list["recipes"].append({"output": output, "input": input})
    
    def compile(self, script_name):
        print(json.dumps(self.recipes_list, indent=4))