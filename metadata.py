import tinytag

vid = tinytag.TinyTag.get('test.mp4')

print(vid.as_dict())