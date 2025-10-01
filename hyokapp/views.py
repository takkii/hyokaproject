import gc
import os
import random
import traceback
from os.path import dirname, join
from typing import Optional

import face_recognition
import golden_eagle as ga
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
GAN = os.environ.get("ga_num") or ""
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
        # Specify the path of the face photo to be compared.
        my_before = face_recognition.load_image_file(os.path.expanduser(str(BFP)))
        my_after = face_recognition.load_image_file(os.path.expanduser(str(AFP)))

        # facecompare version.
        print("golden-eagle_version: " + ga.__version__)

        # golden-eagle accuary number.
        ga_lose: Optional[str] = GAN

        # value is 0.6 and lower numbers make face comparisons more strict:
        ga.compare_before_after(my_before, my_after, float(ga_lose))

        # Define again, set of values.
        before_image = face_recognition.load_image_file(os.path.expanduser(str(BFP)))
        after_image = face_recognition.load_image_file(os.path.expanduser(str(AFP)))

        # The data is processed as a feature quantity.
        en_b = face_recognition.face_encodings(before_image)[0]
        en_a = face_recognition.face_encodings(after_image)[0]
        face_d: npt.NDArray = face_recognition.face_distance([en_b], en_a)
        hyoka = np.floor(face_d * 1000).astype(int) / 1000

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
            raise ValueError("Please check the passcode for your face photo.")

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
