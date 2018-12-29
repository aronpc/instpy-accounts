### Prerequisites

```
docker
docker-compose
```

### Installing

```bash
git clone git@github.com:aronpc/instpy-accounts.git
cd instpy-accounts
git submodule init
```

## Configure 
Copy acc-example dir

```bash
cp -rv accounts/acc-example accounts/new-account-name
cd accounts/new-account-name
```

Change in accounts/new-account-name/profile.py account, password and options

```python
insta_username  = '' # instagram username
insta_password  = '' # instagram password
```

Change options in accounts/new-account-name/instapy-schedule.py 

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

## Running 
```bash
docker-compose -f docker-schedule.yml up --build --force-recreate -d
```