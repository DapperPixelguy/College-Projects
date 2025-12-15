from . import create_app
from .keepalive import run_threader

app = create_app()

# run_threader()