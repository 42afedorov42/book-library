## book-library
Service for loading, storing and downloading books.

### Install Docker Compose  
https://docs.docker.com/compose/install/  
for linux 
<pre><code>sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose</code></pre> 
<pre><code>sudo chmod +x /usr/local/bin/docker-compose</code></pre>

# Run project
<p>Сredetionals in the .env file.
If you have another base in postgres - change them.<br>
PostgreSQL with postgres database is used by default.</p>  
<pre><code> sudo docker-compose up</code></pre>

### Create superuser
<pre><code>docker exec -it book-library_web python manage.py createsuperuser</code></pre> 