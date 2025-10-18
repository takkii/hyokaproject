import gc
import os
import random
import traceback
from os.path import dirname, join
from typing import Optional

import cv2
import face_recognition
import numpy as np
import numpy.typing as npt
from django.shortcuts import render
from dotenv import load_dotenv
from PIL import Image

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BFP = os.environ.get("before_param")
AFP = os.environ.get("after_param")
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

    # Add exception handling.
    try:
        # Destination for the two images.
        before = os.path.expanduser(str(BFP))
        after = os.path.expanduser(str(AFP))

        # Specify the path of the face photo to be compared.
        my_before = face_recognition.load_image_file(before)
        my_after = face_recognition.load_image_file(after)

        # A list of 128-dimensional face recognition before/after encode.
        before_enc = cv2.cvtColor(my_before, cv2.COLOR_BGR2RGB)
        after_enc = cv2.cvtColor(my_after, cv2.COLOR_BGR2RGB)

        # Which face detection model to use.
        # "hog" is less accurate but faster on CPUs.
        # "cnn" is a more accurate deep-learning model,
        # which is GPU/CUDA accelerated (if available) / The default is "hog".
        lo_before = face_recognition.face_locations(my_before, model='cnn')[0]
        lo_after = face_recognition.face_locations(my_after, model='cnn')[0]

        # The data is processed as a feature quantity.
        en_b = face_recognition.face_encodings(before_enc)[0]
        en_a = face_recognition.face_encodings(after_enc)[0]

        # Add a square green line around the face.
        cv2.rectangle(my_before, (lo_before[3], lo_before[0]), (lo_before[1], lo_before[2]), (0, 255, 0), 3)
        cv2.rectangle(my_after, (lo_after[3], lo_after[0]), (lo_after[1], lo_after[2]), (0, 255, 0), 3)

        # Launch two images.
        cv2.startWindowThread()
        cv2.imshow('Before picture images.', my_before)
        cv2.imshow('After picture images.', my_after)
        cv2.waitKey(15000)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

        # hyoka_accuracy calc / result.
        face_d: npt.NDArray = face_recognition.face_distance([en_b], en_a)
        hyoka: npt.DTypeLike = np.floor(face_d * 1000).astype(int) / 1000

        # Displays phrases from the Hyakunin Isshu at random.
        hyaku: Optional[str] = '/hyokapp/txt/hyakunin.txt'

        # Default, hyoka < lose is float number.
        lose: Optional[str] = LON

        # A return value of lose or less is expected.
        if hyoka.astype(np.float64)[0] < float(lose):
            # The words from Hyakunin Isshu are displayed randomly.
            with open(os.getcwd() + hyaku) as r_meth:
                nin: Optional[list] = list(r_meth.readlines())
                issue: Optional[list] = [s.rstrip() for s in nin]
                mark: Optional[str] = str(random.choice(issue))
                print("⭕️ hyoka_accuracy: " + str(hyoka))
                return render(request, 'hyokapp/index.html', context={"check": mark})

        # Values of lose or higher are expected.
        elif not hyoka.astype(np.float64)[0] < float(lose):
            # Please use a different photo as it does not meet the criteria.
            fail = "❎️ lose: " + str(lose) + " < hyoka_accuracy: " + str(hyoka)
            return render(request, 'hyokapp/index.html', context={"failed": fail})

        # Usually not reached.
        else:
            # Unique exception occurrence.
            raise ValueError("hyoka accuracy is diable, Please select diffrent picture.")

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
