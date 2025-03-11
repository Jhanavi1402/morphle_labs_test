from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Jhanavi J S"  
    username = os.getenv("USER", "codespace")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    # Run the `top -b -n 1` command and get output
    top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout

    return f"""
    <pre>
    Name: {name}
    User: {username}
    Server Time (IST): {server_time}

    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
