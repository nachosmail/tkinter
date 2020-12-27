from pprint import pprint
##-------COMANDO PARA CREAR USUARIOS DE TEST DESDE CONSOLA-----------
# curl -X POST -H "Content-Type: application/json" -d '{ "site_id":"MLA" }' https://api.mercadolibre.com/users/test_user?access_token="AQUI PEGAR EL ACCESS_TOKEN"

#PARA UTILIZAR COMO JSON
user1={
	"id":644405827,
	"nickname":"TETE2997594",
	"password":"qatest5960",
	"site_status":"active",
	"email":"test_user_77915330@testuser.com",
	"rol":"comprador",
	"public_key":"TEST-c2daffda-7625-4fea-871c-7ec6095cbdf2",
	"access_token":"TEST-3232494397818692-091417-554ee6f91be9b95881446312e24f0947-644405827"
	#"client_id":"3397191146646529",
	#"client_secret":"InH2WZynpTgzmhMK7ubC2pBDskpWZ7xt"
}

user2={
	"id":644411786,
	"nickname":"TETE8964284",
	"password":"qatest7868",
	"site_status":"active",
	"email":"test_user_53818886@testuser.com",
	"rol":"vendedor",
	"public_key":"TEST-91c96bda-2473-4e9b-b19d-8ccd3b127c1c",
	"access_token":"TEST-3397191146646529-091417-59a35b707bfd354669c294a2da005224-644411786"
	#"client_id":"3397191146646529",
	#"client_secret":"InH2WZynpTgzmhMK7ubC2pBDskpWZ7xt"
}


#pprint(user2)
print(user2["access_token"])
