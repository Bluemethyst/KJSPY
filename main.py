import kubepy

instance_path = r"D:\Coding\KubePY"

recipes = kubepy.Recipes(instance_path=instance_path)

recipes.shapeless('minecraft:oak_log', 'minecraft:oak_plank')
recipes.shapeless('minecraft:oak_log', 'minecraft:oak_plank')
recipes.smelting('minecraft:coal', 'minecraft:diamond')
recipes.campfireCooking('minecraft:torch', 'minecraft:stick')
recipes.blasting('minecraft:coal_block', 'minecraft:diamond')
recipes.custom({
                "type": "minecraft:stonecutting",
                "ingredient": {
                    "item": "minecraft:stone"
                },
                "result": "minecraft:blackstone_stairs",
                "count": 0
                })
recipes.remove({ id: 'minecraft:glowstone'})


recipes.compile('script', '1.20.1')