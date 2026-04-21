from flask import Flask, render_template_string

app = Flask(__name__)

# HTML + CSS for beautiful UI
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Lab App</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            text-align: center;
            animation: fadeIn 1s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        h1 {
            color: #667eea;
            font-size: 3rem;
            margin-bottom: 10px;
        }
        .message {
            font-size: 1.5rem;
            color: #333;
            margin: 20px 0;
            padding: 15px;
            background: #f0f0ff;
            border-radius: 10px;
        }
        .name {
            font-size: 1.2rem;
            color: #764ba2;
            font-weight: bold;
            margin-top: 20px;
            padding-top: 10px;
            border-top: 2px solid #e0e0e0;
        }
        .badge {
            display: inline-block;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8rem;
            margin-top: 15px;
        }
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 25px;
            border-radius: 25px;
            font-size: 1rem;
            cursor: pointer;
            margin-top: 20px;
            transition: transform 0.3s;
        }
        button:hover {
            transform: scale(1.05);
            background: #764ba2;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 DevOps Lab App</h1>
        <div class="message">
            {{ message }}
        </div>
        <div class="name">
            👩‍💻 Naila (FA22-BSE-029)
        </div>
        <div class="badge">
            ✅ Flask | Docker | Kubernetes
        </div>
        <button onclick="location.reload()">🔄 Refresh</button>
    </div>
</body>
</html>
'''

@app.route('/')
def hello():
    return render_template_string(HTML_TEMPLATE, message="Hello DevOps World - Update! 🚀")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)