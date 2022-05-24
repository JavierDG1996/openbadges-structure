# openbadges-structure
## Título
```sh
sudo docker-compose up -d
```

```sh
sudo docker-compose exec badgrserver python manage.py migrate
```

```sh
sudo docker-compose exec badgrserver python manage.py dist
```

```sh
sudo docker-compose exec badgrserver python manage.py collectstatic
```

```sh
sudo docker-compose exec badgrserver python manage.py createsuperuser
```

```sh
badgr.ui:4200
http://badgr.ui:4200
http://badgr.ui:4200/signup/
http://badgr.ui:4200/auth/login/
http://badgr.ui:4200/change-password/
http://badgr.ui:4200/auth/login/
http://badgr.ui:4200/signup/success/
http://badgr.ui:4200/signup/
http://badgr.ui:4200/profile/
http://badgr.ui:4200/public/
```

```sh
rw:profile rw:issuer rw:backpack
```

```sh
localStorage.setItem('config',JSON.stringify({api:{baseUrl:"http://localhost:8080"}}))
```

* Superuser moodle:
  * User: user
  * Passwd: bitnami

```sh
http://api.badgr.io/v2
http://badgr.io
```

```sh
ui:4200
http://badgr.ui:4200
http://badgr.ui:4200/signup/
http://badgr.ui:4200/auth/login/
http://badgr.ui:4200/change-password/
http://badgr.ui:4200/auth/login/
http://badgr.ui:4200/signup/success/
http://badgr.ui:4200/signup/
http://badgr.ui:4200/profile/
http://badgr.ui:4200/public/
```

```sh
sudo docker-compose exec mariadb bash
```

```sh
mysql -u bn_moodle
```

```sh
use bitnami_moodle
```

```sh
select * from mdl_user_preferences;
```

```sh
http://localhost:8081/badges/backpackemailverify.php?data=UDrz2QJmkterrKA
```