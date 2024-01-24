// Written with KubePY, expect errors or it to not work at all
ServerEvents.recipes(event => {
    event.shapeless('minecraft:oak_log', 'minecraft:oak_plank')
    event.shapeless('minecraft:oak_log', 'minecraft:oak_plank')
    event.smelting('minecraft:coal', 'minecraft:diamond')
    event.campfireCooking('minecraft:torch', 'minecraft:stick')
    event.blasting('minecraft:coal_block', 'minecraft:diamond')
    event.custom({
    "type": "minecraft:stonecutting",
    "ingredient": {
        "item": "minecraft:stone"
    },
    "result": "minecraft:blackstone_stairs",
    "count": 0
})
    event.remove({<built-in function id>: 'minecraft:glowstone'}
})