from fanstatic import Library
from fanstatic import Resource

library = Library('fontawesome', 'resources')

# CSS
fontawesome = Resource(
    library, 'css/font-awesome.css',
    minified='css/font-awesome.min.css',
)

