# environment.py
from common import launch_browser

def before_scenario(context, scenario):
    launch_browser(context)
    #launch_browser(context, context.config.userdata.get("browser", "chrome"))

def after_scenario(context, scenario):
    context.driver.quit()
