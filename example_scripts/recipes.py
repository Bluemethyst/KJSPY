import kjspy

# https://kubejs.com/wiki/tutorials/recipes

instance_path = r"D:\Minecraft\instances\1.20.1(2)\.minecraft"
kjspy.init('1.20.1')

recipes = kjspy.Recipes(instance_path=instance_path)

recipes.shapeless('minecraft:diamond', 'minecraft:iron_block')
recipes.shaped('minecraft:stone',['A B',' C ','B A'],{'A': 'minecraft:andesite','B': 'minecraft:diorite','C': 'minecraft:granite'})
recipes.smelting('minecraft:coal', 'minecraft:diamond')
recipes.campfireCooking('minecraft:torch', 'minecraft:stick')
recipes.blasting('minecraft:coal_block', 'minecraft:diamond')
recipes.smithing('minecraft:gold_block', 'minecraft:gold_ingot', 'minecraft:iron_block')
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


recipes.compile('recipes_kpy')