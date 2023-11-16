# Elegancia A La Mode API

doc:
- https://eleganciaalamode-api.onrender.com/api/docs/

# Diagram
![tables](https://files.catbox.moe/cdvtpg.png)


# ROUTES

## USERS
GET https://eleganciaalamode-api.onrender.com/api/users/

Header: AUTHORIZATION BEARER ADMIN TOKEN

Body: NONE

response:
<details>
  
```
[
	{
		"id": 1,
		"username": "Test",
		"email": "test@test.com",
		"name": "Test",
		"is_superuser": true,
		"orders": [
			{
				"id": 1,
				"is_paid": true,
				"date_paid": "2023-11-15",
				"user": 1
			}
		],
		"comments": [
			{
				"id": 1,
				"content": "Great product, love the quality!",
				"rating": 8,
				"product_name": "white shirt",
				"user_name": "Test"
			}
		]
	},
	{
		"id": 2,
		"username": "Kenzie",
		"email": "kenzie@test.com",
		"name": "Kenzie",
		"is_superuser": false,
		"orders": [
			{
				"id": 2,
				"is_paid": true,
				"date_paid": "2023-11-15",
				"user": 2
			}
		],
		"comments": [
			{
				"id": 2,
				"content": "Awesome skirt, fits perfectly!",
				"rating": 8,
				"product_name": "super skirt",
				"user_name": "Kenzie"
			}
		]
	},
]
```
</details>

POST https://eleganciaalamode-api.onrender.com/api/users/

Header: NONE

Body:
<details>
  
```
{
	"username": "Samuel",
	"email": "samuel@kenzie.com",
	"name": "Samuel Oliveira",
	"password": "12345",
	"is_superuser": true
}
```
</details>

response:
<details>
  
```
{
	"id": 1,
	"username": "Samuel",
	"email": "samuel@kenzie.com",
	"name": "Samuel Oliveira",
	"is_superuser": true,
	"orders": [],
	"comments": []
}
```
</details>

POST https://eleganciaalamode-api.onrender.com/api/login/

Header: NONE

Body:
<details>
  
```
{
	"username": "Mauricio",
	"password": "12345"
}
```
</details>

response:
<details>
  
```
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMDE2NDQ5NSwiaWF0IjoxNzAwMDc4MDk1LCJqdGkiOiJlMmU1ZDdiZjRkZGQ0MDFjOTUwZmMxNDk3MTU1NTViNSIsInVzZXJfaWQiOjV9.QqYtgSrLIsLITIPrFkptLrMpzkEq7__DRhjLa2_UorQ",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwMDkyNDk1LCJpYXQiOjE3MDAwNzgwOTUsImp0aSI6ImQxMWMwMDU2ZGU1MjRmOWQ5M2U2NWIwMDg5NTk4ZmQ4IiwidXNlcl9pZCI6NX0.EP83VN7G7B06AJF2kXMQR5ocBqNnIXtuA7oVc_K9Wjg"
}
```
</details>

GET https://eleganciaalamode-api.onrender.com/api/users/<USER_ID>/

Header: AUTHORIZATION BEARER TOKEN ADMIN - (or your own logged account token and user_id matches)

Body: NONE

response:
<details>
  
```
{
	"id": 1,
	"username": "Test",
	"email": "test@test.com",
	"name": "Test",
	"is_superuser": true,
	"orders": [
		{
			"id": 1,
			"is_paid": true,
			"date_paid": "2023-11-15",
			"user": 1
		}
	],
	"comments": [
		{
			"id": 1,
			"content": "Great product, love the quality!",
			"rating": 8,
			"product_name": "white shirt",
			"user_name": "Test"
		}
	]
}
```
</details>

PATCH https://eleganciaalamode-api.onrender.com/api/users/<USER_ID>/

Header: AUTHORIZATION BEARER TOKEN ADMIN - (or your own logged account token and user_id matches)

Body:
<details>
  
```
{
	"username": "Mauricio changed",
	"email": "mauricio@kenzie.com",
	"name": "Mauricio Oliveira changed"
}
```
</details>

response:
<details>
  
```
{
	"id": 3,
	"username": "Mauricio changed",
	"email": "mauricio@kenzie.com",
	"name": "Mauricio Oliveira changed",
	"is_superuser": false,
	"orders": [],
	"comments": []
}
```
</details>

DELETE https://eleganciaalamode-api.onrender.com/api/users/<USER_ID>/

Header: AUTHORIZATION BEARER TOKEN ADMIN - (or your own logged account token and user_id matches)

Body: NONE

response: status 200 ok

## ORDERS

POST https://eleganciaalamode-api.onrender.com/api/user/buy/

Header: AUTHORIZATION BEARER TOKEN

Body:
<details>
  
```
{
	"is_paid": true,
	"items_bought": [
		{
			"product_name": "white shirt",
			"product_price": 9999.00,
			"quantity": 2
		}
	]
}
```
</details>

response:
<details>
  
```
{
	"user_id": 1,
	"is_paid": true,
	"date_paid": "2023-11-16",
	"items_bought": [
		{
			"order": 8,
			"product_name": "blue coat",
			"product_price": 9999.0,
			"quantity": 4
		}
	]
}
```
</details>

GET https://eleganciaalamode-api.onrender.com/api/orders/

Header: AUTHORIZATION BEARER TOKEN ADMIN

Body: NONE

response:
<details>
  
```
[
	{
		"id": 1,
		"user_id": 1,
		"is_paid": true,
		"date_paid": "2023-11-15",
		"items_bought": [
			{
				"order": 1,
				"product_name": "white shirt",
				"product_price": 9999.0,
				"quantity": 2
			}
		]
	},
	{
		"id": 2,
		"user_id": 2,
		"is_paid": true,
		"date_paid": "2023-11-15",
		"items_bought": [
			{
				"order": 2,
				"product_name": "super skirt",
				"product_price": 9999.0,
				"quantity": 1
			},
			{
				"order": 2,
				"product_name": "blue coat",
				"product_price": 9999.0,
				"quantity": 1
			}
		]
	},
]
```
</details>

## PRODUCTs

GET https://eleganciaalamode-api.onrender.com/api/products/

Accepted queries: 
- search (will look for word in name or keyword)
- category
- collection
- sale (true or false)
- spotlight (true or false)

example: https://eleganciaalamode-api.onrender.com/api/products?search=shirt

or by product ID with:

https://eleganciaalamode-api.onrender.com/api/products/<PRODUCT_ID>/

Header: NONE

Body: NONE

response:
<details>
  
```
[
	{
		"id": 1,
		"name": "white shirt",
		"slug": "whiteshirt",
		"price": 9999.99,
		"stock": 10,
		"category": "shirt",
		"visit_number": 0,
		"collection": "summer",
		"sale": false,
		"spotlight": false,
		"keywords": [
			{
				"entry": "shirt"
			},
			{
				"entry": "white"
			},
			{
				"entry": "summer"
			},
			{
				"entry": "light"
			}
		],
		"style": {
			"url": "https://picsum.photos/200"
		},
		"comments": [
			{
				"id": 1,
				"content": "Great product, love the quality!",
				"rating": 8,
				"product_name": "white shirt",
				"user_name": "Test"
			},
			{
				"id": 7,
				"content": "Nice white shirt, fits well!",
				"rating": 8,
				"product_name": "white shirt",
				"user_name": "Mauricio"
			},
			{
				"id": 8,
				"content": "Superb white shirt, excellent quality!",
				"rating": 8,
				"product_name": "white shirt",
				"user_name": "Monica"
			}
		]
	},
]
```
</details>

POST https://eleganciaalamode-api.onrender.com/api/products/

Header: AUTHORIZATION BEARER TOKEN ADMIN

Body:
<details>

```
{
	"name": "white suit",
  	"slug": "whitesuit",
  	"price": 9999.00,
  	"stock": 1,
  	"category": "suit",
  	"visit_number": 0,
  	"collection": "winter",
  	"sale": false,
  	"spotlight": false,
	"style": {
		"url": "www.whitesuit.com"
	},
	"keywords": [
		{
			"entry": "white"
		},
		{
			"entry": "suit"
		},
				{
			"entry": "light"
		},
				{
			"entry": "winter"
		},
				{
			"entry": "party"
		},
				{
			"entry": "normal"
		}
	]
}
```
</details>

response:
<details>
  
```
{
	"id": 1,
	"name": "white suit",
	"slug": "whitesuit",
	"price": 9999.0,
	"stock": 1,
	"category": "suit",
	"visit_number": 0,
	"collection": "winter",
	"sale": false,
	"spotlight": false,
	"keywords": [
		{
			"entry": "white"
		},
		{
			"entry": "light"
		},
		{
			"entry": "party"
		},
		{
			"entry": "suit"
		},
		{
			"entry": "winter"
		},
		{
			"entry": "normal"
		}
	],
	"style": {
		"url": "www.whitesuit.com"
	},
	"comments": []
}
```
</details>

PATCH https://eleganciaalamode-api.onrender.com/api/products/<PRODUCT_ID>/

Header: AUTHORIZATION BEARER TOKEN ADMIN

Body:
<details>

```
{
	"name": "white suit changed",
	"slug": "whitesuitchanged",
	"stock": 0,
	"visit_number": 50,
	"sale": true,
	"spotlight": false,
	"keywords": [
		{
			"entry": "black"
		},
		{
			"entry": "special"
		},
		{
			"entry": "elegant"
		}
	],
	"style": {
		"url": "www.whitesuitchanged.com"
	}
}
```
</details>

response:
<details>
  
```
{
	"id": 4,
	"name": "white suit changed",
	"slug": "whitesuitchanged",
	"price": 9999.0,
	"stock": 0,
	"category": "suit",
	"visit_number": 50,
	"collection": "winter",
	"sale": true,
	"spotlight": false,
	"keywords": [
		{
			"entry": "special"
		},
		{
			"entry": "black"
		},
		{
			"entry": "elegant"
		}
	],
	"style": {
		"url": "www.whitesuitchanged.com"
	},
	"comments": []
}
```
</details>

DELETE https://eleganciaalamode-api.onrender.com/api/products/<PRODUCT_ID>/

Header: AUTHORIZATION BEARER TOKEN ADMIN

Body: NONE

response: status 200 ok

## COMMENTS

GET https://eleganciaalamode-api.onrender.com/api/comments/

Header: NONE

Body: NONE

response:
<details>
  
```
[
	{
		"id": 1,
		"content": "Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat",
		"rating": 5,
		"product_name": "white shirt",
		"user_name": "Fernanda Oliveira"
	},
	{
		"id": 2,
		"content": "Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat",
		"rating": 10,
		"product_name": "white shirt",
		"user_name": "Mauricio Oliveira"
	},
]
```
</details>

POST https://eleganciaalamode-api.onrender.com/api/comments/<COMMENT_ID>/

Header: AUTHORIZATION BEARER TOKEN

Body:
<details>

```
{
	"content": "Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat",
	"rating": 10
}
```
</details>

response:
<details>
  
```
{
	"id": 5,
	"content": "Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat",
	"rating": 10,
	"product_name": "black suit",
	"user_name": "Samuel Oliveira"
}
```
</details>

PATCH https://eleganciaalamode-api.onrender.com/api/comments/<COMMENT_ID>

Header: AUTHORIZATION BEARER TOKEN

Body:
<details>
	
```
{
	"rating": 4,
	"product_name": "blablabla",
	"content": " all changed"
}
```
</details>

response:
<details>
  
```
{
	"id": 1,
	"content": "all changed",
	"rating": 4,
	"product_name": "white shirt",
	"user_name": "Fernanda Oliveira"
}
```
</details>

DELETE https://eleganciaalamode-api.onrender.com/api/comments/<COMMENT_ID>/

Header: AUTHORIZATION BEARER TOKEN ADMIN or Comment made by the user

Body: NONE

response: status 200 ok
