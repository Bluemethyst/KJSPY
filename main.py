import kubepy

# https://kubejs.com/wiki/tutorials/recipes

instance_path = r"D:\Minecraft\instances\1.20.1(2)\.minecraft"

recipes = kubepy.Recipes(instance_path=instance_path)

recipes.shapeless('minecraft:diamond', 'minecraft:iron_block')
recipes.smelting('minecraft:coal', 'minecraft:diamond')
recipes.campfireCooking('minecraft:torch', 'minecraft:stick')
recipes.blasting('minecraft:coal_block', 'minecraft:diamond')
recipes.custom({
  "type": "tconstruct:entity_melting",
  "entity": {
    "types": [
      "minecraft:skeleton",
      "minecraft:stray"
    ]
  },
  "result": {
    "fluid": "tconstruct:molten_iron",
    "amount": 25
  },
  "damage": 2
})
recipes.remove({'id': 'minecraft:glowstone'})


recipes.compile('script', '1.20.1')