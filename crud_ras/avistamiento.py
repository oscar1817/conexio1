from flask import Flask
from flask_cors import CORS
from flask import Blueprint, jsonify,request
import pymysql
## Funcion para conectarnos a la base de datos de mysql
avistamiento_blueprint = Blueprint('avistamiento',__name__)
def conectar(vhost,vuser,vpass,vdb):
     conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb,)
     return conn 

##registrar avistamiento
@avistamiento_blueprint.route("/avistamiento",methods=['POST'])
def registro():
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        x=cur.execute(""" insert into avistamiento (ubicacion,hora,aspecto,ataco,imagen) values \
            ('{0}','{1}','{2}','{3}','{4}')""".format(request.json['ubicacion'],\
           request.json['hora'],request.json['aspecto'],request.json['ataco'],request.json['imagen']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Avistamiento agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})

#consulta_general
@avistamiento_blueprint.route("/avistamientos_general",)
def consulta_general():
    try:
        conn=conectar ('localhost','root','','rasc')
        cur = conn.cursor()
        cur.execute("""SELECT * FROM avistamiento """)
        datos=cur.fetchall()
        data=[]
        for row in datos:
            dato={'numero':row[0],'ubicaicion':row[1],'hora':row[2],'aspecto':row[3],'ataco':row[4],'imagen':row[5],}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify({'baul':data,'mensaje':'Avistamientos en la Zona'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'error'})

