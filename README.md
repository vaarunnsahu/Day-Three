### **Multi-Container Flask + PostgreSQL App using Docker Compose**  

This project demonstrates how to deploy a **Flask** application with a **PostgreSQL** database using **Docker Compose**. It simplifies managing multi-container applications by defining everything in a single `docker-compose.yml` file.  

---

## **📌 Features**
✅ Containerized **Flask** application  
✅ Persistent **PostgreSQL** database using Docker volumes  
✅ Secure **environment variables** for database credentials  
✅ **Health checks** to ensure dependencies start correctly  
✅ Easily scalable & configurable  

---

## **📁 Project Structure**
```
project-folder/
│── app/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│── docker-compose.yml
│── .env
│── README.md
```
- **`app/`** → Contains Flask application code  
- **`Dockerfile`** → Defines how to build the Flask app container  
- **`docker-compose.yml`** → Defines and runs multi-container setup  
- **`.env`** → Stores environment variables securely  

---

## **🚀 Getting Started**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/project-folder.git
cd project-folder
```

### **2️⃣ Set Up Environment Variables**
Create a `.env` file in the root directory and add:  
```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=mydatabase
```

### **3️⃣ Build & Run the Containers**
```bash
docker-compose up --build
```
This will:  
✅ Build and start **Flask & PostgreSQL** containers  
✅ Automatically link services  
✅ Ensure database persistence  

### **4️⃣ Stop Containers**
To stop and remove containers, use:  
```bash
docker-compose down
```

---

## **🛠️ Configuration**
Modify `docker-compose.yml` as needed:  
```yaml
app:
  environment:
    - DATABASE_URL=postgresql://postgres:password@db:5432/mydatabase

db:
  image: postgres:13
  environment:
    POSTGRES_USER: postgres
    POSTGRES_PASSWORD: password
    POSTGRES_DB: mydatabase
  volumes:
    - db_data:/var/lib/postgresql/data
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U postgres"]
    interval: 10s
    retries: 5

volumes:
  db_data:
```

---

## **📌 Flask Application**
The Flask app (`app/app.py`) connects to PostgreSQL and runs on **port 5000**.  
```python
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## **📌 Useful Commands**
| Command | Description |
|---------|-------------|
| `docker-compose up --build` | Build & run the containers |
| `docker-compose down` | Stop and remove all containers |
| `docker ps` | List running containers |
| `docker logs <container_id>` | View logs for a container |
| `docker exec -it <container_id> bash` | Access a running container |

---

## **📌 Next Steps**
🔹 Add **NGINX** as a reverse proxy  
🔹 Deploy on **AWS/GCP** using **ECS/Kubernetes**  
🔹 Implement **CI/CD pipelines**  

---

## **📜 License**
This project is licensed under the MIT License.  

