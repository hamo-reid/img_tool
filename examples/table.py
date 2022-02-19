from img_tool import multi_text, ImageFactory, Box
from PIL import Image

table_size = (301, 301)
table_img = ImageFactory(Image.new('RGBA', table_size, color='white'))
rowCount, columnCount = 6, 3
cell_width, cell_height = int(table_size[0]/columnCount), int(table_size[1]/rowCount)
for x in range(columnCount):
    for y in range(rowCount):
        table_img.add_box(f'cell_{x}_{y}',
                          (cell_width*x, cell_height*y),
                          (cell_width, cell_height))
        table_img.rectangle(f'cell_{x}_{y}', outline='black')
columnIndexes = ['column0', 'column1', 'column2']
for i in range(columnCount):
    text_img = multi_text(columnIndexes[i], default_size=15)
    pos = table_img.align_box(f'cell_{i}_0', text_img, align='center')
    table_img.img_paste(text_img, pos)
background_size = (400, 400)
background_img = ImageFactory(Image.new('RGBA', background_size, color='grey'))
background_img.img_paste(table_img.img, align='center')
background_img.show()
