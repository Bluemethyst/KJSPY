import kubepy

#recipes = kubepy.Recipes(instance_path='D:\\Minecraft\\instances\\1.20.1(2)\\.minecraft')
recipes = kubepy.Recipes(instance_path=r'C:\Users\Admin\Documents\KubePY')

recipes.shapeless('minecraft:oak_log', 'minecraft:oak_plank')
recipes.shapeless('minecraft:oak_log', 'minecraft:oak_plank')
recipes.smelting('minecraft:coal', 'minecraft:diamond')
recipes.custom({
                "type": "minecraft:stonecutting",
                "ingredient": {
                    "item": "minecraft:stone"
                },
                "result": "minecraft:blackstone_stairs",
                "count": 0
                })

recipes.compile('script.js', '1.20.1')