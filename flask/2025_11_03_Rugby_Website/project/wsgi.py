from . import create_app
from ..db_create import db_create

app = create_app()

db_create()

# run_threader()