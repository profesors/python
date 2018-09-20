# -*- coding: utf-8 -*-
import tweepy
import random
import time

auth = tweepy.OAuthHandler("lNO5GkZZ49Lup8RaIbILZ1uYT", "rO7IwmxcoTYi8kFoX2TkUSRO6UwJdmH2Ieyi2vD7xwILvCySjV")
auth.set_access_token("716734506024222720-4z3ni6aYjolRyvyO1GflVgCEe8rYnCf", "8UHpLNofDHnaw3mwjEe4uOEwpR74tTQ1ILN7CYdfAZsYW")

api = tweepy.API(auth)

predicciones = [u"Hoy tendrás un día memorable",u"Hoy descubrirás una sorpresa allí donde no la esperabas",u"Una persona cuida mucho de ti aunque no lo sepas",u"Tus deseos se harán realidad antes de lo que imaginas",u"Llegó el momento de cosechar las alegrías que sembraste en el pasado"]
predicciones.extend([u"Lo mejor ha comenzado hoy", u"Lo que más quieres está por llegar",u"Lucha por lo que quieres y tus preocupaciones terminarán",u"La energía se encuentra en ti, el dinero llegará pronto",u"Felicidades por lo que viene",u"Deja ya tu eterna búsqueda. La felicidad está a tu lado"])

arr = api.followers()
random.seed(int(time.time()))
for i in arr:
    n = random.randint(0, len(predicciones)-1)
    print "@"+i.screen_name+" "+predicciones[n]
    api.update_status("@"+i.screen_name+" "+predicciones[n])
    time.sleep(1)
