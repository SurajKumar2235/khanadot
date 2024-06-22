
# Restaurant Management Django REST API

This Django project implements a REST API for managing restaurants, users, orders, and authentication.

## API Endpoints

### Authentication

#### 1. **Signup**
- **URL:** `/signup/`
- **Method:** POST
- **Description:** Allows users to register with the system. Requires username, email, password, and user type (restaurant owner or delivery person).
- **Parameters:**
  - `username` (string, required)
  - `name` (string, required)
  - `email` (string, required)
  - `password` (string, required)
  - `user_type` (string, required)
  - `aadhaar_number` (string, optional)
- **Response:** Returns JSON with success message or error.
- **Example:** 
- 1
   -  {
   - "username": "abhishek",
   - "name":"Abhishek",
   - "phone_number":"3456786578",
   - "address":"gujarat",
   - "email": "kushvahaabhisek33@gmail.com",
   - "password": "abc",
   - "user_type": "customer",
   - "date_of_birth":"1990-01-01"
   - }
- 2
   - {
   - "username": "delivery123",
   - "name": "Delivery Person",
   - "phone_number":"3456786578",
   - "address":"gujarat",
   - "email": "delivery@example.com",
   - "password": "securepassword",
   - "user_type": "delivery_person",
   - "aadhaar_number": "123456789012",
   - "vehicle_details": "Bike"
   - }
- 3
   -  {
   - "username": "owner123",
   - "name": "Owner Name",
   - "phone_number":"3456786578",
   - "address":"gujarat",
   - "email": "owner@example.com",
   - "password": "securepassword",
   - "user_type": "restaurant_owner",
   - "aadhaar_number":"1234 5678 9101",
   - }
   - 
#### 2. **Login**
- **URL:** `/login/`
- **Method:** POST
- **Description:** Allows users to authenticate and obtain an access token.
- **Parameters:**
  - `email` (string, required)
  - `password` (string, required)
- **Response:** Returns JSON with success message on successful login or error message.

#### 3. **Logout**
- **URL:** `/logout/`
- **Method:** POST
- **Description:** Logs out the currently authenticated user.
- **Authorization:** Bearer Token (required)
- **Response:** Returns JSON with success message.

### User Profile

#### 5. **User Profile**
- **URL:** `/profile/`
- **Method:** GET
- **Description:** Retrieves the profile information of the currently authenticated user.
- **Authorization:** Bearer Token (required)
- **Response:** Returns JSON with username, email, and user type.

### Restaurant Management

#### 6. **List Restaurants**
- **URL:** `/restaurants/`
- **Method:** GET
- **Description:** Retrieves a list of all restaurants.
- **Response:** Returns JSON array of restaurant objects with id and name.

#### 7. **Restaurant Detail**
- **URL:** `/restaurant/<restaurant_id>/`
- **Method:** GET
- **Description:** Retrieves details of a specific restaurant.
- **Parameters:**
  - `restaurant_id` (integer, required)
- **Response:** Returns JSON object with restaurant id, name, and description.

#### 8. **Menu Items**
- **URL:** `/menu/<restaurant_id>/`
- **Method:** GET
- **Description:** Retrieves menu items for a specific restaurant.
- **Parameters:**
  - `restaurant_id` (integer, required)
- **Response:** Returns JSON array of menu item objects with id, name, and price.

### Order Management

#### 9. **Place Order**
- **URL:** `/order/place/<restaurant_id>/`
- **Method:** POST
- **Description:** Allows placing an order at a specific restaurant.
- **Parameters:**
  - `restaurant_id` (integer, required)
- **Request Body:**
  ```json
  {
      "delivery_address": "string",
      "items": [item_id1, item_id2, ...]
  }
  ```
- **Authorization:** Bearer Token (required)
- **Response:** Returns JSON with order details including order id and total amount.

#### 10. **Order Confirmation**
- **URL:** `/order/<order_id>/`
- **Method:** GET
- **Description:** Retrieves details of a specific order.
- **Parameters:**
  - `order_id` (integer, required)
- **Authorization:** Bearer Token (required)
- **Response:** Returns JSON with order id, total amount, and order date.

#### 11. **Order History**
- **URL:** `/orders/history/`
- **Method:** GET
- **Description:** Retrieves order history for the currently authenticated user.
- **Authorization:** Bearer Token (required)
- **Response:** Returns JSON array of order objects with order id, total amount, and order date.
