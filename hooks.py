import datetime


def on_config(config):
    config.copyright = f"© {datetime.date.today().year} Тряпышко Андрей"
    return config
