# Windows Setup for PySpark

This project has been configured to run PySpark on Windows. The following changes were made to ensure compatibility:

## 1. Environment Variables
The `notebooks/03_pyspark_etl.ipynb` notebook has been patched to automatically set the following environment variables at runtime:
- `PYSPARK_PYTHON`: Points to the virtual environment's Python executable.
- `PYSPARK_DRIVER_PYTHON`: Points to the virtual environment's Python executable.
- `HADOOP_HOME`: Points to the local `hadoop` directory in this project.
- `PATH`: Adds `%HADOOP_HOME%\bin` to the system path.

## 2. Hadoop Binaries (Winutils)
A local `hadoop` directory has been created with `bin/winutils.exe` and `bin/hadoop.dll`. These are required for PySpark to perform file system operations on Windows.

## Troubleshooting
If you encounter `SocketTimeoutException` or "Python worker failed to connect back":
1. Ensure you are running the notebook from the `notebooks/` directory.
2. Ensure the `hadoop/bin` directory contains `winutils.exe`.
3. If using a different Python environment, you may need to update the `PYSPARK_PYTHON` path in the notebook.

## References
- [Winutils for Hadoop](https://github.com/cdarlint/winutils)
