#    Rackspace Hosting 2014
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import eventlet


def sync_spawn_n(func, *args, **kwargs):
    """Synchronous spawn_n for testing threaded code."""
    func(*args, **kwargs)


class SyncPool(eventlet.GreenPool):
    """Synchronous pool for testing threaded code without adding sleep
    waits.
    """
    def spawn_n(self, func, *args, **kwargs):
        func(*args, **kwargs)