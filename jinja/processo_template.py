import jinja2
import yaml
import os


def _get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)

def renderiza_template():
    with open(_get_abs_path('redshift.yml.j2'), 'r') as f:
        redshift_yaml = f.read()

    with open(_get_abs_path('config.yml'), 'r') as f:
        config = yaml.safe_load(f)

    redshift_template = jinja2.Template(redshift_yaml)
    redshift_rendered = redshift_template.render({**config, **os.environ})

    with open(_get_abs_path('redshift.yml'), 'w') as f:
        f.write(redshift_rendered)

renderiza_template()