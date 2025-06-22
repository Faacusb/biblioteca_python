import subprocess
import sys

# Actualizar pip
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

# Luego, instalar openpyxl
try:
    import openpyxl
except ImportError:
    print("openpyxl no está instalado. Instalándolo ahora...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    import openpyxl  # Volvemos a intentar importar
