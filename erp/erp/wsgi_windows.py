import os
import sys
import site

from django.core.wsgi import get_wsgi_application


activate_this = 'C:/Users/flore/Envs/erp/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(), dict(__file__=activate_this))

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Users/flore/Envs/erp/Lib/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Users/flore/Envs/erp')
sys.path.append('C:/Users/flore/Envs/erp/erp/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'erp.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp.settings")

application = get_wsgi_application()
