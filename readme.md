Here is the updated documentation for your Restaurant Management Django REST API:

---

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
  - `phone_number` (string, required)
  - `address` (string, required)
  - `email` (string, required)
  - `password` (string, required)
  - `user_type` (string, required)
  - `aadhaar_number` (string, optional)
  - `date_of_birth` (date, optional)
  - `vehicle_details` (string, optional, for delivery person)
- **Response:** Returns JSON with success message or error.
- **Example:**
  ```json
  {
    "username": "abhishek",
    "name": "Abhishek",
    "phone_number": "3456786578",
    "address": "Gujarat",
    "email": "kushvahaabhisek33@gmail.com",
    "password": "abc",
    "user_type": "customer",
    "date_of_birth": "1990-01-01"
  }
  ```

  ```json
  {
    "username": "delivery123",
    "name": "Delivery Person",
    "phone_number": "3456786578",
    "address": "Gujarat",
    "email": "delivery@example.com",
    "password": "securepassword",
    "user_type": "delivery_person",
    "aadhaar_number": "123456789012",
    "vehicle_details": "Bike"
  }
  ```

  ```json
  {
    "username": "owner123",
    "name": "Owner Name",
    "phone_number": "3456786578",
    "address": "Gujarat",
    "email": "owner@example.com",
    "password": "securepassword",
    "user_type": "restaurant_owner",
    "aadhaar_number": "1234 5678 9101"
  }
  ```

#### 2. **Login**
- **URL:** `/login/`
- **Method:** POST
- **Description:** Allows users to authenticate.
- **Parameters:**
  - `email` (string, required)
  - `password` (string, required)
- **Response:** Returns JSON with access token and refresh token or error message.

#### 3. **Logout**
- **URL:** `/logout/`
- **Method:** POST
- **Description:** Logs out the currently authenticated user.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Response:** Returns JSON with success message.

#### 4. **Token**
- **URL:** `/token/`
- **Method:** POST
- **Description:** Retrieves the access token and refresh token.
- **Parameters:**
  - `email` (string, required)
  - `password` (string, required)
- **Response:** Returns JSON with access token and refresh token.

### User Profile

#### 5. **User Profile**
- **URL:** `/profile/`
- **Method:** GET
- **Description:** Retrieves the profile information of the currently authenticated user.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Response:** Returns JSON with username, email, user type, phone number, address, and other relevant details.

### Restaurant Management

#### 6. **List Restaurants**
- **URL:** `/restaurants/`
- **Method:** GET
- **Description:** Retrieves a list of all restaurants.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Response:** Returns JSON array of restaurant objects with id and name.

#### 7. **Restaurant Detail**
- **URL:** `/restaurant/<restaurant_id>/`
- **Method:** GET
- **Description:** Retrieves details of a specific restaurant.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Parameters:**
  - `restaurant_id` (integer, required)
- **Response:** Returns JSON object with restaurant id, name, description, and other relevant details.

#### 8. **Menu Items**
- **URL:** `/menu/<restaurant_id>/`
- **Method:** GET
- **Description:** Retrieves menu items for a specific restaurant.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Parameters:**
  - `restaurant_id` (integer, required)
- **Response:** Returns JSON array of menu item objects with id, name, and price.

### Order Management

#### 9. **Place Order**
- **URL:** `/order/place/<restaurant_id>/`
- **Method:** POST
- **Description:** Allows placing an order at a specific restaurant.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Parameters:**
  - `restaurant_id` (integer, required)
- **Request Body:**
  ```json
  {
      "delivery_address": "string",
      "items": [item_id1, item_id2, ...]
  }
  ```
- **Response:** Returns JSON with order details including order id and total amount.

#### 10. **Order Confirmation**
- **URL:** `/order/<order_id>/`
- **Method:** GET
- **Description:** Retrieves details of a specific order.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Parameters:**
  - `order_id` (integer, required)
- **Response:** Returns JSON with order id, total amount, and order date.

#### 11. **Order History**
- **URL:** `/orders/history/`
- **Method:** GET
- **Description:** Retrieves order history for the currently authenticated user.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Response:** Returns JSON array of order objects with order id, total amount, and order date.

### Update User Details

#### 12. **Update Customer Details**
- **URL:** `/update/customer/`
- **Method:** PUT
- **Description:** Updates details of the currently authenticated customer.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Request Body:**
  ```json
  {
    "phone_number": "9876543210",
    "address": "New Address",
    "date_of_birth": "1995-05-15"
  }
  ```
- **Response:** Returns updated customer details if successful, or error messages.

#### 13. **Update Restaurant Owner Details**
- **URL:** `/update/restaurant_owner/`
- **Method:** PUT
- **Description:** Updates details of the currently authenticated restaurant owner.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Request Body:**
  ```json
  {
    "phone_number": "9876543210",
    "address": "New Address",
    "aadhaar_number": "1234 5678 9101"
  }
  ```
- **Response:** Returns updated restaurant owner details if successful, or error messages.

#### 14. **Update Delivery Person Details**
- **URL:** `/update/delivery_person/`
- **Method:** PUT
- **Description:** Updates details of the currently authenticated delivery person.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Request Body:**
  ```json
  {
    "phone_number": "9876543210",
    "address": "New Address",
    "vehicle_details": "Car"
  }
  ```
- **Response:** Returns updated delivery person details if successful, or error messages.

### Update Restaurant Details

#### 15. **Update Restaurant Details**
- **URL:** `/update/restaurant/<restaurant_id>/`
- **Method:** PUT
- **Description:** Updates details of a specific restaurant identified by `restaurant_id`.
- **Authorization:** Bearer Token (required)
  - Example: `'Authorization':'Bearer <your_access_token>'`
- **Request Body:**
  ```json
  {
    "name": "New Restaurant Name",
    "description": "New Description",
    "location": "New Location"
  }
  ```
- **Response:** Returns updated restaurant details if successful, or error messages.

## Password Reset Using Django Views and Templates

### 1. Request Password Reset

- **URL:** `/password-reset/`
- **Method:** POST
- **Description:** Initiates a password reset process by sending a password reset email to the user's registered email address.

#### Request Body
```json
{
    "email": "user@example.com"
}
```

#### Responses
- **Success Response:** HTTP 200 OK
  ```json
  {
      "success": "Password reset email has been sent."
  }
  ```
  
- **Error Response:** HTTP 400 Bad Request
  ```json
  {
      "error": "Email is required."
  }
  ```
  ```json
  {
      "error": "No user
  }
  ```

### 2. Password Reset Confirmation

- **URL:** `/password-reset-confirm/<uidb64>/<token>/`
- **Method:** 
  - GET: Renders the password reset form if the token is valid.
  - POST: Resets the user's password using the provided new password.

#### GET Method (Rendering Password Reset Form)
- **URL Example:** `/password-reset-confirm/MTE=/5r5-1a48f07a7c746bfecf94/`

#### POST Method (Reset Password)
- **URL Example:** `/password-reset-confirm/MTE=/5r5-1a48f07a7c746bfecf94/`
- **Request Body**
  ```json
  {
      "new_password": "newpassword123"
  }
  ```

#### Responses
- **GET Method:**
  - **Success Response:** Renders the password reset form.
  - **Error Response:** HTTP 404 Not Found if the token is invalid or expired.

- **POST Method:**
  - **Success Response:** HTTP 200 OK
    ```json
    {
        "message": "Password reset successfully."
    }
    ```
  - **Error Response:** HTTP 400 Bad Request
    ```json
    {
        "error": "New password is required."
    }
    ```
    or specific password validation errors.

## Example Usage

### 1. Request Password Reset

```html
<form id="loginForm">
    {% csrf_token %}
    <label for="username">Email:</label><br>
    <input type="text" id="username" name="email" required><br><br>

    <button type="submit">Reset Password</button>
</form>


<div id="loginMessage"></div>

<script>
    document.getElementById("loginForm").addEventListener("submit", function(event) {
        event.preventDefault();

        let formData = new FormData(this);

        fetch('/password-reset/', {
            method: 'POST',
            body: JSON.stringify(Object.fromEntries(formData)),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Fetch CSRF token from cookies
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = '/success';  // Redirect to dashboard or desired page on successful login
            } else {
                // Display error message
                document.getElementById("loginMessage").innerHTML = `<p>Error: ${data.error}</p>`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("loginMessage").innerHTML = `<p>Network Error</p>`;
        });
    });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
</script>
```

### 2. Password Reset Confirmation

#### GET Method (Rendering Password Reset Form)
user will receivbe email and will be directed to password_reset_confirm_page page

#### POST Method (Reset Password)
```html
 <form id="resetForm" action="" method="post">
        {% csrf_token %}
        <input type="hidden" name="uidb64" value="{{ uidb64 }}">
        <input type="hidden" name="token" value="{{ token }}">
        <label for="new_password">New Password:</label><br>
        <input type="password" id="new_password" name="new_password" required><br><br>
        <button type="submit">Reset Password</button>
    </form>
    <div id="resetMessage"></div>
    
    <script>
        document.getElementById("resetForm").addEventListener("submit", function(event) {
            event.preventDefault();
    
            let formData = new FormData(this);
            let uidb64 = document.querySelector("input[name='uidb64']").value;
            let token = document.querySelector("input[name='token']").value;
    
            fetch(`/password-reset-confirm/${uidb64}/${token}/`,// Replace with the correct URL endpoint for password reset confirmation
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                } else {
                    // Handle error
                    
                }
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById("resetMessage").innerHTML = `<p>Network Error</p>`;
            });
        });
    
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.startsWith(name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    </script>
```
