# Ex.08 Design of Interactive Image Gallery

## AIM
  To design a web application for an inteactive image gallery with minimum five images.

## DESIGN STEPS

## Step 1:

Clone the github repository and create Django admin interface

## Step 2:

Change settings.py file to allow request from all hosts.

## Step 3:

Use CSS for positioning and styling.

## Step 4:

Write JavaScript program for implementing interactivit

## Step 5:

Validate the HTML and CSS code

## Step 6:

Publish the website in the given URL.

## PROGRAM

## galler.html

```
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Interactive Gallery</title>
    <style>
        .grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
        }
        .grid img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 8px;
            cursor: pointer;
        }
        #popup {
            display: none;
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(0,0,0,0.8);
            justify-content: center;
            align-items: center;
        }
        #popup img {
            width: 60%;
            border-radius: 10px;
        }
    </style>
</head>
<body>

<h2>Interactive Image Gallery</h2>

<div class="grid">
    {% for img in images %}
        <img src="{% static img %}" onclick="openPopup(this.src)">
    {% endfor %}
</div>

<div id="popup" onclick="closePopup()">
    <img id="popupImg">
</div>

<script>
    function openPopup(src){
        document.getElementById("popupImg").src = src;
        document.getElementById("popup").style.display = "flex";
    }
    function closePopup(){
        document.getElementById("popup").style.display = "none";
    }
</script>

</body>

</html>
```



## OUTPUT

<img width="1909" height="1046" alt="image" src="https://github.com/user-attachments/assets/dad5e8de-82b9-40a4-8684-6ef697b68b04" />

<img width="1919" height="1098" alt="image" src="https://github.com/user-attachments/assets/7abfc77d-5742-4762-a073-24d38b408130" />






## RESULT
  The program for designing an interactive image gallery using HTML, CSS and JavaScript is executed successfully.
