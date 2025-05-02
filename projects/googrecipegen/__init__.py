#Blueprint init for googrecipegen aka qook
from flask import Blueprint

bp = Blueprint(
    'googrecipegen',                    
    __name__,                  
    template_folder='templates',
    static_folder='static'
)

from . import routes       