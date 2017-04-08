from flask_assets import Bundle, Environment

js_assets = Bundle(
    'js/application.js',
    filters='jsmin',
    output='build/packed.js'
)

css_assets = Bundle(
    'css/lib/normalize.css',
    'css/lib/skeleton.css',
    'css/custom.css',
    filters='cssmin',
    output='build/packed.css'
)

assets = Environment()

assets.register('js_all', js_assets)
assets.register('css_all', css_assets)
