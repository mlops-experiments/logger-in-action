## 📁 Setup and Structure

### Step: Package Management

- Write the setup for importing local packages in `setup.py` and `pyproject.toml` files.
- **Tip**: Learn more about these files from `crashcourse.txt`.

### Step: Virtual Environment and Dependencies

- Create a virtual environment and install required dependencies from `requirements.txt`:
  ```bash
  conda create -n vehicle python=3.10 -y
  conda activate vehicle
  pip install -r requirements.txt
  ```
- Verify the local packages by running:
  ```bash
  pip list
  ```

## 📝 Logging, Exception Handling

### Step: Set Up Logging and Exception Handling

- Understand logging concepts with file handler and console handler
- Create logging handling modules. Test on a demo file `demo_logger.py`.

### Step: Set Up Exception Handling

- Create exception handling modules. Test on a demo file `demo_exception.py`
