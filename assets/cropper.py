from PIL import Image
import sys

scale = 1
version = 2

args = sys.argv

for arg in args:
    if "scale=" in arg:
        s = arg.replace("scale=", "").strip()
        s = int(s)
        if s in (1,2,3,4,8,16):
            scale = s
    elif "version=" in arg:
        v = arg.replace("version=", "").strip()
        v = int(v)
        if v in (1, 2):
            version = v

cropdata = {}

with open("crop.txt") as cropfile:
    for line in cropfile.readlines():
        if (line + "#")[0] != "#":
            key, data = line.split("=")
            data = tuple(int(n) * scale for n in data.strip().split(","))
            cropdata[key.strip()] = data
            
with Image.open(f"v{version}/GameAssets_x{scale}.png") as img:
    for name, area in cropdata.items():
        l, u, w, h = area
        r = l + w
        b = u + h
        img.crop((l, u, r, b)).save(f"v{version}/cropped/{name}_x{scale}.png")

print(f"succesfully cropped assets (version={version}, scale={scale})")