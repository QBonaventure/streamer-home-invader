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
            try:
                type = q.get(False)
                print(type)
            except:
                continue
            else:
                print("something has to be triggered")
                if type == "modswitch":
                    print("-> triggers modswitch")
                    rgb.modSwitchLoop()
                elif type == "follows":

                    rgb.run("blink", 'g', 0.5, .6,)
                elif type == "streamchange":
                    print("-> triggers streamchange")
                    rgb.streamChangeLoop()
                elif type == "subscription":
                    rgb.run(("blink", 'b', 10.5, .5,))
                    rgb.run(("blink", 'r', 10, 1,))
                    rgb.run(("blink", 'g', 9.5, 1.5,))
                else:
                    print("-> triggers default")
                    rgb.defaultEventLoop()
        else:
            rgb.queue(("breath", 'r', 0.3, 2.0,))

if __name__ == '__main__':
    q = Queue()
    p = Process(target=led_loop, args=(q,))
    p.start()
    app.run(host='0.0.0.0')
    p.join()
