# Saraha Anonymous Message App

Welcome to the Saraha Anonymous Message App! This app allows users to send and receive anonymous messages, fostering open communication. Below is an overview of the main pages in the app:


## Features

1. **Dashboard:** Upon launching the app, users are directed to the dashboard, providing an initial overview of the app's functionality.

2. **Login and Sign Up:**
   - Users can log in using existing account credentials or create a new account by providing details.
   - Authentication is implemented using Django's built-in authentication system.
   - Usernames are checked for existence before login or registration.

3. **Interface:**
   - After successful login or sign-up, users are directed to the interface page.
   - Each user is assigned a unique generated link for sharing with others.
   - This link allows users to receive anonymous messages from other users.

4. **Message Index:**
   - Clicking on the generated link takes users to the message index page.
   - Users can view received anonymous messages and respond to them.
   - Users can also submit their own messages and view replies from others.

5. **Comments and Replies:**
   - Users can navigate to the comments page to view comments and replies they've received.
   - Comments and replies are associated with users and their unique generated links.

6. **Message Sending and Reply:**
   - Users can post comments and replies through appropriate forms.
   - Comment and reply text is stored in the database using the `Comment_Reply` and `Reply` models.

7. **Success Page:**
   - After successfully sending a message, users are redirected to a success page.
   - This page confirms message delivery and provides a link to return to the message index.

8. **Contact Page:**
   - A contact page is included in the app, though its functionality is not detailed in the provided code.

9. **User Logout:**
   - Users can log out from the app using the logout link.

10. **User Registration:**
    - Users can create accounts with unique usernames.
    - Passwords are securely stored using Django's password hashing.


Here are some screenshots of the app's pages:
## Dashboard

1. Dashboard
   ![Dashboard](static/img/Screenshot%20(1112).png)


## Login  
2. Login 
   ![Login and Sign Up](static/img/Screenshot%20(1115).png)

## Sign Up
1. Sign Up
      ![Login and Sign Up](static/img/Screenshot%20(1114).png)

## Interface

3. Interface    
   ![Interface](static/img/Screenshot%20(1116).png)


## Message Index
4. Message Index
   ![Message Index](static/img/Screenshot%20(1117).png)

## Success Page

5. Success Page
   ![Success Page](static/img/Screenshot%20(1118).png)

## Comments Page

6. Comments Page
   ![Comments Page](static/img/Screenshot%20(1119).png)

## Reply
![Comments Page](static/img/Screenshot%20(1120).png)

## Contributing

We welcome contributions from the community! If you encounter any issues or have suggestions for improvements, feel free to submit a pull request or open an issue on our GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
