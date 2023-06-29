from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment
from os.path import join


def render(template_name, folder="templates", **kwargs):
    # file_path = join(folder, template_name)
    # with open(file_path, encoding="utf-8", errors="ignore") as f:
    #     template = Template(f.read())
    # return template.render(**kwargs)
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)
