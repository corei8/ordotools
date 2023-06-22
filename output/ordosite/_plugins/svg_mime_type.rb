# Source https://stackoverflow.com/questions/13687030/how-do-i-configure-jekyll-to-serve-svg
require 'webrick'
include WEBrick
WEBrick::HTTPUtils::DefaultMimeTypes.store 'svg', 'image/svg+xml'
