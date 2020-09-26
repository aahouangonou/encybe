#coding:utf-8 
 

import cgi
import sys
import codecs


import codecs
import os

sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())

print("content-type:text/html;charset=utf-8\n")

entete="""<!DOCTYPE html>

  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="utf-8"/>
  <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
  <title>Accueil EncyBe</title>
  <meta name="description" content="Thoughts, reviews and ideas since 1999."/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <link rel="shortcut icon" href="#">
  <link rel="stylesheet" type="text/css" href="assets/css/screen.css"/>
  <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Roboto:400,300italic,300,400italic,700,700italic|Playfair+Display:400,700,400italic,700italic"/>
  </head>
    <style type="text/css">/* Style the header with a grey background and some padding */
.header {
  overflow: hidden;
  background-color: black;
  padding: 10px 5px;
}

/* Style the header links */
.header a {
  float: center;
  color: white;
  text-align: left;
  padding: 10px;
  text-decoration: none;
  font-size: 18px;
  line-height: 25px;
  border-radius: 4px;
  display: flex;
  display: inline-block;
}

/* Style the logo link (notice that we set the same value of line-height and font-size to prevent the header to increase when the font gets bigger */
.header a.logo {
  font-size: 25px;
  font-weight: bold;
  display: flex;
}

/* Change the background color on mouse-over */
.header a:hover {
  background-color: orange;
  color: white;
}

/* Style the active/current link*/
.header a.active {
  background-color: dodgerblue;
  color: white;
}

/* Float the link section to the right */
.header-right {
  float: right;
}

/* Add media queries for responsiveness - when the screen is 500px wide or less, stack the links on top of each other */
@media screen and (max-width: 500px) {
  .header a {
    float: none;
    display: inline-block;
    text-align: center;
  }
  .header-right {
    float: none;
  }
}
</style>
  <body class="home-template">
    <div class="header">
  
  <div class="header-center" style="margin-bottom: -20px; ">
    <div style="width: 25%;display: inline-block;">
      <a href="#" class="logo"><img src="assets/img/logo.png" alt="EncyBe"/></a>
    </div>
    <div style="display: inline-block;vertical-align: top;margin-top: 15px;">
      <ul style="list-style-type: none;">
        <li style="display: inline-block;"><a  href="pre_inscription.py">Accueil</a></li>

        <li style="display: inline-block;"><a href="article.py">Articles</a></li>
        <li style="display: inline-block;"><a href="#contact">Espace Logiciel</a></li>
        <li style="display: inline-block;"><a href="contact.py">Contactez-nous</a></li>
        <li style="display: inline-block;"><a href="connexion.py">Connectez-vous</a></li>
      </ul>
    </div>
    
    
  </div>




</div>


</div>"""

html="""
	<header class="main-header " style="background-image: url(assets/img/xxx.jpg)">
	<div class="vertical">
		<div class="main-header-content inner">
			<h1 class="title_encybe">EncyBe</h1>
			<div class="entry-title-divider">
				<span></span><span></span><span></span>
			</div>
			<h2 class="page-description">Tout le savoir du monde en un clique.</h2>
		</div>
	</div>
	<a class="scroll-down icon-arrow-left" href="#content" data-offset="-0"><span class="hidden">Scroll Down</span></a>
	</header>
	
	
	</div>
	</div>
	</main>
  <style="text-align:center">
	<div class="header">
  
  <div class="header-center" style="margin-bottom: -20px; ">
    
    <div style="display: inline-block;vertical-align: top;margin-top: 15px;">
      <ul style="list-style-type: none;">
        <li style="display: inline-block;"><a  href="accueil.py">Accueil</a></li>
        <li style="display: inline-block;"><a href="article.py">Articles</a></li>
        <li style="display: inline-block;"><a href="profil.py">Espace Logiciel</a></li>

        <li style="display: inline-block;"><a  href="contact.py">Contactez-nous</a></li>
                <li style="display: inline-block;"><a href="#">A propos</a></li>
                        <li style="display: inline-block;"><a href="#">Politique de confidentialité</a></li>



        <li style="display: inline-block;"><a href="contact.py"></a></li>
      </ul>
    </div>
    
    
  </div>




</div>


</div>
</div>
	</footer>
</div>

</body>
</html>
"""
print(entete)
print(html)
