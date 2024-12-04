import streamlit as st
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

if st.session_state["authentication_status"] is True:
  # Sidebar pour la navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Pages", ["Accueil", "Découverte de KAWS"])

    # Page Accueil
    if page == "Accueil":
        st.title("Bienvenue à vous, oh Wilder méritants !")
        st.image(
            "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjd4bWFwMmQ4NDl3NHc2cmZwcG5hYnllMDZsdmpxamdtNDZha281aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XD9o33QG9BoMis7iM4/giphy.gif",
            caption="En acceptant les CGV de site, vous agréez expressément à me donner votre âme 🥰",
            use_container_width=True,
        )

    # Page Découverte de KAWS
    elif page == "Découverte de KAWS":
        st.title("KAWS")
        col1, col2, col3 = st.columns(3)

        url = "https://fr.wikipedia.org/wiki/Kaws_(artiste)"
        st.write(
            "Si l'artiste vous intéresse, je vous invite à vous rendre sur la page Wikipedia de l'artiste [link](%s)" % url
        )

        with col1:
            st.image(
                "https://lynartstore.com/cdn/shop/files/KAWS_-THE-PROMISE-Black_-2022-LYNART-STORE-5921027.jpg?v=1728375799&width=823.jpeg",
                caption="Kaws : la transmission",
                use_container_width=True,
            )

        with col2:
            st.image(
                "https://images.cults3d.com/EGYNaN-SVMJ6TlRr1sUgY6oT0zo=/516x516/filters:no_upscale():format(webp)/https://fbi.cults3d.com/uploaders/19078557/illustration-file/1c806de5-6762-400e-8227-cb01777a8578/0000.png",
                caption="Why so serious ?",
                use_container_width=True,
            )

        with col3:
            st.image(
                "https://www.artetrama.com/cdn/shop/files/kaws-bff-time-off-blue-1.webp?v=1714488269.jpeg",
                caption="Affalé",
                use_container_width=True,
            )
            
    authenticator.logout("Déconnexion")
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')
