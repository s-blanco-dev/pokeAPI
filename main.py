from __init__ import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # IMPORTANTE: host="0.0.0.0" para que Docker lo exponga

