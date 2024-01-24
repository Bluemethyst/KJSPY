// Written with KubePY, expect errors or it to not work at all
ServerEvents.recipes(event => {
    event.shapeless('minecraft:diamond', 'minecraft:iron_block')
    event.smelting('minecraft:coal', 'minecraft:diamond')
    event.campfireCooking('minecraft:torch', 'minecraft:stick')
    event.blasting('minecraft:coal_block', 'minecraft:diamond')
    event.custom({
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
    event.remove({'id': 'minecraft:glowstone'})
})