import kubepy

instance_path = r"D:\Minecraft\instances\1.20.1(2)\.minecraft"

items = kubepy.ItemRegistry(instance_path=instance_path)

items.create('test_item').texture('minecraft:item/torch').maxStackSize(16)
items.create('test_item2').texture('minecraft:block/stone').maxStackSize(64)

items.compile('items_kpy', '1.20.1')