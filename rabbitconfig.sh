# add user
sudo rabbitmqctl add_user worker worker

# add new virtual host
sudo rabbitmqctl add_vhost rabbithost

# set permissions for user on vhost
sudo rabbitmqctl set_permissions -p rabbithost user ".*" ".*" ".*"

# restart rabbit
sudo rabbitmqctl restart
