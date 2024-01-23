// Written with KubePY, expect errors or it to not work at all
ServerEvents.recipes(event => {
    event.shapeless('minecraft:log', 'minecraft:stone')
    event.shaped('minecraft:stone_pickaxe', [' S ', ' S ', 'CSC'], {'S': 'minecraft:stick', 'C': 'minecraft:cobblestone'})
    event.smelting('minecraft:coal', 'kubejs:reactants')
})
console.log("Recipes loaded successfully!");