# import necesaary libraries
import cv2
from PIL import Image,ImageDraw,ImageFont
import os
video_path="bad_apple.mp4"
output_folder="bad_apple_frames"
# creating output frame folder
os.makedirs(output_folder,exsist_ok=True)
# open video folder
cap=cv2.VideoCapture(video_path)
frame_number=0
#create a while loop to read the file
while True:
    ret,frame=cap.read()
    if not ret:
        break

# turn video file into image file
frame_image=Image.fromarray(frame)
frame_image.save(os.path.join(output_folder,f{"frame_number:04d"}))

frame_number+=1
#release video capture
cap.release()

# create ascii art
def create_ascii_frame(image_path,width,height):
    image=Image.open(image_path)
    image=image.resize((width,height))
    ascii_image=Image.new("RGB",(width,height),(0,0,0))
    draw=ImageDraw.Draw(ascii_image)

for y in range(height):
    for x in range(width):
        r,g,b=image.getpixel((x,y))
        gray=int(0.2989*r+0.5870*g+0.1140*b)
        draw.text((x,y),chr(9608),fill(gray,gray,gray))

return ascii_image
output_frame=os.listdir(output_folder)
output_frames.sort()

#ascii output folder
os.makedirs("bad_apple_ascii",exist_ok=True)

#  output ascii art
for i ,frame in enumerate(output_frames):
    ascii_frames=create_ascii_frame(os.path.join(output_folder_frame),100,60)
    ascii_frames.save(os.path.join("bad_apple_ascii",f"{i:04d}.png"))

print("character frame generated")



