from PIL import Image

image_paths = [
    r"C:\Users\abdul\Desktop\1.webp",
    r"C:\Users\abdul\Desktop\2.webp",
    r"C:\Users\abdul\Desktop\3.webp",
    r"C:\Users\abdul\Desktop\4.webp",
    r"C:\Users\abdul\Desktop\5.webp",
    r"C:\Users\abdul\Desktop\6.webp",
    r"C:\Users\abdul\Desktop\7.webp",
    r"C:\Users\abdul\Desktop\8.webp",
    r"C:\Users\abdul\Desktop\9.webp",
    r"C:\Users\abdul\Desktop\10.webp"
]


images = [Image.open(img_path) for img_path in image_paths]


images[0].save(
    "animation.gif",
    save_all=True,
    append_images=images[1:],
    duration=250,
    loop=0
)