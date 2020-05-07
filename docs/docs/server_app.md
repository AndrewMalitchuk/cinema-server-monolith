# server_app

## admin.py

### FilmAdmin (`admin.ModelAdmin`)

A class for displaying Cinema entity in proper way for Admin-page

**Attributes**:

* `list_display`: A list of fields for displaying in Admin-page
* `list_display_links`: A list of fields for links
* `search_fields`: A list of fields for searching

### CinemaAdmin (`admin.ModelAdmin`):

A class for displaying Cinema entity in proper way for Admin-page

**Attributes**:

* `list_display`: A list of fields for displaying in Admin-page
* `list_display_links`: A list of fields for links
* `search_fields`: A list of fields for searching

### PosterAdmin (`admin.ModelAdmin`):

A class for displaying Poster entity in proper way for Admin-page

**Attributes**:

* `list_display`: A list of fields for displaying in Admin-page
* `list_display_links`: A list of fields for links
* `search_fields`: A list of fields for searching

### TimelineAdmin (`admin.ModelAdmin`):

A class for displaying Timeline entity in proper way for Admin-page

**Attributes**:

* `list_display`: A list of fields for displaying in Admin-page
* `list_display_links`: A list of fields for links
* `search_fields`: A list of fields for searching

### HallAdmin (`admin.ModelAdmin`):

A class for displaying Hall entity in proper way for Admin-page

**Attributes**:

* `list_display`: A list of fields for displaying in Admin-page
* `list_display_links`: A list of fields for links
* `search_fields`: A list of fields for searching

### TicketAdmin (`admin.ModelAdmin`):

A class for displaying Ticket entity in proper way for Admin-page

**Attributes**:

* `list_display`: A list of fields for displaying in Admin-page
* `list_display_links`: A list of fields for links
* `search_fields`: A list of fields for searching

### StaffAdmin (`admin.ModelAdmin`):

A class for displaying Staff entity in proper way for Admin-page

**Attributes**:

* `list_display`: A list of fields for displaying in Admin-page
* `list_display_links`: A list of fields for links
* `search_fields`: A list of fields for searching

## forms.py

### HallForm (`forms.ModelForm`):

A class that represents a form for Hall entity

### CinemaForm (`forms.ModelForm`):

A class that represents a form for Cinema entity

### PosterForm (`forms.ModelForm`):

A class that represents a form for Poster entity

    
### TimelineForm (`forms.ModelForm`):

A class that represents a form for Timeline entity

## models.py

### Film (`models.Model`):

A class that represents Film entity

**Attributes**:

* `GENRE`: An enumeration for available genres
* `title`: A film's title
* `description`: A film's description
* `date`: A film's date
* `duration`: A film's duration
* `genre`: A film's genre
* `video_url`: A film's trailer URL (`youtube`)
* `pic_url`: A film's poster URL

### Cinema (`models.Model`):

A class that represents Cinema entity

**Attributes**:

* `name`: A cinema's name
* `address`: A cinema's address in current city
* `city`: City's name
* `telephone`: A cinema's telephone
* `geo_lat`: Latitude for location on the map
* `geo_lon`: Longitude for location on the map
* `pic_url`: A cinema's picture/logo URL

### Poster (`models.Model`):

A class that represents Poster entity

**Attributes**:

* `cinema_id`: Cinema's ID for linking
* `film_id`: Film's ID for linking

### Hall (`models.Model`):

A class that represents Hall entity

**Attributes**:

* `name`: A hall's name
* `cinema_id`: Cinema's ID for linking
* `hall_json`: JSON-entity for hall rendering

### Timeline (`models.Model`):

A class that represents Timeline entity

**Attributes**:

* `cinema_id`: Cinema's ID for linking
* `film_id`: Film's ID for linking
* `hall_id`: Hall's ID for linking
* `time`: A session's time
* `date`: A session's date
* `price`: A price for current price

### Ticket (`models.Model`):

A class that represents Ticket entity

**Attributes**:

* `STATUS`: A enumeration that contains Ticket's status
* `place`: Place in hall for current session
* `status`: Ticket's status
* `user`: A User's ID
* `timeline_id`: Timeline's ID for linking

### Staff (`models.Model`):
    
A class that represents Staff entity.

**Attributes**:

* `user_id`: User's ID for linking
* `cinema_id`: Cinema's ID for linking

## permission.py

### IsStaffOrAdminWriteOnly (`permissions.BasePermission`):

Custom permission for certain REST endpoints

So if you are certain user or anon - you could only fulfill GET request to marked endpoints; if you are staff or
admin - you could fulfill all types of requests

**Methods**:

#### `has_permission(self, request, view)`:

Check your user's type to allow access to write operations

* *return* True if permission is granted

## serializers.py

### FilmSerializer (`serializers.ModelSerializer`):

Serializer for Film entity

### CinemaSerializer (`serializers.ModelSerializer`):

Serializer for Cinema entity

### TimelineSerializer (`serializers.ModelSerializer`):

Serializer for Timeline entity
    
### PosterSerializer (`serializers.ModelSerializer`):

Serializer for Poster entity
    
### HallSerializer (`serializers.ModelSerializer`):

Serializer for Hall entity
    
### TicketSerializer (`serializers.ModelSerializer`):

Serializer for Film entity
    
**Methods**:

#### `get_code(self)`:

Generate ticket's QR code

* *return* unique ticket code

#### `create(self, validated_data)`:

Create new Ticket entity using pre-generated unique QR-code

* *param* validated_data
* *return* created Ticket entity

### StaffSerializer (`serializers.ModelSerializer`):

Serializer for Film entity
    
### UserSerializer (`serializers.ModelSerializer`):

Serializer for Film entity

**Methods**:

#### `create(self, validated_data)`:

Create new User from mobile-client; pay attention on is_staff field - it is False

* *param* validated_data
* *return* created User

## tables.py

### FilmTable (`tables.Table`):

Table for Film entities; used for generation bootstrap-table

**Attributes**:

* `about_col`: extra column for opening "About Film" page


### CinemaTableEditable (`tables.Table`):

Table for Cinema entities (`editable`); used for generation bootstrap-table

**Attributes**:

* `update_col`: extra column for updating entity
* `delete_col`: extra column for deleting entity
* `about_col`: extra column for opening "About Cinema" page

### CinemaTableUneditable (`tables.Table`):

Table for Cinema entities (`uneditable`); used for generation bootstrap-table

**Attributes**:

* `about_col`: extra column for opening "About Cinema" page

### PosterTable (`tables.Table`):

Table for Poster entities; used for generation bootstrap-table

**Attributes**:

* `delete_col`: extra column for deleting entity
    
### TicketTable (`tables.Table`):

Table for Ticket entities; used for generation bootstrap-table
 
### HallTable (`tables.Table`):

Table for Hall entities; used for generation bootstrap-table

**Attributes**:

* `update_col`: extra column for updating entity
* `delete_col`: extra column for deleting entity

### TimelineTable (`tables.Table`):

Table for Timeline entities; used for generation bootstrap-table

**Attributes**:

* `delete_col`: extra column for deleting entity

## view.py

### `api_film(request)`:

REST endpoint for Film entity

* *param* request:
* *return* Film entity

### `api_cinema(request)`:

REST endpoint for Cinema entity

* *param* request:
* *return* Cinema entity

### `api_timeline(request)`:

REST endpoint for Timeline entity

* *param* request:
* *return* Cinema entity

### `api_poster(request)`:

REST endpoint for Poster entity

* *param* request:
* *return* Poster entity
   
### `api_hall(request)`:

REST endpoint for Hall entity

* *param* request:
* *return* Hall entity

### `api_ticket(request)`:

REST endpoint for Ticket entity

* *param* request:
* *return* Ticket entity

### `get_staff_job(request)`:

REST endpoint for Staff entity; used for getting Staff' job

* *param* request:
* *return* Staff entity

### `api_user(request)`:

REST endpoint for User entity

* *param* request:
* *return* User entity

### CreateUserView (`CreateAPIView`):

REST endpoint for creating new user


### `cinema_profile(request, cinema_id)`:

Get Cinema's profile

* *param* request
* *param* cinema_id: current cinema's ID
* *return* chosen Cinema

### `about_film(request, film_id)`:
    
Get Film's info

* *param* request:
* *param* film_id: current Film's ID
* *return* chosen Film

### `about_dev(request)`:

Get about dev page

* *param* request
* *return* about dev page

### `about_project(request)`:
    
Get about project page

* *param* request
* *return* about project page
     
### FilmTableView(`ExportMixin, SingleTableView`):
    
Get all Films entities as a table
    
#### `get(self, request, *args, **kwargs)`:
        
Returns Film's table

* *param* request
* *param* args
* *param* kwargs
* *return* Film's table       
        
#### `cinema_table_all(request)`:
    
Returns all Cinema entities as a table

* *param* request
* *return* Cinema's table
    
### `form_cinema_update(request, cinema_id)`:
    
Returns Cinema's update form

* *param* request
* *param* cinema_id: Cinema's ID for updating
* *return* web-page for updating
      
### `form_cinema_insert(request)`:
    
Returns Cinema's insert form

* *param* request
* *return* web-page for creating new entity

### `get_poster_table_by_cinema_id(request, cinema_id)`:
    
Returns all Poster entities with certain Cinema's ID value

* *param* request
* *param* cinema_id: linked Cinema's ID
* *return* table with all Posters 
    
### `form_poster_insert(request, cinema_id)`:
    
Returns Poster's insert form

* *param* request
* *param* cinema_id: linked Cinema's ID
* *return* web-page for creating new entity
    
### `get_timeline_table_by_cinema_id(request, cinema_id)`:
    
Returns all Timeline entities as a table with certain Cinema's ID value

* *param* request
* *param* cinema_id: linked Cinema's ID
* *return* table with all Timeline
        
    
### `form_timeline_insert(request, cinema_id)`:
    
Returns Timeline's insert form

* *param* request
* *param* cinema_id: linked Cinema's ID
* *return* web-page for creating new entity
     

### `get_hall_table_by_cinema_id(request, cinema_id)`:
    
Returns all Hall entities as a table with certain Cinema's ID value

* *param* request
* *param* cinema_id: linked Cinema's ID
* *return* table with all Hall
    
    
### `form_hall_insert(request, cinema_id)`:

Returns Hall's insert form

* *param* request
* *param* cinema_id: linked Hall's ID
* *return* web-page for creating new entity

    
### `form_hall_update(request, cinema_id, hall_id)`:

Returns Hall's update form

* *param* request
* *param* cinema_id: linked Cinema's ID
* *param* hall_id: Hall's ID for updating
* *return* web-page for updating
