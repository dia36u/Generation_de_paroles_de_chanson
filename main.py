import wrapper
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/api/v1/user/', methods=['POST'])
def create_user():
    # On recupere le corps (payload) de la requete
    payload = request.form.to_dict()
    result = wrapper.add_user(**payload)

    if result:
        return jsonify(status='True', message='User created')
    return jsonify(status='False')

@app.route('/api/v1/user/', methods=['GET'])
def get_all_users():
    result = wrapper.get_all_users()
    if result:
        return jsonify(status="True", 
        result= [
            {"nom":user.nom,
             "genres":user.genres,
             "songs":user.songs,
             "popularity": user.popularity,
             "id": user.id} for user in result.all() ])
    return jsonify(status="False")

@app.route('/api/v1/user/<songs>', methods=['GET'])
def get_user(nom):
    result = wrapper.get_user_by_id(nom)
    if result:
        return jsonify(status="True", 
                    result={"nom":result.nom,
                            "genres":result.genres,
                            "songs":result.songs,
                            "popularity": result.popularity,
                            "id": result.id}
                        )
    return jsonify(status="False")

@app.route('/api/v1/user/<nom>', methods=['PUT'])
def mofify_user(nom):
    result = wrapper.update_attribute(nom, request.form.to_dict())
    if result:
        return jsonify(status="True",
                        message= "updated",
                        result={
                            "nom":result.nom,
                            "genres":result.genres,
                            "songs":result.songs,
                            "popularity": result.popularity,
                            "id": result.id}
                            )
    return jsonify(status= "False")


@app.route('/api/v1/user/<nom>', methods=['DELETE'])
def delete_user(nom):
    result = wrapper.delete_user_by_id(nom)
    if result:
        return jsonify(status="True",
                        message= "Deleted",
                        nom=nom
                        )
    return jsonify(status="False")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)