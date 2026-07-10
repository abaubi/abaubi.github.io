#!/bin/bash

# Sol·licitar el nom del repositori d'origen (Google AI Studio)
read -p "Introdueix el nom del repositori de Google AI Studio: " REPO_ORIGEN

# Sol·licitar el nom de la subcarpeta destí dins de /site
read -p "Introdueix el nom de la subcarpeta destí (dins de /site/): " CARPETA_DESTI

# Definir la URL del repositori origen utilitzant l'usuari abaubi
URL_ORIGEN="https://github.com/abaubi/${REPO_ORIGEN}.git"
RUTA_DESTI="site/${CARPETA_DESTI}"

echo "--------------------------------------------------"
echo "Sincronitzant ${URL_ORIGEN} a ${RUTA_DESTI}..."
echo "--------------------------------------------------"

# Executar el subtree pull per portar els canvis de la branca main
if git subtree pull --prefix="${RUTA_DESTI}" "${URL_ORIGEN}" main --squash; then
    echo "--------------------------------------------------"
    echo "✓ Canvis importats correctament a local."
    echo "Pujant els canvis a abaubi.github.io..."
    echo "--------------------------------------------------"
    
    # Pujar els canvis combinats al teu repositori principal
    git push origin main
    
    echo "--------------------------------------------------"
    echo "✓ Procés finalitzat amb èxit. Web actualitzada."
    echo "--------------------------------------------------"
else
    echo "--------------------------------------------------"
    echo "❌ Error en executar el subtree pull."
    echo "Verifica que els noms del repositori i de la carpeta siguin correctes."
    echo "--------------------------------------------------"
fi
