from flask import Flask, render_template,request,redirect,url_for
import pyodbc as odbc

app = Flask(__name__)

# Connexion à la base de données SQL SERVER
conn_str = "Driver={ODBC Driver 17 for SQL Server};Server=Geek_Machine\\SQLEXPRESS;Database=zorodb;Trusted_connection=yes"
conn = odbc.connect(conn_str)
app.config['SQL_CONN'] = conn

#############CONNEXION_PAGE############

@app.route("/")
def Connexion():
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    conn.close()
    return render_template("Connexion.html")

#############ACCUEIL############

@app.route("/Accueil/")
def Accueil():
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    conn.close()
    return render_template("Accueil.html")

#############PRODUIT############

@app.route("/Afficher_produit/")
def Afficher_produit():
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM Produit ")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('./produit/Afficher_produit.html', data=data)

@app.route("/Ajouter_produit/")
def Ajouter_produit():
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    conn.close()
    return render_template('./produit/Ajouter_produit.html')

@app.route("/Ajouter_produit_traitement/",methods=['POST'])
def Ajouter_produit_traitement():
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    Nom = request.form['Nom_produit']
    Cat = request.form['Categorie']
    Prix = request.form['Prix_Unitaire']

    cursor = conn.cursor()
    cursor.execute(
            "INSERT INTO Produit(NomProduit, CatProduit, PrixUnitaire) VALUES (?, ?, ?)",
            (Nom, Cat, Prix)
        )
    cursor.execute("SELECT * FROM Produit")
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return render_template("./produit/Afficher_produit.html",data=data)

@app.route('/Supprimer_produit/<int:Id>', methods=['GET', 'POST'])
def Supprimer_produit(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id = int(Id)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produit WHERE IdProduit = ? ", item_id)
    element = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('./produit/Supprimer_produit.html', element=element,item_id=item_id )
    
@app.route('/Supprimer_produit_traitement/<int:Id>', methods=['GET', 'POST'])
def Supprimer_produit_traitement(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id = int(Id)
    
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Produit WHERE IdProduit = ?', item_id)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('Afficher_produit'))

@app.route('/Modifier_produit/<int:Id>', methods=['GET', 'POST'])
def Modifier_produit(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id = int(Id)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produit WHERE IdProduit = ? ", item_id)
    data = cursor.fetchall()
    cursor.close()
    return render_template('./produit/Modifier_produit.html', data=data,item_id =item_id  )

@app.route('/Modifier_produit_traitement/<int:Id>', methods=['GET', 'POST'])
def Modifier_produit_traitement(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id=int(Id)
    
    Nom = request.form['Nom_produit']
    Cat = request.form['Categorie']
    Prix = request.form['Prix_Unitaire']

    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Produit SET NomProduit = ?, CatProduit = ?, PrixUnitaire= ? WHERE IdProduit = ?",
        (Nom, Cat, Prix, item_id)
    )
    conn.commit()
    return redirect(url_for('Afficher_produit', item_id=item_id))


#############MAGASIN############

@app.route("/Afficher_magasin/")
def Afficher_magasin():
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM Magasin ")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('./magasin/Afficher_magasin.html', data=data)

@app.route("/Ajouter_magasin/")
def Ajouter_magasin():
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    conn.close()
    return render_template('./magasin/Ajouter_magasin.html')

@app.route("/Ajouter_magasin_traitement/",methods=['POST'])
def Ajouter_magasin_traitement():
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    Nom = request.form['Nom_magasin']
    adresse = request.form['Adresse_magasin']
    tel = request.form['Telephone']
    email = request.form['email']

    cursor = conn.cursor()
    cursor.execute(
            "INSERT INTO Magasin(NomMagasin, AdresseMagasin, Telephone, mail) VALUES (?, ?, ?, ?)",
            (Nom, adresse, tel,email)
        )
    cursor.execute("SELECT * FROM Magasin")
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return render_template("./magasin/Afficher_magasin.html",data=data)

@app.route('/Supprimer_magasin/<int:Id>', methods=['GET', 'POST'])
def Supprimer_magasin(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id = int(Id)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Magasin WHERE IdMagasin = ? ", item_id)
    element = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('./magasin/Supprimer_magasin.html', element=element,item_id=item_id )
    
@app.route('/Supprimer_magasin_traitement/<int:Id>', methods=['GET', 'POST'])
def Supprimer_magasin_traitement(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id = int(Id)
    
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Magasin WHERE IdMagasin = ?', item_id)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('Afficher_magasin'))

@app.route('/Modifier_magasin/<int:Id>', methods=['GET', 'POST'])
def Modifier_magasin(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id = int(Id)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Magasin WHERE IdMagasin = ? ", item_id)
    data = cursor.fetchall()
    cursor.close()
    return render_template('./magasin/Modifier_magasin.html', data=data,item_id =item_id  )

@app.route('/Modifier_magasin_traitement/<int:Id>', methods=['GET', 'POST'])
def Modifier_magasin_traitement(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id=int(Id)
    
    Nom = request.form['Nom_magasin']
    adresse = request.form['Adresse_magasin']
    tel = request.form['Telephone']
    email = request.form['email']

    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Magasin SET NomMagasin = ?, AdresseMagasin = ?, Telephone= ?, mail= ? WHERE IdMagasin = ?",
        (Nom, adresse, tel, email, item_id)
    )
    conn.commit()
    return redirect(url_for('Afficher_magasin', item_id=item_id))

#############STOCK############

@app.route("/Afficher_stock/")
def Afficher_stock():
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    cursor = conn.cursor()
    cursor.execute("SELECT Idstock,Quantitestock, NomProduit, NomMagasin FROM Stock INNER JOIN Produit ON Produit.IdProduit=Stock.IdProduit INNER JOIN Magasin ON Magasin.IdMagasin=Stock.IdMagasin")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('./stock/Afficher_stock.html', data=data)

@app.route("/Ajouter_stock/")
def Ajouter_stock():
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    cursor = conn.cursor()
    cursor.execute("SELECT IdProduit,NomProduit FROM Produit")
    data = cursor.fetchall()
    cursor.execute("SELECT IdMagasin,NomMagasin FROM Magasin")
    data1 = cursor.fetchall()
    conn.close()
    return render_template('./stock/Ajouter_stock.html',data=data,data1=data1)

@app.route("/Ajouter_stock_traitement/",methods=['POST'])
def Ajouter_stock_traitement():
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    quantite = request.form['Quantite']
    produit = request.form['Produit']
    magasin = request.form['Magasin']

    cursor = conn.cursor()
    cursor.execute(
            "INSERT INTO Stock (Quantitestock, IdProduit, IdMagasin) VALUES (?, ?, ?)",
            (quantite, produit, magasin)
        )
    cursor.execute("SELECT Idstock,Quantitestock, NomProduit, NomMagasin FROM Stock INNER JOIN Produit ON Produit.IdProduit=Stock.IdProduit INNER JOIN Magasin ON Magasin.IdMagasin=Stock.IdMagasin")
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return render_template("./stock/Afficher_stock.html",data=data)

@app.route('/Supprimer_stock/<int:Id>', methods=['GET', 'POST'])
def Supprimer_stock(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id = int(Id)
    
    cursor = conn.cursor()
    cursor.execute("SELECT Idstock,Quantitestock, NomProduit, NomMagasin FROM Stock INNER JOIN Produit ON Produit.IdProduit=Stock.IdProduit INNER JOIN Magasin ON Magasin.IdMagasin=Stock.IdMagasin WHERE Idstock = ?", item_id)
    element = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('./stock/Supprimer_stock.html', element=element,item_id=item_id )

@app.route('/Supprimer_stock_traitement/<int:Id>', methods=['GET', 'POST'])
def Supprimer_stock_traitement(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id = int(Id)
    
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Stock WHERE Idstock = ?', item_id)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('Afficher_stock'))

@app.route('/Modifier_stock/<int:Id>', methods=['GET', 'POST'])
def Modifier_stock(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id = int(Id)
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT Idstock, Quantitestock, NomProduit, NomMagasin FROM Stock INNER JOIN Produit ON Produit.IdProduit=Stock.IdProduit INNER JOIN Magasin ON Magasin.IdMagasin=Stock.IdMagasin WHERE Idstock = ?", item_id)
    data = cursor.fetchall()
    
    cursor.execute("SELECT IdProduit, NomProduit FROM Produit")
    data1 = cursor.fetchall()
    
    cursor.execute("SELECT IdMagasin, NomMagasin FROM Magasin")
    data2 = cursor.fetchall()
    cursor.close()
    
    return render_template('./stock/Modifier_stock.html', data=data,data1=data1,data2=data2,item_id =item_id  )

@app.route('/Modifier_stock_traitement/<int:Id>', methods=['GET', 'POST'])
def Modifier_stock_traitement(Id):
    conn = odbc.connect(conn_str)
    app.config['SQL_CONN'] = conn
    
    item_id=int(Id)
    
    quantite = request.form['Quantite']
    produit = request.form['Produit']
    magasin = request.form['Magasin']

    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Stock SET Quantitestock = ?, IdProduit = ?, IdMagasin = ? WHERE Idstock = ?",
        (quantite, produit, magasin, item_id)
    )
    conn.commit()
    return redirect(url_for('Afficher_stock', item_id=item_id))


if __name__ == "__main__":
    app.run(debug=True)