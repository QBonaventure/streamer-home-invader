#!/usr/bin/python3

from flask import Flask, request, jsonify
import json
from multiprocessing import Process, Queue
from time import sleep
from streamAnimation import StreamAnimation
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


def led_loop(q, baseClock):
    rgb = RGB(baseClock)
    sa = StreamAnimation(rgb)

    while True:
        if q.qsize() > 0:
          type = q.get(False)
          # sa.stopAll()

          if type == "modswitch":
              sa.banEvent()

          elif type == "follows":
              sa.followEvent()

          elif type == "streamchange":
              sa.banEvent()

          elif type == "subscription":
              sa.subEvent()

          else:
              sa.followEvent()
        else:
            sa.baseLoop()
            sa.rgb.wait()

        sleep(baseClock)

if __name__ == '__main__':
    baseClock = 1/1000
    q = Queue()
    p = Process(target=led_loop, args=(q,baseClock,))
    p.start()
    app.run(host='0.0.0.0')
    p.join()
