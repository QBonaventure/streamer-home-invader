#!/usr/bin/python3

from flask import Flask, request, jsonify
import json
from multiprocessing import Process, Queue
from gpiozero import PWMLED
from time import sleep
from rgb import RGB

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def foo():
    return {
        'statusCode': 200
    }


@app.route('/event_triggered', methods=['POST'])
def event_triggered(**kwargs):
    type = request.args.get("type", None)
    print(type)
    q.put(type)

    return {
        'statusCode': 200
    }


def led_loop(q):
    rgb = RGB()
    rgb.white()
    sleep(0.5)
    rgb.black()
    sleep(0.5)

    while True:
        if q.qsize() > 0:
          type = q.get(False)

          if type == "modswitch":
            rgb.modSwitchLoop()

          elif type == "follows":
            rgb.followLoop()

          elif type == "streamchange":
            rgb.streamChangeLoop()

          elif type == "subscription":
              rgb.black()
              rgb.subscriptionLoop()

          else:
            print("-> triggers default")
            rgb.defaultEventLoop()
        else:
            rgb.black()
            rgb.breath(rgb.r, 1/10, 1<<8, 1<<16)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=led_loop, args=(q,))
    p.start()
    app.run(host='0.0.0.0')
    p.join()
