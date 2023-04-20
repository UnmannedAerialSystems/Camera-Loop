from picamera import PiCamera
from time import sleep
import time


def camera_loop(air_speed, img_size, altitude, focal_length, img_overlap, sensor_size):
    # img_size in px
    # altitude in m
    # focal length in mm 
    # air speed in m/s
    # img_overlap between 0 and 1 
    while True:
        # take picture 
        img_size_meters = get_img_size_meters(img_size, altitude, focal_length, sensor_size)
        delta_meters = img_size_meters * (1 - img_overlap)
        delta_seconds = delta_meters / air_speed
        time.sleep(delta_seconds)


def get_img_size_meters(img_width, altitude, focal_length, sensor_size):
    # img_width in pixels
    # focal_length in mm
    # sensor_size in mm
    # altitude in m

    GSD = (sensor_size * altitude * 100) / (focal_length * img_width)
    footprint_width = GSD * img_width
    return footprint_width * img_width

    #C = 2.41 # Constant determined through experiments, should be tested with pi cam
    # focal_length_px = focal_length * img_size / sensor_size
    # return C * (img_size / focal_length_px) * altitude 

'''
def get_GPS_offset(latitude, longitude, coordinates):
    # latitude in decimal degrees
    # longitude in decimal degrees
    # coordinates is a tuple (x, y)
    x, y = coordinates
    GSD = (sensor_size * altitude * 100) / (focal_length * img_width)
    footprint_width = GSD * img_width
'''



camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/tmp/picture.jpg')
camera.stop_preview()