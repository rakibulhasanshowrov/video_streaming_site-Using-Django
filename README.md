# StreamY

**StreamY** is a simple video streaming website where users can register, log in, view YouTube videos, and leave comments. Since storing and streaming actual video files can be resource-heavy, StreamY simply embeds YouTube videos for seamless streaming. Admins can enlist new videos, and users can update their profiles.User can search video and only logged in user can give feedback on a video(Comment).

## Features

1. **User Registration**: Users can sign up with a unique username and password.
2. **User Login**: Registered users can log in to access and comment on videos.
3. **Stream Videos**: Users can view videos embedded from YouTube.
4. **User Profile**: Each user has a profile page where they can view and update their personal information.
5. **Enlist Videos**: Admins can add new video links to the platform for streaming (requires admin privileges).
6. **Video Comments**: Users can leave comments on videos to share their thoughts.
7. **Security**: Basic security measures are in place to protect user data, including password hashing and restricted admin access.
8. **Search**: User can Search Video using any keyword

## Pages

- **Landing Page**: The main page where users can browse and view videos.
- ![image](https://github.com/user-attachments/assets/78988331-b8c1-49dd-af68-f0271ede4476)

- **User Registration**: A form where users can create an account.
  ![image](https://github.com/user-attachments/assets/78593315-afd6-4d57-be36-1bb588d61ead)

- **User Login**: A page to log in to their account.
  ![image](https://github.com/user-attachments/assets/bac4f224-9a7a-44fd-9552-ec5ef9af52cd)
  
  ![image](https://github.com/user-attachments/assets/a5fd3340-5298-457f-9786-be4a4491c1a4)

- **Search**: Any User can Search Using Keyword in the Search bar
  ![image](https://github.com/user-attachments/assets/c8458bf8-0edc-4385-90bb-84a5af8af504)


- **User Profile**: A page where users can update their profile information.
  ![image](https://github.com/user-attachments/assets/6969e4b3-e4b9-4870-81dc-0d5311890bae)

  ![image](https://github.com/user-attachments/assets/68cec2d9-1575-4e40-9377-df96b73ef65e)


- **Admin Panel**: Available only to admins for enlisting new videos.
  ![image](https://github.com/user-attachments/assets/03df0dbc-7bd8-4ed6-aa6e-bd8638e165ed)

- **Video Page**: Individual pages for each video, where users can stream the video and leave comments.
  ![image](https://github.com/user-attachments/assets/bd83a703-3075-463b-b692-0059a91f0153)

  ![image](https://github.com/user-attachments/assets/d4593176-bfe1-4171-89ea-bebd0254b127)





## Requirements

- **Python 3.12**: The project is developed using Python.
- **Django 4.2**: The web framework used for building the website.
- **Django Rest Framework (optional)**: For APIs if needed.
- **CSS**: For front-end styling.
- **Google Font**: For Icon 
- **SQLite or any DB of your choice**: For database management.
- **Internet**: Since, I generate the thumbnail image from a Youtube video link thats why internet is needed to load the thumbnail image from internet



## Usage
###Access the website in your browser at `http://127.0.0.1:8000/`.
1. **User Registration**: Visit `account/signup` to create an account.
2. **User Login**: Visit `account/login` to log in.
3. **View Videos**: Browse or search videos on the landing page.
4. **Comment on Videos**: Leave a comment on the video detail page after logging in.
5. **Update Profile**: Visit your profile to update your information.
6. **Admin Panel**: Admins can visit `/admin` to enlist new YouTube videos.

## Security

- **Password Hashing**: User passwords are securely hashed using Django's built-in authentication system.
- **Admin Privileges**: Only users with admin rights can enlist new videos.
- **Login Required**: Users must be logged in to comment and update their profile.




