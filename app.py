import os
from predict import create_demo

demo = create_demo()

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT",7860))
)
