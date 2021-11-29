## Spoelkeuken

De PublicSpaces Spoelkeuken

### Developent

Run migrations after manual editing a DocType's json:

```
bench --site spoelkeuken.localhost migrate
```


#### Troubleshooting

When MySQL/MariaDB tables crash after altering DocTypes add the following setting to your database server config:

```
[mysqld]
alter_algorithm=copy
```


#### License

MIT