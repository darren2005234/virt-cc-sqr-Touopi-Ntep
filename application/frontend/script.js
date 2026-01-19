const input = document.getElementById("input");
const message = document.getElementById("message");

// frontend/js/app.js
const API_URL = "http://localhost:8000/api"; // pour navigateur local



/* Ajouter un caractère */
function addChar(char) {
    input.value += (char === 'x') ? '*' : char;
}

/* Supprimer */
function delChar() {
    input.value = input.value.slice(0, -1);
}

/* Annuler */
function cancelAction() {
    input.value = "";
    message.textContent = "Entrez votre calcul";
}

/* Envoyer le calcul (POST) avec validation côté client */
async function validateInput() {
    const expr = input.value.trim();
    if (expr === "") {
        message.textContent = "Entrez une expression valide !";
        return;
    }

    // Vérifier que l'expression contient seulement des caractères autorisés
    if (!/^[0-9+\-*/().\s]+$/.test(expr)) {
        message.textContent = "Expression invalide  (caractères interdits)";
        return;
    }

    // Optionnel : tester si l'expression peut être évaluée sans erreur
    try {
        // eslint-disable-next-line no-eval
        eval(expr);
    } catch (err) {
        message.textContent = "Expression invalide (erreur de syntaxe)";
        return;
    }

    message.textContent = "Calcul envoyé...";

    try {
        const response = await fetch(`${API_URL}/calcul/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ expression: expr })
        });

        if (!response.ok) {
            message.textContent = `Erreur serveur (${response.status})`;
            alert ("erreur serveur");
            return;
        }

        const data = await response.json();

        if (!data.id) {
            message.textContent = "Erreur serveur : ID manquant";
            return;
        }

        input.value = data.id; // Remplace le calcul par l'ID
        message.textContent = "Calcul enregistré (conservez l'ID)";
    } catch (err) {
        message.textContent = "Erreur réseau";
        console.error(err);
    }
}


/* Récupérer le résultat */
async function getResult() {
    const id = input.value.trim();
    if (!id) return;

    message.textContent = "Vérification du résultat...";

    try {
        const response = await fetch(`${API_URL}/calcul/${id}/`);
        const data = await response.json();

        if (data.statut === "TERMINE") {
            input.value = data.resultat;
            message.textContent = "Résultat disponible";
        } else {
            message.textContent = "Calcul en cours… ";
        }
    } catch (err) {
        message.textContent = "Erreur réseau";
        console.error(err);
        
    }
} 
// Afficher la section pour saisir l'ID
function showSearch() {
    document.getElementById("search-section").style.display = "block";
    message.textContent = "Entrez l'ID pour récupérer le résultat";
}

async function searchById() {
    const id = document.getElementById("search-id").value.trim();

    if (!id) {
        message.textContent = "Veuillez saisir un ID valide";
        return;
    }

    message.textContent = "Récupération du résultat...";

    try {
        const response = await fetch(`${API_URL}/calcul/${id}/`);

        if (response.status === 404) {
            message.textContent = "ID introuvable";
            return;
        }

        if (!response.ok) {
            message.textContent = `Erreur serveur (${response.status})`;
            return;
        }

        const data = await response.json();

        if (data.statut === "TERMINE") {
            message.textContent = `Résultat : ${data.resultat}`;
            input.value = data.resultat; // si tu veux mettre le résultat dans l'input
        } else {
            message.textContent = "Calcul en cours…";
        }
    } catch (err) {
        message.textContent = "Erreur réseau";
        console.error(err);
    }
}
