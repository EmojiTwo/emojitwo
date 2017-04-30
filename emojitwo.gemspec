Gem::Specification.new do |s|
  s.name        = 'emojitwo'
  s.version     = '2.3'
  s.license     = 'CC-BY-4.0'
  s.summary     = 'Emoji assets for everyone.'
  s.description = 'Emojis in SVG and PNG format based upon Emojione. Emojitwo is a complete set of emojis (as of Unicode 9.0, Emoji 4.0) designed for the web.'
  s.authors     = ['Ranks.com', 'Christoph Päper']
  s.email       = 'emoji@crissov.de'
  s.files       = Dir.glob('svg/*.svg') +
                  Dir.glob('png/*.png') +
                  ['emoji.json'] +
                  ['emojitwo.gemspec']
  s.require_paths = ['']
  s.homepage    = 'http://emojitwo.github.io'
end
