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
        
    def create(self, item_name, tool = None):
        
        if tool != None:
            self.item_list["items"].append({"new_item": f"'{item_name}', '{tool}'"})
        else:
            self.item_list["items"].append({"new_item": f"'{item_name}'"})
        return self

    def texture(self, texture):
        if self.item_list["items"]:
            self.item_list["items"][-1]["texture"] = texture
        return self

    def maxStackSize(self, maxStackSize):
        if self.item_list["items"]:
            self.item_list["items"][-1]["maxStackSize"] = maxStackSize
        return self
    
    def maxDamage(self, maxDamage):
        if self.item_list["items"]:
            self.item_list["items"][-1]["maxDamage"] = maxDamage
        return self
    
    def burnTime(self, burnTime):
        if self.item_list["items"]:
            self.item_list["items"][-1]["burnTime"] = burnTime
        return self
    
    def fireResistant(self, fireResistant):
        if self.item_list["items"]:
            self.item_list["items"][-1]["fireResistant"] = fireResistant
        return self
    
    def rarity(self, rarity):
        if self.item_list["items"]:
            self.item_list["items"][-1]["rarity"] = rarity
        return self
    
    def glow(self, glow):
        if self.item_list["items"]:
            self.item_list["items"][-1]["glow"] = glow
        return self
    
    def tooltip(self, tooltip):
        if self.item_list["items"]:
            self.item_list["items"][-1]["tooltip"] = tooltip
        return self
    
    def color(self, color):
        if self.item_list["items"]:
            self.item_list["items"][-1]["color"] = color
        return self
        
    def displayName(self, displayName):
        if self.item_list["items"]:
            self.item_list["items"][-1]["displayName"] = displayName
        return self
        
    def tag(self, tag):
        if self.item_list["items"]:
            self.item_list["items"][-1]["tag"] = tag
        return self
    
    def tier(self, tier):
        if self.item_list["items"]:
            self.item_list["items"][-1]["tier"] = tier
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
                f.write("\nonEvent('item.registry', event => {")
            else:
                f.write("\nStartupEvents.registry('item', event => {")
            for item in self.item_list["items"]:
                create_str = f"event.create({item['new_item']})"
                if 'texture' in item:
                    create_str += f".texture('{item['texture']}')"
                if 'maxStackSize' in item:
                    create_str += f".maxStackSize({item['maxStackSize']})"
                if 'maxDamage' in item:
                    create_str += f".maxDamage({item['maxDamage']})"
                if 'burnTime' in item:
                    create_str += f".burnTime({item['burnTime']})"
                if 'fireResistant' in item:
                    create_str += f".fireResistant({item['fireResistant']})"
                if 'rarity' in item:
                    create_str += f".rarity('{item['rarity']}')"
                if 'glow' in item:
                    create_str += f".glow({item['glow']})"
                if 'tooltip' in item:
                    create_str += f".tooltip('{item['tooltip']}')"
                if 'color' in item:
                    create_str += f".color({item['color']})"
                if 'displayName' in item:
                    create_str += f".displayName('{item['displayName']}')"
                if 'tag' in item:
                    create_str += f".tag('{item['tag']}')"
                if 'tier' in item:
                    create_str += f".tier('{item['tier']}')"
                # Add other properties here...
                f.write(f"\n    {create_str}")
            f.write("\n})")
            print(json.dumps(self.item_list, indent=4))
    
    
class BlockRegistry():
    def __init__(self, instance_path: str):
        self.instance_path = instance_path
        self.block_list = {"blocks": []}
        
    def create(self, block_name, tool = None):
        if tool != None:
            self.block_list["blocks"].append({"new_block": f"'{block_name}', '{tool}'"})
        else:
            self.block_list["blocks"].append({"new_block": f"'{block_name}'"})
        return self

    def textureAll(self, textureAll):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["textureAll"] = textureAll
        return self

    def maxStackSize(self, maxStackSize):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["maxStackSize"] = maxStackSize
        return self
    
    def maxDamage(self, maxDamage):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["maxDamage"] = maxDamage
        return self
    
    def burnTime(self, burnTime):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["burnTime"] = burnTime
        return self
    
    def fireResistant(self, fireResistant):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["fireResistant"] = fireResistant
        return self
    
    def rarity(self, rarity):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["rarity"] = rarity
        return self
    
    def glow(self, glow):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["glow"] = glow
        return self
    
    def tooltip(self, tooltip):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["tooltip"] = tooltip
        return self
    
    def color(self, color):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["color"] = color
        return self
        
    def displayName(self, displayName):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["displayName"] = displayName
        return self
        
    def tag(self, tag):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["tag"] = tag
        return self
    
    def tier(self, tier):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["tier"] = tier
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
                f.write("\nonEvent('block.registry', event => {")
            else:
                f.write("\nStartupEvents.registry('block', event => {")
            for block in self.block_list["blocks"]:
                create_str = f"event.create({block['new_block']})"
                if 'textureAll' in block:
                    create_str += f".textureAll('{block['textureAll']}')"
                if 'maxStackSize' in block:
                    create_str += f".maxStackSize({block['maxStackSize']})"
                if 'maxDamage' in block:
                    create_str += f".maxDamage({block['maxDamage']})"
                if 'burnTime' in block:
                    create_str += f".burnTime({block['burnTime']})"
                if 'fireResistant' in block:
                    create_str += f".fireResistant({block['fireResistant']})"
                if 'rarity' in block:
                    create_str += f".rarity('{block['rarity']}')"
                if 'glow' in block:
                    create_str += f".glow({block['glow']})"
                if 'tooltip' in block:
                    create_str += f".tooltip('{block['tooltip']}')"
                if 'color' in block:
                    create_str += f".color({block['color']})"
                if 'displayName' in block:
                    create_str += f".displayName('{block['displayName']}')"
                if 'tag' in block:
                    create_str += f".tag('{block['tag']}')"
                if 'tier' in block:
                    create_str += f".tier('{block['tier']}')"
                # Add other properties here...
                f.write(f"\n    {create_str}")
            f.write("\n})")
            print(json.dumps(self.block_list, indent=4))