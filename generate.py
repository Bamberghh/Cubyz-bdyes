from pathlib import Path
import shutil

short_recipes: bool = False

root = Path('.')
recipes_dir = root / 'recipes'
dye_items_dir = root / 'items/dye'

dirs = [
    recipes_dir,
    dye_items_dir,
]

for dir_ in dirs:
    dir_.mkdir(exist_ok=True)

item_types = [
    ('cubyz:chalk', 'chalk'),
    ('cubyz:cloth/block', 'cloth_block'),
    ('cubyz:glass', 'glass'),
]

colors = [
    'aqua',
    'black',
    'blue',
    'brown',
    'crimson',
    'cyan',
    'dark_grey',
    'green',
    'grey',
    'indigo',
    'lime',
    'magenta',
    'orange',
    'pink',
    'purple',
    'red',
    'violet',
    'viridian',
    'white',
    'yellow',
]

for dye_color in colors:
    dye_item_file = dye_items_dir / f'{dye_color}.zig.zon'
    with dye_item_file.open('w', encoding='utf-8') as dye_item:
        dye_item.write(
f'''.{{
	.texture = "dye/{dye_color}.png",
}}
''')

for (item_type, item_type_short) in item_types:
    recipes_file = recipes_dir / f'{item_type_short}.zig.zon'
    with recipes_file.open('w', encoding='utf-8') as recipes:
        recipes.write('.{\n')
        for item_color in colors:
            for dye_color in colors:
                if item_color == dye_color:
                    continue
                recipes.write(f'    .{{ .inputs = .{{ "{item_type}/{item_color}", "bdyes:dye/{dye_color}" }}, .output = "{item_type}/{dye_color}" }},\n')
        recipes.write('}')

