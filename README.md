# Django - Crud
# Feature Tasks 
- snacks_crud_project Django project
    - snacks app
    - Snack model
        - title field
        - purchaser field
        - description field

- `SnackListView` that extends appropriate generic view
associated url path is an `empty string`
- `SnackDetailView` that extends appropriate generic view
associated url path is `<int:pk>/`
- `SnackCreateView` that extends appropriate generic view
associated url path is `create/`
- `SnackUpdateView` that extends appropriate generic view
associated url path is `<int:pk>/update/`
- `SnackDeleteView` that extends appropriate generic view
associated url path is `<int:pk>/delete/`
- urls to support all views, with appropriate names
- templates support all views
- navigation links in appropriate locations to access all pages

# To run this project in your device : 
```
- $ git clone git@github.com:ayat93a/crud-snacks.git
- $ cd snacks_crud_project
- $ poetry install
- $ poetry shell
- $ python manage.py runserver
```