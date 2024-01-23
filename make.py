#!/usr/bin/env python3
import json
from io import TextIOWrapper
from zipfile import ZipFile

tools: dict[str, dict] = {
    "minecraft:netherite_axe": {
        "type": "computercraft:tool",
        "item": "minecraft:netherite_axe",
        "adjective": "upgrade.minecraft.diamond_axe.adjective",
        "damageMultiplier": 6,
        "allowEnchantments": True,
        "consumeDurability": "when_enchanted",
    },
    "minecraft:netherite_pickaxe": {
        "type": "computercraft:tool",
        "item": "minecraft:netherite_pickaxe",
        "adjective": "upgrade.minecraft.diamond_pickaxe.adjective",
        "allowEnchantments": True,
        "consumeDurability": "when_enchanted",
    },
    "minecraft:netherite_hoe": {
        "type": "computercraft:tool",
        "item": "minecraft:netherite_hoe",
        "adjective": "upgrade.minecraft.diamond_hoe.adjective",
        "breakable": "computercraft:turtle_hoe_harvestable",
        "allowEnchantments": True,
        "consumeDurability": "when_enchanted",
    },
    "minecraft:netherite_shovel": {
        "type": "computercraft:tool",
        "item": "minecraft:netherite_shovel",
        "adjective": "upgrade.minecraft.diamond_shovel.adjective",
        "breakable": "computercraft:turtle_shovel_harvestable",
        "allowEnchantments": True,
        "consumeDurability": "when_enchanted",
    },
    "minecraft:netherite_sword": {
        "type": "computercraft:tool",
        "item": "minecraft:netherite_sword",
        "adjective": "upgrade.minecraft.diamond_sword.adjective",
        "breakable": "computercraft:turtle_sword_harvestable",
        "damageMultiplier": 9,
        "allowEnchantments": True,
        "consumeDurability": "when_enchanted",
    },
}

extra_files = [
    "pack.mcmeta",
]

with ZipFile("netherite-tools.zip", "w") as zip:
    for id, tool in tools.items():
        mod, path = id.split(":", maxsplit=1)
        with zip.open(f"data/{mod}/computercraft/turtle_upgrades/{path}.json", "w") as out:
            with TextIOWrapper(out) as wrapper:
                json.dump(tool, wrapper)

    for file in extra_files:
        with open(file, "rb") as input:
            zip.write(file)
