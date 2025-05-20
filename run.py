from app import app
if __name__ == '__main__':
    app.run(debug=True)
    # In run.py (when project.env is in same directory)
load_dotenv('project.env')


# from app import app
# if __name__ == '__main__':
#     app.run(debug=True)
#     # In run.py (when project.env is in same directory)
# load_dotenv('project.env')
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
