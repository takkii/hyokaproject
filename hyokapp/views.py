import gc
import os
import tkinter as tk
import traceback
from logging import DEBUG, Formatter, getLogger, handlers
from os.path import dirname, join
from typing import Optional

import cv2
import face_recognition
import imutils
import numpy as np
from django.shortcuts import render
from dotenv import load_dotenv
from PIL import Image, ImageTk

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BFP = os.environ.get("before_param")
ONM = os.environ.get("one_name")
PCI = os.environ.get("picture_images")

FLN = os.environ.get("fl_num") or ""
ICO = os.environ.get("int_conn") or ""
INN = os.environ.get("int_num") or ""
LON = os.environ.get("lo_num") or ""


# Accuracy Evaluation Project
def index(request):
    # face picture save path
    img_jpg = './Images/face.jpg'

    # create image file face.gif
    img_gif = './Images/face.gif'

    # face picture path
    is_file_jpg = os.path.isfile(img_jpg)
    is_file_gif = os.path.isfile(img_gif)

    # if jpeg image to path
    if is_file_jpg and not is_file_gif:
        img_jpg = './Images/face.jpg'
        img = Image.open(str(img_jpg))
        img.save('./Images/face.gif', 'gif')
        print('create image file ./Images/face.gif')
    else:
        pass

    root_logger = getLogger()
    root_logger.setLevel(DEBUG)

    # When the log reaches Default Settings,
    # it is backed up and a new file is created.
    rotating_handler = handlers.RotatingFileHandler(r'./hyokaproject.log',
                                                    mode="a",
                                                    maxBytes=int(INN) * 1024,
                                                    backupCount=3,
                                                    encoding="utf-8")

    logger = getLogger(__name__)
    format = Formatter(
        '%(asctime)s : %(levelname)s : %(filename)s - %(message)s')
    rotating_handler.setFormatter(format)
    root_logger.addHandler(rotating_handler)

    # Add exception handling.
    try:
        # Get a reference to webcam #0 (Built-in camera)
        video_capture = cv2.VideoCapture(int(ICO))
        # Get a reference to webcam #1 (External usb camera)
        # video_capture = cv2.VideoCapture(1)

        # Load a one sample picture and learn how to recognize it.
        one_image = face_recognition.load_image_file(str(BFP))
        one_face_encoding = face_recognition.face_encodings(one_image)[0]

        # Create arrays of known face encodings and their names
        known_face_encodings = [one_face_encoding]

        known_face_names = [str(ONM)]

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while True:
            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Only process every other frame of video to save time
            if process_this_frame:
                # Convert frame of BGR2RGB for faster face recognition processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image to COLOR_BGR2RGB color (which face_recognition uses)
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

                # The default is "hog" / other select "cnn"
                face_locations = face_recognition.face_locations(
                    rgb_small_frame, model='cnn')
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, face_locations)

                face_names = []
                lose = FLN

                for face_encoding in face_encodings:
                    # Setting, tolerance in .env
                    matches = face_recognition.compare_faces(
                        known_face_encodings,
                        face_encoding,
                        tolerance=float(lose))
                    name = "Unknown"

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(
                        known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                        logger.debug(name)

                    face_names.append(name)

            process_this_frame = not process_this_frame

            # Display the results
            for (top, right, bottom,
                 left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 5
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0),
                              2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom),
                              (0, 255, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.8,
                            (255, 255, 255), 1)

                # Display the resulting image
                cv2.imshow("Face Recognition Videos: s=save | q=exit", frame)
                k = cv2.waitKey(1) & 0xff
                img = imutils.resize(frame, width=350)

                # Hit 'q' on the keyboard to quit!
                if k == ord('s'):
                    cv2.imwrite(str(PCI), img)
                    if os.path.isfile(str(PCI)):
                        pil_image = Image.open(str(PCI))
                        w_size = int(pil_image.width)
                        h_size = int(pil_image.height)
                        root = tk.Tk()
                        root.title("Take On: q=exit | alt+F4=close")
                        canvas = tk.Canvas(root, width=w_size, height=h_size)
                        canvas.pack()
                        tk_image = ImageTk.PhotoImage(
                            image=pil_image.resize((w_size, h_size)))
                        canvas.create_image(0, 0, anchor='nw', image=tk_image)
                        root.mainloop()
                    else:
                        raise ValueError('No images saved')

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

    # TraceBack.
    except Exception:
        # Specify the folder to record the exception log.
        except_folder: Optional[str] = os.getcwd()
        # Specify the file to log exception occurrences.
        except_file: Optional[str] = os.getcwd() + '.log'

        # Load the dictionary.
        if os.path.isdir(os.path.expanduser(except_folder)):
            # Log writing process.
            with open(os.path.expanduser(except_file), 'a') as log_py:
                traceback.print_exc(file=log_py)

            # throw except.
            raise RuntimeError from None

        # Current directory Not Found.
        else:
            # Unique exception occurrence.
            raise ValueError("None, Please Check the Current directory.")

    # Once Exec.
    finally:
        gc.collect()
