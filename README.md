# flask-api
Build a simple api with flask - python
```
git clone https://github.com/Yukie-Billal/flask-api.git
```
## Run app
```
python3 venv .venv
flask-api/.venv/Scripts/activate

pip install flask
pip install validator
```

Then run the application

```
flask run
```
it will be created host on `127.0.0.1:5000` for default

## Access the api
### use curl
open your terminal or cmd (Recomended)
Then use curl
```
curl -X GET http://localhost:5000 -i
```
and curl will display the return value in file ``api.py`` on the last line
