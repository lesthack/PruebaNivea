# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from .models import *
from datetime import datetime

def inserts_escalas():
    # Escalas
    escala_fv, c = Escala.objects.get_or_create(nombre='Falso-Verdadero')
    if escala_fv:
        falso = EscalaItem.objects.get_or_create(escala=escala_fv, nombre='Falso')
        verdadero = EscalaItem.objects.get_or_create(escala=escala_fv, nombre='Verdadero')
    # Likert 1
    escala_likert1, c = Escala.objects.get_or_create(nombre='Likert1')
    if escala_likert1:
        nunca = EscalaItem.objects.get_or_create(escala=escala_likert1, nombre='Nunca')
        algunas_veces = EscalaItem.objects.get_or_create(escala=escala_likert1, nombre='Algunas Veces')
        frecuentemente = EscalaItem.objects.get_or_create(escala=escala_likert1, nombre='Frecuentemente')
        muy_frecuentemente = EscalaItem.objects.get_or_create(escala=escala_likert1, nombre='Muy Frecuentemente')
    # Likert 2
    escala_likert2, c = Escala.objects.get_or_create(nombre='Likert2')
    if escala_likert2:
        nada = EscalaItem.objects.get_or_create(escala=escala_likert2, nombre='Nada')
        poco = EscalaItem.objects.get_or_create(escala=escala_likert2, nombre='Poco')
        moderadamente = EscalaItem.objects.get_or_create(escala=escala_likert2, nombre='Moderadamente')
        bastante = EscalaItem.objects.get_or_create(escala=escala_likert2, nombre='Bastante')
        muchisimo = EscalaItem.objects.get_or_create(escala=escala_likert2, nombre='Muchisimo')

def inserts_competencias():
    Competencia.objects.get_or_create(nombre='Apego a normas', orden=1)
    Competencia.objects.get_or_create(nombre='Adaptabilidad', orden=2)
    Competencia.objects.get_or_create(nombre='Trabajo en equipo', orden=3)
    Competencia.objects.get_or_create(nombre='Honestidad', orden=4)
    Competencia.objects.get_or_create(nombre='Impulsividad', orden=5)
    Competencia.objects.get_or_create(nombre='Manejo de conflictos', orden=6)
    Competencia.objects.get_or_create(nombre='Uso de sustancias', orden=7)
    Competencia.objects.get_or_create(nombre='Violencia', orden=8)
    Competencia.objects.get_or_create(nombre='Liderazgo negativo', orden=9)
    Competencia.objects.get_or_create(nombre='Autocuidado', orden=10)

def inserts_localidades():
    Localidad.objects.get_or_create(nombre='Guanajuato')
    Localidad.objects.get_or_create(nombre='Irapuato')
    Localidad.objects.get_or_create(nombre='León')
    Localidad.objects.get_or_create(nombre='Romita')
    Localidad.objects.get_or_create(nombre='Silao')

def inserts_instrumento():
    me = User.objects.get(id=1)

    lista_preguntas = {
        'Likert1': [
            [1,'Disfruto estar con otras personas. ',[3,2,1,0]],
            [2,'Mentir es malo solo si me descubren.',[0,1,2,3]],
            [3,'Soy cuidadosa/o.',[3,2,1,0]],
            [4,'No importa mentir a alguien si con ello evito problemas.',[0,1,2,3]],
            [5,'Alguno de mis amigo/as han usado drogas.',[0,1,2,3]],
            [6,'Pierdo la paciencia a menudo.',[0,1,2,3]],
            [7,'Digo lo primero que se me viene a la cabeza.',[0,1,2,3]],
            [8,'Planeo cosas con anticipación.',[3,2,1,0]],
            [9,'A mi familia le molestan mis amigas/os.',[0,1,2,3]],
            [10,'Pienso mis decisiones a futuro. ',[3,2,1,0]],
            [11,'Durante la adolescencia me escapé alguna vez de casa y pasé la noche fuera.',[0,1,2,3]],
            [12,'Realizo actividades que le sirven a otros. ',[3,2,1,0]],
            [13,'Acostumbro a comer aun cuando no tengo hambre.',[0,1,2,3]],
            [14,'Reconozco y valoro las ideas de los demás. ',[3,2,1,0]],
            [15,'Soy impulsivo.',[0,2,3,4]],
            [16,'Me considero una persona optimista. ',[3,2,1,0]],
            [17,'He amenazado a otros con hacerles daño o lastimarlos.',[0,3,4,5]],
            [18,'Sé decir no cuando algo me molesta.',[3,2,1,0]],
            [19,'He dañado intencionalmente las cosas de otros.',[0,3,4,5]],
            [20,'Me he peleado físicamente con  amigas/os o familiares.',[0,1,2,3]],
            [21,'He molestado o le he hecho daño a los animales.',[0,2,3,4]],
            [22,'Se han aburrido mis amigas/os en las fiestas donde no hay tragos.',[0,1,2,3]],
            [23,'Las decisiones que afectan a mi vida y a mi trabajo las tomo con rapidez.',[0,1,2,3]],
            [24,'Me opongo a las normas porque quitan libertad a la gente.',[0,1,2,3]],
            [25,'Me gusta o gustaría manejar rápido.',[0,1,2,3]],
            [26,'Me siento en capacidad de expresarme cuando no estoy de acuerdo.',[0,1,2,3]],
            [27,'Me gusta cambiar de casa.',[0,1,2,3]],
            [28,'Me siento valorado por otros. ',[3,2,1,0]],
            [29,'Me interesa dedicar tiempo a cosas en las que no gano nada.',[3,2,1,0]],
            [30,'Soy buena compañía para otras personas. ',[3,2,1,0]],
            [31,'Me resulta difícil controlar las emociones.',[0,1,2,3]],
            [32,'Mis amigas/os han tenido problemas con las autoridades.',[0,1,2,3]],
            [33,'No me gusta esperar en una fila.',[0,1,2,3]],
            [34,'Termino las cosas que empiezo.',[3,2,1,0]],
            [35,'Me es fácil concentrarme.',[0,1,2,3]],
            [36,'Tengo más de tres personas con quien hablar de las cosas que son muy personales.',[3,2,1,0]],
            [37,'Me siento satisfecho conmigo  y con lo que hago.',[3,2,1,0]],
            [38,'Soy más valiente que la mayoría de mis compañeros.',[0,1,2,3]],
            [39,'Perdía los útiles escolares.',[0,1,2,3]],
            [40,'Terminaba las tareas muy rápido. ',[0,1,2,3]],
            [41,'Trataba de ser el primero en los juegos.',[0,1,2,3]],
            [42,'Primero hacia las tareas fáciles y después las difíciles.',[0,1,2,3]],
            [43,'Era muy activa/o',[0,1,2,3]],
            [44,'Me gustaba desarmar cosas.',[0,1,2,3]],
            [45,'Me aburría en el salón de clases.',[0,1,2,3]],
            [46,'Me distraía con facilidad.',[0,2,3,4]],
            [47,'Tenía dificultad para esperar los turnos.',[0,1,2,3]],
            [48,'Me costaba trabajo estar mucho tiempo en mi silla.',[0,1,2,3]],
            [49,'Me costaba dormirme.',[0,1,2,3]],
            [50,'Dejaba la tarea para el final del día.',[0,1,2,3]],
            [51,'Defendía a golpes a mis compañeros.',[0,1,2,3]],
            [52,'Era inquieta/o, me movía de un lugar a otro.',[0,1,2,3]],
            [53,'Pelaba con las/los compañeras/os.',[0,3,4,5]],
            [54,'Me costaba trabajo levantarme.',[0,1,2,3]],
            [55,'Me molestaba que me dieran órdenes.',[0,1,2,3]],
            [56,'Me metía en problemas constantemente con mis compañeros.',[0,1,2,3]],
            [57,'Empezaba las actividades antes de los otros niños/as.',[0,1,2,3]],
            [58,'Cambiaba fácilmente de una actividad a otra.',[0,1,2,3]],
            [59,'Culpaba a otras/os niñas/os de las travesuras que yo hacía.',[0,1,2,3]],
            [60,'Me costaba trabajo esperar.',[0,1,2,3]],
            [61,'Me gustaba hacer muchas cosas al mismo tiempo.',[0,1,2,3]],
        ],
        'Likert2': [
            [62,'Alguna vez fueron tan agresivas/os conmigo que grite o golpee.',[0,2,3,4,5]],
            [63,'Era difícil confiar en mis compañeras/os o jefes.',[0,1,2,3,4]],
            [64,'Eran poco comprensivos conmigo.',[0,1,2,3,4]],
            [65,'Me criticaban en mi forma de ser o trabajar.',[0,1,2,3,4]],
            [66,'Me hacían explotar por comentarios o acciones de mis compañeras/os o jefes.',[0,2,3,4,5]],
            [67,'Me hacían sentir menos o que no valía.',[0,1,2,3,4]],
            [68,'Me involucraba frecuentemente en discusiones.',[0,2,3,4,5]],
            [69,'Las/los compañeras/os hacían cosas mal y a mi me culpaban. ',[0,1,2,3,4]],
            [70,'Las/los compañeras/os o jefes eran poco amistosos/as. ',[0,1,2,3,4]],
            [71,'Me comportaba con timidez.',[0,1,2,3,4]],
            [72,'Me sentía  incómoda/o al comer con mis compañeras/os.',[0,1,2,3,4]],
            [73,'Me sentía incómoda/o cuando la gente me miraba o hablaba de mí.',[0,1,2,3,4]],
            [74,'Me sentía enojada/o.',[0,1,2,3,4]],
            [75,'Me sentía herida/o o lastimada/o por mis compañeros o jefes.',[0,1,2,3,4]],
            [76,'Me sentía muy tímida/o con los demás.',[0,1,2,3,4]],
            [77,'Si tenían oportunidad mis compañeras/os se aprovechaban de mí.',[0,1,2,3,4]],
            [78,'Mis compañeras/os hablaban a mis espaldas. ',[0,2,3,4,5]],
            [79,'Mis compañeras/os o jefes no valoraban mis logros.',[0,1,2,3,4]],
            [80,'Mis compañeras/os o jefes se oponían a mi forma de pensar.',[0,1,2,3,4]],
        ]
    }
    
    instrumento_ejemplo, c = Instrumento.objects.get_or_create(nombre='Ejemplo', created_by=me)
    for nombre_escala in lista_preguntas.keys():
        view_escala = Escala.objects.get(nombre=nombre_escala)
        lista_escala = list(view_escala.getItems())
        for pregunta in lista_preguntas[nombre_escala]:
            new_instrumento_item, c = InstrumentoItem.objects.get_or_create(
                instrumento = instrumento_ejemplo,
                pregunta = pregunta[1],
                orden = pregunta[0],
                escala = view_escala
            )
            if new_instrumento_item:
                for i in range(len(pregunta[2])):
                    InstrumentoValor.objects.get_or_create(
                        instrumento_item = new_instrumento_item,
                        escala_item = lista_escala[i],
                        valor = pregunta[2][i]
                    )

#def inserts_instrumento():
#    me = User.objects.get(id=1)
#    instrumento_ejemplo, c = Instrumento.objects.get_or_create(nombre='Ejemplo', created_by=me)
#
#    lista_preguntas = {
#        'Apego a normas': {
#            'Likert1': [
#                [11,'Durante la adolescencia me escapé alguna vez de casa y pasé la noche fuera.',[5,4,3,0]],
#                [23,'Las decisiones que afectan a mi vida y a mi trabajo las tomo con rapidez.',[4,3,2,1]],
#                [34,'Termino las cosas que empiezo.',[0,2,3,4]],
#                [39,'Perdía los útiles escolares.',[4,3,2,1]],
#                [42,'Primero hacia las tareas fáciles y después las difíciles.',[4,3,2,1]],
#                [48,'Me costaba trabajo estar mucho tiempo en mi silla.',[4,3,2,1]],
#                [50,'Dejaba la tarea para el final del día.',[4,3,2,1]],
#                [54,'Me costaba trabajo levantarme.',[4,3,2,1]],
#                [55,'Me molestaba que me dieran órdenes.',[5,4,3,0]],
#                [57,'Empezaba las actividades antes de los otros niños/as.',[4,3,2,1]]
#            ]
#        },
#        'Adaptabilidad': {
#            'Likert1': [
#                [1,'Disfruto estar con otras personas.',[0,1,2,3]],
#                [12,'Realizo actividades que le sirven a otros.',[0,2,3,4]],
#                [14,'Reconozco y valoro las ideas de los demás.',[0,2,3,4]],
#                [16,'Me considero una persona optimista.',[0,1,2,3]],
#                [18,'Sé decir no cuando algo te molesta.',[0,1,2,3]],
#                [26,'Me siento en capacidad de expresarme cuando no estoy de acuerdo.',[0,1,2,3]],
#                [28,'Me siento valorado por otros.',[0,1,2,3]],
#                [29,'Me interesa dedicar tiempo a cosas en las que no gano nada.',[0,2,3,4]],
#                [30,'Soy buena compañía para para otras personas.',[0,1,2,3]],
#            ]
#        },
#        'Trabajo en equipo': {
#            'Likert1': [
#                [12,'Realizo actividades que le sirven a otros.',[0,2,3,4]],
#                [14,'Reconozco y valoro las ideas de los demás.',[0,2,3,4]],
#                [26,'Me siento en capacidad de expresarme cuando no estoy de acuerdo.',[0,1,2,3]],
#                [28,'Me siento valorado por otros.',[0,1,2,3]],
#                [30,'Soy buena compañía para para otras personas.',[0,1,2,3]],
#                [41,'Trataba de ser el primero en los juegos.',[3,2,1,0]],
#                [47,'Tenía dificultad para esperar los turnos.',[3,2,1,0]],
#                [53,'Pelaba con las/los compañeras/os.',[3,2,1,0]],
#                [56,'Me metía en problemas constantemente con mis compañeros.',[3,2,1,0]],
#            ],
#            'Likert2': [
#                [62,'Alguna vez fueron tan agresivas/os conmigo que grite o golpee.',[4,3,2,1,0]],
#                [69,'Las/los compañeras/os hacían cosas mal y a mi me culpaban.',[4,3,2,1,0]],
#                [70,'Las/los compañeras/os o jefes eran poco amistosos.',[4,3,2,1,0]],
#                [75,'Me sentía herida/o o lastimada/o por mis compañeros o jefes.',[4,3,2,1,0]],
#                [77,'Si tenían oportunidad mis compañeras/os se aprovechaban de mi.',[4,3,2,1,0]],
#                [79,'Mis compañeras/os o jefes no valoraban mis logros.',[4,3,2,1,0]],
#            ]
#        },
#        'Honestidad': {
#            'Likert1': [
#                [26,'Me siento en capacidad de expresarme cuando no estoy de acuerdo.',[0,1,2,3]],
#                [18,'Sé decir no cuando algo te molesta.',[0,1,2,3]],
#                [2,'Mentir es malo solo si me descubren.',[4,3,2,1]],
#                [4,'No importa mentir a alguien si con ello evito problemas.',[4,3,2,1]],
#                [7,'Digo lo primero que se me viene a la cabeza.',[0,1,3,3]],
#                [59,'Culpaba a otras/os niñas/os de las travesuras que yo hacía.',[4,3,2,1]],
#            ]
#        },
#        'Impulsividad': {
#            'Likert1': [
#                [7,'Digo lo primero que se me viene a la cabeza.',[0,1,3,3]],
#                [41,'Trataba de ser el primero en los juegos.',[0,1,3,3]],
#                [47,'Tenía dificultad para esperar los turnos.',[0,1,3,3]],
#                [23,'Las decisiones que afectan a mi vida y a mi trabajo las tomo con rapidez.',[0,1,3,3]],
#                [34,'Termino las cosas que empiezo.',[3,2,1,0]],
#                [42,'Primero hacia las tareas fáciles y después las difíciles.',[0,1,3,3]],
#                [48,'Me costaba trabajo estar mucho tiempo en mi silla.',[0,1,3,3]],
#                [54,'Me costaba trabajo levantarme.',[0,1,3,3]],
#                [8,'Planeo cosas con anticipación.',[3,2,1,0]],
#                [10,'Pienso mis decisiones a futuro. ',[3,2,1,0]],
#                [13,'Acostumbro a comer aun cuando no tengo hambre.',[0,1,3,3]],
#                [15,'Soy impulsivo.',[0,1,3,3]],
#                [27,'Me gusta cambiar de casa.',[0,1,3,3]],
#                [33,'No me gusta esperar en una fila.',[0,1,3,3]],
#                [40,'Terminaba las tareas muy rápido. ',[0,1,3,3]],
#                [43,'Era muy activa/o',[0,1,3,3]],
#                [45,'Me aburría en el salón de clases.',[0,1,3,3]],
#                [49,'Me costaba dormirme.',[0,1,3,3]],
#                [52,'Era inquieta/o, me movía de un lugar a otro.',[0,1,3,3]],
#                [58,'Cambiaba fácilmente de una actividad a otra.',[0,1,3,3]],
#                [60,'Me costaba trabajo esperar.',[0,1,3,3]],
#            ]
#        },
#        'Manejo de conflictos': {
#            'Likert2': [
#                [69,'Las/los compañeras/os hacían cosas mal y a mi me culpaban.',[4,3,2,1,0]],
#                [70,'Las/los compañeras/os o jefes eran poco amistosos.',[4,3,2,1,0]],
#                [75,'Me sentía herida/o o lastimada/o por mis compañeros o jefes.',[4,3,2,1,0]],
#                [77,'Si tenían oportunidad mis compañeras/os se aprovechaban de mi.',[4,3,2,1,0]],
#                [79,'Mis compañeras/os o jefes no valoraban mis logros.',[4,3,2,1,0]],
#                [63,'Era difícil confiar en mis compañeras/os o jefes.',[4,3,2,1,0]],
#                [64,'Eran poco comprensivos conmigo.',[4,3,2,1,0]],
#                [65,'Me criticaban en mi forma de ser o trabajar.',[4,3,2,1,0]],
#                [66,'Me hacían explotar por comentarios o acciones de mis compañeras/os o jefes.',[4,3,2,1,0]],
#                [67,'Me hacían sentir menos o que no valía.',[4,3,2,1,0]],
#                [68,'Me involucraba frecuentemente en discusiones.',[4,3,2,1,0]],
#                [71,'Me comportaba con timidez.',[4,3,2,1,0]],
#                [72,'Me sentía  incómoda/o al comer con mis compañeras/os.',[4,3,2,1,0]],
#                [73,'Me sentía incómoda/o cuando la gente me miraba o hablaba de mí.',[4,3,2,1,0]],
#                [74,'Me sentía enojada/o.',[4,3,2,1,0]],
#                [76,'Me sentía muy tímida/o con los demás.',[4,3,2,1,0]],
#                [78,'Mis compañeras/os hablaban a mis espaldas. ',[4,3,2,1,0]],
#                [80,'Mis compañeras/os o jefes se oponían a mi forma de pensar.',[4,3,2,1,0]],
#            ]
#        },
#        'Uso de sustancias': {
#            'Likert1': [
#                [9,'A mi familia le molestan mis amigas/os.',[0,1,2,3]],
#                [5,'Alguno de mis amigo/as han usado drogas.',[0,1,2,3]],
#                [17,'He amenazado a otros con hacerles daño o lastimarlos.',[0,1,2,3]],
#                [19,'He dañado intencionalmente las cosas de otros.',[0,1,2,3]],
#                [21,'He molestado o le he hecho daño a los animales.',[0,1,2,3]],
#                [22,'Se han aburrido mis amigas/os en las fiestas donde no hay tragos.',[0,1,2,3]],
#                [32,'Mis amigas/os han tenido problemas con las autoridades.',[0,1,2,3]],
#            ]
#        },
#        'Violencia': {
#            'Likert1': [
#                [17,'He amenazado a otros con hacerles daño o lastimarlos.',[0,4,5,6]],
#                [19,'He dañado intencionalmente las cosas de otros.',[0,4,5,6]],
#                [21,'He molestado o le he hecho daño a los animales.',[0,3,4,5]],
#                [53,'Pelaba con las/los compañeras/os.',[0,1,2,3]],
#                [56,'Me metía en problemas constantemente con mis compañeros.',[0,1,2,0]],
#                [6,'Pierdo la paciencia a menudo.',[0,2,3,4]],
#                [20,'Me he peleado físicamente con  amigas/os o familiares.',[0,4,5,6]],
#                [51,'Defendía a golpes a mis compañeros.',[0,1,2,3]],
#            ],
#            'Likert2': [
#                [68,'Me involucraba frecuentemente en discusiones.',[0,1,2,3,4]],
#                [74,'Me sentía enojada/o.',[0,1,2,3,4]],
#                [62,'Alguna vez fueron tan agresivas/os conmigo que grite o golpee.',[0,1,2,3,4]],
#            ]
#        },
#        'Liderazgo negativo': {
#            'Likert2': [
#                [68,'Me involucraba frecuentemente en discusiones.',[0,1,2,3,4]],
#                [51,'Defendía a golpes a mis compañeros.',[0,1,2,3,]],
#                [63,'Era difícil confiar en mis compañeras/os o jefes.',[0,1,2,3,4]],
#                [65,'Me criticaban en mi forma de ser o trabajar.',[0,1,2,3,4]],
#                [66,'Me hacían explotar por comentarios o acciones de mis compañeras/os o jefes.',[0,1,2,3,4]],
#            ],
#            'Likert1': [
#                [51,'Defendía a golpes a mis compañeros.',[0,1,2,3]],
#                [32,'Mis amigas/os han tenido problemas con las autoridades.',[0,1,2,3]],
#                [59,'Culpaba a otras/os niñas/os de las travesuras que yo hacía.',[0,1,2,3]],
#                [12,'Realizo actividades que le sirven a otros. ',[4,3,2,1]],
#                [14,'Reconozco y valoro las ideas de los demás. ',[4,3,2,1]],
#                [55,'Me molestaba que me dieran órdenes.',[0,1,2,3]],
#                [24,'Me opongo a las normas porque quitan libertad a la gente.',[0,4,5,6]],
#            ]
#        },
#        'Autocuidado': {
#            'Likert1': [
#                [47,'Tenía dificultad para esperar los turnos.',[3,2,1,0]],
#                [8,'Planeo cosas con anticipación.',[0,1,2,3]],
#                [10,'Pienso mis decisiones a futuro. ',[0,1,2,3]],
#                [33,'No me gusta esperar en una fila.',[3,2,1,0]],
#                [52,'Era inquieta/o, me movía de un lugar a otro.',[3,2,1,0]],
#                [3,'Soy cuidadosa/o.',[0,1,2,3]],
#                [36,'Tengo más de tres personas con quien hablar de las cosas que son muy personales.',[0,1,2,3]],
#                [37,'Me siento satisfecho contigo  y con lo que hago.',[0,1,2,3]],
#                [35,'Me es fácil concentrarme.',[0,1,2,3]],
#                [46,'Me distraía con facilidad.',[3,2,1,0]],
#                [61,'Me gustaba hacer muchas cosas al mismo tiempo.',[3,2,3,0]],
#            ]
#        }
#    }
#    for nombre_categoria in lista_preguntas.keys():
#        view_categoria = Categoria.objects.get(nombre=nombre_categoria)
#        for nombre_escala in lista_preguntas[nombre_categoria].keys():
#            view_escala = Escala.objects.get(nombre=nombre_escala)
#            lista_escala = list(view_escala.getItems())
#            for pregunta in lista_preguntas[nombre_categoria][nombre_escala]:
#                new_instrumento_item, c = InstrumentoItem.objects.get_or_create(
#                    instrumento = instrumento_ejemplo,
#                    pregunta = pregunta[1],
#                    orden = pregunta[0],
#                    escala = view_escala
#                )
#                if new_instrumento_item:
#                    new_instrumento_item.categoria.add(view_categoria)
#                    for i in range(len(pregunta[2])):
#                        InstrumentoValor.objects.get_or_create(
#                            instrumento_item = new_instrumento_item,
#                            escala_item = lista_escala[i],
#                            valor = pregunta[2][i]
#                        )
