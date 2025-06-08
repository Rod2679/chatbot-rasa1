from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionEjercicioRespiracionGuiada(Action):
    def name(self) -> Text:
        return "action_ejercicio_respiracion_guiada"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mensaje = (
            "Vamos a realizar un ejercicio de respiración guiada:\n\n"
            "🫁 Inhala profundamente por la nariz durante 4 segundos.\n"
            "✋ Sostén la respiración durante 4 segundos.\n"
            "💨 Exhala lentamente por la boca durante 6 segundos.\n"
            "🔁 Repite este ciclo durante al menos 1 minuto.\n\n"
            "Este ejercicio ayuda a calmar la mente y reducir la ansiedad."
        )
        dispatcher.utter_message(text=mensaje)
        return []

class ActionApoyoEmocional(Action):
    def name(self) -> Text:
        return "action_apoyo_emocional"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mensaje = (
            "Lamento que te sientas así. Tus emociones son importantes y está bien hablar de ellas.\n"
            "Recuerda que buscar ayuda no es signo de debilidad, sino de valentía.\n"
            "Estoy aquí para escucharte. ¿Quieres compartir lo que estás sintiendo?"
        )
        dispatcher.utter_message(text=mensaje)
        return []

class ActionConsejoAutoestima(Action):
    def name(self) -> Text:
        return "action_consejo_autoestima"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        consejos = [
            "💡 No te compares con otros. Tu proceso es único.",
            "💬 Háblate a ti mismo con la misma compasión con la que hablarías a un amigo.",
            "📈 Celebra tus pequeños logros. Cada paso cuenta.",
            "🧠 Reconoce tus cualidades. Haz una lista de cosas que te gustan de ti.",
        ]
        dispatcher.utter_message(text=random.choice(consejos))
        return []

class ActionRecomendarProfesional(Action):
    def name(self) -> Text:
        return "action_recomendar_profesional"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mensaje = (
            "Si sientes que necesitas más apoyo, hablar con un profesional puede marcar la diferencia.\n"
            "📞 En México, puedes contactar a SAPTEL al 800 472 7835, disponible 24/7.\n"
            "¿Te gustaría que te recomiende técnicas para relajarte mientras tanto?"
        )
        dispatcher.utter_message(text=mensaje)
        return []
