build-dev:
  hugo --environment development

build:
  hugo --environment production

dev:
  rm -rf public
  hugo server --buildDrafts --noHTTPCache --disableFastRender --environment='development' --bind 0.0.0.0
