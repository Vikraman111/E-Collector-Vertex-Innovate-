from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

MODEL_PATH = 'yolov3.weights'
CONFIG_PATH = 'yolov3.cfg'
LABELS_PATH = 'coco.names'

CATEGORIES ={
    "Mobile Devices": [
        "mobile phone","cell phone","smartphone","iphone",
        "android phone","mobile device"],
    "Computing Devices": [
        "laptop","mouse","keyboard","monitor"
        "computer","desktop","tablet","touchpad",
        "pc","macbook","chromebook"],
        "Audio Devices":[
            "headphones","earbuds","earphones","wireless earbuds","speaker",
            "bluetooth speaker","headset", "airpods","earpods","microphone",   ],  
                     
        "Power & Charging":[
            "power adapter,""charger","power supply","power bank"
        ],
        
        
}