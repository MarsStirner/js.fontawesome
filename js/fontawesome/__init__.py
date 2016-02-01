from fanstatic import Library
from fanstatic import Resource
from js.angular import angular
from js.bootstrap import bootstrap

library = Library('fontawesome', 'resources')

# CSS
fontawesome = Resource(
    library, 'css/font-awesome.css',
    minified='css/font-awesome.min.css',
    depends=[angular, bootstrap]
)

