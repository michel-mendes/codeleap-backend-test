
# CodeLeap Backend Test

CodeLeap Backend Test - A Django REST Framework API for managing CRUD operations.

## Tech Stack

**Server:** Python, Django, Django REST Framework, SQLParse


## API Reference

- #### Get all Posts (10 items pagination)

```http
  GET /posts/?{parameters}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`| `string` | **Optional** Filter posts by user name |
| `search`   | `string` | **Optional** Search for "title" or "content" |
| `ordering` | `string` | **Optional** Available values: "created_datetime", "likes" |

- #### Create new Post 

```http
  POST /posts/
```

| Request body attribute | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`| `string` | Username of the Post owner |
| `title`   | `string` | Post title |
| `content` | `string` | Post content |

- #### Get post

```http
  GET /posts/{id}/
```

- #### Update Post 

```http
  PATCH /posts/{id}/
```

| Request body attribute | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`   | `string` | Post title |
| `content` | `string` | Post content |

- #### Delete Post 

```http
  DELETE /posts/{id}/
```

- #### Like a Post 

```http
  POST /posts/{id}/likes/
```

- #### Unlike a Post 

```http
  DELETE /posts/{id}/likes/
```

- #### Get a Post comments

```http
  GET /posts/{id}/comments/
```

- #### Comment a Post

```http
  POST /posts/{id}/comments/
```
| Request body attribute | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`   | `string` | Comment owner |
| `content` | `string` | Comment content |

- #### Get a Post comment

```http
  GET /posts/{id}/comments/{commentId}/
```

- #### Delete a Post comment

```http
  DELETE /posts/{id}/comments/{commentId}/
```
## Installation

```bash
git clone https://github.com/michel-mendes/codeleap-backend-test.git
cd codeleap-backend-test
python -m venv env
source env/bin/activate   # on Windows use: 'env\Scripts\activate'
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
    
