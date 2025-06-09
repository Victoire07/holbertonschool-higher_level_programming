# README projet restful-api :

📚 0. Basics of HTTP/HTTPS :

🔀 DIFFERENCE ENTRE HTTP ET HTTPS : 

HTTP : ❌ 
° Ce n'est pas sécurisé : les données sont envoyées en clair. Tout le monde interceptant la connexion peut lire ou modifier les données comme des mots de passe par exemple
° souvent marqué comme "Non sécurisé" dans la barre d’adresse
° Mieux vaut l'utiliser uniquement pour des sites sans données sensibles

HTTPS : ✅
° C'est sécurisé : les données sont chiffrées grâce à SSL/TLS. Même en cas d’interception, les données sont illisibles sans la clé de déchiffrement
° Affichage d’un cadenas : signe visuel de sécurité
° À utiliser obligatoirement pour les formulaires, connexions, paiements... 


🔍 4 MÉTHODES HTTP COURANTES + EXPLICATION DE LEUR USAGE :

👉 1. GET / 2. POST / 3. PUT / 4. DELETE

1️⃣ GET
Utilité : Récupérer des données depuis le serveur

2️⃣ POST
Utilité : Envoyer des données pour créer une nouvelle ressource

3️⃣ PUT
Utilité : Remplacer entièrement une ressource existante

4️⃣ DELETE
Utilité : Supprimer une ressource du serveur


🧾 5 codes de statut HTTP fréquents + EXPLICATION :

1️⃣ 200 OK : "Réponse standard pour les requêtes HTTP réussies. La réponse dépend de la méthode de requête utilisée. Dans une requête GET, la réponse contient une entité correspondant à la ressource demandée. Dans une requête POST, la réponse contient une entité décrivant ou contenant le résultat de l'action" (source : Ressource Holberton : https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

2️⃣ 201 Created : "La demande a été satisfaite, ce qui a donné lieu à la création d'une nouvelle ressource" (source : Ressource Holberton : https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

3️⃣  400 Bad Request : "Le serveur ne peut pas ou ne veut pas traiter la demande en raison d'une erreur client apparente. Par exemple, une syntaxe de demande mal formée, une taille trop grande, un cadrage de message de demande non valide ou un routage de demande trompeur" (source : Ressource Holberton : https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

4️⃣ 404 Not Found : "La ressource demandée est introuvable, mais pourrait être disponible ultérieurement. Le client peut effectuer des demandes ultérieures" (source : Ressource Holberton : https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

5️⃣ 500 Internal Server Error : "Un message d'erreur générique, émis lorsqu'une condition inattendue a été rencontrée et qu'aucun message plus spécifique n'est approprié" (source : Ressource Holberton : https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
