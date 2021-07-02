# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def video_to_images(videoFileName, outputFolderName):
    vidcap = cv2.VideoCapture(videoFileName)

    success, image = vidcap.read()
    count = 0
    while success:
#        print(f"{1:02d}")
#        print(f'{val:02}')
        cv2.imwrite(f"image/{outputFolderName}/frame{count:04}.jpg", image)  # save frame as JPEG file
        success, image = vidcap.read()
        print(f'Read a new frame[{count:04}]: ', success)
        count += 1


if __name__ == '__main__':
    print_hi('PyCharm');

#    fileName = '20210511_1120'
#    fileName = '20210510_1139'
#    fileName = '20210510_1737'
#    video_to_images('video/' + fileName + '.mp4', fileName);