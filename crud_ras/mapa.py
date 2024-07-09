from flask import Flask
from flask_cors import CORS
from flask import Blueprint, jsonify,request
import pymysql
## Funcion para conectarnos a la base de datos de mysql
mapa_blueprint = Blueprint('mapa',__name__)
def conectar(vhost,vuser,vpass,vdb):
     conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb,)
     return conn 


##registrar avistamiento
@mapa_blueprint.route("/mapa",methods=['POST'])
def registro():
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        x=cur.execute(""" insert into mapa (cordenada,nombre,color,veneno) values \
            ('{0}','{1}','{2}','{3}')""".format(request.json['cordenada'],\
            request.json['nombre'],request.json['color'],request.json['veneno'],))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'informacion del mapa'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})

#consulta_general
@mapa_blueprint.route("/mapa_general",)
def consulta_general():
    try:
        conn=conectar ('localhost','root','','rasc')
        cur = conn.cursor()
        cur.execute("""SELECT * FROM mapa """)
        datos=cur.fetchall()
        data=[]
        for row in datos:
            dato={'cordenada':row[0],'nombre':row[1],'color':row[2],'veneno':row[3]}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify({'baul':data,'mensaje':'informacion del mapa'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'error'})

    
