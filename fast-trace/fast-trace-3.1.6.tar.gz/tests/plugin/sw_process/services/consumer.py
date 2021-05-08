#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import time
import requests
from fast_tracker import agent, config
from fast_tracker.trace.ipc.process import FastProcess
import multiprocessing


def post():
    requests.post("http://provider:9091/users")
    time.sleep(3)


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    config.service_name = 'consumer'
    config.logging_level = 'DEBUG'
    config.flask_collect_http_params = True
    agent.start()

    from flask import Flask, jsonify

    app = Flask(__name__)

    @app.route("/users", methods=["POST", "GET"])
    def application():
        p1 = FastProcess(target=post)
        p1.start()
        p1.join()

        res = requests.post("http://provider:9091/users")

        return jsonify(res.json())

    PORT = 9090
    app.run(host='0.0.0.0', port=PORT, debug=False)
