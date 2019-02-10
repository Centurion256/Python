# What is MovieLocator?

MapLocator is a project written in Python 3.0 that allows for creation of customizable color-coded maps based on movies produced each year. It uses the locations.list dataset provided by IMDB.


## Why was it created?

MapLocator was created for an assignment of the Computer Science course.
   

## How can I utilize it?

As of now, you can use this module to generate maps in .html format and analyse the relations between population and movie releases.

## What packages does it use?

MapLocator uses folium to create maps. Folium, respectively, uses maps provided by OpenStreetMap project.


## Installation

You can clone this repository or individually download the files listed. If you use PyCharm, the packages required to run this module will be provided in the requirements.txt. Otherwise, you will have to install them manually. 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install __folium__ and __branca__.

```bash
pip install folium
pip install branca
```

## State of the project

As of now, the project is barebones since it was made in a few days. I do, however, welcome any contribution to it. If I do return to it at some point in future, I'll update it with new features. For more info, take a look at the __roadmap__ section  

## Roadmap

* Add a layer with filming locations of 100 highest-rated movies on IMDB with the help of geopy package
* Make dynamic population color indicators using the json package
* Fix bugs


## This looks interesting. Can I contribute?
Sure! Both pull and push requests are welcome. If you would like to make any major changes, please open an issue first.


## HTML-tag description

```HTML
<!DOCTYPE html> <!-- a DTD, which is crucial tag which tell the browser how to render the page 0 -->

<head> <!-- an opening head element tag, which contains information about the webpage -->
    
    <meta/> <!-- specifies charsets and page descriptions -->
    <script></script> <!-- a tag for JavaScript code -->
    <link/> <!-- a tag used to add style sheets -->
    <style> <!-- an opening tag for declaring style sheets -->
    </style> <!-- a closing style tag -->

</head> <!-- a closing head tag -->
<body> <!-- an opening tag which holds all the main content of the page -->

    <div></div> <!-- nests a block of content; a container -->

</body> <!-- a closing body tag -->

```
## License
This project is distributed under the
[MIT](https://choosealicense.com/licenses/mit/) license.