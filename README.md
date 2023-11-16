# Elegancia A La Mode API

doc:
- https://eleganciaalamode-api.onrender.com/api/docs/

# Diagram
![tables](https://files.catbox.moe/cdvtpg.png)


# ROUTES

# Users
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
