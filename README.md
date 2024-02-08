# Group 6 project 
#Django e-commerce website

## Table of Contents

- [Django Ecommerce](#django-ecommerce)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation](#installation)
  - [Contributing](#contributing)
  - [License](#license)



## Description

Django Ecommerce is a simple and elegant online store built with Python and Django. It allows users to browse, search, and purchase products, as well as manage their orders and profile. It also features a user-friendly admin panel for managing products, categories, and orders.

## Installation
First, clone this repository:

```bash
# Clone this repository
Git clone https://gitlab.com/group-6-saad/group-6-project.git
cd group-6-project
```
Next, create and activate a virtual environment:

```bash
# Create a virtual environment(you can use any name for the virtual environment)
python -m venv env 

# Activate the virtual environment
source env/bin/activate
```

Then, install the required packages:

```bash
# Install the requirements
pip install -r requirements.txt
```

Finally, migrate the database and run the server:

```bash
# Migrate the database
python manage.py migrate

# Run the server
Python manage.py runserver
```

## Contributing

We welcome contributions from anyone who wants to improve this project. To contribute, please follow these steps:

1. Fork this repository and clone it to your local machine.
2. Create a new branch with a descriptive name, such as `feature-add-payment-method` or `bugfix-fix-cart-total`.
3. Make your changes and commit them with a clear and concise message, following the [conventional commits](^6^) format.
4. Push your changes to your forked repository and create a pull request to the `main` branch of this repository.
5. Wait for your pull request to be reviewed and merged.

Please make sure to follow the [PEP 8](^7^) code style and write tests and documentation for your changes.

## License

This project is licensed under the [MIT License]. See the [LICENSE] file for more details.


