from webbot import Browser
import os

user = os.environ.get("urjc_user")
pass_ = os.environ.get("urjc_pass")

web = Browser()

web.go_to("https://www.aulavirtual.urjc.es/moodle/login/index.php")
web.type(user, into = "username")
web.type(pass_, into ="password")
web.click(id = "loginbtn")













