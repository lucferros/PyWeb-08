from .settings import *

DEBUG = True
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['http://ec2-54-213-12-141.us-west-2.compute.amazonaws.com/', 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
