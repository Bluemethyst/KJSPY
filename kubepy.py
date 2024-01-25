import json
import os


class Recipes():
    def __init__(self, instance_path):
        self.instance_path = instance_path
        self.recipes_list = {"recipes": {"vanilla": [], "custom": []}}
        self.remove_list = {"removals": []}
        
    def custom(self, custom_json):
        self.recipes_list["recipes"]["custom"].append(custom_json)
        
    def remove(self, input):
        self.remove_list["removals"].append(f"{input}")
    
    def shaped(self, output, input, key):
        self.recipes_list["recipes"]["vanilla"].append({"type": "shaped", "output": output, "input": input, "key": key})
    
    def shapeless(self, output, input):
        self.recipes_list["recipes"]["vanilla"].append({"type": "shapeless", "output": output, "input": input})
        
    def smelting(self, output, input):
        self.recipes_list["recipes"]["vanilla"].append({"type": "smelting", "output": output, "input": input})
        
    def smoking(self, output, input):
        self.recipes_list["recipes"]["vanilla"].append({"type": "smoking", "output": output, "input": input})
        
    def blasting(self, output, input):
        self.recipes_list["recipes"]["vanilla"].append({"type": "blasting", "output": output, "input": input})
        
    def campfireCooking(self, output, input):
        self.recipes_list["recipes"]["vanilla"].append({"type": "campfireCooking", "output": output, "input": input})
        
    def stonecutting(self, output, input):
        self.recipes_list["recipes"]["vanilla"].append({"type": "stonecutting", "output": output, "input": input})
    
    def smithing(self, output, input, upgrade_item):
        self.recipes_list["recipes"]["vanilla"].append({"type": "smithing", "output": output, "input": input, "upgrade_item": upgrade_item})
    
    def compile(self, script_name, version):
        dir_path = f"{self.instance_path}\\kubejs\\server_scripts"
        os.makedirs(dir_path, exist_ok=True)
        #print(json.dumps(self.recipes_list, indent=4))
        with open(f"{dir_path}\\{script_name}.js", 'w') as f:
            f.write('// Written with KubePY, expect errors or it to not work at all')
            f.write('\nServerEvents.recipes(event => {')
            for recipe in self.recipes_list["recipes"]["vanilla"]:
                if recipe["type"] == "smithing":
                    f.write(f"\n    event.{recipe['type']}('{recipe['output']}', '{recipe['input']}', '{recipe['upgrade_item']}')")
                elif recipe["type"] == "shaped":
                    f.write(f"\n    event.{recipe['type']}('{recipe['output']}', {recipe['input']}, {recipe['key']})")
                else:
                    f.write(f"\n    event.{recipe['type']}('{recipe['output']}', '{recipe['input']}')")
            for recipe in self.recipes_list["recipes"]["custom"]:
                f.write(f"\n    event.custom({json.dumps(recipe, indent=4)})")
            for recipe in self.remove_list["removals"]:
                f.write(f"\n    event.remove({recipe})")
            f.write("\n})")
            

