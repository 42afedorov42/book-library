# book-library
Service for loading, storing and downloading books.

# Install Docker Compose  
https://docs.docker.com/compose/install/    

# Run project
Create a .env file with credetionals in the book-library directory  

<pre><code>sudo vim .env<pre><code>
  
SECRET_KEY=django-insecure-#37q)+nzo(pk&4j_4m6x#r=vuzb$xul!(d9#j1w#^^g*o&*-6j  
DJANGO_ALLOWED_HOSTS=*  
POSTGRES_DB=postgres  
POSTGRES_USER=postgres  
POSTGRES_PASSWORD=postgres  
POSTGRES_HOST=db  
POSTGRES_PORT=5432
     
<pre><code>sudo docker-compose up<pre><code>  