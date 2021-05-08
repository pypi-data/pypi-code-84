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

from skywalking import agent, config

if __name__ == '__main__':
    config.service_name = 'provider'
    config.logging_level = 'DEBUG'
    agent.start()

    from flask import Flask, jsonify
    import redis

    app = Flask(__name__)

    @app.route("/users", methods=["POST", "GET"])
    def application():
        time.sleep(0.5)

        r = redis.StrictRedis(host='redis', port=6379, db=0)

        r.set('foo', 'bar')
        r.get('foo')

        return jsonify({"song": "Despacito", "artist": "Luis Fonsi"})

    PORT = 9091
    app.run(host='0.0.0.0', port=PORT, debug=True)
