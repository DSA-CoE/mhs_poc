# flake8: noqa

'''
This is a global test configuration file. Commonly used to place global fixtures to be shared in tests across apps

See: https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files#:~:text=If%20you%20want%20to%20use,and%20inject%20it%20when%20needed.

Fixtures: 
    Define fixtures for static data used by tests. This data can be accessed by all tests in the suite unless specified otherwise. 
    This could be data as well as helpers of modules which will be passed to all tests.

External plugin loading: 
    conftest.py is used to import external plugins or modules. By defining the following global variable, pytest will load the 
    module and make it available for its test. Plugins are generally files defined in your project or other modules which might be needed in your tests. 
    You can also load a set of predefined plugins as explained here.

    pytest_plugins = "someapp.someplugin"

Hooks: 
    You can specify hooks such as setup and teardown methods and much more to improve your tests. 
    For a set of available hooks, read here. Example:

        def pytest_runtest_setup(item):
        """ called before ``pytest_runtest_call(item). """
        #do some stuff`

'''

# Sample. As see here: https://djangostars.com/blog/django-pytest-testing
# import pytest

# @pytest.fixture
# def auto_login_user(db, client, create_user, test_password):
#    def make_auto_login(user=None):
#        if user is None:
#            user = create_user()
#        client.login(username=user.username, password=test_password)
#        return cliimport pytest


# @pytest.fixture
# def auto_login_user(db, client, create_user, test_password):
#    def make_auto_login(user=None):
#        if user is None:
#            user = create_user()
#        client.login(username=user.username, password=test_password)
#        return client, user
#    return make_auto_loginent, user
#    return make_auto_login
