# FullStack-TodoApp
=====================

A modern Todo App built with a full-stack architecture, utilizing HTML, CSS, JavaScript, Node.js, Express.js, and MongoDB.

## Table of Contents
-------------------

*   [Project Overview](#project-overview)
*   [Features](#features)
*   [Technologies Used](#technologies-used)
*   [Setup and Installation](#setup-and-installation)
*   [Running the Application](#running-the-application)
*   [Database Schema](#database-schema)
*   [Commit Message Guidelines](#commit-message-guidelines)

## Project Overview
-----------------

This Todo App is designed to demonstrate a full-stack development approach, where the client-side and server-side components are seamlessly integrated to provide a robust and scalable application. The application features a user-friendly interface for adding, removing, and editing tasks, with real-time updates and data persistence.

## Features
------------

*   Task creation, deletion, and editing
*   Real-time updates for each task operation
*   Data persistence using MongoDB
*   Robust and scalable architecture using Express.js and Node.js
*   User-friendly interface with HTML, CSS, and JavaScript

## Technologies Used
---------------------

*   **Frontend:**
    *   HTML5
    *   CSS3 (Tailwind CSS)
    *   JavaScript (ES6+ syntax)
    *   React.js (optional for client-side rendering)
*   **Backend:**
    *   Node.js (14.x or higher)
    *   Express.js (4.x or higher)
    *   MongoDB (4.x or higher)
    *   Mongoose (latest version)
*   **Utilities:**
    *   npm (14.x or higher)
    *   MongoDB Compass (for database management)

## Setup and Installation
-------------------------

### Prerequisites

*   Node.js (14.x or higher) installed on the system
*   npm (14.x or higher) installed on the system
*   MongoDB (4.x or higher) installed and running on the system
*   MongoDB Compass (for database management)

### Installing Dependencies

```bash
# Navigate to the project root directory
cd FullStack-TodoApp

# Install dependencies using npm
npm install
```

### Creating a Database

```bash
# Create a new MongoDB database
mongo

# Create a new database (e.g., "TodoApp")
use TodoApp

# Create a new collection (e.g., "tasks")
db.createCollection("tasks")
```

## Running the Application
---------------------------

### Development Mode

```bash
# Run the application in development mode (nodemon)
npm start
```

### Production Mode

```bash
# Run the application in production mode (pm2)
pm2 start app.js --watch
```

## Database Schema
-----------------

The database schema is defined using Mongoose.js. The following are the main data models:

*   **Task:** Represents a single task with the following attributes:
    *   `_id` (ObjectId): Unique identifier for the task
    *   `title` (string): Title of the task
    *   `description` (string): Description of the task
    *   `completed` (boolean): Task completion status
    *   `created` (Date): Timestamp when the task was created

## Commit Message Guidelines
---------------------------

*   Follow the conventional commit message format (e.g., "fix: <description>", "feat: <description>", etc.)
*   Use imperative mood (e.g., "Add new task model", "Remove redundant code")

Author Information:

*   Name: [Your Name]
*   Email: [Your Email]
*   GitHub Profile: [Your GitHub Profile]

License and Copyright:

*   This project is licensed under the MIT License.
*   Copyright 2023 [Your Name]. All rights reserved.