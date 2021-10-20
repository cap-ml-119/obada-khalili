# yata - Yet Another Todo App 😃

Simple Flask To-Do app serving RESTful endpoints to manipulate a set of todos maintained in server's memory.

# Running Locally, and API Docs

## Running yata via Docker

- First, build the image with:

```sh
docker build -t yata .
```

- Then run the image:

```sh
docker run -dp 8081:8081 yata
```

## API Docs

### Retrieve To-Do's

- Endpoint: `GET /api/v1/todos`.
- Response: `[{ title: string, status: "PENDING" | "DONE" | "CANCELED" }]`, 200 status.

### Create To-Do

- Endpoint: `POST /api/v1/todos`.
- Request body schema: `{ title: string }`.
- Responses:
  - 200 status.
  - "Invalid JSON body. Should contain 'title'", 400 status.
  - "Internal server error", 500 status.

### Update To-Do

- Endpoint: `PATCH /api/v1/todos/:uid`.
- Request body schema: `[{ title?: string, status?: "PENDING" | "DONE" | "CANCELED" }]`.
- Responses:
  - 200 status.
  - "Todo doesn't exist", 400 status.
  - "Internal server error", 500 status.

### Delete To-Do

- Endpoint: `DELETE /api/v1/todos/:uid`.
- Responses:
  - 200 status.
  - "Todo doesn't exist", 400 status.
  - "Internal server error", 500 status.
