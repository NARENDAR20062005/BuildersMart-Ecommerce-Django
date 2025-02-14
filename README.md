# Ecommerce WebApp Using Django Framework



A simple project based on an Online Ecommerce Site that uses Python with Django Web Framework. Following Django project contains all the important features which can be in use for the second year IT students for their college projects. It has a number of important features that will allow the users to shop online, manage orders, and more. This system as well as the website’s concept is all clear, it’s the same as real-life scenarios and well-implemented on it. 

In particular, this eCommerce site project in Python Django focuses mainly on dealing with online shopping, and order management. Also, the system displays all the available products. In addition, the system allows managing customer records. Evidently, this project is divided into two categories: Customer, and Admin Panel. In an overview of this web application, a customer can simply register from the client-side. Initially, the website displays all the available products with their respective details. Just like every other eCommerce website, this one has also got a cart system. This allows the customers to add a number of products to their cart before checking out. Speaking of check out, there’s a simple payment form that needs to be completed by the customers. In fact, the customers can view their orders list and track orders after successful payment. Besides, customers can make search queries and update their user profiles.

## Admin Panel
An administrator has full control over the system. He/she can manage customers, orders, and products. Here, each and every section has its own respective details such as name, images, and other important details. The very first step of the management of this system is to set up products. There are minor fields for each such as name, short description, price, and image. All the published products are totally visible from the client-side. By accessing the admin panel, the user can oversee the overall records such as the number of registered users, orders, and published products. Talking about the registered users, the admin can view a list of users with every possible detail. Here, the admin can take actions such as removing or updating customers’ details.

## Order Management and Invoice
Moving towards the order management section, the system forwards each and every customer’s order details after their successful payment. By default, every order is marked under pending status which is also visible from both. An administrator can view a number of pending orders and take action accordingly. For this, an admin has to update the order status for each(codeastro.com). The user can update the status of an order from pending to order confirmed, on the way, or delivered. Which totally depends upon the status of their product and delivery stages. In fact, with each and every update, the customers can view and track each and every order. This helps to know the information about their orders and their arrivals. With it, the customers can also download an invoice from the orders section with displays every detail related to it.

Last but not least, a clean and simple dashboard is presented with various color combinations for a greater user experience while using this eCommerce Site Project in Python Django Framework. For its UI elements, a free open-source CSS framework; Bootstrap is on board with some Vanilla CSS too(codeastro.com). Presenting a new e-commerce website Project in Python Django which includes an admin panel with client-side interaction.

[Watch Full Video]()

## Available Features:

- Client-Side Interaction
- Admin Panel
- Customer Registration
- Add to Cart System
- Search Products
- Simple Payment Structure
- List Orders
- Track Orders
- Download Invoice (PDF)
- send invoice to mail(pdf)
- View/Update Profile
- Order Management
- Product Management
- Customer Management

## File Stucrure

```shell
├── Ecommerce-WebApp (Current Directory)
    ├── ecom
    ├── ecommerce
    ├── templates
    ├── db.sqlite3
    ├── manage.py
    ├── requirements.txt
    └── static
        
```



## How to Install and Run this project?

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
 python -m venv venv
```
For Mac
```
python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
source venv/scripts/activate
```

For Mac
```
source venv/bin/activate
```

**3. Install Requirements from 'requirements.txt'**
```
pip install -r requirements.txt
```

**4. make database migrations**
```python
python manage.py migrate
```

**5. Login Credentials**

Create Super User (HOD)
```
$  python manage.py createsuperuser
```
Then Add Email, Username and Password

**6. Now Run Server**

Command for Windows:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

## Screenshots
USER DASHBOARD :  


![Image](https://github.com/user-attachments/assets/63f43ff3-0745-424f-8841-3514b6c9a033)

![Image](https://github.com/user-attachments/assets/898db0b9-f09a-4c00-9837-cb8beba30eb8)

![Image](https://github.com/user-attachments/assets/cf931fe2-3428-400b-b732-462cbfd5a55e)

![Image](https://github.com/user-attachments/assets/bbd8075d-d166-4b10-85df-861a6b60f141)

![Image](https://github.com/user-attachments/assets/82cf25c8-9f44-4a62-8549-f52a92fe1829)

![Image](https://github.com/user-attachments/assets/e295aecd-0b86-4a94-8ac3-dea259a9eac9)

![Image](https://github.com/user-attachments/assets/903a73ce-761a-4ba2-bc5f-726b04364af3)

![Image](https://github.com/user-attachments/assets/469a9a1b-749b-41a2-8b9e-1a7dd855f9f6)

![Image](https://github.com/user-attachments/assets/db1e6575-bbed-48b0-8b42-0dd59eb14906)

![Image](https://github.com/user-attachments/assets/2cfbe28f-4523-4001-a912-7e095d40e5d2)

![Image](https://github.com/user-attachments/assets/5ca99679-fc21-4e1e-8589-f1e5c860712c)

![Image](https://github.com/user-attachments/assets/f9b9c15b-3c68-4add-98ca-b81aad3c1ed6)

![Image](https://github.com/user-attachments/assets/e783cda4-6e3a-4626-9094-2b2ebe48b713)

![Image](https://github.com/user-attachments/assets/3f107b0d-4db2-453c-a830-40fb48a44358)

![Image](https://github.com/user-attachments/assets/95f3f6f7-6452-4735-a3bd-1b1f0bed07a9)

![Image](https://github.com/user-attachments/assets/e48cec65-bc4c-40e1-9c81-8ac2094de514)

![Image](https://github.com/user-attachments/assets/87079fb5-4c2e-4b75-9608-831a8b4c2f9e)

![Image](https://github.com/user-attachments/assets/a064b831-27fb-41a9-835b-0f9ee2549a60)


 
ADMIN DASHBOARD :


![Image](https://github.com/user-attachments/assets/06261fae-e42a-4f9f-aaab-945da1981c26)

![Image](https://github.com/user-attachments/assets/8c9ac4f3-9f65-431b-8b24-b024f7dbd7b4)

![Image](https://github.com/user-attachments/assets/8be56bb1-cd00-47ce-a941-ebc07f5ae3a1)

![Image](https://github.com/user-attachments/assets/6c47e3fe-ed33-45b8-878a-fb474ae7fe69)

![Image](https://github.com/user-attachments/assets/8fa18410-aabb-453d-bea2-c9e105f57cdb)

![Image](https://github.com/user-attachments/assets/12923f0d-eb5d-4a8a-ae3d-ee811af59ed3)

![Image](https://github.com/user-attachments/assets/eb953cf9-7a59-4084-9503-fc8ff34cac8f)

![Image](https://github.com/user-attachments/assets/4b5582f2-0a1d-4e0b-80e2-f51fbff063a3)

![Image](https://github.com/user-attachments/assets/ab1c8ddc-ec01-4965-8e94-376b9643e3cd)



## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.





