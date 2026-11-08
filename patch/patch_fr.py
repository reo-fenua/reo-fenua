# Reo Fenua : patch principal appliqué à bitchat-android par le workflow build-apk.yml.
# Ne pas lancer à la main : le workflow l'exécute dans le dossier « upstream ».
import re, pathlib, os

def warn(msg):
    print(f"::warning::{msg}")

RES = pathlib.Path("app/src/main/res")
UI = pathlib.Path("app/src/main/java/com/bitchat/android/ui")

FR_EXTRA = r'''cashu_pay_via	payer avec Cashu
cashu_payment_description	Paiement Cashu
cashu_copy_token	Copier le jeton
cashu_redeem_wallet	Encaisser dans le portefeuille
cashu_redeem_web	Encaisser sur le web
mesh_service_channel_name	Réseau en arrière-plan
mesh_service_channel_desc	Garde le réseau Bluetooth actif en arrière-plan
cd_favorite	Favori
cd_favorited_you	Vous a mis en favori
conversations	Conversations
offline_not_in_mesh	Hors ligne · pas dans le réseau
offline_reachable_via_nostr	Hors du réseau local · joignable par internet
delete	Supprimer
delete_conversation_action	Supprimer la conversation
delete_conversation_title	Supprimer la conversation ?
delete_conversation_message	Supprimer votre conversation avec %1$s de ce téléphone ?
search_conversations	Chercher une conversation
clear	Effacer
loading_conversations	Chargement des conversations privées…
conversation_storage_error	Impossible de charger les conversations privées
no_conversations_yet	Vos conversations privées apparaîtront ici
no_conversation_results	Aucune conversation trouvée
online_conversations	EN LIGNE
offline_conversations	HORS LIGNE
mark_read	Marquer comme lu
mark_unread	Marquer comme non lu
pin_conversation	Épingler
unpin_conversation	Désépingler
mute_conversation	Mettre en sourdine
unmute_conversation	Réactiver le son
conversation_actions	Actions sur la conversation
conversation_unread_count	%1$d messages non lus
conversation_read	Lu
conversation_draft_preview	Brouillon : %1$s
conversation_you_preview	Vous : %1$s
conversation_preview_timestamp	· %1$s
conversation_delete_failed	Impossible de supprimer la conversation
conversation_deleted	Conversation avec %1$s supprimée
undo	Annuler
conversation_restore_failed	Impossible de restaurer la conversation
notification_reply	Répondre
notification_mark_read	Marquer lu
notification_private_message	Nouveau message privé
notification_content_hidden	Ouvrez Reo Fenua pour le lire
notification_channel_direct_messages	Messages privés
notification_channel_direct_messages_description	Notifications des messages privés
notification_channel_geohash	Discussions par lieu
notification_channel_geohash_description	Notifications des mentions et messages dans les discussions par lieu
you	Vous
cd_location_notes	Notes du lieu
private_media_legacy_title	Envoyer sans chiffrement ?
private_media_legacy_body	%1$s ne peut pas être envoyé chiffré à %2$s car son application est trop ancienne. %3$s
private_media_legacy_send_once	Envoyer ce fichier une fois
panic_confirm_title	Tout effacer ?
panic_confirm_body	Cela efface définitivement votre identité, vos clés, vos messages et vos fichiers sur ce téléphone, puis crée une nouvelle identité. Impossible d'annuler.
panic_confirm_action	Effacer
system_panic_completed	tout est effacé — nouvelle identité créée
system_panic_incomplete	effacement incomplet — touchez 3 fois le logo pour réessayer.
cd_save_current_image	Enregistrer l'image
cd_close	Fermer
toast_image_saved	Image enregistrée dans Téléchargements
toast_failed_to_save_image	Impossible d'enregistrer l'image
cd_image_index_of	Image %1$d sur %2$d
cd_pick_file	Choisir un fichier
about_tagline	La voix du fenua, même sans réseau
about_tab_info	Infos
about_tab_settings	Réglages
about_how_to_use_heading	Mode d'emploi
about_howto_nickname	Touchez votre nom pour le changer
about_howto_channels	Touchez le nom du canal pour changer de canal
about_howto_people	Touchez l'icône des personnes pour voir qui est là
about_howto_bookmark	Ajoutez un canal en favori pour le garder
about_howto_mention	Tapez @ pour citer quelqu'un
about_howto_commands	Tapez / pour voir les commandes
about_howto_panic	Touchez 3 fois le logo pour tout effacer
about_section_about	À propos
about_section_theme	Apparence
about_section_settings	Réglages
about_no_tracking_title	Aucun pistage
about_no_tracking_desc	Pas de serveur, pas de compte, aucune donnée collectée.
about_ephemeral_title	Identité temporaire
about_ephemeral_desc	Un nouvel identifiant est créé régulièrement.
about_panic_desc	Touchez 3 fois le logo pour tout effacer immédiatement.
about_tor_title	Réseau Tor
about_difficulty	Difficulté
about_difficulty_value	%1$d bits • %2$s
about_tor_connected	Connecté (%1$d%%)
about_tor_disconnected	Déconnecté
chat_ui_matrix	Texte
chat_ui_bubbles	Bulles
cd_privacy_protected	Vie privée protégée
share_bitchat_title	Partager Reo Fenua
share_bitchat_subtitle	Partager le fichier d'installation, sans internet
share_apk_title	Partager l'application Reo Fenua
share_apk_explanation	Cela partage le fichier d'installation de Reo Fenua pour que d'autres l'installent sans internet. Plus il y a de téléphones, plus le réseau porte loin !
share_apk_receiver_instructions	La personne qui reçoit doit :\n• Autoriser « Installer des applis inconnues » dans les réglages Android\n• Désinstaller l'ancienne version si elle vient d'ailleurs (signatures différentes)
share_apk_confirm	Partager
share_apk_chooser_title	Partager Reo Fenua avec…
share_apk_error	Impossible de préparer l'application. Réessayez.
prepare_apk_title	Préparer l'application à partager
prepare_apk_ready_title	Application prête à partager sans internet
prepare_apk_subtitle	Télécharger la version universelle pour la partager
prepare_apk_status_not_downloaded	Pas prête • Touchez pour télécharger
prepare_apk_status_ready	Prête à partager
prepare_apk_ready_detail	Prête à partager • %1$s • %2$d Mo\n%3$s
prepare_apk_status_resumable	%1$s • %2$d%% téléchargé
prepare_apk_source_installed	Source : cette application installée
prepare_apk_source_installed_arm64	Source : cette application installée • téléphones ARM64 seulement
prepare_apk_source_downloaded	Source : version universelle téléchargée et vérifiée
prepare_apk_update_available	La version %1$s est disponible. Vous pouvez continuer à partager celle-ci ou télécharger la nouvelle.
prepare_apk_update_warning	Nouvelle version disponible
prepare_apk_get_universal	Télécharger la version universelle
prepare_apk_retry	Réessayer
prepare_apk_status_downloading	Téléchargement… %1$d%%
prepare_apk_phase_awaiting_connectivity	En attente du réseau…
prepare_apk_phase_retrying	Nouvel essai…
prepare_apk_phase_selecting_source	Choix de la source…
prepare_apk_phase_awaiting_route	En attente de Tor…
prepare_apk_phase_transferring	Téléchargement…
prepare_apk_phase_verifying_signature	Vérification de la signature…
prepare_apk_stop	Arrêter
prepare_apk_button_prepare	Préparer
prepare_apk_button_delete	Supprimer
prepare_apk_info	Version %1$s • %2$d Mo
prepare_apk_dialog_title	Télécharger la version universelle ?
prepare_apk_update_dialog_title	Télécharger la nouvelle version universelle ?
prepare_apk_dialog_message_unknown_size	Cela télécharge une version universelle vérifiée. Il suffit de le faire une fois.
prepare_apk_update_dialog_message	La version %1$s est disponible sur GitHub (%2$d Mo). Vous pouvez continuer à partager l'actuelle pendant le téléchargement.
prepare_apk_dialog_confirm	Télécharger
prepare_apk_downloading_title	Téléchargement de la version universelle
prepare_apk_downloading_message	Téléchargement de %1$d Mo…
prepare_apk_success	Version universelle prête !
prepare_apk_error_network	Erreur réseau. Vérifiez votre connexion.
prepare_apk_error_storage	Pas assez d'espace de stockage.
prepare_apk_error_rate_limited	%1$s est momentanément limité. Réessayez plus tard.
prepare_apk_error_no_universal	%1$s n'a pas de version universelle pour le moment.
prepare_apk_error_http	Échec du téléchargement depuis %1$s : HTTP %2$s %3$s
prepare_apk_error_generic	Échec du téléchargement. Réessayez.
prepare_apk_error_storage_needed	Pas assez d'espace : %1$s Mo nécessaires, %2$s Mo libres.
prepare_apk_error_no_sources	Aucune source de téléchargement configurée.
prepare_apk_error_tor_connecting	Tor se connecte encore. Réessayez quand il est prêt.
prepare_apk_error_no_url	%1$s n'a pas de lien utilisable.
prepare_apk_error_unreachable	Impossible de joindre %1$s.
prepare_apk_error_insecure_redirect	%1$s redirige vers un lien non sécurisé.
prepare_apk_error_resume_rejected	%1$s a refusé la reprise. Le prochain essai recommencera depuis le début.
prepare_apk_error_incomplete	Le téléchargement depuis %1$s s'est arrêté avant la fin. Il peut être repris.
prepare_apk_error_invalid_resume	%1$s a mal répondu à la reprise. Le prochain essai recommencera depuis le début.
prepare_apk_error_untrusted_key	L'application venant de %1$s n'est pas signée par une clé de confiance.
prepare_apk_error_not_universal	%1$s a envoyé une version pour un seul type de téléphone, pas la version universelle.
prepare_apk_error_apk_unreadable	Le fichier téléchargé est illisible.
prepare_apk_error_not_bitchat	Le fichier téléchargé n'est pas la bonne application.
prepare_apk_error_no_version	Le fichier téléchargé n'a pas de numéro de version.
prepare_apk_error_source_failed	Échec du téléchargement depuis %1$s.
prepare_apk_error_all_sources	Toutes les sources ont échoué.
prepare_apk_delete_confirm	Supprimer le fichier gardé ?
prepare_apk_delete_message	Cela libère environ %1$d Mo.
prepare_apk_required	Préparez d'abord l'application à partager.
prepare_apk_download_interrupted	Téléchargement interrompu
prepare_apk_download_cancelled	Téléchargement annulé
apk_download_notification_title	Téléchargement de l'application
apk_download_channel_name	Téléchargements
hotspot_share_via	Partager par point d'accès Wi-Fi
hotspot_share_via_subtitle	Créer un Wi-Fi pour partager sans internet
hotspot_share_other	Partager par Quick Share
hotspot_share_other_subtitle	Utiliser le partage Android habituel
hotspot_disconnect_title	Couper la connexion Wi-Fi Direct actuelle ?
hotspot_disconnect_message	Le point d'accès va couper la connexion Wi-Fi Direct actuelle. Cela peut interrompre Cast, Android Auto, Quick Share ou un autre appareil proche.
hotspot_disconnect_confirm	Couper et démarrer
install_bitchat_title	Installer l'application reçue
install_bitchat_subtitle	Installer Reo Fenua depuis les fichiers reçus
install_apk_dialog_title	Mettre à jour Reo Fenua
install_apk_dialog_message	Installer Reo Fenua depuis le fichier reçu ? Cela permet de partager l'application sans internet.
install_apk_permission_title	Autorisation nécessaire
install_apk_permission_message	Reo Fenua a besoin de l'autorisation d'installer des applications. Activez « Installer des applis inconnues » sur l'écran suivant.
install_apk_confirm	Installer
install_apk_grant_permission	Autoriser
install_apk_select_files	Choisir le fichier
install_apk_error	Échec de l'installation. Réessayez.
install_apk_no_files	Aucun fichier choisi.
cd_direct_wifi_aware	Wi-Fi direct
cd_direct_bluetooth	Bluetooth direct
cd_routed_mesh	Relayé par le réseau
notification_action_quit_bitchat	Quitter Reo Fenua
about_background_title	Fonctionner en arrière-plan
about_background_desc	Garde le réseau actif quand l'application est fermée
location_bluetooth_wifi_subtitle	Bluetooth • Wi-Fi • %1$s
action_private_message_title	Écrire à %1$s
action_private_message_subtitle	Envoyer un message privé
location_channels_heading	Discussions par lieu
location_channels_nearby	À proximité
mesh_section_subtitle	Réseau local. Pas besoin d'internet.
section_nearby	À proximité
location_tor_routing_title	Passer par Tor
location_tor_routing_desc	Cache votre adresse IP dans les discussions par lieu.
badge_recommended	Conseillé
people_count_title	Personnes (%1$d)
section_people	Personnes
section_on_location	Sur place
section_teleported_in	Venus de loin
mesh_title	Réseau local
debug_verbose_hint	Journalise les arrivées et départs, les connexions et les relais
debug_roles_hint	Activer ou couper les rôles et fermer les connexions
debug_rssi_fmt	Signal : %1$s
background_location_required_title	Localisation en arrière-plan conseillée
background_location_required_subtitle	Facultatif, rend le réseau plus fiable
background_location_explanation	Android demande la localisation en arrière-plan pour que Reo Fenua trouve les téléphones proches même application fermée. Le réseau reste actif après un redémarrage.
background_location_settings_tip	Dans les réglages, choisissez « Toujours autoriser ».
background_location_needs_for	Reo Fenua utilise la localisation en arrière-plan pour :
background_location_needs_bullets	- Trouver les téléphones proches application fermée\n- Se reconnecter après un redémarrage\n- Garder le réseau actif en arrière-plan
background_location_privacy_note	Votre position n'est JAMAIS collectée ni enregistrée.
grant_background_location	Autoriser en arrière-plan
skip_background_location	Continuer sans
perm_background_location_desc	Conseillé pour trouver les téléphones proches en arrière-plan
perm_background_location_system	Autoriser la localisation en arrière-plan
perm_type_background_location	Localisation en arrière-plan
tor_not_available_in_this_build	Tor n'est pas disponible dans cette version
checking	Vérification…
apk_not_ready_please_prepare_it_first	Application pas prête. Préparez-la d'abord.
'''
FR_FRIENDLY = r'''permissions_header	Quelques autorisations
privacy_first	Votre vie privée d'abord
privacy_protected	Votre vie privée est respectée
privacy_bullets	• Pas de compte, pas de numéro de téléphone\n• Personne ne suit où vous êtes\n• Les messages passent de téléphone en téléphone, sans internet
grant_permissions	C'est parti !
continue_btn	Continuer
skip	Plus tard
try_again	Réessayer
check_again	Vérifier encore
open_settings	Ouvrir les réglages
setup_not_complete	Presque prêt…
should_take_seconds	Juste quelques secondes…
initializing_mesh_network	Préparation de Reo Fenua
setting_up_bluetooth	On prépare la connexion avec les téléphones proches…
perm_type_nearby_devices	Téléphones à proximité
perm_nearby_devices_desc	Pour trouver les téléphones autour de vous et leur envoyer vos messages
perm_nearby_devices_system	Autoriser Reo Fenua à se connecter aux téléphones proches
perm_type_precise_location	Localisation
perm_location_desc	Android l'exige pour chercher les téléphones proches. Reo Fenua ne regarde jamais où vous êtes.
perm_location_system	Nécessaire pour trouver les téléphones proches
perm_type_notifications	Notifications
perm_notifications_desc	Pour être prévenu quand vous recevez un message
perm_notifications_system	Autoriser Reo Fenua à vous prévenir des nouveaux messages
perm_type_microphone	Micro
perm_type_battery_optimization	Batterie
perm_battery_desc	Pour que Reo Fenua continue de recevoir vos messages quand l'écran est éteint
perm_battery_system	Laisser Reo Fenua fonctionner en arrière-plan
perm_type_other	Autre
perm_type_background_location	Fonctionner écran éteint
perm_background_location_desc	Pour recevoir les messages même quand l'application est fermée (conseillé)
perm_background_location_system	Autoriser tout le temps
permission_bluetooth_rationale	Le Bluetooth sert à parler aux téléphones proches, sans internet.
permission_location_rationale	Android demande la localisation pour trouver les téléphones proches. Votre position n'est jamais utilisée.
permission_notification_rationale	Les notifications vous préviennent quand un message arrive.
bluetooth_recommended	Allumez le Bluetooth
bluetooth_needs_for	Le Bluetooth permet à Reo Fenua de :
bluetooth_needs_bullets	• Trouver les personnes autour de vous\n• Envoyer et recevoir des messages\n• Marcher sans internet ni réseau téléphone
enable_bluetooth	Allumer le Bluetooth
checking_bluetooth_status	On vérifie le Bluetooth…
bluetooth_not_supported	Bluetooth non compatible
bluetooth_unsupported_explanation	Désolé, ce téléphone n'a pas le Bluetooth nécessaire pour Reo Fenua.\n\nReo Fenua a besoin du Bluetooth pour parler aux téléphones proches sans internet.
location_services_required	Allumez la localisation
location_needs_for	Android demande la localisation pour :
location_needs_bullets	• Chercher les téléphones proches en Bluetooth\n• Vous montrer qui est autour de vous\n• Reo Fenua ne suit jamais où vous êtes
location_explanation	Reo Fenua ne regarde PAS où vous êtes.\n\nAndroid oblige simplement à allumer la localisation pour pouvoir chercher les téléphones proches.
open_location_settings	Allumer la localisation
checking_location_services	On vérifie la localisation…
location_services_unavailable	Localisation indisponible
location_unavailable_explanation	Ce téléphone n'a pas de localisation, ce qui est rare.\n\nAndroid en a besoin pour chercher les téléphones proches. Sans elle, Reo Fenua ne peut pas trouver les autres.
background_location_required_title	Recevoir les messages écran éteint
background_location_required_subtitle	Facultatif, mais conseillé
background_location_explanation	Pour que vos messages continuent d'arriver quand Reo Fenua est fermé, Android demande la localisation « tout le temps ».
background_location_settings_tip	Dans l'écran suivant, choisissez « Toujours autoriser ».
background_location_needs_for	Cela permet de :
background_location_needs_bullets	- Recevoir les messages application fermée\n- Se reconnecter tout seul après un redémarrage\n- Relayer les messages des voisins
background_location_privacy_note	Votre position n'est JAMAIS enregistrée ni envoyée.
grant_background_location	Oui, autoriser
skip_background_location	Non merci, continuer
battery_optimization_detected_title	Votre téléphone peut couper Reo Fenua
battery_optimization_enabled_title	Votre téléphone peut couper Reo Fenua
battery_optimization_explanation_short	Pour économiser la batterie, votre téléphone peut arrêter Reo Fenua quand l'écran est éteint. Vous risquez alors de manquer des messages.
benefits_of_disabling	En autorisant Reo Fenua :
battery_benefits_short	• Vos messages arrivent toujours\n• Vous aidez à relayer les messages des voisins\n• La connexion ne se coupe pas
disable_battery_optimization	Autoriser Reo Fenua
battery_optimization_skip	Plus tard
battery_optimization_disabled_title	C'est réglé !
battery_optimization_success_message	Reo Fenua peut fonctionner tranquillement en arrière-plan.
battery_optimization_not_required	Rien à régler
battery_optimization_not_supported_message	Votre téléphone n'a pas besoin de réglage. Reo Fenua marchera normalement.
cd_checking_battery_optimization	Vérification de la batterie
cd_battery_optimization	Batterie
cd_not_supported_battery_optimization	Aucun réglage nécessaire
cd_location_services	Localisation
cd_privacy	Vie privée
cd_privacy_protected	Vie privée respectée
cd_benefits	Avantages
location_channels_title	Choisir une discussion
mesh_label	Autour de moi
mesh_title	Autour de moi
mesh_section_subtitle	Les personnes près de vous. Marche sans internet.
location_bluetooth_subtitle	Bluetooth • %1$s
location_channels_heading	Discussions de mon quartier
location_channels_desc	Avec internet, parlez aux gens de votre rue, de votre quartier, de votre commune ou de votre île. Seule une zone approximative est partagée, jamais votre position exacte.
location_channels_nearby	Près de chez moi
enable_location_services	Allumer la localisation
disable_location_services	Couper l'accès à la localisation
location_permission_denied	La localisation est refusée. Ouvrez les réglages pour l'autoriser et voir les discussions de quartier.
geohash_placeholder	code d'un lieu
invalid_geohash	Ce code de lieu n'existe pas
teleport	Visiter
cd_teleported	Visité à distance
finding_nearby_channels	On cherche les discussions près de vous…
location_level_block	Ma rue
location_level_neighborhood	Mon quartier
location_level_city	Ma commune
location_level_province	Mon île
location_level_region	Mon archipel
cd_location_notes	Petits mots laissés ici
nearby_notes_reveal	Voir les petits mots laissés ici
nearby_notes_one	1 petit mot laissé ici — touchez pour le lire
nearby_notes_many	%d petits mots laissés ici — touchez pour les lire
location_notes_empty_title	Aucun petit mot pour le moment
loading_location_notes	Chargement…
location_notes_relays_unavailable	Pas d'internet : les petits mots sont en pause
about_network	Protection
location_tor_routing_title	Mode discret
location_tor_routing_desc	Cache votre connexion internet dans les discussions de quartier. Un peu plus lent.
bookmarked	Mes favoris
cd_add_bookmark	Ajouter aux favoris
cd_remove_bookmark	Retirer des favoris
cd_open_map	Ouvrir la carte
'''
CODE_FR = r'''Nearby Devices	Téléphones à proximité
Precise Location	Localisation
Background Location	Fonctionner écran éteint
Microphone	Micro
Wi‑Fi Aware	Wi-Fi entre téléphones
Battery Optimization	Batterie
Other	Autre
Required to discover bitchat users via Bluetooth	Pour trouver les téléphones autour de vous et leur envoyer vos messages
Allow bitchat to connect to nearby devices	Autoriser Reo Fenua à se connecter aux téléphones proches
Required by Android to discover nearby bitchat users via Bluetooth	Android l'exige pour chercher les téléphones proches. Reo Fenua ne regarde jamais où vous êtes.
bitchat needs this to scan for nearby devices	Nécessaire pour trouver les téléphones proches
Enable Wi‑Fi Aware to discover and connect to nearby bitchat users over Wi‑Fi.	Pour envoyer photos et fichiers plus vite et plus loin, par Wi-Fi entre téléphones (sans internet).
Allow bitchat to discover nearby Wi‑Fi devices	Autoriser Reo Fenua à trouver les téléphones proches par Wi-Fi
Receive notifications when you receive private messages	Pour être prévenu quand vous recevez un message
Allow bitchat to send you notifications	Autoriser Reo Fenua à vous prévenir des nouveaux messages
Disable battery optimization to ensure bitchat runs reliably in the background and maintains mesh network connections	Pour que Reo Fenua continue de recevoir vos messages quand l'écran est éteint
Allow bitchat to run without battery restrictions	Laisser Reo Fenua fonctionner en arrière-plan
Bluetooth/Nearby Devices	Bluetooth / téléphones à proximité
Location (for Bluetooth scanning)	Localisation (pour trouver les téléphones)
Nearby Wi‑Fi Devices (for Wi‑Fi Aware)	Wi-Fi entre téléphones
Some permissions were denied:\n	Certaines autorisations ont été refusées :\n
\nbitchat may not work properly without all permissions.	\nReo Fenua risque de mal fonctionner sans elles.
Critical permissions were denied. bitchat requires these permissions to function:\n	Il manque des autorisations indispensables pour Reo Fenua :\n
\nPlease grant these permissions in Settings to use bitchat.	\nOuvrez les réglages du téléphone pour les autoriser, puis revenez dans Reo Fenua.
Some permissions were revoked. Please grant all permissions to continue.	Des autorisations ont été retirées. Autorisez-les à nouveau pour continuer.
Failed to initialize the app: ${e.message}	Reo Fenua n'a pas pu démarrer : ${e.message}
Location services are required for Bluetooth scanning on Android. Please enable location services to continue.	Android a besoin de la localisation allumée pour trouver les téléphones proches. Allumez-la pour continuer.
Location services have been disabled.	La localisation a été éteinte.
Failed to open location settings: ${e.message}	Impossible d'ouvrir les réglages de localisation : ${e.message}
Location services are not available on this device.	Ce téléphone n'a pas de localisation.
Location services are enabled and ready	La localisation est allumée
Location services are disabled. Please enable location services for Bluetooth scanning.	La localisation est éteinte. Allumez-la pour trouver les téléphones proches.
Bluetooth is required for bitchat to discover and connect to nearby users. Please enable Bluetooth to continue.	Reo Fenua a besoin du Bluetooth pour parler aux téléphones proches. Allumez-le pour continuer.
Bluetooth permissions are required before enabling Bluetooth. Please grant permissions first.	Autorisez d'abord Reo Fenua à utiliser le Bluetooth.
Failed to request Bluetooth enable: ${e.message}	Impossible d'allumer le Bluetooth : ${e.message}
This device doesn't support Bluetooth, which is required for bitchat to function.	Ce téléphone n'a pas le Bluetooth nécessaire pour Reo Fenua.
Bluetooth is enabled and ready	Le Bluetooth est allumé
Bluetooth is disabled. Please enable Bluetooth to use bitchat.	Le Bluetooth est éteint. Allumez-le pour utiliser Reo Fenua.
This device doesn't support Bluetooth.	Ce téléphone n'a pas le Bluetooth.
Unable to open battery optimization settings: ${e.message}	Impossible d'ouvrir les réglages de batterie : ${e.message}
Unable to open settings: ${e.message}	Impossible d'ouvrir les réglages : ${e.message}
Unable to open app settings: ${e.message}	Impossible d'ouvrir les réglages de l'application : ${e.message}
cannot start chat with $peerNickname: user is blocked.	impossible de parler à $peerNickname : cette personne est bloquée.
cannot send message to $recipientNickname: user is blocked.	impossible d'écrire à $recipientNickname : cette personne est bloquée.
blocked user $peerNickname	personne bloquée : $peerNickname
unblocked user $peerNickname	personne débloquée : $peerNickname
'''
GUIDE_KT = r'''package com.bitchat.android.ui

import android.content.Context
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import androidx.compose.foundation.layout.BoxScope
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.zIndex
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.graphics.PathEffect
import androidx.compose.ui.graphics.StrokeCap
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.drawText
import androidx.compose.ui.text.rememberTextMeasurer
import android.graphics.BitmapFactory
import androidx.compose.foundation.Image
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.layout.ContentScale
import java.io.File
import android.net.Uri
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.interaction.collectIsPressedAsState
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Attachment
import androidx.compose.material3.Icon
import androidx.compose.ui.draw.rotate
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.statusBars
import androidx.compose.foundation.layout.asPaddingValues

/** Marge du haut des écrans Reo Fenua : suit la barre d'état du téléphone (encoche comprise). */
@Composable
fun reoHeaderTop(): Dp {
    val inset = WindowInsets.statusBars.asPaddingValues().calculateTopPadding()
    return (if (inset > 24.dp) inset else 24.dp) + 12.dp
}

/** Reo Fenua : introduction au premier lancement et rubrique d'aide. */
object ReoFenuaGuide {
    private const val PREFS = "reo_fenua_guide"
    private const val KEY_SEEN = "intro_seen_v1"

    val showIntro = mutableStateOf(false)

    fun introSeen(context: Context): Boolean =
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getBoolean(KEY_SEEN, false)

    fun markSeen(context: Context) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit().putBoolean(KEY_SEEN, true).apply()
    }
}

private val Lagon = Color(0xFF0E7C86)
private val Ocean = Color(0xFF0B3C5D)
private val LagonClair = Color(0xFF4FC3CC)
private val Ciel = Color(0xFFD7ECEE)
private val Sable = Color(0xFFF3E3C6)
private val Vanille = Color(0xFFE8B33A)

private class IntroPage(val title: String, val body: String)

private val introPages = listOf(
    IntroPage(
        "Ia ora na !",
        "Bienvenue sur Reo Fenua, la messagerie qui marche même sans internet et sans réseau téléphone."
    ),
    IntroPage(
        "Comment ça marche ?",
        "Votre téléphone parle directement aux téléphones proches, par Bluetooth et Wi-Fi.\n\n" +
            "Chaque téléphone fait passer le message au suivant, comme une chaîne, jusqu'à la bonne personne."
    ),
    IntroPage(
        "Plus on est nombreux, plus ça porte loin",
        "Il faut que d'autres personnes autour de vous aient Reo Fenua.\n\n" +
            "Partagez l'application avec votre famille, vos voisins et votre quartier."
    ),
    IntroPage(
        "En cas de coupure",
        "Pendant un cyclone ou une panne, Reo Fenua continue de marcher.\n\n" +
            "Gardez votre téléphone chargé. Dès que le réseau revient, appelez si besoin le 15 (SAMU), le 17 (police), le 18 (pompiers), le 16 (secours en mer) ou le 112."
    )
)

private class HelpItem(val question: String, val answer: String)

private val helpItems = listOf(
    HelpItem(
        "Pourquoi je vois 0 personne ?",
        "Personne autour de vous n'a Reo Fenua ouvert, ou le Bluetooth est éteint. Rapprochez-vous : la portée est d'environ 10 à 30 mètres entre deux téléphones, un peu plus en plein air. La carte « Étendre le réseau » (dans Alerte et dans Plus) aide aussi à trouver un Wi-Fi gratuit."
    ),
    HelpItem(
        "Faut-il internet ?",
        "Non. Les messages passent de téléphone en téléphone. Si internet est disponible, Reo Fenua l'utilise aussi pour aller plus loin."
    ),
    HelpItem(
        "Qui peut lire mes messages ?",
        "Les messages écrits dans « Autour de moi » sont lus par tous ceux qui sont autour. Pour un message privé et chiffré, touchez « Proches » en bas, puis « Écrire à… ». Le texte gris de la case d'écriture dit toujours qui pourra lire."
    ),
    HelpItem(
        "Comment changer mon nom ?",
        "Touchez votre nom en haut de l'écran (par exemple @anon1234) et tapez le nom que vous voulez."
    ),
    HelpItem(
        "Comment envoyer une photo, un fichier ou un vocal ?",
        "Photo : touchez l'appareil photo (appui long pour en prendre une). Document ou vidéo : touchez le trombone (10 Mo maximum). Message vocal : gardez le doigt appuyé sur le micro pendant que vous parlez, puis relâchez."
    ),
    HelpItem(
        "Comment partager l'application ?",
        "Touchez « Plus » en bas, puis « Partager Reo Fenua ». Vous pouvez aussi envoyer le fichier d'installation par WhatsApp ou Bluetooth."
    ),
    HelpItem(
        "Est-ce que ça use la batterie ?",
        "Un peu plus que d'habitude, car le Bluetooth cherche les téléphones proches. En cas de coupure, gardez une batterie externe chargée."
    ),
    HelpItem(
        "Comment bloquer quelqu'un ?",
        "Touchez « Proches » en bas, puis « Noms, photos et blocage ». Sous la personne, touchez « Bloquer cette personne » et confirmez. Vous ne recevrez plus ses messages ni ses lettres. Vous pouvez la débloquer au même endroit."
    ),
    HelpItem(
        "Comment tout effacer en urgence ?",
        "Touchez « Plus » en bas, puis « Tout effacer » tout en bas, et confirmez. En urgence : touchez 3 fois rapidement le logo en haut à gauche, puis « Effacer ». Tous vos messages et votre identité sont alors effacés de ce téléphone. Impossible d'annuler."
    )
)

/** Affiche l'introduction au premier lancement, ou quand on la redemande depuis l'aide. */
@Composable
fun ReoFenuaIntroGate() {
    val context = LocalContext.current
    LaunchedEffect(Unit) {
        if (!ReoFenuaGuide.introSeen(context)) ReoFenuaGuide.showIntro.value = true
    }
    if (ReoFenuaGuide.showIntro.value) {
        ReoFenuaIntroDialog(onDone = {
            ReoFenuaGuide.markSeen(context)
            ReoFenuaGuide.showIntro.value = false
        })
    }
}

/** Dessin du lagon : ciel, soleil, montagnes, lagon et plage. */
@Composable
private fun LagonIllustration(modifier: Modifier = Modifier) {
    Canvas(modifier = modifier) {
        val w = size.width
        val h = size.height
        drawRect(color = Ciel, size = Size(w, h * 0.62f))
        drawCircle(color = Vanille, radius = h * 0.09f, center = Offset(w * 0.76f, h * 0.2f))

        val montagnes = Path().apply {
            moveTo(0f, h * 0.62f)
            lineTo(w * 0.14f, h * 0.45f)
            lineTo(w * 0.24f, h * 0.51f)
            lineTo(w * 0.38f, h * 0.39f)
            lineTo(w * 0.52f, h * 0.49f)
            lineTo(w * 0.62f, h * 0.43f)
            lineTo(w * 0.8f, h * 0.62f)
            close()
        }
        drawPath(path = montagnes, color = Ocean)

        drawRect(color = Lagon, topLeft = Offset(0f, h * 0.6f), size = Size(w, h * 0.3f))

        for (row in 0 until 3) {
            val y = h * (0.66f + row * 0.08f)
            val vague = Path().apply {
                moveTo(0f, y)
                var x = 0f
                val step = w / 8f
                while (x < w) {
                    quadraticTo(x + step / 4f, y - h * 0.025f, x + step / 2f, y)
                    quadraticTo(x + step * 3f / 4f, y + h * 0.025f, x + step, y)
                    x += step
                }
                lineTo(w, y + h * 0.012f)
                lineTo(0f, y + h * 0.012f)
                close()
            }
            drawPath(path = vague, color = LagonClair)
        }

        drawRect(color = Sable, topLeft = Offset(0f, h * 0.88f), size = Size(w, h * 0.12f))
    }
}

@Composable
fun ReoFenuaIntroDialog(onDone: () -> Unit) {
    var page by remember { mutableStateOf(0) }
    val last = introPages.size - 1
    val current = introPages[page]

    Dialog(
        onDismissRequest = onDone,
        properties = DialogProperties(usePlatformDefaultWidth = false)
    ) {
        Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
            Column(modifier = Modifier.fillMaxSize()) {
                Box(modifier = Modifier.fillMaxWidth()) {
                    val illustrationModifier = Modifier
                        .fillMaxWidth()
                        .height(if (page == 0) 300.dp else 230.dp)
                    when (page) {
                        1 -> ChainSchema(illustrationModifier)
                        2 -> NetworkSchema(illustrationModifier)
                        3 -> OutageSchema(illustrationModifier)
                        else -> LagonIllustration(illustrationModifier)
                    }
                    TextButton(
                        onClick = onDone,
                        modifier = Modifier
                            .align(Alignment.TopEnd)
                            .padding(8.dp)
                    ) {
                        Text(text = "Passer", fontSize = 17.sp, color = Ocean)
                    }
                    if (page == 0) {
                        Text(
                            text = "Reo Fenua",
                            fontSize = 40.sp,
                            fontWeight = FontWeight.Bold,
                            color = Ocean,
                            modifier = Modifier
                                .align(Alignment.TopStart)
                                .padding(start = 24.dp, top = 44.dp)
                        )
                    }
                }
                NihoManoBand(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(14.dp)
                )

                Column(
                    modifier = Modifier
                        .weight(1f)
                        .fillMaxWidth()
                        .verticalScroll(rememberScrollState())
                        .padding(horizontal = 24.dp, vertical = 24.dp),
                    verticalArrangement = Arrangement.spacedBy(16.dp)
                ) {
                    Text(
                        text = current.title,
                        fontSize = 28.sp,
                        fontWeight = FontWeight.Bold,
                        color = MaterialTheme.colorScheme.primary
                    )
                    Text(
                        text = current.body,
                        fontSize = 19.sp,
                        lineHeight = 28.sp,
                        color = MaterialTheme.colorScheme.onBackground
                    )
                }

                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(bottom = 12.dp),
                    horizontalArrangement = Arrangement.Center
                ) {
                    for (i in introPages.indices) {
                        Box(
                            modifier = Modifier
                                .padding(horizontal = 5.dp)
                                .size(if (i == page) 12.dp else 9.dp)
                                .background(
                                    color = if (i == page) Lagon else MaterialTheme.colorScheme.outline,
                                    shape = CircleShape
                                )
                        )
                    }
                }

                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(start = 24.dp, end = 24.dp, bottom = 32.dp),
                    horizontalArrangement = Arrangement.spacedBy(12.dp)
                ) {
                    if (page > 0) {
                        OutlinedButton(
                            onClick = { page -= 1 },
                            modifier = Modifier
                                .weight(1f)
                                .heightIn(min = 56.dp)
                        ) {
                            Text(text = "Retour", fontSize = 18.sp)
                        }
                    }
                    Button(
                        onClick = { if (page < last) page += 1 else onDone() },
                        modifier = Modifier
                            .weight(1f)
                            .heightIn(min = 56.dp)
                    ) {
                        Text(text = if (page < last) "Suivant" else "Commencer", fontSize = 18.sp)
                    }
                }
            }
        }
    }
}

/** Rubrique d'aide : questions fréquentes, à toucher pour voir la réponse. */
@Composable
fun ReoFenuaHelpCard() {
    var openIndex by remember { mutableStateOf(-1) }

    Surface(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp, vertical = 12.dp),
        color = MaterialTheme.colorScheme.surface,
        shape = MaterialTheme.shapes.large
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text(
                text = "Aide",
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold,
                color = MaterialTheme.colorScheme.primary
            )
            Spacer(modifier = Modifier.height(8.dp))
            helpItems.forEachIndexed { index, item ->
                val open = openIndex == index
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .heightIn(min = 48.dp)
                        .clickable { openIndex = if (open) -1 else index }
                        .padding(vertical = 12.dp)
                ) {
                    Text(
                        text = (if (open) "▾  " else "▸  ") + item.question,
                        fontSize = 17.sp,
                        fontWeight = FontWeight.SemiBold,
                        color = MaterialTheme.colorScheme.onSurface
                    )
                    if (open) {
                        Text(
                            text = item.answer,
                            fontSize = 16.sp,
                            lineHeight = 24.sp,
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                            modifier = Modifier.padding(top = 8.dp, start = 22.dp)
                        )
                    }
                }
                if (index < helpItems.size - 1) {
                    HorizontalDivider(color = MaterialTheme.colorScheme.outlineVariant)
                }
            }
            Spacer(modifier = Modifier.height(12.dp))
            Button(
                onClick = { ReoFenuaSteps.show.value = true },
                modifier = Modifier
                    .fillMaxWidth()
                    .heightIn(min = 52.dp)
            ) {
                Text(text = "Mode d'emploi pas à pas", fontSize = 17.sp, textAlign = TextAlign.Center)
            }
            Spacer(modifier = Modifier.height(8.dp))
            OutlinedButton(
                onClick = { ReoFenuaGuide.showIntro.value = true },
                modifier = Modifier
                    .fillMaxWidth()
                    .heightIn(min = 52.dp)
            ) {
                Text(text = "Revoir l'introduction", fontSize = 17.sp, textAlign = TextAlign.Center)
            }
        }
    }
}


// ===================== Mode d'emploi pas à pas =====================

private class Step(val title: String, val body: String)

private val guideSteps = listOf(
    Step("Choisir votre nom",
        "En haut à gauche, touchez votre nom (par exemple @anon1234).\n\nTapez le nom que vous voulez, puis validez. C'est ce nom que les autres verront."),
    Step("Voir qui est autour",
        "En haut à droite, le chiffre à côté des deux personnes montre combien de téléphones avec Reo Fenua sont près de vous.\n\nTouchez-le pour voir la liste."),
    Step("Écrire à tout le monde",
        "En bas, touchez « écrire un message… », tapez votre texte, puis touchez la flèche pour envoyer.\n\nTout le monde autour de vous le reçoit."),
    Step("Écrire à une seule personne",
        "En bas, touchez « Proches », puis « Écrire à… » sous la personne. Si elle n'est pas autour, une lettre l'attend.\n\nVotre message privé est chiffré : seule cette personne peut le lire."),
    Step("Envoyer une photo",
        "Touchez le bouton de l'appareil photo pour choisir une photo dans votre galerie.\n\nPour prendre une photo tout de suite, gardez le doigt appuyé sur ce bouton."),
    Step("Envoyer un document ou une vidéo",
        "Touchez le trombone, à gauche de l'appareil photo, puis choisissez votre fichier : PDF, Word, vidéo…\n\nTaille maximum : environ 10 Mo. Les petits fichiers arrivent plus vite et plus loin."),
    Step("Envoyer un message vocal",
        "Gardez le doigt appuyé sur le bouton jaune du micro, parlez, puis relâchez. Le message part tout seul."),
    Step("Changer de discussion",
        "En bas, touchez « Radar » pour choisir jusqu'où parler.\n\n« Autour de moi » = les personnes près de vous, sans internet. Avec internet, vous pouvez aussi parler à votre quartier, votre commune ou votre île."),
    Step("En cas d'urgence : Alerte",
        "Touchez le gros bouton rouge « ALERTE », au milieu en bas.\n\nChoisissez « Je vais bien », « J'ai besoin d'aide », « Besoin d'eau »… Vous avez 3 secondes pour toucher « Annuler », puis le message part avec votre nom et votre lieu, sans rien écrire."),
    Step("Écrire une lettre",
        "En bas, touchez « Proches », puis « Boîte aux lettres ».\n\nUne lettre peut aller à quelqu'un qui n'est pas là : elle attend jusqu'à 24 h et part dès que la personne est joignable."),
    Step("Partager l'application",
        "En bas, touchez « Plus », puis « Partager Reo Fenua ».\n\nPlus il y a de téléphones, plus les messages vont loin."),
    Step("Besoin d'aide ?",
        "En bas, touchez « Plus » pour la taille du texte, le son, le fond d'écran, la carte du réseau, le mode relais et le partage.\n\nLe bouton « Aide », en bas, vous ramène toujours à ce mode d'emploi.")
)

object ReoFenuaSteps {
    val show = mutableStateOf(false)
}

@Composable
fun ReoFenuaStepsDialog(onDone: () -> Unit) {
    var index by remember { mutableStateOf(0) }
    val steps = guideSteps
    val last = steps.size - 1
    val step = steps[index.coerceIn(0, last)]

    Dialog(
        onDismissRequest = onDone,
        properties = DialogProperties(usePlatformDefaultWidth = false)
    ) {
        Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
            Column(modifier = Modifier.fillMaxSize()) {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(Lagon)
                        .padding(start = 24.dp, end = 8.dp, top = reoHeaderTop(), bottom = 16.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Text(
                        text = "Mode d'emploi",
                        fontSize = 24.sp,
                        fontWeight = FontWeight.Bold,
                        color = Color.White,
                        modifier = Modifier.weight(1f)
                    )
                    TextButton(onClick = onDone) {
                        Text(text = "← Retour", fontSize = 17.sp, color = Color.White)
                    }
                }

                NihoManoBand(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(14.dp),
                    color = Ocean,
                    accent = Vanille
                )
                Column(
                    modifier = Modifier
                        .weight(1f)
                        .fillMaxWidth()
                        .verticalScroll(rememberScrollState())
                        .padding(24.dp),
                    verticalArrangement = Arrangement.spacedBy(18.dp)
                ) {
                    Box(
                        modifier = Modifier
                            .size(72.dp)
                            .background(Vanille, CircleShape),
                        contentAlignment = Alignment.Center
                    ) {
                        Text(
                            text = (index + 1).toString(),
                            fontSize = 34.sp,
                            fontWeight = FontWeight.Bold,
                            color = Ocean
                        )
                    }
                    Text(
                        text = "Étape " + (index + 1) + " sur " + steps.size,
                        fontSize = 16.sp,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                    Text(
                        text = step.title,
                        fontSize = 28.sp,
                        fontWeight = FontWeight.Bold,
                        color = MaterialTheme.colorScheme.primary
                    )
                    Text(
                        text = step.body,
                        fontSize = 19.sp,
                        lineHeight = 28.sp,
                        color = MaterialTheme.colorScheme.onBackground
                    )
                }

                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(bottom = 12.dp),
                    horizontalArrangement = Arrangement.Center
                ) {
                    for (i in steps.indices) {
                        Box(
                            modifier = Modifier
                                .padding(horizontal = 4.dp)
                                .size(if (i == index) 11.dp else 8.dp)
                                .background(
                                    color = if (i == index) Lagon else MaterialTheme.colorScheme.outline,
                                    shape = CircleShape
                                )
                        )
                    }
                }

                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(start = 24.dp, end = 24.dp, bottom = 32.dp),
                    horizontalArrangement = Arrangement.spacedBy(12.dp)
                ) {
                    if (index > 0) {
                        OutlinedButton(
                            onClick = { index -= 1 },
                            modifier = Modifier
                                .weight(1f)
                                .heightIn(min = 56.dp)
                        ) {
                            Text(text = "Retour", fontSize = 18.sp)
                        }
                    }
                    Button(
                        onClick = { if (index < last) index += 1 else onDone() },
                        modifier = Modifier
                            .weight(1f)
                            .heightIn(min = 56.dp)
                    ) {
                        Text(text = if (index < last) "Suivant" else "J'ai compris", fontSize = 18.sp)
                    }
                }
            }
        }
    }
}

object ReoFenuaUpdateDialog {
    val show = mutableStateOf(false)
}

/** Un bouton rond avec un mot dessous : icône + mot, toujours. */
@Composable
private fun RoundAction(
    label: String,
    background: Color,
    onClick: () -> Unit,
    badge: Int = 0,
    content: @Composable () -> Unit
) {
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Box(
            modifier = Modifier
                .size(50.dp)
                .background(background, CircleShape)
                .clickable { onClick() }
                .semantics { contentDescription = label },
            contentAlignment = Alignment.Center
        ) {
            content()
            if (badge > 0) {
                Box(
                    modifier = Modifier
                        .align(Alignment.TopEnd)
                        .size(20.dp)
                        .background(Color(0xFFC8102E), CircleShape),
                    contentAlignment = Alignment.Center
                ) {
                    Text(text = if (badge > 9) "9+" else badge.toString(), fontSize = 11.sp, fontWeight = FontWeight.Bold, color = Color.White)
                }
            }
        }
        Box(
            modifier = Modifier
                .padding(top = 3.dp)
                .background(SableClair, MaterialTheme.shapes.small)
                .padding(horizontal = 6.dp, vertical = 2.dp)
        ) {
            Text(text = label, fontSize = 13.sp, fontWeight = FontWeight.SemiBold, color = Ocean)
        }
    }
}


/** Boutons ronds sur l'écran principal : Alerte, Lettres, Aide, Mise à jour. */
@Composable
fun BoxScope.ReoFenuaHelpButton(viewModel: ChatViewModel, topPadding: Dp) {
    ReoFenuaMode.load(LocalContext.current)
    LaunchedEffect(Unit) { ReoFenuaUpdate.checkInBackground() }
    val newVersion = ReoFenuaUpdate.available.value
    // Bandeau « position partagée » en haut, au centre
    ReoFenuaLocationBanner(
        viewModel = viewModel,
        modifier = Modifier
            .align(Alignment.TopCenter)
            .zIndex(10f)
            .padding(top = topPadding)
    )
    // Pastille « Mode » bien visible, en haut à droite
    ReoFenuaModePill(
        modifier = Modifier
            .align(Alignment.TopEnd)
            .zIndex(10f)
            .padding(top = topPadding + 6.dp, end = 10.dp)
    )
    // Bandeau « Nouvelle version » bien visible en haut, seulement quand une mise à jour existe
    if (newVersion != null && !ReoFenuaUpdate.bannerHidden.value) {
        Surface(
            color = Lagon,
            shape = RoundedCornerShape(20.dp),
            shadowElevation = 6.dp,
            modifier = Modifier
                .align(Alignment.TopCenter)
                .zIndex(11f)
                .padding(top = topPadding + 60.dp, start = 12.dp, end = 12.dp)
                .fillMaxWidth()
        ) {
            Row(
                modifier = Modifier.padding(start = 14.dp, end = 6.dp, top = 8.dp, bottom = 8.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                Column(modifier = Modifier.weight(1f)) {
                    Text(text = "Nouvelle version disponible", fontSize = 16.sp, fontWeight = FontWeight.Bold, color = Color.White)
                    Text(text = "Améliorations et corrections", fontSize = 13.sp, color = Color.White.copy(alpha = 0.85f))
                }
                Button(
                    onClick = { ReoFenuaUpdateDialog.show.value = true },
                    colors = ButtonDefaults.buttonColors(containerColor = Color.White, contentColor = Lagon),
                    modifier = Modifier.heightIn(min = 44.dp)
                ) { Text(text = "Mettre à jour", fontSize = 15.sp, fontWeight = FontWeight.Bold) }
                TextButton(onClick = { ReoFenuaUpdate.bannerHidden.value = true }) {
                    Text(text = "Plus tard", fontSize = 13.sp, color = Color.White)
                }
            }
        }
    }
    if (ReoFenuaSteps.show.value) {
        ReoFenuaStepsDialog(onDone = { ReoFenuaSteps.show.value = false })
    }
    if (ReoFenuaUpdateDialog.show.value) {
        Dialog(onDismissRequest = { ReoFenuaUpdateDialog.show.value = false }) {
            Surface(
                color = MaterialTheme.colorScheme.background,
                shape = MaterialTheme.shapes.extraLarge
            ) {
                Column(modifier = Modifier.padding(vertical = 8.dp)) {
                    ReoFenuaUpdateCard()
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(end = 16.dp),
                        horizontalArrangement = Arrangement.End
                    ) {
                        TextButton(onClick = { ReoFenuaUpdateDialog.show.value = false }) {
                            Text(text = "Fermer", fontSize = 17.sp)
                        }
                    }
                }
            }
        }
    }
}

// ===================== Fond d'écran =====================

object ReoFenuaWallpaper {
    private const val PREFS = "reo_fenua_guide"
    private const val KEY = "wallpaper"
    val names = listOf("Aucun", "Lagon", "Vagues", "Tiare", "Ma photo")
    val choice = mutableStateOf(-1)
    val photoVersion = mutableStateOf(0)

    fun photoFile(context: Context): File = File(context.filesDir, "reo_wallpaper.jpg")

    fun load(context: Context) {
        if (choice.value < 0) {
            choice.value = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getInt(KEY, 1)
        }
    }

    fun save(context: Context, value: Int) {
        choice.value = value
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putInt(KEY, value).apply()
    }
}

/** Fond d'écran dessiné derrière les messages, très léger pour garder le texte lisible. */
@Composable
fun BoxScope.ReoFenuaWallpaperLayer() {
    val context = LocalContext.current
    LaunchedEffect(Unit) { ReoFenuaWallpaper.load(context) }
    val choice = ReoFenuaWallpaper.choice.value
    if (choice <= 0) return

    if (choice == 4) {
        val version = ReoFenuaWallpaper.photoVersion.value
        val photo = remember(version) {
            val f = ReoFenuaWallpaper.photoFile(context)
            if (f.exists()) BitmapFactory.decodeFile(f.absolutePath)?.asImageBitmap() else null
        }
        if (photo != null) {
            Image(
                bitmap = photo,
                contentDescription = null,
                contentScale = ContentScale.Crop,
                modifier = Modifier.matchParentSize()
            )
            // Voile clair par-dessus la photo pour que les messages restent lisibles
            Box(
                modifier = Modifier
                    .matchParentSize()
                    .background(MaterialTheme.colorScheme.background.copy(alpha = 0.62f))
            )
        }
        return
    }

    Canvas(modifier = Modifier.matchParentSize()) {
        val w = size.width
        val h = size.height
        when (choice) {
            1 -> {
                drawCircle(color = Vanille.copy(alpha = 0.25f), radius = w * 0.12f, center = Offset(w * 0.8f, h * 0.55f))
                val top = h * 0.62f
                val montagnes = Path().apply {
                    moveTo(0f, h * 0.78f)
                    lineTo(w * 0.15f, top + h * 0.06f)
                    lineTo(w * 0.27f, top + h * 0.1f)
                    lineTo(w * 0.42f, top)
                    lineTo(w * 0.58f, top + h * 0.09f)
                    lineTo(w * 0.7f, top + h * 0.05f)
                    lineTo(w * 0.92f, h * 0.78f)
                    close()
                }
                drawPath(path = montagnes, color = Ocean.copy(alpha = 0.14f))
                drawRect(color = Lagon.copy(alpha = 0.16f), topLeft = Offset(0f, h * 0.77f), size = Size(w, h * 0.23f))
                for (row in 0 until 4) {
                    val y = h * (0.8f + row * 0.05f)
                    val vague = Path().apply {
                        moveTo(0f, y)
                        var x = 0f
                        val step = w / 6f
                        while (x < w) {
                            quadraticTo(x + step / 4f, y - h * 0.012f, x + step / 2f, y)
                            quadraticTo(x + step * 3f / 4f, y + h * 0.012f, x + step, y)
                            x += step
                        }
                        lineTo(w, y + h * 0.006f)
                        lineTo(0f, y + h * 0.006f)
                        close()
                    }
                    drawPath(path = vague, color = LagonClair.copy(alpha = 0.22f))
                }
            }
            2 -> {
                var y = h * 0.08f
                while (y < h) {
                    val vague = Path().apply {
                        moveTo(0f, y)
                        var x = 0f
                        val step = w / 5f
                        while (x < w) {
                            quadraticTo(x + step / 4f, y - h * 0.015f, x + step / 2f, y)
                            quadraticTo(x + step * 3f / 4f, y + h * 0.015f, x + step, y)
                            x += step
                        }
                        lineTo(w, y + h * 0.005f)
                        lineTo(0f, y + h * 0.005f)
                        close()
                    }
                    drawPath(path = vague, color = Lagon.copy(alpha = 0.10f))
                    y += h * 0.09f
                }
            }
            else -> {
                val cell = w / 4f
                var row = 0
                var y = cell * 0.6f
                while (y < h) {
                    var x = if (row % 2 == 0) cell * 0.5f else cell
                    while (x < w + cell) {
                        val r = cell * 0.13f
                        for (p in 0 until 5) {
                            val a = Math.toRadians(p * 72.0 - 90.0)
                            drawCircle(
                                color = Lagon.copy(alpha = 0.10f),
                                radius = r,
                                center = Offset(x + (r * 1.1f * Math.cos(a)).toFloat(), y + (r * 1.1f * Math.sin(a)).toFloat())
                            )
                        }
                        drawCircle(color = Vanille.copy(alpha = 0.35f), radius = r * 0.55f, center = Offset(x, y))
                        x += cell
                    }
                    y += cell * 0.9f
                    row += 1
                }
            }
        }
    }
}

/** Carte de choix du fond d'écran, dans l'écran d'information. */
@Composable
fun ReoFenuaWallpaperCard() {
    val context = LocalContext.current
    LaunchedEffect(Unit) { ReoFenuaWallpaper.load(context) }
    val current = ReoFenuaWallpaper.choice.value

    val photoPicker = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.GetContent()
    ) { uri: Uri? ->
        if (uri != null) {
            val tmp = com.bitchat.android.features.media.ImageUtils.downscaleAndSaveToAppFiles(
                context, uri, maxDim = 1600, quality = 85
            )
            if (tmp != null) {
                try {
                    val src = File(tmp)
                    src.copyTo(ReoFenuaWallpaper.photoFile(context), overwrite = true)
                    src.delete()
                    ReoFenuaWallpaper.photoVersion.value += 1
                    ReoFenuaWallpaper.save(context, 4)
                } catch (e: Exception) {
                    // photo non enregistrée : on garde le fond actuel
                }
            }
        }
    }

    Surface(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp, vertical = 12.dp),
        color = MaterialTheme.colorScheme.surface,
        shape = MaterialTheme.shapes.large
    ) {
        Column(
            modifier = Modifier.padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(10.dp)
        ) {
            Text(
                text = "Fond d'écran",
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold,
                color = MaterialTheme.colorScheme.primary
            )
            for (rowStart in listOf(0, 2)) {
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    for (i in rowStart until rowStart + 2) {
                        val name = ReoFenuaWallpaper.names[i]
                        if (i == current) {
                            Button(
                                onClick = { ReoFenuaWallpaper.save(context, i) },
                                modifier = Modifier
                                    .weight(1f)
                                    .heightIn(min = 52.dp)
                            ) {
                                Text(text = "✓ " + name, fontSize = 17.sp)
                            }
                        } else {
                            OutlinedButton(
                                onClick = { ReoFenuaWallpaper.save(context, i) },
                                modifier = Modifier
                                    .weight(1f)
                                    .heightIn(min = 52.dp)
                            ) {
                                Text(text = name, fontSize = 17.sp)
                            }
                        }
                    }
                }
            }
            if (current == 4) {
                Button(
                    onClick = { photoPicker.launch("image/*") },
                    modifier = Modifier
                        .fillMaxWidth()
                        .heightIn(min = 52.dp)
                ) {
                    Text(text = "✓ Ma photo — changer de photo", fontSize = 17.sp)
                }
            } else {
                OutlinedButton(
                    onClick = { photoPicker.launch("image/*") },
                    modifier = Modifier
                        .fillMaxWidth()
                        .heightIn(min = 52.dp)
                ) {
                    Text(text = "Choisir ma photo dans la galerie", fontSize = 17.sp)
                }
            }
        }
    }
}


// ===================== Bouton « envoyer un fichier » =====================

/** Trombone à côté de l'appareil photo : documents, PDF, vidéos… (jusqu'à environ 10 Mo). */
@Composable
fun ReoFenuaFileButton(onFileReady: (String) -> Unit) {
    val context = LocalContext.current
    val picker = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.OpenDocument()
    ) { uri: Uri? ->
        if (uri != null) {
            val path = com.bitchat.android.features.file.FileUtils.copyFileForSending(context, uri)
            if (!path.isNullOrBlank()) onFileReady(path)
        }
    }
    val interactionSource = remember { MutableInteractionSource() }
    val isPressed by interactionSource.collectIsPressedAsState()

    ComposerActionSurface(
        isActive = false,
        isPressed = isPressed,
        contentDescription = "Envoyer un fichier",
        modifier = Modifier.clickable(
            interactionSource = interactionSource,
            indication = null
        ) { picker.launch(arrayOf("*/*")) }
    ) { tint ->
        Icon(
            imageVector = Icons.Filled.Attachment,
            contentDescription = null,
            tint = tint,
            modifier = Modifier
                .size(ComposerIconSize)
                .rotate(90f)
        )
    }
}


// ===================== Motif tahitien et explication des discussions =====================

/** Bande de motif niho mano (dents de requin), motif traditionnel polynésien. */
@Composable
fun NihoManoBand(modifier: Modifier = Modifier, color: Color = Ocean, accent: Color = Lagon) {
    Canvas(modifier = modifier) {
        val h = size.height
        val w = size.width
        val tooth = h * 1.2f
        var x = 0f
        var i = 0
        while (x < w) {
            val dent = Path().apply {
                moveTo(x, h)
                lineTo(x + tooth / 2f, 0f)
                lineTo(x + tooth, h)
                close()
            }
            drawPath(path = dent, color = if (i % 2 == 0) color else accent)
            x += tooth
            i += 1
        }
    }
}

private class ChannelStep(val number: String, val title: String, val body: String)

private val channelSteps = listOf(
    ChannelStep("1", "Autour de moi",
        "Pour parler aux personnes près de vous, sans internet. C'est le choix habituel."),
    ChannelStep("2", "Discussions de mon quartier",
        "Si vous avez internet : touchez « Ma rue », « Mon quartier », « Ma commune » ou « Mon île » pour parler aux gens de cette zone."),
    ChannelStep("3", "Visiter un autre lieu",
        "Tapez le code d'un lieu puis touchez « Visiter » pour voir sa discussion, même de loin.")
)

/** Carte d'explication pas à pas, en haut du menu « Choisir une discussion ». */
@Composable
fun ReoFenuaChannelsExplainer() {
    val context = LocalContext.current
    val prefs = remember { context.getSharedPreferences("reo_fenua_guide", Context.MODE_PRIVATE) }
    var open by remember { mutableStateOf(!prefs.getBoolean("channels_help_hidden", false)) }

    Surface(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp, vertical = 8.dp),
        color = MaterialTheme.colorScheme.surface,
        shape = MaterialTheme.shapes.extraLarge
    ) {
        Column {
            NihoManoBand(
                modifier = Modifier
                    .fillMaxWidth()
                    .height(14.dp)
            )
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .clickable { open = !open }
                    .padding(16.dp)
            ) {
                Text(
                    text = (if (open) "▾  " else "▸  ") + "Comment choisir ?",
                    fontSize = 19.sp,
                    fontWeight = FontWeight.Bold,
                    color = MaterialTheme.colorScheme.primary
                )
                if (!open) {
                    Text(
                        text = "Touchez ici pour voir l'explication",
                        fontSize = 15.sp,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                        modifier = Modifier.padding(start = 22.dp, top = 2.dp)
                    )
                }
            }
            if (open) {
                Column(
                    modifier = Modifier.padding(start = 16.dp, end = 16.dp, bottom = 16.dp),
                    verticalArrangement = Arrangement.spacedBy(14.dp)
                ) {
                    for (step in channelSteps) {
                        Row(verticalAlignment = Alignment.Top) {
                            Box(
                                modifier = Modifier
                                    .size(40.dp)
                                    .background(Vanille, CircleShape),
                                contentAlignment = Alignment.Center
                            ) {
                                Text(text = step.number, fontSize = 20.sp, fontWeight = FontWeight.Bold, color = Ocean)
                            }
                            Column(modifier = Modifier.padding(start = 14.dp)) {
                                Text(
                                    text = step.title,
                                    fontSize = 17.sp,
                                    fontWeight = FontWeight.SemiBold,
                                    color = MaterialTheme.colorScheme.onSurface
                                )
                                Text(
                                    text = step.body,
                                    fontSize = 16.sp,
                                    lineHeight = 23.sp,
                                    color = MaterialTheme.colorScheme.onSurfaceVariant
                                )
                            }
                        }
                    }
                    Button(
                        onClick = {
                            open = false
                            prefs.edit().putBoolean("channels_help_hidden", true).apply()
                        },
                        modifier = Modifier
                            .fillMaxWidth()
                            .heightIn(min = 52.dp)
                    ) {
                        Text(text = "J'ai compris", fontSize = 17.sp)
                    }
                }
            }
        }
    }
}


// ===================== Schémas de l'introduction =====================

private val SableClair = Color(0xFFF7EFE2)
private val CielGris = Color(0xFF9FB8C2)
private val Rouge = Color(0xFFC8102E)
private val Vert = Color(0xFF2E7D32)

private fun dashed(h: Float) = Stroke(
    width = h * 0.018f,
    cap = StrokeCap.Round,
    pathEffect = PathEffect.dashPathEffect(floatArrayOf(h * 0.04f, h * 0.045f), 0f)
)

private fun DrawScope.phone(c: Offset, h: Float) {
    val w = h * 0.56f
    drawRoundRect(
        color = Ocean,
        topLeft = Offset(c.x - w / 2f, c.y - h / 2f),
        size = Size(w, h),
        cornerRadius = CornerRadius(w * 0.2f)
    )
    drawRoundRect(
        color = SableClair,
        topLeft = Offset(c.x - w / 2f + w * 0.12f, c.y - h / 2f + h * 0.1f),
        size = Size(w * 0.76f, h * 0.74f),
        cornerRadius = CornerRadius(w * 0.08f)
    )
}

private fun DrawScope.bubble(c: Offset, s: Float) {
    drawRoundRect(
        color = Vanille,
        topLeft = Offset(c.x - s, c.y - s * 0.65f),
        size = Size(s * 2f, s * 1.25f),
        cornerRadius = CornerRadius(s * 0.35f)
    )
    val tail = Path().apply {
        moveTo(c.x - s * 0.4f, c.y + s * 0.55f)
        lineTo(c.x - s * 0.7f, c.y + s * 1.05f)
        lineTo(c.x + s * 0.1f, c.y + s * 0.55f)
        close()
    }
    drawPath(path = tail, color = Vanille)
}

/** Page 2 : le message saute de téléphone en téléphone. */
@Composable
private fun ChainSchema(modifier: Modifier) {
    Box(modifier = modifier.background(Ciel)) {
        Canvas(modifier = Modifier.matchParentSize()) {
            val w = size.width
            val h = size.height
            val y = h * 0.5f
            val ph = h * 0.38f
            val xs = listOf(w / 6f, w / 2f, w * 5f / 6f)
            for (i in 0 until 2) {
                val mid = (xs[i] + xs[i + 1]) / 2f
                val arc = Path().apply {
                    moveTo(xs[i] + ph * 0.36f, y - ph * 0.15f)
                    quadraticTo(mid, y - ph * 0.85f, xs[i + 1] - ph * 0.36f, y - ph * 0.15f)
                }
                drawPath(path = arc, color = Lagon, style = dashed(h))
                bubble(Offset(mid, y - ph * 0.78f), ph * 0.2f)
            }
            for (x in xs) phone(Offset(x, y), ph)
        }
        Row(
            modifier = Modifier
                .align(Alignment.BottomCenter)
                .fillMaxWidth()
                .padding(bottom = 14.dp)
        ) {
            for (label in listOf("Vous", "Voisin", "Mama")) {
                Text(
                    text = label,
                    modifier = Modifier.weight(1f),
                    textAlign = TextAlign.Center,
                    fontSize = 19.sp,
                    fontWeight = FontWeight.Bold,
                    color = Ocean
                )
            }
        }
    }
}

/** Page 3 : chaque téléphone agrandit le réseau, dans la vallée et au bord du lagon. */
@Composable
private fun NetworkSchema(modifier: Modifier) {
    Canvas(modifier = modifier) {
        val w = size.width
        val h = size.height
        drawRect(color = Ciel, size = Size(w, h))
        val montagnes = Path().apply {
            moveTo(0f, h * 0.72f)
            lineTo(w * 0.14f, h * 0.45f)
            lineTo(w * 0.24f, h * 0.56f)
            lineTo(w * 0.4f, h * 0.22f)
            lineTo(w * 0.55f, h * 0.52f)
            lineTo(w * 0.66f, h * 0.42f)
            lineTo(w * 0.84f, h * 0.72f)
            close()
        }
        drawPath(path = montagnes, color = Ocean.copy(alpha = 0.85f))
        drawRect(color = Lagon, topLeft = Offset(0f, h * 0.7f), size = Size(w, h * 0.3f))

        val nodes = listOf(
            Offset(w * 0.1f, h * 0.8f),
            Offset(w * 0.3f, h * 0.74f),
            Offset(w * 0.5f, h * 0.8f),
            Offset(w * 0.7f, h * 0.74f),
            Offset(w * 0.9f, h * 0.8f)
        )
        for (n in nodes) drawCircle(color = LagonClair.copy(alpha = 0.3f), radius = w * 0.11f, center = n)
        for (i in 0 until nodes.size - 1) {
            drawLine(
                color = Vanille,
                start = nodes[i],
                end = nodes[i + 1],
                strokeWidth = h * 0.016f,
                cap = StrokeCap.Round,
                pathEffect = PathEffect.dashPathEffect(floatArrayOf(h * 0.035f, h * 0.04f), 0f)
            )
        }
        for (n in nodes) {
            drawCircle(color = SableClair, radius = h * 0.045f, center = n)
            drawCircle(color = Ocean, radius = h * 0.02f, center = n)
        }
    }
}

/** Page 4 : mini écran de Reo Fenua avec les numéros des boutons importants. */
@Composable
private fun ScreenSchema(modifier: Modifier) {
    val measurer = rememberTextMeasurer()
    val numStyle = TextStyle(fontSize = 16.sp, fontWeight = FontWeight.Bold, color = Ocean)
    Canvas(modifier = modifier.background(Color(0xFFEFE5D5))) {
        val w = size.width
        val h = size.height
        val pw = h * 0.6f
        val phh = h * 0.9f
        val left = w / 2f - pw / 2f
        val top = h * 0.05f
        drawRoundRect(color = Ocean, topLeft = Offset(left, top), size = Size(pw, phh), cornerRadius = CornerRadius(pw * 0.1f))
        val sl = left + pw * 0.05f
        val st = top + phh * 0.04f
        val sw = pw * 0.9f
        val sh = phh * 0.92f
        drawRoundRect(color = SableClair, topLeft = Offset(sl, st), size = Size(sw, sh), cornerRadius = CornerRadius(pw * 0.06f))

        val nameY = st + sh * 0.08f
        drawRoundRect(
            color = Lagon,
            topLeft = Offset(sl + sw * 0.07f, nameY - sh * 0.03f),
            size = Size(sw * 0.42f, sh * 0.06f),
            cornerRadius = CornerRadius(sh * 0.02f)
        )
        val people = Offset(sl + sw * 0.85f, nameY)
        drawCircle(color = Lagon, radius = sh * 0.035f, center = people)
        val help = Offset(sl + sw * 0.85f, st + sh * 0.21f)
        drawCircle(color = Vanille, radius = sh * 0.045f, center = help)
        val inputY = st + sh * 0.9f
        drawRoundRect(
            color = Color.White,
            topLeft = Offset(sl + sw * 0.07f, inputY - sh * 0.04f),
            size = Size(sw * 0.62f, sh * 0.08f),
            cornerRadius = CornerRadius(sh * 0.04f)
        )
        drawCircle(color = Vanille, radius = sh * 0.045f, center = Offset(sl + sw * 0.84f, inputY))

        val r = h * 0.07f
        val gap = r * 2.3f
        val badges = listOf(
            Triple(Offset(left - gap, nameY), Offset(sl + sw * 0.07f, nameY), "1"),
            Triple(Offset(left + pw + gap, nameY), Offset(people.x + sh * 0.035f, nameY), "2"),
            Triple(Offset(left + pw + gap, help.y + h * 0.12f), Offset(help.x + sh * 0.04f, help.y), "3"),
            Triple(Offset(left - gap, inputY), Offset(sl + sw * 0.07f, inputY), "4")
        )
        for ((c, target, n) in badges) {
            drawLine(color = Ocean, start = c, end = target, strokeWidth = h * 0.01f)
            drawCircle(color = Vanille, radius = r, center = c)
            val t = measurer.measure(n, numStyle)
            drawText(t, topLeft = Offset(c.x - t.size.width / 2f, c.y - t.size.height / 2f))
        }
    }
}

/** Page 5 : cyclone, plus de réseau, mais les téléphones se parlent quand même. */
@Composable
private fun OutageSchema(modifier: Modifier) {
    Canvas(modifier = modifier) {
        val w = size.width
        val h = size.height
        drawRect(color = CielGris, size = Size(w, h))

        // Symbole du cyclone : un œil et deux bras en spirale
        val cc = Offset(w * 0.18f, h * 0.27f)
        val cr = h * 0.08f
        val spiral = Stroke(width = h * 0.035f, cap = StrokeCap.Round)
        drawCircle(color = Ocean.copy(alpha = 0.75f), radius = cr, center = cc, style = Stroke(width = h * 0.03f))
        val bras1 = Path().apply {
            moveTo(cc.x, cc.y - cr)
            quadraticTo(cc.x + cr * 1.9f, cc.y - cr * 1.6f, cc.x + cr * 2.1f, cc.y + cr * 0.2f)
        }
        val bras2 = Path().apply {
            moveTo(cc.x, cc.y + cr)
            quadraticTo(cc.x - cr * 1.9f, cc.y + cr * 1.6f, cc.x - cr * 2.1f, cc.y - cr * 0.2f)
        }
        drawPath(path = bras1, color = Ocean.copy(alpha = 0.75f), style = spiral)
        drawPath(path = bras2, color = Ocean.copy(alpha = 0.75f), style = spiral)

        // Antenne barrée : pas de réseau
        val ax = w * 0.82f
        drawLine(color = Ocean, start = Offset(ax, h * 0.12f), end = Offset(ax, h * 0.42f), strokeWidth = h * 0.02f)
        val ondes = Path().apply {
            moveTo(ax - h * 0.08f, h * 0.15f)
            quadraticTo(ax, h * 0.06f, ax + h * 0.08f, h * 0.15f)
        }
        drawPath(path = ondes, color = Ocean, style = Stroke(width = h * 0.015f, cap = StrokeCap.Round))
        drawLine(
            color = Rouge,
            start = Offset(ax - h * 0.11f, h * 0.1f),
            end = Offset(ax + h * 0.11f, h * 0.44f),
            strokeWidth = h * 0.03f,
            cap = StrokeCap.Round
        )

        // Deux téléphones qui se parlent quand même
        val y = h * 0.7f
        val ph = h * 0.32f
        val p1 = Offset(w * 0.3f, y)
        val p2 = Offset(w * 0.7f, y)
        val arc = Path().apply {
            moveTo(p1.x + ph * 0.36f, y - ph * 0.2f)
            quadraticTo(w / 2f, y - ph * 0.95f, p2.x - ph * 0.36f, y - ph * 0.2f)
        }
        drawPath(path = arc, color = Vanille, style = dashed(h))
        phone(p1, ph)
        phone(p2, ph)
        val ok = Path().apply {
            moveTo(w / 2f - h * 0.04f, y - ph * 0.72f)
            lineTo(w / 2f - h * 0.005f, y - ph * 0.62f)
            lineTo(w / 2f + h * 0.06f, y - ph * 0.86f)
        }
        drawPath(path = ok, color = Vert, style = Stroke(width = h * 0.025f, cap = StrokeCap.Round))

        // Batterie pleine
        val bw = h * 0.16f
        val bh = h * 0.08f
        val bl = Offset(w / 2f - bw / 2f, h * 0.9f - bh / 2f)
        drawRoundRect(color = Ocean, topLeft = bl, size = Size(bw, bh), cornerRadius = CornerRadius(h * 0.012f), style = Stroke(width = h * 0.012f))
        drawRect(color = Ocean, topLeft = Offset(bl.x + bw, bl.y + bh * 0.3f), size = Size(h * 0.015f, bh * 0.4f))
        drawRect(color = Vert, topLeft = Offset(bl.x + h * 0.012f, bl.y + h * 0.012f), size = Size(bw - h * 0.024f, bh - h * 0.024f))
    }
}
'''
UPDATE_KT = r'''package com.bitchat.android.ui

import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Build
import android.provider.Settings
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.core.content.FileProvider
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import org.json.JSONObject
import java.io.File
import java.net.HttpURLConnection
import java.net.URL

/** Reo Fenua : vérifie, télécharge et installe les nouvelles versions publiées dans les Releases GitHub. */
object ReoFenuaUpdate {
    const val REPO = "__REPO__"
    const val CURRENT_TAG = "__TAG__"

    class Release(val tag: String, val url: String, val size: Long, val fileName: String)

    /** Numéro de la nouvelle version si elle existe (sinon null). Sert à n'afficher le bouton que si besoin. */
    val available = androidx.compose.runtime.mutableStateOf<String?>(null)
    private var running = false
    /** « Plus tard » : on cache le bandeau jusqu'au prochain lancement de l'app. */
    val bannerHidden = androidx.compose.runtime.mutableStateOf(false)

    /** Vérifie au lancement puis toutes les 3 heures tant que l'app est ouverte (si internet). */
    suspend fun checkInBackground() {
        if (running) return
        running = true
        try {
            while (true) {
                try {
                    val r = withContext(Dispatchers.IO) { fetchLatest() }
                    if (r != null && r.tag != CURRENT_TAG) available.value = r.tag
                } catch (e: Exception) {
                    // pas d'internet : on réessaiera plus tard
                }
                kotlinx.coroutines.delay(3L * 3600 * 1000)
            }
        } finally {
            running = false
        }
    }

    /** Choisit la version la plus légère adaptée à ce téléphone, sinon la version universelle. */
    fun fetchLatest(): Release? {
        val conn = URL("https://api.github.com/repos/$REPO/releases/latest")
            .openConnection() as HttpURLConnection
        conn.connectTimeout = 15000
        conn.readTimeout = 15000
        conn.setRequestProperty("Accept", "application/vnd.github+json")
        conn.setRequestProperty("User-Agent", "ReoFenua")
        try {
            if (conn.responseCode != 200) return null
            val text = conn.inputStream.bufferedReader().use { it.readText() }
            val json = JSONObject(text)
            val tag = json.getString("tag_name")
            val assets = json.optJSONArray("assets") ?: return null
            val byName = HashMap<String, JSONObject>()
            for (i in 0 until assets.length()) {
                val a = assets.getJSONObject(i)
                byName[a.optString("name")] = a
            }
            val wanted = ArrayList<String>()
            for (abi in Build.SUPPORTED_ABIS) wanted.add("reo-fenua-$abi.apk")
            wanted.add("reo-fenua.apk")
            var chosen: JSONObject? = null
            for (name in wanted) {
                val a = byName[name]
                if (a != null) {
                    chosen = a
                    break
                }
            }
            if (chosen == null) {
                for (a in byName.values) {
                    if (a.optString("name").endsWith(".apk")) {
                        chosen = a
                        break
                    }
                }
            }
            val asset = chosen ?: return null
            return Release(
                tag = tag,
                url = asset.getString("browser_download_url"),
                size = asset.optLong("size", -1L),
                fileName = asset.optString("name")
            )
        } finally {
            conn.disconnect()
        }
    }

    fun updateFile(context: Context): File {
        val dir = File(context.cacheDir, "apk_update")
        dir.mkdirs()
        return File(dir, "reo-fenua-update.apk")
    }

    /** Télécharge le fichier en entier ; renvoie true seulement s'il est complet. */
    fun download(context: Context, release: Release, onProgress: (Float) -> Unit): Boolean {
        val target = updateFile(context)
        val partial = File(target.parentFile, target.name + ".part")
        partial.delete()
        val conn = URL(release.url).openConnection() as HttpURLConnection
        conn.connectTimeout = 20000
        conn.readTimeout = 30000
        conn.instanceFollowRedirects = true
        conn.setRequestProperty("User-Agent", "ReoFenua")
        try {
            if (conn.responseCode != 200) return false
            val total = if (release.size > 0) release.size else conn.contentLengthLong
            var done = 0L
            conn.inputStream.use { input ->
                partial.outputStream().use { output ->
                    val buffer = ByteArray(64 * 1024)
                    while (true) {
                        val n = input.read(buffer)
                        if (n < 0) break
                        output.write(buffer, 0, n)
                        done += n
                        if (total > 0) onProgress((done.toFloat() / total.toFloat()).coerceIn(0f, 1f))
                    }
                }
            }
            if (total > 0 && done != total) {
                partial.delete()
                return false
            }
            target.delete()
            return partial.renameTo(target)
        } finally {
            conn.disconnect()
        }
    }

    /** Lance l'installation ; renvoie false si Android demande d'abord l'autorisation. */
    fun install(context: Context): Boolean {
        if (!context.packageManager.canRequestPackageInstalls()) {
            val settings = Intent(
                Settings.ACTION_MANAGE_UNKNOWN_APP_SOURCES,
                Uri.parse("package:" + context.packageName)
            )
            settings.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            context.startActivity(settings)
            return false
        }
        val uri = FileProvider.getUriForFile(
            context,
            context.packageName + ".fileprovider",
            updateFile(context)
        )
        val intent = Intent(Intent.ACTION_VIEW)
        intent.setDataAndType(uri, "application/vnd.android.package-archive")
        intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        context.startActivity(intent)
        return true
    }
}

@Composable
fun ReoFenuaUpdateCard() {
    val context = LocalContext.current
    val scope = rememberCoroutineScope()
    var status by remember { mutableStateOf("Version installée : " + ReoFenuaUpdate.CURRENT_TAG) }
    var release by remember { mutableStateOf<ReoFenuaUpdate.Release?>(null) }
    var busy by remember { mutableStateOf(false) }
    var downloading by remember { mutableStateOf(false) }
    var progress by remember { mutableFloatStateOf(0f) }
    var ready by remember { mutableStateOf(false) }

    fun startInstall() {
        try {
            if (!ReoFenuaUpdate.install(context)) {
                status = "Autorisez Reo Fenua à installer des applications dans l'écran qui s'ouvre, puis revenez et touchez « Installer »."
            }
        } catch (e: Exception) {
            status = "L'installation n'a pas pu démarrer. Réessayez."
        }
    }

    Surface(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp, vertical = 12.dp),
        color = MaterialTheme.colorScheme.primaryContainer,
        shape = MaterialTheme.shapes.large
    ) {
        Column(
            modifier = Modifier.padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(10.dp)
        ) {
            Text(
                text = "Mises à jour",
                fontSize = 19.sp,
                fontWeight = FontWeight.Bold,
                color = MaterialTheme.colorScheme.onPrimaryContainer
            )
            Text(
                text = status,
                fontSize = 16.sp,
                color = MaterialTheme.colorScheme.onPrimaryContainer
            )
            if (downloading) {
                LinearProgressIndicator(
                    progress = { progress },
                    modifier = Modifier.fillMaxWidth()
                )
                Text(
                    text = "Téléchargement : " + (progress * 100f).toInt() + " %",
                    fontSize = 15.sp,
                    color = MaterialTheme.colorScheme.onPrimaryContainer
                )
            }
            val rel = release
            when {
                ready -> {
                    Button(
                        onClick = { startInstall() },
                        modifier = Modifier
                            .fillMaxWidth()
                            .heightIn(min = 52.dp)
                    ) {
                        Text(text = "Installer la mise à jour", fontSize = 17.sp)
                    }
                }
                rel != null && !downloading -> {
                    Button(
                        onClick = {
                            downloading = true
                            progress = 0f
                            status = "Téléchargement en cours… Gardez l'application ouverte."
                            scope.launch {
                                val ok = try {
                                    withContext(Dispatchers.IO) {
                                        ReoFenuaUpdate.download(context, rel) { p -> progress = p }
                                    }
                                } catch (e: Exception) {
                                    false
                                }
                                downloading = false
                                if (ok) {
                                    ready = true
                                    status = "Téléchargement terminé ! Touchez « Installer », puis « Mettre à jour ». Vos messages sont conservés."
                                    startInstall()
                                } else {
                                    status = "Le téléchargement s'est arrêté (connexion coupée ?). Touchez à nouveau pour réessayer."
                                }
                            }
                        },
                        modifier = Modifier
                            .fillMaxWidth()
                            .heightIn(min = 52.dp)
                    ) {
                        Text(text = "Télécharger la mise à jour", fontSize = 17.sp)
                    }
                }
                !downloading -> {
                    Button(
                        enabled = !busy,
                        onClick = {
                            busy = true
                            status = "Recherche en cours…"
                            scope.launch {
                                val result = try {
                                    withContext(Dispatchers.IO) { ReoFenuaUpdate.fetchLatest() }
                                } catch (e: Exception) {
                                    null
                                }
                                busy = false
                                if (result == null) {
                                    status = "Impossible de vérifier. Il faut une connexion internet."
                                } else if (result.tag == ReoFenuaUpdate.CURRENT_TAG) {
                                    status = "Vous avez la dernière version (" + result.tag + ")."
                                } else {
                                    val mo = if (result.size > 0) " (" + (result.size / (1024 * 1024)) + " Mo)" else ""
                                    status = "Nouvelle version disponible : " + result.tag + mo +
                                        ".\nConseil : utilisez le Wi-Fi pour ne pas consommer votre forfait."
                                    release = result
                                }
                            }
                        },
                        modifier = Modifier
                            .fillMaxWidth()
                            .heightIn(min = 52.dp)
                    ) {
                        Text(text = "Rechercher une mise à jour", fontSize = 17.sp)
                    }
                }
            }
        }
    }
}
'''
MAILBOX_KT = r'''package com.bitchat.android.ui

import android.content.Context
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import com.bitchat.android.model.BitchatMessage
import com.bitchat.android.model.DeliveryStatus
import kotlinx.coroutines.launch
import org.json.JSONArray
import org.json.JSONObject
import java.io.File
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

/**
 * Reo Fenua : Boîte aux lettres.
 * Une lettre est un message privé chiffré qui commence par « ✉ Sujet ».
 * L'application garde sa propre copie des lettres pour qu'aucune ne se perde.
 */
data class ReoLetter(
    val id: String,
    val conversation: String,
    val name: String,
    val subject: String,
    val body: String,
    val time: Long,
    val incoming: Boolean,
    val status: String,
    val opened: Boolean
)

object ReoFenuaLetters {
    const val MARK = "✉ "
    private const val FILE = "reo_letters.json"

    val letters = mutableStateListOf<ReoLetter>()
    val show = mutableStateOf(false)

    /** Personne à qui écrire directement (depuis « Mes proches »). */
    val writeTo = mutableStateOf<String?>(null)
    private var loaded = false

    fun format(subject: String, body: String): String =
        MARK + subject.trim().ifEmpty { "Sans sujet" } + "\n\n" + body.trim()

    fun parse(content: String): Pair<String, String> {
        val rest = content.removePrefix(MARK)
        val cut = rest.indexOf("\n\n")
        return if (cut >= 0) Pair(rest.substring(0, cut).trim(), rest.substring(cut + 2).trim())
        else Pair(rest.trim(), "")
    }

    fun statusOf(status: DeliveryStatus?): String = when (status) {
        is DeliveryStatus.Read -> "read"
        is DeliveryStatus.Delivered -> "delivered"
        is DeliveryStatus.PartiallyDelivered -> "delivered"
        is DeliveryStatus.Failed -> "waiting"
        is DeliveryStatus.Sent -> "sent"
        else -> "waiting"
    }

    fun load(context: Context) {
        if (loaded) return
        loaded = true
        try {
            val f = File(context.filesDir, FILE)
            if (!f.exists()) return
            val raw = f.readText()
            val plain = ReoFenuaVault.open(raw) ?: return
            val arr = JSONArray(plain)
            val wasPlain = !ReoFenuaVault.isSealed(raw)
            val list = ArrayList<ReoLetter>()
            for (i in 0 until arr.length()) {
                val o = arr.getJSONObject(i)
                list.add(
                    ReoLetter(
                        id = o.getString("id"),
                        conversation = o.optString("conversation"),
                        name = o.optString("name"),
                        subject = o.optString("subject"),
                        body = o.optString("body"),
                        time = o.optLong("time"),
                        incoming = o.optBoolean("incoming"),
                        status = o.optString("status", "waiting"),
                        opened = o.optBoolean("opened")
                    )
                )
            }
            // Les lettres de plus de 30 jours sont effacées automatiquement
            val limit = System.currentTimeMillis() - 30L * 24 * 3600 * 1000
            val kept = list.filter { it.time == 0L || it.time >= limit }
            letters.clear()
            letters.addAll(kept)
            if (kept.size != list.size || wasPlain) save(context)
        } catch (e: Exception) {
            // fichier abîmé : on repart d'une boîte vide
        }
    }

    fun save(context: Context) {
        try {
            val arr = JSONArray()
            for (l in letters) {
                val o = JSONObject()
                o.put("id", l.id)
                o.put("conversation", l.conversation)
                o.put("name", l.name)
                o.put("subject", l.subject)
                o.put("body", l.body)
                o.put("time", l.time)
                o.put("incoming", l.incoming)
                o.put("status", l.status)
                o.put("opened", l.opened)
                arr.put(o)
            }
            File(context.filesDir, FILE).writeText(ReoFenuaVault.seal(arr.toString()))
        } catch (e: Exception) {
            // on réessaiera à la prochaine lettre
        }
    }

    /** Récupère les lettres présentes dans les conversations privées et met à jour leur état. */
    fun ingest(
        context: Context,
        chats: Map<String, List<BitchatMessage>>,
        myPeerID: String,
        myNickname: String
    ) {
        load(context)
        var changed = false
        for ((conversation, messages) in chats) {
            for (m in messages) {
                if (!m.content.startsWith(MARK)) continue
                val mine = m.senderPeerID == myPeerID || (m.senderPeerID == null && m.sender == myNickname)
                val index = letters.indexOfFirst { it.id == m.id }
                if (index < 0) {
                    val (subject, body) = parse(m.content)
                    val local = if (mine) letters.indexOfFirst {
                        it.id.startsWith("local-") && !it.incoming && it.subject == subject && it.body == body
                    } else -1
                    if (local >= 0) {
                        letters[local] = letters[local].copy(id = m.id, status = statusOf(m.deliveryStatus))
                        changed = true
                        continue
                    }
                    val name = if (mine) (m.recipientNickname ?: "?") else m.sender
                    letters.add(
                        ReoLetter(
                            id = m.id,
                            conversation = conversation,
                            name = name,
                            subject = subject,
                            body = body,
                            time = m.timestamp.time,
                            incoming = !mine,
                            status = if (mine) statusOf(m.deliveryStatus) else "received",
                            opened = mine
                        )
                    )
                    changed = true
                } else if (mine) {
                    val old = letters[index]
                    val st = statusOf(m.deliveryStatus)
                    if (rank(st) > rank(old.status)) {
                        letters[index] = old.copy(status = st)
                        changed = true
                    }
                }
            }
        }
        if (changed) save(context)
    }

    private fun rank(s: String): Int = when (s) {
        "read" -> 3
        "delivered" -> 2
        "sent" -> 1
        else -> 0
    }

    /** Copie locale d'une lettre envoyée, au cas où elle n'apparaît pas tout de suite dans les conversations. */
    fun rememberSent(context: Context, conversation: String, name: String, content: String) {
        load(context)
        val (subject, body) = parse(content)
        val exists = letters.any { !it.incoming && it.subject == subject && it.body == body && it.conversation == conversation }
        if (!exists) {
            letters.add(
                ReoLetter(
                    id = "local-" + System.currentTimeMillis(),
                    conversation = conversation,
                    name = name,
                    subject = subject,
                    body = body,
                    time = System.currentTimeMillis(),
                    incoming = false,
                    status = "waiting",
                    opened = true
                )
            )
            save(context)
        }
    }

    fun markOpened(context: Context, id: String) {
        val i = letters.indexOfFirst { it.id == id }
        if (i >= 0 && !letters[i].opened) {
            letters[i] = letters[i].copy(opened = true)
            save(context)
        }
    }

    fun unreadCount(): Int = letters.count { it.incoming && !it.opened && !ReoFenuaBlock.isBlocked(it.conversation) }
}

private val LOcean = Color(0xFF0B3C5D)
private val LLagon = Color(0xFF0E7C86)
private val LVanille = Color(0xFFE8B33A)
private val LVert = Color(0xFF2E7D32)
private val LGris = Color(0xFFC9BBA4)

private val quickMessages = listOf(
    "Je vais bien.",
    "J'ai besoin d'eau.",
    "J'ai besoin d'un médecin.",
    "Où es-tu ?",
    "Appelle-moi dès que possible."
)

private fun dateText(time: Long): String =
    SimpleDateFormat("d MMM 'à' HH'h'mm", Locale.FRENCH).format(Date(time))

/** Toujours présent sur l'écran principal : récupère les lettres et ouvre la boîte quand on la demande. */
@Composable
fun ReoFenuaMailboxHost(viewModel: ChatViewModel) {
    val context = LocalContext.current
    val chats by viewModel.privateChats.collectAsState()
    val nickname by viewModel.nickname.collectAsState()
    LaunchedEffect(chats) {
        ReoFenuaContacts.load(context)
        ReoFenuaLetters.ingest(context, chats, viewModel.myPeerID, nickname)
    }
    if (ReoFenuaLetters.show.value) {
        Dialog(
            onDismissRequest = { ReoFenuaLetters.show.value = false },
            properties = DialogProperties(usePlatformDefaultWidth = false)
        ) {
            Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
                MailboxScreen(viewModel = viewModel, onClose = { ReoFenuaLetters.show.value = false })
            }
        }
    }
}

private class ReoPerson(val id: String, val name: String)

@Composable
private fun MailboxScreen(viewModel: ChatViewModel, onClose: () -> Unit) {
    val context = LocalContext.current
    var tab by remember { mutableStateOf(0) }
    var writing by remember { mutableStateOf(false) }
    var openId by remember { mutableStateOf<String?>(null) }
    var replyTo by remember { mutableStateOf<String?>(null) }
    var replySubject by remember { mutableStateOf("") }
    LaunchedEffect(Unit) {
        val dest = ReoFenuaLetters.writeTo.value
        if (dest != null) {
            replyTo = dest
            replySubject = ""
            writing = true
            ReoFenuaLetters.writeTo.value = null
        }
    }

    Column(modifier = Modifier.fillMaxSize()) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .background(LLagon)
                .padding(start = 20.dp, end = 8.dp, top = reoHeaderTop(), bottom = 14.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            Column(modifier = Modifier.weight(1f)) {
                Text(
                    text = if (writing) "Écrire une lettre" else "✉ Boîte aux lettres",
                    fontSize = 24.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.White
                )
                Text(
                    text = if (writing) "Elle partira dès que possible" else "Vos lettres voyagent de téléphone en téléphone",
                    fontSize = 14.sp,
                    color = Color.White
                )
            }
            TextButton(onClick = {
                when {
                    writing -> writing = false
                    openId != null -> openId = null
                    else -> onClose()
                }
            }) {
                Text(text = "← Retour", fontSize = 17.sp, color = Color.White)
            }
        }
        NihoManoBand(
            modifier = Modifier
                .fillMaxWidth()
                .height(12.dp)
        )

        val current = openId?.let { id -> ReoFenuaLetters.letters.firstOrNull { it.id == id } }
        when {
            writing -> WriteLetter(
                viewModel = viewModel,
                initialTo = replyTo,
                initialSubject = replySubject,
                onSent = {
                    writing = false
                    tab = 1
                }
            )
            current != null -> LetterDetail(
                letter = current,
                onReply = {
                    replyTo = current.conversation
                    replySubject = if (current.subject.startsWith("Re :")) current.subject else "Re : " + current.subject
                    openId = null
                    writing = true
                }
            )
            else -> {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(horizontal = 16.dp, vertical = 10.dp),
                    horizontalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    val unread = ReoFenuaLetters.unreadCount()
                    val labels = listOf(if (unread > 0) "Reçues ($unread)" else "Reçues", "Envoyées")
                    for (i in 0..1) {
                        if (tab == i) {
                            Button(onClick = { tab = i }, modifier = Modifier.weight(1f).heightIn(min = 48.dp)) {
                                Text(text = labels[i], fontSize = 16.sp)
                            }
                        } else {
                            OutlinedButton(onClick = { tab = i }, modifier = Modifier.weight(1f).heightIn(min = 48.dp)) {
                                Text(text = labels[i], fontSize = 16.sp)
                            }
                        }
                    }
                }
                val list = ReoFenuaLetters.letters
                    .filter { it.incoming == (tab == 0) }
                    .filter { !(it.incoming && ReoFenuaBlock.isBlocked(it.conversation)) }
                    .sortedByDescending { it.time }
                Column(
                    modifier = Modifier
                        .weight(1f)
                        .fillMaxWidth()
                        .verticalScroll(rememberScrollState())
                        .padding(horizontal = 16.dp),
                    verticalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    if (list.isEmpty()) {
                        Text(
                            text = if (tab == 0) "Aucune lettre reçue pour le moment." else "Vous n'avez pas encore envoyé de lettre.",
                            fontSize = 17.sp,
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                            modifier = Modifier.padding(top = 24.dp)
                        )
                    }
                    for (l in list) {
                        LetterRow(letter = l, onClick = {
                            ReoFenuaLetters.markOpened(context, l.id)
                            openId = l.id
                        })
                    }
                    Spacer(modifier = Modifier.height(90.dp))
                }
                TextButton(
                    onClick = { ReoFenuaContacts.show.value = true },
                    modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp)
                ) {
                    Text(text = "Mes proches : ajouter un nom et une photo", fontSize = 16.sp)
                }
                Box(modifier = Modifier.fillMaxWidth().padding(start = 16.dp, end = 16.dp, bottom = 16.dp)) {
                    Button(
                        onClick = {
                            replyTo = null
                            replySubject = ""
                            writing = true
                        },
                        modifier = Modifier
                            .fillMaxWidth()
                            .heightIn(min = 56.dp)
                    ) {
                        Text(text = "✎  Écrire une lettre", fontSize = 18.sp)
                    }
                }
            }
        }
    }
}

@Composable
private fun LetterRow(letter: ReoLetter, onClick: () -> Unit) {
    Surface(
        modifier = Modifier
            .fillMaxWidth()
            .clickable { onClick() },
        color = MaterialTheme.colorScheme.surface,
        shape = MaterialTheme.shapes.large
    ) {
        val shownName = ReoFenuaContacts.nameFor(letter.conversation, letter.name)
        Row(modifier = Modifier.padding(14.dp), verticalAlignment = Alignment.Top) {
            ReoFenuaAvatar(key = letter.conversation, name = shownName, size = 46.dp)
            Column(
                modifier = Modifier
                    .weight(1f)
                    .padding(start = 12.dp)
            ) {
                Text(
                    text = (if (letter.incoming) "" else "À : ") + shownName,
                    fontSize = 17.sp,
                    fontWeight = FontWeight.Bold,
                    color = MaterialTheme.colorScheme.onSurface
                )
                Text(
                    text = letter.subject,
                    fontSize = 16.sp,
                    fontWeight = FontWeight.SemiBold,
                    color = MaterialTheme.colorScheme.onSurface
                )
                Text(
                    text = letter.body.take(70),
                    fontSize = 15.sp,
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
                Text(
                    text = dateText(letter.time) + (if (letter.incoming) "" else " · " + statusLabel(letter.status)),
                    fontSize = 13.sp,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    modifier = Modifier.padding(top = 4.dp)
                )
            }
            if (letter.incoming && !letter.opened) {
                Box(
                    modifier = Modifier
                        .padding(top = 4.dp)
                        .size(12.dp)
                        .background(LVanille, CircleShape)
                )
            }
        }
    }
}

private fun statusLabel(s: String): String = when (s) {
    "read" -> "Lue"
    "delivered" -> "Arrivée"
    "sent" -> "En route"
    else -> "En attente"
}

@Composable
private fun LetterDetail(letter: ReoLetter, onReply: () -> Unit) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(14.dp)
    ) {
        Text(
            text = letter.subject,
            fontSize = 24.sp,
            fontWeight = FontWeight.Bold,
            color = MaterialTheme.colorScheme.primary
        )
        Text(
            text = (if (letter.incoming) "De : " else "À : ") + ReoFenuaContacts.nameFor(letter.conversation, letter.name) + " · " + dateText(letter.time),
            fontSize = 15.sp,
            color = MaterialTheme.colorScheme.onSurfaceVariant
        )
        if (!letter.incoming) {
            Surface(color = MaterialTheme.colorScheme.surface, shape = MaterialTheme.shapes.large) {
                Column(modifier = Modifier.fillMaxWidth().padding(14.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                    Text(text = "Où est votre lettre ?", fontSize = 16.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onSurface)
                    val r = when (letter.status) { "read" -> 3; "delivered" -> 2; "sent" -> 1; else -> 0 }
                    StepLine(done = true, label = if (r >= 1) "Partie de votre téléphone" else "En attente que " + letter.name + " soit joignable (jusqu'à 24 h)")
                    StepLine(done = r >= 2, label = "Arrivée chez " + letter.name)
                    StepLine(done = r >= 3, label = "Lue")
                }
            }
        }
        Surface(color = MaterialTheme.colorScheme.surface, shape = MaterialTheme.shapes.large) {
            Text(
                text = letter.body,
                fontSize = 18.sp,
                lineHeight = 27.sp,
                color = MaterialTheme.colorScheme.onSurface,
                modifier = Modifier.fillMaxWidth().padding(16.dp)
            )
        }
        if (letter.incoming) {
            Button(
                onClick = onReply,
                modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp)
            ) {
                Text(text = "Répondre", fontSize = 18.sp)
            }
        }
    }
}

@Composable
private fun StepLine(done: Boolean, label: String) {
    Row(verticalAlignment = Alignment.CenterVertically) {
        Box(
            modifier = Modifier
                .size(26.dp)
                .background(if (done) LVert else LGris, CircleShape),
            contentAlignment = Alignment.Center
        ) {
            if (done) Text(text = "✓", fontSize = 15.sp, fontWeight = FontWeight.Bold, color = Color.White)
        }
        Text(
            text = label,
            fontSize = 16.sp,
            color = MaterialTheme.colorScheme.onSurface,
            modifier = Modifier.padding(start = 12.dp)
        )
    }
}

@Composable
private fun WriteLetter(
    viewModel: ChatViewModel,
    initialTo: String?,
    initialSubject: String,
    onSent: () -> Unit
) {
    val context = LocalContext.current
    val scope = rememberCoroutineScope()
    val chats by viewModel.privateChats.collectAsState()
    val nicknames by viewModel.peerNicknames.collectAsState()
    val myNick by viewModel.nickname.collectAsState()

    // Les personnes connues : conversations privées existantes + personnes autour maintenant
    val people = remember(chats, nicknames) {
        val map = LinkedHashMap<String, String>()
        for ((conv, msgs) in chats) {
            val other = msgs.lastOrNull { it.senderPeerID != viewModel.myPeerID && it.sender != myNick }
            val name = other?.sender ?: msgs.lastOrNull()?.recipientNickname ?: nicknames[conv]
            if (!name.isNullOrBlank()) map[conv] = name
        }
        for ((id, name) in nicknames) {
            if (id != viewModel.myPeerID && !map.containsKey(id) && name.isNotBlank()) map[id] = name
        }
        map.map { ReoPerson(it.key, it.value) }
    }

    var to by remember { mutableStateOf(initialTo) }
    var subject by remember { mutableStateOf(initialSubject) }
    var body by remember { mutableStateOf("") }
    var info by remember { mutableStateOf("") }
    var sending by remember { mutableStateOf(false) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        Text(text = "À qui ?", fontSize = 16.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onSurface)
        if (people.isEmpty()) {
            Text(
                text = "Vous ne connaissez encore personne. Rencontrez d'abord quelqu'un dans « Autour de moi », puis vous pourrez lui écrire même quand il est loin.",
                fontSize = 16.sp,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }
        for (p in people) {
            val selected = to == p.id
            Surface(
                modifier = Modifier
                    .fillMaxWidth()
                    .clickable { to = p.id },
                color = if (selected) Color(0xFFD7ECEE) else MaterialTheme.colorScheme.surface,
                shape = MaterialTheme.shapes.large
            ) {
                Row(modifier = Modifier.padding(12.dp), verticalAlignment = Alignment.CenterVertically) {
                    val shown = ReoFenuaContacts.nameFor(p.id, p.name)
                    ReoFenuaAvatar(key = p.id, name = shown, size = 40.dp)
                    Text(
                        text = shown,
                        fontSize = 17.sp,
                        fontWeight = if (selected) FontWeight.Bold else FontWeight.Normal,
                        color = MaterialTheme.colorScheme.onSurface,
                        modifier = Modifier.weight(1f).padding(start = 12.dp)
                    )
                    if (selected) {
                        Box(
                            modifier = Modifier.size(28.dp).background(LLagon, CircleShape),
                            contentAlignment = Alignment.Center
                        ) {
                            Text(text = "✓", fontSize = 15.sp, fontWeight = FontWeight.Bold, color = Color.White)
                        }
                    }
                }
            }
        }

        OutlinedTextField(
            value = subject,
            onValueChange = { subject = it.take(80) },
            label = { Text("Sujet") },
            singleLine = true,
            modifier = Modifier.fillMaxWidth()
        )
        OutlinedTextField(
            value = body,
            onValueChange = { body = it },
            label = { Text("Votre lettre") },
            minLines = 5,
            modifier = Modifier.fillMaxWidth()
        )

        Text(text = "Messages rapides", fontSize = 15.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        for (q in quickMessages) {
            OutlinedButton(
                onClick = {
                    body = if (body.isBlank()) q else body.trimEnd() + " " + q
                    if (subject.isBlank()) subject = q.trimEnd('.', ' ', '?')
                },
                modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)
            ) {
                Text(text = q, fontSize = 16.sp)
            }
        }

        if (info.isNotEmpty()) {
            Text(text = info, fontSize = 16.sp, color = MaterialTheme.colorScheme.error)
        }

        Button(
            enabled = !sending,
            onClick = {
                val dest = to
                when {
                    dest == null -> info = "Choisissez à qui envoyer la lettre."
                    body.isBlank() -> info = "Écrivez quelques mots avant d'envoyer."
                    else -> {
                        sending = true
                        info = ""
                        val content = ReoFenuaLetters.format(subject, body)
                        scope.launch {
                            val before = viewModel.selectedPrivateChatPeer.value
                            // On ferme d'abord toute conversation ouverte, pour être sûr d'écrire à la bonne personne
                            if (before != null) viewModel.endPrivateChat()
                            try {
                                viewModel.startPrivateChat(dest)
                            } catch (e: Exception) {
                                // vérifié juste après
                            }
                            // Sécurité : on n'envoie JAMAIS la lettre si la conversation privée n'est pas ouverte,
                            // sinon elle partirait en public.
                            if (viewModel.selectedPrivateChatPeer.value == null) {
                                sending = false
                                info = "Impossible d'écrire à cette personne pour le moment. Réessayez quand elle aura été autour de vous."
                                if (before != null) viewModel.startPrivateChat(before)
                            } else {
                                val recipientName = people.firstOrNull { it.id == dest }?.let { ReoFenuaContacts.nameFor(it.id, it.name) } ?: "?"
                                viewModel.sendMessage(content)
                                kotlinx.coroutines.delay(1500)
                                ReoFenuaLetters.rememberSent(context, dest, recipientName, content)
                                viewModel.endPrivateChat()
                                if (before != null) viewModel.startPrivateChat(before)
                                sending = false
                                onSent()
                            }
                        }
                    }
                }
            },
            modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp)
        ) {
            Text(text = if (sending) "Envoi…" else "Envoyer la lettre ✉", fontSize = 18.sp)
        }
        Text(
            text = "La lettre est chiffrée : seule cette personne peut la lire. Si elle est loin, la lettre attend jusqu'à 24 h qu'elle soit joignable.",
            fontSize = 14.sp,
            color = MaterialTheme.colorScheme.onSurfaceVariant
        )
        Spacer(modifier = Modifier.height(24.dp))
    }
}
'''
SOUND_KT = r'''package com.bitchat.android.ui

import android.content.Context
import android.media.AudioAttributes
import android.media.AudioManager
import android.media.MediaPlayer
import android.net.Uri
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.bitchat.android.R

/** Reo Fenua : petit son polynésien quand un message, une photo, un fichier ou une lettre arrive. */
object ReoFenuaSound {
    private const val PREFS = "reo_fenua_guide"
    private const val KEY = "message_sound"

    val names = listOf("Ukulélé", "Pū (conque)", "Clochette", "Aucun son")
    val choice = mutableStateOf(-1)
    private var lastPlay = 0L

    fun load(context: Context) {
        if (choice.value < 0) {
            choice.value = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getInt(KEY, 0)
        }
    }

    fun save(context: Context, value: Int) {
        choice.value = value
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putInt(KEY, value).apply()
    }

    private fun resId(index: Int): Int = when (index) {
        0 -> R.raw.reo_ukulele
        1 -> R.raw.reo_pu
        2 -> R.raw.reo_clochette
        else -> 0
    }

    /** Joue le son choisi. Respecte le mode silencieux / vibreur du téléphone. */
    fun play(context: Context, index: Int = -1, force: Boolean = false) {
        load(context)
        val chosen = if (index >= 0) index else choice.value
        val id = resId(chosen)
        if (id == 0) return
        val now = System.currentTimeMillis()
        if (!force && now - lastPlay < 1500) return
        lastPlay = now
        val audio = context.getSystemService(Context.AUDIO_SERVICE) as? AudioManager
        if (audio != null && audio.ringerMode != AudioManager.RINGER_MODE_NORMAL) return
        try {
            val player = MediaPlayer()
            player.setAudioAttributes(
                AudioAttributes.Builder()
                    .setUsage(AudioAttributes.USAGE_NOTIFICATION_EVENT)
                    .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
                    .build()
            )
            player.setDataSource(context, Uri.parse("android.resource://" + context.packageName + "/" + id))
            player.setOnCompletionListener { it.release() }
            player.setOnErrorListener { p, _, _ ->
                p.release()
                true
            }
            player.prepare()
            player.start()
        } catch (e: Exception) {
            // pas de son possible : on continue sans
        }
    }
}

/** Écoute les nouveaux messages (publics, privés, lettres, photos, fichiers…) et joue le son. */
@Composable
fun ReoFenuaSoundWatcher(viewModel: ChatViewModel) {
    val context = LocalContext.current
    val messages by viewModel.messages.collectAsState()
    val chats by viewModel.privateChats.collectAsState()
    val seen = remember { HashSet<String>() }
    val primed = remember { mutableStateOf(false) }

    LaunchedEffect(messages, chats) {
        val me = viewModel.myPeerID
        val myNick = viewModel.nickname.value
        val recent = System.currentTimeMillis() - 120_000L
        var fresh = false
        var alert: com.bitchat.android.model.BitchatMessage? = null
        val all = ArrayList<com.bitchat.android.model.BitchatMessage>()
        all.addAll(messages)
        for (list in chats.values) all.addAll(list)
        for (m in all) {
            val isNew = seen.add(m.id)
            if (isNew && m.senderPeerID != me && m.sender != myNick && m.sender != "system") {
                ReoFenuaWellbeing.observe(context, m)
            }
            if (isNew && primed.value) {
                val fromOther = m.senderPeerID != me && m.sender != myNick && m.sender != "system"
                if (fromOther && m.timestamp.time > recent) {
                    fresh = true
                    if (m.content.startsWith(ReoFenuaAlert.PREFIX)) alert = m
                }
            }
        }
        primed.value = true
        val a = alert
        if (a != null) {
            // Alerte reçue : grande carte rouge et son du pū, même si un autre son est choisi.
            ReoFenuaAlert.received.value = Pair(a.sender, a.content)
            ReoFenuaSound.play(context, index = 1, force = true)
        } else if (fresh) {
            ReoFenuaSound.play(context)
        }
    }
}

/** Carte « Son des messages » dans l'écran d'information. */
@Composable
fun ReoFenuaSoundCard() {
    val context = LocalContext.current
    LaunchedEffect(Unit) { ReoFenuaSound.load(context) }
    val current = ReoFenuaSound.choice.value

    Surface(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp, vertical = 12.dp),
        color = MaterialTheme.colorScheme.surface,
        shape = MaterialTheme.shapes.large
    ) {
        Column(
            modifier = Modifier.padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(10.dp)
        ) {
            Text(
                text = "Son des messages",
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold,
                color = MaterialTheme.colorScheme.primary
            )
            Text(
                text = "Touchez un son pour l'écouter et le choisir. Le téléphone en mode silencieux reste silencieux.",
                fontSize = 15.sp,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
            for (rowStart in listOf(0, 2)) {
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    for (i in rowStart until rowStart + 2) {
                        val name = ReoFenuaSound.names[i]
                        val onPick = {
                            ReoFenuaSound.save(context, i)
                            ReoFenuaSound.play(context, i, force = true)
                        }
                        if (i == current) {
                            Button(
                                onClick = onPick,
                                modifier = Modifier
                                    .weight(1f)
                                    .heightIn(min = 52.dp)
                            ) {
                                Text(text = "✓ " + name, fontSize = 16.sp)
                            }
                        } else {
                            OutlinedButton(
                                onClick = onPick,
                                modifier = Modifier
                                    .weight(1f)
                                    .heightIn(min = 52.dp)
                            ) {
                                Text(text = name, fontSize = 16.sp)
                            }
                        }
                    }
                }
            }
        }
    }
}
'''
EASY_KT = r'''package com.bitchat.android.ui

import android.content.Context
import android.graphics.BitmapFactory
import android.net.Uri
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateMapOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import com.bitchat.android.model.DeliveryStatus
import org.json.JSONObject
import java.io.File

private val EOcean = Color(0xFF0B3C5D)
private val ELagon = Color(0xFF0E7C86)
private val EVanille = Color(0xFFE8B33A)
private val ERouge = Color(0xFFC8102E)
private val EVert = Color(0xFF2E7D32)

// ===================== Statut de livraison en mots =====================

/** Mot simple affiché à côté des coches sous vos messages privés. */
fun reoFenuaStatusWord(status: DeliveryStatus): String = when (status) {
    is DeliveryStatus.Sending -> "envoi…"
    is DeliveryStatus.Sent -> "parti"
    is DeliveryStatus.Delivered -> "arrivé"
    is DeliveryStatus.Read -> "lu"
    is DeliveryStatus.Failed -> "pas encore parti"
    is DeliveryStatus.PartiallyDelivered -> "arrivé " + status.reached + "/" + status.total
}

// ===================== Taille du texte =====================

object ReoFenuaTextSize {
    private const val PREFS = "reo_fenua_guide"
    private const val KEY = "text_scale"
    val names = listOf("Normal", "Grand", "Très grand")
    val values = listOf(1.0f, 1.15f, 1.3f)
    val scale = mutableStateOf(1.0f)
    private var loaded = false

    fun load(context: Context) {
        if (loaded) return
        loaded = true
        scale.value = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getFloat(KEY, 1.0f)
    }

    fun save(context: Context, value: Float) {
        scale.value = value
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putFloat(KEY, value).apply()
    }
}

// ===================== Mes proches (nom et photo) =====================

object ReoFenuaContacts {
    private const val FILE = "reo_contacts.json"
    val aliases = mutableStateMapOf<String, String>()
    val photoVersion = mutableStateOf(0)
    val show = mutableStateOf(false)
    private var loaded = false

    fun load(context: Context) {
        if (loaded) return
        loaded = true
        try {
            val f = File(context.filesDir, FILE)
            if (!f.exists()) return
            val o = JSONObject(f.readText())
            val keys = o.keys()
            while (keys.hasNext()) {
                val k = keys.next()
                aliases[k] = o.optString(k)
            }
        } catch (e: Exception) {
            // fichier abîmé : on repart de zéro
        }
    }

    fun save(context: Context) {
        try {
            val o = JSONObject()
            for ((k, v) in aliases) o.put(k, v)
            File(context.filesDir, FILE).writeText(o.toString())
        } catch (e: Exception) {
            // on réessaiera
        }
    }

    fun nameFor(key: String, fallback: String): String {
        val a = aliases[key]
        return if (a.isNullOrBlank()) fallback else a
    }

    fun rename(context: Context, key: String, name: String) {
        load(context)
        aliases[key] = name.trim().take(40)
        save(context)
    }

    fun photoFile(context: Context, key: String): File {
        val dir = File(context.filesDir, "reo_contacts")
        dir.mkdirs()
        val safe = key.replace(Regex("[^A-Za-z0-9_-]"), "_").take(80)
        return File(dir, "$safe.jpg")
    }
}

// ===================== Bloquer une personne =====================

/** Personnes bloquées (copie locale pour l'affichage ; le blocage réel est fait par l'application). */
object ReoFenuaBlock {
    private const val PREFS = "reo_fenua_guide"
    private const val KEY = "blocked_keys"
    val blocked = mutableStateMapOf<String, Boolean>()
    private var loaded = false

    fun load(context: Context) {
        if (loaded) return
        loaded = true
        val set = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getStringSet(KEY, emptySet()) ?: emptySet()
        for (s in set) blocked[s] = true
    }

    private fun save(context: Context) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit()
            .putStringSet(KEY, HashSet(blocked.keys)).apply()
    }

    fun isBlocked(key: String): Boolean = blocked[key] == true

    /** Bloque par l'identifiant, sinon par le pseudo. Renvoie false si la personne est introuvable. */
    fun block(context: Context, viewModel: ChatViewModel, key: String, nickname: String): Boolean {
        load(context)
        val mesh = viewModel.meshServiceFacade
        val ok = try {
            viewModel.privateChatManager.blockPeer(key, mesh) ||
                viewModel.privateChatManager.blockPeerByNickname(nickname, mesh)
        } catch (e: Exception) {
            false
        }
        if (ok) {
            blocked[key] = true
            save(context)
        }
        return ok
    }

    fun unblock(context: Context, viewModel: ChatViewModel, key: String, nickname: String) {
        load(context)
        val mesh = viewModel.meshServiceFacade
        try {
            if (!viewModel.privateChatManager.unblockPeer(key, mesh)) {
                viewModel.privateChatManager.unblockPeerByNickname(nickname, mesh)
            }
        } catch (e: Exception) {
            // on retire quand même de la liste locale
        }
        blocked.remove(key)
        save(context)
    }
}

/** Les personnes connues : conversations privées + personnes autour en ce moment. */
fun reoKnownPeople(
    chats: Map<String, List<com.bitchat.android.model.BitchatMessage>>,
    nicknames: Map<String, String>,
    myPeerID: String,
    myNick: String
): List<Pair<String, String>> {
    val map = LinkedHashMap<String, String>()
    for ((conv, msgs) in chats) {
        val other = msgs.lastOrNull { it.senderPeerID != myPeerID && it.sender != myNick && it.sender != "system" }
        val name = other?.sender ?: msgs.lastOrNull()?.recipientNickname ?: nicknames[conv]
        if (!name.isNullOrBlank()) map[conv] = name
    }
    for ((id, name) in nicknames) {
        if (id != myPeerID && !map.containsKey(id) && name.isNotBlank()) map[id] = name
    }
    return map.map { Pair(it.key, it.value) }
}

/** Photo ronde du proche, ou la première lettre de son nom. */
@Composable
fun ReoFenuaAvatar(key: String, name: String, size: Dp) {
    val context = LocalContext.current
    val version = ReoFenuaContacts.photoVersion.value
    val photo = remember(key, version) {
        val f = ReoFenuaContacts.photoFile(context, key)
        if (f.exists()) BitmapFactory.decodeFile(f.absolutePath)?.asImageBitmap() else null
    }
    if (photo != null) {
        Image(
            bitmap = photo,
            contentDescription = name,
            contentScale = ContentScale.Crop,
            modifier = Modifier
                .size(size)
                .clip(CircleShape)
        )
    } else if (ReoFenuaStyle.stylised) {
        ReoFenuaDrawnAvatar(key = key, size = size)
    } else {
        Box(
            modifier = Modifier
                .size(size)
                .background(Color(0xFFD7ECEE), CircleShape),
            contentAlignment = Alignment.Center
        ) {
            Text(
                text = name.trim().take(1).uppercase(),
                fontSize = (size.value * 0.42f).sp,
                fontWeight = FontWeight.Bold,
                color = EOcean
            )
        }
    }
}

// ===================== Alerte : messages rapides =====================

object ReoFenuaAlert {
    val show = mutableStateOf(false)

    /** Alerte reçue à montrer en grand : (nom de l'expéditeur, texte). */
    val received = mutableStateOf<Pair<String, String>?>(null)

    /** Les alertes urgentes commencent par ce mot, pour être reconnues à l'arrivée. */
    const val PREFIX = "ALERTE · "
    private const val PREFS = "reo_fenua_guide"
    private const val KEY_PLACE = "alert_place"
    private val lastSent = HashMap<String, Long>()

    fun loadPlace(context: Context): String =
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getString(KEY_PLACE, "") ?: ""

    fun savePlace(context: Context, place: String) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putString(KEY_PLACE, place.trim()).apply()
    }

    /** Une seule alerte identique par minute, pour éviter les envois en rafale. */
    fun canSend(message: String): Boolean {
        val last = lastSent[message] ?: 0L
        return System.currentTimeMillis() - last >= 60_000L
    }

    fun markSent(message: String) {
        lastSent[message] = System.currentTimeMillis()
    }

    /** Texte final : « ALERTE · J'ai besoin d'aide ! — Brian · Pirae, PK 3,5 ». */
    fun compose(text: String, urgent: Boolean, name: String, place: String): String {
        val who = StringBuilder()
        val n = name.trim()
        if (n.isNotEmpty() && !n.startsWith("anon")) who.append(n)
        val p = place.trim()
        if (p.isNotEmpty()) {
            if (who.isNotEmpty()) who.append(" · ")
            who.append(p)
        }
        val base = (if (urgent) PREFIX else "") + text
        return if (who.isEmpty()) base else base + " — " + who.toString()
    }
}

private class QuickAlert(
    val label: String,
    val text: String,
    val color: Color,
    val onColor: Color,
    val urgent: Boolean
)

private val quickAlerts = listOf(
    QuickAlert("Je vais bien", "Je vais bien.", EVert, Color.White, false),
    QuickAlert("J'ai besoin d'aide !", "J'ai besoin d'aide !", ERouge, Color.White, true),
    QuickAlert("Besoin d'eau", "J'ai besoin d'eau.", ELagon, Color.White, true),
    QuickAlert("Besoin d'un médecin", "J'ai besoin d'un médecin.", ERouge, Color.White, true),
    QuickAlert("Route coupée ici", "Attention : la route est coupée ici.", EVanille, EOcean, true),
    QuickAlert("Je suis à l'abri", "Je suis à l'abri.", EVert, Color.White, false),
    QuickAlert("Besoin de batterie", "J'ai besoin de recharger mon téléphone.", ELagon, Color.White, false),
    QuickAlert("Où êtes-vous ?", "Où êtes-vous ?", EOcean, Color.White, false)
)

// ===================== Étendre le réseau (Wi-Fi gratuit, Bluetooth) =====================

object ReoFenuaExtend {
    private fun open(context: Context, action: String): Boolean {
        return try {
            val intent = android.content.Intent(action)
            intent.addFlags(android.content.Intent.FLAG_ACTIVITY_NEW_TASK)
            context.startActivity(intent)
            true
        } catch (e: Exception) {
            false
        }
    }

    /** Ouvre la liste des Wi-Fi du téléphone : la personne choisit elle-même un réseau gratuit. */
    fun openWifi(context: Context) {
        val ok = if (android.os.Build.VERSION.SDK_INT >= 29) {
            open(context, android.provider.Settings.Panel.ACTION_WIFI)
        } else {
            false
        }
        if (!ok) open(context, android.provider.Settings.ACTION_WIFI_SETTINGS)
    }

    fun openBluetooth(context: Context) {
        open(context, android.provider.Settings.ACTION_BLUETOOTH_SETTINGS)
    }
}

/** Carte « Étendre le réseau » : Wi-Fi gratuit, Bluetooth, relais. Rien ne se fait sans votre accord. */
@Composable
fun ReoFenuaExtendCard(peopleAround: Int) {
    val context = LocalContext.current
    Surface(color = MaterialTheme.colorScheme.surface, shape = MaterialTheme.shapes.large) {
        Column(modifier = Modifier.fillMaxWidth().padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
            Text(text = "Étendre le réseau", fontSize = 19.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
            Text(
                text = if (peopleAround == 0) "Personne autour pour le moment. Montez en hauteur, rapprochez-vous d'une maison voisine, ou connectez-vous à un Wi-Fi gratuit : avec internet, vos messages vont plus loin."
                else "$peopleAround personne(s) autour. Avec un Wi-Fi gratuit, vos messages vont encore plus loin.",
                fontSize = 16.sp,
                color = MaterialTheme.colorScheme.onSurface
            )
            Button(
                onClick = { ReoFenuaExtend.openWifi(context) },
                modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
            ) { Text(text = "Chercher un Wi-Fi gratuit", fontSize = 17.sp) }
            OutlinedButton(
                onClick = { ReoFenuaExtend.openBluetooth(context) },
                modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
            ) { Text(text = "Allumer le Bluetooth", fontSize = 17.sp) }
            Text(
                text = "Vous choisissez vous-même le réseau : Reo Fenua ne se connecte jamais seul. Évitez les Wi-Fi qui demandent vos codes ou votre carte bancaire.",
                fontSize = 14.sp,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }
    }
}

// ===================== Votre nom (demandé une fois) =====================

object ReoFenuaName {
    private const val PREFS = "reo_fenua_guide"
    private const val KEY = "name_asked"
    val needsAsk = mutableStateOf(false)
    private var loaded = false

    fun load(context: Context, currentNick: String) {
        if (loaded) return
        loaded = true
        val asked = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getBoolean(KEY, false)
        needsAsk.value = !asked && currentNick.startsWith("anon")
    }

    fun done(context: Context) {
        needsAsk.value = false
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putBoolean(KEY, true).apply()
    }
}

@Composable
private fun NameAsker(viewModel: ChatViewModel) {
    val context = LocalContext.current
    val myNick by viewModel.nickname.collectAsState()
    LaunchedEffect(myNick) { if (myNick.isNotBlank()) ReoFenuaName.load(context, myNick) }
    if (!ReoFenuaName.needsAsk.value || ReoFenuaGuide.showIntro.value) return
    var name by remember { mutableStateOf("") }

    Dialog(
        onDismissRequest = { },
        properties = DialogProperties(usePlatformDefaultWidth = false, dismissOnClickOutside = false)
    ) {
        Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .verticalScroll(rememberScrollState())
            ) {
                NihoManoBand(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(top = reoHeaderTop())
                        .height(14.dp)
                )
                Column(modifier = Modifier.padding(24.dp), verticalArrangement = Arrangement.spacedBy(18.dp)) {
                    Text(text = "Comment vous appelez-vous ?", fontSize = 28.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
                    Text(
                        text = "Le nom que vos proches connaissent. Il s'affiche à côté de vos messages et de vos alertes.",
                        fontSize = 18.sp,
                        color = MaterialTheme.colorScheme.onBackground
                    )
                    OutlinedTextField(
                        value = name,
                        onValueChange = { name = it.take(30) },
                        label = { Text("Votre prénom (par exemple : Teva, Mama Hina…)") },
                        singleLine = true,
                        modifier = Modifier.fillMaxWidth()
                    )
                    Button(
                        onClick = {
                            val n = name.trim()
                            if (n.isNotEmpty()) viewModel.setNickname(n)
                            ReoFenuaName.done(context)
                        },
                        enabled = name.trim().isNotEmpty(),
                        modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp)
                    ) { Text(text = "Continuer", fontSize = 18.sp) }
                    TextButton(
                        onClick = { ReoFenuaName.done(context) },
                        modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)
                    ) { Text(text = "Plus tard (je pourrai toucher mon nom en haut)", fontSize = 15.sp) }
                }
            }
        }
    }
}

// ===================== Alerte reçue =====================

@Composable
private fun ReceivedAlertDialog(viewModel: ChatViewModel) {
    val alert = ReoFenuaAlert.received.value ?: return
    val sender = alert.first
    Dialog(onDismissRequest = { ReoFenuaAlert.received.value = null }) {
        Surface(color = ERouge, shape = MaterialTheme.shapes.extraLarge) {
            Column(modifier = Modifier.fillMaxWidth().padding(20.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
                Text(text = "ALERTE REÇUE", fontSize = 15.sp, fontWeight = FontWeight.Bold, color = Color.White)
                Text(
                    text = alert.second.removePrefix(ReoFenuaAlert.PREFIX),
                    fontSize = 22.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.White
                )
                Text(text = "Envoyée par : $sender", fontSize = 16.sp, color = Color.White)
                Button(
                    onClick = {
                        viewModel.sendMessage("J'arrive pour vous aider, $sender !")
                        ReoFenuaAlert.received.value = null
                    },
                    colors = ButtonDefaults.buttonColors(containerColor = Color.White, contentColor = ERouge),
                    modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp)
                ) { Text(text = "J'arrive", fontSize = 19.sp, fontWeight = FontWeight.Bold) }
                Button(
                    onClick = {
                        viewModel.sendMessage("Je préviens les secours pour $sender.")
                        ReoFenuaAlert.received.value = null
                    },
                    colors = ButtonDefaults.buttonColors(containerColor = Color.White, contentColor = ERouge),
                    modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp)
                ) { Text(text = "Je préviens les secours", fontSize = 17.sp) }
                TextButton(
                    onClick = { ReoFenuaAlert.received.value = null },
                    modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)
                ) { Text(text = "← Retour", fontSize = 17.sp, color = Color.White) }
            }
        }
    }
}

/** Texte gris dans la case d'écriture : dit qui pourra lire le message. */
fun reoFenuaPlaceholder(privatePeer: String?, channel: String?): String = when {
    privatePeer != null -> "Privé : seule cette personne peut lire"
    channel != null -> "Salon : les membres du salon peuvent lire"
    else -> "Public : tout le monde autour peut lire"
}

/** Hôte des écrans « faciles » : alerte et mes proches. Toujours présent sur l'écran principal. */
@Composable
fun ReoFenuaEasyHost(viewModel: ChatViewModel) {
    ReoFenuaLockHost(viewModel)
    NameAsker(viewModel)
    ReoFenuaCharterScreen()
    ReoFenuaModeChooser()
    ReceivedAlertDialog(viewModel)
    if (ReoFenuaAlert.show.value) {
        AlertDialogScreen(viewModel = viewModel, onClose = { ReoFenuaAlert.show.value = false })
    }
    if (ReoFenuaContacts.show.value) {
        Dialog(
            onDismissRequest = { ReoFenuaContacts.show.value = false },
            properties = DialogProperties(usePlatformDefaultWidth = false)
        ) {
            Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
                ContactsScreen(viewModel = viewModel, onClose = { ReoFenuaContacts.show.value = false })
            }
        }
    }
}

@Composable
private fun AlertDialogScreen(viewModel: ChatViewModel, onClose: () -> Unit) {
    val context = LocalContext.current
    val selected by viewModel.selectedPrivateChatPeer.collectAsState()
    val nicknames by viewModel.peerNicknames.collectAsState()
    val myNick by viewModel.nickname.collectAsState()
    val peers by viewModel.connectedPeers.collectAsState()
    var sentText by remember { mutableStateOf("") }
    var place by remember { mutableStateOf(ReoFenuaAlert.loadPlace(context)) }
    var pending by remember { mutableStateOf<QuickAlert?>(null) }
    var countdown by remember { mutableStateOf(3) }
    val target = selected?.let { id -> ReoFenuaContacts.nameFor(id, nicknames[id] ?: "cette personne") }
    val around = peers.count { it != viewModel.myPeerID }

    // Compte à rebours de 3 secondes : « Annuler » arrête tout.
    LaunchedEffect(pending) {
        val q = pending ?: return@LaunchedEffect
        countdown = 3
        while (countdown > 0) {
            kotlinx.coroutines.delay(1000)
            countdown -= 1
        }
        val message = ReoFenuaAlert.compose(q.text, q.urgent, myNick, place)
        if (ReoFenuaAlert.canSend(message)) {
            viewModel.sendMessage(message)
            ReoFenuaAlert.markSent(message)
            sentText = "Envoyé ✓  « " + message.removePrefix(ReoFenuaAlert.PREFIX) + " »"
        } else {
            sentText = "Ce message est déjà parti il y a moins d'une minute. Attendez un peu avant de le renvoyer."
        }
        pending = null
    }

    Dialog(
        onDismissRequest = onClose,
        properties = DialogProperties(usePlatformDefaultWidth = false)
    ) {
        Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
            Column(modifier = Modifier.fillMaxSize()) {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(ERouge)
                        .padding(start = 20.dp, end = 8.dp, top = reoHeaderTop(), bottom = 14.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Column(modifier = Modifier.weight(1f)) {
                        Text(text = "Message rapide", fontSize = 24.sp, fontWeight = FontWeight.Bold, color = Color.White)
                        Text(
                            text = if (target != null) "Envoyé à : $target" else "Envoyé à : tout le monde autour de vous",
                            fontSize = 15.sp,
                            color = Color.White
                        )
                    }
                    TextButton(onClick = onClose, modifier = Modifier.heightIn(min = 48.dp)) {
                        Text(text = "← Retour", fontSize = 17.sp, color = Color.White)
                    }
                }
                NihoManoBand(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(12.dp)
                )
                Column(
                    modifier = Modifier
                        .weight(1f)
                        .fillMaxWidth()
                        .verticalScroll(rememberScrollState())
                        .padding(16.dp),
                    verticalArrangement = Arrangement.spacedBy(12.dp)
                ) {
                    val q = pending
                    if (q != null) {
                        Surface(color = Color(0xFFFDECEE), shape = MaterialTheme.shapes.large) {
                            Column(modifier = Modifier.fillMaxWidth().padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                                Text(text = "Message qui va partir", fontSize = 14.sp, fontWeight = FontWeight.SemiBold, color = EOcean)
                                Text(
                                    text = ReoFenuaAlert.compose(q.text, false, myNick, place),
                                    fontSize = 20.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = EOcean
                                )
                                Row(verticalAlignment = Alignment.CenterVertically) {
                                    Box(
                                        modifier = Modifier
                                            .size(64.dp)
                                            .background(ERouge, CircleShape),
                                        contentAlignment = Alignment.Center
                                    ) {
                                        Text(text = countdown.toString(), fontSize = 30.sp, fontWeight = FontWeight.Bold, color = Color.White)
                                    }
                                    Text(
                                        text = "Envoi dans $countdown seconde(s)…\nTouchez « Annuler » si c'est une erreur.",
                                        fontSize = 16.sp,
                                        color = EOcean,
                                        modifier = Modifier.padding(start = 14.dp)
                                    )
                                }
                            }
                        }
                        OutlinedButton(
                            onClick = { pending = null; sentText = "Annulé : rien n'est parti." },
                            modifier = Modifier.fillMaxWidth().heightIn(min = 64.dp)
                        ) {
                            Text(text = "Annuler", fontSize = 22.sp, fontWeight = FontWeight.Bold)
                        }
                    } else {
                        Text(
                            text = "Touchez un bouton : vous avez 3 secondes pour annuler, puis le message part avec votre nom et votre lieu.",
                            fontSize = 17.sp,
                            color = MaterialTheme.colorScheme.onBackground
                        )
                        OutlinedTextField(
                            value = place,
                            onValueChange = {
                                place = it.take(60)
                                ReoFenuaAlert.savePlace(context, place)
                            },
                            label = { Text("Votre lieu (commune, quartier, PK, côté mer ou montagne)") },
                            singleLine = true,
                            modifier = Modifier.fillMaxWidth()
                        )
                        for (alertItem in quickAlerts) {
                            Button(
                                onClick = { sentText = ""; pending = alertItem },
                                colors = ButtonDefaults.buttonColors(containerColor = alertItem.color, contentColor = alertItem.onColor),
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .heightIn(min = 64.dp)
                            ) {
                                Text(text = alertItem.label, fontSize = 20.sp, fontWeight = FontWeight.Bold)
                            }
                        }
                    }
                    if (sentText.isNotEmpty()) {
                        Text(text = sentText, fontSize = 17.sp, fontWeight = FontWeight.SemiBold, color = EVert)
                    }
                    Text(
                        text = "Le message passe de téléphone en téléphone. Plus il y a de monde autour, plus il va loin.",
                        fontSize = 15.sp,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                    ReoFenuaExtendCard(peopleAround = around)
                    Spacer(modifier = Modifier.height(24.dp))
                }
            }
        }
    }
}

@Composable
private fun ContactsScreen(viewModel: ChatViewModel, onClose: () -> Unit) {
    val context = LocalContext.current
    LaunchedEffect(Unit) { ReoFenuaContacts.load(context) }
    val chats by viewModel.privateChats.collectAsState()
    val nicknames by viewModel.peerNicknames.collectAsState()
    val myNick by viewModel.nickname.collectAsState()
    val people = remember(chats, nicknames, myNick) {
        reoKnownPeople(chats, nicknames, viewModel.myPeerID, myNick)
    }
    var editing by remember { mutableStateOf<String?>(null) }
    var editText by remember { mutableStateOf("") }
    var pickingFor by remember { mutableStateOf<String?>(null) }
    var confirmBlock by remember { mutableStateOf<Pair<String, String>?>(null) }
    var blockInfo by remember { mutableStateOf("") }
    LaunchedEffect(Unit) { ReoFenuaBlock.load(context) }

    val picker = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.GetContent()
    ) { uri: Uri? ->
        val key = pickingFor
        if (uri != null && key != null) {
            val tmp = com.bitchat.android.features.media.ImageUtils.downscaleAndSaveToAppFiles(
                context, uri, maxDim = 400, quality = 85
            )
            if (tmp != null) {
                try {
                    val src = File(tmp)
                    src.copyTo(ReoFenuaContacts.photoFile(context, key), overwrite = true)
                    src.delete()
                    ReoFenuaContacts.photoVersion.value += 1
                } catch (e: Exception) {
                    // photo non enregistrée
                }
            }
        }
        pickingFor = null
    }

    Column(modifier = Modifier.fillMaxSize()) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .background(ELagon)
                .padding(start = 20.dp, end = 8.dp, top = reoHeaderTop(), bottom = 14.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            Column(modifier = Modifier.weight(1f)) {
                Text(text = "Mes proches", fontSize = 24.sp, fontWeight = FontWeight.Bold, color = Color.White)
                Text(text = "Donnez un nom et une photo à vos proches", fontSize = 14.sp, color = Color.White)
            }
            TextButton(onClick = onClose) {
                Text(text = "← Retour", fontSize = 17.sp, color = Color.White)
            }
        }
        NihoManoBand(
            modifier = Modifier
                .fillMaxWidth()
                .height(12.dp)
        )
        Column(
            modifier = Modifier
                .weight(1f)
                .fillMaxWidth()
                .verticalScroll(rememberScrollState())
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            if (people.isEmpty()) {
                Text(
                    text = "Personne pour le moment. Les personnes que vous rencontrez dans « Autour de moi » apparaîtront ici.",
                    fontSize = 17.sp,
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
            }
            if (blockInfo.isNotEmpty()) {
                Text(text = blockInfo, fontSize = 16.sp, fontWeight = FontWeight.SemiBold, color = ERouge)
            }
            val ask = confirmBlock
            if (ask != null) {
                Surface(color = Color(0xFFFDE3E7), shape = MaterialTheme.shapes.large) {
                    Column(modifier = Modifier.fillMaxWidth().padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                        Text(
                            text = "Bloquer " + ReoFenuaContacts.nameFor(ask.first, ask.second) + " ?",
                            fontSize = 19.sp,
                            fontWeight = FontWeight.Bold,
                            color = ERouge
                        )
                        Text(
                            text = "Vous ne recevrez plus ses messages ni ses lettres, et elle ne pourra plus vous écrire en privé. Vous pourrez la débloquer quand vous voulez.",
                            fontSize = 16.sp,
                            color = EOcean
                        )
                        Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                            Button(
                                onClick = {
                                    val ok = ReoFenuaBlock.block(context, viewModel, ask.first, ask.second)
                                    blockInfo = if (ok) "Personne bloquée." else "Impossible pour le moment : la personne doit avoir été autour de vous récemment. Réessayez plus tard."
                                    confirmBlock = null
                                },
                                colors = ButtonDefaults.buttonColors(containerColor = ERouge, contentColor = Color.White),
                                modifier = Modifier.weight(1f).heightIn(min = 52.dp)
                            ) { Text(text = "Oui, bloquer", fontSize = 16.sp) }
                            OutlinedButton(
                                onClick = { confirmBlock = null },
                                modifier = Modifier.weight(1f).heightIn(min = 52.dp)
                            ) { Text(text = "Non", fontSize = 16.sp) }
                        }
                    }
                }
            }
            for ((key, defaultName) in people) {
                val shown = ReoFenuaContacts.nameFor(key, defaultName)
                val isBlocked = ReoFenuaBlock.isBlocked(key)
                Surface(color = MaterialTheme.colorScheme.surface, shape = MaterialTheme.shapes.large) {
                    Column(modifier = Modifier.fillMaxWidth().padding(14.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            ReoFenuaAvatar(key = key, name = shown, size = 56.dp)
                            Column(modifier = Modifier.weight(1f).padding(start = 14.dp)) {
                                Text(text = shown, fontSize = 19.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onSurface)
                                if (shown != defaultName) {
                                    Text(text = "Pseudo : $defaultName", fontSize = 14.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
                                }
                                if (isBlocked) {
                                    Text(text = "Bloquée", fontSize = 14.sp, fontWeight = FontWeight.Bold, color = ERouge)
                                }
                            }
                        }
                        if (editing == key) {
                            OutlinedTextField(
                                value = editText,
                                onValueChange = { editText = it.take(40) },
                                label = { Text("Nom (par exemple : Mama, Teva…)") },
                                singleLine = true,
                                modifier = Modifier.fillMaxWidth()
                            )
                            Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                                Button(
                                    onClick = {
                                        ReoFenuaContacts.rename(context, key, editText)
                                        editing = null
                                    },
                                    modifier = Modifier.weight(1f).heightIn(min = 48.dp)
                                ) { Text(text = "Enregistrer", fontSize = 16.sp) }
                                OutlinedButton(
                                    onClick = { editing = null },
                                    modifier = Modifier.weight(1f).heightIn(min = 48.dp)
                                ) { Text(text = "Annuler", fontSize = 16.sp) }
                            }
                        } else {
                            Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                                OutlinedButton(
                                    onClick = {
                                        editing = key
                                        editText = shown
                                    },
                                    modifier = Modifier.weight(1f).heightIn(min = 48.dp)
                                ) { Text(text = "Changer le nom", fontSize = 15.sp) }
                                OutlinedButton(
                                    onClick = {
                                        pickingFor = key
                                        picker.launch("image/*")
                                    },
                                    modifier = Modifier.weight(1f).heightIn(min = 48.dp)
                                ) { Text(text = "Choisir une photo", fontSize = 15.sp) }
                            }
                            if (isBlocked) {
                                OutlinedButton(
                                    onClick = {
                                        ReoFenuaBlock.unblock(context, viewModel, key, defaultName)
                                        blockInfo = "Personne débloquée."
                                    },
                                    modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)
                                ) { Text(text = "Débloquer", fontSize = 15.sp) }
                            } else {
                                TextButton(
                                    onClick = { confirmBlock = Pair(key, defaultName) },
                                    modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)
                                ) { Text(text = "Bloquer cette personne", fontSize = 15.sp, color = ERouge) }
                            }
                        }
                    }
                }
            }
            Spacer(modifier = Modifier.height(24.dp))
        }
    }
}

// ===================== Carte « Facilité » dans l'écran d'information =====================

@Composable
fun ReoFenuaEasyCard() {
    val context = LocalContext.current
    LaunchedEffect(Unit) { ReoFenuaTextSize.load(context) }
    val current = ReoFenuaTextSize.scale.value

    Surface(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp, vertical = 12.dp),
        color = MaterialTheme.colorScheme.surface,
        shape = MaterialTheme.shapes.large
    ) {
        Column(modifier = Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
            Text(text = "Taille du texte", fontSize = 20.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
            Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                for (i in ReoFenuaTextSize.names.indices) {
                    val v = ReoFenuaTextSize.values[i]
                    val selected = kotlin.math.abs(current - v) < 0.01f
                    if (selected) {
                        Button(
                            onClick = { ReoFenuaTextSize.save(context, v) },
                            modifier = Modifier.weight(1f).heightIn(min = 52.dp)
                        ) { Text(text = ReoFenuaTextSize.names[i], fontSize = 15.sp) }
                    } else {
                        OutlinedButton(
                            onClick = { ReoFenuaTextSize.save(context, v) },
                            modifier = Modifier.weight(1f).heightIn(min = 52.dp)
                        ) { Text(text = ReoFenuaTextSize.names[i], fontSize = 15.sp) }
                    }
                }
            }
            Spacer(modifier = Modifier.height(4.dp))
            Text(text = "Mes proches et le réseau", fontSize = 20.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
            Button(
                onClick = { ReoFenuaContacts.show.value = true },
                modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
            ) { Text(text = "Mes proches (nom et photo)", fontSize = 17.sp) }
            OutlinedButton(
                onClick = { ReoFenuaNetwork.showMap.value = true },
                modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
            ) { Text(text = "Carte du réseau", fontSize = 17.sp) }
            OutlinedButton(
                onClick = { ReoFenuaNetwork.showRelay.value = true },
                modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
            ) { Text(text = "Mode relais (vieux téléphone fixe)", fontSize = 17.sp) }
        }
    }
}

// ===================== Mode simple / mode complet =====================

object ReoFenuaMode {
    private const val PREFS = "reo_fenua_guide"
    private const val KEY = "simple_mode"
    val simple = mutableStateOf(false)
    val needsChoice = mutableStateOf(false)
    private var loaded = false

    fun load(context: Context) {
        if (loaded) return
        loaded = true
        val prefs = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
        needsChoice.value = !prefs.contains(KEY)
        simple.value = prefs.getBoolean(KEY, false)
    }

    fun set(context: Context, isSimple: Boolean) {
        simple.value = isSimple
        needsChoice.value = false
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putBoolean(KEY, isSimple).apply()
        // En mode simple, on met le texte en grand (si la personne ne l'a pas déjà agrandi)
        ReoFenuaTextSize.load(context)
        if (isSimple && ReoFenuaTextSize.scale.value < 1.1f) ReoFenuaTextSize.save(context, 1.15f)
    }
}

/** Écran de choix affiché une fois, après l'introduction. */
@Composable
fun ReoFenuaModeChooser() {
    val context = LocalContext.current
    LaunchedEffect(Unit) { ReoFenuaMode.load(context) }
    if (!ReoFenuaMode.needsChoice.value || ReoFenuaGuide.showIntro.value || ReoFenuaName.needsAsk.value || ReoFenuaCharter.needs.value) return

    Dialog(
        onDismissRequest = { },
        properties = DialogProperties(usePlatformDefaultWidth = false, dismissOnClickOutside = false)
    ) {
        Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .verticalScroll(rememberScrollState())
            ) {
                NihoManoBand(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(top = reoHeaderTop())
                        .height(14.dp)
                )
                Column(modifier = Modifier.padding(20.dp), verticalArrangement = Arrangement.spacedBy(16.dp)) {
                    Text(text = "Comment voulez-vous utiliser Reo Fenua ?", fontSize = 26.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
                    Text(text = "Vous pourrez changer plus tard dans « Plus », en bas de l'écran.", fontSize = 16.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
                    ModeChoice(
                        title = "Mode simple",
                        body = "Messages, photos, vocaux, Mes proches, lettres et le bouton ALERTE. Grand texte, peu de réglages.",
                        color = EVert,
                        onClick = { ReoFenuaMode.set(context, true) }
                    )
                    ModeChoice(
                        title = "Mode complet",
                        body = "Tout le mode simple, plus la carte du réseau, le mode relais, le fond d'écran et les réglages avancés.",
                        color = ELagon,
                        onClick = { ReoFenuaMode.set(context, false) }
                    )
                    ModeChoice(
                        title = "Mode stylisé",
                        body = "Tout le mode complet, avec les couleurs de la nuit polynésienne (Pō) et des avatars dessinés. Vous pourrez choisir Mahana ou Tīfaifai dans « Plus ».",
                        color = Color(0xFF071A2B),
                        onClick = {
                            ReoFenuaMode.set(context, false)
                            ReoFenuaStyle.set(context, ReoTheme.PO)
                        }
                    )
                }
            }
        }
    }
}

@Composable
private fun ModeChoice(title: String, body: String, color: Color, onClick: () -> Unit) {
    Button(
        onClick = onClick,
        colors = ButtonDefaults.buttonColors(containerColor = color, contentColor = Color.White),
        shape = MaterialTheme.shapes.extraLarge,
        modifier = Modifier
            .fillMaxWidth()
            .heightIn(min = 120.dp)
    ) {
        Column(modifier = Modifier.fillMaxWidth().padding(8.dp), verticalArrangement = Arrangement.spacedBy(6.dp)) {
            Text(text = title, fontSize = 24.sp, fontWeight = FontWeight.Bold)
            Text(text = body, fontSize = 16.sp)
        }
    }
}

/** Carte en haut de l'écran d'information : changer de mode à tout moment. */
@Composable
fun ReoFenuaModeCard() {
    val context = LocalContext.current
    LaunchedEffect(Unit) { ReoFenuaMode.load(context) }
    val isSimple = ReoFenuaMode.simple.value
    Surface(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp, vertical = 12.dp),
        color = MaterialTheme.colorScheme.surface,
        shape = MaterialTheme.shapes.large
    ) {
        Column(modifier = Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
            Text(
                text = if (isSimple) "Vous êtes en mode simple" else "Vous êtes en mode complet",
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold,
                color = MaterialTheme.colorScheme.primary
            )
            Text(
                text = if (isSimple) "Messages, Mes proches, lettres et Alerte. Les réglages avancés sont cachés."
                else "Toutes les fonctions sont visibles.",
                fontSize = 15.sp,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
            OutlinedButton(
                onClick = { ReoFenuaMode.set(context, !isSimple) },
                modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
            ) {
                Text(text = if (isSimple) "Passer en mode complet" else "Passer en mode simple", fontSize = 17.sp)
            }
        }
    }
}
'''
NETWORK_KT = r'''package com.bitchat.android.ui

import android.content.Context
import android.content.Intent
import android.os.BatteryManager
import android.provider.Settings
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.PathEffect
import androidx.compose.ui.graphics.StrokeCap
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.drawText
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.rememberTextMeasurer
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import kotlinx.coroutines.delay

private val NOcean = Color(0xFF0B3C5D)
private val NLagon = Color(0xFF0E7C86)
private val NLagonClair = Color(0xFF4FC3CC)
private val NVanille = Color(0xFFE8B33A)
private val NNuit = Color(0xFF071E2E)

object ReoFenuaNetwork {
    val showRelay = mutableStateOf(false)
    val showMap = mutableStateOf(false)

    fun batteryLevel(context: Context): Int {
        val bm = context.getSystemService(Context.BATTERY_SERVICE) as? BatteryManager ?: return -1
        return bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
    }

    fun isCharging(context: Context): Boolean {
        val bm = context.getSystemService(Context.BATTERY_SERVICE) as? BatteryManager ?: return false
        return bm.isCharging
    }
}

/** Hôte du mode relais et de la carte du réseau. Toujours présent sur l'écran principal. */
@Composable
fun ReoFenuaNetworkHost(viewModel: ChatViewModel) {
    if (ReoFenuaNetwork.showRelay.value) {
        Dialog(
            onDismissRequest = { ReoFenuaNetwork.showRelay.value = false },
            properties = DialogProperties(usePlatformDefaultWidth = false)
        ) {
            Surface(modifier = Modifier.fillMaxSize(), color = NNuit) {
                RelayScreen(viewModel = viewModel, onClose = { ReoFenuaNetwork.showRelay.value = false })
            }
        }
    }
    if (ReoFenuaNetwork.showMap.value) {
        Dialog(
            onDismissRequest = { ReoFenuaNetwork.showMap.value = false },
            properties = DialogProperties(usePlatformDefaultWidth = false)
        ) {
            Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
                MapScreen(viewModel = viewModel, onClose = { ReoFenuaNetwork.showMap.value = false })
            }
        }
    }
}

@Composable
private fun RelayScreen(viewModel: ChatViewModel, onClose: () -> Unit) {
    val context = LocalContext.current
    val connected by viewModel.connectedPeers.collectAsState()
    var battery by remember { mutableIntStateOf(-1) }
    var charging by remember { mutableStateOf(false) }
    var direct by remember { mutableIntStateOf(0) }

    // Le relais continue même écran éteint grâce au service en arrière-plan
    LaunchedEffect(Unit) {
        try {
            com.bitchat.android.service.MeshServicePreferences.setBackgroundEnabled(true)
            com.bitchat.android.service.MeshForegroundService.start(context)
        } catch (e: Exception) {
            // le service démarrera avec l'application
        }
    }
    LaunchedEffect(connected) {
        while (true) {
            battery = ReoFenuaNetwork.batteryLevel(context)
            charging = ReoFenuaNetwork.isCharging(context)
            direct = connected.count { viewModel.getMeshPeerInfo(it)?.isDirectConnection == true }
            delay(10_000L)
        }
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
            .padding(24.dp),
        verticalArrangement = Arrangement.spacedBy(18.dp)
    ) {
        Spacer(modifier = Modifier.height(24.dp))
        NihoManoBand(
            modifier = Modifier
                .fillMaxWidth()
                .height(12.dp),
            color = NLagon,
            accent = NVanille
        )
        Text(text = "Relais actif", fontSize = 36.sp, fontWeight = FontWeight.Bold, color = NLagonClair)
        Text(
            text = "Ce téléphone fait passer les messages de tout le monde autour.",
            fontSize = 19.sp,
            lineHeight = 27.sp,
            color = Color(0xFFF3ECE0)
        )
        Surface(color = Color(0xFF0B2A3E), shape = MaterialTheme.shapes.large) {
            Column(modifier = Modifier.fillMaxWidth().padding(18.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                Text(
                    text = connected.size.toString() + if (connected.size > 1) " téléphones reliés" else " téléphone relié",
                    fontSize = 26.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.White
                )
                Text(text = "dont $direct en direct", fontSize = 17.sp, color = Color(0xFFA9BFCC))
                val batteryText = when {
                    battery < 0 -> "Batterie : inconnue"
                    charging -> "Batterie : $battery % · en charge ✓"
                    else -> "Batterie : $battery % · pas en charge"
                }
                Text(
                    text = batteryText,
                    fontSize = 17.sp,
                    color = if (!charging && battery in 0..30) NVanille else Color(0xFFA9BFCC)
                )
            }
        }
        Text(text = "Pour un bon relais :", fontSize = 18.sp, fontWeight = FontWeight.Bold, color = Color.White)
        Text(
            text = "• Branchez-le sur un chargeur ou un petit panneau solaire.\n" +
                "• Placez-le en hauteur, près d'une fenêtre, vers la vallée ou la route.\n" +
                "• Vous pouvez éteindre l'écran : le relais continue.\n" +
                "• Laissez le Bluetooth allumé.",
            fontSize = 17.sp,
            lineHeight = 26.sp,
            color = Color(0xFFF3ECE0)
        )
        OutlinedButton(
            onClick = {
                try {
                    val intent = Intent(Settings.ACTION_IGNORE_BATTERY_OPTIMIZATION_SETTINGS)
                    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                    context.startActivity(intent)
                } catch (e: Exception) {
                    // réglage indisponible sur ce téléphone
                }
            },
            modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp)
        ) {
            Text(text = "Empêcher la batterie de couper le relais", fontSize = 16.sp, color = NLagonClair)
        }
        Button(
            onClick = onClose,
            modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp)
        ) {
            Text(text = "Quitter cet écran (le relais reste actif)", fontSize = 16.sp)
        }
        Spacer(modifier = Modifier.height(24.dp))
    }
}

@Composable
private fun MapScreen(viewModel: ChatViewModel, onClose: () -> Unit) {
    val context = LocalContext.current
    val connected by viewModel.connectedPeers.collectAsState()
    val nicknames by viewModel.peerNicknames.collectAsState()
    var tick by remember { mutableIntStateOf(0) }
    LaunchedEffect(Unit) {
        while (true) {
            delay(5_000L)
            tick += 1
        }
    }
    val directIds = remember(connected, tick) {
        connected.filter { viewModel.getMeshPeerInfo(it)?.isDirectConnection == true }
    }
    val relayedIds = remember(connected, tick) { connected.filter { it !in directIds } }
    fun nameOf(id: String): String = ReoFenuaContacts.nameFor(id, nicknames[id] ?: "?").take(12)

    val measurer = rememberTextMeasurer()
    val labelStyle = TextStyle(fontSize = 13.sp, fontWeight = FontWeight.SemiBold, color = NOcean)
    val meStyle = TextStyle(fontSize = 15.sp, fontWeight = FontWeight.Bold, color = NOcean)

    Column(modifier = Modifier.fillMaxSize()) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .background(NLagon)
                .padding(start = 20.dp, end = 8.dp, top = reoHeaderTop(), bottom = 14.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            Column(modifier = Modifier.weight(1f)) {
                Text(text = "Carte du réseau", fontSize = 24.sp, fontWeight = FontWeight.Bold, color = Color.White)
                Text(text = "Les téléphones Reo Fenua autour de vous", fontSize = 14.sp, color = Color.White)
            }
            TextButton(onClick = onClose) {
                Text(text = "← Retour", fontSize = 17.sp, color = Color.White)
            }
        }
        NihoManoBand(
            modifier = Modifier
                .fillMaxWidth()
                .height(12.dp)
        )
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(360.dp)
                .background(Color(0xFFD7ECEE))
        ) {
            Canvas(modifier = Modifier.fillMaxSize()) {
                val c = Offset(size.width / 2f, size.height / 2f)
                val r1 = size.minDimension * 0.27f
                val r2 = size.minDimension * 0.44f
                drawCircle(color = NLagonClair.copy(alpha = 0.18f), radius = r2, center = c)
                drawCircle(color = NLagonClair.copy(alpha = 0.25f), radius = r1, center = c)
                fun ring(ids: List<String>, r: Float, start: Float, dot: Color, link: Boolean) {
                    val n = ids.size
                    for (i in 0 until n) {
                        val a = start + (2.0 * Math.PI * i / n).toFloat()
                        val p = Offset(c.x + r * kotlin.math.cos(a), c.y + r * kotlin.math.sin(a))
                        if (link) {
                            drawLine(
                                color = NVanille,
                                start = c,
                                end = p,
                                strokeWidth = 5f,
                                cap = StrokeCap.Round,
                                pathEffect = PathEffect.dashPathEffect(floatArrayOf(14f, 14f), 0f)
                            )
                        }
                        drawCircle(color = Color.White, radius = 22f, center = p)
                        drawCircle(color = dot, radius = 15f, center = p)
                        val t = measurer.measure(nameOf(ids[i]), labelStyle)
                        drawText(t, topLeft = Offset(p.x - t.size.width / 2f, p.y + 26f))
                    }
                }
                ring(directIds, r1, -1.2f, NLagon, true)
                ring(relayedIds, r2, -0.6f, NLagonClair, false)
                drawCircle(color = NVanille, radius = 34f, center = c)
                drawCircle(color = NOcean, radius = 34f, center = c, style = Stroke(width = 4f))
                val me = measurer.measure("Vous", meStyle)
                drawText(me, topLeft = Offset(c.x - me.size.width / 2f, c.y - me.size.height / 2f))
            }
        }
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .verticalScroll(rememberScrollState())
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(10.dp)
        ) {
            if (connected.isEmpty()) {
                Text(
                    text = "Personne autour pour le moment. Rapprochez-vous d'autres téléphones avec Reo Fenua, ou installez un relais.",
                    fontSize = 17.sp,
                    color = MaterialTheme.colorScheme.onBackground
                )
            } else {
                Text(
                    text = connected.size.toString() + " téléphone" + (if (connected.size > 1) "s" else "") + " autour de vous",
                    fontSize = 20.sp,
                    fontWeight = FontWeight.Bold,
                    color = MaterialTheme.colorScheme.primary
                )
            }
            Row(verticalAlignment = Alignment.CenterVertically) {
                Box(modifier = Modifier.size(18.dp).background(NLagon, CircleShape))
                Text(
                    text = "  En direct (" + directIds.size + ") : tout près de vous, par Bluetooth ou Wi-Fi",
                    fontSize = 15.sp,
                    color = MaterialTheme.colorScheme.onBackground
                )
            }
            Row(verticalAlignment = Alignment.CenterVertically) {
                Box(modifier = Modifier.size(18.dp).background(NLagonClair, CircleShape))
                Text(
                    text = "  Par relais (" + relayedIds.size + ") : plus loin, joints grâce à d'autres téléphones",
                    fontSize = 15.sp,
                    color = MaterialTheme.colorScheme.onBackground
                )
            }
            Text(
                text = "Astuce : un vieux téléphone en « Mode relais », branché en hauteur, agrandit beaucoup le réseau.",
                fontSize = 15.sp,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
            OutlinedButton(
                onClick = {
                    ReoFenuaNetwork.showMap.value = false
                    ReoFenuaNetwork.showRelay.value = true
                },
                modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
            ) {
                Text(text = "Passer ce téléphone en mode relais", fontSize = 16.sp)
            }
            ReoFenuaExtendCard(peopleAround = connected.size)
        }
    }
}
'''
NAV_KT = r'''package com.bitchat.android.ui

import android.content.Context
import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.ime
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.StrokeCap
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import com.bitchat.android.geohash.ChannelID
import com.bitchat.android.geohash.GeohashChannel
import com.bitchat.android.geohash.GeohashChannelLevel
import com.bitchat.android.geohash.LocationChannelManager

private val VOcean = Color(0xFF0B3C5D)
private val VLagon = Color(0xFF0E7C86)
private val VLagonClair = Color(0xFF4FC3CC)
private val VVanille = Color(0xFFE8B33A)
private val VRouge = Color(0xFFC8102E)
private val VSable = Color(0xFFF7EFE2)

/** Écrans ouverts depuis la barre du bas. */
object ReoFenuaNav {
    val showRadar = mutableStateOf(false)
    val showProches = mutableStateOf(false)
    val showPlus = mutableStateOf(false)
}

// ===================== En-tête commun : « ← Retour » à gauche =====================

@Composable
fun ReoFenuaScreenHeader(title: String, subtitle: String, color: Color, onBack: () -> Unit) {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .background(color)
            .padding(start = 8.dp, end = 20.dp, top = reoHeaderTop(), bottom = 14.dp)
    ) {
        TextButton(onClick = onBack, modifier = Modifier.heightIn(min = 48.dp)) {
            Text(text = "← Retour", fontSize = 17.sp, color = Color.White)
        }
        Text(
            text = title,
            fontSize = 26.sp,
            fontWeight = FontWeight.Bold,
            color = Color.White,
            modifier = Modifier.padding(start = 12.dp)
        )
        if (subtitle.isNotEmpty()) {
            Text(text = subtitle, fontSize = 15.sp, color = Color.White, modifier = Modifier.padding(start = 12.dp))
        }
    }
    NihoManoBand(
        modifier = Modifier
            .fillMaxWidth()
            .height(12.dp)
    )
}

@Composable
private fun FullScreen(onDismiss: () -> Unit, content: @Composable () -> Unit) {
    Dialog(
        onDismissRequest = onDismiss,
        properties = DialogProperties(usePlatformDefaultWidth = false)
    ) {
        Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
            content()
        }
    }
}

// ===================== Barre du bas =====================

private enum class NavIcon { Radar, Proches, Alerte, Aide, Plus }

@Composable
private fun NavItem(label: String, icon: NavIcon, onClick: () -> Unit, modifier: Modifier = Modifier, badge: Int = 0) {
    val isAlert = icon == NavIcon.Alerte
    Column(
        modifier = modifier
            .heightIn(min = 64.dp)
            .clickable { onClick() }
            .semantics { contentDescription = label }
            .padding(vertical = 6.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Box(contentAlignment = Alignment.Center) {
            if (isAlert) {
                Box(
                    modifier = Modifier
                        .size(52.dp)
                        .background(VRouge, CircleShape),
                    contentAlignment = Alignment.Center
                ) {
                    Text(text = "!", fontSize = 28.sp, fontWeight = FontWeight.Bold, color = Color.White)
                }
            } else {
                val tint = MaterialTheme.colorScheme.primary
                Canvas(modifier = Modifier.size(30.dp)) {
                    val s = size.width
                    val c = Offset(s / 2f, s / 2f)
                    val line = s * 0.09f
                    when (icon) {
                        NavIcon.Radar -> {
                            drawCircle(color = tint, radius = s * 0.10f, center = c)
                            drawCircle(color = tint, radius = s * 0.27f, center = c, style = Stroke(width = line))
                            drawCircle(color = tint, radius = s * 0.45f, center = c, style = Stroke(width = line))
                            drawLine(color = tint, start = c, end = Offset(s * 0.86f, s * 0.2f), strokeWidth = line, cap = StrokeCap.Round)
                        }
                        NavIcon.Proches -> {
                            drawCircle(color = tint, radius = s * 0.14f, center = Offset(s * 0.34f, s * 0.32f))
                            drawCircle(color = tint, radius = s * 0.14f, center = Offset(s * 0.68f, s * 0.32f))
                            drawCircle(color = tint, radius = s * 0.24f, center = Offset(s * 0.34f, s * 0.86f), style = Stroke(width = line))
                            drawCircle(color = tint, radius = s * 0.24f, center = Offset(s * 0.68f, s * 0.86f), style = Stroke(width = line))
                        }
                        NavIcon.Aide -> {
                            drawCircle(color = tint, radius = s * 0.45f, center = c, style = Stroke(width = line))
                        }
                        else -> {
                            drawCircle(color = tint, radius = s * 0.09f, center = Offset(s * 0.2f, s / 2f))
                            drawCircle(color = tint, radius = s * 0.09f, center = c)
                            drawCircle(color = tint, radius = s * 0.09f, center = Offset(s * 0.8f, s / 2f))
                        }
                    }
                }
                if (icon == NavIcon.Aide) {
                    Text(text = "?", fontSize = 17.sp, fontWeight = FontWeight.Bold, color = tint)
                }
            }
            if (badge > 0) {
                Box(
                    modifier = Modifier
                        .align(Alignment.TopEnd)
                        .size(18.dp)
                        .background(VRouge, CircleShape),
                    contentAlignment = Alignment.Center
                ) {
                    Text(text = if (badge > 9) "9+" else badge.toString(), fontSize = 10.sp, fontWeight = FontWeight.Bold, color = Color.White)
                }
            }
        }
        Text(
            text = label,
            fontSize = 13.sp,
            fontWeight = if (isAlert) FontWeight.Bold else FontWeight.SemiBold,
            color = if (isAlert) VRouge else MaterialTheme.colorScheme.onSurface,
            textAlign = TextAlign.Center,
            maxLines = 1
        )
    }
}

/** Barre du bas : Radar · Mes proches · ALERTE · Aide · Plus. Cachée quand le clavier est ouvert. */
@Composable
fun ReoFenuaBottomBar(viewModel: ChatViewModel) {
    val imeVisible = WindowInsets.ime.getBottom(LocalDensity.current) > 0
    if (imeVisible) return
    Column(modifier = Modifier.fillMaxWidth()) {
        HorizontalDivider(color = MaterialTheme.colorScheme.outlineVariant)
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .background(MaterialTheme.colorScheme.surface)
                .padding(horizontal = 4.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            NavItem("Radar", NavIcon.Radar, { ReoFenuaNav.showRadar.value = true }, Modifier.weight(1f))
            NavItem(
                "Proches",
                NavIcon.Proches,
                { ReoFenuaNav.showProches.value = true },
                Modifier.weight(1f),
                badge = ReoFenuaLetters.unreadCount()
            )
            NavItem("ALERTE", NavIcon.Alerte, { ReoFenuaAlert.show.value = true }, Modifier.weight(1.2f))
            NavItem("Aide", NavIcon.Aide, { ReoFenuaSteps.show.value = true }, Modifier.weight(1f))
            NavItem("Plus", NavIcon.Plus, { ReoFenuaNav.showPlus.value = true }, Modifier.weight(1f), badge = if (ReoFenuaUpdate.available.value != null) 1 else 0)
        }
    }
}

/** Hôte des écrans de la barre du bas. Toujours présent sur l'écran principal. */
@Composable
fun ReoFenuaNavHost(viewModel: ChatViewModel) {
    if (ReoFenuaNav.showRadar.value) {
        FullScreen(onDismiss = { ReoFenuaNav.showRadar.value = false }) {
            RadarScreen(viewModel = viewModel, onClose = { ReoFenuaNav.showRadar.value = false })
        }
    }
    if (ReoFenuaNav.showProches.value) {
        FullScreen(onDismiss = { ReoFenuaNav.showProches.value = false }) {
            ProchesScreen(viewModel = viewModel, onClose = { ReoFenuaNav.showProches.value = false })
        }
    }
    if (ReoFenuaNav.showPlus.value) {
        FullScreen(onDismiss = { ReoFenuaNav.showPlus.value = false }) {
            PlusScreen(viewModel = viewModel, onClose = { ReoFenuaNav.showPlus.value = false })
        }
    }
}

// ===================== Radar : autour de moi, quartier, commune, île =====================

private object RadarPrefs {
    private const val PREFS = "reo_fenua_guide"
    private const val KEY = "radar_warned"
    fun warned(context: Context): Boolean =
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getBoolean(KEY, false)
    fun setWarned(context: Context) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putBoolean(KEY, true).apply()
    }
}

private fun levelLabel(level: GeohashChannelLevel): String = when (level) {
    GeohashChannelLevel.NEIGHBORHOOD -> "Mon quartier"
    GeohashChannelLevel.CITY -> "Ma commune"
    GeohashChannelLevel.PROVINCE -> "Mon île"
    else -> "Ma région"
}

private fun levelSize(level: GeohashChannelLevel): String = when (level) {
    GeohashChannelLevel.NEIGHBORHOOD -> "environ 1 km"
    GeohashChannelLevel.CITY -> "environ 5 km"
    GeohashChannelLevel.PROVINCE -> "environ 40 km"
    else -> "très large"
}

private fun levelForCode(length: Int): GeohashChannelLevel = when {
    length <= 2 -> GeohashChannelLevel.REGION
    length <= 4 -> GeohashChannelLevel.PROVINCE
    length == 5 -> GeohashChannelLevel.CITY
    else -> GeohashChannelLevel.NEIGHBORHOOD
}

@Composable
private fun RadarDrawing() {
    Canvas(
        modifier = Modifier
            .fillMaxWidth()
            .height(180.dp)
            .background(Color(0xFFD7ECEE))
    ) {
        val c = Offset(size.width / 2f, size.height / 2f)
        val m = size.minDimension
        drawCircle(color = VLagonClair.copy(alpha = 0.18f), radius = m * 0.48f, center = c)
        drawCircle(color = VLagonClair.copy(alpha = 0.26f), radius = m * 0.36f, center = c)
        drawCircle(color = VLagonClair.copy(alpha = 0.36f), radius = m * 0.24f, center = c)
        drawCircle(color = VLagon.copy(alpha = 0.55f), radius = m * 0.12f, center = c)
        drawLine(
            color = VOcean,
            start = c,
            end = Offset(c.x + m * 0.36f, c.y - m * 0.32f),
            strokeWidth = 6f,
            cap = StrokeCap.Round
        )
        drawCircle(color = VVanille, radius = m * 0.05f, center = c)
    }
}

@Composable
private fun RadarChoice(
    title: String,
    body: String,
    selected: Boolean,
    enabled: Boolean,
    onClick: () -> Unit
) {
    Surface(
        color = if (selected) Color(0xFFD7ECEE) else MaterialTheme.colorScheme.surface,
        shape = MaterialTheme.shapes.large,
        modifier = Modifier
            .fillMaxWidth()
            .clickable(enabled = enabled) { onClick() }
    ) {
        Column(modifier = Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(4.dp)) {
            Text(
                text = (if (selected) "✓  " else "") + title,
                fontSize = 19.sp,
                fontWeight = FontWeight.Bold,
                color = if (enabled) VOcean else MaterialTheme.colorScheme.onSurfaceVariant
            )
            Text(text = body, fontSize = 15.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
        }
    }
}

@Composable
private fun RadarScreen(viewModel: ChatViewModel, onClose: () -> Unit) {
    val context = LocalContext.current
    val manager = remember { LocationChannelManager.getInstance(context) }
    val permission by manager.permissionState.collectAsState()
    val available by manager.availableChannels.collectAsState()
    val names by manager.locationNames.collectAsState()
    val selected by manager.selectedChannel.collectAsState()
    val locationOn by manager.effectiveLocationEnabled.collectAsState()
    var askFor by remember { mutableStateOf<GeohashChannel?>(null) }
    var code by remember { mutableStateOf("") }
    var info by remember { mutableStateOf("") }

    DisposableEffect(Unit) {
        manager.refreshChannels()
        manager.beginLiveRefresh()
        onDispose { manager.endLiveRefresh() }
    }

    fun join(channel: GeohashChannel) {
        if (manager.selectNearby(channel)) {
            onClose()
        } else {
            info = "Impossible pour le moment : la localisation n'est pas prête. Réessayez dans quelques secondes."
        }
    }

    val zones = available
        .filter {
            it.level == GeohashChannelLevel.NEIGHBORHOOD ||
                it.level == GeohashChannelLevel.CITY ||
                it.level == GeohashChannelLevel.PROVINCE
        }
        .sortedByDescending { it.level.precision }

    Column(modifier = Modifier.fillMaxSize()) {
        ReoFenuaScreenHeader(
            title = "Radar",
            subtitle = "Choisissez jusqu'où vous voulez parler",
            color = VLagon,
            onBack = onClose
        )
        Column(
            modifier = Modifier
                .weight(1f)
                .fillMaxWidth()
                .verticalScroll(rememberScrollState())
        ) {
            RadarDrawing()
            Column(modifier = Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
                val ask = askFor
                if (ask != null) {
                    Surface(color = Color(0xFFFFF4DC), shape = MaterialTheme.shapes.large) {
                        Column(modifier = Modifier.fillMaxWidth().padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                            Text(text = "Avant de continuer", fontSize = 19.sp, fontWeight = FontWeight.Bold, color = VOcean)
                            Text(
                                text = "Les personnes de « " + levelLabel(ask.level) + " » sauront que vous êtes quelque part dans cette zone (" +
                                    levelSize(ask.level) + "). Votre adresse exacte n'est jamais envoyée. Ces discussions passent par internet.",
                                fontSize = 16.sp,
                                color = VOcean
                            )
                            Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                                Button(
                                    onClick = {
                                        RadarPrefs.setWarned(context)
                                        askFor = null
                                        join(ask)
                                    },
                                    modifier = Modifier.weight(1f).heightIn(min = 52.dp)
                                ) { Text(text = "D'accord", fontSize = 17.sp) }
                                OutlinedButton(
                                    onClick = { askFor = null },
                                    modifier = Modifier.weight(1f).heightIn(min = 52.dp)
                                ) { Text(text = "Non merci", fontSize = 17.sp) }
                            }
                        }
                    }
                }

                RadarChoice(
                    title = "Autour de moi",
                    body = "Bluetooth, sans internet, jusqu'à environ 30 m. Personne ne connaît votre position.",
                    selected = selected is ChannelID.Mesh,
                    enabled = true,
                    onClick = {
                        manager.select(ChannelID.Mesh)
                        onClose()
                    }
                )

                if (!locationOn || permission != LocationChannelManager.PermissionState.AUTHORIZED) {
                    Surface(color = MaterialTheme.colorScheme.surface, shape = MaterialTheme.shapes.large) {
                        Column(modifier = Modifier.fillMaxWidth().padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                            Text(
                                text = "Pour parler à votre quartier, votre commune ou votre île, il faut internet et la localisation.",
                                fontSize = 16.sp,
                                color = MaterialTheme.colorScheme.onSurface
                            )
                            Button(
                                onClick = {
                                    manager.enableLocationServices()
                                    manager.refreshChannels()
                                    if (manager.permissionState.value != LocationChannelManager.PermissionState.AUTHORIZED) {
                                        try {
                                            val intent = Intent(
                                                android.provider.Settings.ACTION_APPLICATION_DETAILS_SETTINGS,
                                                Uri.parse("package:" + context.packageName)
                                            )
                                            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                                            context.startActivity(intent)
                                            info = "Dans l'écran qui s'ouvre : Autorisations, puis Position. Revenez ensuite ici."
                                        } catch (e: Exception) {
                                            info = "Autorisez la position pour Reo Fenua dans les réglages du téléphone."
                                        }
                                    }
                                },
                                modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
                            ) { Text(text = "Allumer la localisation", fontSize = 17.sp) }
                        }
                    }
                } else if (zones.isEmpty()) {
                    Text(text = "Recherche de votre zone…", fontSize = 16.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
                } else {
                    for (zone in zones) {
                        val place = names[zone.level]
                        RadarChoice(
                            title = levelLabel(zone.level) + (if (!place.isNullOrBlank()) " : $place" else ""),
                            body = "Avec internet, " + levelSize(zone.level) + ". Les autres savent seulement que vous êtes dans cette zone.",
                            selected = selected == ChannelID.Location(zone),
                            enabled = true,
                            onClick = {
                                if (RadarPrefs.warned(context)) join(zone) else askFor = zone
                            }
                        )
                    }
                    OutlinedButton(
                        onClick = {
                            manager.disableLocationServices()
                            manager.select(ChannelID.Mesh)
                            info = "Localisation coupée. Vous êtes revenu dans « Autour de moi »."
                        },
                        modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
                    ) { Text(text = "Couper la localisation", fontSize = 16.sp) }
                }

                if (info.isNotEmpty()) {
                    Text(text = info, fontSize = 15.sp, fontWeight = FontWeight.SemiBold, color = VLagon)
                }

                Spacer(modifier = Modifier.height(4.dp))
                Text(text = "Voir un lieu sans partager ma position", fontSize = 18.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
                Text(
                    text = "Tapez le code d'un lieu (par exemple donné par un proche). Vous lisez et écrivez dans ce lieu sans que votre position soit utilisée.",
                    fontSize = 15.sp,
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
                OutlinedTextField(
                    value = code,
                    onValueChange = { value ->
                        val allowed = "0123456789bcdefghjkmnpqrstuvwxyz"
                        code = value.lowercase().filter { allowed.indexOf(it) >= 0 }.take(6)
                    },
                    label = { Text("Code du lieu (2 à 6 lettres)") },
                    singleLine = true,
                    modifier = Modifier.fillMaxWidth()
                )
                OutlinedButton(
                    onClick = {
                        manager.selectManual(GeohashChannel(levelForCode(code.length), code), true)
                        onClose()
                    },
                    enabled = code.length >= 2,
                    modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
                ) { Text(text = "Visiter ce lieu", fontSize = 16.sp) }
                Spacer(modifier = Modifier.height(24.dp))
            }
        }
    }
}

/** Petit bandeau sur l'écran principal quand la position est partagée avec un lieu. */
@Composable
fun ReoFenuaLocationBanner(viewModel: ChatViewModel, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val manager = remember { LocationChannelManager.getInstance(context) }
    val selected by manager.selectedChannel.collectAsState()
    val teleported by manager.teleported.collectAsState()
    val loc = selected as? ChannelID.Location ?: return
    val label = if (teleported) "Lieu visité (position non partagée)" else "Position partagée : " + levelLabel(loc.channel.level).lowercase()
    Surface(color = if (teleported) VLagon else VOcean, shape = MaterialTheme.shapes.extraLarge, modifier = modifier) {
        Row(modifier = Modifier.padding(start = 14.dp, end = 4.dp), verticalAlignment = Alignment.CenterVertically) {
            Text(text = label, fontSize = 14.sp, fontWeight = FontWeight.SemiBold, color = Color.White)
            TextButton(onClick = { manager.select(ChannelID.Mesh) }, modifier = Modifier.heightIn(min = 48.dp)) {
                Text(text = "Arrêter", fontSize = 14.sp, fontWeight = FontWeight.Bold, color = VVanille)
            }
        }
    }
}

// ===================== Mes proches : une seule place par personne =====================

@Composable
private fun ProchesScreen(viewModel: ChatViewModel, onClose: () -> Unit) {
    val context = LocalContext.current
    LaunchedEffect(Unit) { ReoFenuaContacts.load(context) }
    val chats by viewModel.privateChats.collectAsState()
    val nicknames by viewModel.peerNicknames.collectAsState()
    val myNick by viewModel.nickname.collectAsState()
    val connected by viewModel.connectedPeers.collectAsState()
    val people = remember(chats, nicknames, myNick) {
        reoKnownPeople(chats, nicknames, viewModel.myPeerID, myNick)
    }

    Column(modifier = Modifier.fillMaxSize()) {
        ReoFenuaScreenHeader(
            title = "Mes proches",
            subtitle = "Écrivez à une personne : tout de suite si elle est là, sinon une lettre l'attend",
            color = VLagon,
            onBack = onClose
        )
        Column(
            modifier = Modifier
                .weight(1f)
                .fillMaxWidth()
                .verticalScroll(rememberScrollState())
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            Button(
                onClick = {
                    onClose()
                    ReoFenuaLetters.show.value = true
                },
                colors = ButtonDefaults.buttonColors(containerColor = VOcean, contentColor = Color.White),
                modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp)
            ) {
                val unread = ReoFenuaLetters.unreadCount()
                Text(text = "✉  Boîte aux lettres" + (if (unread > 0) " ($unread nouvelle" + (if (unread > 1) "s" else "") + ")" else ""), fontSize = 18.sp)
            }
            if (people.isEmpty()) {
                Text(
                    text = "Personne pour le moment. Les personnes que vous croisez dans « Autour de moi » apparaîtront ici.",
                    fontSize = 17.sp,
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
            }
            val sorted = people.sortedByDescending { connected.contains(it.first) }
            for ((key, defaultName) in sorted) {
                val shown = ReoFenuaContacts.nameFor(key, defaultName)
                val here = connected.contains(key)
                Surface(color = MaterialTheme.colorScheme.surface, shape = MaterialTheme.shapes.large) {
                    Column(modifier = Modifier.fillMaxWidth().padding(14.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            ReoFenuaAvatar(key = key, name = shown, size = 56.dp)
                            Column(modifier = Modifier.weight(1f).padding(start = 14.dp)) {
                                Text(text = shown, fontSize = 19.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onSurface)
                                Text(
                                    text = if (here) "Autour de vous en ce moment" else "Pas autour de vous",
                                    fontSize = 14.sp,
                                    fontWeight = FontWeight.SemiBold,
                                    color = if (here) Color(0xFF2E7D32) else MaterialTheme.colorScheme.onSurfaceVariant
                                )
                                ReoFenuaWellbeingLine(key = key, name = defaultName)
                            }
                        }
                        Button(
                            onClick = {
                                onClose()
                                if (here) {
                                    viewModel.showPrivateChatSheet(key)
                                } else {
                                    ReoFenuaLetters.writeTo.value = key
                                    ReoFenuaLetters.show.value = true
                                }
                            },
                            modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
                        ) {
                            Text(text = if (here) "Écrire à $shown" else "Laisser une lettre à $shown", fontSize = 17.sp)
                        }
                        if (!here) {
                            TextButton(
                                onClick = {
                                    onClose()
                                    viewModel.showPrivateChatSheet(key)
                                },
                                modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)
                            ) { Text(text = "Voir nos messages", fontSize = 15.sp) }
                        }
                    }
                }
            }
            OutlinedButton(
                onClick = { ReoFenuaContacts.show.value = true },
                modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
            ) { Text(text = "Noms, photos et blocage", fontSize = 16.sp) }
            Spacer(modifier = Modifier.height(24.dp))
        }
    }
}

// ===================== Plus : réglages rangés =====================

@Composable
private fun SectionTitle(text: String) {
    Text(
        text = text,
        fontSize = 20.sp,
        fontWeight = FontWeight.Bold,
        color = MaterialTheme.colorScheme.primary,
        modifier = Modifier.padding(start = 20.dp, top = 16.dp, bottom = 4.dp)
    )
}

@Composable
private fun PlusButton(text: String, onClick: () -> Unit) {
    OutlinedButton(
        onClick = onClick,
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp, vertical = 4.dp)
            .heightIn(min = 52.dp)
    ) { Text(text = text, fontSize = 17.sp) }
}

@Composable
private fun PlusScreen(viewModel: ChatViewModel, onClose: () -> Unit) {
    val context = LocalContext.current
    val simple = ReoFenuaMode.simple.value
    var confirmErase by remember { mutableStateOf(false) }
    LaunchedEffect(Unit) { ReoFenuaTextSize.load(context) }

    Column(modifier = Modifier.fillMaxSize()) {
        ReoFenuaScreenHeader(title = "Plus", subtitle = "Réglages, réseau et partage", color = VOcean, onBack = onClose)
        Column(
            modifier = Modifier
                .weight(1f)
                .fillMaxWidth()
                .verticalScroll(rememberScrollState())
        ) {
            SectionTitle(if (ReoFenuaUpdate.available.value != null) "Nouvelle version disponible" else "Mise à jour")
            ReoFenuaUpdateCard()

            SectionTitle("Réglages")
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 20.dp, vertical = 4.dp),
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                val current = ReoFenuaTextSize.scale.value
                for (i in ReoFenuaTextSize.names.indices) {
                    val v = ReoFenuaTextSize.values[i]
                    val on = kotlin.math.abs(current - v) < 0.01f
                    if (on) {
                        Button(
                            onClick = { ReoFenuaTextSize.save(context, v) },
                            modifier = Modifier.weight(1f).heightIn(min = 52.dp)
                        ) { Text(text = ReoFenuaTextSize.names[i], fontSize = 15.sp) }
                    } else {
                        OutlinedButton(
                            onClick = { ReoFenuaTextSize.save(context, v) },
                            modifier = Modifier.weight(1f).heightIn(min = 52.dp)
                        ) { Text(text = ReoFenuaTextSize.names[i], fontSize = 15.sp) }
                    }
                }
            }
            ReoFenuaSoundCard()
            ReoFenuaModeCard()
            if (!simple) ReoFenuaWallpaperCard()

            SectionTitle("Apparence")
            ReoFenuaStyleSetting()

            SectionTitle("Réseau")
            PlusButton("Radar : quartier, commune, île") {
                onClose()
                ReoFenuaNav.showRadar.value = true
            }
            if (!simple) {
                PlusButton("Carte du réseau") {
                    onClose()
                    ReoFenuaNetwork.showMap.value = true
                }
                PlusButton("Mode relais (vieux téléphone fixe)") {
                    onClose()
                    ReoFenuaNetwork.showRelay.value = true
                }
            }
            Column(modifier = Modifier.padding(horizontal = 20.dp, vertical = 4.dp)) {
                ReoFenuaExtendCard(peopleAround = viewModel.connectedPeers.value.count { it != viewModel.myPeerID })
            }

            SectionTitle("Batterie")
            ReoFenuaBatteryCard()

            SectionTitle("Sécurité")
            ReoFenuaLockSetting()
            PlusButton("Vérifier un proche (QR code)") {
                onClose()
                viewModel.showVerificationSheet()
            }
            PlusButton("Relire nos règles de vie") {
                ReoFenuaCharter.needs.value = true
            }

            SectionTitle("Partager")
            PlusButton("Partager Reo Fenua") {
                try {
                    val send = Intent(Intent.ACTION_SEND)
                    send.type = "text/plain"
                    send.putExtra(
                        Intent.EXTRA_TEXT,
                        "Reo Fenua, la messagerie qui marche même sans réseau. Installez-la ici : https://github.com/" +
                            ReoFenuaUpdate.REPO + "/releases/latest"
                    )
                    val chooser = Intent.createChooser(send, "Partager Reo Fenua")
                    chooser.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                    context.startActivity(chooser)
                } catch (e: Exception) {
                    // aucune application de partage
                }
            }

            SectionTitle("Aide")
            PlusButton("Mode d'emploi pas à pas") {
                onClose()
                ReoFenuaSteps.show.value = true
            }
            PlusButton("Revoir l'introduction") {
                onClose()
                ReoFenuaGuide.showIntro.value = true
            }

            if (!simple) {
                SectionTitle("Réglages avancés")
                PlusButton("Réglages techniques (BitChat, Tor, mises à jour)") {
                    onClose()
                    viewModel.showAppInfo()
                }
            }

            SectionTitle("Remettre en ordre")
            ReoFenuaResetSetting()

            SectionTitle("Nouvelle identité / Tout effacer")
            if (confirmErase) {
                Surface(
                    color = Color(0xFFFDE3E7),
                    shape = MaterialTheme.shapes.large,
                    modifier = Modifier.padding(horizontal = 20.dp, vertical = 4.dp)
                ) {
                    Column(modifier = Modifier.fillMaxWidth().padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                        Text(
                            text = "Tout effacer ? Vous aurez une nouvelle identité : personne ne pourra plus reconnaître ce téléphone à son ancien identifiant Bluetooth. Vos messages, vos lettres et vos fichiers seront supprimés de ce téléphone. Impossible d'annuler.",
                            fontSize = 16.sp,
                            color = VOcean
                        )
                        Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                            Button(
                                onClick = {
                                    confirmErase = false
                                    onClose()
                                    ReoFenuaVault.wipe(context)
                                    viewModel.panicClearAllData()
                                },
                                colors = ButtonDefaults.buttonColors(containerColor = VRouge, contentColor = Color.White),
                                modifier = Modifier.weight(1f).heightIn(min = 52.dp)
                            ) { Text(text = "Oui, tout effacer", fontSize = 16.sp) }
                            OutlinedButton(
                                onClick = { confirmErase = false },
                                modifier = Modifier.weight(1f).heightIn(min = 52.dp)
                            ) { Text(text = "Non", fontSize = 16.sp) }
                        }
                    }
                }
            } else {
                TextButton(
                    onClick = { confirmErase = true },
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(horizontal = 20.dp)
                        .heightIn(min = 52.dp)
                ) { Text(text = "Nouvelle identité (tout effacer)", fontSize = 16.sp, color = VRouge) }
            }
            Spacer(modifier = Modifier.height(32.dp))
        }
    }
}
'''
EMOJI_KT = r'''package com.bitchat.android.ui

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.InlineTextContent
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.text.Placeholder
import androidx.compose.ui.text.PlaceholderVerticalAlign
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.TextRange
import androidx.compose.ui.text.appendInlineContent
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.OffsetMapping
import androidx.compose.ui.text.input.TextFieldValue
import androidx.compose.ui.text.input.TransformedText
import androidx.compose.ui.text.input.VisualTransformation
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.em
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import com.bitchat.android.R

/**
 * Emoji Reo Fenua.
 * Sur le réseau, un emoji voyage comme un petit texte : l'emoji standard le plus proche,
 * puis son nom entre deux séparateurs invisibles (U+2063). Exemple : "🐢⁣Honu⁣".
 * BitChat sur iPhone affiche donc "🐢Honu" ; Reo Fenua affiche le dessin du fenua.
 * Base graphique : Twemoji (CC-BY 4.0), touche polynésienne : Reo Fenua.
 */
data class ReoEmoji(
    val group: String,
    val code: String,
    val label: String,
    val fallback: String,
    val res: Int,
    val variantOf: String? = null,
) {
    val token: String get() = fallback + ReoFenuaEmoji.SEP + label + ReoFenuaEmoji.SEP
}

data class ReoEmojiHit(val start: Int, val end: Int, val emoji: ReoEmoji)

object ReoFenuaEmoji {
    const val SEP = '⁣'
    private const val INLINE_PREFIX = "reo_emoji:"

    val all: List<ReoEmoji> = listOf(
        ReoEmoji("Visages", "sourire", "Sourire", "🙂", R.drawable.reo_emoji_sourire),
        ReoEmoji("Visages", "rire", "Rire", "😂", R.drawable.reo_emoji_rire),
        ReoEmoji("Visages", "clin", "Clin d'œil", "😉", R.drawable.reo_emoji_clin),
        ReoEmoji("Visages", "amour", "Amoureux", "😍", R.drawable.reo_emoji_amour),
        ReoEmoji("Visages", "bisou", "Bisou", "😘", R.drawable.reo_emoji_bisou),
        ReoEmoji("Visages", "cool", "Cool", "😎", R.drawable.reo_emoji_cool),
        ReoEmoji("Visages", "tranquille", "Tranquille", "😌", R.drawable.reo_emoji_tranquille),
        ReoEmoji("Visages", "fiu", "Fiu", "😑", R.drawable.reo_emoji_fiu),
        ReoEmoji("Visages", "dodo", "Dodo", "😴", R.drawable.reo_emoji_dodo),
        ReoEmoji("Visages", "timide", "Gêné", "😊", R.drawable.reo_emoji_timide),
        ReoEmoji("Visages", "miam", "Miam", "😋", R.drawable.reo_emoji_miam),
        ReoEmoji("Visages", "fete", "Fête", "🥳", R.drawable.reo_emoji_fete),
        ReoEmoji("Visages", "pense", "Je réfléchis", "🤔", R.drawable.reo_emoji_pense),
        ReoEmoji("Fenua", "tiare", "Tiare", "🌺", R.drawable.reo_emoji_tiare),
        ReoEmoji("Fenua", "hei", "Hei", "💐", R.drawable.reo_emoji_hei),
        ReoEmoji("Fenua", "bodyboard", "Bodyboard", "🏄", R.drawable.reo_emoji_bodyboard),
        ReoEmoji("Fenua", "famille", "Fēti'i", "👨‍👩‍👧", R.drawable.reo_emoji_famille),
        ReoEmoji("Fenua", "famille-1", "Fēti'i (clair)", "👨‍👩‍👧", R.drawable.reo_emoji_famille_1, variantOf = "famille"),
        ReoEmoji("Fenua", "famille-2", "Fēti'i (mat)", "👨‍👩‍👧", R.drawable.reo_emoji_famille_2, variantOf = "famille"),
        ReoEmoji("Fenua", "famille-3", "Fēti'i (doré)", "👨‍👩‍👧", R.drawable.reo_emoji_famille_3, variantOf = "famille"),
        ReoEmoji("Fenua", "famille-4", "Fēti'i (brun)", "👨‍👩‍👧", R.drawable.reo_emoji_famille_4, variantOf = "famille"),
        ReoEmoji("Fenua", "famille-5", "Fēti'i (foncé)", "👨‍👩‍👧", R.drawable.reo_emoji_famille_5, variantOf = "famille"),
        ReoEmoji("Mots", "iaorana", "Ia ora na", "👋", R.drawable.reo_emoji_iaorana),
        ReoEmoji("Mots", "mauruuru", "Māuruuru", "🙏", R.drawable.reo_emoji_mauruuru),
        ReoEmoji("Mots", "maeva", "Maeva", "🤗", R.drawable.reo_emoji_maeva),
        ReoEmoji("Mots", "nana", "Nana", "👋", R.drawable.reo_emoji_nana),
        ReoEmoji("Mots", "faaitoito", "Fa'aitoito !", "💪", R.drawable.reo_emoji_faaitoito),
        ReoEmoji("Mots", "aitapeapea", "'Aita pe'ape'a", "👌", R.drawable.reo_emoji_aitapeapea),
        ReoEmoji("Mots", "manuia", "Manuia !", "🥂", R.drawable.reo_emoji_manuia),
        ReoEmoji("Mots", "haeremai", "Haere mai", "👋", R.drawable.reo_emoji_haeremai),
        ReoEmoji("Mots", "aue", "Aue !", "😲", R.drawable.reo_emoji_aue),
        ReoEmoji("Mots", "ahatehuru", "E aha te huru ?", "🙂", R.drawable.reo_emoji_ahatehuru),
        ReoEmoji("Mots", "maitairoa", "Maita'i roa", "👍", R.drawable.reo_emoji_maitairoa),
        ReoEmoji("Mots", "uareva", "Ua reva !", "🚀", R.drawable.reo_emoji_uareva),
        ReoEmoji("Mots", "aroha", "Aroha", "❤️", R.drawable.reo_emoji_aroha),
        ReoEmoji("Urgence", "securite", "Je suis en sécurité", "✅", R.drawable.reo_emoji_securite),
        ReoEmoji("Urgence", "aide", "Besoin d'aide", "🆘", R.drawable.reo_emoji_aide),
        ReoEmoji("Urgence", "eau", "Besoin d'eau", "💧", R.drawable.reo_emoji_eau),
        ReoEmoji("Urgence", "cyclone", "Cyclone", "🌀", R.drawable.reo_emoji_cyclone),
        ReoEmoji("Urgence", "medecin", "Blessé / soins", "🩹", R.drawable.reo_emoji_medecin),
        ReoEmoji("Prévention", "non-ice", "Non à l'ice", "🚫", R.drawable.reo_emoji_non_ice),
        ReoEmoji("Prévention", "non-alcool", "Non à l'alcool", "🚫🍺", R.drawable.reo_emoji_non_alcool),
        ReoEmoji("Prévention", "non-cigarette", "Non à la cigarette", "🚭", R.drawable.reo_emoji_non_cigarette),
        ReoEmoji("Prévention", "non-vape", "Non au vapotage", "🚫💨", R.drawable.reo_emoji_non_vape),
        ReoEmoji("Prévention", "non-violence", "Non à la violence", "🚫👊", R.drawable.reo_emoji_non_violence),
        ReoEmoji("Prévention", "protege", "Je protège les miens", "🫶", R.drawable.reo_emoji_protege),
        ReoEmoji("Prévention", "parler", "J'ai besoin de parler", "💬", R.drawable.reo_emoji_parler)
    )

    val groups: List<String> = all.map { it.group }.distinct()
    fun variantsOf(e: ReoEmoji): List<ReoEmoji> =
        if (e.variantOf != null) emptyList() else all.filter { it.variantOf == e.code }
    private val byLabel: Map<String, ReoEmoji> = all.associateBy { it.label }
    private val byCode: Map<String, ReoEmoji> = all.associateBy { it.code }
    private val tokenRegex = Regex("⁣([^⁣\n]{1,40})⁣")

    /** Repère les emoji Reo Fenua dans un texte (avec leur emoji standard devant). */
    fun find(text: String): List<ReoEmojiHit> {
        if (text.indexOf(SEP) < 0) return emptyList()
        val out = ArrayList<ReoEmojiHit>()
        for (m in tokenRegex.findAll(text)) {
            val e = byLabel[m.groupValues[1]] ?: continue
            var start = m.range.first
            val fb = e.fallback
            if (start >= fb.length && text.regionMatches(start - fb.length, fb, 0, fb.length)) {
                start -= fb.length
            }
            if (out.isNotEmpty() && start < out.last().end) continue
            out.add(ReoEmojiHit(start, m.range.last + 1, e))
        }
        return out
    }

    /** Remplace les emoji Reo Fenua par des images dans un texte de message. */
    fun decorate(text: AnnotatedString): AnnotatedString {
        val hits = try { find(text.text) } catch (_: Exception) { emptyList() }
        if (hits.isEmpty()) return text
        return try {
            buildAnnotatedString {
                var pos = 0
                for (h in hits) {
                    if (h.start > pos) append(text.subSequence(pos, h.start))
                    appendInlineContent(INLINE_PREFIX + h.emoji.code, " ")
                    pos = h.end
                }
                if (pos < text.length) append(text.subSequence(pos, text.length))
            }
        } catch (_: Exception) {
            text
        }
    }

    val inlineContent: Map<String, InlineTextContent> by lazy {
        all.associate { e ->
            (INLINE_PREFIX + e.code) to InlineTextContent(
                Placeholder(1.4.em, 1.4.em, PlaceholderVerticalAlign.TextCenter)
            ) {
                Image(
                    painter = painterResource(e.res),
                    contentDescription = e.label,
                    modifier = Modifier.fillMaxSize()
                )
            }
        }
    }

    /** Insère un emoji à la place du curseur. */
    fun insert(v: TextFieldValue, e: ReoEmoji): TextFieldValue {
        val s = v.selection.min.coerceIn(0, v.text.length)
        val en = v.selection.max.coerceIn(0, v.text.length)
        val t = v.text.substring(0, s) + e.token + v.text.substring(en)
        return TextFieldValue(t, TextRange(s + e.token.length))
    }

    /** Un seul appui sur « effacer » retire l'emoji entier, pas une lettre invisible. */
    fun smartDelete(old: TextFieldValue, new: TextFieldValue): TextFieldValue {
        val o = old.text
        val n = new.text
        if (n.length >= o.length || o.length - n.length > 12 || o.indexOf(SEP) < 0) return new
        var i = 0
        while (i < n.length && n[i] == o[i]) i++
        val hit = find(o).firstOrNull { i >= it.start && i < it.end } ?: return new
        val t = o.removeRange(hit.start, hit.end)
        return TextFieldValue(t, TextRange(hit.start))
    }

    fun codeOf(code: String): ReoEmoji? = byCode[code]
}

/** Dans la case d'écriture : on garde l'emoji standard visible et on cache son nom. */
class ReoFenuaEmojiVisualTransformation : VisualTransformation {
    override fun filter(text: AnnotatedString): TransformedText {
        val hits = try { ReoFenuaEmoji.find(text.text) } catch (_: Exception) { emptyList() }
        if (hits.isEmpty()) return TransformedText(text, OffsetMapping.Identity)
        val b = AnnotatedString.Builder(text)
        for (h in hits) {
            val hideFrom = h.start + h.emoji.fallback.length
            if (hideFrom < h.end) {
                b.addStyle(SpanStyle(fontSize = 0.1.sp, color = Color.Transparent), hideFrom, h.end)
            }
        }
        return TransformedText(b.toAnnotatedString(), OffsetMapping.Identity)
    }
}

/** Bouton tiare à gauche de la case d'écriture. */
@Composable
fun ReoFenuaEmojiButton(value: TextFieldValue, onValueChange: (TextFieldValue) -> Unit) {
    var open by remember { mutableStateOf(false) }
    val current by rememberUpdatedState(value)
    val change by rememberUpdatedState(onValueChange)
    Box(
        modifier = Modifier
            .padding(start = 6.dp, bottom = 6.dp)
            .size(44.dp)
            .clip(CircleShape)
            .clickable { open = true }
            .semantics { contentDescription = "Emoji Reo Fenua" },
        contentAlignment = Alignment.Center
    ) {
        Image(
            painter = painterResource(R.drawable.reo_emoji_tiare),
            contentDescription = null,
            modifier = Modifier.size(30.dp)
        )
    }
    if (open) {
        ReoFenuaEmojiPicker(
            onPick = { e -> change(ReoFenuaEmoji.insert(current, e)) },
            onDismiss = { open = false }
        )
    }
}

@Composable
private fun ReoFenuaEmojiPicker(onPick: (ReoEmoji) -> Unit, onDismiss: () -> Unit) {
    var group by remember { mutableStateOf(ReoFenuaEmoji.groups.first()) }
    var count by remember { mutableStateOf(0) }
    var toneFor by remember { mutableStateOf<ReoEmoji?>(null) }
    val noRipple = remember { MutableInteractionSource() }
    val noRipple2 = remember { MutableInteractionSource() }
    Dialog(
        onDismissRequest = onDismiss,
        properties = DialogProperties(usePlatformDefaultWidth = false)
    ) {
        Box(
            modifier = Modifier
                .fillMaxSize()
                .clickable(interactionSource = noRipple, indication = null) { onDismiss() },
            contentAlignment = Alignment.BottomCenter
        ) {
            Surface(
                modifier = Modifier
                    .fillMaxWidth()
                    .clickable(interactionSource = noRipple2, indication = null) { },
                shape = RoundedCornerShape(topStart = 24.dp, topEnd = 24.dp),
                color = MaterialTheme.colorScheme.surface,
                tonalElevation = 4.dp
            ) {
                Column(
                    modifier = Modifier
                        .navigationBarsPadding()
                        .padding(horizontal = 12.dp, vertical = 10.dp)
                ) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text(
                            text = "Emoji Reo Fenua",
                            fontWeight = FontWeight.Bold,
                            fontSize = 18.sp,
                            color = MaterialTheme.colorScheme.onSurface,
                            modifier = Modifier.weight(1f)
                        )
                        TextButton(onClick = onDismiss) {
                            Text(if (count > 0) "OK ($count)" else "Fermer", fontSize = 16.sp)
                        }
                    }
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .horizontalScroll(rememberScrollState())
                            .padding(vertical = 6.dp),
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        ReoFenuaEmoji.groups.forEach { g ->
                            val sel = g == group
                            Box(
                                modifier = Modifier
                                    .clip(RoundedCornerShape(50))
                                    .background(
                                        if (sel) Color(0xFF0E7C86)
                                        else MaterialTheme.colorScheme.onSurface.copy(alpha = 0.08f)
                                    )
                                    .clickable { group = g; toneFor = null }
                                    .padding(horizontal = 14.dp, vertical = 9.dp)
                            ) {
                                Text(
                                    text = g,
                                    fontSize = 15.sp,
                                    fontWeight = if (sel) FontWeight.Bold else FontWeight.Normal,
                                    color = if (sel) Color.White else MaterialTheme.colorScheme.onSurface
                                )
                            }
                        }
                    }
                    toneFor?.let { base ->
                        Text(
                            text = "Choisissez la couleur de peau :",
                            fontSize = 14.sp,
                            color = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.75f)
                        )
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .horizontalScroll(rememberScrollState())
                                .padding(vertical = 4.dp),
                            horizontalArrangement = Arrangement.spacedBy(6.dp)
                        ) {
                            (listOf(base) + ReoFenuaEmoji.variantsOf(base)).forEach { v ->
                                Box(
                                    modifier = Modifier
                                        .size(56.dp)
                                        .clip(RoundedCornerShape(14.dp))
                                        .background(Color(0xFF0E7C86).copy(alpha = 0.10f))
                                        .clickable {
                                            onPick(v)
                                            count++
                                            toneFor = null
                                        }
                                        .semantics { contentDescription = v.label },
                                    contentAlignment = Alignment.Center
                                ) {
                                    Image(
                                        painter = painterResource(v.res),
                                        contentDescription = null,
                                        modifier = Modifier.size(44.dp)
                                    )
                                }
                            }
                        }
                    }
                    LazyVerticalGrid(
                        columns = GridCells.Adaptive(minSize = 68.dp),
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(300.dp)
                    ) {
                        items(ReoFenuaEmoji.all.filter { it.group == group && it.variantOf == null }, key = { it.code }) { e ->
                            Column(
                                modifier = Modifier
                                    .padding(3.dp)
                                    .clip(RoundedCornerShape(14.dp))
                                    .clickable {
                                        if (ReoFenuaEmoji.variantsOf(e).isNotEmpty()) {
                                            toneFor = e
                                        } else {
                                            onPick(e)
                                            count++
                                        }
                                    }
                                    .padding(vertical = 6.dp, horizontal = 2.dp),
                                horizontalAlignment = Alignment.CenterHorizontally
                            ) {
                                Image(
                                    painter = painterResource(e.res),
                                    contentDescription = e.label,
                                    modifier = Modifier.size(46.dp)
                                )
                                Text(
                                    text = e.label,
                                    fontSize = 11.sp,
                                    maxLines = 1,
                                    overflow = TextOverflow.Ellipsis,
                                    color = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.75f)
                                )
                            }
                        }
                    }
                    Text(
                        text = "Sur iPhone (BitChat), l'emoji arrive en version standard avec son nom.",
                        fontSize = 12.sp,
                        color = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.6f),
                        modifier = Modifier.padding(top = 4.dp)
                    )
                    Text(
                        text = "Dessins : Twemoji (CC-BY 4.0), avec la touche Reo Fenua.",
                        fontSize = 11.sp,
                        color = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.5f)
                    )
                }
            }
        }
    }
}
'''
SAFETY_KT = r'''package com.bitchat.android.ui

import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Build
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.mutableStateOf
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties

// ===================== Charte d'utilisation (une fois) =====================

object ReoFenuaCharter {
    private const val PREFS = "reo_fenua_guide"
    private const val KEY = "charter_v1"
    val needs = mutableStateOf(false)
    private var loaded = false

    fun load(context: Context) {
        if (loaded) return
        loaded = true
        needs.value = !context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getBoolean(KEY, false)
    }

    fun accept(context: Context) {
        needs.value = false
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putBoolean(KEY, true).apply()
    }
}

private val CharterRules = listOf(
    "Pas de drogue, pas de vente ni d'échange de produits interdits.",
    "Pas de violence, de menaces ni de harcèlement.",
    "Pas de contenu sexuel. Respect absolu des mineurs.",
    "Pas de fausses alertes : l'ALERTE sert aux vraies urgences."
)

@Composable
fun ReoFenuaCharterScreen() {
    val context = LocalContext.current
    LaunchedEffect(Unit) { ReoFenuaCharter.load(context) }
    if (!ReoFenuaCharter.needs.value || ReoFenuaGuide.showIntro.value || ReoFenuaName.needsAsk.value) return

    Dialog(
        onDismissRequest = { },
        properties = DialogProperties(usePlatformDefaultWidth = false, dismissOnClickOutside = false)
    ) {
        Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .verticalScroll(rememberScrollState())
            ) {
                NihoManoBand(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(top = reoHeaderTop())
                        .height(14.dp)
                )
                Column(modifier = Modifier.padding(24.dp), verticalArrangement = Arrangement.spacedBy(14.dp)) {
                    Text(
                        text = "Nos règles de vie",
                        fontSize = 28.sp,
                        fontWeight = FontWeight.Bold,
                        color = MaterialTheme.colorScheme.primary
                    )
                    Text(
                        text = "Reo Fenua sert à s'entraider. En l'utilisant, vous acceptez ces règles :",
                        fontSize = 18.sp,
                        color = MaterialTheme.colorScheme.onBackground
                    )
                    CharterRules.forEachIndexed { i, rule ->
                        Row(verticalAlignment = Alignment.Top, horizontalArrangement = Arrangement.spacedBy(12.dp)) {
                            Box(
                                modifier = Modifier
                                    .padding(top = 2.dp)
                                    .background(Color(0xFF0E7C86), MaterialTheme.shapes.small)
                                    .padding(horizontal = 9.dp, vertical = 2.dp)
                            ) {
                                Text(text = "${i + 1}", color = Color.White, fontWeight = FontWeight.Bold, fontSize = 16.sp)
                            }
                            Text(text = rule, fontSize = 17.sp, color = MaterialTheme.colorScheme.onBackground)
                        }
                    }
                    Surface(color = Color(0xFFFDECEE), shape = MaterialTheme.shapes.large) {
                        Text(
                            text = "Les contenus illégaux restent illégaux, même sans internet. " +
                                "Si quelqu'un vous dérange : appui long sur son message, puis « Bloquer ».",
                            fontSize = 15.sp,
                            color = Color(0xFF7A1020),
                            modifier = Modifier.padding(14.dp)
                        )
                    }
                    Text(
                        text = "Reo Fenua ne lit, ne garde et ne transmet aucun message : pas de serveur, pas de compte, pas de fichier sur vous. " +
                            "Seule la personne qui reçoit un message peut choisir de le montrer.",
                        fontSize = 15.sp,
                        fontWeight = FontWeight.Bold,
                        color = MaterialTheme.colorScheme.onBackground
                    )
                    Text(
                        text = "Les images des personnes que vous ne connaissez pas arrivent floues : vous choisissez de les voir ou non.",
                        fontSize = 15.sp,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                    Button(
                        onClick = { ReoFenuaCharter.accept(context) },
                        modifier = Modifier
                            .fillMaxWidth()
                            .heightIn(min = 56.dp)
                    ) { Text(text = "J'accepte", fontSize = 18.sp) }
                }
            }
        }
    }
}

// ===================== Images reçues : floues jusqu'au toucher =====================

/** Cache posé sur une image reçue tant que la personne n'a pas choisi de la voir. */
@Composable
fun ReoFenuaImageCover(modifier: Modifier, onReveal: () -> Unit) {
    // Sur Android 11 et moins, le flou n'existe pas : le cache est alors opaque.
    val strong = Build.VERSION.SDK_INT < Build.VERSION_CODES.S
    Box(
        modifier = modifier
            .background(Color(0xFF0B3C5D).copy(alpha = if (strong) 0.96f else 0.45f))
            .clickable { onReveal() },
        contentAlignment = Alignment.Center
    ) {
        Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.padding(12.dp)) {
            Text(text = "Image reçue", color = Color.White, fontWeight = FontWeight.Bold, fontSize = 16.sp)
            Text(
                text = "Toucher pour voir",
                color = Color.White.copy(alpha = 0.9f),
                fontSize = 14.sp,
                textAlign = TextAlign.Center
            )
        }
    }
}

// ===================== Signaler un message =====================

const val REO_FENUA_CONTACT = "reofenua.contact@gmail.com"

/**
 * Partage UN message reçu, à la demande de la personne, comme une capture d'écran.
 * Pas d'identifiant, pas d'historique, rien n'est gardé sur le téléphone ni envoyé seul.
 */
fun reoFenuaReport(
    context: Context,
    @Suppress("UNUSED_PARAMETER") viewModel: ChatViewModel,
    nickname: String,
    selected: com.bitchat.android.model.BitchatMessage?
) {
    val fmt = java.text.SimpleDateFormat("dd/MM/yyyy HH:mm", java.util.Locale.FRENCH)
    val text = buildString {
        append("Message reçu sur Reo Fenua\n")
        if (selected != null) {
            append("De : ").append(nickname).append(" · ").append(fmt.format(selected.timestamp)).append("\n\n")
            append(selected.content.take(1000)).append("\n")
        } else {
            append("De : ").append(nickname).append("\n")
        }
    }
    try {
        val send = Intent(Intent.ACTION_SEND).apply {
            type = "text/plain"
            putExtra(Intent.EXTRA_TEXT, text)
        }
        context.startActivity(
            Intent.createChooser(send, "Montrer ce message à…").addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        )
    } catch (_: Exception) {
        android.widget.Toast.makeText(context, "Impossible de partager ce message.", android.widget.Toast.LENGTH_LONG).show()
    }
}
'''
URGENCE_KT = r'''package com.bitchat.android.ui

import android.content.Context
import android.content.Intent
import android.provider.Settings
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateMapOf
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import org.json.JSONObject
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

// ===================== Mes proches vont bien ? =====================

/**
 * Retient, pour chaque personne, son dernier « Je vais bien » / « Je suis à l'abri »
 * ou sa dernière ALERTE, pendant 3 jours. Tout reste sur ce téléphone.
 */
object ReoFenuaWellbeing {
    private const val PREFS = "reo_fenua_guide"
    private const val KEY = "wellbeing_v1"
    private const val KEEP_MS = 3L * 24 * 3600 * 1000

    enum class Kind { OK, NEED }
    data class Status(val kind: Kind, val time: Long)

    /** Clé = identifiant de la personne, ou « nom:<pseudo> » si l'identifiant manque. */
    val status = mutableStateMapOf<String, Status>()
    private var loaded = false

    fun load(context: Context) {
        if (loaded) return
        loaded = true
        try {
            val stored = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getString(KEY, null) ?: return
            val raw = ReoFenuaVault.open(stored) ?: return
            val o = JSONObject(raw)
            val limit = System.currentTimeMillis() - KEEP_MS
            for (k in o.keys()) {
                val v = o.getJSONObject(k)
                val t = v.optLong("t")
                if (t < limit) continue
                status[k] = Status(if (v.optString("k") == "NEED") Kind.NEED else Kind.OK, t)
            }
        } catch (_: Exception) {
        }
    }

    private fun save(context: Context) {
        try {
            val o = JSONObject()
            for ((k, s) in status) o.put(k, JSONObject().put("k", s.kind.name).put("t", s.time))
            context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putString(KEY, ReoFenuaVault.seal(o.toString())).apply()
        } catch (_: Exception) {
        }
    }

    private fun classify(content: String): Kind? {
        val c = content.trim()
        if (c.startsWith(ReoFenuaAlert.PREFIX)) return Kind.NEED
        if (c.startsWith("Je vais bien") || c.startsWith("Je suis à l'abri")) return Kind.OK
        if (c.contains(ReoFenuaEmoji.SEP + "Je suis en sécurité" + ReoFenuaEmoji.SEP)) return Kind.OK
        if (c.contains(ReoFenuaEmoji.SEP + "Besoin d'aide" + ReoFenuaEmoji.SEP)) return Kind.NEED
        return null
    }

    /** Appelé pour chaque nouveau message reçu d'une autre personne. */
    fun observe(context: Context, m: com.bitchat.android.model.BitchatMessage) {
        load(context)
        val kind = classify(m.content) ?: return
        val t = m.timestamp.time
        if (t < System.currentTimeMillis() - KEEP_MS) return
        val keys = ArrayList<String>()
        m.senderPeerID?.let { keys.add(it) }
        if (m.sender.isNotBlank()) keys.add("nom:" + m.sender)
        var changed = false
        for (k in keys) {
            val old = status[k]
            if (old == null || old.time <= t) {
                status[k] = Status(kind, t)
                changed = true
            }
        }
        if (changed) save(context)
    }

    fun find(key: String, name: String): Status? {
        val a = status[key]
        val b = status["nom:$name"]
        return when {
            a == null -> b
            b == null -> a
            else -> if (a.time >= b.time) a else b
        }
    }

    fun label(s: Status): String {
        val now = System.currentTimeMillis()
        val day = SimpleDateFormat("yyyyMMdd", Locale.FRENCH)
        val sameDay = day.format(Date(now)) == day.format(Date(s.time))
        val whenText = if (sameDay) {
            "à " + SimpleDateFormat("HH'h'mm", Locale.FRENCH).format(Date(s.time))
        } else {
            "le " + SimpleDateFormat("d MMM 'à' HH'h'mm", Locale.FRENCH).format(Date(s.time))
        }
        return when (s.kind) {
            Kind.OK -> "✅ Va bien ($whenText)"
            Kind.NEED -> "🆘 A demandé de l'aide ($whenText)"
        }
    }
}

/** Petite ligne sous le nom d'un proche. Rien si on n'a pas de nouvelles récentes. */
@Composable
fun ReoFenuaWellbeingLine(key: String, name: String) {
    val context = LocalContext.current
    ReoFenuaWellbeing.load(context)
    val s = ReoFenuaWellbeing.find(key, name) ?: return
    Text(
        text = ReoFenuaWellbeing.label(s),
        fontSize = 14.sp,
        fontWeight = FontWeight.Bold,
        color = if (s.kind == ReoFenuaWellbeing.Kind.OK) Color(0xFF2E7D32) else Color(0xFFC8102E)
    )
}

// ===================== Batterie =====================

@Composable
fun ReoFenuaBatteryCard() {
    val context = LocalContext.current
    Surface(
        color = Color(0xFFFFF4D6),
        shape = MaterialTheme.shapes.large,
        modifier = Modifier.padding(horizontal = 20.dp, vertical = 4.dp)
    ) {
        Column(modifier = Modifier.fillMaxWidth().padding(16.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Text(text = "🔋 Tenir plusieurs jours pendant une coupure", fontSize = 17.sp, fontWeight = FontWeight.Bold, color = Color(0xFF0B3C5D))
            Text(
                text = "Reo Fenua écoute déjà moins souvent quand la batterie est faible.\n" +
                    "• Baissez la luminosité de l'écran.\n" +
                    "• Coupez les données mobiles et le Wi-Fi s'il n'y a pas de réseau.\n" +
                    "• Gardez le Bluetooth allumé et ne fermez pas Reo Fenua.\n" +
                    "• Avant un cyclone : chargez le téléphone et une batterie externe.",
                fontSize = 15.sp,
                color = Color(0xFF1D2A33)
            )
            OutlinedButton(
                onClick = { openBatterySaver(context) },
                modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)
            ) { Text(text = "Ouvrir l'économiseur de batterie", fontSize = 15.sp) }
        }
    }
}

private fun openBatterySaver(context: Context) {
    val actions = listOf(Settings.ACTION_BATTERY_SAVER_SETTINGS, Settings.ACTION_SETTINGS)
    for (a in actions) {
        try {
            context.startActivity(Intent(a).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK))
            return
        } catch (_: Exception) {
        }
    }
}
'''
VAULT_KT = r'''package com.bitchat.android.ui

import android.content.Context
import android.security.keystore.KeyGenParameterSpec
import android.security.keystore.KeyProperties
import android.util.Base64
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.lifecycle.compose.LocalLifecycleOwner
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import java.security.KeyStore
import java.security.SecureRandom
import javax.crypto.Cipher
import javax.crypto.KeyGenerator
import javax.crypto.SecretKey
import javax.crypto.SecretKeyFactory
import javax.crypto.spec.GCMParameterSpec
import javax.crypto.spec.PBEKeySpec

// ===================== Coffre-fort : données Reo Fenua chiffrées sur le téléphone =====================

/**
 * Chiffre les lettres et « Mes proches vont bien » avec une clé AES-256-GCM
 * qui reste dans le coffre-fort matériel d'Android (Keystore) et ne sort jamais.
 * Les anciens fichiers en clair sont relus une fois puis réécrits chiffrés.
 */
object ReoFenuaVault {
    private const val ALIAS = "reo_fenua_storage_v1"
    private const val PROVIDER = "AndroidKeyStore"
    private const val PREFIX = "RFV1:"
    private const val IV_BYTES = 12

    private fun key(): SecretKey {
        val ks = KeyStore.getInstance(PROVIDER).apply { load(null) }
        (ks.getKey(ALIAS, null) as? SecretKey)?.let { return it }
        val gen = KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_AES, PROVIDER)
        gen.init(
            KeyGenParameterSpec.Builder(ALIAS, KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT)
                .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                .setKeySize(256)
                .build()
        )
        return gen.generateKey()
    }

    /** Texte en clair → texte chiffré. En cas de souci matériel, on garde le texte tel quel. */
    fun seal(plain: String): String = try {
        val c = Cipher.getInstance("AES/GCM/NoPadding")
        c.init(Cipher.ENCRYPT_MODE, key())
        val iv = c.iv
        val ct = c.doFinal(plain.toByteArray(Charsets.UTF_8))
        PREFIX + Base64.encodeToString(iv + ct, Base64.NO_WRAP)
    } catch (_: Exception) {
        plain
    }

    /** Texte chiffré (ou ancien texte en clair) → texte en clair. Null si illisible. */
    fun open(stored: String): String? {
        if (!stored.startsWith(PREFIX)) return stored
        return try {
            val all = Base64.decode(stored.substring(PREFIX.length), Base64.NO_WRAP)
            val iv = all.copyOfRange(0, IV_BYTES)
            val ct = all.copyOfRange(IV_BYTES, all.size)
            val c = Cipher.getInstance("AES/GCM/NoPadding")
            c.init(Cipher.DECRYPT_MODE, key(), GCMParameterSpec(128, iv))
            String(c.doFinal(ct), Charsets.UTF_8)
        } catch (_: Exception) {
            null
        }
    }

    fun isSealed(stored: String): Boolean = stored.startsWith(PREFIX)

    /** « Nouvelle identité » : on détruit la clé et les données Reo Fenua. */
    fun wipe(context: Context) {
        try {
            KeyStore.getInstance(PROVIDER).apply { load(null) }.deleteEntry(ALIAS)
        } catch (_: Exception) {
        }
        try {
            java.io.File(context.filesDir, "reo_letters.json").delete()
        } catch (_: Exception) {
        }
        try {
            context.getSharedPreferences("reo_fenua_guide", Context.MODE_PRIVATE).edit()
                .remove("wellbeing_v1").remove("lock_hash").remove("lock_salt").apply()
        } catch (_: Exception) {
        }
        ReoFenuaWellbeing.status.clear()
        ReoFenuaLetters.letters.clear()
        ReoFenuaLock.enabled.value = false
        ReoFenuaLock.locked.value = false
    }
}

// ===================== Verrouillage de l'app par un code (facultatif) =====================

object ReoFenuaLock {
    private const val PREFS = "reo_fenua_guide"
    private const val K_HASH = "lock_hash"
    private const val K_SALT = "lock_salt"
    private const val RELOCK_MS = 2 * 60 * 1000L

    val enabled = mutableStateOf(false)
    val locked = mutableStateOf(false)
    private var loaded = false
    private var stoppedAt = 0L
    private var failures = 0
    var relockAfterAlert = false

    fun load(context: Context) {
        if (loaded) return
        loaded = true
        enabled.value = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).contains(K_HASH)
        locked.value = enabled.value
    }

    private fun hash(pin: String, salt: ByteArray): String {
        val f = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256")
        val k = f.generateSecret(PBEKeySpec(pin.toCharArray(), salt, 120_000, 256)).encoded
        return Base64.encodeToString(k, Base64.NO_WRAP)
    }

    fun set(context: Context, pin: String) {
        val salt = ByteArray(16).also { SecureRandom().nextBytes(it) }
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit()
            .putString(K_SALT, Base64.encodeToString(salt, Base64.NO_WRAP))
            .putString(K_HASH, hash(pin, salt))
            .apply()
        enabled.value = true
    }

    fun remove(context: Context) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().remove(K_HASH).remove(K_SALT).apply()
        enabled.value = false
        locked.value = false
    }

    fun check(context: Context, pin: String): Boolean {
        val p = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
        val salt = Base64.decode(p.getString(K_SALT, "") ?: "", Base64.NO_WRAP)
        val ok = p.getString(K_HASH, null) == hash(pin, salt)
        if (ok) {
            failures = 0
            locked.value = false
        } else {
            failures++
        }
        return ok
    }

    /** Après plusieurs erreurs, on fait patienter un peu plus à chaque fois. */
    fun waitSeconds(): Int = if (failures < 5) 0 else minOf(60, (failures - 4) * 10)

    fun onStop() { stoppedAt = System.currentTimeMillis() }
    fun onStart() {
        if (enabled.value && stoppedAt > 0 && System.currentTimeMillis() - stoppedAt > RELOCK_MS) locked.value = true
    }
}

/** Écran de verrouillage, posé au-dessus de toute l'application. */
@Composable
fun ReoFenuaLockHost(viewModel: ChatViewModel) {
    val context = LocalContext.current
    ReoFenuaLock.load(context)
    val owner = LocalLifecycleOwner.current
    DisposableEffect(owner) {
        val obs = LifecycleEventObserver { _, e ->
            when (e) {
                Lifecycle.Event.ON_STOP -> ReoFenuaLock.onStop()
                Lifecycle.Event.ON_START -> ReoFenuaLock.onStart()
                else -> Unit
            }
        }
        owner.lifecycle.addObserver(obs)
        onDispose { owner.lifecycle.removeObserver(obs) }
    }
    androidx.compose.runtime.LaunchedEffect(ReoFenuaAlert.show.value) {
        if (ReoFenuaLock.relockAfterAlert && !ReoFenuaAlert.show.value) {
            ReoFenuaLock.relockAfterAlert = false
            ReoFenuaLock.locked.value = true
        }
    }
    if (!ReoFenuaLock.locked.value) return

    var pin by remember { mutableStateOf("") }
    var error by remember { mutableStateOf<String?>(null) }
    var confirmErase by remember { mutableStateOf(false) }
    Dialog(
        onDismissRequest = { },
        properties = DialogProperties(
            usePlatformDefaultWidth = false,
            dismissOnBackPress = false,
            dismissOnClickOutside = false
        )
    ) {
        Surface(modifier = Modifier.fillMaxSize(), color = Color(0xFF0B3C5D)) {
            Column(
                modifier = Modifier.fillMaxSize().padding(28.dp),
                verticalArrangement = Arrangement.Center,
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Text(text = "🔒 Reo Fenua", fontSize = 30.sp, fontWeight = FontWeight.Bold, color = Color.White)
                Text(text = "Entrez votre code", fontSize = 18.sp, color = Color.White, modifier = Modifier.padding(top = 8.dp, bottom = 20.dp))
                OutlinedTextField(
                    value = pin,
                    onValueChange = { v -> pin = v.filter { it.isDigit() }.take(8); error = null },
                    singleLine = true,
                    visualTransformation = PasswordVisualTransformation(),
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.NumberPassword),
                    modifier = Modifier.fillMaxWidth()
                )
                error?.let { Text(text = it, color = Color(0xFFFFB4B4), fontSize = 15.sp, modifier = Modifier.padding(top = 8.dp)) }
                Button(
                    onClick = {
                        val wait = ReoFenuaLock.waitSeconds()
                        if (wait > 0 && error != null && error!!.startsWith("Trop")) return@Button
                        if (!ReoFenuaLock.check(context, pin)) {
                            pin = ""
                            val w = ReoFenuaLock.waitSeconds()
                            error = if (w > 0) "Trop d'erreurs : patientez $w secondes." else "Code incorrect."
                            if (w > 0) {
                                android.os.Handler(android.os.Looper.getMainLooper()).postDelayed({ error = "Réessayez." }, w * 1000L)
                            }
                        }
                    },
                    enabled = pin.length >= 4,
                    modifier = Modifier.fillMaxWidth().padding(top = 16.dp).heightIn(min = 56.dp)
                ) { Text(text = "Ouvrir", fontSize = 18.sp) }
                Text(
                    text = "L'ALERTE reste possible : touchez ci-dessous.",
                    color = Color.White.copy(alpha = 0.8f),
                    fontSize = 14.sp,
                    modifier = Modifier.padding(top = 24.dp)
                )
                Button(
                    onClick = {
                        ReoFenuaLock.locked.value = false
                        ReoFenuaAlert.show.value = true
                        // on reverrouille dès la fermeture de l'écran d'alerte
                        ReoFenuaLock.relockAfterAlert = true
                    },
                    colors = androidx.compose.material3.ButtonDefaults.buttonColors(containerColor = Color(0xFFC8102E), contentColor = Color.White),
                    modifier = Modifier.fillMaxWidth().padding(top = 8.dp).heightIn(min = 56.dp)
                ) { Text(text = "! ALERTE", fontSize = 20.sp, fontWeight = FontWeight.Bold) }
                if (!confirmErase) {
                    TextButton(onClick = { confirmErase = true }, modifier = Modifier.padding(top = 18.dp)) {
                        Text(text = "Code oublié ?", color = Color.White, fontSize = 15.sp)
                    }
                } else {
                    Text(
                        text = "Sans le code, la seule solution est de tout effacer et de repartir avec une nouvelle identité.",
                        color = Color.White,
                        fontSize = 15.sp,
                        modifier = Modifier.padding(top = 18.dp)
                    )
                    TextButton(onClick = {
                        ReoFenuaVault.wipe(context)
                        ReoFenuaLock.remove(context)
                        viewModel.panicClearAllData()
                    }) { Text(text = "Tout effacer", color = Color(0xFFFFB4B4), fontSize = 16.sp, fontWeight = FontWeight.Bold) }
                }
            }
        }
    }
}

/** Réglage dans « Plus » : activer, changer ou retirer le code. */
@Composable
fun ReoFenuaLockSetting() {
    val context = LocalContext.current
    ReoFenuaLock.load(context)
    var editing by remember { mutableStateOf(false) }
    var a by remember { mutableStateOf("") }
    var b by remember { mutableStateOf("") }
    Surface(
        color = MaterialTheme.colorScheme.surface,
        shape = MaterialTheme.shapes.large,
        modifier = Modifier.padding(horizontal = 20.dp, vertical = 4.dp)
    ) {
        Column(modifier = Modifier.fillMaxWidth().padding(16.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Text(
                text = if (ReoFenuaLock.enabled.value) "🔒 Code de verrouillage : activé" else "🔓 Verrouiller Reo Fenua par un code",
                fontSize = 17.sp,
                fontWeight = FontWeight.Bold,
                color = MaterialTheme.colorScheme.onSurface
            )
            Text(
                text = "L'app se verrouille 2 minutes après l'avoir quittée. Le bouton ALERTE reste toujours accessible. " +
                    "Attention : si vous oubliez ce code, personne ne pourra le retrouver, pas même Reo Fenua. Il faudra tout effacer et repartir avec une nouvelle identité.",
                fontSize = 14.sp,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
            if (editing) {
                OutlinedTextField(
                    value = a, onValueChange = { v -> a = v.filter { it.isDigit() }.take(8) },
                    label = { Text("Nouveau code (4 à 8 chiffres)") }, singleLine = true,
                    visualTransformation = PasswordVisualTransformation(),
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.NumberPassword),
                    modifier = Modifier.fillMaxWidth()
                )
                OutlinedTextField(
                    value = b, onValueChange = { v -> b = v.filter { it.isDigit() }.take(8) },
                    label = { Text("Le même code, encore une fois") }, singleLine = true,
                    visualTransformation = PasswordVisualTransformation(),
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.NumberPassword),
                    modifier = Modifier.fillMaxWidth()
                )
                Button(
                    onClick = { ReoFenuaLock.set(context, a); editing = false; a = ""; b = "" },
                    enabled = a.length >= 4 && a == b,
                    modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)
                ) { Text("Enregistrer le code", fontSize = 16.sp) }
                TextButton(onClick = { editing = false; a = ""; b = "" }) { Text("Annuler") }
            } else {
                Button(onClick = { editing = true }, modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)) {
                    Text(if (ReoFenuaLock.enabled.value) "Changer le code" else "Choisir un code", fontSize = 16.sp)
                }
                if (ReoFenuaLock.enabled.value) {
                    TextButton(onClick = { ReoFenuaLock.remove(context) }) { Text("Retirer le code", fontSize = 15.sp) }
                }
            }
        }
    }
}

// ===================== Réinitialiser les réglages =====================

/** Remet les réglages d'origine (mode, texte, son, lieu, Radar, aide). Garde identité, messages, lettres et code. */
object ReoFenuaReset {
    private val KEYS = listOf(
        "simple_mode", "text_scale", "message_sound", "alert_place",
        "radar_warned", "intro_seen_v1", "wallpaper", "channels_help_hidden", "style_theme"
    )

    fun resetSettings(context: Context) {
        try {
            val e = context.getSharedPreferences("reo_fenua_guide", Context.MODE_PRIVATE).edit()
            for (k in KEYS) e.remove(k)
            e.commit()
        } catch (_: Exception) {
        }
        // Redémarre l'app pour repartir proprement
        try {
            val launch = context.packageManager.getLaunchIntentForPackage(context.packageName)
            if (launch != null) {
                launch.addFlags(android.content.Intent.FLAG_ACTIVITY_NEW_TASK or android.content.Intent.FLAG_ACTIVITY_CLEAR_TASK)
                context.startActivity(launch)
            }
            (context as? android.app.Activity)?.finishAffinity()
            android.os.Process.killProcess(android.os.Process.myPid())
        } catch (_: Exception) {
        }
    }
}

@Composable
fun ReoFenuaResetSetting() {
    val context = LocalContext.current
    var confirm by remember { mutableStateOf(false) }
    Surface(
        color = MaterialTheme.colorScheme.surface,
        shape = MaterialTheme.shapes.large,
        modifier = Modifier.padding(horizontal = 20.dp, vertical = 4.dp)
    ) {
        Column(modifier = Modifier.fillMaxWidth().padding(16.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Text(text = "↺ Réinitialiser les réglages", fontSize = 17.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onSurface)
            Text(
                text = "Remet le mode, la taille du texte, le son, le lieu d'alerte et l'aide comme au premier jour. " +
                    "Votre prénom, vos messages, vos lettres, vos proches et votre code sont gardés.",
                fontSize = 14.sp,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
            if (!confirm) {
                Button(onClick = { confirm = true }, modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)) {
                    Text("Réinitialiser", fontSize = 16.sp)
                }
            } else {
                Text(text = "L'app va redémarrer. Continuer ?", fontSize = 15.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onSurface)
                Button(onClick = { ReoFenuaReset.resetSettings(context) }, modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)) {
                    Text("Oui, réinitialiser", fontSize = 16.sp)
                }
                TextButton(onClick = { confirm = false }) { Text("Non", fontSize = 15.sp) }
            }
        }
    }
}
'''
STYLE_KT = r'''package com.bitchat.android.ui

import android.content.Context
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.ColorScheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.bitchat.android.R

// ===================== Mode stylisé : thèmes polynésiens =====================

enum class ReoTheme(val id: String, val label: String, val sub: String, val dark: Boolean) {
    PO("po", "Pō", "nuit étoilée", true),
    MAHANA("mahana", "Mahana", "coucher de soleil", false),
    TIFAIFAI("tifaifai", "Tīfaifai", "rouge et blanc", false);

    val scheme: ColorScheme
        get() = when (this) {
            PO -> darkColorScheme(
                primary = Color(0xFF5FF2E6), onPrimary = Color(0xFF071A2B),
                primaryContainer = Color(0xFF0E4A55), onPrimaryContainer = Color(0xFFCFFAF6),
                secondary = Color(0xFFFFB86B), onSecondary = Color(0xFF2B1600),
                secondaryContainer = Color(0xFF14324C), onSecondaryContainer = Color(0xFFE6F7F8),
                tertiary = Color(0xFFFF7AA8), onTertiary = Color(0xFF3A0016),
                background = Color(0xFF071A2B), onBackground = Color(0xFFE6F7F8),
                surface = Color(0xFF0E2A42), onSurface = Color(0xFFE6F7F8),
                surfaceVariant = Color(0xFF14324C), onSurfaceVariant = Color(0xFF8FB3C4),
                outline = Color(0xFF24506E), outlineVariant = Color(0xFF1C3B52),
                error = Color(0xFFFF6B7F), onError = Color.Black
            )
            MAHANA -> lightColorScheme(
                primary = Color(0xFFD9573A), onPrimary = Color.White,
                primaryContainer = Color(0xFFFFDCCB), onPrimaryContainer = Color(0xFF3B1A10),
                secondary = Color(0xFF7A2E1E), onSecondary = Color.White,
                secondaryContainer = Color(0xFFFFE9C9), onSecondaryContainer = Color(0xFF3B1A10),
                tertiary = Color(0xFFE8A33A), onTertiary = Color(0xFF2B1600),
                background = Color(0xFFFFF3E8), onBackground = Color(0xFF3B1A10),
                surface = Color(0xFFFFFFFF), onSurface = Color(0xFF3B1A10),
                surfaceVariant = Color(0xFFFFE3D2), onSurfaceVariant = Color(0xFF6E3A28),
                outline = Color(0xFFF0B593), outlineVariant = Color(0xFFF8D6C2),
                error = Color(0xFFB3261E), onError = Color.White
            )
            TIFAIFAI -> lightColorScheme(
                primary = Color(0xFFC8102E), onPrimary = Color.White,
                primaryContainer = Color(0xFFFBE3E6), onPrimaryContainer = Color(0xFF4A0613),
                secondary = Color(0xFF0B3C5D), onSecondary = Color.White,
                secondaryContainer = Color(0xFFD7ECEE), onSecondaryContainer = Color(0xFF072638),
                tertiary = Color(0xFF2E7D32), onTertiary = Color.White,
                background = Color(0xFFFFF8EE), onBackground = Color(0xFF2A1215),
                surface = Color(0xFFFFFFFF), onSurface = Color(0xFF2A1215),
                surfaceVariant = Color(0xFFFBE9EA), onSurfaceVariant = Color(0xFF5C2A30),
                outline = Color(0xFFE7A6AE), outlineVariant = Color(0xFFF3D3D7),
                error = Color(0xFF8E0B21), onError = Color.White
            )
        }

    val swatch: Brush
        get() = when (this) {
            PO -> Brush.linearGradient(listOf(Color(0xFF071A2B), Color(0xFF16365A)))
            MAHANA -> Brush.linearGradient(listOf(Color(0xFFE8735A), Color(0xFFFBE07A)))
            TIFAIFAI -> Brush.linearGradient(listOf(Color(0xFFC8102E), Color(0xFF8E0B21)))
        }
    val swatchText: Color get() = if (this == MAHANA) Color(0xFF3B1A10) else Color.White
}

object ReoFenuaStyle {
    private const val PREFS = "reo_fenua_guide"
    private const val KEY = "style_theme"
    /** Thème choisi, ou null = couleurs classiques Reo Fenua. */
    val theme = mutableStateOf<ReoTheme?>(null)
    private var loaded = false

    fun load(context: Context) {
        if (loaded) return
        loaded = true
        val id = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getString(KEY, null)
        theme.value = ReoTheme.values().firstOrNull { it.id == id }
    }

    fun set(context: Context, t: ReoTheme?) {
        theme.value = t
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().apply {
            if (t == null) remove(KEY) else putString(KEY, t.id)
        }.apply()
    }

    val stylised: Boolean get() = theme.value != null
}

// ===================== Avatars dessinés (calculés, jamais envoyés) =====================

private val AvBg = intArrayOf(R.drawable.reo_av_bg_0, R.drawable.reo_av_bg_1, R.drawable.reo_av_bg_2, R.drawable.reo_av_bg_3, R.drawable.reo_av_bg_4)
private val AvFace = intArrayOf(
    R.drawable.reo_av_face_0, R.drawable.reo_av_face_1, R.drawable.reo_av_face_2,
    R.drawable.reo_av_face_3, R.drawable.reo_av_face_4, R.drawable.reo_av_face_5
)
private val AvAcc = intArrayOf(0, R.drawable.reo_av_acc_1, R.drawable.reo_av_acc_2, R.drawable.reo_av_acc_3, R.drawable.reo_av_acc_4)

/**
 * Avatar polynésien tiré de l'identifiant : chaque personne a toujours le même,
 * sans photo et sans rien envoyer sur le réseau.
 */
@Composable
fun ReoFenuaDrawnAvatar(key: String, size: Dp) {
    val h = (key.hashCode().toLong() and 0x7fffffffL)
    val face = AvFace[(h % AvFace.size).toInt()]
    val acc = AvAcc[((h / AvFace.size) % AvAcc.size).toInt()]
    val bg = AvBg[((h / (AvFace.size * AvAcc.size)) % AvBg.size).toInt()]
    Box(modifier = Modifier.size(size).clip(CircleShape)) {
        Image(painter = painterResource(bg), contentDescription = null, modifier = Modifier.fillMaxSize())
        Image(painter = painterResource(face), contentDescription = null, modifier = Modifier.fillMaxSize())
        if (acc != 0) Image(painter = painterResource(acc), contentDescription = null, modifier = Modifier.fillMaxSize())
    }
}

// ===================== Réglage « Apparence » dans Plus =====================

@Composable
fun ReoFenuaStyleSetting() {
    val context = LocalContext.current
    ReoFenuaStyle.load(context)
    val current = ReoFenuaStyle.theme.value
    Surface(
        color = MaterialTheme.colorScheme.surface,
        shape = MaterialTheme.shapes.large,
        modifier = Modifier.padding(horizontal = 20.dp, vertical = 4.dp)
    ) {
        Column(modifier = Modifier.fillMaxWidth().padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
            Text(text = "✨ Mode stylisé", fontSize = 17.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onSurface)
            Text(
                text = "Des couleurs inspirées du fenua et des avatars dessinés pour vos proches. Tout le reste ne change pas.",
                fontSize = 14.sp,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp), modifier = Modifier.fillMaxWidth()) {
                ReoTheme.values().forEach { t ->
                    val sel = current == t
                    Box(
                        modifier = Modifier
                            .weight(1f)
                            .height(78.dp)
                            .clip(RoundedCornerShape(16.dp))
                            .background(t.swatch)
                            .then(if (sel) Modifier.border(3.dp, MaterialTheme.colorScheme.primary, RoundedCornerShape(16.dp)) else Modifier)
                            .clickable { ReoFenuaStyle.set(context, t) }
                            .padding(10.dp),
                        contentAlignment = Alignment.BottomStart
                    ) {
                        Column {
                            Text(text = t.label, color = t.swatchText, fontSize = 17.sp, fontWeight = FontWeight.Bold)
                            Text(text = t.sub, color = t.swatchText.copy(alpha = 0.85f), fontSize = 11.sp)
                        }
                    }
                }
            }
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .clip(RoundedCornerShape(14.dp))
                    .background(if (current == null) MaterialTheme.colorScheme.primaryContainer else MaterialTheme.colorScheme.surfaceVariant)
                    .clickable { ReoFenuaStyle.set(context, null) }
                    .padding(12.dp),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = if (current == null) "✓ Couleurs classiques Reo Fenua" else "Revenir aux couleurs classiques",
                    fontSize = 15.sp,
                    fontWeight = FontWeight.Bold,
                    color = MaterialTheme.colorScheme.onSurface
                )
            }
            if (current != null) {
                Row(horizontalArrangement = Arrangement.spacedBy(6.dp), verticalAlignment = Alignment.CenterVertically) {
                    listOf("Teva", "Hina", "Manu", "Vaiana", "Tama").forEach { n -> ReoFenuaDrawnAvatar(key = n, size = 40.dp) }
                    Text(text = "  avatars", fontSize = 13.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
                }
            }
        }
    }
}

// ===================== Changer de mode depuis la page principale =====================

object ReoFenuaModeSheet {
    val show = mutableStateOf(false)
}

private enum class ReoModeKind { SIMPLE, COMPLET, STYLISE }

private fun currentMode(): ReoModeKind = when {
    ReoFenuaMode.simple.value -> ReoModeKind.SIMPLE
    ReoFenuaStyle.stylised -> ReoModeKind.STYLISE
    else -> ReoModeKind.COMPLET
}

/** Pastille bien visible en haut de la page principale : mode actuel, un toucher pour changer. */
@Composable
fun ReoFenuaModePill(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    ReoFenuaMode.load(context)
    ReoFenuaStyle.load(context)
    val (icon, label) = when (currentMode()) {
        ReoModeKind.SIMPLE -> "🌺" to "Simple"
        ReoModeKind.COMPLET -> "☰" to "Complet"
        ReoModeKind.STYLISE -> "✨" to "Stylisé"
    }
    Surface(
        color = MaterialTheme.colorScheme.primary,
        contentColor = MaterialTheme.colorScheme.onPrimary,
        shape = RoundedCornerShape(50),
        shadowElevation = 6.dp,
        modifier = modifier
            .clip(RoundedCornerShape(50))
            .clickable { ReoFenuaModeSheet.show.value = true }
            .semantics { contentDescription = "Mode $label. Toucher pour changer de mode" }
    ) {
        Row(
            modifier = Modifier.padding(horizontal = 14.dp, vertical = 9.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(6.dp)
        ) {
            Text(text = icon, fontSize = 16.sp)
            Text(text = "Mode $label", fontSize = 15.sp, fontWeight = FontWeight.Bold)
            Text(text = "▾", fontSize = 13.sp)
        }
    }
    if (ReoFenuaModeSheet.show.value) ReoFenuaModeSheetDialog()
}

private fun applyMode(context: Context, kind: ReoModeKind) {
    when (kind) {
        ReoModeKind.SIMPLE -> { ReoFenuaMode.set(context, true); ReoFenuaStyle.set(context, null) }
        ReoModeKind.COMPLET -> { ReoFenuaMode.set(context, false); ReoFenuaStyle.set(context, null) }
        ReoModeKind.STYLISE -> {
            ReoFenuaMode.set(context, false)
            if (ReoFenuaStyle.theme.value == null) ReoFenuaStyle.set(context, ReoTheme.PO)
        }
    }
    val name = when (kind) { ReoModeKind.SIMPLE -> "Simple"; ReoModeKind.COMPLET -> "Complet"; ReoModeKind.STYLISE -> "Stylisé" }
    android.widget.Toast.makeText(context, "Mode $name activé. Pour changer : touchez la pastille en haut.", android.widget.Toast.LENGTH_LONG).show()
}

@Composable
private fun ReoFenuaModeSheetDialog() {
    val context = LocalContext.current
    val current = currentMode()
    var confirmFor by androidx.compose.runtime.remember { mutableStateOf<ReoModeKind?>(null) }
    val close = { ReoFenuaModeSheet.show.value = false }
    androidx.compose.ui.window.Dialog(
        onDismissRequest = close,
        properties = androidx.compose.ui.window.DialogProperties(usePlatformDefaultWidth = false)
    ) {
        Box(
            modifier = Modifier
                .fillMaxSize()
                .clickable(
                    interactionSource = androidx.compose.runtime.remember { androidx.compose.foundation.interaction.MutableInteractionSource() },
                    indication = null
                ) { close() },
            contentAlignment = Alignment.BottomCenter
        ) {
            Surface(
                shape = RoundedCornerShape(topStart = 26.dp, topEnd = 26.dp),
                color = MaterialTheme.colorScheme.surface,
                modifier = Modifier
                    .fillMaxWidth()
                    .clickable(
                        interactionSource = androidx.compose.runtime.remember { androidx.compose.foundation.interaction.MutableInteractionSource() },
                        indication = null
                    ) { }
            ) {
                Column(
                    modifier = Modifier
                        .navigationBarsPadding()
                        .padding(16.dp),
                    verticalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    Text(text = "Choisir un mode", fontSize = 22.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onSurface)
                    Text(
                        text = "Vos messages, vos proches, vos lettres et l'ALERTE restent les mêmes. Seul l'affichage change.",
                        fontSize = 14.sp,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                    val pending = confirmFor
                    if (pending != null) {
                        val n = when (pending) { ReoModeKind.SIMPLE -> "Simple"; ReoModeKind.COMPLET -> "Complet"; ReoModeKind.STYLISE -> "Stylisé" }
                        Text(text = "Passer au mode $n ?", fontSize = 20.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onSurface)
                        androidx.compose.material3.Button(
                            onClick = { applyMode(context, pending); close() },
                            modifier = Modifier.fillMaxWidth().height(56.dp)
                        ) { Text("Oui", fontSize = 18.sp) }
                        androidx.compose.material3.OutlinedButton(
                            onClick = { confirmFor = null },
                            modifier = Modifier.fillMaxWidth().height(56.dp)
                        ) { Text("Non", fontSize = 18.sp) }
                    } else {
                        ModeCard(
                            emoji = "🌺", title = "Simple", body = "Gros boutons, l'essentiel : ALERTE, famille, lettres.",
                            selected = current == ReoModeKind.SIMPLE, brush = Brush.linearGradient(listOf(Color(0xFFFFF4DC), Color(0xFFFFE3B0))), dark = false
                        ) { if (current != ReoModeKind.SIMPLE) { applyMode(context, ReoModeKind.SIMPLE); close() } }
                        ModeCard(
                            emoji = "☰", title = "Complet", body = "Tout Reo Fenua : discussions, Radar, réseau, réglages.",
                            selected = current == ReoModeKind.COMPLET, brush = Brush.linearGradient(listOf(Color(0xFFD7ECEE), Color(0xFFB8DDE1))), dark = false
                        ) {
                            if (current == ReoModeKind.SIMPLE) confirmFor = ReoModeKind.COMPLET
                            else if (current != ReoModeKind.COMPLET) { applyMode(context, ReoModeKind.COMPLET); close() }
                        }
                        ModeCard(
                            emoji = "✨", title = "Stylisé", body = "Couleurs du fenua, avatars dessinés, petits gestes.",
                            selected = current == ReoModeKind.STYLISE, brush = Brush.linearGradient(listOf(Color(0xFF071A2B), Color(0xFF16365A))), dark = true
                        ) {
                            if (current == ReoModeKind.SIMPLE) confirmFor = ReoModeKind.STYLISE
                            else if (current != ReoModeKind.STYLISE) { applyMode(context, ReoModeKind.STYLISE); close() }
                        }
                        if (current == ReoModeKind.STYLISE) {
                            Row(horizontalArrangement = Arrangement.spacedBy(8.dp), modifier = Modifier.fillMaxWidth()) {
                                ReoTheme.values().forEach { t ->
                                    val sel = ReoFenuaStyle.theme.value == t
                                    Box(
                                        modifier = Modifier
                                            .weight(1f)
                                            .height(48.dp)
                                            .clip(RoundedCornerShape(14.dp))
                                            .background(t.swatch)
                                            .then(if (sel) Modifier.border(3.dp, MaterialTheme.colorScheme.primary, RoundedCornerShape(14.dp)) else Modifier)
                                            .clickable { ReoFenuaStyle.set(context, t) },
                                        contentAlignment = Alignment.Center
                                    ) { Text(text = t.label, color = t.swatchText, fontWeight = FontWeight.Bold, fontSize = 15.sp) }
                                }
                            }
                        }
                        androidx.compose.material3.TextButton(onClick = close, modifier = Modifier.fillMaxWidth()) {
                            Text("Annuler", fontSize = 17.sp)
                        }
                    }
                }
            }
        }
    }
}

@Composable
private fun ModeCard(emoji: String, title: String, body: String, selected: Boolean, brush: Brush, dark: Boolean, onClick: () -> Unit) {
    val fg = if (dark) Color.White else Color(0xFF0B3C5D)
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(18.dp))
            .background(brush)
            .then(if (selected) Modifier.border(3.dp, MaterialTheme.colorScheme.primary, RoundedCornerShape(18.dp)) else Modifier)
            .clickable { onClick() }
            .padding(horizontal = 16.dp, vertical = 14.dp)
    ) {
        Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(14.dp)) {
            Text(text = emoji, fontSize = 30.sp)
            Column(modifier = Modifier.weight(1f)) {
                Text(text = title + if (selected) "  ✓ actuel" else "", fontSize = 19.sp, fontWeight = FontWeight.Bold, color = fg)
                Text(text = body, fontSize = 14.sp, color = fg.copy(alpha = 0.85f))
            }
        }
    }
}
'''
EMOJI_PNG = {"reo_emoji_sourire": "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", "reo_emoji_rire": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEX+y00AAABcrOtmRQD5+vv+y03YqTmNZxN0VA3n6+zsu0OxhyXGmTD/y0zT3OL/zEz/zEz/y0z/y0zt59Pt3KuZchn/1Ebqxmf/yktqWy1kruP9qjKWt7KCXQ7Y4uhcre63u5TUw3bU19ZcrOt0sdO0p4tiaVOQeUmieh6qmHP802xcreu9ki3Gt5Vaq/KmfSCpuaPEwIXisj732ZL14bXh6Oz//1XPxbD/zDPy9fdcrOtPt/rGuqH1kxD/v0Dvy478///09/lelLV9YSdgrfCEaTOZhFaci2eFtMSRx/LY0L/j3Mz2+vpfiZxeoNBcrOxheXdgf4VjncJpqtWLcj6Yuq6jj2bMvHLj6O3z+Pn09/lfi6JemsJdrO1csetlmrhgv/9gsOdss+yoxder1PXGwoTHz8/f///6nyH4vmvx3KP54J7h5+zl6+/r7/P//wD28d/x9fgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACultnoAAAAgHRSTlP+AP7//s//////////Uf81Z6yJ////DP8M////////Nv///0r////////+jP//Fv///////5YD/wXO2Az//wT/Dk///xL/////////OP//vf//////P///M2+L//9+J/8ISv///2z/CP//qf9fpMQB/7YAAAAAAAAAAAAAAAAAAInwhkEAAAYMSURBVHjazZpnW+M4EICNe1xiJ04jBAghIQRC77C79LLA9np7vff2/7+cZNmxbEu27Nzds/NhF5A0rzVN48JNMEnDMsslSZI4IOC/Utm0GmwrufQpj6yyqzgqUtl6ND7AsktcgpRsaxxAzUzU7jHMWk7Avi1xTCKZ+zkANZvLIHYtK8CSuEwiWZkAjTKXWcowbk8+HBzcpwNMLpeYE/cilNMUwG45n35u6RdRLHQA4SQRUJNyqq9UHLFQjG4hBrByKd/+dbtSqYiiq188eE8H5DH/kuOqdQLAzm8nFICd5/pFT4CFCu4Pf+zsvCcD8oWPr1cUZ9APv+/s7PxIAuQMT98yYkASxb9P4gArZ3j+JRZnfIIYyGkUkFc/twW2gPaw9fOxU5jpzBSLEHkaBvwp5QVw4LpniuCf+hQQB+0CZMRBGFDOrZ8DGQYUdopTUw8fTm2PbPQhBDC5MQAwiQFj6qcQ4B4H1MhLZb0qJ6k2qvomBKBUQyby9X8ScjLpbJSrAhSNrn/TnbB47Cs9rh87nQKu3wcQImioCkh0OmANzbj2g3QGeVd0nO2KhQP2YxEk++rBBdIBaItC2wOgWAXx5FQqW1INA0RLkFYVAklwgoxmdPzAHO2jUgHndACIetgItCt6opNBEPiAQtFPY/BrZQkM7o4ANtGygqDqGkOQ6sIeyDOYuo7jW2rLbTV8wK5EMqygGKx5sOJdeW/PByy5ncauBwhvQPH0G1mq0V2h0Fnv9XqOB/C7AAQI5cC0Zx0tWzJriqD2r68HBbekbnldJQI0CNe/mL1eeJaF5tr2/1ZzAXbcv0aeirTorV1aCjpKFyDF4lrPV/O83WPGlSAAt5Ca1z64/6rYX2oAYOIR7YZn7rKtqdHUNwEgOGg0Ia16pgkysYp1xAAgRTagj3HyeI42MCdwtYgHpsObluXEDcXGo1uocVZkf1iEyl5YKJR6RxrXI16wODsCwHMzqKkaMXcJ41oEYHPlcJQNIynh11WZchTExvVwHJY5vBCtVQ3CkUA8dujjhrKG3+RyUtJRRSWkjQdhRAZsCgTR2MdxQELOR0RhH08TY+EJcp3iihozs+9abFz9dEFm1V9/yfNPQiemoYRyUI2eqGD8jOe/rLPp3+ChvIvuSg0A4PSKFpR3cE1zjkX/uqufb8UNhwVRbPAGrWqn62+hmXwzU5Gre6sIBImsn+c3sgDaPIUQzYP10USCjRKky1MuTAqVCuxCgOSxEJSQp0t4sfPihziR1ULQe3i0lrFyzc2F9PPr7IAbnkawsQNnrhkGvDIYU1MehhfyXQ47cEZHZv1VZBqvwmKgJ52ZmqzDQrHAUwm14NDvRmfxC6PjZFqp6lCGhiwbQ/jTWlWZHt0EvYgtbQWHvt+2tGKT+BcCo5zF17aDtsUkBBCSM1YAYS1fHzVerhPqTdIkRv2TpLXIDQ3Y/JaIDoDyw8qgP5mivD9Y+Za4eB3dIKD2vU2cwqOHNM7tg97g7VX/9eW5CgNLPb983b96O+g9uEX3ZI/Jq+t++w5s1CRP+U5kEgrgBloI3UK1yDP4x2yAbyjLN7xbqInvKRP4lw6L/g5tede/CVymzXgq9NL1DyZpy/mvPcAhdYYgnO8lq19RBTrgGQJc8AkAQbh8QFffhkG8QF+/6gJm6RO8JOivEJQXen00mgCYdQHzqQCYUFeDlb3bO3CfXbjbA3nRDx73/DuABEkAzLuAL8YETKb54CjZyami0td7YfqMNv4ZWzV9Slt/6AGoTnjOBnhOW7/sAY7GslCCEy78R2qUWtGqsgH0Fn0DCHBELBZNwq0eyccypdwffhU81iQls9vsa6mbWCS0bKMsC578zpP1w/s9JUl9VSM2hV6S4c+uo4Ru0P7REYtBTzbXJV4/9nh/dZnUOHkNnK4SbiqHtDsL6N9VwluoIx/RJLS92rAadHKqUjXiDWW95fv68wvai7rV2fnZN1KWxzeR+5k3QMHqxH/1spSzdxnfJ+d83WL9Dy+sP5pX7pnfm9q5PnswWT97sPfzfhnC9uHGWJ+eNJIZJbPxsX88Q/n8x2b+/Ocfv6+KR8AkG20AAAAASUVORK5CYII=", "reo_emoji_clin": "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", "reo_emoji_amour": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEXoo6LPz6ni6OvgUGX3rrrs5dz5wHCWdS65q5DBIDjgKkP6nyD/r8vh6Oxugjt+qGW/GzO+R0KosEzgKT3dRlnecoH1r2/zrLrm5ub+y0zcLUMAAABmRQDz9vjyqrjn6u13sVXoWG3YNkX/y0z3t0juhpf/zEvwmKf/zEzsdojpZXj/zEz/y0zmWkb/y0zd5Oj0mUn3qErv6NfPRE53VAjWpzjpZ0bsdkdckTttmEx2qFHhREbvh0j/00b9qDD/ykvJnDGBXA2Qsm7v3OHHqpWMZhOyqIWjxJPR2Mjzqrrssrbtxs6xyanW5NX//1WZchq4W0mvhSTqbYDu8vWDcj2Jq3D0qrntuMPyyIvt1dqSekeDoVKjex7gPUTisj7qytH41Jjq2K/s6+11i0WXhkmYw4OndlG/kyynqXu10qrXrKP0kg3zqrn/v0Dxt8T/zDPh6u///wD////2+P16eTyGnFOQmWaVtoewZkq4iXK0m36ltGyiv5TcLELdLUPWV2ZkEtWzAAAAgHRSTlPy+Jr0JOTt////KP8LRP//////GY///2sK/v8A//7+/////s///07+Zv//Nq7/iv/////////////////7Dv8O////////////sPz8//8D/////8z//0r///3//////8///9b///////////+VBNoFNAEBJ////////////1C6/y7whvYAAAbLSURBVHja7ZlnW9tIEIBFS8/1JgmtrOIi2xgb94aNjcEBAwEChBZKeu/J5ZJc/vrNriQj21pJxvDhnrv5AIidmXdndnZ29YjhrbIuigLIJP5xAyHkl6Sk5tf88Gf+YwvGplT1CA8u5fPwP6RJScmvaUGEXhim5KfVJWN9eHUs4HGieQz2a9KaPxxGRHIbugOMb7Y2cnMIBSXwLvnJ8NiwbkqUegGvQ4HRG4g5GMYaU0TpAKywc8NDPlczYxNFcT6fm8UADSFJwsMv1oW26dTQ82cI3dg8AbzZZFh2AdTIHG5PT08JwvqBPnHIEnj5kM/l5sn8RULZyOX+MsbDUhDNXsJwYWp6+lAQF1n2AhnZNAHXINssqyJUJ2rq06u3J0VhiTEJkOFCwVeoCfBfYcgE5JE5jtAcMRQOrz5VtxG6gGcLRowJ+B20GLaE/LqaHoH42AdJmNV9zPl8hXc7TZjj0REeE+9dfFeoPWmP1/TUQQS38SOb8Ptx4kwAKRfm8loQZ7e9BuK8D6Rm+L8ncxynslgOx8Z+gwd5F48TQs03RExhAnU8WeZbMkxW5tmoCQhK4RE5LBpFIOqh3Mce3n96VPMV/uSwTLCGFPGT/B6PP7i0AeHlv0BOsSUGQG39YNTWMwLYxBGEpcvwz8XtOgE0SanfLRRg5skHN2VOl4TuP64/yQ92d4F8c2fnu1yu0GqSAoNaCWoSl9S0NSgOdI1UEc5RUOJGJCm8UCeL2Gp9+f5WkuuWjA7I9Awkb+U+LhHLIVJZSVmS1lB9C41aIhiRgkGIgUQwn78lc71StGSoBzFPqhjPNSxBlrbI02h7DcA7Lni8F0ShZeseRAfYjyXxEs7h+Wtbi2iBbJkDvAavXuCm4Df35KOWOEdxb9SRShmU6kP5D+ABJ0FYJJW7/opnBGHb2DEa7Mm5fP7ujxxVyCon6OPJu+BHOOl6Y8N/AODxgkEI6ltKpjuIW4rIVm5CB7G01aXjYQZW1Df7ZLamM8B/khsE4Hv0ZJtkZ+qItEWBESf1HfUZ3M/WfLtO/l1ThAm++0vgGdqGShoDpEicJF1BbNZ8vh3Zydp5kQ1CYf5xE3e0p7ilCQIzvIh75E+fm4LYZL5x3KAATv5EHF9QDwUDYLQfUagzsoutvg9ctDTB9AhLsM5cb7e3SSHoEoDR7SactZDpURS20HXmbbumRNENkNUBWWetBTJ14rHOvMEAOKkWSESaCyDe0U1pEsa+0DaZ8i888+YY/tpiyHlcdAGY54GLGieFf2UQ9o+uQC96G9RkOSnLYSbsbQlcF0EvCD9UzQg5cL5yHiVuAkqe1GUp+VW/tvztEWD6d9sJbfnbuBddkT2pZ9oATzmCEH42AMveQk6cAOKeDErLBiDkaUZF1iJFTxEHDEDUU8wlK8BDzFBzUR1Q8ZTVfbZDZM5LTZcJIES5i1Bq1FsIekWECEAxTGTPK+C6CrKRTwUDKqZJYt9bCbkXUrGtXQZA4MQo49ZHrZLxsmECAIhZjBJFjwnCsu82fZAYAJQOq6y3BNGT1BmrwjPlLjM1KztvAafJyFm1S6fMRHrsehBZliIT3e57VSJMyDb6zL7NMeBIKGbjdhohJkaxTZQmZDf/JkHOlFSKQoyJOpgn4tlMlnWUTKYUTziMRxmFPVdRzh/AnrP8D/gvAP79+yB6voAotdmdkcTs2/XZScjmwDGkOjM+PrOyWr3jZH+nurqC9ao0hUjPkWlKerwtqcbqw3S6o+Or6fTD1UbqRCdNcVPuPvTb0hjvlVRqptGYSaVshlYoRdR1bbHIeH+Soqxx58VrAMC4vRd88SqfJ6CCL7/2Wy3Vn/8Z+21mub53y0p/gD37XUAA9jmq9gdIUzJkvkINvAi0DBGAfR3t9eN/lVJDxmus7V5T+wHYXuwU8zWWssx7gwYQan9ioWyF1GA1yi6ffMOxD+HOQAnSAzAAZcWtozqJfUNXXlo/c1FOherptwAb6fyOFj01IU3ro52Aivu5Y9+maW8e5e4vgZSuzaoNJ/8N2lEZ6P3USL1eVKnlmqIexTGbb5mv6Vewh7YI+knPRl/bfSyNONweqj3dey/toF62/xobcbzhpPH9xLhlXEw7qkZon3sDZ3PZClC/J58NocN/F4A/g4tkiHcCDB5DgHcGuKy0q0R4NwBfGeCVRCnz7gB++dSvDKFl3gvg1AsRsfNlC+ArpwgiVuG9A2Ct+1wJJUJxRAP0uSVCVDd0AP8y4DEKJfSSPw0Ar7aHl9xowNGFMwCW25kRDVRcHLgBQJ5HYra5UmKR5+7WHgAkkEggFlUUAoJf0VAgUvFm+Q8uRBooUcY7dgAAAABJRU5ErkJggg==", "reo_emoji_bisou": "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", "reo_emoji_cool": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEX+y0wAAAApLjNmRQD09/n/y0z/zEv/y0z/zEzm6+3/zUt1ZzvT3OLNp0YzNzVcVTjXqDhKSDb/y03/y0yMdz62lkP/00npuUXv6NLGmTD9qjLt3Ku0iSfa4uaMZxOkiUHQ19zhsT1kWjmbdBqCXQ7h6Ox5VgqXnaH/v0D14LP//1Xy9fclKzC3tqz1kxD702z22Zj8///09/l8gYWXf0CheR6mfSDAnETFys37wm/1y43//wD2+vopLjJESk9MUVWAbj2agkCCh4uboaW+kiynrLDbsUj/zDPj6O3z+Pn09/keLS0qKiozOyo/QDVJSSxJRTZFQjZcYWVgZmpuc3V4foONlJm7rYK7v8HBw73f///6nyH4vmvx3KP54J7h5+zl6+/r7/P28d/x9fgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMW51PAAAAgHRSTlP+AP7//tBOrmv/Mf////////8Pjf/9EP//////////////////lv//BP8Dzir///7/Dk//////9v///wE4if///////////wUzb4sREh7/I7jM//////////8I//+p/1+kxP+2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJQW52wAAAT6SURBVHjazZpnd6M4FIZlgwCDwabbcbfjOGUym55Mkul9dme29777///DCtFtCQSYc/Z+yHFs8T7cqyvpIgEabCYLpggh8AxCKJqCbLBdCFjEJREQDEpydcAhRTw0MReSDRAy1QOGUBZwKEDAZFAqBWCVxyY5RQGyCAoZlAsBHBMUNtPL29MPR0f3uYA7CZQyoXHPe3aWAzg0y+mDz37n+dYUEU4zAYZYUn4w6PGt9roLGwAZlhE/+ONgMBjwPNbnj97RAXIZ+R6W7cWA5Z+nFIBQJjh8YChCLfzh7+XyHRlQSh+Eujw/8j/8tVwufyEByumDMDJ8TOL5f083AXLJ9PyHb49CAh/b2TqgrD44QS74Ppz8dttrjaajdttDnqUBBiwLAOi+R23059EOsp7vBRoRR2mAWFofoBGGBKftnZ2HD3cOohh9SAEkUAHgDWLE2Pk1BbhPAhxQCeAPNT9Eof77VCeLVQAnoejto9vetJXUDwECqAQIk3Tk9y7f6x0MhCTg4/XEUjqdjq43I9P0uaI8syb2G7ryG9W+sBTlOAD4uYry6efj4x/tLyPA42aO6R1loqal1YnSie5mGiZm6Mdo9YOGvn/sAz5vspneiUxP/zL19VvBQEb/vnyCf3iAAQ+aVe0nNM68oTu9CSN13kwAvqgMOPdjM335OgQ8TQIaX1UFaN/dtFo3r1er1dQHtPzvvw46WbxobsOefPv9+QucqPwL/IUl+gAD5YTGpjG3VPVayXRmhQjH+NM1AA4GeLOQyqRv+ylqZ8fr6Tf4dr28ljAAT9MTBn0lHAQKQ+PnuKD0AIZ/EcM1kxBgMzR2cUsHAYJpSM+/JhrMLsOoDKtJ0DBZ3dbiiUJjDaeJAMFKmd8J8xigsIYTNoARzl6511gx4DlzOB0gM7udmE9V5nDKIFqLO3kXJWfrvLvpRM9WIHoYsFhHAUsnROE0gcjqtp0E2KzhFAFkdFtLr2isjWECYLHmUJHGyXIxM0aamwa4GmPCJU1n7YG8XuhQihCVMYVyE0mllTkKwywRG3XgPKMXUgrz/We0nmcVgTbhtnSb1lqdM7TeeOxQbWuu65qme6Xjha26mWWpOrFQ0eml1CfU3pq4G/IQ1GoQiPUCRGDWCzCBVC9AAnK9ADlaMmsyI1r0a0oiVFXUmkZmXHjVY0JcOtbUBVHxu27dWTGlWZfcBWH5vtGe44ZF9K84jnRHfvlO2kXochy3y+xEfw81J7ngBI9QhJ8W6BJu4bLIu2PcljQRBc9opDxyOWyLbq78JW64R84hH3AHKUHCV/az5F+Ng2akcML9cK+COBRCAsddUTqju4iaEB2Vos2QfWKm9rnYLtf9mPUXe/HPZC/3490W8pydJKCkGl8Oh/0usv5wnPqFoi8ltnPILqwRqEZOBOgkN6SkrAzMtl1KLssNpi21YZ7+kDqPpgHUTcHZXpb8mDpOnPW9a/raTHdit5sxT29sjmcsPK92ifL9rIVmE5C5tTxbz8zxMGueEu9IJyB59YXbHV4txuOFNxpymjrkI5atVTAy7ZBI2NZCTD2FErauv5VDItIURD3mErZ7/6SDuu31L+WosQoBGizHvU7pYlI6ZDxPFrYUHvqBdZkTWdModORe9MGn4JE7srdSoZcG3v4PX3uo/8UNP2ezIyUKRvWXZxyKH9CU97fzdg5++0dKvf4jMb/+8x/Z4mEEWaitmwAAAABJRU5ErkJggg==", "reo_emoji_tranquille": "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", "reo_emoji_fiu": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEX+y00AAABmRQD09vfXqTj/y0z/y0v/zEv/y0z/zEzt3Kz/y0zn6+zb4uf/yU7/1Enz6c3xuEf702752or//wDU3eL247H9piuvhSSCXQ7z9vWGYRD2lRT4wnP28NxzUQfisj7/v0D+0F3//1X////2+fyfeB2geB2ofyG+kizP2d//zDPyy5Dt3Kji6fDh5uPr7u71+PoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACeH3x0AAAAgHRSTlP+AP/+/89RMa1p/Y7//xAP///9/wH//////9n///////8E/wMNLP//////Bf/SI2XAlAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHrRZ6UAAAMuSURBVHja7Zppk+IgEIZbCSFAQi41c+hcO7P3+f//3EISHaOQQY7d2qp9v8SySD8BmqsbWFhJkJRnGIMSxhnnlNi9uACLMoQPlk+EeUr8AYRmMCNMSx9Amc5aH5SlwhHwhWKwEk5dACUFe80gTACC4SLhdHUJQHC4WJmwB6TgpNQS8I6Do7LSBiAwOAuTtwHEyXKDENqoH2Tx/PI8B3Bs/juktGGM3cjnzYsRQMGxAkWuCGyDUF4U6JcJ4Pj90KKir0Il7SvSjQHgal8B+hqg/VMPIM7ew9BYhXywr6+Bu/2WVeOnr4d6/PyuAazc/V86z2h7bCj2QwPg7uOr6q2uWV3vBmdi384Bqa99hOpu233tCRWjp4DS3f5mtF91221X58Vn1d+NOAFk7gC0167rOkXLJaHKpgB3D5KjeOjZfJ2zHRtHg6wCOQaUHjPok7RXFOuJm8pni48BFDzUolcVh1/tuP70AAFeatQUV00BlVwcVgcABV/1Q61vmlyOalQ1hyVUAR6xN6AZAYUcAozt17fVCPCvwL4ncgVoJrsA8BsDJ+NNuefxJmAACAijOzUg2slfogfQQICnDbprz3ZKEoAhlJqzjZICCIgoIQFpTEAqATwmgEsAjgnACyghqlZA4gII0LiAFHhcAAftRJScq56WqDVFtGcS0DjR1VKn22Pz19oiV3aAh+XyrdevDEUezv1U1z6Gtz+8FnlvKJJYAWrD25/erkFt1/OJroXvJw388V5T5DqB/3KY7QD/44AMstiA6JNd9Ok6+oIjIPKSGX3Rj79tibrxohIQdd9Sht38gnbzu6Axt6YKUF608Fy00JSzR6h6aa3a2EI9wOBHiT0gMYeCZ46x3oDDMdbUzbe29m9nYtmzoYTEUmCuQIhgyHww3j+cY57njgNSESYkMg2p8QizxAQgwp+Qw4U1Z9Mt4BvZn2+gQKFlcwMFCo6bPChceH8m3xUmQXG6EBuTRDS4/UBJIrP9UGkuc74xUKJO5z9/K9UYP1kaP93rmrAu46bcycW3EqiH81veq7C99gC8dL0ZYndxw+vqiUhjXj35E5dnNNd/VLPYX//5DT68JW8O6TKlAAAAAElFTkSuQmCC", "reo_emoji_dodo": "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", "reo_emoji_timide": "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", "reo_emoji_miam": "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", "reo_emoji_fete": "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", "reo_emoji_pense": "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", "reo_emoji_tiare": "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", "reo_emoji_hei": "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", "reo_emoji_bodyboard": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEVUq+0AAAA7iMMiZpm53PRIl9RTq+8tdq5Uq+1UrO5Uq+02grtUq+5Uq+0mbaJSrPRKtfchZZg2hMVDjcdsqdY6h8I6h8KWxOY4h8MhZZg4h8U6h8I6h8IplNaGuuAbY5shZpkhZZkhZZkSW5IXXaIeZJsfZpkA//8hZpkwj782grxLnt5LneSBt96mz+0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACnCqLUAAAAgHRSTlP+AP7+//8v/tFLsf90kf8TEMsV///Obf9QZjaNqgb/FypZlg4LM0ECoxDa10H//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADF1/44AAALaSURBVHja7ZrZlqIwEIbLaBYIm4LS6ow93bOv7/94g60oCKlUCMzN8F8p5/h/VipblcJiYsEMmAH/FJCKStkkABHFIdyk4kiMCRAx9CiM0lEAaa/7lSG8AUEIqOLMCxAosCoaDshCoEgFwwBZBFSF2QCAUECXSp0BAbhJuAGwqWlQ4ALIFMB4hC5AwCAFVMBAf2MeYCx/gJQC8PCHkABIbSacVeLcIQ1Anz9cy2UtKRmnDVILgO0+bPmohHU2VwsA2X64XPZJcmsIQEpw9fUTKWViQ0QYAEmwlJpddE/DutLbC93c9jCAOQGSNaTlev/5uf7Qh5dv64Rjqw2sA8TZg7abtsWnlx/IGN0AiurfJSwWh5/GxQaWE4D1qUuoz28zQDn4M/bOdAMx5iAgjE9Rrsr6wVP/QZsZZ5Gy+herN+XXt+/dro6BbYB4efFfldcHOzeAJQP5aXVTHcLGBSDwDBSrhuqHRxdAjAWQl03/WwTsQAd8RdfAqeVf3BcDHYAvMoO/aar2AWIqoGzvG2QAoIDftf2fx23pSAQIHMB7RsdhqgJyUvIG4ZQTt6QegLKdBLwo8v5N70ABZMhRbNOWAkDOemkl7AgA5LKSaCthYweE2G3CCjjaAch1US/9QwAkx5BX10ObbFMV0At7dXPzDQHQgrK6x/lmAdCCW1NCwI9nwEvW893TBsCXM+AdCUkIAT8XAC+KOSGEnQ/gHMLSD2BTYh0kTwC3hvDkBziXT3gI3019yjDKKIDzYtCOZ8KtXxNQABUhcUtBo51Fax1obJC6C/lXs3SmtSF4Qk7xx/221W6jdjpMWZCv+y/3mnP/2qo5nWTwv1fNlxdseLcG86+lwUcde51YmiOu4sjX723v+CD0vTMiRzK/IjjS8po1a9as/1dqavt4WkAMYlqAQMvYEUYIbyWMEMC52xJM5x/gPbsx/K9903AK+8tP/lDXC+GoyVZh/c+IvwNoKrmn+EBpAAAAAElFTkSuQmCC", "reo_emoji_famille": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEX+21z+qzOYqbT5dD0AAABckTvz9vjBaU5mIRP8yE7+tDrjo1P2ukz/qzLQhlLn6+z/qzL/qzK3hTrSmUv/qy3/rDD/rDHb4+jw1amXq7P7dDz/qzL212Z1NBr1yorId1Dzx3H05a/y6NGDRSGUWSiqsqXUoUr7l0dndn5vjTpolj1nlUaudzWlq6b7vmejbDC4q4y3uZrdVR/atU3OxVLYyX3Mw4f8iTj6lzf/qhz/21z50ZL75ZN1hY91m26KpJjDvZDmXSf6h0P/syj/21f/217/3Vv/3Fzr3cX/41ZfkUCOhzuSqkWwuEzAjj3Uq2jX3+X6fUD1kg78t0D/wkX/21x/n4KIkYegqkevpm7Ffj3CkT7CqoDVsWzf2szgYyX/uT3/213/32D/4F3+4Xf//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABNkRaPAAAAgHRSTlP+/v//AP/////+//79jv//rs7//xQxTf//QEBr/f///////////v/+///////////7//////z///8JjP///////f//DhItUGT/Ff///////////9HK2//////////n///Ssggp/wEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO6ypikAAAWySURBVHjatZgHd9s2EIBBUqINCLREy5LYSpZkecUzTuI6Xo0dbzdtmrRN9x7//y8UBEXyAIIALDn3np8lCHcfDncYB1QRpd0NGg6XMOi2K9Yi6LXADwj2ao375BK0bKzr9CAgcBTSMCO0emPAUTtohI5aggXd1JTrJQikdlGUslgsBGY9ZO5W5oSNXgxoORYSFgntsr505J9kepeo6zgTEUqHP/T9ut/P9JBjKeGljX3a7/v+O9/3sxZrgNMw2t/tn0RR5HeY/dwFewDMJeX8R7Hh0SgBRP2HA5wsDAvK8fuJ1OscEA0fDghSQEMd3M6YMP6L6EMBzpHGAYcmZseAeuwIlQDYBOiqI4wJ/zfy67EPfbp714kBHT8SARgRU6omAKmVoGRkQzbmTidyvnH643AsCQCCkJHAwywvfabHCbvRHTN6BwBDCIjtGwk8U6W1j9GYQHme+n2y+3ti/wQGObHPehJjHgVF+0yoQ5MYd/jfqD7qwzRN7RsQjUKS4lxxmC8DFuKoTwEAdBMZBAu8UAIQqLWU5ih3YQkuNMl+Akksk3EElQAqaJyygXfq/igGvPNH44CiJA2UwhFYCL0AkMbV42MfLSUenPC4cABGSIPgs6AEkEL306VYRhxAk8gzAEU6IU6ahRkgyPNfJb1e7EOUjJupO0gvBIP1EQKAxvF/T08RTgbuIIqsBKRpV+uAPL78Y3NlW4LBFpIDWmIG0e2VpqgHW3I/8ezs7IoYYdhC85X8nzhDK6ybOF3Fllh+Ya2zQstb2ILBfh0KMxT3mhcU45a3BcB8ATBfBLTy88AAmH8oAIEjrT0RgLLWZaHlhdACDpxLAbDMur0QFIstXJ4uLq9pWuCpH8JlvLa8+FTUK7bYLoQ2uFWgxxZ4Mep+JECYlUwfCdBNAUcfCZDf4MNpALVYClsg5jm00GblahB0A8VmSrmihf0ZLgpAKwidkuM4lkSvSJBHgudiaRYPnkIxSUTVJlcsmLM7D7D62kqwxXkQWpgvvygZh+egBdMo9Hc9YlAOUOVK34Wa7vRa7UZciB/rbxXOFITveKV//wGuACjUxr5DaEExBYzfKv5JE21GEkysKisq66WA6/Qx5EZJGGBsWbvRgdL+Tf6cc5utsrzbGrIuEAkcWrbWbuB70W2WV2tzg5nBoEnl/Ce66WI2a3MDpjhXS81/uBZfvK5NGaSdr+J6++tKflK7Oi65LmYLCj8gVW9Vj4L3x5odwrBliJrH9yWvjhVxlRQ3BKIJQi5/VypWgG8VGw5YGULUhSBULAF/qkslnFqG+xQpB3wCRemBYrvFVHoaEACfQkEulJ5iH8WlhwTOMw0CsAfFCCjf8AmoD2EvqgF8Bg38ZtqMiXoYNQ3gHOrvWZxYqQswi9Y1gFVYjrqGWhKuDdjN0wBgEIZuDc6QvN3QMgDWAkAQzt2vcwCrdhal6mcR7ii1shDIgGd5xx13LwcssqIFXsbAdw5Yz396rwXkczR03Z08xnLZBb5zgIfVSVoEZC6ssi/WgEMvc+HCAEijcBB/rmUAwxS99DyqylEVICFw+3GU7YIcW6JK+wqAu/rsfDX5tGeTpjieoVguauvvPRtALjs2hQzmM1QqWgALghXAmxjwq7xVKMokonXAAHBrRFFfYWmz86YA7EhzRGORZsibBuDumbZT8nI6gLtjCPGhNyXAPdAfN97UgPH+l5S3mTTVW9tEgNUerNDT2sTSvg0g3WFrsDZRHV4TA1IfWA3ArTep7fzYAtwfhor4HnqPB/j8yU89+dHkj9ePCnjiHkAEvXj+/LEB8NLEovt4gO9fbVW5bIEn1epYNt78PB0gNc5lPwP8CFo3ticHnEHz1epXGWBTaH8zKeCsKspman9f+mFjMsDZF5KdzIWtqj1BAyjYT13YL/xQnZ8A8KpopvqlIgIGF8oB1aqasL+p+qHUhf8BvH6MHw0KmrcAAAAASUVORK5CYII=", "reo_emoji_famille_1": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEX23c0oLjKYqbT5dD0AAABckTvz9vjBaU9mIRPao4/o6uszODooLjLqx7VHSErNhm7PuKzYxbdXV1eomZAoLjIoLjJraGayq6aQi4i0hnfc4ucoKSwmLTEnLTEnLjJwdHazpJuwtrqXq7PLyMX7dDx1NCbMm4g9QUSVlJNllUaSm6I6PUGCRjfX19blzsDx49qEfHeLg33suaP/5tBgXlx4g4nGc1r5eUX2mHBveoJvjTqMV0fytpv23c2WYFGgbV6ndmfdVR/KfGT8pCfmrJX5yoT33c4cHBwkMTFcY2dvRTZ1m26Uqm2KpJisWTjUknzAr6TZ3+PmXSf0hlnr07saLS1KOTRdW1pfkUBjYF6OhzusgTy7j4DYZTbCw5v1kg74onz7vmX34M0aMzM0ODsuMzhUX2ZoZGN/n4J7oFiVUjiBeXSNg327fzygsnu5v5O7v8K8wMLFfj3LvJXf0rfrbzz4jWH9sD/9sUL23cz33s733c/33c744M8AAAAAAABAQb+zAAAAgHRSTlP+/v//AP////////+O/v////79/a7O/f/+//8UMU1r/f/+QP5A//////////////////8S//////7////9iv////////3/aQkV////////////////Dv/U/////////////zEKrdz/y////8zS////////////////Hj5b2koAAMjshowAAAZ6SURBVHjatZiHd9s2EIdBUqItUaQpUhIZ2ZbsqrZk2bK8V5zlOM5eTdI2aZIm6d57t/97Ac4DCIK0rPzes58E4e4jcIdxRAVas61KTfJUr7RmC7lF2c2AHxDsNRP0iVWZyeNdZAcBFYmjWjZCaBcArs9WanWJr8q0aGqy7BB/iLTSYjFdEdu1fEBWt7RB5LCrPcGAGSmH6jeSk5PW1+qU3chuGrUkaSRC6uM3VLWsbkd2SMqp+pM8/pf3e6r6UFVVLWzJDZBqmf5vuj25P682sX/V1U4NgLnEm3/NIY4HHR/ghIRTAKQolaa5z696KpfL5H+/3z49oBICuMum7T86CbGqNvG/zvJpAdJ1wQAky3ft/y+TgQw0GqDZWYAWP8K2P90DtUzGcO3P16hJAE3VoQEu2spKVR/AtBpozp8j7L7ZfHz146vX/LlSf6IAFkLIyhNmdumbCHljb/R/xLODAGAbArqrGIAaOTKVWfs2sZvDs2Q5Xgyu/fF64PvvwyAbVeTJNjLziA5Bz7erNqSuH+Om9zcYdLZhmlooEoXQOKu5Rq2uyM50g3Xg/XvY7y0DwDqCMteiWFiO22WjDADhuD2Vwxz1hjB0tAigzaGEqs66EQzN1tIADcpkiB8cLzAvAA/VMlo1AoBmIr7mDD+G1XjSKEAbMYBoivAISGye+oA5lCqMMMhwNB5gK9F9WC4Phx6hqRqmn/aIGScjPEwyzQ4EBFmkVdOMCGFeWiMfDQyoigBINxywPuoAsJ5uNCwP0Zr34KaEhAMgY/ATC6RpsNBWMwz9BzdQFOHFi5eZaOMWPfxsxIAZOoP0yxcXmVGDFjdunZycPE/3gy1tcCLEOwTRedxNpwxhS/zMNm6dpPo9hy022K+9q1wUOtLrHGVIWp4npuxcAkC1+Hk0E58HSAw4d1qACY40cuRrpwaYuHUlvaUKDpxpCrCCu9HZkWzxdGlhpSRogad+HQJKKwuXaLtkSx7Bm1ENAsYleDFqvSVAPSqZYBaNEdAKAZ+8BUAVXh1JlKsjuyoRbbCtjpdD07O4XK1UWnipPWB7bHiGabsl8D/hie22jpdxBZZ7FjsE344l6Ig9z/QpokUW8FRKFJOGTe+9nqHO2NmZ54GnB2vca5LxINNyC32W7X5dS72JZT6ehm7YGV3mNNFdzzCFxm4FFTbF/tsZ92FNRFj9lBTiF0T+jcyqRBOsiG+9Sn/zX7gCoDZWjRx1j5GwC3O1GryreBMm2gQjfStXZdVg7ULAX+HLkH/oRRZoR7dz1m72Dtf/f/HrnJNolVHdtJwAAw4+Wmsn8H3RSbSQS1M7EztH9w9JjlFOugICvv0d3z/amTiaKkVL+YR+4/WGkwOUS9cRRSFp/Df7Sm3zAm+HBrMQ1JJ8sbYXNjnv7FgEdKiRkTvpMTFT3DNvHQtUt2/AWxrfQTV1WfSg4WahkAvwRbz3R5FzY4QFi2qq2CnkBHwQWq9R1zF3ywg2Ib3BjzLt8h0oLqDH2WHbOBzLmLYsJcpghN6FQjIU5cUSVjL4hZMbV28QoCtQAkAj+WxUFneNuPSBvQ4FgE7yJEjfjHUrfgwYg2MBgPLm8mtV9laeyKI9AWAemspUpZSqLhuoXQEABmEgd+EMsSejSYXKTosxCwBBMOXP400GVzsLTPUTfvduNFPxT6+EADBHjrwf39IXcNECL2Pge48AHqXNEAuI56gjy/iNVTel7ALfybH3vvI4uqIqYkA0hHn8RcsDIJvuLWUv/OVRBiCMQod8Nsh2EE1JiZmiUgy4pygbvBzlAXyC51++GcVAEGRy0v2mKLs61z8HIM9j+Z/2wVGVmqY2mSGiR6/2dpU8gFj9PIWM681QqoQAvNTMTMCapCkjA/bZw4DcC48Rs6vfGx0gL1uc+oquYvAiOAOgzxTcOhFdI0kvzgKQe1nbqfW1ciaA7GTUP7eUMwLoUy6h88qZATIsbyMFW+miMgbAPK940Llb52iAkHAcuz/y/eu74wFEe3jJq0927gc752EO//kAco8X3z1FGRtgez+RrYcv3hsnoN2m0/Xw9ytXxg2AFwJ8NRkf4MvbS0VPSzHgl2Kgg2c/nw0QOvcUHz53QOvBd6MD7kL3xeL3EYBufzYq4G6RVjRHL5kfDkYD3P2Q8VP8IQB8VcxPEAAS/sMhvEz8UPxoBMDtpJviHeL/8VLyh4MRAEWe7vyKqku8H1KH8D+0GrGSHbadDQAAAABJRU5ErkJggg==", "reo_emoji_famille_2": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEXy0qIoLjKYqbT5dD0AAABckTvz9vjBaU9mIRPryJnWm3Y1ODnUt44oLjLl6u1ISEXNhGSrlXhYVk/ruYsoLjIoLjLMq4VuZ1iVh2+4o4Lb4ucnLDAnLTGztbAnKSuGemUnLjKXq7OyhmX7dDxtdHXHdVholUaqd1iiqq7bwpPpzaKDRTCRm6Lx486Gi43VxKg+QD5xMB54NyRiXVJxe4KPlpnX19T5eUPziFTo3ctvjTqSXEL3mmYcHBw7QkdzRDNkamx3hIyPUjqeaEyxgF/dVR/bonvGvqrY3uL8pCfhrIT10qHy0aEkMTE4PkNcY2d1m26KpJisWTjGys3mXSf5uW333J741qTz0aPz0qJKOTRAQT9bV1BfkUCOhzuOplycqmSsgTy6uXvYZDTEuHz1kg7xpHLy0aEeLS01ODkuMzZUX2ZnYVV6cV9jkz9/n4KAc2GOgWu7fzy0oH+7v8LFfj3Mf2Hrbzz3k1/9sD/9sULy0aL/5pkAAAAAAAAAAADpgiRIAAAAgHRSTlP+/v//AP/////////+jv////79/q7N//////8xTf4T/2tA/0D8///////9/////Pz///////////7/////Cf//+P////////////8sjBX//////////xAWUGT//9T////////////82xGl3P/L////zMn///////////+yCgAAAFU8wHwAAAaISURBVHjatZiJe9M2FMBlOzFR7MSJ0yZO2jQda0tC01KgJ2eBUUrLzbg3YLDB7vve/vjJko8nWZbdJHvf13y1rPd+0ntPxzMq8DI7X5nSqExX5mcLuYXTmwEvEOw1E/SJpTKTx7pKDwIqmkSmshFKvQBwcbYyNa3JpTKnck26HkMg+RR5SYvFXCVbD2V3S5tEHj0fMKPlkOnbSeek9XUfVlcjvTk0r2kjEVKHv2uaVfNKpIe0nDL9ZR77d9Y3THPfNE0rbMkN0KYy7d9d3dCHXbND7Jur1pEBMJdk/rf6vuHNhwzQDwlHAGhRKs1Jx29SqVar/u9wuHB0QCUESJfNAhu6H2LT7FTNav/SUQHaRcUENJeZZr9VfyJVhwdYXhZgXh7hOnP3pln154D/frTT8QEds88DPORmpSoDCK0OqjMfEfOdDrr5xU3MfGV2OYCDEHbzhFlc+k3ECLvDX4l3dgBgFwIsjAjhbI5MFdZ+neihNvGS26cxwH892mT2V2GQHRtRqTuZecSHwGN6dku7xGLcoX+b+w/XYZq6GIXCISzJaoZJarUjPdsL1gH92R9u3AGAHoJi96JYOG3PEqMMAOG8qayEOcqmsBovNKuOEmK3e3QmLpmSlQZoYcQBSGpWTRqAfXMH2W4AsGwkl7bDYmjHTuMAC0J/OvaVFTaDDdLwHQPUUaqQeDj+dCwZ4Gyy/8rKzs4O3SpMh2QvavmAFlIIdjR/fm0ICLIodeI0GF0aV6KONBupCTRPzoIYBICeQmsFoR4deFNDygn4BMw6xmkaLDScocgG7qBm2FA+f0KYDGxxYgDbKqKB2SfOlwXToMWLR1oqlZa5fg3ScjV8WAAnQrxD+HKVdGtwirAlHvNx0lrips211MF+Ta9yAzCw0nHOqYmWPACWRzPxecCZOzE+wAZHmn/kW+ioM2iS1suJligqNjhw5iAALZNuTU4x2ULl2unlcnoLhqf+NASUl09fE7Iv0ZJDMLwZTUHApARejOb/J8B0VDKBLJqU4PjWQuqhHDvFUcWGV0c/yoORh7pXJnKQOHxoDs3NknK1UpknS60t9jjw9faSExNbyseoiM09sowrsNxzhZ0RMz0h09EAiedZo+aL2I8cCIli0vH4kVHFhrhBZJ4HzEE96TXJaWdquujrzHTAPSv1JtbK0MYWul3PsF+3VHc9R33iehVUeKweQivjPmw1Vdpf+YX4LfWtIkssxRx+opX+v+8DY2VRDnLYJ15qJhSDyNjBt4pDfgnEknWbDyMt6oVJfhh+DHkqJSw26jlrt/qi1P7T+HPOs3CV/Q66YWzlBDgYDK2Gof3we9GzaCGXa4vHFhdrB6QbVxQ6awpCG+FmbZEo1srhUn5/yH/xOpTkAGfSa6uikND954n4Se1xIlsHvBeQKiLign4m+yj4REBAg9YgqPRShF9tt56kfHUscN1+TCxXO3VZcBvr40IhF+DbeO+PPOC9iBudtCAUcgI+CbW5SsD23BfBrAatPIAPoEgBXnKHqrcsWro3w6i48PWHUJAO5SR3VigrGVLeenH1BgENAwoPOAVN7CbHxvlqzYlLn5EArOZI34wxtdpKVJzvFIAuNLCqnAB37eaCvJ0XoHOVUqqsiYHaUgBglE/pl4CHsHgNip6pj46nhUAEgCB09W/iO+5HpdIZuN+AZ3qjqcWvLigBwEd9fT2+pZ8mRQv0Fnimm/p2modEQOyjU7o+1LS14Ems9MCzvyc+N3CKhxKAbuwhXbfyAi4bF+Q5lASEUbjh/+9ELjpDDML7Knj2D6IHhtGQRkACYARqX78bARRB9gF/GMZWQ2pfAtC73W6f/bceH1XpaVr3PeTL9oU/t4w8gFiGWsbHniCLHhjpogSQpdbMBPQ0yxgZsC4cBvR2KTBd5QQyAPodV1JfYb78fG6MARhavLWGL8Ld4+04AH0jazt1rxpjAfT+SaX9Xy4bYwL0G0rAeWNsQLD/4RonwT5RNiYACJy0x9cm0q1zNEC4wzZBbRLY35oMQO8GXtqrUethDfAoh/18AH1DVm9vG8bEAFfW22K2vnv78SQBCwv6DYhobF+/PmkAvBBgw5gc4Id7S0UqSzHg82Ig517+Nh4gNE4l/or2GrSe+3l0wH1ovlh8HQH49pejAu4XeVlKeCicxGiA+58KdopvpBNQExSAhP3iEltvbxIvip+NALiXNFN8RQv075Mvzo0AKMrk1QDbS7IXqVP4D/GutqpKesBoAAAAAElFTkSuQmCC", "reo_emoji_famille_3": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEXUqocoLjKYqbT5dD0AAABckTvz9vjBaU9mIRPKiGo1ODnJmXlLR0TGeFsoLjKqiG/l6u6Od2W3lXgoLjIoLjJ2Z1mmqalYU07b4ucnLDAnLTEnKSt4NyZlWlAnLjKXq7P7dDyYgGyia1Fmk0WqdFn0eEVpdXyHSzaVZ1CRm6K6qpvQon3sh1iRWUOJjI2wfWHY1tPgmW9xe4JvjTp4hY2Qlpuuom/Mysnm2ckcHBw7QkdFPDlBQD5cYmVnbG+KmVbdVR/UrYfUq4fdxrPY3uL8pCf5yoQkMTE4PkNvRTZ1m26Jcl+KpJisWTi0tbXaqoXUq4fUq4jbt4PYs5XmXSfiyrdUTklfkUB4aFmOhzusgTzUq4f1kg77vmXn1L4eLS0zNTgtMjVeVE1UX2Zhkj5/n4KVUji7fzy7v8LcXirSZjvFfj3If2LFn4DUqojrbzznjmL9sD/9sULms4Do498AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAffwUwAAAAgHRSTlP+/v//AP////////7//47///7/rs3//v3/MU0T//9rQED////////////9//7//////f///P////8J////+Pn//yyM/////xX/////////F1BkEP///9T/yv//2////xGl3Mv//////////////7L/+v//Cv8AAAAAAAAAAAAAAKaJ0GEAAAZASURBVHjatZgHd9s2EIBBUmIdkiJFWdO2lMpbkbfjveLYmXYz7KZtmibde4///0qA6zAIwpJy71lPhnD3Ebg74I6oQMtExx3XiFTdzkRBWSi9FvgBwVmtaE4qbkvFukwPAlxNIOP5CKleBNibcMermljcSdnWZOuFCCReIi1Zvph08/VQ/rSsRajoYUBLU5DqI35zsuY2dsorid4k6mjaQITMxz82zbJ5N9FDmqJUv1Sx/3hjyzTPTdO04hFlgDaea/9oZUvvPTObgX1zxboxAMaSaP+tOja8thMC6jHhBgAtCaVJ4fObRMrlMv7s9eZvDnBjgDBt5sNHxy42zWbZLNf3bwrQ9iQL0Bqh6fCzjBdSdmiA5ecBOmIP++F2r5llvIaH/7zdbWJA06zTAB818kI1BDCjh6gb7lFgvtl89+CLBw/DvTKfUQAHIeSouJlNfQ8hsvbj3k/B7uwCwDEEWL8HgLw1kEhlct/Hel6wS4068cHDv9+uhfZXoJMPK4iIb+XGkcvbR6jS0PZDHzfJ39r5zgYMUwcl4sN9sgTZDIPU8hK9ih/lAfk47209BoAaglKpJQzHW7RYLwOAYwO1V3GMkiXsdNNEs7qIk4oXUhxq1xhAm1J5FTx4kGDEAefmGqo4EcCqILF4TrjHlZRAAeh1o2vy7Ltr4Qq2gpFaCOiiTOkeEO+kBAhocNPP3u2ene38RwAO9k4bAxpIJo6G1+dBQBRFlp2hcr1LcqwWqiPNlgLsQw/kRxUAatlK16/OUI08uKehNlIRD4RplGh5KqFnHZQE8urCMrOY1YVFO92qBNCiI8heXphlVr24sJpkVTo6Nja2QM+DIzVwI5CvSWgsBNPoJ4MjaYTOBqNj1DxqxAfnNSnlEpt4Fr0EfgTLNAegRkIntNL7gDI3zQGmOcCsHFABVxq+8q0bA7xgdCp7xAYXziQFmAqmeZQiP0JkeWxqlRtJ58FbvwoB3tTYMhN93IiKwMpoHAJGJbAw6rwnQDVpmRQSeRBAJwbsvQdABZaO2Mv2wKZuYbEFp10QQ5MTQbvquh2XFCvMCUQUFex/QIQdDs6ilgvbPYe9B0M9lmAj9j6zS1i4J2loXDPp+PSTEUV26b7afeDVhGWS4+VqOujrfPO17GIs9/Es9MjPmdKV1nqZJUn0bC4qPJfbb+fUw5Z0m77Cjfh9eVWRJ7I1fEY6/X/fwAyAYivYD+pmTi+OQTt6V3FKp0Aq/YZSZ9Vm9WLAafwy5IWQULJ9xd7NF9t/kb7OeZlkGTXNUgRY8NGSXHsB3xe9TE+UUgApkcOIWoAlowWRZP+G9UrJKfbmlH7jdSpKEmij5sm8wOn+ccW+UnvORatNnQoo6iXFwuq+FL0UZBHQICmlvexdonPh/lXGW8cCnSVcMlUOMuMIKl4VCkqAbwStGGinHJiEVC1fUAR8ItSu+A0rWpXdFnuZNnkbihAgOG67bYtULolXHPjrh1CQDoW5xGSdTNDeXqTdGwTYBhQJ4Ih/NmqvLCdtfeCsdQngDrRwLAhAKk+c9L6AneRfEkAdGrgr7lUFBRPt5CVVgJ7hYdGBAh01JwFQTtD3YadkcwUPjIWLLB+zAOCEuv5teshMM90J+J9UNLNZO8QCwB7p+kZapbN9HfifHOpzWTvEAnQI6NGARQawmAIOjL44SHlAPd0hXbdUAPjQfWIsZSyAA8ReuIO/OwkA93WrTJ+3mja4HxnGutADAkBIIPb1owQgcTIG/GkYc+tC+wKAXg8k/LYBrqrMMPXxDmGZW1qaM1QAqfRkJ0UsF2SHMkUKCFItv0CvaZYxMGCDPSoE7ZUjXUAOQH/sCPqrPt1+HhhDAHpMw21joXsk7ZdhAPpW3nHq/GAMBWBuOb57e2IMC7gjBSwbQwPiJZQoiUp0zxgBoC5qHvqiy2VAQEywQQ8Q2Z8bDSA5w2+F/UmcausK9tUA+orIvyXDGBng7jyHuPXzxyMFzNPhur50796oAbAg6BvG6ADfP50pEpkB5Vwxks3Xvw4HiI0T2U4AJ2B088fBAZfQfLF4kgDo8deDAi6LtCR7tM38sDkY4PJTxk6yRzNFdYIEwNmPl7DN/VD8fADAU95M6IX+d/wPmwMAiiI56aPtGdEPmUv4H4uuphbo/kH9AAAAAElFTkSuQmCC", "reo_emoji_famille_4": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEWufVYoLjKZqbT5dD0AAABckTuQWTTz9vhgNSqPZ0k0NTagbEVvWEVNRDwoLjKYYjzl6u2bclEoLjIoLjKKXEFCPThxRjTb4ucnLDAnLTEnKSsnLjKXq7POeUv7dDxsdHhojTushmijlIZTS0WQhEuRm6LpdEKTmJurgFh9YEmFi4/LuavW1dNxe4J4hIuip6scHBw8QkdVWVxaYmdmbG+xXTqufVbdVR/JysvY3uL8pCf5yoQkMTE4PkNMQz1fkUBzi0JjlEp1m26KpJi1eVWufFaufleuflazgFWskXrFpYvmXSfm3MtgT0GGTTeOhzuufVesgTyzt7vMZjrNsZzSwrT1kg77vmUeLS0wMTUsMTRfTkBWVVJsVkV/n4KIeWu7fzyvflaugFe/gGCupZ+7v8LXWSTFfj3jbDz9sD/9sULq2b4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwhfFzAAAAgHRSTlP+/v7+AP///////////47///6uzf////8xTRNrQP5A///8/f////7///r8//////8J//f/+P+M//////8V/9H//////xcsUGQQ/////////9v/////////EaXczt/J////siwI//////////8AAAAAAAAAAAAAAAAAAAAAAAAAAGk/O/sAAAXmSURBVHjatZnpV9s4EMBlO4kjY5uY4CQkmyUQkgCFcpSlUMqWLeUoS49tu9u973v//+9rST5GsmwrJp33ygNZMz+NZkbyuKjCy1LPXdCoNN3eUkVZOL0OeIDgrE44JxG3o2I9Tw8CXE0iC8WIXL0QsLvkLjQ1ubjdvK3J1mMIJHeRl6xYdN1iPVQ8LcsJFT0C6GgK0nyc3pysuftHjc1Yr4t6mlaKkLn8A9NsmPdjPaQpSvNrFfun2xPTPDZN04pGlAHaQqH9B5sTffTGbAf2zU1ragDMJdn+WzvE8NYRA+xEhCkAWpxKXen6TSqNRoP8HI2Wpwe4EUBaNsts6STEptlumI2dvWkB2m6OA9o+M81+NogjjSEPsOwiQE8eYZtt95bZID6c/Pv+tk0AbXOHB9jIKUpVBhCjizDbo8B8u/3fo68enbC9Mt9wAB+hQgINs1j6GCHq+8Hoj2B3bgHgAAIshIoJNFOF2t8gejjYpf0dGoOTf95vMfubMMiWRwFowyrMIz4ENtPzHG2PxbhN/20dH23DNHVQLDZEWJJqhklq4VjPWw7rgP44Hk1OAcBGULDtx4HBHK8pAHwPqL2LcpS6cA8UGlhGsp6Q4nAuCQCHU7kJFh4UGA3AsXm0jp0QILPPPPGZc15C4AAv+OkrdPVbXzIPJsFIWGhZ9llykOxKCBDgiLPXb+4RuaWAIWZJidLzOLE0ss0YAlw+71KYFeLD7yyufgDwUD4Bg/poAoCdrfP83Q2y6cKxhvIdiPcKpGlYaEUqbOE+iiOAWzXRKhixEkBHiECtJUYRjAA/6/V6i58HR16AGyE6gZi0gmm8HhxJ2LguTlyEIzY4r+mrnAeWUV8UFyaMpMylR1gQOsl9gD4IYDe+8q2pATgVA27EAxdOlwOQHcepGEiqt1YXs4Ebgbd+EwJwq14Ts08cURH4ZrQAAbMS+GLU+0CAZtwyKRRyGUAvAux+AIAHXx1JlL3SpuaIyE67IIe6S0G76ro9V3aLyBXT02pUxOHgqOi4sN1zRBeYXpqbGpknkhp1tFQz6WzwhqhiamFq9wGWv7Y6xYFw0LfF5u3slzG7MPnQ442i1ee+6xVsgO2iyrP8KcOC92Erd5u+IY34Yd4Mv7AryTs0fqCd/vVrmMhQoqs4X3wsUWTVGX6ruIh2uyZIYb8QxkHUiwAX0ceQSzkB2Yq9G5bbv0w+51zFVcZNsxQBPlxaXGuX8HvRFShIMgknbxJRLPNowfS5eaoYH0avf+W/eF1I30thSeGpquGXa/GT2rND2QkNW0Q8RapeyT4KiggsWsipaf5wPLzO+OpY4aZ9l2rFPEvpTPqtUlECfCrZYnDuObDIh1CxMi2AW55nO1bk1VAeZd7kR1CkAMmRjIcWjUscFR8+/RgK0qGswHnf5x75wWaB/pADGFByAPv5B75n+UmqwVn9HMAqtHCgcX2A7DqMu7dSgE2FGytyAWbROAegQ1Vd6dJlB4qdFQIRAIKwou9pKi9wjljJuQCwR6v6g+QVdFFof8Df9MydywqBCJiAHdK3k1OsLjQt4G8KGGeFQAQke7Si6yMesChvwwjAN7IcSAH0xAFdt1QAJI1eGuMMB9KAMArPye9DlS0igE8Moy93IA1gBGo/iLJVHGQCIJb6UvsSQIBYDX/ZVmlkNjStRU2N+/2xoQSIZaRSB0GQ3xrZkgsISg0rAHyjNGBbPCokbZJDQlwWoJ86kv5K6ABaxh0AI6u4O/n7LgB9UtSfOLkbVAzgT3DJdfDSuCtgNRdQsH4VQHT+zXMSpu+cMQOAvg479Bps1PvGTAATJBLmpZdXaUAc6Ll57nOBwvpVAfdl8X1rzBCw/NO6aP/Pz2cKWNZX4Wtff/zw4awBXMkZxuwAPz79rErlSWJ/rRrK4NVfdwNExqmspQGE8XN5wDk0DwEDbvxVWcB5lZeBzAH6oBzg/IlgJ3bhrKpOyAGk7EcurKUeVL8oAXiaNlM9o//NNEg/GJQAVGVyto7WBrIHmS78D+Vpk76BdB0IAAAAAElFTkSuQmCC", "reo_emoji_famille_5": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEV7Uj0pLjKYqbT5cz0AAABckTtpRzXz9vhKLh5OOCwzMzRaQjYoLjLl6u0oLjIoLjLb4ucnLDAnLTEnKSuSm6InLjKXq7P7dDyWVzutXTp8V0WJiouQlptpdHuIenRrizqFaFnQZzxzZjxoamtyfIKmqKphPix4hIyrmZDJysvW1tUcHBw8QkdTWFpaYmdeizp7UDx7Uj5peTu8Yz22tLTdVR/Y3uLkbTz8pCf5yoQkMTE4NjY4PkNDSk9fkUB5VTt6Uj18UTxjlEp1m26ATDeBXEmXgXaKpJi1pJvmXSdNLyBMMB9EOTV7Uj2GTTeOhzusgTz1kg77vmXp3cceLS0tMDNRQTdOTU97Uz5wZF9/n4KAQEC7fzy7v8LSVCLFfj3AsqrHwb/9sD/9sULq2b4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfedc1AAAAgHRSTlP+/v/+AP/+//////6O/67N/zFNE/5rQED+/v3+///9//3+//r////7////Cf/3//8sjP/9////////Fdb///8XUGT//xD/////////ztv///////8Rpcnfsv//CP///////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHDR3V0AAAXUSURBVHjatZgJV9s4EIBlJ5Gx7Fwk2U1IOEISbgp0KZQW2rKlwLbbdrfd+77+/29YyYrt0WFJJHTeI48o0nyaS9YYlUVZ7MQ1L5F63FksO4uwrgl+QHBWczonl7jpot20DgJiTyM1O8K4bgrYXYxrdU8vccvkmuJ1HIH0JopSFItWbF+H7NOKjHBZxwBNz0HqT1TnFM3d3672s3Ut1PG8mQiF2x8FQTXYzNYhz1Hq37noPx8PguAkCAKSjjgDvJpV/4P+wG8fBw2qP+iTOwNgLun8TyZM8c42B0xSwh0AXpZKLe3+g0Sq1Sr7bLeX7w6IU4C2bJb51lmIg6BRDaqTvbsCvF2DAd4+V80/q8yQ6oUIIJEN0NFHOOLu3gmqzIazfz98bDBAI5iIgAgRW6pygBxdhLmPqPpG47/H3z4+474KjgUAQchKSMIslz5GKLF91P6deucjAIwggNB5CIUOmSrVfsTWMRv2J0kMzv75sMP192GQuX66F2LNo1jVTwmht8dj3Ej+dk62xzBNCcpEQBBNNcMkTffFEKNpHSQfJ+3BOQCECAoOSa5A4NUlANCP0Faao4kJx6O80IRpKWRKIYJJEkDc1xbdOC2wbQY4Cf5ewmQK0OnnEMJ9jHOCABD1o1fJ7rePuQX9acqgJM1QMYIgSIAAIs9eur693bqd7CSAC8wJSN6HQsDTLMwAscb/0JC1vyhhi+slFICRmQDrow4AUfGita1rFIa8PpDRADYFodyEGig07LSQIJwnZyitgSMkBzTFCJvX5XZitRzgSAieCKKHQsUaOIIFdZ4CyEYicF7XBQ+p7tI7MFIAwggPQjN/HgjqIgWgpoDFAgweaYtCEegBWAswxACDB05LAJhjAIeVbBBG4FO/DgE0Z0Ili2zJrxF4M6ppzom5BV6MOp8IUM9aJjkf7gnQSQG7nwCA4dWRRRnPrImLBkBzqLVI29U47sQaQMFCJI/ghUSwWujNuO4VPI6Z6NdhJNc0S2JNHoee0kySSK4atZSoeqeSwPoLGbEHgqCndvVh8WXMuj0PPYksU8x3PYsRUYzKzy3bt9yHzYTvWSN+ZPShtSsxEX5IOv2rt2ImQyEOfQ9Rl6UKp+8qDqffNxYkwaFTZxUq66YKD9OXIS+0hBBHjr0bDrX6X+Svcy6zfM+nbbgEIL1EbsB9Qf3p+6LLrKQ2wnDhDa9IwQBiomF2Gw9fL9B1qfq3h+Ibr0NbBkXYFAVl7U9X8iu150faewZoESOTjyS51L0UlBGRnOyGpBVr4eiq4K1jWZj2tVJMxQThvPm1XL4jIC9WcDAJUReCUHYEPNWupl0hSQs4dAF8BkUL0By3ETvBCfCZEOXPoSAfyhKc96PxyKfOAv0hBHRLUETAGlSxr8/AvLkieS7DWT0DYAVqGFk6JUzy5wU08wsDoA8VbBoNEMsRAoYGQBsu9S29JDxQ4LSSAQCjvObvQQ/hovtUKDmyawSAIKz4D/IraCRlE/ieALpFIZABg3ziwB/nIZCbFvA9ObKG+U+nRkCeqGs0IjlA9jP4zgBhqatPUhWQhblNvxBXwLvSUB9iFZBGYYX9f+HiIpandNs9bQQ0AE5I9LMo24PMAExTT6tfA/Db/X6b/zcGjUxhmlIWTlSdDoenJRcAQLk0MhQwLBWLEUBLzQ4IaQ7NDBhLR4WuSyJeb3aAf040/ZX0bgWX5gC0ic2CiJzOA/AHtuOUGB1kB0iPUfVx8K40L2DFCOiW5gb4r2B7m4mjfhdAewl26FzeYEf9LoD0IYGVHsBBvxPAHyylb+SZ9tdpi9Er3RfAH+tSyUm/I2Bz+WcZ0f3jq3sFLPvX8NrXGz56dN8AeCGg0b0/wC8vv6wk8iwHrFemsvr+z/kAqfJE1jPAQzC6+tvsgBuovlJ5mAFWhfH3swJuKqIcKB5KjZgNcPNM0pP5aLXiTjAAFP2pCevKD5VvZgC8VNVMo3Cg/rA6A6BS0RPWD3Q/FJrwP2fdg9eSLHo9AAAAAElFTkSuQmCC", "reo_emoji_iaorana": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEUafokAAAD7/f3S5ugqh5FnqrGz1dhaoqo6kJlOnKTg7u96tLqHu8EafomUw8gVgIgcgIrD3eAXeo0afokafokZgImlzdEYfogYfYkZgIoagIlBlJ2BuL7B3N8afooAAP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMK/nbAAAAgHRSTlP+AP//////////////r/8V//8ZktMw/08zQ2////9+AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADfkaXIAAAIJSURBVHja7ZnbktsgDIYFAp+Nz042yW7f/y0rjHETQqeZ2ehiO/wXmSAjfbIk3wAIZkECJEACJEAC/CDAcmlneKPm9mu5A4wtMKgdPeAETPpwgA8ARgKIERjVEaDlBLQCFmDVGSZewBfMvADm8ElJSUlJSU9SWmtWQC5l9V8AVCalHBq1W/tmkBLXgh4g6itKBCiRTJmvp8EMNFlW9ewdAZTSKdut2b4uoZDy9kmRQe+m2u+o8m29PntHABQw0zfa45Ko6V9T24wtoLHp9fRjtLEmn0KGqw3bh94xQFFn9BBtylZUnxu9OLkUBEAslYLSrM50ALDf1ir0jje5NINNx5W4cnvJRRfS+yltUB5pEsD82fngHe1BZRuIfwEcZdtqcgAatyUPvSMAW2CamE+/BV0vyXr1AGrkoPaSBIDQOwLYqr3l6LbYture7E3eADREqProG4TesRJtU1bVfggV7oOn4e4N7CBS3OtTiQLvGMAOORa5c7KEYY9/AMDY+Mr4lt8DQu+YCp0/DvFV67x/sJS6fNk7KSkpKemHqOUOf+EFXKDjBYwgWM/UJjp17LiPNTkPZhfmo+WTPxzvmA/HSee3t3pa/nFBEc7z229AHuOfBStgXgQroO0EK2DqBCvgxHTNdfcxcgLmUbACvtXeFwDTL8EKOLHeZX7n630JMHeCFzCKdJ/s9BsF6R0VbCYwQQAAAABJRU5ErkJggg==", "reo_emoji_mauruuru": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEX+qzIAAAA7Kg/IhyiRYh6wdyRqSRfnmy1UOhPclCuhbSF4Uhr/qzL/rC//qjFALRCbaSCFWxz/rTH/rDH/qzL/qzJeQRb/sCy9gCf/qhz//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAArqnejAAAAgHRSTlP+AP////////////+vGzT///9KkNNx/xb/CQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACqX3RcAAAHxSURBVHja7ZnbboMwDIadpEmAhlPpYdv7P+jsUCrD1lIJPGmS/xt+OcFfYsNNAkZYoAAFKEABCvhHgOaSzrCjzunSMMAtgYBSPQFOIKTTCBDLD9AQoAZB3RCQJAHJQAOiamCQBQxwlgUIp1epVCqVakW+IO2WznVd57OLd+ctaTfA4ZGtR5MXHkn7AvIWigfAVy4/XX44F7ONvluG7hbIflQlDzFAG2ygMBkCHO2diWxHcXvAshW0AB5itrS2xLccC80AWPSS8vYZcLU2ULXiAkCteQ6g0WcACy1FWusywIc+N9rPAW3oXfUccAzex6eAHhNTEcYSYfou/ADY63327wAb56NzAIZw9dUIQIfNtrZaALqXgACvANi/QGsgAG030qQKqqnVh7FkKBZilt5ZjC4Anc1ruOZS4aQYCIC2iGUIDDAPTXYCsNACEBHwQRvJO7ChyNuM+XutOICFmJ0ALDQDYH/G9hIg/9AeLX1LLW3syAAsxOwE4KMvVLIfsXS/DL85qlKpVKp/oiSd/iILuEAtC6jBiJ6pDdLHmvVfHMzKHy0bUwsfjtPx/u6tHpqVC4rl97z7DciPbkkCzrURBaSbEQUMX0YUcBK65tre3rcAW9r7DiB9GlHAtvauA06id5nb27sC2N7eFcCn0fvkUd/MTxyAAJNTgQAAAABJRU5ErkJggg==", "reo_emoji_maeva": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEVckDsAAAD9/v1omUrZ5dGoxJePs3iCqmm80q6bvId2olrN3cPE17izzKRbkDpakjhbkTlbkDri69zm7uFajjZbkDp8p2JakThZjzpbkDoA/wBiiTuAgAChv44AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANXcBgAAAAgHRSTlP+AP///////////////68cSpD//xXT/zYxcQENAv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG6ftXUAAAJRSURBVHja7ZnbjqMwDIYdkhDCsVCg7R7e/zU3tpOW2e3AjKZeaaT8qlQCwZ/jAxcJKGFBBmRABmRABnwjwPXWL/BCLf3tsgHMPQionxPgBEI6MUDMPsAFAQMIagiAXhLQK7iCqC4wygJGWGQBwuazsrKysgTkClQVR28GrwQUPCjlACUNmg1Al7bzOk0LI78+NVB7a0t9CGjISvEAdHzd0qu1ubuBPli8dw4XGjT7xLfeBXQ0F8AXhTEMaIviQdbnNKpxDt8L/2bzxO4B6jghGPcMwGScrZ3C38o0UzVkWseMeXoHXTPePrL4DqBBb+hdPRHAtbQmJuvotKWFIscxVEPwx8Qn6x6gpNVbtD2lJNfhZykj5GwZRFlg14EihKHS7E4sk+eAFad3aHvF3FVUNV1MbJvyTfqdgh+jqn0V5/ldQMeZMORZxbEJCW/vgMmwYh3FcHHjGNMcABwZNGnpVYowjVoytgkAxshx1vB5Ezn7AOB16gSIEe4IsMaRLqbGcS1YjlAsP22OAZ7DvQEUlW+xKxoOivGeGyH1e6qywlpT7TSC4/VTeTvYhgjNtff63TQ5kbiGuM/OmopkF0Am4Q7gDi0xRtPmU8FG9KN16UMz1WA+/4l05ZsvmA5t4J5M089vZ2VlZWV9C/XS5m+ygBsMsoAZlOie2vg/tjXFN2blt5aVGoQ3x4MuL0/1eD04oPi7nl9+AvJPtiQBy6BEAf1PJQoYfylRwEnomCvZvypRwFfS+xEAN6McYPyhRAEn0bPMr6f3ALDMShYw5/PkqD/XNR30631qZAAAAABJRU5ErkJggg==", "reo_emoji_nana": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEUiZpkAAAD9/v7G1+SXt8+wydqGq8dsmbtTiK/Z5e04daPk7PIbZJkhZZghZZi90eAgZZkhZZghZZh7pMIdY5ohZJhDfaihvtMVWZAfZZoAVaoiZplfkLUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYb6/LAAAAgHRSTlP+AP////////////8brc//NnKU/ytF//8MSQMe/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAECu1vUAAAIQSURBVHja7ZnbcqwgEEVbBBrvOtfc/v87A3bjGDOVYTLTp3Kq2A8qtrCADT7QUAgLMiADMiADMuA/AoxT18MT1XfTuAK0HQioayPgFYR0JMARQJAAxTsIqvWAThLQFTCCqA6wkwVM0MsChJvPysrK+quyZVBNhfD4bIBWQYYK4VEGoD6kAc0GgGdTGn2anx2i81c9mH2s5bQpB+3uACi9BriK385TV4b7fi6TWXXJ4ejdLYAJH4fuNARwapFmQM3lIdSplnCZBsDBX6oLIHSw0WjUUjT+M2r2xIPWeI7dSgDM/bPUNf/OUEMzyM23qtE8MG+D9f1ArqrTADTDdQQEX+NUIHEqNoNaPFngfpgkwJ7qlhdAjdrQlFiKnb+26CyHkwHzJGHJAHNxmQE2fhtcthSqkgE2VlqZbLCeOVtAyTdbA94FgLi2ycwhvroCiLtF3wdwCwB5gVt1FVAzAJd9cROg13uaUZVpFFLs2giUNxmTdtpqMVcMgOivo+WzBQxxUze8fFMBTq0HH9qkSd4CTo1aAs0v/7GI+NN/zP0czsrKysr6++qkm5+kD6RaWUALheiZ2s6fOrbSx5qSB7Oj8NHy6786HPc6PN3q3XgjQbFdz0/PgHxzSxLQHwpRQP9SiAJ2b4UoYBJKcz1ubxLgEXtTAA/ZmwB4zN7bgKNoLtPnd2STpX0rnI19KXI+mfQJebEa1bB+fUgAAAAASUVORK5CYII=", "reo_emoji_faaitoito": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEXcLUMAAAD+/f7mbHv41NjjV2neOE3wp7DodoX1xsz75ungRVnrh5Ptkp7umaPcLUPeK0PiTmHeLUPjLUH0u8LcLUPcLUPcLUPztLz63eHocH/jKDzdKUP/AADjHDncLD7gLUMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCFsKZAAAAgHRSTlP+AP////////////////+vM/9KG/+T03T///8VHgEJHTkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALTML54AAAJuSURBVHja7ZnZctswDEVJcJFI7ZYsb2nS///KAqDlJXbsdmLMNDO8D7IskjjYpAdSaWGpDMiADMiADPhBgH7TzeqFmrtNfwH46JSAunEBrJSQVgkgZl+pngBvSlAjAjpJQKdVr0TVq7UsYKNmWYCw+aysrKysrP9AgzHnP01obia4aXL/YK8ySac1DcTzKPAfc2WwAWhonb+1dA+M01nt8qAEex4ti1IpD8XlCt+2aLuAz4D9hZFrgCXVGHvdoAsGAhoxbVmR75gvU0Bg31xdO8+eVq6MUFIMvkwTaRigvg8YlnFU8INtVc336LcF64/31Y5+o8MQAZkkr9plIqUIoHwECDhxSk5UEWJhARwD8CbahsYnHLcMaCIF7tGpWMTFMC34MkVBOUy3j7Clh2ZbpYgtFSSSixU7ih47AlCMmKAtXXEksKkI1ddFxmbZFwGOc33N9+0FwLCfdL0ABNhx7KnvLKj7gJralFO03zGAUlSba0Aq4Q0gMiD1Xd2qBzVw5KFLEfDq+gTYwW7vPA9hcSsG4KU1njJ2TB6GXUzuAQCn2a0t2Bm0HcLW4joGULYmSj8O4zMGcM8NGCqkblBcn/Cki6BsOWasNcQqYMEZ4CIBUksWKgEoFlzo0DpYd3xDoXn40TDnl9+bqw+Bd4b7w7nrL0OaeppZDflLnpWVlfXT1Emb30hvSI2ygIPSontqa9x1HKW3NcU3ZuW3lrUehTfHaXv/5aVe908OKD7388tPQG6qJQmY37QooDtoUcD6lxYFrISOuRb7v7UoYB61KKB716KA75X3OWAlepb5nbf3rwDzQcsC3nU+T076A80/H8LPgAnuAAAAAElFTkSuQmCC", "reo_emoji_aitapeapea": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEUafokAAAD7/f0riJLT5ulkqK9Nm6O01diWxMl5s7paoqrC3eCkzNAcgIpDlZ6JvMI7kZoafokafokWgIgafomBuL7h7vAZgIkZeYwYfYkZgIoafokagInA3N8afooAAP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABud8vPAAAAgHRSTlP+AP///////////////////7CSFNL//y8YM0RUav9+AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACLK13cAAAL3SURBVHja7Zlrs6IwDIZL0hYod1HU47n8/3+5SVsUnbPiLmTP7Az5gJXJ5KFJydspKhE2tQE2wAbYABvgPwIcP7u9WtH23e44AZw6JWC7fgRclJC9BcCbUoIElZyUoPUE6CQBXaKOStTOaicL+FR7WYBw+M02+xdmjZv+zYpsZUAKmq6GDOm3BgBcF1AywFJcyD1P8wwyqFcDZJAyhSy93mt1BFS1XTyfhgMD6DTkhkZKMw6MqjL+/WiXAdDUygFkecjRFJD6XyjWqANYDJEYYClybhALSPmyvOoVPabi58YAoLqEGiDWzQDLC+58gTOfoynAlIPPkV0hQ8H0DUBBW+I6zJYDKrgaBkADUBrry47DcoChpRgncgiA8N4ZnpMmjFvcLChwAOkA8As091dX84Jd3SrfmipncFODzf5SN79rJ8Yu181nNkC5WDefmoY/2gygHWUKXVtF3aS7tzSgw7uRhubB47dWQOl7DWfdsngNtddN9AJWVtxRTc59iAMb9iiQkphPPOYAOrZOBmmORLqJsaE2DDiMWskD6qclLQOceMwAtK5rzR1OcyNzQYwtZxlHTSiRboOntiwP7b3HDIAbPLXOlJ2pq40blhZt5sXTX7h7c8cujYn7gYnHHAB9yy/sqDMMqJq4iYiqxqrTNKPH4d7jxRkQ4Lb26DEzy0nzM8Cg0YepGEw8ZgCD9ruRhrRyQIWkWkFjQtVDDfzQWj87C4W795grcphqy1ngVeSfMvMCSdeKAKlfZ7pSH3wzbognHrM10HGva64JVnxPt3kUfhu3K+h3j9o9eMwC0Jk2vqbGVeMecnx5uchoolzSwKpHjxdW0TObX+o/C9jsB6yTDv8uC3hXvSzgpBLRM7UdnTr20seakgezx3C0LEa4jIfjvczh+HlyvH9eudQPx/vfflh4WM+rfwG5j39ORAH7YyIK6PpEFLDrE1HARegz1+RllATsT4koYFF5XwDsvhJRwEX0W+aSt/clwL5PZAGnZPueHOwX3AQi7uhCwuQAAAAASUVORK5CYII=", "reo_emoji_manuia": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEX+qzIAAAA7Kg+wdyRoRxdSORPlmi3LiSl3URqbaSDakyuGWxySYx7/qzJALRD/rC//qzD/rTH/rDL/qzJeQRWhbSH/qzK9gCf/sCz/qhz//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuUkcZAAAAgHRSTlP+AP//////////////r/8bNEqT0///dP8WCQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEvLeAcAAAJKSURBVHja7Zlpj8IgEIaHo5y91Hrs/v8fujD0cC3GJnU2a8L7wSLSeeg7Q00AGLGgAAqgAAqgAD4I0F+aE7xRp+bS3wFuDRCo6SbAAYh0SACy+AB9BHRAqFsANJSAhkEPpOrhSAu4wIkWQBy+qKioqOifSBjvSAGcc7NtJmEkr1O73XwXgORcZLEiB6iW5lYAqFxn9QTA9TipEaCtMRb7bLwEvzX22ni3w4uwNuZACS+9uAfoNSAE9nEstsxESnMJ9qlqnEIcCtMlWXRt+eJAutOtAaLibWpdEeDjLTGqQoDBGEMOEObE26GdkwhhbCbJosbZSC4dAgx+9fgZOiqhPNLWAF3Fploeoc4DojlxmHBjDq7BaYnzmp0KHmUsAu1SGsdo58WtO8A5jlY2+DQCtJHou8fILiXvmgXUckAH1RRtyAAsUqoQTyMgPKe0Zz8B1FR+AjOBP48AF7LnrWhngLIiCwhLDAsMAS5ZWq8AOlkhqxlgZgOnVeEgDzCp1hAQPioFNpXsPSB+kdrXcgZgnlz0U03roM0stBojh1QkgEql7dCJX4BUsGoB+LRezFT9MYzMAmIEGAFYFeEZ1gA18FQS8zqItWCjm/rpE2RfM1o//eXhFaQfOlz5IysqKir6MDXU4S/UG1IdLaADRrqndqTe1uz+YmOWfmuZsY54czxu77891cf+xQHFYz2//QRklS1KwKljpIDmxkgBx29GCjgQHXPtT+8mwJ70bgE0X4wUsC+9rwEH0rPM/el9Adif3heAL1bOk5N+ANe3HG9zdu5AAAAAAElFTkSuQmCC", "reo_emoji_haeremai": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEVckDsAAAD8/fuoxJdomUmGrW2Os3i0zaXh69vF2Lp0oVjm7uFbkDrX5M9akjhbkTmZuoVajjZbkDpbkDp9p2NZjjpbkDq70a1akTihv47M3MIA/wBiiTuAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB7ly/aAAAAgHRSTlP+AP////////////+v/xxK/xWT0/8wdP84//8BDQIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALq3mGwAAAIaSURBVHja7ZmLbuowDIade+/0QiljO+//msd2Sls2OiYNT5qWXwJaJ/2/xA4gJaCEBQmQAAmQAAnwiwDjqRrgiRqq03kD6CoQUNVdAQcQ0iECxPwBzgRoQFANAipJQKVgBFGN0MsCTjDIAoTtk5KSkpL+vKyzsv5a6w3BhEB3RQitDCCLd07r/FlTKEwBuwBnzJxBZ4Jx1N17fISmeY2wiXdgDd3aNvg4cm9is/d+D+BKTaJuga8C5hA78KSXCGdWl5a7WnrEYKTl5gzN8GMHUGBTXXO7p8748gQwFFojEaAZeJnY17J/XvIwPwBmIWAqcSwXrQvArkcqV01Wdd6GTWQGZK7gORTY0oLLsTl67wNQRxN44pSMQJdkVc5rY47MgJzzmPO14aqF6T4Ai+LNtWsswnHBcjKIvEZmgNm8B7D50rxfA+ppYYozuNBascv4NpEV8LICLpQncvsMkNMC8lzIkt5sprMlAWvkLqAkH/N4BrrWLTkRhhbgtADWyF0ALb6sDuS2D7DZnP+X6IcxuwDWyF2Ao8FZQyvwFnD7M+L9+ivitjc7kZtnXfojSUpKSvqVqqTtT9IbUo0soAMluqfW/8S2pvjGrPzWslKN8OY46vz0UvfjgwOK9+v56ScgH6olCRgaJQqo3pQooP+nRAEHoWOuq/+oRAHfKe9XAPHLKAfoX5Uo4CB6lvn98j4ADJ2SBXTpPHnWf9HKHK5BI7W4AAAAAElFTkSuQmCC", "reo_emoji_aue": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEXzkAwAAAD+/vz3s1j96M75yoz72Kn2q0j4umn1pDnzjwv1myT5jAX2kgj0jgrzjwv0kAv5wXj60pzzkAv1kAr0kAvzkAv0kAvzjwvzjwz84Lz+8N30jwv2jwn//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFchIUAAAAgHRSTlP+AP//////////8f8SHDKvSP//rjdzktKU1P//dVQBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJftbCwAAAINSURBVHja7ZnbcoMgEIYXQRBFjdGYU9v3f8wqp6JpE+xkO80M/4UTibvf8nO4ACDIggRIgARIgAR4IUBz6I/wRJ3btyEAqBYQ1CoH2JWAonJnADvAUjnMgBrwVNYToEUEQEugAVQ1MOICDnDEBZyhhKSkpKR/KplryU1BOiT220wr3wRgUwSL/Nbkj/58M0BYQHbHI1nkHV208CmAxzvEufeI+9JmqM4qmKlgH0TtV+8PHKJ0fv4AoK6LYcl59KgJk3p+im8BUue+6mfhw4rF2z3tTWUX1+UbgG6QdrL5MOr8i3KoA+hc+A3A9425H67jItqhCqByedYAYcZoEg9dqUzYY/l8zHrkGyoDKLJQedjzaIe4qy+zY6IBcg24MsaKrQC6qG+23I9lEQB+v9HxJYDbvNJ6NgGkX+SU58Gw0ryoYvchppWZUnWfmJCXzM7E+Y+rsJZ1i8BIh4qvpeOmpe6NMO/WRVOAK1pmWdRC4GEd1qPO7X0W4BvCWRoLWGzTzNI6m0usNzsWJLxs3uADVTcDOLXkq3IFpZCUlJSU9KJqcdP38IZ9IFXjAhSQE2b+cT7WxDzzqpEPZpu/OVompO5RZqgKjveH8dm9ODUPLijW8/npNyDL/ANBBZxrggowVxl4gFERTICezJiAhqACjjVBBfSKoAJOHwQV8I56l6n3WkzAURFcgEr3yVafID0aCTBtE0oAAAAASUVORK5CYII=", "reo_emoji_ahatehuru": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEUiZpkAAAD8/f5rmLrK2uZVibCXt8+ux9l9pMM4daJEfajX5O1ekLWEqcbj7PIhZZgbZJkgZZohZpggZZghZZi90eEhZZgeZZkhZZqiv9QcVY4wcJ8AAP8AgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB6H5iAAAAgHRSTlP+AP////////////////+vGTVKk9P/dDIe/wn/AQIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG/+9QUAAAKCSURBVHja7ZnbcuMgDIYxEmDH61PObbfv/5qVZLzFScfOJtZFZ/gvPEGx+QCBxIAplGUyIAMyIAMy4BcBhnN3NBvq2J2HBNB3RkFdPwH2Rkn7EaBWvzEDA65GUT0BOk1AV5jBqOpiDrqAsznqApSrz8rKelZ/rPWbVLSzUf4XAxBYbiwDskEAjUOLO7K50Fr0zwNCUvRjd0AA/Ksm5mgLTwNqTyqlVFHJOWovA4IvhUV9gupk7Ws+wFiGnXHWtgwgE3WioeECQ6Nlqw16QMONwotOBn5WHlu2uQ18IC7n1kaA42dt29L5FwDJLGp4zJ2dAQRClOcBySThCYO1nwEqtrXNNgCeMRbK+RDx1GUMbLLw4IdqHOxycM56QPgfwWy3uiIA3fMAz4GpWXnnftE8DpDAt7isG6qs5qxF2av2CYDaxhEU+b8SqZcByypYSCyk0FTNcj59kyaUMXvVE6B+G3NZKUFBoidaT+AyscSlvTxGHHqDd46zF0xtofSLEDjLzAAEreEWQPG8Xcw+IB9QbRSlMXYB5XPOZTOA4G8A9Pnpw6wDMIbRNnEyP+eA6h4Q/uXXZcBJejDtV74BIAN8ioD4/mQZg6tb3xYGYE/wQNX+BuDYEZACEotMclzbwXCOso1kKkwyzfQcd0YJILHEr9dyj5e1WIkXQnULAMlvKeDbwqJNwMf65hnG0YQfp5tzixaXQ3eWypmUdvVn7QOpqy6gN4XqmdqBTh177WNN9YNZ/aNl/cNx0mVzVx+GlQuK2/m8+Q3Inbc0AcdroQoYvaUHOHwWqoC90jXXVP+lUAUc+0IV0L0XqoDD30IVsFe9y3xl9T4EeN29K4D3It8nj/oCfW0en2n5I1sAAAAASUVORK5CYII=", "reo_emoji_maitairoa": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEU9cRwAAAD8/fxHeSiZtIizx6Z6nWODpW9jjUhvlVbO28ZXhDrE1Lra5NOqwJvm7eI9cRw7cRqju5M8cBs7cho9cRw9cRw9cRzh6dxAbRtdiEF+oWg3axcAgAA9bxy+0LMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADA7+SpAAAAgHRSTlP+AP//////////////////rzL/SRiS03T/HP//EgIu/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGbuTJYAAAJESURBVHja7ZnrjqMwDIWNAyHcLwV6m915/7dc29BCC9pO1Xo0I+VILTf5fNhO+JFAoCzwAA/wAA/wgF8EaPb1AG/UUO//LgBdDQqquwtgB0rajQA1fyFA8AGK6ghQawLqABpQVQO9LmAPgy5A2d7Ly8vLy+vHyOX56e6Wsdac08g8Z5RZa7MpfDwZFSKG/HRh5xCzHDF5DkBGmPNJi2J5fd22Je8SFwCDaFwZwvMAcakmQBKGyZiZcXGFMeeQxWFCB0Rw1o7ZWAdx666P5sA1oBLjBAXg+ICpgRjRRnJhzEGOJ0hzoFsSFmFEKVuTy6MY5sA14BBhwRFlRYAUscw5ggEhsYvCkFNExtFofAWQX0L5p3ySzYEbAII7qm8mGZQx1zoSANePCxS2ADlWt4BD6ji3QpJfBG6UCAosY0xBSmX5PehiAQDXSrFuATKaRkf5vwRuNJl/OSWHU4lscQvgEsWfK4BZAMo5cAtgxpFEAMdVdNcM6C+0krgpNgEpHywFzYFbACowvwm5UR+KqOCuC0CGxolaHVVTte4AVP6qpBgzB24CyM0JgFF45r4IgH3wxFOlTXiorABw5umTG5gDHymxN0PZJAnPquw/35rLPLPGf8G9vLy8fp9qbfu99oLUURfQQaC6ptbTqqNqCkflhdnme5aWg+CovDjOy/tvb3XfPNiguB/Pb98BWXVLEzA0gSqg/ghUAf2fQBWwU9rmer29XwIMXaAKeKm9XwD0mluNr7f3IaDR3Sx9vb0PAJ3fT570DydWHqQ1GUfhAAAAAElFTkSuQmCC", "reo_emoji_uareva": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEUafokAAAD9/v7Q5Ocph5FnqbCZxsuz1NhMmqOjy9Dh7vB2sbiJvMIXeYwafokafolaoqoafokZgIkcgIpClZ7D3eAYfYoUgIcZgIoafokZgIk8kpsafoqDub8AAP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADdg3rdAAAAgHRSTlP+AP//////////////F6+Q/9My////NxZOQ3L/cv8BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOSSYfgAAAIPSURBVHja7ZnZcsMgDEWF2GJjvGZruvz/ZxaBnUlx0nQmUaed4T4EYl90QAp5ABDMggIogAIogAL4R4Dx1A7wRA3t23gB8C0wqPUL4AhMekmAF2DTngAeGHUIgJYT0AoYgVV76HgBHQy8AObwRUVFRUVFK2213lKrtN48FqmfI2WqEA21GlE+BpCIDTfA3Qc4DG21JMtKoyyigqkJw2urwElpKR2xycyI/V2AwaR5UI22Cd+ii7SDDRKPfDY3V+febQANd9rOjyJAEiC8xMaFrg6PwgelQ+dmE9HfA1RvmtjdLQAptVKwi1HVPO2Keqhys6Ol3q2BchXNWS6A9MMIrQyaFynJbFdmfR0QZ5T4FlTA1dJeAmJaMQFiZWnyhlaUm7ex/CuFwHJKvwEDTVzOZgWQqd2oNCMtKd25Ob1eidIpjaGlblO+1HoFIehOUSwbI9rYyczTjY1GE0kKY95DU6Orl2wuAFXPHpfyFWuemRWey51Jp9EmLFDRQhrKyFdAnCjOM4x7Ym2ebuzk9IfXv6b8Tb1+ve658meYm6/XoKioqKjoL6vlDn/iBZzA8wI8CNYzte43jjXZD2YZj5aPy+H4gflwPGj/9FJ3450Lisz/9vQbkK/xR8EKGLxgBbResAK6g2AFHJmuuS42IydgOAhWwEPl/QGg+xCsgCPrXeYju/dHgMELXoAv98mzPgHMnBwZtXqLmQAAAABJRU5ErkJggg==", "reo_emoji_aroha": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEXcLUMAAAD+/v7cLUPcLUPdLULcLUPcLUPdLELpeIb41Nn75+neNkvgRFj63eDjV2nmaXnrhpPwpa7kK0H0usH1xcvumaTdKkPnKTnkGzbgK0PbJDv/AEriTmHytLz/AAD/MzPocH/ulJ8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcZl3XAAAAgHRSTlP+AP+PrlHOcC7/////////////Fv///xYQCSgTA///AQX//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM1bcDoAAANsSURBVHja7ZrnkuMgDIBlisFtjUuctvXe/yEPsOO4QIJjmLmbWf2IG+gDia5AFFjgF/BvAs6UMkwIwZjx5nH+I2dYJ2WUnt0AJ0ZgKjHjNu0cx7OkhF2fAug8y8CgJvVuSecAbspjRjBLSiDcCrhisEvMnUqiBJ/MAA6PhToUf10YcM2kSnZLip8mpWvA80w3whdxSMqWABf9A4E4JWVzgJt+nc01KZ0CKLgKdU/K74AjhJC4GQEkCKD3GGwy0Ea5DIA4FID0gGAV0H6GgBXQXoDoAgHlXQJwSACVgDgkAEdwDKkf4ghoUACcgIUFcMBhAQzIfw7AoQEkPACHNlHwVhS4o1HgoTtaFBYQejSNX50P2jQVjsO1ZUoWqZTKmvENocR1wmmMXz6RlHQ34Gib9HOkpRifS22RsurEHVD+qT6G+lZdUhhdoACmGSFB6FAj1MnbQl7KDCGpPlXQLOkBolZPiqe+SmmNa2Uw72xahCrR20gC6oPMDyUaJNGASt8fdILx/UIa28pOWahQPx89QKJSkJRDWcj7LFeAQ5ek2oqSlAn1vjVYSAOYyUJvoDR2GpAd8h5a9hehAJ992dWrRP5UhjbBBsDJZKH6lqcYKq+u6luqHpWJ5H2mP+VVq72QLdWcb8t3bLBQW9ef2kbF0JrUNZ8AkrExSe1pXa0B4/J9tXpM0CjdqHgwkSq1mAFaXZtkDbhvQJY7EJklUz1ZFW0EKJe8iXx08ghIFUBkKwCZ7NH4ykJ6lFAN82MELJrptAbqZbYE8OkukywtpFUqc3Qj4NbRfgBWPpAFSvs2sKjADeA47ZRCGAbRXIjCtskcN+IkyA5wAvC+yL4uzyqY753H6rQl9r2/XAK8Li8a04EUC2Cg+ZEa8W+gOaDxBTjbTh2pt/297VjTy0qYPTg3fY/9OmB98ru/Q8fnx0fL3KsDTIfj1K9+w+k789TD7PED4qsBWQMUZO8c8AzwTvzpN4dYvok3/bYgEfGl3wbYbiW8NcyFd7efZ3E0tq/9OwTq6I7+6xYJdB2X4uOrocar0+hNTq/HMr/xDve6BUufOSK+7I3GNg/NRJr94d4v9krr3BRPtsUVH3t3U8CavVh894h4sxqb8NlzyH0ePSaXyH9M/45wV7/xTwOUGCLSfv+VwDE+Rb//q/gFzOUvVuYkuMEoKB4AAAAASUVORK5CYII=", "reo_emoji_securite": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEV3slX+/v4AAACHumnW58ynzZG416Z2sVSTwXh2s1ObxoPl8N53slTJ4Lt2slTF3bau0Jl2slR2sVR3sVTh7toAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD0lgauAAAAgHRSTlP+/wD/////qv8u//9I/x7//3WP0/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABD672kAAAGaSURBVHja7VrblsIgDEwKhFLs3f//1lW7HitW9oFMd93TeehbZw4jJFMMVTeE0c+kiNmPYWGm66PzBIDv7gInAuG0CMD4bwpUdQREdxHwSAFfUSAoAk1YgYlmrACY/sCBPwV3ZmZbw/gtL2jB/JdFQPiFH2gA/GbFD1mCXQuwPv/wxM8GahBiBc8GcVQ/YckCHNggBhvE2sWiSfjVSwXaoDbh164TdcJv0QZpH+J+Z4P6T9tBsnONUN9BEbyDPt4gCzYo7TICNigeBv0zg5pyg0wjzgCLaJttH31pTjH541/eZWy+wBQb5PKvS3GQs9ktaMrbcL6PxPI2HHNZRxRyShoG1woqXca9CDx+SKuSU14F7k4MOkHObCg41Ta8pTCoFtEtBVH92NtS6FVzion8E4xy12L1IJdXOAM6r/7XcPueXzABWtWgzdqgn1Mc0qD3CtCUpX+fUjM46eKv5BIFQwS9FwXdTVugQU9HzhIOTkRqOnDgd+DR9CNWYMT/5Q4fGqigSwjgwY2wz+gJfnjmOv6jPl4xfY//fAHO2wuESNS7+wAAAABJRU5ErkJggg==", "reo_emoji_aide": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEXcLUP+/v4AAADeOE31xcvmZ3fgRVjjVmj75+nxqLHrh5P41NnpeYfumaT0usLysrrcLUPdLELiTmH53eHeLULtkp3dKkTdLkPdLUPcLUPocH/cLD7iLEIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7TUcFAAAAgHRSTlP+/wD/////////////////qjD//0n/HnWP0/8dIwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO5O5YUAAALRSURBVHja7ZrJciMhDIYh7PTqdrxl5v2fc9xxu8Ui5GQqzGGK/5CDgU8sklBXYG+fOlzmG/tB3ebL4UFm65/zzCpoPj8NvLNKen8YqMZn7LAa+MUq6nw3MNc0ML+xA6uqA7vWNXBlt7oGKuObmpqampr+Rxk/dpZzK53XWLvo3dhx3o1Oib8A9PexIGlSuo/b/TcBQvJEMaG3abtVMWAkATobz3kAEB1HJMXXAUdsPDl6VSfIGXRgQKLjX/EDCyMJYB9os6WWF69SkQDGgvVZuU/3hMzu7qKfrpqcZAjoMgDTe+u4uq9Qbu3jtlYPg92y+buD30wOYBtgP6F+B8Cxmr3VYl6hok2iAYwNz/YFic4+misEbfjzgHYB7QvGEsARmX9kWL4A3DU923skvTzbprRld20NBvyLFXCX5agTYEqme9giBJD4CZe9QOfZ5cPsvjYKELvplihhGiLz6XzhlgIUMoVUqW1F+BcFSH0OQlbFLYI4f00AMmdPkrHK8hbLt88QgDwyQUcRbUOucPtKAJiOQ1Ol+qoBJoYcMFKX7sPDqTMQSYJAAWnZIJOErok0ZfIYzAFIaRJ2MYzIIvj5pABEGo7jtF8lrhxoHQlANUCGG8qLfXYaCIAr1HjgR6q4R54IcpZXJngek+AqVhR8CL0ELG1AB5fAULgQJLFDEeARyN6H9ewYDIaZOvSSeiyAAMBspm0zxRRd8xChcnd4DSE1IACX1AlwX8hB+SmJk7DumtQihPkYk3xTBHCqcNwXaDghUy4c0x0ql36+zPc0QKSXPjK70nURBsfwAlCong155X0LYJDqvlsK6QUrURYEYKNE16fbOKTxaZIeyTdYBnApQA9Qd0uPhb+GC6VDviJfA9ZOapUof+nqxZhFE+2vAE1NTU1NTU0lzbXxl7oGLvX/5V790cBb1SX8/hcPN+o/Pan/eGZ9/vPjzyuu2/OfP1S0GmCTFUAOAAAAAElFTkSuQmCC", "reo_emoji_eau": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEUAAABcrOtXq/NcrOtcrOxcre1crOxcrOtcrOtUtfNgv/9bsO1gqvSA//9mzP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACIstn4AAAAgHRSTlMA/hHNUDBukqwPCCcYAgUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEnjkuEAAAGrSURBVHja7VmLbsQwCCsQEtK72/9/7u2hSpvW9gLBUqXNH4BFbEggy/KPZLw1MEGlAo3fiWhFErR3AuQhKX1AcQTySSCw+IW+gNKZaQOjLLqhwSy6QVEW3SAwi26oKIvidC4/45PBLArSuf4ikI6yKERn2yHI1Fn34mfqLLsEeU2v0AFWlEWTm149JMgphvtx/JymZycEGTornYJRFk3TudALKMqiSTq3lwRzTe9OA2CURROantIQFGXR6cut0CAqyqKTOrdxAoNZdKbpmYcgcLmpK36g6YmPwF0M1Rnf2/SY3Cgoi4aKIZCAT+dIAp4UQgl4UrAYAd2wCYynUKME9MAUsbcWbuH4g207fkJEUA8N+0gmCGpwZE01qs4QWOZjJXorTBEQ2KXXICiXJhC0TeUKhQZvFVPNTtHtel2wKts1rsyJM2Lws8WwL0fHjMDgBKKlUGADWmCWjRipQ2dA96jckfNNRAZ7LLBdS3ij4xBaGLsvEsau1Cy+FuxG4L3m62OS2e11P22tkvHNwscUNekniute52ipP+Nav+strSK+lFlLKarcl7+EJ9o3EfBZyKyMAAAAAElFTkSuQmCC", "reo_emoji_cyclone": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEUAAABUq+1Uq+1SrO9Tq/NUq+1Uq+1Tq+5Uq+1JtfYA//8zzP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXDYQ5AAAAgHRSTlMA/tAuE5CvTGwPAQUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPOSLPIAAAOBSURBVHjazVrpcmshCI4gi+n7v+/N6W0nrggmmSn/Os0B2T4QvN3+CBW8qOT3c85CDOlJQIpvY47KaUos5Q3cCZJBrC/JKGpy/0907JGsyUdnIgolP8VF3DXFSIKuhRQljiih6YTcSuR52DOpPLL4lhFlnhlOJXD8EnRMqVn6gUeCjCGC6yyMS5ABDsxvMgUldPxhj2jIEQkdf3V5TfwSWv9yOUp6uK8NepybjRK6/BnvNEUl4gfRo9y06uU69VeOI5P/UBigCd9aAu/VhOIrDJWMWsLUSGXNHw3kfuZJLSHbBmrts4CmMVeqGCRbgWJDx2iorwGEixVBEjh+o0RlJDVSjFbRt68FTy6w9kDtYIxWG1rmAs/+g5F6hq0neaUBHfL/CU1eRWoebVeChZ/bmNN5ncc5crjomyUs8UIudCnHBvo93TMXdhh/0LdclQBNuLi9YKCfWL076wketV5cO4FMAXAk4IIg2lQFB8Jdl6c8b+608jJYAgyIe15pJmUC6rMdeaAtFTJJZ/QIYBsPDAnoi1Mb0axo1kpAibtYN63UFZvi0GBpoX1CssvJ1e+74+26wUcYOcCoKny8bya75vr5NzhuaF27hXvQAgOvJ590Nd9xYYSc9lgEz+OYSTATwOpA0+oMKWqiqkPGvQDtQFX3SclpH0SlOgP0UOaHLXZEKfYpJ4GkFIeA3OcpBHDXg9VlQKU+9Na9K91cPij2d0ZvZl2w6x8NHLj6UiDFXVwLkOlg50dEUT4d7UAV9/P+C9ohaprVZk/BJLv8H8+mmsZD0mED5uopHuh2P2nBNm1pbjTFlwxUlHic2bQ1g14wEM6TgtrOA44NVBZBhS1AS/wa0p9Ulr11fIyKs/6KlmVQohJw2tHoEu/APbAY3ckG9HEv2zfMbka/YmG3DMI9035Z3SLHxLtPbgQ7JdrJ9W4AVqnAv2PKL2vh0s2f61IEuw6btiWGxSqluJ2hkrmV4nF43pRScSwpaFzawXfzPV/XNecn11U5tD9pkgaK86p5uj8p7tu4Uwn1dy8DQEh8e4XBdYW9uCzCKcZ/AnLrlcVksIBHKyOeycBJkkM+3wle8f8LgijzhTCV15emAO/ZbR40LsHtbA52LhBf9wtE56cfEwF6vIFHR6NNr72FyPYbAtA3vIJY3mv4jQ85iihVKQBA8oG3KJfFHs9cPsP5L9I/B3UcwLSgZXwAAAAASUVORK5CYII=", "reo_emoji_medecin": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEUAAADYnYHpuabBaU/23NP/v4DVlnraoYbjsJnYnYHOhmvGdVrux7fZnYHYnYHKfGHZnYHZnYDYnYHam4PkpovXpYLjm4DjrZX/qqrcoIHdoX8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACL8PGjAAAAgHRSTlMA/v///wT//96x////bJL/TS3HFQsOENgDLB4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH7TShoAAAL2SURBVHja1ZrLoqMgDEBFKwgUX33e+f8PHTszrRBiJRAXk1035xSSWAmtqv8iptE5N07XI9j3sZ/FO+Z+nHjxv7SAMTMqLr3AQv8w8UexFY6F78R29G05vxffYi6tqFaL7zE/2fhyaKxBdont+w/NEpI10+H+2JcAWYK4MO2/3VhB9ibB/JqFb9FET0z1I6XEK0kfUp+FWQj4ck/gyup/ye4ggs9WFu5R+1Bhcv3yfH1swBJuRH5X1ypssFUgG6Rcf8h8z2AAEFvBSOevhuUZFDSwQRraZfD9XdoNSjO/+OfTmWboad//fFoCMYBO9j72dH68hlf5DCAXkpgDj/9X4BvA0/RPuVpaFfn8U5TpJuwH45frlM33DAOygveWXfP5fj/Y4DfZWDtIwrNoi59SrWN6/SP8BMOl5PvHBmkkuc2+80PDAPpBiHsxPzBEj2vHwI/6wRdcOfiewYLXl5GH7/WDsX6WHRd/o1o1Hx816JaRjxiY+ZGBnQ8MB/ADwyF8z3AQ/2PY5z/qVVDXVMM+X6tVUNdUQwJfiLfhXFNDJfH/GXLikcbPNnSp/EwDgZ9lIPEzDEQ+2UDmEw0ZfJJhl1+h53fFx3f++9n62624+COYzljSGvb5V3Ag8o67ioMfDCiBYN+QwL9HAyybnukEPpiASmPC13BVyr/tHSO+GLqyEfSuoUuaIOvP4S3YmuVsZ3YMafwnPp2RwelX5fOrCT+wmyaoJpXN/6Tg20QAM6TyP10G56sWzJdUJn/tAhlNZeR2LaXzdy4aNgxdVR0gWA1dW3AVA+erJq5WEj9qZFA9Ju4HGv/TBxvzVdMEEwJF5oOHdTRfhQNk9SDfYCH3DSYcgfs50S3rhRv9/IvdSB7M33gnisat+XxYR8h8tYyPNzN8mpbw0SyY6DpAt6w3t7IBIzjdMt/dGtsMkotfPedD6tN/OZrZbjK2DJr1wo32yOD6I8OEL6K/VGwxxZnobxVrTM53aHepqgP+rfL6K8xhf4bhjt+URy/qGWK4HQAAAABJRU5ErkJggg==", "reo_emoji_non_ice": "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", "reo_emoji_non_alcool": "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", "reo_emoji_non_cigarette": "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", "reo_emoji_non_vape": "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", "reo_emoji_non_violence": "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", "reo_emoji_protege": "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", "reo_emoji_parler": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAABgFBMVEW83PMAAAAqZ5e83fS83PO83PO83PO+3fW83PO85/1llr2OuNc6dKKlyuW83fi84ffH4/xRh7Cbwd7////D2/g3cZ93pcjB3fhdkLefxOHB4PfQ//9Ce6aBrc2///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbWWMXAAAAgHRSTlP+AP9N0Y+vLW4Q/////xQoDv//ARX//yX//yEF//8EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP+9H6YAAAKbSURBVHjazZrneqswDIblIY+GlZDunnP/l1lKKCEUg22ktN9PPYlevGXJIJgFfwrgbS9PDjgrNEbDRNoYVBUJwDoDQRln9wEUwpY0qkxAG+F9ENo2GdA4SJF2aYBE973cezwgw32PiAO0SkOmtIoA1Nnu+3lbbQEU7JRaBXgDu4UrgEoDgXQTAiggkl0GkPm/GQjg8D9twwiogVT1HGBp/V9HegB4DdSE9gZggFw4BThgkLoCLLCoGgGGB4DfAAVMeh4AmguAFwBbAwDOPcDwAfAL4IFRbQdwnADVATQnAAXUwCoBihdgIRyAlovGMvqnl0GAwCQtX6SUx8PM+lRIWTzNjIdj99OXACP0/Qd50cONtbgYP26MD8NPD8uRWAAwuJLytODqBvv9KbJYPnfWG9D10sQ6GuXEeByNhwTA+K3y8Wo8XQGTdj1Kudid62IH/CProlAnFUv/yhtkkz5Ni4RpGgLAa+9svqaO817rV18PfQ0ttOBuXZ7K2K2iPIXvbWC5NzvBC6iA80jutqJ7HJmsh351j7CFM/CqmUNHM8SmbIGFvVf4LioegL9eoRTzFUoIZL4EikZzzCDOizj4eSrB0l/P7pwMIb2N299JSJGNQx1OCr4RzFZdraU1/+9eca7dSMzafYnZ83ZqGQmzsouA/Bagj0mOZ8cAWMWl9/MWg3Y+tkCRMwRGJZRY0j8ebUqRKK2HtNksps0Bi+e/c2j03DWqOqNQV6/VZir/bK36khUis9SI2xWHXcVST+5/BnCRtatcgI/aXXYAfjRAW0EJOP9YoV6QApC4++eAZq1aRQEw9J8fDrzwTP4qYTrCxgpBDjDbZ8cugBvL8zwPN9RwMr0zvQx56/Z3pxohuJ6eeBbff/DxTI4+AQmrGoCR6c71AAAAAElFTkSuQmCC", "reo_av_bg_0": "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", "reo_av_bg_1": "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", "reo_av_bg_2": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUOfIYAAABf4NZZ2dAWho4xp6hNysQjlps7s7JCvLlGwb0pnaANe4YOfIYOeoUNfIUIgIIOfIYNe4UekJYPeYcAAP8QgIde4NYAVapW1tFg3NVa2tFg39YAbZIUg4wlm5sjl5tAuLha2tFe4NZg39UUgYpGxblMyMNd3dNe39Va2tJf4ddf4NVA/79g39UWho8amZkA//8nmZ0qmaEqoaE1qqo4r68toaQ7sbFAr69Cvb1EvbtQysVMyMNV1Kpe3tRa4dJd4Ndg379g39Rg4ddg4daA//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADTnuUhAAAAgHRSTlP+AP7+/v/+/v7////RSi+uDG2L/xQBIM0DEA3PTAfZEEUwZ681RBbMS5SnZpAEgHQKAbkeHj9AvJcQG3AwkAY2EVIIYE2oAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIxKPcYAAAZ2SURBVHjaxZtnm6MqFIBNQMGu6dNndmZ7ub2Xvf3//6QLiAgKCiZh+LTPbODlwAFOM1g8Uwtm9quqgrVN5Qtc5KsyC5SWlXVenBW8q8vA2Mp6dxbwJl9lwUTLVnl1WvAhXwWWbZUfTgau6sCp1ZuTgDerwLnV1dHgmzqY1eqb48B5NgMKmaLlR4CL0hVJGkpDhOg/ymIm+CvHVYbrNEwisCQNgCgJEfxiOwf88w/QSVYUM2bXQIS/rtzB/yxBklqjYdjHNmx87wi+fMv6xcgKPZS2Q/945wK+3PNuIIQ24nZYwFv3h9d39uBXr0VPkEwKDRMgoFGCQ9JwTLSsHeLqJ1twdQtD3I02LjSEaftDAoVQrH6IIz7E1Ss78CZr1q/tN7bTEBEJObY/QfJ/fIirCxvwJhNbx/uByCQ0/UlEFUv/E4JuFnx/MQ2upEuS9GuPBTKMS5lkOzEyzCxttmx/OQWusr5E7WXQR8OUr2SC4hE1gM2vHj9OgPu3cyc0wGHHprojVACOa18j9ON/o+Bct43SHRiGKSKvQKexdHenzvmazfHTGHin6ydfS/SoRtL9APS7r9HB5fKzGVxlI/109yGIQ7vrnJ4sVcEUsNHIQWECjsDyQ/3OBM7H9knaVr63Dliuj7/owZvJjpjewGybY1nF7d/sb7Tg0sLGYCqdUtNmlglY6sBF4KHlGnDpA5wdBmAvAhN7ewAu/YCzqgf2JHC3yy048wXOtgo4DwLPIgeeBSYiy+Ai8NgKCbzyCV514G3mE9yoV+BZtYR6BR4vD2WtKXjbc62PG9ZihBZctO9t3Dy31KibRSdmRvtiJ2O22I6DqedPbFDh5HG4I5taZuoQiWn6NQeXQRgBMLCogAuauKqaIQy+T9mAt2jYx8E7NmE5WhtVqBj4weTN047IyniNgHmEGGovLwL+WzEdcayMYrHeEANFxv4QGlejZuBPAyu582zpXNYT4FRycYQq02gMME5+xcD/Mmzal0N0BOHoCUJpGxBAfW9NzD5CA+0i4D3VIt3OiWhEYo4IxERztdheVEFV04yBjecGpuJU6tWb/ICdO3PMAOJ2CDWIQ8F/RWbNFeutC/5AviRRqNXcvsYDvIbSeQoWd3DUqxb9yImE8o0s/OYpxxwDKYoDO/CE9QGFd0z0PoW8pdJf8dR5S6UjgllgF+6mwexWUo5pLN+v5oiQ9oSwHkkc/0rAuc3FBIz30tr6AZE7PlmBSb9EhyZY5PR2dV2v7cBN6EZlA2Ab21WeTVcwiwnwR5775tjZM2c3cdPeWCiXMmkWl50VDhBhBTJElDy4gU9p1Af62Na5G71AqucCH54DfKCvU+af2zyLpX9wYwis/IMb06f2D84ZuHiOY0zB1XOcJu7C+Nct4bR5bbXipnoOv1BwpbrVxw47PUSlhiLYk4XjGJNcy7xnjxiB9NVjI6RmfCkHX9ZN+F2kWuIwhc5PbRzxIXhe1TD9LviyRcM8i2POQeTdFMdRa6VI4abFb3qvOraVmqTMtS4yRY8F2BZPBus1wnbWKzZ65hq7Ww4pLkRqPkoieRCLBJ7ImHZZc8Xi79vAShB1cd1kDhHJr5BMC82Xd7nMqeVG3W+pQqE18ZmRmn2ExrDx4gojyZkjVR2tT6b3fOVDm4rxpawQJAJg3eR7gfLFPRzkmAR6xD0iVnocCqw2sd14uUJN8+lkiOhndlVIopXsKTCl1LvtF679IBmivbCJdzwmdBNpILphiGbJNSJtnC+3THhBIfTgRDJ/hKXq4cj1KOIGTZyvtE7xdUIrscl15z+COIB2hTEE/eCQ1Fxj+YwSv4k6P53fNxb/6E9++VabTd3NKOWxCgh0O3bplriGStCwF2WFgX3907Vzqh7KUrtjOfqda3ECf+Nj0L/93V7s2y8dyzGke7RRK/pUz8iZF24FKMNMx8x8Se1WcnPi/JptkdEJbfhqqqxql501UT5SSHYOcraxKZ07A7myLBbMzi6voTxyU55Vr0YKQm9OSC4PLiWw25O5rvXWsei3OGVBgFOZc3WC5S43cwq7j1/u2lspu1RDT8Qt/BXvSzX0ty+P+1zB4eMMpYb+xe9Hf6Bhh1Zr6F9c+PokRamht8DafoRT5aVtDf3jm48n/uyozqZr6Pfv/zjHh1aV/pMnXkO///DnxeKcn5bVKp065vsP75/8fEy3KfKmvbz//rtvvX7Fd3T7H6/CUJGpJ3AlAAAAAElFTkSuQmCC", "reo_av_bg_3": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUAAADyl1ruiFr1pFv3t2T4x23qe1r61XT2rWDthlr63Hf//wDpdlnzm1n613XpelrygVHrd1rpd1npd1ruilrthVr7x2rpd1rpd1rsgmH4xmz92HT613X62Xb/gIDznFv2nGD3t2X3tGP5yW7ui1n2plz51HT/1ID/v4Dth1vuiFrxk1rxlFr/qlX1rGD5yG773Hjxk1vxlFv1pVz/vWb4u2b4vGjbbUnfgGD/AAD/VVXtbVv2pVn1oVz1oVv3q2D3rmD4u2b4x23/4Xj/kkn2ol33rWD3tWL4xGv//4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADP7ReCAAAAgHRSTlMA/v7+/v7+/v/TRQEtLmjRDhZOc0mvEZGwDs8TNMsCSxJV0q8rqLIGBGyCZqwDMG6QiNRqCS6pBwgBAw4sgNBAjJQmEQdY3mCUAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFX/LpYAAAMBSURBVHja5ZtpU+owFIbb9BJtK12BFlpUQBBRVsV9967//w9dLTuULmlyMg4Pw/jxmZO8NM7JqSB8Mx7MgwDzAcp4YDmujlfQXds6YCu1XbwV12YjNy1HxzHojmXQtd5bDk6IY91T05ZtnArbpLPGDk4NBfWNjYmwb7J5LR0ToltZfj4uzoBL+vO6s3FG7DuiULk4My5ByCxMhbQ7fetgSji3qR4ZOqaGXk7uNSh605gNGVNFT3hymDJGdD+ymaxeRB05Qc1lBt5Pc+w+G0XEhGJMzYeMvJ/mw0hxBzGjE+UtIIacRASLpTcqYEWmYlTc5j1DjDkL954g5hg8FnrrYhcQAIVN708ZQix34ZO1JV+GDCPeOKcKCIi1XVZlKLGs8il4vWQZTiwDP7TCT6kOpHjpYFZHkOKleBUQKIt4FUVRROIEgL/D+UqLwMwzDS2e5focWnw+FV9Aiy84bbEoTv65z8OL83y2eLbJQ3jxkE+2ZukawYtHgVjkwJf3mIf4mKc4z0Oc5yk+2inx0U6Kdy/VeW5PLkmUJOjvl7grcSDoSDzDe5+DY7EJL24G4id48VMgvoQX/wrEj/Dix0lXHl487dY3+WSLwyZfTsU9aHFvdvXCaYvBN7k574G87EuQn5dFu0naB+T3UjfzFVL8utTZ6/0ApLfczKzDeesr3dsanLi22igHK7m+2igX/vApWBDaQCXX2+vXMDU+BUMF+zrkim8MIR6HXS6+sfe+hd6mltiLS+EXyDUOyZpwDZ+sCVeVHEMqpe1jEWOW4veoQZA+O28/euamwcr7N2bIqM3I3PgXN97EJmCVq/iBrlIFNtAL3umLS8mG9mjXXEnoFQSPasIaib10zY1umlFUldqTpK+mnL71c7m9XPavn37c2GvtZablkQxYq1pWr0Y6yu5nKrrlC+QoVVJtVcn22sAp4Xprp5nflCBRU9CSqClpg1NaSRyzltKm+wLQh5YgZ1Xtg8UrT54yiJBXB4onMMTXNu3VgeYLIHi+Msf3hG/Ff6tyrSgUnQiRAAAAAElFTkSuQmCC", "reo_av_bg_4": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUSLEYAAAD+4ZkYNEsSK0Ve8eUSK0YRK0URLEUPKUgRLEYSK0UiOU0xRVbz2ZUQMUUpZ3ZV19DYxIwpVGf7/PxHVVmLiHBXZm9zdmgCQEI2iZEbRFkAAICZk3XKuYdmbGNoeYlBpahItbVa5dtd7ePjzJASMUoAVVUgIEBQy8d5iJaroXyyusPDydAxfIa5rIEfTGBZYl9g8+eKl6S8xMvU2N1fcIKbprGqtL3e4eUUNEs3TWIweIMyfIc6kphFWW5db4FAqqpNwsJU29NV//9e8uZg399g8eeBj52imnm9sIPY3eHq7O4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuO+wKAAAAgHRSTlP+AP//0P5LL6wQbI7///8Q////////////Bv//Av///////////yEDCP///////////0D/////////WP9AgP///xg/QAPQEKj//////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANmS1I0AAATMSURBVHjazZtng5s4EIa1FlYDDLbBuLdkbW/PlrTryV1yJfn/v+cAl7XXKgiDyHzjg/SANBqJeUfgrCIDOdtRilOj1BQYI5tY4MAswhAuFbxgBAiNsEUpYA/ZFnB+doHELBvRYsFLZCcdt6+DjxGQm42WhYE9tul0+jEIHh2gMkYLAXv2rsfoJgimEIAi0Cpwj+31B6PHqQsymRKtACNL3j+EogGw0Algjyiw7du+PxCuL5wXjFTj2W7W6/WZeNJZLjC1lRM5exWDX7clQYXqg1Wzm9j8dQyu+zI/R7pglsV1+8kXNwfygLLSAtuZ1sybebPZ7CsWtuVlB1OSbbHGbu23lQGFT+aBPQsUahbNBsYFc/nkYzAtnMslAxNcHvkluEdAKUZ6cvCwJG5MHkrBNijNbBkYgRINi8FemdwXgeQATEoFAyICM1CyMT4YCyOyA3NQHM5xlHLBgoF2wm6nG7ma2LhRpxtC8WADlUc73VatVjvv6JHdu0at1rgLxecCoAqV4X+1xM67Olw4Shs1ro48e3kEFnnW5Dzto9bRmWfYWjdqQaF/bcE90d4waeQAO5u3bR05mNV7ARbGrPv1yzc6WkM9XoPHUHj624KFm6F7lX7y+F4L3G2I3tY6BIuDNAyvxq3WXdfRW8SjuNGYuxTQAVi2+7v3k4mrG0KccDIJuS9r7YMxMGh4D2ybBNt7YMsk2HoGI2DU0A5MzILtHRgYti0YmwYvNmBmGsw2YGIaTDZgYNyGKRibB+MUzMyDWQq2zYPtFEzMg0kKtsyDrRQMKrAEvKoCvIrBtAowjcG4CjDWBOf7fYMOF6xxCnAfbz78ro199/R0eSL43dsguNT9Zvc6CJ7co0OIFviPvOAb5zSwe3n9vq091NGH6ynggHWcy3Fdfe+CnEZ7Xj3w/YF+n36GtDEv17yIwYv0yb9oNi98zS4yJcqPuP240adt5ILzRNaYa4J/S6WBN3qN/Iu40dcYvEzBSRcqeQHkEEOO7TZB/bXdFmHyGvULzVFTyj/cL47Fqi+7gwC8jV/+VR/o9yETvLg2mNXrfz8ffWC73/ehtn/KJD4h2e//un/YE+uTuURNaaOfqj3eDqs60Ff3C1PZTxuuYIpT8LCCKa4kFUGqT76cgYrSTdUl2CpLKUr/GKEb6p+0oBPyc6iHSVSZe4WJrtGaQM20cSKGjBxl2liWKF8n+SO9RHktY6JcHDajja6RSxpoAaU0oBRDRjopeqeRWQwRznJUrPyDjpU2keC1HrWGnuD1r0DwIhyJD4v85LwR20hT4msljcahWLwGSpkehp1RJ3I017HTHY26rkSuB6b0comMW/4mhX40qb6kqpcMxQnl7lJYVoDCzFQmcGp9iKHCF3NFRkNVWdWqnLKq1Y9bSFaKa9OKigW9wssjs/mVV3hBaDbusvgS2BxxI0PRbxlxMlOZs1fAcOcpcy7io1lZpeyKz8UnFO+/rMPNntY6qXg/SVPsu7cTXZq6rrB/LyS9oPHd1AWNNJDtrqR8C4J/oKkrKekujVI3a79/e6P6aySoV+y1I8qsOFs7lZ/sLUbLuGhFkytPh04+aA/2Ljt5pV4tY8902J/NZ3GW27IZNnOZjmKU2C9/Pjw8fO6dmbzFd7L9D8WeR2o3w+ynAAAAAElFTkSuQmCC", "reo_av_face_0": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUAAAD+21z/rDPBaU5mIRP7xk32u0r/tDr/rDH/qzD/qzL/qzLgo1X/qzL/qzKQVif/rC63hDn/21zUmk3/tyj/3Fz/3Fv/21z/5FfJelDQhlF8PR6ncDH/21z/3Vj/21zfoVX/qhz/yCz/32AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC7y4VUAAAAgHRSTlMA/v7///7//k8wjbD/ym3/F/9r/w5OLdUN/////6kXi/8JFxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEr0PUcAAAMFSURBVHja7Zpb26IgEICFAhTSr/XUYbf6dvf//8e1MvOAGDNQF8t712OPrwPDgGAUBQKBQCAQCAQCgY+RxFKq9IpSMkve4tzGUtExyrs8mUpbUrn1py0lNeFNndAlnKvLpmNT+gqydKiNFbXAWZrFKbVDfkZ7TXB8T5eKgki8p/EcGa6ZKf2IGePFmHFeSuO39y8uw0q0l6agIpbixaBKklEX2Df21omXKmuxdCO2Djlx5LUOeS5g7jvkOS8RfhN7rmYRQqxDdtHSrBEzr22tLx6CEIA5Q3fx3WttVtgy/fA2CF+dvDV7LYPeosrHwNvAvUzLsTafR7BJg3OBza54IdzOPVQJ3dNYibNxvTLAei6h7QQJjZiRJRjvPyJzJObkFdq47z+ciAV5Edb7N7SCxMN54VXE8+/AiBObDh6a2bTCSEjlEsQK1j2ogM0SsIBvg2taVDPItEjAwN5kpNVQ0sJBK4FspqUZn68hutFlOzt1aT262dd6/VPf65orsEWXNqeLdcMvnVd3pXtzsxIrnfjH9fZfOrHuigAt6TNdbsHEkIU1w4g5aF+gxIsZ7B0mdSaGvLW5EKcRYMeHYYYTg206JbrCZVVAGHAzQjs3WZTMhxi06YOYIx5i+00Q5UYcg7abBF78G7ShiBerCLTRZRDzzQ2+IIbsZirTyqdYtRyNi900Am4az9511cFMYtjGsWmR+RRzw2oPFPAt5Nm7Hh/eg6mLoTvlypBdmxZmWGWqCHpei1xXJ4jDH44YxbhjGKhYwBv6bmbQlk6Rh6p7XTMaf7aphT5dvEzyuRlDva5nzcgqpgHjj3L/amtH0apZoa0iwsURcjVqxK50FEVXRr5Hje/m0Pw0vOthNWXUzX/cHJjvd/qQn2yG3trVUf151JDHofYw6uHK3bcJNZlXj7UuvZME661AJoM4d/sZSP1qxaoix9S7z3ib3D4ta3dnLx/6VEtB55EvcpP2co78sZ9VX/aRZ3QNvsu9a28Jnp968t0pr6M3Uld5Q1Xvo0AgEPhf+AcZTDMbYhEu7gAAAABJRU5ErkJggg==", "reo_av_face_1": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUAAAD23c0oLjLBaU9mIRMmLDAoLjLao44nLTEnLjIoLjLoyLckKC2OVkcnLjJuamfOt6ummpHaxbcyNzp5c2+zhXZISUrmuqiDe3f33c723c2zpJr33s5YV1bOh2/43s//5tOLgnyUioPQm4j23c0+QUN7PS+bkIikcWK8q6HKfWX44c0cHBwbLS1gXl3/3tX/4+M8PkFkYV/GdFvUk3323c334M4gMDAoMDB6b2TAr6XhrpvkzsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADLphw3AAAAgHRSTlMA/v7//zDN/1FwrP4U/5L///z/////////a9D/T/z/NhL///+N////////KQkP/w8J/////65GECAX////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMEFSVoAAAN0SURBVHja7Zppf6IwEMZJFAS0KMdi8ahn66q9rz2//+daD6AYEjSTRF9snnf9Af6bzMzDJMEwtLS0tLS0tLS0tLQuJtP2PNfaynU9xzwLs2V7LiblKoebZWgqy2kpHK2Hq+SqGraJj8lrKYishU+RI5XqnAbdx9pWn0+sUEuZ7xYvdisJSeZgkESn+8HC+BJkE8wVy24Ti8i5EBc+26JcaG63hLnYAoFdcTAozDaWIX4Lu5fCxe65DEs4vyQNePN+ljTgNjf5Bx+YYZVt9KI2sVne0UEdtbXssAaM0FJpRdHNI0Zb+Srnmhri22AHRv1QWSnTbTrlIhTEqoL8k/J8uERfuuYhPwglddxBRQWREvMqvyAiRCqYDsk5iYahYD9gVw83Z/vtmMi+322htHbK5ctS4EfxQb0FbQG7PgRP0BE1+1FYiIgPB9unjvdLy2HqqRt1QmghF8FDdKKmW9wjKpOB4OBU8N5XmnsycKpNjgAXtckrv+wwHsQybxGXJvk/+gJ7S+QPTfnAaJE9sICB87cTAisErWQ8rlJixRvQaGYO0ietosM0EfKKD2pBTPpMX9Xrd00qt3wlyMFcTVex18k1q2/0ncalXYF1ey4txN+2P39FA9OuxKBVjEN7C/OBX0FriX2Qr0XAEWxfQBw8gS3bLGHwFJLUqYUIgRew7QibAm4wy4l2xYftRpgUMJeBZGDunR9qU8thmagPCvE+uyIkoD5wE8QVezllYBu0+/IqAt7H+B60oTgUAS9gM73ru+KKJr6xU5d9xzV0N9Ot6nxmtVQ3zFseoZuZdrYwoKmWq8m65Ra8cYzzLrkKzJrsv+Dd2+2QmfV0k3HfqpIaulPu4pAZwUYq5kxH4AHvEnsp0lebAocSkYBviRzD2CEU/AjxjiLZh3EDbD0IgY0xzbUq/0wXMMLnmnPyN//UaqtC8TY3lTUj7+lIONUcU73jvZtZNtVFhjKO7AeHv9nNrGP1PsttpEGYh5zzemKy32plEUH/JenEvEcf8peIAa9lHdUTYW7eHGJXRIQ/5X2bMEJsNIlFA5lfRYxKhdpNO5BSESdyvwIZnWpZA8O4CFk6d5NhH8exvSclH/qMeke4iaFKSRV2/mSo03PCGvV8bCjWgILuJc/GGTT+nBfgvY9kbZxPT+vRIEmSwfrZ0NLS0vpf9A/cR0H3CHmB1AAAAABJRU5ErkJggg==", "reo_av_face_2": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUAAADy0aH/5B3BaU9mIRP63VHz1JH32W/94i3/5Rz/5hvWmnb/5B3kt43/5B3/5hn/5B3/5R2NUjrtx5ny0qHz0qKxf1710qHy0aHIeFvPhmX41aT84EF7OyiibE/boXvasojz0aHy0qH/46r//yCygV+ygWDMf2Dfp4DiroX/z5//6UP/5pkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADS8K2+AAAAgHRSTlMA/v7////+/v5PMP+N/7AUym3//2tO/y3V//8V//////+piwkI//////8QFwoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIhjcp0AAAM4SURBVHja7ZrbgpowEEBJNCFc5LJgUdd219Vur///fQUvKCEBMxP0oTmvKMdJZoaQ6HkOh8PhcDgcDofjaYRBHCdZQ5LEefgQZxrECZVJJpeHfemZLE4njDamQ0ymDukY1tXNxGb0Hqyqg4QaYC3NgoyaET9H2yQ4frjThIIIJ09jHTlumCl9ihnjxZhxXkqDh88vLsNStJdmB4g4w4tBnSSnNgifMdDH9YGxOLYjNg45tOQ1DlkXMJs6ZJ2Xi2kTW9ezOOHGIdsYaUYI8Scda3XzEIQAzDl6igUnJ7OYLK8PQ15CDDMM2bau3hqjqkpR7aPjrYNmkzyW+9XkExnem2rBtgKZXcFwuFc3E9LHfIYS53K/Ilo68uYH9ichhkbMyAhXOVMVOlQ86r0tbq4odKBYkDs56raKQk9gYn6v+KTj/bYag+qYkfvh27buGEycjhWSDnb5obeDnUMeEj4xw798wYeJM/MZVk24+ZtMDJjh3qhDVgK5ZqQX7zpP74oPeTq1aS2N9Mt8/nWh9PavcNiiS9k8onnNN5VXdaV9czMSn3Y+tt1bfW9u/6ISq64I0JI+V+XWF61YdYUhFtZWxGb7Agd74hDwWo4S+5CkPrcQSfypFX/qxZkH2PFhmHLyYZtOoapjmjSQi9h4M0LZqg1a5kUM2vRBPCMuYvNNkMSOOABtN1kQp6ANRYEWJ7AdxQHx4i1qWIysBCC7mc0ka+8azc780H5kC+gebQvRLrlmLdqYBXjjeGiROS7m0ICPIWvTenPxrouB3ILulCf67CpOuRVFxUBuJR706Ae5rg4Rhz8MUcWoYxgBDXkLH+iT2QeONPqU71WRWFIFFYUqtdCnix/yPX/WNXSjLurKivoB449yf8vxHst3sziFuYiUXUTYOEJeSk+HtnVEUdtGpJB9O4fmu+5d17M+3Vnmf+wcmP9dqUO+0g2YV7aO6qXMLjZd7Vqa4aW9/yZU8ipgo9fa9PYSrKnl41Pi7Vevhku7fwOp7m1ZS88y1eo53jrDduPa1eskf/RZjgVdelNRDmk/Xr3p2JdP0WoHfFXuvQdQlbsb+WpXVt4DqZZlzbLaew6Hw/G/8A8nHTlGf68SeAAAAABJRU5ErkJggg==", "reo_av_face_3": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUAAADTqoeWOyLBaU9mIRPKmHeqaEvHiGqRRi+VOSGVOiGVOiGVOiG3d1iVOiGVOR2VOSGVNxqlVzvVq4jEd1rUq4fUq4e0fWC9gmOVOh/QoX7Wq4TUqofTqod2NiSWNSGVW0SpXkLUsIWgTTLTq4fjqo6VKhWfQCCiLhexZDcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABR8Z4oAAAAgHRSTlMA/v7///7///9QzXCs/pItMRX9MP9Nbf/8SP8QjtX/E///Fv+oCQwICxcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHnBsoIAAAM7SURBVHja7Zpr26IgEIaFQjygmaad990O7x7+/x9ctbRS0BggPyzPty69vBtgHodBx7GysrKysrKysrKymkoL3w/DOGYsCBiLw8VnoGGAe2LG4VsO9aYgXJrDJkLsLW5TYS/wmOIvzcjlNmYBfkeh1oll+H0Fvi6sH2A5seUk2EqJ+twyDJLqcC8CjKcgbzFcKqvbx3gSshoX460xmxoTzECXylwcgMCBOhg0zSHWoeUUA12bpzQ41gOW9s5EExfHmgJ2pcmShYHgKSfkmV3YIs8iiJrNZcFIuwjJk5fq5uGhShuTY83nEgQhy6Ty7yEuQuRiapKTQW4p19Akc16IKXoRST0T5tXPpgj1RN0O23NT1erLHxrm57ijF3h5Gz0pLeuw61cDIjRqh/1S/XYV7DocG+b+sD8cBkVwsN+1q3HdA63nhHrQRPbFy3kAnbZ3Ex1ggt6W295OgUO9kJrgh8rZXfcdRgL81XkvSJCbP+rB3hKwgCty9AgeAm5fiwgs2L4xlkol4UqTLzQbB6HdlBGu8d6VNagEWfBH2pvPf/DR/SuPXAZUmZ01vZ6X+snj8q7Aqj3Gcy23ejw3wXhXLqBdTMhbW3LgFLSXSNTBLqwLow+cALblSuAIsqjvFqIDHEA6Pq5KOkWwbkTCc0wZA2k2HNKdH65VS1hmAwY1fRTeEU0VIt8EYXrAW1C76aQCXgP7TYlMhSkowCAj7fwarrgIrUVGKgFIp54NVT50dtdKeEsKbWb6Q0X1rJXwFg/cph8qMsfBO3D3tgpZmE+rFiy6Y6NwLsEGVhe9azewtoAB1xsKCs4mD9qgvxWbYO/aqB7DQMEpxDueyRGMS3DwR+2oLeM9tZM43KWlfK554JjW6gm9KzOL9gNWP9Xcd59ZZ29j0oRyXSRV5zpOzgOXUZdJ3NpIJ+SNnq8Urq8zOuOos1/7q+fA/MwP+UmdgDNdR/WZ0Khvg96Z4VzftwlZrwoQY3VyedlMSF2DkF4SF3o/A8netazc0az9cRpuST6MY49nIx/6ZGNBF44pFUPYw94xp/NhEuzNuq+cuS2+nQ/onD/HfbwWmfM57bMsL4oiz74dKysrq/9F/wC2wTaq586fGAAAAABJRU5ErkJggg==", "reo_av_face_4": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUAAACufVZgNSmPWDVmIROWZkZ0SDWgbEZgNCldNCdgMyiNXEFeMyhgMyhfNClgNClfNClgNCmvfVZbNiWYYjyufVZfNClgNCmudlVfMyl9UDqufVZfMylhIyOugFVgMiKFSC+ufVawfFWufVZdLhexgE5VKipVORxmMxp6TiwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBUV1RAAAAgHRSTlMA/v7///7+/44uUP5OM85tsa5rGf9O7cYRjP/VbQsuF/+pK4sLDQwJChcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAElxTWoAAAMPSURBVHja7Zppe6IwEICTYCKXXIqCVlvtdo///wfXWmWVHJCZUD9s3q/08e1MhskFIR6Px+PxeDwej+dpRHHbFptPiiLMo29xLuO2YH3KfDGxdiFLr2zC/YTRhsxE+zrVyK7ZAOHSsfJ3GhbZoPai/uFQG5fMAmdlFm+YHaETbZoxazb4kd4XDMIam+6IQclxo8vgvDzJi4k5ZThiaFdmWGAV9or2sgw0a2R4MWsB3hfmAvtkL514WWEtDt2IrUOOHHlZ6ShgYW22XAdqpnxBrcWhk55FKbeep1xkOqAAc4RvHoJSgNlqrtAlGmK2qeu9yXtGTDXIS7OX0sDGvES1D0Ef2U4yLctvU0IlEinhW4FdA0lLHk6VcCG95gJV1rk5zY/yQDz+oUBMyrHUNszw24hvVa9bCxzjLR3DNcdcYQ5hEQs6kkTX3EqYmI5HdH/OgREvbAb40czlDhOCVrbUiqD7R4GzxNrQOMwDndyPuL04gwV8D2wnE9qWtLrS7FcCua5VzrWi/hMOmZ266amfvtlspkms/KQTA1aZvUwn51+fvSlrSvGk27lZiUuVOPj8eWW9qZ4I0JI+dyeGLKwDjPg2Y6V2p0x4cQDbw2zQ4gRS1IS0rsQZAZw0BZjXicOOuyLVnGjVQDhoiL92MQGFt8ybGHToE1AEHHQi8NW7BF6cWotzJ+L1L9CBMUqcwDJNfg4sQOYXjOsv4GlmaRLz4MrKuATJCPDQWB9Oh3HRlULERL9LHCsGBXwJWVtdq0ExBwdMSGHI9Xw+UF1byAnqv6MQjllXw2+VFyP3qOpM465h4Ov5gmBIE2imM+SlagMNGH27+C7Vc+8dOr9Z8k7HwVXuh7J3rB57pxSwiyvkWtO0Vpx3baQXMnfzqcBR1y21ffOPmwvzj92Qude/Tq6u6htto1bOjLW7bxMO+jlCnpAdeuUCM6xAKrefgRzGdo6aOOawe473XGHHYe2umeRDn3oo6IpMRWXSvjdkOprqKVptwnfV5NpLgVfHO/nuWJ3IN3KoqzP1qSEej8fzv/AXW7o0IyRq/PUAAAAASUVORK5CYII=", "reo_av_face_5": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUAAAB7Uj0KAgA9LiRtSTZSNikoGBEJAAAIAAA5IxkKAgAKAQAKAQBcQDFELCEKAAB7Uj17UTx7Uj11VDd7UDtCKR58Uj17Uj1gPy93SjI3IRZ5Tz2ATTOAUEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB1pmpfAAAAgHRSTlMA/v7//v7+TzD/jbDK//9ta07VES3/qYv/ERcqChAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJkr+D8AAALdSURBVHja7ZrZYuogEEABIUCIWTS17V3+/zev2qTGsERmoHm4nNfYHhmGgQwSUigUCoVCoVAoFHZDybo2zQ1j6k79jFTWhq0x2eXKlk40dU5vzUJkUyu2RZ1jYhv2CknV0rAIkqWZbFgc9T7aW4In8BoGQmVPYx8dLsyM7WLGeDFmnJcx+ePzi8wwtBe4qhq8GFRJOpYCtUeg7+eDxPtuviGrRN7oIfsGXOUess/LMye2r2ZxKqLNKSKtKY03qwTFg1KAucNPMacQs0GLJy+lPN8kB71XdCaxci0kuoTrLNuyvZre6BreWsVEV9jskqEwL9yispZ5hRJ3wTCv5Pp5vfEKUbvkRpi9cu1ablCxpq8wxZg7zEBxRV+kfXz6A1pB5GZeOSP++LgAjlhFTPDSfA23sCtMDapcNAo9f1EO3CW+/6iNE9P2bTnj8eImfoZdEx7/JlPHprRNBToJzKVLrMfhjYD1RIC2ReWOdOUNvv2Eww5dzpwW3kLmegJ7czOuKW690+56AjvSd3hxhThYa4xYw/oC6cQK8FqOEreQpJ5KSApxA+n4aMxyErCmk3JJYgrILFaQVoSm8JI5i0FNH00RCGATxOA2p1ksQe2mBGJYQxElbmGR/squwAnjeIeHzl/AbqYJicVhQgSPIA20aewd0OEb70fgjWPH0SdCzOF3IjKQXduhFohOuQlM8vG4kV0altJzsD/Aqwl1BaTgRVNgr2Hg53lDMEgBfYPB3vKdXf91e6+sGMHybmmva4gvGyCONcUTXOX+tb2Hh5oLZxWpUlwhDy7xzX3FU0ZEmnvri6doHXx1k/9KI/5zcg/5wfH5q42prurP637as1asZnhI99uEkfrVa21Kr5Vgt7U77RHWGu7T/gpkfLVkDSQxv0/7eAn5vGxrT59ZfugzbA26J7noQ9r3M8nHud9F6w34qc+uvS+t/rKQny79SH6QceivDOOZFAqFwv/CP9/uLaxMKHLoAAAAAElFTkSuQmCC", "reo_av_acc_1": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUAAAD09/nl6u7b4+jh6O3w9Pf9///n7PH1+PvV3eP+qTDz9/nz9/nz9vn0+Pr2lhTj5uz44b3a5ub8tEn4xnv1zZD17N3l5fXi6ezg5+3b29vU1P/d4+rf5+zb///jzKYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACtJkQqAAAAgHRSTlMA/f//l9IKri///0yTsm//Lv8U/////xNKcQcGJWAH/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJMsP8oAAAEaSURBVHja7daJkYMwDIVhZHwBhkCuTfZK/12uDWGWCsQk838NvJEtWa4qAAAAvKaYkt8h1vci4tSTP7+TSCPSK1d7s1akziWLXsl+6Ps+2CC1KcH2QyvXlThxrhx0FuxRJ7iT1XzSYu3dKwU32+BcudMZqiim3lY86zSSnZi5q6bzeTJ1U2ciUeeSTWnoNjNr7RrjfAu5r03zaA+HdtI869HmGRa5luDrGuxVgpdJvpxOl+dRq1xx9RWWsNJic5u5oDPI/j+3rAln7Y/SFt7klpkOWq91nPPW1yOXPGptiTy3ZY7DGqy2F9NzK7nl7UiKf61hiPdlmvNVx0rX73HsSs2p2oHvhmGPfyYAAAAAAAAAAAAAAACAt/EHMv0HKRrFEe4AAAAASUVORK5CYII=", "reo_av_acc_2": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUAAAD09/nl6u7b4+jh6O3w9Pf9///n7PH1+PvV3eP+qTDz9/nz9/nz9vn0+Pr2lhTj5uz44b3a5ub8tEn4xnv1zZD17N3l5fXi6ezg5+3b29vU1P/d4+rf5+zb///jzKYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACtJkQqAAAAgHRSTlMA/f//l9IKri///0yTsm//Lv8U/////xNKcQcGJWAH/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJMsP8oAAAEaSURBVHja7daJkYMwDIVhZHwBhkCuTfZK/12uDWGWCkRm8n8NvJEtWa4qAAAAvIKYkt8h1vci4tSTP7+TSCPSK1d7s1akziWLXsl+6Ps+2CC1KcH2QyvXlThxrhx0FuxRJ7iT1XzSYu3dKwU32+BcudMZqiim3lY86zSSnZi5q6bzeTJ1U2ciUeeSTWnoNjNr7RrjfAu5r03zaA+HdtI869HmGRa5luDrGuxVgpdJvpxOl+dRq1xx9RWWsNJic5u5oDPI/j+3rAln7Y/SFt7klpkOWq91nPPW1yOXPGptiTy3ZY7DGqy2F9NzK7nl7UiKf61hiPdlmvNVx0rX73HsSs2p2oHvhmGPfyYAAAAAAAAAAAAAAACAN/YHmNwHKST+gSQAAAAASUVORK5CYII=", "reo_av_acc_3": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUAAADz9vjzqrnl6u7pWW53sVX9/v7td4nxmanw9Pfd5Oni6O3rZXn+yk71+PrviJns19Xx9Pf8pSnwu8bzqrnm7O/z9viJtWfQOE/zq7n7uFLuyc/s2+L1+Pp2sVS0q4jMqZra5dr1q7vv48vj6e7l6e7k6+92slSyyKj7q7jzsLf19/ujr3nCJDvsbYD2lhP0qrn0qrrzqrny163j4+1tpkt2s1TbZnnZubPN3cviTWPwj6D5u3H3tZT4w3PwypJulEhll0dwrFJ4tlF4slZ2sVSXmmyGsVawtI631KrUrKHD2bz6s7f/zFf/zkv/ylH20pvq7vFbkDpVqlVqoENzrVJ8oWF2sVOAqlWfr3WNsGaezIW+wXy5y42s0Jqz06TCHTXKKUDaQVffcW3Sq57Zrabf6urf5+vf6Ozlg0Plgm3yp0jzp5j/qsb2tpn/tMP0uMb/y0v+xmD1yNXo0Nr109z66qoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZiBNXAAAAgHRSTlMA/P7+//4J///T/5T//zH//4///rOtr/7/kf/6/3CS/P76Lf8tSmlx/xH/Rv////9Ubs7/Ev9H///6//////b/yf8ME7nL////////FRE2uP/LuANj3v80Bv+xMv///kb/////y5UYQHj/////CbIRuE7VT23KMAAAAAAAAAAAAP1LUdIAAAOYSURBVHja7ZdncxpJEIbpmdnEBliyAIkokoKVLUuy5Jzj5Zxzzr//uhvBXV1dnbVg2R+un6pF1A7T73SYnlEqJQiC8L9i2LZfvOjPjx8uKKU2X7DsxlYYHitiY/rOXjwf/6PFlalh9PVyGI7UoVKFybsYwDsP5QjQsO/HHkD0Pbl69LXjGKW22jzcjUEDxOcgvKjRsFcEnYa4jboZ52LFBLSCwo921PM9Gofl5+9zzIaB5YcoFxhnzbiui19/pwGPh/3l5yb46GG7UNgc7hRhLEzPKw2Uc4PKJ4ExRo0AJiOeB6U/HtmbhYWN+Vwfbv4SPubi/c1nZ1l8cPUWvQoOKijsKAXp6ZJ0vRaGP3AChnPoPthSR2F4WWE8a1hUert6hNYvDd4gh00QkCqSZeWT6hOts0qFYfUf+yw51CHC8JtD4+Y5mtULuRPy+w7n2FWOoRSrRgtLrpO7kANQtM++VQGuaGEOYbLqfrqG9sdpPM7lOlTWmt7j45iMUs1bVwf3Nehcrgp1Gvhu7SKHovBgHmG0vWacPGZP67TezpJ+GvbVGMdVzd3d3QHlt7MNFGllAtxnHAnVnlW4gOt3TKXiODXQ06IGuHv7nprQsKzXL02GyOPDwHxkMuvrmTmi3WavDj7GTeNi4bD1Fn6WbljlsrVKo03Lunnd4zDQcI3emUq+ljHr2NXmKS7HmIMgk3FVLcvmi74fpa7dsJB3Pm++bVlLb6U8igetiJMfGCrFej4/+mm2zWwvs+66e1q8++yx36WxV5dQ8Vrq+tLSm9ROuY8/BeAcYymS+/U6zHZs2HGRWzI+XKTNK9S84n+1ZEf2Tnc5ZmEnk2dhTQUJK8kPBZybH9ePS8JXXtt7twT/feTav9LPRzXNlciFmFh4BSe1BuovMKd7z5zV/wx/mc/WYdJdwU5+/GK4yuXGvUaDdVcxp8+e1bdWm/ssmD0+oT/FLxJn2IO0bpWpeO+MWLd/lml9qwyT7tqhiusmv3HQqdC6jcJ34X7Zurl3tmn9D8YxRuEsZTr5+Wz7PvXB997HtlT0z56qD7GZp9O682Sbt30p+Xb6yju9cGjt9RJezqbdNZ28ulLdv81OFLAd3/embX0G4YglxyaiZEv2OVZPca63MkPn4jizjaTL3jnt6r1opl6NvavU6/VKM1yX+ZL95Uv4x8ouQeklyAqCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAjJ+ROVG0fj8u8kjAAAAABJRU5ErkJggg==", "reo_av_acc_4": "iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAMAAAAOusbgAAABgFBMVEUAAABPpOUcY5lEl9YoLjMbYpgUY5sbYpgbYpgseLIYY5gia6M5iccaYpgcXItPpOcbYphNpetPpOVPpecoLjJOo+RPpOUcWYgPWqQkJDAoLjImNkIiQ1wqergygb1EmNdNpOUXLi4eU30ZWIcnLDEoLjIiSGRAn/8fTXIPWpYXXpAcW4oA//8pLzEoMTclQFMhSmgkb6gkebYrfbgrerkqe7g5iMM2hcI/ldRHndxKnd4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAak8D8AAAAgHRSTlMA/v7+/nET0Iv+Lv7+UPtOsQ6wM8aMy5AJDIv//7H/sW4L/2Y2uv8IexFX2AFd/8JWyxUvcYGr3kGC0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANn0YGQAAAIdSURBVHja7ZiHVsJAEEWzk7LpgYigKGDvvev/f5ghAgYIKVvmHI9zf+DyZmZnNxgG8Ud4fh2NXp6QpVvJ9iTMGI8Qpd2DlBWYJF0UbbJk/eEr0a/ts3I+tcbupmwzHxonilXypsu7zWp4d3Roz1NWixdpaG+fNSCwlYvTJl5mgovd33mxFZuTht4sMqisdpc1JgDw8Qud1xo41uJYIgRQ1+Z+C3HWZGXFTlhbMccPzNhUDBF2h+dijjzSC7GKyOftvNODrCZyIiRWMNipmFj6LN8wMTFHnumFWLrWB6JiG7nFs+ME0JEUM1ExoN3Eq2Ifd7bMhThCXR8Fsa1kqM0FSOIJM8deAEsEnheaVS8QFeLHFWnBXi7/FUstTRsq8cI18ViJOIJaVt2eilLvQCM8s2RjSok70JBCbFAgjqAFs9i/p0l8gTjQjlwdKhC70JYgLMyW8K72QRJH92RtAj9wLPXo4uJeaz8Wf4FE4oHPLGuqHoiJY/HAd9aU/Qsh77F44MHtsNc7HZ5IB+a8XbsvZW7DPHB8du/Pz6Lj2w2Pl9ynyzXA0Z7V213ZoVFH39qYbelMu+bNL8o6t9x75yq2yr35r7K5rsDGIMt7elix1TbeH5J/BDxY1rCmGeVq6W/Tk8P6OSh7Byr8M7HqRbbWbNfAYnnGuWPgUZgzVG9hzrC9eWzbdW2DIAiCIAiCIAiCIAiCIAiCIAiC+Kd8A+F/ISBFO+RAAAAAAElFTkSuQmCC"}
SOUNDS_B64 = {'reo_ukulele.ogg': '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', 'reo_pu.ogg': 'T2dnUwACAAAAAAAAAADgaMElAAAAAFRY+kIBHgF2b3JiaXMAAAAAASJWAAAAAAAAHp0AAAAAAACpAU9nZ1MAAAAAAAAAAAAA4GjBJQEAAABHLs/TDkD////////////////FA3ZvcmJpcw0AAABMYXZmNjAuMTYuMTAwAQAAAB8AAABlbmNvZGVyPUxhdmM2MC4zMS4xMDIgbGlidm9yYmlzAQV2b3JiaXMiQkNWAQBAAAAYQhAqBa1jjjrIFSGMGaKgQsopxx1C0CGjJEOIOsY1xxhjR7lkikLJgdCQVQAAQAAApBxXUHJJLeecc6MYV8xx6CDnnHPlIGfMcQkl55xzjjnnknKOMeecc6MYVw5yKS3nnHOBFEeKcacY55xzpBxHinGoGOecc20xt5JyzjnnnHPmIIdScq4155xzpBhnDnILJeecc8YgZ8xx6yDnnHOMNbfUcs4555xzzjnnnHPOOeecc4wx55xzzjnnnHNuMecWc64555xzzjnnHHPOOeeccyA0ZBUAkAAAoKEoiuIoDhAasgoAyAAAEEBxFEeRFEuxHMvRJA0IDVkFAAABAAgAAKBIhqRIiqVYjmZpniZ6oiiaoiqrsmnKsizLsuu6LhAasgoASAAAUFEUxXAUBwgNWQUAZAAACGAoiqM4juRYkqVZngeEhqwCAIAAAAQAAFAMR7EUTfEkz/I8z/M8z/M8z/M8z/M8z/M8z/M8DQgNWQUAIAAAAIIoZBgDQkNWAQBAAAAIIRoZQ51SElwKFkIcEUMdQs5DqaWD4CmFJWPSU6xBCCF87z333nvvgdCQVQAAEAAAYRQ4iIHHJAghhGIUJ0RxpiAIIYTlJFjKeegkCN2DEEK4nHvLuffeeyA0ZBUAAAgAwCCEEEIIIYQQQggppJRSSCmmmGKKKcccc8wxxyCDDDLooJNOOsmkkk46yiSjjlJrKbUUU0yx5RZjrbXWnHOvQSljjDHGGGOMMcYYY4wxxhgjCA1ZBQCAAAAQBhlkkEEIIYQUUkgppphyzDHHHANCQ1YBAIAAAAIAAAAcRVIkR3IkR5IkyZIsSZM8y7M8y7M8TdRETRVV1VVt1/ZtX/Zt39Vl3/Zl29VlXZZl3bVtXdZdXdd1Xdd1Xdd1Xdd1Xdd1XdeB0JBVAIAEAICO5DiO5DiO5EiOpEgKEBqyCgCQAQAQAICjOIrjSI7kWI4lWZImaZZneZaneZqoiR4QGrIKAAAEABAAAAAAAICiKIqjOI4kWZamaZ6neqIomqqqiqapqqpqmqZpmqZpmqZpmqZpmqZpmqZpmqZpmqZpmqZpmqZpmqZpAqEhqwAACQAAHcdxHEdxHMdxJEeSJCA0ZBUAIAMAIAAAQ1EcRXIsx5I0S7M8y9NEz/RcUTZ1U1dtIDRkFQAACAAgAAAAAAAAx3M8x3M8yZM8y3M8x5M8SdM0TdM0TdM0TdM0TdM0TdM0TdM0TdM0TdM0TdM0TdM0TdM0TdM0TdM0TQNCQ1YCAGQAABCTkEpOsVdGKcYktF4qpBST1HuomGJMOu2pQgYpB7mHSiGloNPeMqWQUgx7p5hCyBjqoYOQMYWw19pzz733HggNWREARAEAAMYgxhBjyDEmJYMSMcckZFIi55yUTkompaRWWsykhJhKi5FzTkonJZNSWgupZZJKayWmAgAAAhwAAAIshEJDVgQAUQAAiDFIKaQUUkoxp5hDSinHlGNIKeWcck45x5h0ECrnGHQOSqSUco45p5xzEjIHlXMOQiadAACAAAcAgAALodCQFQFAnAAAgJBzijEIEWMQQgkphVBSqpyT0kFJqYOSUkmpxZJSjJVzUjoJKXUSUiopxVhSii2kVGNpLdfSUo0txpxbjL2GlGItqdVaWqu5xVhzizX3yDlKnZTWOimtpdZqTa3V2klpLaTWYmktxtZizSnGnDMprYWWYiupxdhiyzW1mHNpLdcUY88pxp5rrLnHnIMwrdWcWss5xZh7zLHnmHMPknOUOimtdVJaS63VmlqrNZPSWmmtxpBaiy3GnFuLMWdSWiypxVhaijHFmHOLLdfQWq4pxpxTiznHWoOSsfZeWqs5xZh7iq3nmHMwNseeO0q5ltZ6Lq31XnMuQtbci2gt59RqDyrGnnPOwdjcgxCt5Zxq7D3F2HvuORjbc/Ct1uBbzUXInIPQufimezBG1dqDzLUImXMQOugidPDJeJRqLq3lXFrrPdYafM05CNFa7inG3lOLvdeem7C9ByFayz3F2IOKMfiaczA652JUrcHHnIOQtRahey9K5yCUqrUHmWtQMtcidPDF6KCLLwAAYMABACDAhDJQaMiKACBOAIBByDmlGIRKKQihhJRCKClVjEnImIOSMSellFJaCCW1ijEImWNSMsekhBJaKiW0EkppqZTSWiiltZZajCm1FkMpqYVSWiultJZaqjG1VmPEmJTMOSmZY1JKKa2VUlqrHJOSMSipg5BKKSnFUlKLlXNSMuiodBBKKqnEVFJpraTSUimlxZJSbCnFVFuLtYZSWiypxFZSajG1VFuLMdeIMSkZc1Iy56SUUlIrpbSWOSelg45K5qCkklJrpaQUM+akdA5KyiCjUlKKLaUSUyiltZJSbKWk1lqMtabUWi0ltVZSarGUEluLMdcWS02dlNZKKjGGUlprMeaaWosxlBJbKSnGkkpsrcWaW2w5hlJaLKnEVkpqsdWWY2ux5tRSjSm1mltsucaUU4+19pxaqzW1VGNrseZYW2+11pw7Ka2FUlorJcWYWouxxVhzKCW2klJspaQYW2y5thZjD6G0WEpqsaQSY2sx5hhbjqm1WltsuabUYq219hxbbj2lFmuLsebSUo01195jTTkVAAAw4AAAEGBCGSg0ZCUAEAUAABjDGGMQGqWcc05Kg5RzzknJnIMQQkqZcxBCSClzTkJKLWXOQUiptVBKSq3FFkpJqbUWCwAAKHAAAAiwQVNicYBCQ1YCAFEAAIgxSjEGoTFGKecgNMYoxRiESinGnJNQKcWYc1Ayx5yDUErmnHMQSgkhlFJKSiGEUkpJqQAAgAIHAIAAGzQlFgcoNGRFABAFAAAYY5wzziEKnaXOUiSpo9ZRayilGkuMncZWe+u50xp7bbk3lEqNqdaOa8u51d5pTT23HAsAADtwAAA7sBAKDVkJAOQBABDGKMWYc84ZhRhzzjnnDFKMOeecc4ox55yDEELFmHPOQQghc845CKGEkjnnHIQQSuicg1BKKaV0zkEIoZRSOucghFJKKZ1zEEoppZQCAIAKHAAAAmwU2ZxgJKjQkJUAQB4AAGAMQs5Jaa1hzDkILdXYMMYclJRii5yDkFKLuUbMQUgpxqA7KCm1GGzwnYSUWos5B5NSizXn3oNIqbWag8491VZzz733nGKsNefecy8AAHfBAQDswEaRzQlGggoNWQkA5AEAEAgpxZhzzhmlGHPMOeeMUowx5pxzijHGnHPOQcUYY845ByFjzDnnIISQMeaccxBC6JxzDkIIIXTOOQchhBA656CDEEIInXMQQgghhAIAgAocAAACbBTZnGAkqNCQlQBAOAAAACGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBC6JxzzjnnnHPOOeecc84555xzzjknAMi3wgHA/8HGGVaSzgpHgwsNWQkAhAMAAApBKKViEEopJZJOOimdk1BKKZGDUkrppJRSSgmllFJKCKWUUkoIHZRSQimllFJKKaWUUkoppZRSOimllFJKKaWUyjkppZNSSimlRM5JKSGUUkoppYRSSimllFJKKaWUUkoppZRSSimlhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEAgC4GxwAIBJsnGEl6axwNLjQkJUAQEgAAKAUc45KCCmUkFKomKKOQikppFJKChFjzknqHIVQUiipg8o5CKWklEIqIXXOQQclhZBSCSGVjjroKJRQUiollNI5KKWEFEpKKZWQQkipdJRSKCWVlEIqIZVSSkgllRBKCp2kVEoKqaRUUgiddJBCJyWkkkoKqZOUUiolpZRKSiV0UkIqKaUQQkqplBBKSCmlTlJJqaQUQighhZRSSiWlkkpKIZVUQgmlpJRSKKGkVFJKKaWSUikAAODAAQAgwAg6yaiyCBtNuPAAFBqyEgAgAwBAlHTWaadJIggxRZknDSnGILWkLMMQU5KJ8RRjjDkoRkMOMeSUGBdKCKGDYjwmlUPKUFG5t9Q5BcUWY3zvsRcBAAAIAgAEhAQAGCAomAEABgcIIwcCHQEEDm0AgIEImQkMCqHBQSYAPEBESAUAiQmK0oUuCCGCdBFk8cCFEzeeuOGEDm0QAAAAAAAQAPABAJBQABER0cxVWFxgZGhscHR4fICEBAAAAAAACAB8AAAkIkBERDRzFRYXGBkaGxwdHh8gIQEAAAAAAAAAAEBAQAAAAAAAIAAAAEBAT2dnUwAEIlYAAAAAAADgaMElAgAAADAjCTAtWV12c3Jvcm9tcXN5cnJzd3NydG9ubnBucXVybmx0b3F3cnB4cW1vbnFzbWhoPC/vbFftgwWola3/Jj1+0b21JzQILf7thKZpnl/SYCTUqO/s2dPZ3d3dsO1zDDwVANCHqwHyzIARLFvnMUGNjvMlbfBQrU4CHWdWA6Dz1SB9HIAZMoUYVQtEvYXAYVeLtkV1TXWQ0ufu0GYYLCUFd0UAo4YLnKHuX+n2rfJvn6aP42PcaP67/Mo96jVbHpOZ4viINxLVj4/Yj0agWFp+9WoszpZWV0K+WCexKapJxkyq5EPlPwIaeqQl78MDVs3cMH+X6BUYQEuR204CeH6zOgYBK2PY0xtAog2wOQMcjs3Wooe4ZiKTxCKRk4RsDfT+nwq7KSCH6sLrjmXW3E6Tm9/QVf2IPNaDFGV26Br+4K5TTjDSG6+At56405PN9errfWTYGyUizorzHPFb3rqEVPatAOCGPbzwOyA9C2vRtq22AAKaPrA+rwsMAqC2C2jaFABOIb86b6drmAmZdOg1QBlXve4gMbzVNq3JJaaMEWwjvgfYn6PUCtuWkeaYT9WOCdG+YqHF1q1ezfY6X1S31Mr8/IDIqhVIcu5D6m/0AB7rxCmvwwJYc8McHvhJCEAz27JtDvBwScINQwmbjwK0WYH7UQDAfivEEqnk3FHxENo8sf/gDWJ777UTkmcypZbmQGextGbaWtJa7tiJiN7K+0TW679DZJybDGxUbfGSjFqsBC77W1OtnWv2TWWOLOEqAp4bRamMQwNYc4PDh27FhAPNis1sCaCsH0hSBkv4ehTgGAC/IVB2NZlRzkzay0Xu+Y2mpz+VhuQbSuKbabF9ZHk/KFcrg6jwg61VJr1TaZvcgEsVuODscN/SMIV6bUD1tBX1tnrGwB5hhTJaWf5vAL47hSZD0wDW3LBNbeFbYtKDXBpsWwywcv0aTHcbwPqZAi9n4NcAcB4tO+m6vTKW6rDXlHh1qmDokyRX3q+9lNCs3V5dskzwVk90qtrhW1Rs/wdIvCJG5JwD1EdqUxxH7Vw1K39wTj6PT8trLrLctzmIBL4bxanUQwNYsxvmHxwHVBhYkGQ2d3IA08YaqnkDcPUk8MeAJwmAhMVrrS6AQ83pg0p66ZLSV28jHQOOoelGMoAYwg+I/ELIVMdZpkeXU9Xy1SIoG2bzOsWT01qOR6Vo3P3LsxUarctdZ0qbZVhWA94rhVTqrQHghj0lfAQ2AQbbZrYYwPKlOvSbXsDJtgL/C/BjC7CU9tZ2NWYUMaPBNIE4C4R5Mk7/EFFuBE2mg+GL4hgOeqnz46u0ngOcA8IrXcKTgY7qkJlFFWdxe2yXqNq/d+JDfJQCoqIgOze+K4WEh2HgsOYGTQG/JBYgmbANthxA4E8hWL/vArMvBJikwNEegG7Nh82eDWzcjh2eCtGp47tzcdHbaeJCTxBZLHaobUcEcdiazQI73izQ6EwIA58Y9fdr7n0/lZTEAdM64h8mBP7NvTtsNAaMiP9NDr4rhVLGYQAsucGpCqJCALJt264ogEu1XkJdkeCkBXg5BBwTAcSxfmEzV0qdJ666+peaaY57cHmai5Jr0l1CUmaIeyHq1KFBsWyystvexz1bUTDlMlyA/1dKUJZ13xU+S37gOzC3sGfAfTbP6up9XCK5XQC+G8WlrMMAWHPDfjbchPTAY/XYtnMA51fOYTrZK2H+H1A3aeA4BgBVsssCNxNr1qd0DiQnP2l5KTZOUyvrleQxfID+06i1Wl8pMnFOZTcFb0pUQD5SyGjcUUaquMhCpYODyC8nafSy2lRcNrtTvkJ5RG4LVC4aUW0AvjuFxutQANbcMH8PXyChk3C2bTsB3LSuYbr1ANsvFHhiBaRTgJ7Z/32hUhrP85vR/eGst7W6L1Itznbqq28b2oDyiFiDfz0sE69nOCW1iTBHeiij/o7mrZuEFNCeEwUTBAlEjfNVEwxcwPke20ub3Xt/nivFpexDA9jihv0PHBcIBzx2wnayAeSkE6iUIAFhIMCTCFwtAUAZasZn8x6LIjl+kNBrIH+98rbGrcwUqNPpmirst+j5fS8YIZVZ5X+rV6MSzvu+YrxVF9WhmaZZNW+jLPpsbZXeljBrW1PYsFTDja4YvhvFpQzDAJi5Yb4XegUDULQTNrMdQGFnA/13mYDNPwJ0G8CrAjQQ/PTh69nXyxsn3CWmIXQKJrR7AfJ2ebu4ZHUtZ5UXGVeSkP2GM8WwlFqLQ1/Iu37W2t80e5vLQHpRnapjhPwUKVIkaSBrjM15b710AL4bxY2HYQPgBk0dfmBSpzDUJ2xn2wCPNF7JWjMG9nlUYL0C3wC8RbT6JUzQQEQ1HnMO0MQx7MryEhG4h5D7TePXqsfbQ+MaGzXDp0IpFwb/u6aoWpKy5k7RDiPHcvvDCWUJAUdT13og52IRqgUfZCfoDM3Od5EDviuFUuplAWA3bFMLSoUKCUAiYSecBPBh7RE4H/WAQaAEuVIALxoA+046k1/wNMYloxvac6u8Jn/SaqI5DkLs6LE04us1CwKKrvx7XoETu94aTYcDZYjvWijy4KZd25bt9XrMtqKge6M2QXXqlNRPqq6nAL4rhVSGYQAsuWH+Hr5gE5AM27adDeA92sLRywyY3q7Aiw0wtBNgdldWWsKGcRGS0Rh2FTYW0jR7vOma/H+mzim5Jzhr0Rla1DMX2BA832EVl0rKBjFkrgiLDYIVGympjKkmdQXHUnmP77DQyAVdhBqxDH4rpSWvwwJYc8P+5aFdIBydpG0zWzbAaPwILPIK+LoR4DEA3F4oMFWZac2laSaBKMhVeHwWy2hXIUvUcbGQUIgbeg9Viki8eZTtxNYpXYf6iy2bY69WujFuTmq+4OyqhN/jn8Hz1+avjDei+gOpgMrNBLUAviuFVMahAay5Yb4nfAQEwLadbTMB+atkK+h1ggUc/wH42wA2awAF6n7jZSZ9K5jvLX3ckgyIhveLfZnCTsUdRtVuoQzK07NXkFI4qa7oalNl1ChkQTjLpkQd/gD3c8EsKJHOgqjU7p76GfqBiFcA/itFiVKHAbDmBocXfkB6kKjYzpYDOPDpSNbTEHBnhfrQAjZrFTAf5YzvHMNZpsQy/36yXJKTQegREolXPTEwEiZnXOFGFloAz1MM8xcrqyXWMKSGgEWyKVcejEK8ze1017IfliofjPcNlElN2wK+O4VSxq0B4AZNAS+hYJFIONuWAALHEawfxiV8PgH4ZAUqSYEu3+37vDy27i+ie1lltt9VZbWSWS5He5vLWaMotu1AxtTv3NBu4SQCMTgJV/qeg/BkI6TLai4SNUnHtmdTRFyaxilqPKtWDqXVE74rhZTHoQGsucFngagQgErCypwYwKr3CebqSKgtCfByCLhPBPCgSnJD5Pp0f+SUtjfSM+h4WW4vcX4FlbAnLWH8BCUc4tWZo3dbZNB/QQOqPTjTxmXlY6U3PHLSBPX+1o/nSV5D98phQE0NSPcU8gG+K4VShqEBrLlhPxu+EsMD27Zt2QLwOZnB0cp2sP4PwFUB3yYAxOBtbsihWV4uCEbNNboDwJqzod6cUf4sdrU2iLrW48ub2Vh2TUeimbhhoc2KiGG8ky9bfYCH7xKBlIVllb7yF9uP427s8ia5Rn4rpSnTSwFYcsP8FY4D0oFi2AmnADiWa6ge+AIvaxV4cODHCo7A6BO3uzMsZmzGQtIw0G3MAZf9Xq5vGNYCh8ZvOhsWq5ru+la3LxnHG6mDgbTuEs7LhKKJ1cetxbaueWtSeec2ZsfQknSErV3l9XMNnivFDTQFYMkNe3jhIyA9SNh2MeEYwAUdF/qDE8DNZBPYLahsr0CT9Jwvtl85wonesicW5PvVC19RvYLENnrrjXovedeVp2jG2l+fxiHBiTlOEpVaJVIVnXlcfzo5SEy7o6bi8wJZd6FymDwx3XJeytBiE+IFnhvFJQvDAFhyg6aAc2I5FkXbtp1tA5Q2FOjVkYTpR4C/IuB2ANADs80bZhcy8fNaWed4nMPoyOhsdMxfIJzDbbdU5uolUL4rnbQq3kQXVeUSLJKY5C/0rUCsu23WUQiSVGNqYCzBu7BVp4ORCBYyP24G3jtFpRKXArDkhvks0KoQsLA9tm2LAfzd7SV2oiehOyJApwXARgEojfqxfTrDeIA6wAlhzt+oK3KG5PSDHLxjN6ZqHzigiEmSVeHsJxBccQlbCGnjoZF3nNcHQbSpilOcMrUm5VlhIDXq3WPYtwL+K0WpVocGsOaG/XX4AuNBMcEkJ4DTX1OYDoOAo1egrhvgOBFAWC02RD4iQtXjeI8amZq6S3LLiT318VisULpgHq+sw8EJZEpH72YxTlhD/b7f+jetrQEfpeeQuVhnRF15Ici5kq2zPXxi5yl+K6WNxWYArLlh/i98BSQgYXtsZzMgB6dXMD3gChhsKzBmCxwnCaVB43RrtkfewdywHJLseSElmxgVWM4jaGJbk40xxsnlRmfDmmIicNXN4KhE4xPNw6JkAdZdvRM+Tuf9EyS3h67RbpXRFHGc8+CfQGxHBJ4rxSmvwwBYc8P+GdoFwtHxOGfbtgBz3x+BdaoCNrcJ8BgA3gmAoprH3J21DW7mLmLOuMFvL7yeJ7evvh1vq428fU/jlLmlkwtLnS96BOWkWCwDaRQixocp001zbcSBZLf1daOD2M6+VHXLye7SBr47hVKGpQEsuWG+J3wEJgDJhOySOYDV3q5gfdsp4OtRgH8FuOoQgKuTtGuxExqZeN2csAuhvPOUKIHOcw1HfI/xovWttvTyykbSUVjsvNRmtbomq8b16PQy2uqfaOeVVdLWs7cRHgLAn1uPqIPsA3oHviuFUuphACzZ1QAAqYOkbdvMCYShDeRnCpKqwI0NAAz8OVFMx50/frK4Ujf0LPPTBA/77pqXpiuxCSy21Sh3oUetRt5VRmjOjISqETg7iXSrCtoKfo59YVW9H/f0uOAVb0GVzGo5+DbtaGsgX1m3h0+t07bbvAO+K4XG9dIAcMOeCrQS0gLWSqK0xQAmhw5YuR+odyuojQBDOwBkcUv4aPYa7vbs2rXzadSTjL+0e3XWq9Ecr++NpyH91rs6tAIfbFXAeqpJoOW7huzyONrcBPiOPGjaEm1+SpYjz615FfG6f1RZTKTF8AB+K8UlC8MAWHLD/A0+h00dGIpW2zkBNM/WMNWbDDxtK0i3Ags7AJr9J7eLWT0wDGb5ne3VWlA6pSURpDAaZ3haZNUUjR1loZGU4vYmDIWw/IlYeWIlfgq1gPzIk0F1biQOoI/nzhflfq2Bxr/laZ8BfhuFUqnLAsAN+xeDLFjQSeak7ZgN4G0/AcakgOMvAD4X4JgK0HWM9a24A3lpJRNrgXp4PHl1XQMhveZMPdVLDuM0P7ORczXzGUICJupAzrH1btEEbyLlM4Zus0aK4w6ItQEVr7r1ap1kXsLaPFxiOpVloAHUiw4zfvuEVNZmAKy5wamGn4DwdDy2bdtMAOd/9LA+FxfgTAVqkwFsBRBIRWuZ5SyNmBg3cBX3L7V+zP3GxRj/Dl2A5qnNVq8ANSlLe4AuuDobrYCSJmFpsmSiO5DhTESrwztVyrVyb0LtEy54U/dRfcPzQQ8++4SS96EBrLlBU4efhATw7BJOAtAvdyTrd6XA/G6ANltgswLAjn2Wj749/XMj6827fjXf20tWntJkaQhQLV0Ik1S48Hvd1XW1qBc2X6JMZucwDeoCC6IUa+fm4uwMwP2a9F88NX1WPrre9WEV/trEKe9DAVhyg6aAbgUOJJht284BHHwjBbmvJ2H7JeD3EejXK0Arpf4UGXFkeb0opojDx7vONG2LgNyR6nAdcBZmtkeFREVNfNtqzE0KB9zEeTkrEklBOC+TjJmylJaVyFpn5R1vJkA2873K6+3p3qqkKa9LA1hzw3wWaFUIWCQSNmNyAA/ioaTy+0oIEcDWAlSSAqpDz7Y3W/xptxqUJeWrz5i6TCcs44WxooSasBXP4S/R7htV6+P3zNlkw1erZXhW6YjI1CGInFM7o1vt1eST6HXD/ObQxHvPbQLeqoRSicNAwZIb9jvwBcODpM2d5ACUZh2m7rKEq7sBPhUwpypgsfS09LxoxSXFINqIf2zDlvrIiLn1obqQR/C+YrKMKQOr3aUjPgHpVaqkdkLrMY+KrrRqG94O6EP97eKo2LM1PK/co6dSSwjm+P0uH16KxE3GZQDghvk7aAcmHeBFq52wHZAedQ9skgbsZqrAnwjkVJDCfamtz31rPJMsQ1N+xVGKWeH0WX5ss1fD4GS4wu7Fxax7yip8WStGTViHDFjyUUJIyGgsiPSZSuzdFcQzUaTaszJoq0UxDmVRrbZSLws+WoRShqUBrLnB4YWfgPSgaGW2YwJM19MC/fOYABtV4EMGtmwBACD+IuOKtYjaKUDlaDVlzcysYXxWPnt9uq71229DyWXGDcwZCC2LLCGrkjOpKkxTkIL1tXyIMl40Rd6vYYdbf690576MezoJXvmjgxa3BrDmhnd4oJ8AUGVOTALyYq4FmwMCuL4L4F2BG1uApu+M2+94Yk2YX9yMWr7Czr2xxmrS0XRaP1FdKNKiw+rnTcvJds9E3jfWzFfqU0s9p5anO7+mZM3Xdq4qX95gamhfXAa+98Ilq6ekwNL4YievPbAZYwkJXPuLPjXGcz6FqdMvIqAiAvzx6RAAgHEZZTy1XoAJuJy1nwCkPLy8aJyJP4MXAjDOcPWuLi5BmI2fvrz4YmYztwMAeHnRwPdHAUw00anqfp4qvtcqAA==', 'reo_clochette.ogg': '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'}
ICON_BG = r'''<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp" android:height="108dp"
    android:viewportWidth="108" android:viewportHeight="108">
    <path android:fillColor="#0E7C86" android:pathData="M0,0h108v108h-108z"/>
    <path android:fillColor="#0B3C5D" android:pathData="M0,84 C18,79 36,89 54,84 C72,79 90,89 108,84 V108 H0 Z"/>
</vector>
'''
ICON_FG = r'''<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp" android:height="108dp"
    android:viewportWidth="108" android:viewportHeight="108">
    <!-- Bulle de message -->
    <path android:fillColor="#FFF7EFE2"
        android:pathData="M40,32 H68 A10,10 0 0 1 78,42 V60 A10,10 0 0 1 68,70 H50 L37,80 L40,70 A10,10 0 0 1 30,60 V42 A10,10 0 0 1 40,32 Z"/>
    <!-- Soleil -->
    <path android:fillColor="#E8B33A" android:pathData="M58,44 a5,5 0 1,0 10,0 a5,5 0 1,0 -10,0 Z"/>
    <!-- Montagnes -->
    <path android:fillColor="#0B3C5D" android:pathData="M33,62 L43,47 L48,53 L54,44 L67,62 Z"/>
    <!-- Lagon -->
    <path android:fillColor="#0E7C86" android:pathData="M31,59 C35,56.5 39,61.5 44,59 C49,56.5 53,61.5 58,59 C63,56.5 67,61.5 77,59 V64 H31 Z"/>
</vector>
'''
ICON_MONO = r'''<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp" android:height="108dp"
    android:viewportWidth="108" android:viewportHeight="108">
    <path android:fillColor="#FFFFFFFF" android:fillType="evenOdd"
        android:pathData="M40,32 H68 A10,10 0 0 1 78,42 V60 A10,10 0 0 1 68,70 H50 L37,80 L40,70 A10,10 0 0 1 30,60 V42 A10,10 0 0 1 40,32 Z M33,62 L43,47 L48,53 L54,44 L67,62 Z"/>
</vector>
'''

# ---------- 1. Application 100 % en français ----------
def esc(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;")
    t = re.sub(r"(?<!\\)'", r"\\'", t)
    t = re.sub(r'(?<!\\)"', r'\\"', t)
    return t

STR_RE = re.compile(r'(<string name="([^"]+)"[^>]*>)(.*?)(</string>)', re.S)
PLU_RE = re.compile(r'<plurals name="([^"]+)">.*?</plurals>', re.S)

base = RES / "values/strings.xml"
fr_file = RES / "values-fr/strings.xml"
if base.exists() and fr_file.exists():
    fr_text = fr_file.read_text()
    fr = {m.group(2): m.group(3) for m in STR_RE.finditer(fr_text)}
    fr_plurals = {m.group(1): m.group(0) for m in PLU_RE.finditer(fr_text)}
    for line in FR_EXTRA.strip().splitlines():
        if "\t" in line:
            k, v = line.split("\t", 1)
            fr[k] = esc(v)
    # Textes des écrans de démarrage, réécrits en français simple et chaleureux
    for line in FR_FRIENDLY.strip().splitlines():
        if "\t" in line:
            k, v = line.split("\t", 1)
            fr[k] = esc(v)

    missing = []
    def repl_str(m):
        k = m.group(2)
        if k in fr:
            return m.group(1) + fr[k] + m.group(4)
        missing.append(k)
        return m.group(0)
    s = STR_RE.sub(repl_str, base.read_text())
    s = PLU_RE.sub(lambda m: fr_plurals.get(m.group(1), m.group(0)), s)
    # Le nom de l'application partout
    s = re.sub(r"(?i)bitchatters", "utilisateurs de Reo Fenua", s)
    s = s.replace("\\nbitchat", "\\nReo Fenua")
    s = re.sub(r"(?<![\w./@:-])(?:bitchat|BitChat|Bitchat)(?![\w:/]|\.\w)", "Reo Fenua", s)
    s = re.sub(r'<string name="app_name">[^<]*</string>', '<string name="app_name">Reo Fenua</string>', s)
    s = re.sub(r'<string name="about_tagline">[^<]*</string>',
               '<string name="about_tagline">La voix du fenua, même sans réseau</string>', s)
    base.write_text(s)
    if missing:
        warn(f"{len(missing)} textes restent en anglais : {', '.join(missing[:15])}")

    # Retirer les autres langues : l'application est en français sur tous les téléphones
    removed = 0
    for f in RES.glob("values-*/strings.xml"):
        q = f.parent.name[len("values-"):]
        if q in ("night",) or q.startswith("v") and q[1:].isdigit():
            continue
        f.unlink()
        removed += 1
    print(f"Application en français ({removed} autres langues retirées).")
else:
    warn("Fichiers de textes introuvables : traduction ignorée.")

# ---------- 1b. Textes anglais écrits directement dans le code (écrans de démarrage) ----------
JAVA = pathlib.Path("app/src/main/java/com/bitchat/android")
code_files = list((JAVA / "onboarding").glob("*.kt")) + [JAVA / "MainActivity.kt", JAVA / "ui" / "PrivateChatManager.kt"]
pairs = [l.split("\t", 1) for l in CODE_FR.strip().splitlines() if "\t" in l]
done = 0
for f in code_files:
    if not f.exists():
        continue
    t = f.read_text()
    n = t
    for en, frt in pairs:
        n = n.replace('"' + en + '"', '"' + frt + '"')
    if n != t:
        f.write_text(n)
        done += 1
print(f"Textes du code traduits dans {done} fichiers.")

# ---------- 2. Police plus lisible (au lieu de la police « machine à écrire ») ----------
tokens = UI / "theme/ChatVisualTokens.kt"
if tokens.exists():
    t = tokens.read_text()
    n = re.sub(r"internal val BitchatFontFamily = FontFamily\((?:.|\n)*?\n\)",
               "internal val BitchatFontFamily: FontFamily = FontFamily.Default", t, count=1)
    if n != t:
        tokens.write_text(n)
        print("Police lisible appliquée.")
    else:
        warn("Police non modifiée.")

# ---------- 3. Introduction au premier lancement + rubrique Aide ----------
(UI / "ReoFenuaGuide.kt").write_text(GUIDE_KT)
(UI / "ReoFenuaMailbox.kt").write_text(MAILBOX_KT)
(UI / "ReoFenuaSound.kt").write_text(SOUND_KT)
(UI / "ReoFenuaEasy.kt").write_text(EASY_KT)
(UI / "ReoFenuaNetwork.kt").write_text(NETWORK_KT)
(UI / "ReoFenuaNav.kt").write_text(NAV_KT)
(UI / "ReoFenuaEmoji.kt").write_text(EMOJI_KT)
(UI / "ReoFenuaSafety.kt").write_text(SAFETY_KT)
(UI / "ReoFenuaUrgence.kt").write_text(URGENCE_KT)
(UI / "ReoFenuaVault.kt").write_text(VAULT_KT)
(UI / "ReoFenuaStyle.kt").write_text(STYLE_KT)
import base64 as _b64
raw = RES / "raw"
raw.mkdir(parents=True, exist_ok=True)
for _name, _data in SOUNDS_B64.items():
    (raw / _name).write_bytes(_b64.b64decode(_data))
print("Sons polynésiens ajoutés.")

chat = UI / "ChatScreen.kt"
anchor = "    // About sheet\n"
c = chat.read_text() if chat.exists() else ""
if c.count(anchor) == 1:
    c = c.replace(anchor, "    // Reo Fenua : introduction et boîte aux lettres\n    ReoFenuaIntroGate()\n    ReoFenuaMailboxHost(viewModel)\n    ReoFenuaSoundWatcher(viewModel)\n    ReoFenuaEasyHost(viewModel)\n    ReoFenuaNetworkHost(viewModel)\n    ReoFenuaNavHost(viewModel)\n\n" + anchor)
    print("Introduction ajoutée.")
else:
    warn("Emplacement de l'introduction introuvable.")

# Fond d'écran (derrière) et boutons « ? » + mise à jour (devant) sur l'écran principal
anchor3 = "        val statusBarHeight = WindowInsets.statusBars.asPaddingValues().calculateTopPadding()\n"
if c.count(anchor3) == 1:
    c = c.replace(anchor3, anchor3 +
        "        ReoFenuaWallpaperLayer()\n"
        "        ReoFenuaHelpButton(viewModel = viewModel, topPadding = statusBarHeight + headerHeight + 10.dp)\n")
    print("Fond d'écran et boutons d'aide ajoutés.")
else:
    warn("Emplacement du fond d'écran introuvable.")
# Barre du bas (Radar · Proches · ALERTE · Aide · Plus), sous la case d'écriture
anchor_bar = "          }\n        }\n\n        // Floating header"
if c.count(anchor_bar) == 1:
    c = c.replace(anchor_bar, "          }\n          ReoFenuaBottomBar(viewModel)\n        }\n\n        // Floating header")
    print("Barre du bas ajoutée.")
else:
    warn("Emplacement de la barre du bas introuvable.")
if c:
    chat.write_text(c)

about = UI / "AboutSheet.kt"
anchor2 = '                    item(key = "tabs") {'
a = about.read_text() if about.exists() else ""
if a.count(anchor2) == 1:
    about.write_text(a.replace(anchor2,
        '                    item(key = "reo_help") {\n'
        '                        ReoFenuaHelpCard()\n'
        '                    }\n\n'
        '                    item(key = "reo_wallpaper") {\n'
        '                        ReoFenuaWallpaperCard()\n'
        '                    }\n\n'
        '                    item(key = "reo_sound") {\n'
        '                        ReoFenuaSoundCard()\n'
        '                    }\n\n'
        '                    item(key = "reo_easy") {\n'
        '                        ReoFenuaEasyCard()\n'
        '                    }\n\n' + anchor2))
    print("Rubrique Aide ajoutée.")
    # Mode simple : carte de mode en premier, fonctions avancées cachées
    a = about.read_text()
    a = a.replace('                    item(key = "reo_update") {',
                  '                    item(key = "reo_mode") {\n'
                  '                        ReoFenuaModeCard()\n'
                  '                    }\n\n'
                  '                    if (!ReoFenuaMode.simple.value) item(key = "reo_update") {', 1)
    for _k in ("reo_wallpaper", "reo_easy"):
        a = a.replace('                    item(key = "' + _k + '") {',
                      '                    if (!ReoFenuaMode.simple.value) item(key = "' + _k + '") {', 1)
    a = a.replace('                    item(key = "tabs") {',
                  '                    if (!ReoFenuaMode.simple.value) item(key = "tabs") {', 1)
    a = a.replace('                    if (selectedTab == AboutTab.Settings) {',
                  '                    if (selectedTab == AboutTab.Settings && !ReoFenuaMode.simple.value) {', 1)
    about.write_text(a)
    print("Mode simple branché dans l'écran d'information.")
else:
    warn("Emplacement de l'aide introuvable.")

# ---------- 3b. Bouton trombone pour envoyer documents et vidéos ----------
inp = UI / "InputComponents.kt"
old_btn = """                                ImagePickerButton(
                                    onImageReady = { outPath ->
                                        onSendImageNote(
                                            latestSelectedPeer.value,
                                            latestChannel.value,
                                            outPath
                                        )
                                    }
                                )
"""
new_btn = """                                // Pas d'images ni de fichiers dans « Autour de moi » et le Radar (public)
                                if (latestSelectedPeer.value != null || latestChannel.value != null) Row(verticalAlignment = Alignment.CenterVertically) {
                                    ReoFenuaFileButton(
                                        onFileReady = { path ->
                                            onSendFileNote(
                                                latestSelectedPeer.value,
                                                latestChannel.value,
                                                path
                                            )
                                        }
                                    )
                                    Spacer(Modifier.width(8.dp))
                                    ImagePickerButton(
                                        onImageReady = { outPath ->
                                            onSendImageNote(
                                                latestSelectedPeer.value,
                                                latestChannel.value,
                                                outPath
                                            )
                                        }
                                    )
                                }
"""
t = inp.read_text() if inp.exists() else ""
if t.count(old_btn) == 1:
    inp.write_text(t.replace(old_btn, new_btn))
    print("Bouton d'envoi de fichiers ajouté.")
else:
    warn("Emplacement du bouton fichier introuvable : bouton non ajouté.")

# Case d'écriture : dire qui pourra lire le message
t = inp.read_text() if inp.exists() else ""
old_ph = "stringResource(R.string.type_a_message_placeholder)"
if t.count(old_ph) == 1:
    inp.write_text(t.replace(old_ph, "reoFenuaPlaceholder(selectedPrivatePeer, currentChannel)"))
    print("Case d'écriture : qui peut lire.")
else:
    warn("Texte de la case d'écriture : emplacement introuvable.")

# Boutons du haut : 48 dp minimum (recommandation Android)
hdr = UI / "ChatHeader.kt"
t = hdr.read_text() if hdr.exists() else ""
if "private val HeaderTapTarget = 44.dp" in t:
    hdr.write_text(t.replace("private val HeaderTapTarget = 44.dp", "private val HeaderTapTarget = 48.dp"))
    print("Boutons du haut agrandis.")
else:
    warn("Taille des boutons du haut : emplacement introuvable.")

msm = UI / "MediaSendingManager.kt"
if msm.exists():
    t = msm.read_text()
    n = t.replace('"cannot send ${file.name}: file is too large (${sizeMb} MB, max $maxMb MB)"',
                  '"impossible d\'envoyer ${file.name} : fichier trop lourd (${sizeMb} Mo, maximum $maxMb Mo)"')
    if n != t:
        msm.write_text(n)

# ---------- 3c. Menu « Choisir une discussion » plus simple ----------
lcs = UI / "LocationChannelsSheet.kt"
t = lcs.read_text() if lcs.exists() else ""
anchor_lc = '                    item(key = "mesh_card") {'
if t.count(anchor_lc) == 1:
    t = t.replace(anchor_lc,
        '                    item(key = "reo_channels_help") {\n'
        '                        ReoFenuaChannelsExplainer()\n'
        '                    }\n\n' + anchor_lc)
    t = t.replace("stringResource(R.string.teleport).uppercase()", "stringResource(R.string.teleport)")
    # Confidentialité : on retire le niveau « Ma rue » (environ 150 m), trop précis
    old_lv = "availableChannels.filter { it.level != GeohashChannelLevel.BUILDING }"
    if t.count(old_lv) == 1:
        t = t.replace(old_lv, "availableChannels.filter { it.level != GeohashChannelLevel.BUILDING && it.level != GeohashChannelLevel.BLOCK }")
        print("Niveau « Ma rue » retiré.")
    else:
        warn("Filtre des niveaux de lieu introuvable.")
    lcs.write_text(t)
    print("Explication ajoutée au menu des discussions.")
else:
    warn("Emplacement de l'explication des discussions introuvable.")

# Boutons arrondis, sans majuscules forcées
sec = UI / "AboutSections.kt"
t = sec.read_text() if sec.exists() else ""
i = t.find("fun SheetDestructiveButton")
if i >= 0:
    j = t.find("\n}\n", i)
    body = t[i:j]
    nb = body.replace("text = text.uppercase(),", "text = text,") \
             .replace("shape = RoundedCornerShape(10.dp)", "shape = RoundedCornerShape(28.dp)") \
             .replace("letterSpacing = 0.8.sp", "letterSpacing = 0.sp")
    sec.write_text(t[:i] + nb + t[j:])
    print("Boutons arrondis.")

# ---------- 3d. Mise à jour téléchargée et installée par l'application ----------
(UI / "ReoFenuaUpdate.kt").write_text(
    UPDATE_KT.replace("__REPO__", os.environ.get("REPO", "")).replace("__TAG__", os.environ.get("TAG", ""))
)
man = pathlib.Path("app/src/main/AndroidManifest.xml")
m = man.read_text()
if "REQUEST_INSTALL_PACKAGES" not in m:
    m = m.replace('    <uses-permission android:name="android.permission.INTERNET" />',
                  '    <uses-permission android:name="android.permission.INTERNET" />\n'
                  '    <uses-permission android:name="android.permission.REQUEST_INSTALL_PACKAGES" />', 1)
    man.write_text(m)
print("Mise à jour intégrée à l'application.")

# ---------- 3e. Statut en mots sous les messages + texte plus grand ----------
mcf = UI / "MessageComponents.kt"
t = mcf.read_text() if mcf.exists() else ""
old_status = """    Text(
        text = text,
        fontSize = 10.sp,
        fontWeight = FontWeight.Normal,
        modifier = Modifier.graphicsLayer {
            scaleX = scale.value
            scaleY = scale.value
        }
    )
}"""
new_status = """    androidx.compose.foundation.layout.Row(verticalAlignment = Alignment.CenterVertically) {
        Text(
            text = text,
            fontSize = 10.sp,
            fontWeight = FontWeight.Normal,
            modifier = Modifier.graphicsLayer {
                scaleX = scale.value
                scaleY = scale.value
            }
        )
        Text(
            text = reoFenuaStatusWord(status),
            fontSize = 11.sp,
            color = colorScheme.onSurfaceVariant,
            modifier = Modifier.padding(start = 3.dp)
        )
    }
}"""
if t.count(old_status) == 1:
    t = t.replace(old_status, new_status)
    mcf.write_text(t)
    print("Statut de livraison en mots.")
else:
    warn("Statut de livraison : emplacement introuvable.")

thf = UI / "theme/Theme.kt"
t = thf.read_text() if thf.exists() else ""
old_cp = "    CompositionLocalProvider(LocalBitchatPalette provides palette) {"
new_cp = """    val reoContext = androidx.compose.ui.platform.LocalContext.current
    com.bitchat.android.ui.ReoFenuaTextSize.load(reoContext)
    val reoDensity = androidx.compose.ui.platform.LocalDensity.current
    val reoScale = com.bitchat.android.ui.ReoFenuaTextSize.scale.value
    CompositionLocalProvider(
        LocalBitchatPalette provides palette,
        androidx.compose.ui.platform.LocalDensity provides androidx.compose.ui.unit.Density(
            reoDensity.density,
            reoDensity.fontScale * reoScale
        )
    ) {"""
if t.count(old_cp) == 1:
    thf.write_text(t.replace(old_cp, new_cp))
    print("Option « grand texte » branchée.")
else:
    warn("Taille du texte : emplacement introuvable.")

# ---------- 4. Nouvelle icône ----------
draw = RES / "drawable"
draw.mkdir(parents=True, exist_ok=True)
(draw / "ic_launcher_background.xml").write_text(ICON_BG)
(draw / "ic_launcher_foreground.xml").write_text(ICON_FG)
(draw / "ic_launcher_monochrome.xml").write_text(ICON_MONO)
print("Nouvelle icône Reo Fenua.")

# ---------- 5. Écran de démarrage couleur lagon ----------
for th in [RES / "values/themes.xml", RES / "values-night/themes.xml"]:
    if not th.exists():
        continue
    t = th.read_text()
    if "windowSplashScreenBackground" in t:
        continue
    if 'xmlns:tools=' not in t:
        t = t.replace("<resources>", '<resources xmlns:tools="http://schemas.android.com/tools">', 1)
    t = re.sub(r'(<style name="Theme\.BitchatAndroid"[^>]*>)',
               r'\1\n        <item name="android:windowSplashScreenBackground" tools:targetApi="31">#0E7C86</item>',
               t, count=1)
    th.write_text(t)
print("Écran de démarrage couleur lagon.")

# ---------- 6. Emoji Reo Fenua ----------
import base64 as _b64
_nodpi = RES / "drawable-nodpi"
_nodpi.mkdir(parents=True, exist_ok=True)
for _name, _data in EMOJI_PNG.items():
    (_nodpi / (_name + ".png")).write_bytes(_b64.b64decode(_data))
print(f"{len(EMOJI_PNG)} images Reo Fenua ajoutées (emoji et avatars).")

# Les messages affichent les dessins à la place des codes
act = pathlib.Path("app/src/main/java/com/bitchat/android/core/ui/component/text/AnnotatedClickableText.kt")
t = act.read_text() if act.exists() else ""
old_a = """    var layoutResult by remember { mutableStateOf<TextLayoutResult?>(null) }
"""
new_a = """    val text = remember(text) { com.bitchat.android.ui.ReoFenuaEmoji.decorate(text) }
    var layoutResult by remember { mutableStateOf<TextLayoutResult?>(null) }
"""
old_b = """    Text(
        text = text,
        modifier = modifier.pointerInput("""
new_b = """    Text(
        text = text,
        inlineContent = com.bitchat.android.ui.ReoFenuaEmoji.inlineContent,
        modifier = modifier.pointerInput("""
if t.count(old_a) == 1 and t.count(old_b) == 1:
    act.write_text(t.replace(old_a, new_a).replace(old_b, new_b))
    print("Emoji affichés dans les messages.")
else:
    warn("Affichage des emoji : emplacement introuvable.")

# Bouton tiare dans la case d'écriture
t = inp.read_text() if inp.exists() else ""
old_box = """            Box(
                modifier = Modifier
                    .weight(1f)
                    .padding(start = 18.dp, end = 4.dp, top = 15.dp, bottom = 15.dp)
            ) {"""
new_box = """            ReoFenuaEmojiButton(value = value, onValueChange = onValueChange)
            Box(
                modifier = Modifier
                    .weight(1f)
                    .padding(start = 4.dp, end = 4.dp, top = 15.dp, bottom = 15.dp)
            ) {"""
old_ov = """                BasicTextField(
                    value = value,
                    onValueChange = onValueChange,"""
new_ov = """                BasicTextField(
                    value = value,
                    onValueChange = { nv -> onValueChange(ReoFenuaEmoji.smartDelete(value, nv)) },"""
old_vt = """                                MentionVisualTransformation(
                                    mentionPeerIdentities = mentionPeerIdentities,
                                    palette = palette,
                                ),
"""
new_vt = old_vt + """                                ReoFenuaEmojiVisualTransformation(),
"""
if t.count(old_box) == 1 and t.count(old_ov) == 1 and t.count(old_vt) == 1:
    inp.write_text(t.replace(old_box, new_box).replace(old_ov, new_ov).replace(old_vt, new_vt))
    print("Bouton emoji ajouté à la case d'écriture.")
else:
    warn("Bouton emoji : emplacement introuvable.")

# ---------- 7. Une seule ligne « Localisation » dans les autorisations manquantes ----------
onb = pathlib.Path("app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt")
t = onb.read_text() if onb.exists() else ""
_m = re.search(r"deniedCritical\.keys\.forEach \{ permission ->\s*append\(\"- \$\{getPermissionDisplayName\(permission\)\}\\n\"\)\s*\}", t)
if _m:
    t = t[:_m.start()] + 'deniedCritical.keys.map { getPermissionDisplayName(it) }.distinct().forEach { name ->\n                    append("- $name\\n")\n                }' + t[_m.end():]
    onb.write_text(t)
    print("Autorisations : doublons retirés.")
else:
    warn("Autorisations : liste introuvable.")

# ---------- 8. Sécurité : images reçues floues, signaler, pas de « gifle » ----------
imf = UI / "media" / "ImageMessageItem.kt"
t = imf.read_text() if imf.exists() else ""
old_imp = "import androidx.compose.ui.draw.clip\n"
old_img = """            // Fully revealed image
            Image(
                bitmap = img,
                contentDescription = stringResource(com.bitchat.android.R.string.cd_image),
                modifier = imageModifier,
                contentScale = ContentScale.Fit
            )
"""
new_img = """            // Reo Fenua : les images reçues restent floues jusqu'au toucher
            var reoShown by androidx.compose.runtime.saveable.rememberSaveable(message.id) {
                mutableStateOf(message.sender == currentUserNickname)
            }
            Box {
                Image(
                    bitmap = img,
                    contentDescription = stringResource(com.bitchat.android.R.string.cd_image),
                    modifier = if (reoShown) imageModifier else imageModifier.blur(28.dp),
                    contentScale = ContentScale.Fit
                )
                if (!reoShown) {
                    com.bitchat.android.ui.ReoFenuaImageCover(
                        modifier = Modifier.matchParentSize().clip(imageShape),
                        onReveal = { reoShown = true }
                    )
                }
            }
"""
if t.count(old_imp) == 1 and t.count(old_img) == 1:
    t = t.replace(old_imp, old_imp + "import androidx.compose.ui.draw.blur\n").replace(old_img, new_img)
    imf.write_text(t)
    print("Images reçues floues jusqu'au toucher.")
else:
    warn("Images floues : emplacement introuvable.")

cus = UI / "ChatUserSheet.kt"
t = cus.read_text() if cus.exists() else ""
_m = re.search(r"\n[ \t]*// Slap action\n.*?(?=\n[ \t]*// Hug action)", t, re.S)
if _m and "/slap" in _m.group(0):
    t = t[:_m.start()] + t[_m.end():]
    print("Action « gifle » retirée.")
else:
    warn("Action « gifle » : introuvable.")
old_blk = """                        // Block action
                        item {"""
new_blk = """                        // Signaler (Reo Fenua)
                        item {
                            val reoCtx = androidx.compose.ui.platform.LocalContext.current
                            UserActionRow(
                                title = "Montrer ce message",
                                subtitle = "Le partager avec la personne de votre choix (rien n'est gardé)",
                                titleColor = standardRed,
                                onClick = {
                                    com.bitchat.android.ui.reoFenuaReport(reoCtx, viewModel, targetNickname, selectedMessage)
                                    onDismiss()
                                }
                            )
                        }

                        // Block action
                        item {"""
if t.count(old_blk) == 1:
    t = t.replace(old_blk, new_blk)
    print("Bouton « Montrer ce message » ajouté.")
else:
    warn("Bouton « Montrer ce message » : emplacement introuvable.")
cus.write_text(t)

# ---------- 9. Mode stylisé : thèmes Pō, Mahana, Tīfaifai ----------
thf = UI / "theme/Theme.kt"
t = thf.read_text() if thf.exists() else ""
old_d = "    val shouldUseDark = when (darkTheme) {"
old_c = "    val colorScheme = if (shouldUseDark) DarkBitchatColorScheme else LightBitchatColorScheme\n"
new_c = """    val reoStyleCtx = androidx.compose.ui.platform.LocalContext.current
    com.bitchat.android.ui.ReoFenuaStyle.load(reoStyleCtx)
    val reoTheme = com.bitchat.android.ui.ReoFenuaStyle.theme.value
    val shouldUseDark = reoTheme?.dark ?: shouldUseDarkBase
    val colorScheme = reoTheme?.scheme ?: (if (shouldUseDark) DarkBitchatColorScheme else LightBitchatColorScheme)
"""
if t.count(old_d) == 1 and t.count(old_c) == 1:
    t = t.replace(old_d, "    val shouldUseDarkBase = when (darkTheme) {").replace(old_c, new_c)
    thf.write_text(t)
    print("Thèmes du mode stylisé branchés.")
else:
    warn("Thèmes du mode stylisé : emplacement introuvable.")
