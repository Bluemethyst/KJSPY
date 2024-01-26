import json
import os
import requests
import git
import shutil

#https://packaging.python.org/en/latest/tutorials/packaging-projects/
#https://docs.python.org/3/library/typing.html
            

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
    
    def compile(self, script_name: str, version):
        dir_path = f"{self.instance_path}\\kubejs\\server_scripts"
        os.makedirs(dir_path, exist_ok=True)
        #print(json.dumps(self.recipes_list, indent=4))
        with open(f"{dir_path}\\{script_name}.js", 'w') as f:
            f.write('// Written with KubePY, expect errors or it to not work at all')
            if version < "1.19.2":
                f.write("\nonEvent('recipes', event => {")
            else:
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
    

class ItemRegistry():
    def __init__(self, instance_path: str):
        self.instance_path = instance_path
        self.item_list = {"items": []}
        
    def create(self, item_name):
        self.item_list["items"].append({"new_item": item_name})
        return self

    def texture(self, texture):
        if self.item_list["items"]:
            self.item_list["items"][-1]["texture"] = texture
        return self

    def maxStackSize(self, max_stack_size):
        if self.item_list["items"]:
            self.item_list["items"][-1]["max_stack_size"] = max_stack_size
        return self
        
    def compile(self, script_name: str, version: str):
        """compile the kubepy code to valid kubejs code

        Args:
            script_name (str): name of the script
            version (str): minecraft version of the script
        """
        dir_path = f"{self.instance_path}\\kubejs\\startup_scripts"
        os.makedirs(dir_path, exist_ok=True)
        #print(json.dumps(self.recipes_list, indent=4))
        with open(f"{dir_path}\\{script_name}.js", 'w') as f:
            f.write('// Written with KubePY, expect errors or it to not work at all')
            if version < "1.19.2":
                f.write("\nonEvent('recipes', event => {")
            else:
                f.write('\nServerEvents.recipes(event => {')
            for item in self.item_list["items"]:
                f.write(f"\n    event.create('{item['new_item']}')")
            f.write(json.dumps(self.item_list, indent=4))
    
    
class BlockRegistry():
    def __init__(self, instance_path):
        self.instance_path = instance_path
        self.block_list = {"blocks": []}