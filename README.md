<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Food Ordering Web Application (Zomato)</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f8f8f8;
            color: #333;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
        }

        h1 {
            color: #0066cc;
        }

        h2 {
            color: #009933;
        }

        p {
            line-height: 1.6;
        }

        a {
            color: #0066cc;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: 'Courier New', Courier, monospace;
        }
    </style>
</head>

<body>
    <header>
        <h1>Food Ordering Web Application (Zomato)</h1>
    </header>

    <section>
        <h2>Table of Contents</h2>
        <ul>
            <li><a href="#stack">Tech Stack</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#security">Security</a></li>
            <li><a href="#cart">Cart Operations</a></li>
            <li><a href="#payment">Payment Gateway Integration</a></li>
            <li><a href="#gmail">Gmail Integration</a></li>
            <li><a href="#getting-started">Getting Started</a></li>
            <li><a href="#license">License</a></li>
        </ul>
    </section>

    <section id="stack">
        <h2>Tech Stack</h2>
        <p>
            Web Stack: Python with Django framework (back end), HTML, CSS, JavaScript (front end), MySQL (DBMS).
        </p>
    </section>

    <section id="features">
        <h2>Features</h2>
        <ul>
            <li>Authentication functionality (login, register, logout)</li>
            <li>Multiuser application using sessions</li>
            <li>Security to prevent unauthorized access</li>
            <li>Cart operations: Add, Remove, Increase quantity</li>
            <li>Payment Gateway Integration (Razor Pay)</li>
            <li>Gmail Integration</li>
        </ul>
    </section>

    <section id="getting-started">
        <h2>Getting Started</h2>
        <p>
            Follow these steps to get the project up and running on your local machine:
            <ol>
                <li>Clone the repository: <code>git clone https://github.com/your-username/your-repo.git</code></li>
                <li>Install dependencies: <code>npm install</code></li>
                <li>Run the application: <code>npm start</code></li>
            </ol>
        </p>
    </section>

    <section id="license">
        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    </section>
</body>

</html>
