## Spoelkeuken

De PublicSpaces Spoelkeuken

### Developent

Run migrations after manual editing a DocType's json:

```
bench --site spoelkeuken.localhost migrate
```


### Building

```
ERPNEXT_VERSION=v13 FRAPPE_VERSION=v13 docker buildx bake --push
```


#### Troubleshooting

When MySQL/MariaDB tables crash after altering DocTypes add the following setting to your database server config:

```
[mysqld]
alter_algorithm=copy
```


#### License

MIT