import kubepy

recipes = kubepy.Recipes(instance_path='D:\\Minecraft\\instances\\1.20.1(2)\\.minecraft')

recipes.shapeless('minecraft:oak_log', 'minecraft:oak_plank')
recipes.shapeless('minecraft:oak_log', 'minecraft:oak_plank')

recipes.compile('script.js')