# This manifest installs and configures nginx

  exec { 'apt-update':
    command  => 'sudo /usr/bin/apt-get update',
    provider => shell,
  }

  exec { 'install-nginx':
    command  => 'sudo /usr/bin/apt-get install -y nginx',
    provider => shell,
    require  => Exec['apt-update'],
  }

  exec { 'create-index':
    command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
    provider => shell,
    require  => Exec['install-nginx'],
  }

  exec { 'add-redirect':
    command  => 'sudo sed -i "s/server_name _;/server_name _;\\n\\trewrite ^\/redirect_me https:\/\/stackoverflow.com permanent;/" /etc/nginx/sites-enabled/default',
    provider => shell,
    require  => Exec['create-index'],
  }

  exec { 'create-404':
    command  => 'echo "Ceci n\'est pas une page" | sudo tee /var/www/html/404.html',
    provider => shell,
    require  => Exec['add-redirect'],
  }

  exec { 'configure-nginx':
    command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\terror_page 404 \/404.html;\\n\\tlocation = \/404.html {\\n\\t\\troot \/var\/www\/html;\\n\\t}/" /etc/nginx/sites-enabled/default',
    provider => shell,
    require  => Exec['create-404'],
  }

  exec { 'response-header':
    command  => 'sudo sed -i "s/server_name _;/server_name _;\\n\\tadd_header X-Served-By \\$hostname;/" /etc/nginx/sites-enabled/default',
    provider => shell,
    require  => Exec['configure-nginx'],
  }

  exec { 'restart-nginx':
    command  => 'sudo /etc/init.d/nginx restart',
    provider => shell,
    require  => Exec['response-header'],
  }
