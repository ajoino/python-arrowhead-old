from source.arrowhead_system import ArrowheadSystem
from source.service_provider import ServiceProvider
from flask import request
import datetime

time_format = "%H:%M:%S"
def current_time():
    return str(datetime.datetime.now().strftime(time_format))

class AdvancedTimeProvider(ServiceProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time_format = "%H:%M:%S"
        self.add_route('/current_time', self.current_time)
        self.add_route('/format', self.change_format, ['POST'])

    def current_time(self):
        return str(datetime.datetime.now().strftime(self.time_format))

    def change_format(self):
        self.time_format = request.form['fmt']
        return self.time_format
        #print(request.form)
        #self.time_format = fmt

if __name__ == '__main__':
    service_registry = ArrowheadSystem('Service registry', '127.0.0.1', '8442')
    time_system = ArrowheadSystem('Time', '127.0.0.1', '1337')
    time_provider = AdvancedTimeProvider('Time', service_uri='/Time', provider_system=time_system, consumer_system=None, service_registry=service_registry)
    time_provider.run(auth=False)

