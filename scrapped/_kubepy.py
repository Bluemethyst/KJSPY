import json

class ServerEvents():
    """Used for server scripts"""
    def __init__(self, instance_path):
        """Initialize

        Args:
            instance_path (str): Path of your minecraft instance.
        """
        self.instance_path = instance_path
        self.recipes_list = {"recipes": []}
        self.shapeless_recipes = None
        self.shaped_recipes = None
        self.smelting_recipes = None
        self.blasting_recipes = None

       
    def recipes(self, **kwargs):
        """
        Goes into server_scripts. Create recipes here.
        """
        if "shapeless" in kwargs:
            self.shapeless_recipes = f"event.shapeless{kwargs['shapeless']}"
            '''print("Shapeless Recipe: ", kwargs["shapeless"])
            self.recipes_list['shapeless'] = kwargs["shapeless"]
            json_result = {
                "type": "minecraft:crafting_shapeless",
                "ingredients": kwargs["shapeless"][1],
                "result": {
                    "item": kwargs["shapeless"][0]
                }
            }
            print(json_result)'''

        if "shaped" in kwargs:
            self.shaped_recipes = f"event.shaped{kwargs['shaped']}"

        if "smelting" in kwargs:
            self.smelting_recipes = f"event.smelting{kwargs['smelting']}"

        if "blasting" in kwargs:
            self.blasting_recipes = f"event.blasting{kwargs['blasting']}"
            
    def compile(self, script_name):
        """Compile you python script in a hopefully valid kubejs script

        Args:
            script_name (str): the name of the script
        """
        print(json.dumps(self.recipes_list, indent=4))
        with open(f"{self.instance_path}\kubejs\server_scripts\{script_name}.js", 'w') as f:
            f.write('// Written with KubePY, expect errors or it to not work at all')
            f.write('\nServerEvents.recipes(event => {')
            if self.shapeless_recipes is not None:
                f.write(f'\n    {self.shapeless_recipes}')
            if self.shaped_recipes is not None:
                f.write(f'\n    {self.shaped_recipes}')
            if self.smelting_recipes is not None:
                f.write(f'\n    {self.smelting_recipes}')
            if self.blasting_recipes is not None:
                f.write(f'\n    {self.blasting_recipes}')
            f.write('\n})\n')
            f.write('console.log("Recipes loaded successfully!");')
        

                