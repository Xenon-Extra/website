# Xenon-Extra Website
> The website for Xenon Extra

Explanation:
* All the pages inherit from the `base.html` file, which has the Navbar
* In the `base.html` file, there is a section that goes like so:

    >{% block content %} {% endblock %}

* This is the part that gets swapped out. In the other files, such as `about.html` or `index.html` or `pricing.html`, you can swap everything between the content blocks with HTML and CSS.