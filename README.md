## File uploader service backend

This is a simple file uploader service backend. It is written in python and uses FastAPI as the web framework.

### How to run

1. Install the dependencies

```bash
pip install -r requirements.txt

```
3. Create a .env file and add the following variables    
```bash
API_KEY=<your_api_key>
```

4. Run the server

```bash
./start.sh
```

5. Stop the server

```bash
./stop.sh
```

### How to use

1. Upload a file


```bash
curl -F "file=@/path/to/file" \
    'http://<host><port>:8083/upload?dir=<directory>&name_of_file=<name_of_file>' \
    -H "API_KEY: <your_api_key>"
```

2. GET a file

```bash
curl -X 'GET' \
  'http://<host>:<port>/<path_to_file>' \
```

3. Delete a file

```bash
curl -X 'DELETE' \
    'http://<host>:<port>/files/delete?file=<file_name>&dir=<directory>' \
    -H 'API_KEY: <your_api_key>'
    -H 'accept: application/json'

```
4. GET a list of files

```bash
curl -X 'GET' \
    'http://<host>:<port>/files?dir=<directory>&file=<file_name>' \
    -H 'API_KEY: <your_api_key>'
    -H 'accept: application/json'
```
