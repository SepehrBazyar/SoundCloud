# SoundCloud
Stream and listen to music online for free with SoundCloud

## How to Run?
### Easy Setup by Docker
```
docker compose up
```
### Installation without Docker
1. Clone the Project
```
git clone https://github.com/SepehrBazyar/SoundCloud.git
```
2. Create a Virtual Environment("venv" is a Selective Name).
```
python3 -m venv venv
```
3. Activate the Interpreter of the Virtual Environment
    * Windows:
    ```
    venv\Script\active
    ```
    * Linux:
    ```
    source venv/bin/active
    ```
4. Install the Requirements
```
pip install -r requirements/production.txt
```
5. Create a `.env` file in root directory and add your created config:
```python
DEBUG = <project-debug-status>
SECRET_KEY = <django-insecure-secret-key>
```
6. After that, migration:
```
python3 manage.py migrate
```
7. Write the Following Command to Run the Server
```
python3 manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
