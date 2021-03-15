import os
from config import app,api
from api.Dataset import Dataset

api.add_resource(Dataset,'/api/dataset')


if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5004, debug=True)