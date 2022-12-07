requirements: docker, python
using the following libraries: fastapi, uvicorn, pydantic

to run use:
```bash
 docker build -t fastapi_demo .
 docker run -ti -p 8989:8080 fastapi_demo
```

try to add track using curl or browser
```
curl -X 'POST' \
  'http://127.0.0.1:8989/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 0,
  "name": "asdasd",
  "artist": "asdsad",
  "type": "mp3",
  "length": "3:14",
  "size": "12155KB",
  "created": "12/12/2013",
  "path": "/sdad/asddasd/sad.mp3"
}'

 ```
