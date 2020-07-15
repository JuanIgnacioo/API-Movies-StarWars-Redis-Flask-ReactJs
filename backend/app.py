from flask import Flask, request
from flask_cors import CORS
from flask import jsonify, json
import redis


app = Flask(__name__)
CORS(app)

def connect_db():
    """Crear conexion a la base de datos."""
    conexion = redis.StrictRedis(host="db_redis_vader_fr",port=6379, db=0)
    if(conexion.ping()):
        print("conectado al servidor de redis")
    else:
        print("error")
    return conexion

db = connect_db()
db.flushdb()


#FUNCIONES------------------------------------------------------------------
#CARGAR LOS EPISODIOS
def cargarepisodios(): 
    
    db.hset("Chapter1: The Mandalorian","estado","disponible")    
    db.hset("Chapter1: The Mandalorian","descripcion","Cinco anios despues de la derrota del Imperio Galactico, un cazarrecompensas mandaloriano acepta un trabajo fuera de registro de un cliente enigmatico con conexiones imperiales, que le exige que viaje al planeta desierto Arvala-7 y encuentre a un objetivo de 50 anios. Si bien el cliente es indiferente al bienestar del objetivo, su colega, el Dr. Pershing, insiste en que el objetivo regrese con vida. El Mandaloriano recibe una barra de acero Beskar como anticipo, que la lleva a un armero para crearse una nueva pieza de armadura. Viajando a Arvala-7, un granjero de vapor llamado Kuiil lo salva de dos Blurgg. El Mandaloriano es ayudado nuevamente por Kuiil mostrandole el campamento de los criminales que habitan el planeta, la ubicacion del objetivo. Kuiil le advierte, sin embargo, que los cazadores de recompensas anteriores que intentaron viajar alli murieron. Al llegar a la ubicacion, el Mandaloriano se une a reganiadientes con el droide caza-recompensas IG-11 para despejar la instalacion y encontrar al objetivo, que es un bebe que pertenece a la misma especie que Yoda. Cuando IG-11 intenta asesinar al bebe, el Mandaloriano dispara y destruye al droide antes de tomarlo.")
    db.hset("Chapter1: The Mandalorian", "precio", "5 USD$")
    db.hset("Chapter1: The Mandalorian", "foto", "https://m.media-amazon.com/images/M/MV5BMjA3MDM0NjQwMl5BMl5BanBnXkFtZTgwOTU0MTk4NzM@._V1_UX224_CR0,0,224,126_AL_.jpg")

    db.hset("Chapter2: The Child","estado","disponible")    
    db.hset("Chapter2: The Child","descripcion","Mientras regresa a su nave a pie con el ninio a cuestas, el Mandaloriano es emboscado por un trio de guerreros trandoshanos. Desintegra a uno de ellos que intenta apresarle y matar al ninio, revelando un llavero de rastreo. Al regresar a su nave, se encuentra con un equipo de Jawas que roban partes de su nave. Despues de una breve batalla, se retiran en su sandcrawler y aturden al inconsciente Mandaloriano con explosiones de iones. Regresa a su nave y la descubre destruida y todo su armamento robado. Con la ayuda de Kuiil, negocia a reganiadientes con los Jawas para devolver las partes de su nave a cambio de recuperar un huevo. El Mandaloriano localiza una guarida, con una gran bestia con cuernos que lo tirar y golpea a la intemperie al Mandaloriano. Con sus armas fallando y su armadura daniada, la bestia se prepara para acabar con el, pero el ninio usa la Fuerza para levantar a la bestia, permitiendo que el Mandaloriano la apuniale y la mate. Regresa con el Huevo, y los Jawas lo abren y se comen el contenido. el y Kuill reparan su nave, despues de lo cual Kuiil rechaza la oferta de recompensa del Mandaloriano y tripula su nave. Despues de separarse como amigos, el Mandaloriano toma el espacio y el ninio se despierta por primera vez despues de agotarse usando la Fuerza.")
    db.hset("Chapter2: The Child", "precio", "7 USD$")    
    db.hset("Chapter2: The Child", "foto", "https://m.media-amazon.com/images/M/MV5BYTA5MWZiYzYtZmNlZi00OGYzLThmNWUtMzQ2Y2VlY2MxNDVkXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX224_CR0,0,224,126_AL_.jpg")

    db.hset("Chapter3: The Sin","estado","disponible")    
    db.hset("Chapter3: The Sin","descripcion","El mandaloriano regresa a Nevarro y entrega al ninio a su cliente, a quien le cuestiona sobre sus planes con el ninio, pero este se niega. El cliente le paga la recompensa en acero beskar, usandolo para mejorar su armadura, cortesia de la Armera que dirige su tribu. Regresa a Greef Karga para buscar su nueva recompensa. Sin embargo, antes de partir, el Mandaloriano cambia de parecer y regresa a liberar al ninio. Aunque logra eliminar al contingente imperial que lo resguarda, es confrontado por Karga y otros mercenarios, al haber roto el codigo del Sindicato de Cazarrecompensas. Afortunadamente, es salvado por la intervencion de sus companieros mandalorianos, logrando asi incapacitar a Karga y escapar con el ninio.")
    db.hset("Chapter3: The Sin", "precio", "6 USD$")
    db.hset("Chapter3: The Sin", "foto", "https://m.media-amazon.com/images/M/MV5BMGMyMjhhMzAtYmIyNy00NDliLTkxZjItNzg1OTE4ZWYwMGFiXkEyXkFqcGdeQXVyOTg3NjI1MTg@._V1_UY126_CR39,0,224,126_AL_.jpg")

    db.hset("Chapter4: Sanctuary","estado","disponible")    
    db.hset("Chapter4: Sanctuary","descripcion","El mandaloriano llega junto con el ninio al planeta Sorgon en busqueda de refugio. Mientras inspecciona el planeta, se encuentra a una interesante Shock Trooper llamada Cara Dune quien demuestra una fortaleza y habilidades de combate impresionantes. Algunos pobladores locales, una comunidad de pacificos agricultores de krill liderados por Omera, buscan contratar los servicios del mandaloriano para espantar una banda de despiadados piratas, y este acepta a cambio de alojamiento a mitad de la nada, sin saber que en esa mision se enfrentarian a un AT-ST Imperial Walker.")
    db.hset("Chapter4: Sanctuary", "precio", "12 USD$")
    db.hset("Chapter4: Sanctuary", "foto", "https://m.media-amazon.com/images/M/MV5BMGMyMjhhMzAtYmIyNy00NDliLTkxZjItNzg1OTE4ZWYwMGFiXkEyXkFqcGdeQXVyOTg3NjI1MTg@._V1_UY126_CR39,0,224,126_AL_.jpg")

    db.hset("Chapter5: The Gunslinger","estado","disponible")    
    db.hset("Chapter5: The Gunslinger","descripcion","El Mandaloriano derrota a un caza recompensas en una batalla espacial. Aterriza su nave daniada en un muelle de reparacion cercano, dirigido por Peli Motto en Mos Eisley en Tatooine. Busca trabajo en una cantina para pagar las reparaciones, conociendo al aspirante a cazarrecompensas Toro Calican, que esta rastreando a la mercenaria de elite y asesina Fennec Shand. Calican necesita atrapar a Shand para unirse al gremio, y el Mandaloriano acepta ayudar cuando Calican le ofrezca quedarse con el dinero. Capturan a Shand en el desierto, pero ella destruye una de sus bicicletas speeder, por lo que el Mandaloriano va a buscar un rocio que pasaron para el transporte. Mientras Calican observa a Shand, ella le dice que el Mandaloriano traiciono al gremio, haciendo que la recompensa sobre el y el Ninio valiera mas que la de ella. Shand ofrece ayudar a Calican a capturar a Mandalorian si el la libera, pero el le dispara. Calican monta la bicicleta speeder restante hasta el muelle de reparacion, tomando a Motto y al Ninio como rehenes. Llega el Mandaloriano, usa una bengala para desorientar a Calican y lo mata. El toma el dinero de Calican para pagarle a Motto las reparaciones, agradeciendole antes de irse de Tatooine. En el desierto, una figura misteriosa se acerca al cuerpo de Shand.")
    db.hset("Chapter5: The Gunslinger", "precio", "9 USD$")
    db.hset("Chapter5: The Gunslinger","foto","https://vignette.wikia.nocookie.net/es.starwars/images/e/e6/TheMandalorianChapter5.jpg/revision/latest/scale-to-width-down/150?cb=20191206100245")

    db.hset("Chapter6: The Prisoner","estado","disponible")    
    db.hset("Chapter6: The Prisoner","descripcion","El Mandaloriano se acerca a su antiguo companiero Ran para trabajar. Ran le da la bienvenida a su estacion espacial y le informa al Mandaloriano que lo necesita a el y a su nave para un trabajo de cinco hombres. Se le unieron el ex francotirador imperial Mayfield, el hombre fuerte devaroniano Burg, el piloto droide Q9-0 y la mujer twi lek Xi an para una mision para rescatar al hermano Qin de Xi an, un prisionero de la Nueva Republica. Despues de infiltrarse en el barco de la prision, luchan a traves de droides de seguridad y llegan a la sala de control donde un soldado de la Nueva Republica dispara un faro de seguridad antes de ser asesinado por Xi an. La tripulacion rescata a Qin pero traiciona al Mandaloriano. El escapa y derrota a cada miembro de la tripulacion, luego captura a Qin. Q9-0 encuentra a The Child despues de descifrar la transmision archivada de Greef Karga, pero el Mandaloriano le dispara antes de que pueda daniarlo. El Mandaloriano entrega Qin a Ran y sale con su pago. Ran inmediatamente se mueve para lanzar un luchador para matar al Mandaloriano, pero descubre que la baliza de la Nueva Republica habia sido colocada en Qin, llevando un trio de alas X a la estacion de Ran donde atacan. En la escena final, se revela que Mayfield, Burg y Xi an estan encerrados en una celda en el transporte de la prision, despues de que el Mandaloriano los haya salvado.")
    db.hset("Chapter6: The Prisoner", "precio", "15 USD$")
    db.hset("Chapter6: The Prisoner", "foto", "https://m.media-amazon.com/images/M/MV5BZGYzOGEyNTgtMmEyZS00Yjk0LWIwYzUtMTNhZGMzODIzM2Q1XkEyXkFqcGdeQXVyNDM5MDAzNTA@._V1_UY126_CR38,0,224,126_AL_.jpg")

    db.hset("Chapter7: The Reckoning","estado","disponible")    
    db.hset("Chapter7: The Reckoning","descripcion","El mandaloriano recibe un mensaje de Greef Karga. La ciudad de Karga ha sido invadida por tropas imperiales dirigidas por el Cliente, que esta desesperado por recuperar al Ninio. Karga propone que el Mandaloriano use al Ninio como cebo para matar al Cliente y liberar la ciudad. A cambio, Karga enfrentara las cosas con el Gremio, lo que permitiria al Mandaloriano y al Ninio vivir en paz. Sintiendo una trampa, el Mandaloriano recluta a Cara Dune y Kuiil el Ugnaught para que lo ayuden. Kuill tambien ha reconstruido y reprogramado IG-11, y el grupo viaja a Nevarro. A su llegada se encuentran con Karga y sus asociados, pero en el camino hacia la ciudad son atacados por Mynocks. Karga esta herido pero el Ninio usa la fuerza para curar su herida. A cambio, Karga dispara a sus asociados y explica su plan original para matar al Mandaloriano y llevar al Ninio al Cliente. El grupo formula un nuevo plan: Karga fingira que Dune capturo al Mandaloriano, y los tres entraran a la ciudad para encontrarse con el Cliente. Mientras tanto, Kuiil devolvera al Ninio a la nave. Durante la reunion, el Cliente recibe una llamada de Moff Gideon, cuyas tropas rodean el edificio y abren fuego, matando al Cliente. Gideon llega y se jacta de que el Ninio pronto estara en su poder. En el desierto a las afueras de la ciudad, los soldados exploradores rastrean y matan a Kuiil y secuestran al Ninio.")
    db.hset("Chapter7: The Reckoning", "precio", "2 USD$")
    db.hset("Chapter7: The Reckoning", "foto", "https://m.media-amazon.com/images/M/MV5BMTBiMmYzMjItM2Y1My00MjVjLTk0MWMtYjBhNmFhZWNkYTBmXkEyXkFqcGdeQXVyODkzNTgxMDg@._V1_UY126_CR37,0,224,126_AL_.jpg")

    db.hset("Chapter8: Redemption","estado","disponible")    
    db.hset("Chapter8: Redemption","descripcion","IG-11 rescata al Ninio de los soldados exploradores. Gideon advierte a Karga, Dune, y el Mandaloriano (a quien se refiere por su verdadero nombre, Din Djarin) que a menos que acepten cooperar con el, seguramente moriran. IG-11 llega e interrumpe la situacion, pero Gideon hiere gravemente a Djarin. Un stormtrroper llega con un lanzallamas a atacar la cantina donde se refugian, pero el Ninio usa la Fuerza para disuadir las llamas. Djarin envia al resto a huir a traves de un desague con el Ninio para buscar ayuda del enclave mandaloriano. Mientras tanto, IG-11 le quita su casco para aplicar bacta a su herida y curarla. Reuniendose con los demas, encuentran que los Mandalorianos han muerto o escapado del planeta, a excepcion de la Armera. Ella le asigna a Djarin la tarea de cuidar del Ninio como si fuese suyo, descubrir su origen y enviarlo de vuelta a donde pertenece. La Armera fabrica un sello propio para Djarin, y le obsequia un jetpack. Mientras la Armera permanece atras para enfrentarse a los Stormtroopers, el resto del grupo trata de huir navegando por un rio subterraneo de lava. Cuando son emboscados por los soldados imperiales, IG-11 se autodestruye para eliminarlos. Moff Gideon los ataca a bordo de su caza TIE, pero el Mandaloriano, con ayuda de su jetpack, logra incapacitar su nave y vencerlo. Djarin hace las paces con Greef Karga, y se marcha junto al Ninio, mientras que Karga y Dune permanecen en Nevarro. Mientras tanto, Gideon logra salir de los restos de su nave usando el Sable Oscuro.")
    db.hset("Chapter8: Redemption", "precio", "10 USD$")
    db.hset("Chapter8: Redemption", "foto", "https://m.media-amazon.com/images/M/MV5BMGU0MDVlOWQtYjc1ZC00OWQ4LWI2ZWYtOWUyNmYyNzRmOWU5XkEyXkFqcGdeQXVyNjczOTE0MzM@._V1_UX224_CR0,0,224,126_AL_.jpg")
    return 'Ok'

cargarepisodios()

#LISTAR LOS EPIOSIDIOS
def listarEpisodios():
    
    liste = ["Chapter1: The Mandalorian","Chapter2: The Child","Chapter3: The Sin","Chapter4: Sanctuary","Chapter5: The Gunslinger","Chapter6: The Prisoner","Chapter7: The Reckoning","Chapter8: Redemption"]
    for k in liste:
        #print(k)
        #if(db.type(k) == 'hash'):
        if (db.pttl('reservado'+ k) == -2) and (db.pttl('alquilado'+ k) == -2) : 
            
            #if(db.hget(k,"estado") != "disponible"):
            db.hset(k,"estado","disponible")
            print(db.type(k))
        
    
    chapters = [        
        
            {
            "nombre": "Chapter1: The Mandalorian",
            "estado": db.hget("Chapter1: The Mandalorian","estado").decode("utf-8"),
            "descripcion": db.hget("Chapter1: The Mandalorian","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter1: The Mandalorian","precio").decode("utf-8"),
            "foto": db.hget("Chapter1: The Mandalorian","foto").decode("utf-8")
            },       
        
            {
            "nombre": "Chapter2: The Child",
            "estado": db.hget("Chapter2: The Child", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter2: The Child","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter2: The Child","precio").decode("utf-8"),
            "foto": db.hget("Chapter2: The Child","foto").decode("utf-8")
            },       
        
            {
            "nombre": "Chapter3: The Sin",
            "estado": db.hget("Chapter3: The Sin", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter3: The Sin","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter3: The Sin","precio").decode("utf-8"),
            "foto": db.hget("Chapter3: The Sin","foto").decode("utf-8")
            },        
        
            {
            "nombre": "Chapter4: Sanctuary",
            "estado": db.hget("Chapter4: Sanctuary", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter4: Sanctuary","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter4: Sanctuary","precio").decode("utf-8"),
            "foto": db.hget("Chapter4: Sanctuary","foto").decode("utf-8")
            },       
        
            {
            "nombre": "Chapter5: The Gunslinger",
            "estado": db.hget("Chapter5: The Gunslinger", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter5: The Gunslinger","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter5: The Gunslinger","precio").decode("utf-8"),
            "foto": db.hget("Chapter5: The Gunslinger","foto").decode("utf-8")
            },       
        
            {
            "nombre": "Chapter6: The Prisoner",
            "estado": db.hget("Chapter6: The Prisoner", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter6: The Prisoner","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter6: The Prisoner","precio").decode("utf-8"),
            "foto": db.hget("Chapter6: The Prisoner","foto").decode("utf-8")
            },        
        
            {
            "nombre": "Chapter7: The Reckoning",
            "estado": db.hget("Chapter7: The Reckoning", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter7: The Reckoning","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter7: The Reckoning","precio").decode("utf-8"),
            "foto": db.hget("Chapter7: The Reckoning","foto").decode("utf-8")
            },        
        
            {
            "nombre": "Chapter8: Redemption",
            "estado": db.hget("Chapter8: Redemption", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter8: Redemption","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter8: Redemption","precio").decode("utf-8"),
            "foto": db.hget("Chapter8: Redemption","foto").decode("utf-8")
            }
                 
    ]
        
    a = jsonify(chapters)
    return (a)
  

def reservar(capitulo):
    r = db.hget(capitulo,"estado").decode("utf-8")
    print(r)
    if(r == 'disponible'):  
        db.hset(capitulo,"estado","reservado")
        db.setex('reservado' + capitulo, 240, capitulo)
        return 'Si'
    if(r == 'reservado'):   
        print('ENTRO EN NO')            
        return 'No'
    if(r == 'alquilado'):
        print(r)
        return 'No'

def pagar(capitulo):
    
    if(db.pttl('reservado'+ capitulo) != -2):
        db.delete('reservado' + capitulo)
        db.hset(capitulo,"estado","alquilado")
        db.setex('alquilado'+capitulo, 1440, capitulo)
        return 'Alquilado por 24hrs'
    
    else:   
        return 'No se encuentra reservado'




@app.route('/obtenerListado', methods=['GET'])
def obtenerListado():    
    if request.method == 'GET':
        e = listarEpisodios()
        return e
    
    
@app.route('/pagarCapitulo', methods=['POST'])
def pagarCapitulo():
    if request.method == 'POST':                
        e = request.args['capitulo']
        aux = pagar(e)
        
        if(aux == 'No se encuentra reservado'):
            return 'falta reservarlo o se encuentra alquilado'
        else:
            return 'Pagado'


@app.route('/reservarCapitulo', methods=['POST'])
def reservarCapitulo():
    if request.method == 'POST':
        e = request.args['capitulo']
        aux = reservar(e)
        if (aux == 'Si'):
            return 'Reservado con exito'
        if (aux == 'No'):
            return 'Ya se encuentra reservado o alquilado'


        


if __name__ == '__main__':
    app.run(host='backend', port='5000', debug=False)

