from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

#pour trouver des emojis : webfx.com/tools/emoji-cheat-sheet
st.set_page_config(page_title="Mon portfolio", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#utiliser le CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#-----LOAD ASSETS------
lottie_girl = load_lottieurl("https://lottie.host/c7931b93-c8d5-4ac4-9212-57dd018d538f/ksZntAqqbB.json")
img_moodle = Image.open("images/moodle.png")
img_filboost = Image.open("images/filboost.png")
img_affiche = Image.open("images/affiche.png")
img_procreate = Image.open("images/procreate.png")
img_livres = Image.open("images/livres.png")
img_criminou = Image.open("images/criminou.png")
img_plats = Image.open("images/plats.png")
img_notionhome = Image.open("images/notionhome.png")
img_notionmaslow = Image.open("images/notionmaslow.png")
img_notioncuisine = Image.open("images/notioncuisine.png")
img_notionrevisions = Image.open("images/notionrevisions.png")
img_moodlefigma = Image.open("images/moodlefigma.png")
img_portraits = Image.open("images/portraits.png")
img_morpion = Image.open("images/morpion.png")
img_site = Image.open("images/site.png")
img_bandedessinee = Image.open("images/bandedessinee.png")
img_page1 = Image.open("images/page1.png")
img_page19 = Image.open("images/page19.png")
img_page21 = Image.open("images/page21.png")
img_page23 = Image.open("images/page23.png")
img_mamabulle = Image.open("images/mamabulle.png")
img_theblessedclub = Image.open("images/theblessedclub.png")
img_complementsbblj = Image.open("images/complementsbblj.png")
img_feedbblj = Image.open("images/feedbblj.png")
img_programmebblj = Image.open("images/programmebblj.png")
img_guidevoiture  = Image.open("images/guidevoiture.png")
img_guidevoiturepage7 = Image.open("images/guidevoiturepage7.png")
img_chefwascute = Image.open("images/chefwascute.png")
img_kissthechef = Image.open("images/kissthechef.png")
img_affiches = Image.open("images/affiches.png")



#Header
with st.container():
    st.subheader("Bonjour, je m'appelle Marina :wave:")
    st.write("Je suis en train d'apprendre le Python en créant ce portfolio")
    st.write("Découvrez qui je suis ainsi que mes travaux ici !")

#qui suis-je
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Qui suis-je ?")
        st.write("##")
        st.write(
            """
            Depuis petite je suis passionnée par deux choses.
Ma première passion, c'est de créer. Cuisiner (j'ai écrit deux livres), dessiner, peindre, fabriquer des objets, des bijoux, des vêtements, rénover de vieux meubles, faire de la couture, des perles, de la poterie...
Bref : je suis très manuelle et très créative.


Ma deuxième passion ? Les ordinateurs !
J'ai grandi avec vieil ordinateur sous Windows XP, sans même internet ! J'adorais explorer, cliquer partout pour comprendre comment cela fonctionne.

""" 

#expérience
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Mon expérience professionnelle")
        st.write("##")
        st.write(
"""
- Je suis créatrice de contenu sur les réseaux sociaux ce qui m'a appris à communiquer, créer des visuels efficaces, créatifs, originaux et faire une veille constante. Cela m'a permis de réunir en 3 mois 50 000 abonnés.
- J'ai été assistante de communication pour une influenceuse Fitness qui m'a chargée de certains gros projets comme la création d'une gamme de compléments alimentaires bio, made in France, le design de ses packagings, la création d'une charte grahique.
Le fitness est un secteur où il y a beaucoup de concurrence, il était donc nécessaire de se démarquer et d'être toujours au courant des dernières tendances.
- J'ai fait des missions freelance pour des auto-entrepreneurs qui avaient besoin d'une nouvelle identité visuelle, de mockups pour un site internet, de logo...

Concernant mes études, je suis diplômée d'une licence de psychologie et étudie actuellement en master Sciences Cognitives parcours IA à l'IDMC de Nancy.
Ma connaissance de l'Humain acquise lors de ma licence me permettra d'intégrer la technologie et l'IA tout en respectant des principes éthiques. 
Et celà bien-sûr avec ma touche de créativité pour rendre votre entreprise unique !


            """
        )
with right_column:
    st_lottie(lottie_girl, height=300, key="coding")

#projets 
with st.container():
    st.write("---") #c'est le divider
    st.header("Mes projets")
    st.write("##") #hashtag pour chaque colonne
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_filboost)
    with text_column :
        st.subheader("Identité visuelle de Filboost")
        st.write(
            """
                 Voici l'avant/après du feed Instagram de l'entreprise. 
                 """
                 )


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_affiche)
    with text_column:
        st.subheader("Affiche de recrutement de participants")
        st.write(
            """
            Voici l'avant/après d'une affiche de recrutement de participants pour une expérience sur la psychologie et la musique.
            """
        )


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_moodle)
    with text_column:
        st.subheader("Proposition de refonte de Moodle")
        st.write(
            """
            Voici l'avant/après de Moodle tel que je l'imagine. Ici vous voyez Moodle tel qu'il est actuellement
            """
        )
        st.markdown("[Voir en vrai](https://moodle.univ-lille.fr)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_moodlefigma)
    with text_column:
        st.write(
            """
            Et voici ma proposition !
            """
        )
        st.markdown("[Voir sur Figma](https://www.figma.com/file/f02LfNdSTNNk6LIL2KQh8O/MOODLE?type=design&node-id=3101%3A2&mode=design&t=3tFdqvqPXnG2EO0W-1)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_mamabulle)
    with text_column:
        st.subheader("Charte graphique de Mam'a Bulle")
        st.write(
            """
            J'ai réalisé une charte graphique et le mock-up d'un site internet pour l'entreprise MamaBulle : réflexologie et accompagnement en périnatalité.
            """
        )
        st.markdown("[Voir la charte entière](https://www.fichier-pdf.fr/2024/05/30/presentation-mama-bulle/)")


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_theblessedclub)
    with text_column:
        st.subheader("Charte graphique de The Blessed Club")
        st.write(
            """
            J'ai réalisé une charte graphique et le mock-up d'une appli mobile pour The Blessed Club : rencontres amoureuses et amicales entre chrétiens.
            """
        )
        st.markdown("[Voir la charte entière](https://www.fichier-pdf.fr/2024/06/17/presentation-the-blessed-clb/)")
        

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_feedbblj)
    with text_column:
        st.subheader("Charte graphique de Bombshell by Lucile Joseph")
        st.write(
            """
            Lucile Joseph est coach sportive diplômée et vends des programmes sportifs et nutritionnels en ligne sur son site internet. J'ai travaillé pour elle pendant un an et demi en tant qu'assistante de communication.
            L'une de mes premières missions a été de faire une refonte de son feed Instagram pour le rendre plus à son image. 
            
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_programmebblj)
    with text_column:
        st.subheader("Refonte des programmes sportifs de Lucile Joseph")
        st.write(
            """
            J'ai ensuite travaillé sur la refonte de ses programmes sportifs.
            """
        )

        
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_complementsbblj)
    with text_column:
        st.subheader("Création d'une gamme de compléments alimentaires")
        st.write(
            """
           Enfin j'ai géré un projet de création d'une gamme de compléments alimentaires (gélules) bio et made in France. 
           En plus du contact avec le laboratoire, de l'élaboration des formules et du choix des noms, j'ai aussi travaillé sur le design des packagings.
            """
        )


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_site)
    with text_column:
        st.subheader("Mon site de cuisine")
        st.write(
            """
            Voici mon site internet "1repas1euro". Il vient tout juste d'être refait donc il n'y a pas encore énormément de contenu dessus car je dois tout remettre à la main !
            """
        )
        st.markdown("[Voir le site](https://1repas1euro.fr)")


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_guidevoiture)
    with text_column:
        st.subheader("Mes ebooks")
        st.write(
            """
            J'ai créé plusieurs ebooks sur diverses thématiques, par exemple celui-ci pour apprendre à choisir une voiture d'occasion : vérifier la fiabilité du vendeur, l'extérieur et l'intérieur du véhicule, l'essai routier...
            """
        )
        st.markdown("[Voir l'ebook](https://1repas1euro.fr/wp-content/uploads/2024/07/Guide-voiture-2-compresse.pdf)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_guidevoiturepage7)
    with text_column:
        st.write(
            """
            La page 7.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_livres)
    with text_column:
        st.subheader("Mes deux livres de cuisine")
        st.write(
            """
            Voici les deux livres que j'ai écrits, édités par la maison SOLAR.
            """
        )
 
        
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_notionhome)
    with text_column:
        st.subheader("Mon deuxième cerveau sur Notion")
        st.write(
            """
            J'ai créé un espace Notion appellé "mon deuxième cerveau", afin d'organiser toutes les sphères de ma vie :
            études, ménage, cuisine, suivi de candidatures, rendez-vous médicaux et bien d'autres ! Voici la page d'accueil avec la navigation.
            """
        )
        st.markdown("[pour voir le template entier](https://silly-trout-24d.notion.site/Bonjour-pr-nom-a6bc4328e8074461a5e6694606ecef00?pvs=4)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_notionmaslow)
    with text_column:
        st.write(
            """
            Ici, c'est la pyramide de Maslow. Elle permet d'identifier les aspects de ma vie sur lesquels je suis satisfaite et ceux que je devrais améliorer pour me sentir mieux.
            C'est un bon exemple de la combinaison de mes connaissances en psychologie et de mon envie de créer des outils technologiques.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_notionrevisions)
    with text_column:
        st.write(
            """
            Par ici un outil pour organiser mes révisions en vue des examens.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_notioncuisine)
    with text_column:
        st.write(
            """
            Ici c'est la cuisine avec un inventaire : je coche les ingrédients que j'ai à la maison et il m'affiche les recettes que je peux réaliser sans avoir besoin de faire des achats !
            """
        )


#loisirs 
with st.container():
    st.write("---") #c'est le divider
    st.header("Mes loisirs")
    st.write("##") #hashtag pour chaque colonne
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_procreate)
    with text_column :
        st.subheader("Dessin")
        st.write(
            """
                 Du dessin digital...Voici des dessins réalisés sur Procreate. 
                 """
                 )
        st.markdown("[Voir le timelapse d'un dessin](https://youtu.be/g4fSyc2o_AQ)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_bandedessinee)
    with text_column:
        st.subheader("Bande dessinée")
        st.write(
            """
            J'ai réalisé une bande dessinée de 22 pages pour offrir. Chaque planche représente un souvenir vécu avec la personne. J'ai créé les cases et les bulles avec Canva. J'ai ensuite exporté le document et ai dessiné sur Procreate.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_page1)
    with text_column:
        st.write(
            """
            La première de couverture.
            """
        )


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_page19)
    with text_column:
        st.write(
            """
            La page 19.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_page21)
    with text_column:
        st.write(
            """
            La page 21.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_page23)
    with text_column:
        st.write(
            """
            La page 23.
            """
        )


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_affiches)
    with text_column:
        st.subheader("Dessin d'affiches")
        st.write(
            """
            J'ai réalisé quelques affiches décoratives.
            """
        )

        with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_chefwascute)
    with text_column:
        st.write(
            """
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_kissthechef)
    with text_column:
        st.write(
            """

            """
        )



with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_plats)
    with text_column:
        st.subheader("J'essaie d'apprendre la photo")
        st.write(
            """
            J'aimerais pouvoir photographier mes recettes de façon professionnelle, j'essaie donc d'apprendre dans ce domaine.
            """
        )


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_portraits)
    with text_column:
        st.write(
            """
            Et la photo de portraits aussi. Ici ce sont des autoportraits.
            """
        )


#formulaire de contact
with st.container():
    st.write("---")
    st.header("Contactez-moi !")
    st.write("##")

    #formsubmit.com 
    contact_form = """
    <form action="https://formsubmit.co/marinanowicki@outlook.fr" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="nom" placeholder="Votre nom" requiered>
        <input type="email" name="email" placeholder="Votre email" requiered>
        <textarea name="message" placeholder="Votre message" requiered></textarea>
        <button type="submit">Envoyer</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
