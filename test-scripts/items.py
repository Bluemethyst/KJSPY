import kjspy

kjspy.init('1.20.1')
instance_path = r"D:\Minecraft\instances\1.20.1(2)\.minecraft"

items = kjspy.ItemRegistry(instance_path=instance_path)
blocks = kjspy.BlockRegistry(instance_path=instance_path)
fluids = kjspy.FluidRegistry(instance_path=instance_path)

fluids.create('test_fluid').thinTexture('0xff0000')

blocks.create('test_block').textureAll('minecraft:block/oak_log')
blocks.create('test_2').texture('up', 'minecraft:block/white_wool').waterlogged().transparent(True)

items.create('test_item').texture('minecraft:block/torch').maxStackSize(16).displayName('yoo this workin?')
items.create('test_item2').texture('minecraft:block/stone').maxStackSize(64).burnTime(120)
items.create('test_item3').texture('minecraft:block/blackstone').maxStackSize(64).rarity('rare')
items.create('test_tool', 'axe').texture('minecraft:item/diamond_axe').tier('diamond')

items.compile('items_kpy')
blocks.compile('blocks_kpy')
fluids.compile('fluids_kpy')