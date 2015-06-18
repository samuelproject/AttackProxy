# AttackProxy

En el mundo de la Seguridad Informática es importante realizar análisis de vulnerabilidades de forma manual, sin embargo
es primordial automatizar la busqueda de vulnerabilidades, ya que esto permite que el Pentester pueda optimizar el tiempo, y de esta  manera obtener resultados de una manera mas expedita, (Por supuesto que es importante verificar que las vulnerabilidades encontradas no se traten de falsos positivos).

Se desarrolló una herramienta denominada AttackProxy, la cual permite realizar un ataque de fuerza bruta hacia un servicio 
proxy que se encuentre disponible. Cuando se realiza un Pentesting en BlackBox (Caja Negra), el pentester puede 
encontrarse limitado si tiene que auditar un servicio como éste, ya que probar credenciales de manera manual se vuelve
un tanto fastidioso.


#Usage
----

Dar permisos de ejecución,chmod +x.
Posteriormente:

./AttackProxy.py -h 

./AttackProxy.py -t [target] -u [user_proxy] -w [wordlist_password]      



#Screenshots
----

Ejemplo de un Proxy

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/8218104/361a4098-1517-11e5-925a-e7451737e559.jpg)

Ejemplo Tool

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/8217617/edb4c488-1514-11e5-8e00-f419deda7070.JPG)

Ejemplo Tool en ejecución

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/8217618/edc32d98-1514-11e5-998b-f9b9f476ab2c.JPG)


Como se puede observar en las imagenes anteriores, es posible realizar un ataque de fuerza bruta hacia este servicio,
además.
Cabe destacar que si no se conoce el nombre de usuario de Proxy, puede utilizar la opción -U la cual permite utilizar una lista de nombre de usuarios, para realizar el ataque.

Nota Legal
----

Es importante mencionar que este script esta hecho con fines netamente Éticos. No me hago responsable por el mal uso que puedan brindarle.
