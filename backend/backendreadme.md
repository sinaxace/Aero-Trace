# User Model and Authentication
We are using django.contrib.auth `s User model which give as a default User with id, username, email. In addition to that we are creating authentication.py class to add custom authentication.
We are checking user's email and password .
After we need to add this code block to settings.py

``` python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
]
```
In this code block we first try to use ModelBackend to authenticate user, after that if needed 
we can authenticate user with EmailAuthBackend it basically follow the order.

*The order of the backends listed in the AUTHENTICATION_BACKENDS setting matters. If the same credentials are valid for multiple backends, Django will stop at the first backend that successfully authenticates the user.*

# JSON Web Tokens Authentication Project

* Start Here *

``` python
python3 -m venv venv
#Create a vitual environment called venv
python -m django --version
#3.0.5

pip install djangorestframework djangorestframework-jwt
# THis will provide JSON WT authentication layer with DJANGO

django-admin startproject JWTAuth

# Now add those lines to Settings.py file

INSTALLED_APPS = [
    ...
    'rest_framework',
]
 
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
```
**Don`t forget to import -> pip install djangorestframework-jwt**

## How does it work ?
* Basic Auth - a username and password are passed with each API request. This provides only a minimum level of security and user credentials are visible in the URLs
  
* Session Auth - requires the user to log in through the server-side application before using the API. This is more secure than Basic Auth but is not convenient for working with single-page apps in a framework like Angular.
  
* JSON Web Tokens are an industry standard mechanism for generating a token which can be passed in the HTTP headers of each request, authenticating the user. This is the mechanism we will use for authentication.

## Now we will modify the JWT_AUTH settings

``` python
JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3600),
}
```
Don`t forget to import datetime 

JWT tokens have a life span, after which they are no longer valid. The default is only 5 minutes, but we can set it to a longer time (say, 1 hour) using the JWT_EXPIRATION_DELTA setting. The JWT_ALLOW_REFRESH setting enables a feature of DRF-JWT where an application can request a refreshed token with a new expiration date.


## urls.py file updates 

Update your urls.py file like this one 

```python
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
]
```
These endpoints provide us with a means to authenticate via the API and to request a new token.

**r'** is for re_ath() function which is a raw string they can contains sequences like  **\d** When patterns match it direct them to views.py file to read what to show. More on [here](https://docs.djangoproject.com/en/3.0/ref/urls/)

## Creating app inside of the project

First go to manage.py level directory and run the command

``python
python manage.py startapp microblog
```
Under new app, we will crea te a simple View and template which will serve the single-page app

microblog/views.py

```python

from django.shortcuts import render

# Create your views here.
def index(request, path=''):
    """
    The home page. This renders the container for the single pag app
    """
    # IN Django we will use two template files : base.html -> providing the outer HTML shell
    #index.html -> content of the html page itself.
    
    return render(request, 'index.html') 
```
## Creating templates

Create a template folder under microblog directory. And create index.html and base.html under template/

**base.html**
```
{% load staticfiles %}
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Angular, Django Rest Framework, and JWT token demo</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    {% block heading %}
      <h1>Angular, Django Rest Framework, and JWT demo</h1>
    {% endblock %}
 
    {% block content %}{% endblock %}
  </div>
</body>
</html>
```

**index.html**

```
{% extends "base.html" %}
{% load staticfiles %}
 
{% block content %}
  <p>This is a mini-blog application using a back-end built on Django 2.0 and Django Rest Framework. It illustrates how to create and send JSON Web Token authentication headers with the HTTP requests.</p>
 
  <app-root>Loading the app...</app-root>
 
  <script type="text/javascript" src="{% static 'front-end/runtime.js' %}"></script>
  <script type="text/javascript" src="{% static 'front-end/polyfills.js' %}"></script>
  <script type="text/javascript" src="{% static 'front-end/styles.js' %}"></script>
  <script type="text/javascript" src="{% static 'front-end/vendor.js' %}"></script>
  <script type="text/javascript" src="{% static 'front-end/main.js' %}"></script>
 
{% endblock %}
```
# Front -end  settings

Go to microblog directory and 
```
ng new front-end
```

* app - The location of the Angular module, components, and services
* angular.json - The configuration for the Angular CLI
* dist - The destination where the Angular CLI will place the compiled files. We'll change this in just a moment to be compatible with Django.

Now we need figure out the static files directory.
Django {% load staticfiles %} command will look through Django/static folder. Now we will edit Angular.json to reach static files from Django app`s folder

```
...
  "projects": {
    "ng-demo": {
      ...
      "architect": {
        "build": {
          ...
          "options": {
            "outputPath": "../static/front-end",   <-- change this line
...
```
## What's in our Angular app
The Angular app we're creating here will contain the following pieces:

* microblog/front-end/src/app/app.component.html - a template that will contain the login form

* microblog/front-end/src/app/app.component.ts - our main component
* microblog/front-end/src/app/user.service.ts - a service that will manage the authentication API requests

**front-end/src/app/app.module.ts**
```
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';    // add this
import { FormsModule } from '@angular/forms';    // add this
import { AppComponent } from './app.component';
import { UserService } from './user.service';    // add this
 
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, FormsModule, HttpClientModule],    // add this
  providers: [UserService],    // add this
  bootstrap: [AppComponent]
})
export class AppModule { }
```

UserService is a custom module , we will build in a sec.

**front-end/src/app/app.component.ts**
```
mport {Component, OnInit} from '@angular/core';
import {UserService} from './user.service';
import {throwError} from 'rxjs';
 
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
 
  /**
   * An object representing the user for the login form
   */
  public user: any;
 
  constructor(private _userService: UserService) { }
 
  ngOnInit() {
    this.user = {
      username: '',
      password: ''
    };
  }
 
  login() {
    this._userService.login({'username': this.user.username, 'password': this.user.password});
  }
 
  refreshToken() {
    this._userService.refreshToken();
  }
 
  logout() {
    this._userService.logout();
  }
 
}
```

**front-end/src/app/app.component.html**
```
<h2>Log In</h2>
<div class="row" *ngIf="!_userService.token">
  <div class="col-sm-4">
    <label>Username:</label><br />
    <input type="text" name="login-username" [(ngModel)]="user.username">
    <span *ngFor="let error of _userService.errors.username"><br />
    {{ error }}</span></div>
  <div class="col-sm-4">
    <label>Password:</label><br />
    <input type="password" name="login-password" [(ngModel)]="user.password">
    <span *ngFor="let error of _userService.errors.password"><br />
    {{ error }}</span>
  </div>
  <div class="col-sm-4">
    <button (click)="login()" class="btn btn-primary">Log In</button
  </div>
  <div class="col-sm-12">
    <span *ngFor="let error of _userService.errors.non_field_errors">{{ error }}<br /></span>
  </div>
</div>
<div class="row" *ngIf="_userService.token">
  <div class="col-sm-12">You are logged in as {{ _userService.username }}.<br />
    Token Expires: {{ _userService.token_expires }}<br />
    <button (click)="refreshToken()" class="btn btn-primary">Refresh Token</button>
    <button (click)="logout()" class="btn btn-primary">Log Out</button>
  </div>
</div>
```
We are outputing their expration data as well.

Now we are creting new class -> src/app/user.service.ts

```
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable()
export class UserService { 

    //httpOptions used for making API calls
    private httpOptions: any;

    //the actual JWT token
    public token: string;

    //the token expiration date
    public token_expires: Date;

    //the username of the logged in user
    public username: string;

    //error messages reveiced from the login attempt
    public errors: any = [];

    constructor(private http: HttpClient) { 
        this.httpOptions = {
            headers: new HttpHeaders({ 'Content-Type': 'application/json' })
        };
    }

    //Uses http.post() to get an auth token from djangorestframework-jwt endpoint
    public login(user) {
        this.http.post('/api-token-auth/', JSON.stringify(user), this.httpOptions).subscribe(
            data => {
                this.updateData(data['token']);
            },
            err => {
                this.errors = err['error'];
            }
        );
    }

    // Refreshes the JWT token, to extend the time the user is logged in
    public refreshToken() {
        this.http.post('/api-token-refresh/', JSON.stringify({ token: this.token }), this.httpOptions).subscribe(
            data => {
                this.updateData(data['token']);
            },
            err => {
                this.errors = err['error'];
            }
        );
    }

    public logout() { 
        this.token = null;
        this.token_expires = null;
        this.username = null;
    }
    private updateData(token) { 
        this.token = token;
        this.errors = [];

        //decode the token to read the username and expiration timestamp
        const token_parts = this.token.split(/\./);
        const token_decoded = JSON.parse(window.atob(token_parts[1]));
        this.token_expires = new Date(token_decoded.exp * 1000);
        this.username = token_decoded.username;
    }

}

```
login() -> send the username and password to  /api-token-auth and receives in response.
refreshToken() -> sends the token **not the username and password** to /api-refresh-token endpoint which retrieves new token for the same user.

Token is base64-encoded strings glued together, we use JSON.parse() and window.atob()

how to send data to Django ? -> We will POST data with our token. We will put JWT Token in the header of http request
make a new class -> src/app/blog_post_service.ts
```
import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { UserService } from './user.service';
import { create } from 'domain';

@Injectable()
export class BlogPostService { 
    constructor(private http: HttpClient, private _userService: UserService) {
    }
        //Send a POST request to the API to create a new blog post
        create(post, token){
            let httpOptions = {
                headers: new HttpHeaders({
                    'Content-Type': 'application/json',
                    'Authorization': 'JWT ' + this._userService.token // we send JWt in the headers.
                })
            };
            return this.http.post('/api/posts', JSON.stringify(post), httpOptions);
        }
    }

```

## How our data flow ?

SQLite Database -> Django Model -> Django Serializer -> Django ViewSet -> Angular Service -> Angular Component

Now we are going back to Django part to create some model.
We define User and Blog Post in angular so we need those to define as a model in Django part. User model is
provided out-of-the-box by Django so we only need to define BlogPost.

**microblog/models.py**

``` python
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
 
class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(
        default=timezone.now
    )
    body = models.CharField(default='', max_length=200)
 
    def __str__(self):
        return self.body
```

After we create models we need to run migrations [You can check more](https://docs.djangoproject.com/en/2.1/topics/migrations/)
Model class creates a table with the given fields, we have a BlogPost table which will held **user, date and post itself**

Now create serializers.py under microblog app  ->microblog/serializers.py

``` python
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BlogPost

class UserSeriazlier(serializers.ModelSerializer):
    """Unlike User Model, we need to define User Serializer """
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name') ##Defines which fields will be converted to JSON

class BlogPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = BlogPost
        fields = ('id','user','date','body')

```
On the Serializers class we are connecting with our models *unlike model class, we have to define the UserSerializer(it won't come out-of-the-box)*
Serializer class helps us to get Model fields and parse it to JSON to use end to end point connections. Such as Angular front-end , DJango back-end

Now we are modifying views.py
``` python
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import BlogPost
from . import serializers
from .permissions import ReadOnly
 
def index(request, path=''):
    return render(request, 'index.html')
 
class UserViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the User model
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (ReadOnly, )
 
class BlogPostViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the Blog Post model
    """
    queryset = BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

For both serializers it query all the objects on the model. Connect model specific serializer.

Permission_classes,  allow full access to authenticated users, but allow read-only access to unauthenticated users. This corresponds to the **IsAuthenticatedOrReadOnly** class in REST framework.
Permissions are first checked on, if any permission fails, rest of the view won`t executed [Read more on here](https://www.django-rest-framework.org/api-guide/permissions/)

perform_create(self, serializer) is CRUD style method that create new object based on request of the user. [Read more on perform method](https://www.django-rest-framework.org/api-guide/generic-views/)

Now *create urls.py under microblog*
``` python
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
## When we are using register method 2 important things 
#-> prefix and viewset(the views.py class)
router.register(r'posts', views.BlogPostViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)), # it include all API endpoints.
    path(r'',views.index,name='index')
]

```

we include all the url endpoint to 'api/' and if we write nothing we go to index page as default.

Now under microblog app, ** create -> permissions.py **
```python
from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class ReadOnly(permissions.BasePermission):
    """
    The endpoint is read-only request.
    """

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
        )
```

### Change {% load staticfiles %} to {% load static %}
## on the console -> python manage.py runserver
First thing is index, if you go to '/api' you will see two end - points.

* Add Cors headers to settings.py
* Fix {% load static %}


