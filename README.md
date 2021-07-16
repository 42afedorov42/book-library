# book-library
Service for loading, storing and downloading books.

# Install Docker Compose  
https://docs.docker.com/compose/install/    

# Run project
Create a .env file with your credetionals in the book-library directory  
**sudo vim .env**  
SECRET_KEY=django-insecure-#37q)+nzo(pk&4j_4m6x#r=vuzb$xul!(d9#j1w#^^g*o&*-6j  
DJANGO_ALLOWED_HOSTS=*  
POSTGRES_DB=your_db_name  
POSTGRES_USER=your_db_user  
POSTGRES_PASSWORD=your_db_passwod  
POSTGRES_HOST=db  
POSTGRES_PORT=5432     
**sudo docker-compose up**  