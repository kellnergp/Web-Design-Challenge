# Web-Design-Challenge

Pages Link: https://kellnergp.github.io/Web-Design-Challenge/

Use the data and plots from the WeatherPy section of the PythonAPI-Challenge to create a Github Pages site with an overview of the project.

Create 7 pages for the site, including:

1. A Landing Page with a Summary of the project, set as the home page in Github Pages
2. A Data page with a Bootstrap table containing all data used for the project
3. A Latitude vs Max Temperature page with the plot and a short analysis
4. A Latitude vs Humidity page with the plot and a short analysis
5. A Latitude vs Cloudiness page with the plot and a short analysis
6. A Latitude vs Wind Speed Page with the plot and a short analysis
7. A Comparisons page displaying all 4 plots

All pages must have a Bootstrap navbar with clearly understandable links to each page.

Each page also needs links to the Bootstrap style page and scripts to ensure the code runs correctly.

A shared CSS style page allows for common visual elements and indication of active page.

## Navbar

Place code for a Bootstrap Navbar object in the \<body> of each page.

Use the existing Bootstrap class to define it as a navbar with a dropdown menu included.

Create navbar-items with links to the Home, Comparisons, and Data pages.

Use the dropdown-menu class to create a dropdown selection for the 4 visualization pages and assign a dropdown-item to each page.

## Landing Page

Name the file for this page 'index.html'.

In the \<head> section, entitle the page 'Landing Page' and reference the Bootstrap style page and the 'style.css' file.

In the \<body> section, place the code for the navbar.

For the content of the page, use a Bootstrap grid.

The first 'row' div contains one column allocated 2/3 of the container for the primary page content on the left with the remaining 1/3 being the 'sidebar' on the right.

### Main Content

In the left-hand column there are 2 rows with the first containing the page header describing project.

The second row contains 2 columns; one on the left with an example image of one of the plots and one on the right with a summary of the project, its means, and its goals.

### Sidebar

The right-hand column contains the 'sidebar' for the page displaying the 4 visualizations.

This section has two rows with each row comprised of two column sections.

In each of the sub-columns there is an image of one of the plot visualizations with a class of 'img-fluid' so that they will scale themselves properly to the viewport size.

