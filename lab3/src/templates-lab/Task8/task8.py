# import Jinja2 library and PyYAML
from jinja2 import Environment, FileSystemLoader
import yaml
# Declare template environment
ENV = Environment(loader=FileSystemLoader('.'))
def get_interface_speed(interface_name):
    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100

ENV.filters['get_interface_speed'] = get_interface_speed
template = ENV.get_template("template-task8.j2")
# We load our YAML file and pass it in to the template when rendering it.
with open("data-task7.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)
    print(template.render(interface_list=interfaces))
