Copy acc-example dir

Change profile account, password and options

```python
insta_username  = '' # instagram username
insta_password  = '' # instagram password
```

Change docker-schedule service names and environment

```yaml
version: '3'
services:
  instapy-{{myAccountName}}-schedule:
    container_name: instapy-{{myAccountName}}-schedule
    command: ["./wait-for-selenium.sh", "http://selenium-instapy-{{myAccountName}}-schedule:4444/wd/hub", "--", "python", "/personal/instapy-schedule.py"]
    environment:
      - PYTHONUNBUFFERED=0
      - SELENIUM_URL=selenium-instapy-{{myAccountName}}-schedule
    build:
      context: .
      dockerfile: ./Dockerfile
    restart: on-failure
    depends_on:
      - selenium-instapy-{{myAccountName}}-schedule
    volumes:
      - ./../logs:/code/logs
      - ./../../InstaPy:/code
      - ./:/personal
  selenium-instapy-{{myAccountName}}-schedule:
    container_name: instapy-selenium-chrome-instapy-{{myAccountName}}-schedule
    image: selenium/standalone-chrome
    shm_size: 512M
```