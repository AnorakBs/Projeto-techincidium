import subprocess
import sys
import os
from dotenv import load_dotenv

load_dotenv()

script_postgres = os.getenv("POSTGRES_EXT")
script_csv = os.getenv("CSV_EXT")
script_mysql = os.getenv("MYSQL_LOAD")

start_date = sys.argv[1]
end_date = sys.argv[2]
conf_file = sys.argv[3]
    
result1 = subprocess.run(["python", script_postgres, start_date, end_date, conf_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result1.returncode == 0:
    print("First script ran successfully with arguments.")
else:
    print("First script failed to run. Check Logs")

result2 = subprocess.run(["python", script_csv, start_date], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result2.returncode == 0:
        print("Second script ran successfully.")
else:
    print("Second script failed to run. Check Logs")


if result1.returncode == 0 and result2.returncode == 0:
    print("Step 1 completo executando Step2...")
    result3 = subprocess.run(["python", script_mysql, start_date, end_date], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result3.returncode == 0:
         print("Third script ran successfully.")
    else:
        print("Third script failed to run. Check Logs")
else:
     print("Step 1 failed ending pipeline")