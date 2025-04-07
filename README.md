[![Python application test with Github Actions](https://github.com/mozaloom/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/mozaloom/functions-from-zero/actions/workflows/main.yml)
# functions-from-zero



### To call Microservice 

something like this
'''bash
curl -X 'POST' \
  'http://127.0.0.1:8080/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
'''

### Build Container
'docker build .'
'docker image ls' --> image_id

### Run Container
'docker run -p 127.0.0.1:8080:8080 <image_id>'



