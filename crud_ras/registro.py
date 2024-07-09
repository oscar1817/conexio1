
from flask import Flask
from flask_cors import CORS
from flask import Blueprint, jsonify,request
import pymysql

## Funcion para conectarnos a la base de datos de mysql
registro_blueprint = Blueprint('registro',__name__)
def conectar(vhost,vuser,vpass,vdb):
     conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb,)
     return conn 
 
##registrar especies 
@registro_blueprint.route("/registro_especie",methods=['POST'])
def registro():
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        x=cur.execute(""" insert into registro (numero,nombre,nombre_cientifico,tipo_de_especie,veneno,habitos,habitat,fecha_avistamiento,escamas) values \
            ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')""".format(request.json['numero'],\
            request.json['nombre'],request.json['nombre_cientifico'],request.json['tipo_de_especie'],request.json['veneno'],request.json['habitos'],request.json['habitat'],request.json['fecha_avistamiento'],request.json['escamas']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})

#consulta_general
@registro_blueprint.route("/especie_general",)
def consulta_general():
    try:
        conn=conectar ('localhost','root','','rasc')
        cur = conn.cursor()
        cur.execute("""SELECT * FROM registro """)
        datos=cur.fetchall()
        data=[]
        for row in datos:
            dato={'numero':row[0],'nombre':row[1],'nombre_cientifico':row[2],'tipo_de_especie':row[3],'veneno':row[4],'habitos':row[5],'habitat':row[6],'fecha_avistamiento':row[7],'escamas':row[8]}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify({'baul':data,'mensaje':'Especies registradas'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'error'})
    
    
##consulta especifica
@registro_blueprint.route("/consultar/<nombre>",methods=['GET'])
def consultar(nombre):
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM registro where nombre='{0}' """.format(nombre))
        datos=cur.fetchone()
        cur.close()
        conn.close()
        if datos!=None:
            dato={'numero':datos[0],'nombre':datos[1],'nombre_cientifico':datos[2],'tipo_de_especie':datos[3],'veneno':datos[4],'habitos':datos[5],'habitat':datos[6],'fecha_avistamiento':datos[7],'escamas':datos[8]}
            return jsonify({'registro':dato,'mensaje':'Registro  encontrado'})
        else:
            return jsonify({'mensaje':'Registro no encontrado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
    
##eliminar especie  
@registro_blueprint.route("/eliminar/<nombre>",methods=['DELETE'])
def eliminar(nombre):
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        x=cur.execute("""delete from registro where nombre={0}""".format(nombre))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'error'})

