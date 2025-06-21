try:
    import openpyxl
except ImportError:
    import subprocess
    import sys
    print("openpyxl no está instalado. Instalándolo ahora...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
