import json
import os
import time
#import git
#import shutil

#https://packaging.python.org/en/latest/tutorials/packaging-projects/
#https://docs.python.org/3/library/typing.html
            

def init(mcVersion):
    global version
    version = mcVersion

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
    
    def compile(self, script_name: str):
        start_time = time.time()
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
        end_time = time.time()
        print(fr"Compiled {script_name}.js to {self.instance_path}\kubejs\server_scripts in {end_time - start_time} seconds")
    

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
        
    def compile(self, script_name: str):
        """compile the kubepy code to valid kubejs code

        Args:
            script_name (str): name of the script
            version (str): minecraft version of the script
        """
        start_time = time.time()
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
            #print(json.dumps(self.item_list, indent=4))
            end_time = time.time()
            print(fr"Compiled {script_name}.js to {self.instance_path}\kubejs\startup_scripts in {end_time - start_time} seconds")
    
    
class BlockRegistry():
    """Create custom blocks. Please read more [here](https://kubejs.com/wiki/ref/BlockBuilder)
    """
    def __init__(self, instance_path: str):
        self.instance_path = instance_path
        self.block_list = {"blocks": []}
        
    def create(self, block_name):
        """Create custom blocks. Please read more [here](https://kubejs.com/wiki/ref/BlockBuilder)
        """
        self.block_list["blocks"].append({"new_block": f"'{block_name}'"})
        return self

    def textureAll(self, textureAll):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["textureAll"] = textureAll
        return self

    def displayName(self, displayName):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["displayName"] = displayName
        return self
    
    def tagBlock(self, tagBlock):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["tagBlock"] = tagBlock
        return self
    
    def tagItem(self, tagItem):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["tagItem"] = tagItem
        return self
    
    def tagBoth(self, tagBoth):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["tagBoth"] = tagBoth
        return self
    
    def hardness(self, hardness):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["hardness"] = hardness
        return self
    
    def resistance(self, resistance):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["resistance"] = resistance
        return self
    
    def unbreakable(self, unbreakable):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["unbreakable"] = unbreakable
        return self
    
    def lightLevel(self, lightLevel):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["lightLevel"] = lightLevel
        return self
        
    def opaque(self, opaque):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["opaque"] = opaque
        return self
        
    def fullBlock(self, fullBlock):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["fullBlock"] = fullBlock
        return self
    
    def requiresTool(self, requiresTool):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["requiresTool"] = requiresTool
        return self
    
    def renderType(self, renderType):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["renderType"] = renderType
        return self
    
    def color(self, color):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["color"] = color
        return self
    
    def texture(self, side, texture):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["texture"] = f"'{side}', '{texture}'"
        return self
    
    def model(self, model):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["model"] = model
        return self
    
    def noItem(self):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["noItem"] = 'noItem'
        return self
    
    def noCollision(self):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["noCollision"] = 'noCollision'
        return self
    
    def waterlogged(self):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["waterlogged"] = 'waterlogged'
        return self
    
    def noDrops(self):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["noDrops"] = 'noDrops'
        return self
    
    def notSolid(self):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["notSolid"] = 'notSolid'
        return self
        
    def slipperiness(self, slipperiness):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["slipperiness"] = slipperiness
        return self
        
    def speedFactor(self, speedFactor):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["speedFactor"] = speedFactor
        return self
        
    def jumpFactor(self, jumpFactor):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["jumpFactor"] = jumpFactor
        return self
        
    def noValidSpawns(self, noValidSpawns):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["noValidSpawns"] = noValidSpawns
        return self
        
    def suffocating(self, suffocating):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["suffocating"] = suffocating
        return self
        
    def viewBlocking(self, viewBlocking):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["viewBlocking"] = viewBlocking
        return self
        
    def redstoneConductor(self, redstoneConductor):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["redstoneConductor"] = redstoneConductor
        return self
        
    def transparent(self, transparent):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["transparent"] = transparent
        return self
    
    def defaultTranslucent(self, defaultTranslucent):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["defaultTranslucent"] = defaultTranslucent
        return self
    
    def defaultCutout(self, defaultCutout):
        if self.block_list["blocks"]:
            self.block_list["blocks"][-1]["defaultCutout"] = defaultCutout
        return self
        
    def compile(self, script_name: str):
        """compile the kubepy code to valid kubejs code

        Args:
            script_name (str): name of the script
            version (str): minecraft version of the script
        """
        start_time = time.time()
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
                if 'displayName' in block:
                    create_str += f".displayName('{block['displayName']}')"
                if 'tagBlock' in block:
                    create_str += f".tagBlock('{block['tagBlock']}')"
                if 'tagItem' in block:
                    create_str += f".tagItem('{block['tagItem']}')"
                if 'tagBoth' in block:
                    create_str += f".tagBoth('{block['tagBoth']}')"
                if 'hardness' in block:
                    create_str += f".hardness({block['hardness']})"
                if 'resistance' in block:
                    create_str += f".resistance({block['resistance']})"
                if 'unbreakable' in block:
                    create_str += f".unbreakable()"
                if 'lightLevel' in block:
                    create_str += f".lightLevel({block['lightLevel']})"
                if 'opaque' in block:
                    create_str += f".opaque({block['opaque']})"
                if 'fullBlock' in block:
                    create_str += f".fullBlock({block['fullBlock']})"
                if 'requiresTool' in block:
                    create_str += f".requiresTool({block['requiresTool']})"
                if 'renderType' in block:
                    create_str += f".renderType('{block['renderType']}')"
                if 'texture' in block:
                    create_str += f".texture({block['texture']})"
                if 'model' in block:
                    create_str += f".model('{block['model']}')"
                if 'noItem' in block:
                    create_str += f".noItem()"
                if 'noCollision' in block:
                    create_str += f".noCollision()"
                if 'notSolid' in block:
                    create_str += f".notSolid()"
                if 'waterlogged' in block:
                    create_str += f".waterlogged()"
                if 'noDrops' in block:
                    create_str += f".noDrops()"
                if 'slipperiness' in block:
                    create_str += f".slipperiness({block['slipperiness']})"
                if 'speedFactor' in block:
                    create_str += f".speedFactor({block['speedFactor']})"
                if 'jumpFactor' in block:
                    create_str += f".jumpFactor({block['jumpFactor']})"
                if 'noValidSpawns' in block:
                    create_str += f".noValidSpawns({block['noValidSpawns']})"
                if 'suffocating' in block:
                    create_str += f".suffocating({block['suffocating']})"
                if 'viewBlocking' in block:
                    create_str += f".viewBlocking({str(block['viewBlocking']).lower()})"
                if 'redstoneConductor' in block:
                    create_str += f".redstoneConductor({str(block['redstoneConductor']).lower()})"
                if 'transparent' in block:
                    create_str += f".transparent({str(block['transparent']).lower()})"
                if 'defaultTranslucent' in block:
                    create_str += f".defaultTranslucent()"
                if 'defaultCutout' in block:
                    create_str += f".defaultCutout()"
                # Add other properties here...
                f.write(f"\n    {create_str}")
            f.write("\n})")
            #print(json.dumps(self.block_list, indent=4))
            end_time = time.time()
            print(fr"Compiled {script_name}.js to {self.instance_path}\kubejs\startup_scripts in {end_time - start_time} seconds")
            
class FluidRegistry():
    """Create custom fluids. Please read more [here](https://kubejs.com/wiki/tutorials/fluid-registry)
    """
    def __init__(self, instance_path: str):
        self.instance_path = instance_path
        self.fluid_list = {"fluids": []}
        
    def create(self, fluid_name):
        """Create custom fluids. Please read more [here](https://kubejs.com/wiki/tutorials/fluid-registry)
        """
        self.fluid_list["fluids"].append({"new_fluid": f"'{fluid_name}'"})
        return self
    
    def displayName(self, displayName):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["displayName"] = displayName
        return self
    
    def rarity(self, rarity):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["rarity"] = rarity
        return self
    
    def color(self, color):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["color"] = color
        return self
    
    def bucketColor(self, bucketColor):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["bucketColor"] = bucketColor
        return self
    
    def thinTexture(self, thinTexture):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["thinTexture"] = thinTexture
        return self
    
    def thickTexture(self, thickTexture):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["thickTexture"] = thickTexture
        return self
    
    def builtinTextures(self):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["builtinTextures"] = 'builtinTextures'
        return self
    
    def stillTexture(self, stillTexture):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["stillTexture"] = stillTexture
        return self
    
    def flowingTexture(self, flowingTexture):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["flowingTexture"] = flowingTexture
        return self
    
    def noBucket(self):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["noBucket"] = 'noBucket'
        return self
    
    def noBlock(self):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["noBlock"] = 'noBlock'
        return self
    
    def gaseous(self):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["gaseous"] = 'gaseous'
        return self
    
    def luminosity(self, luminosity):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["luminosity"] = luminosity
        return self
    
    def density(self, density):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["density"] = density
        return self
    
    def temperature(self, temperature):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["temperature"] = temperature
        return self
    
    def viscosity(self, viscosity):
        if self.fluid_list["fluids"]:
            self.fluid_list["fluids"][-1]["viscosity"] = viscosity
        return self
    
    def compile(self, script_name: str):
            """compile the kubepy code to valid kubejs code

            Args:
                script_name (str): name of the script
                version (str): minecraft version of the script
            """
            start_time = time.time()
            dir_path = f"{self.instance_path}\\kubejs\\startup_scripts"
            os.makedirs(dir_path, exist_ok=True)
            #print(json.dumps(self.fluid_list, indent=4))
            with open(f"{dir_path}\\{script_name}.js", 'w') as f:
                f.write('// Written with KubePY, expect errors or it to not work at all')
                if version < "1.19.2":
                    f.write("\nonEvent('fluid.registry', event => {")
                else:
                    f.write("\nStartupEvents.registry('fluid', event => {")
                for item in self.fluid_list["fluids"]:
                    create_str = f"event.create({item['new_fluid']})"
                    if 'displayName' in item:
                        create_str += f".displayName({item['displayName']})"
                    if 'rarity' in item:
                        create_str += f".rarity('{item['rarity']}')"
                    if 'color' in item:
                        create_str += f".color({item['color']})"
                    if 'bucketColor' in item:
                        create_str += f".bucketColor({item['bucketColor']})"
                    if 'thinTexture' in item:
                        create_str += f".thinTexture({item['thinTexture']})"
                    if 'thickTexture' in item:
                        create_str += f".thickTexture({item['thickTexture']})"
                    if 'builtinTextures' in item:
                        create_str += f".builtinTextures()"
                    if 'stillTexture' in item:
                        create_str += f".stillTexture('{item['stillTexture']}')"
                    if 'flowingTexture' in item:
                        create_str += f".flowingTexture('{item['flowingTexture']}')"
                    if 'noBucket' in item:
                        create_str += f".noBucket()"
                    if 'noBlock' in item:
                        create_str += f".noBlock()"
                    if 'gaseous' in item:
                        create_str += f".gaseous()"
                    if 'luminosity' in item:
                        create_str += f".luminosity({item['luminosity']})"
                    if 'density' in item:
                        create_str += f".density({item['density']})"
                    if 'temperature' in item:
                        create_str += f".temperature({item['temperature']})"
                    if 'viscosity' in item:
                        create_str += f".viscosity({item['viscosity']})"
                    
                    f.write(f"\n    {create_str}")
                f.write("\n})")
                #print(json.dumps(self.item_list, indent=4))
                end_time = time.time()
                print(fr"Compiled {script_name}.js to {self.instance_path}\kubejs\startup_scripts in {end_time - start_time} seconds")