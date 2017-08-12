# django-base-project

A base "scaffold" for a new Django (REST) project that some people - but mostly myself - find very handy.
It's now Python 3 only.

### Features
This heavily resembles my favourite workflow and tools, so some things will differ from 'normal' Django projects.
It contains:
- an 'apps' package directory, with a flattened Django base project structure (no repeating project-name);
- a 'settings' package/directory. Base settings are in settings/__init__.py, and can be overridden/expanded in environment-based settings-files, for example settings/development.py. An environment-file containing the name of the environment is expected. See 'getting started' below. I guess it's a bit like `https://code.djangoproject.com/wiki/SplitSettings#SimplePackageOrganizationforEnvironments`, but simpler.
- a 'main' app, containing useful model-mixins and a default viewset;
- an admin list-display for the internal django admin-log (extended Latest Actions stuff);

- basic fabric commands for local development (`fab run`!), see fabfile.py;


### Requirements/dependencies
My base tools, including django-extensions, pip-tools, bpython, fabric3, etc;
Check out https://github.com/nvie/pip-tools if you're unfamiliar with pip-tools. Then have a look at requirements.in for base requirements.
The default development settings contain sqlite3-settings. Change to your liking.

- runserver_plus for development, gunicorn for staging/production;
