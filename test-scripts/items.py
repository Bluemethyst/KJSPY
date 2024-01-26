import kubepy

instance_path = r"D:\Minecraft\instances\1.20.1(2)\.minecraft"

items = kubepy.ItemRegistry(instance_path=instance_path)
blocks = kubepy.BlockRegistry(instance_path=instance_path)

blocks.create('test_block').textureAll('minecraft:block/oak_log')

items.create('test_item').texture('minecraft:block/torch').maxStackSize(16).displayName('yoo this workin?')
items.create('test_item2').texture('minecraft:block/stone').maxStackSize(64).burnTime(120)
items.create('test_item3').texture('minecraft:block/blackstone').maxStackSize(64).rarity('rare')
items.create('test_tool', 'axe').texture('minecraft:item/diamond_axe').tier('diamond')

items.compile('items_kpy', '1.20.1')
blocks.compile('blocks_kpy', '1.20.1')