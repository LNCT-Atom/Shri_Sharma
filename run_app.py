import os
import sys
import streamlit.web.bootstrap as bootstrap

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(base_dir, "ui", "streamlit_app.py")
    
    # Set arguments for headless desktop launch
    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--global.developmentMode=false",
        "--server.headless=true",
        "--browser.serverAddress=localhost"
    ]
    bootstrap.run(app_path, "", sys.argv[2:], flag_options={})