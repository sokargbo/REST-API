```python
from flask import Flask
import mySecrets ## You can import any file!

app = Flask(__name__)

## Call it like a module.
my_name = mySecrets.username
my_password = mySecrets.password

@app.route('/')
def hello():
	return "Hello, " + my_name + ", welcome to " + my_password

if __name__ == '__main__':
	app.run(debug=True)
