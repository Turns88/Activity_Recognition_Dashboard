from dashboard import create_app

from views import mainbp  # Import the blueprint from views.py

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)




