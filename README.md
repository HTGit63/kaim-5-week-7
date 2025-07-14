
# kaim-5-week-7

## Setup

1. **Copy `.env.example` to `.env`** and fill in your credentials:
   - `API_ID`: Your Telegram API ID.
   - `DB_PASSWORD`: Your PostgreSQL database password.
   
2. **Build and start services**:
   Navigate to the `docker` directory and start the services with Docker Compose:
   ```bash
   cd docker
   docker-compose up --build -d
   ```

3. **Running the Scraper**:
   After the containers are up, you can run the Telegram scraper to collect data. Ensure that the scraper uses the correct credentials from the `.env` file.

4. **Running dbt**:
   To run the dbt models and tests, execute the following commands from the root of the project:
   ```bash
   dbt run --project-dir /app/files --profiles-dir /app/files
   dbt test --project-dir /app/files --profiles-dir /app/files
   ```

5. **Viewing dbt Documentation**:
   If you're able to generate dbt docs (optional step if `dbt docs generate` works), use the following command to view the docs:
   ```bash
   dbt docs generate --project-dir /app/files --profiles-dir /app/files
   dbt docs serve --project-dir /app/files --profiles-dir /app/files
   ```

---

### Notes:

- **Docker Setup**: This project uses Docker to spin up both the PostgreSQL and Python environments. All necessary services and configurations are defined in `docker-compose.yml` and the Dockerfile.
- **Database**: The raw data is loaded into a PostgreSQL database, and the dbt models clean and test this data.
- **dbt**: The dbt models are placed under the `dbt_project/models/` directory. The main focus is the staging model `stg_telegram_messages.sql`.