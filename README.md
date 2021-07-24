## book-library
Service for loading, storing and downloading books.

### Install Docker Compose  
https://docs.docker.com/compose/install/    

# Run project
<p>Сredetionals in the .env file.
If you have another base in postgres - change them.</p>  
<pre><code> sudo docker-compose up</code></pre>

### Create superuser
<pre><code>docker exec -it book-library_web python manage.py createsuperuser</code></pre> 