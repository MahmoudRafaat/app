from fileinput import close
from flask import Flask,request
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    page = """<!DOCTYPE html>
            <html>
            <head>
            <style>
               body{
                   background-color:#E0FFFF;
               }
                
            </style>
            
            <title>Page Title</title>
            </head>
            <body>

            <h1><font size='15' color='black'><center> COVID-19 Test </center></font></h1>
            <img src="https://www.who.int/images/default-source/mca/mca-covid-19/coronavirus-2.tmb-1920v.jpg?Culture=ar&sfvrsn=4dba955c_6%201920w" alt="Covid-19" style="width:1523px;height:350px;">
            <p><font size='15' color='black'> In this web you will be asked about Symptoms of Corona , you will take a result if it is Corona or not and you will be advised by a doctor.</font></p>
            
            <a href="home"><font size='10' color='red'><center> Go to TEST </center></font></a>
            
            </body>
            </html> """
    return page


@app.route('/home', methods=["GET","POST"]) 
def home():
    if request.method == "GET":
        page = """<form method='post'>
            <html>
            <head>
            <style>
               body{
                   background: linear-gradient(#93B874 10%, #C9DCB9 70%);
               }
                
            </style>
            
            <title>Page Title</title>
            </head>
            <body>

            <label for="name">name:</label><br>
            <input type="text" id="name" name="name"><br>
            
            <label for="email">Email:</label><br>
            <input type="text" id="email" name="email"><br>
            
            <label for="age">Age:</label><br>
            <input type="number" id="age" name="age"><br>
            
            <label for="cough">Do you have a cough? </label><br>
            <div>
              <input type="radio" id="yes" name="cough" value=true>
                   
              <label for="yes">Yes</label>
            </div>
            
            <div>
              <input type="radio" id="no" name="cough" value=false>
              <label for="no">No</label>
            </div>
            
            <label for="coryza">Do you have a coryza? </label><br>
            <div>
            
              <input type="radio" id="yes" name="coryza" value=true>
                    
              <label for="yes">Yes</label>
            </div>
            

            <div>
              <input type="radio" id="no" name="coryza"value=false>
              <label for="no">No</label>
            </div>
            <label for="Ntaste">Do you have a New loss of taste or smell? </label><br>
            <div>
              <input type="radio" id="yes" name="Ntaste" value=true>
                  
              <label for="yes">Yes</label>
            </div>

            <div>
              <input type="radio" id="no" name="Ntaste" value=false>
              <label for="no">No</label>
            </div>
            <label for="Fatigue">Do you have a Fatigue? </label><br>
            <div>
              <input type="radio" id="yes" name="Fatigue" value=true>
                    
              <label for="yes">Yes</label>
            </div>

            <div>
              <input type="radio" id="no" name="Fatigue" value=false>
              <label for="no">No</label>
            </div>
            <label for="NOV">Do you have a Nausea or vomiting? </label><br>
            <div>
              <input type="radio" id="yes" name="NOV" value=true>
                  
              <label for="yes">Yes</label>
            </div>

            <div>
              <input type="radio" id="no" name="NOV" value=false>
              <label for="no">No</label>
            </div>
            <label for="Sorethroat">Do you have a Sore throat? </label><br>
            <div>
              <input type="radio" id="yes" name="Sorethroat" value=true>
                   
              <label for="yes">Yes</label>
            </div>

            <div>
              <input type="radio" id="no" name="Sorethroat" value=false>
              <label for="no">No</label>
            </div>
            
            <input type="submit" value="Submit">
            </form>"""
        return page
    
    elif request.method=="POST":
        
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        cough=request.form['cough']
        coryza=request.form['coryza']
        Sorethroat=request.form['Sorethroat']
        Nausea=request.form['NOV']
        Fatigue=request.form['Fatigue']
        Ntaste=request.form['Ntaste']
        
        web=str()
        
        if cough=='true'and coryza=='true' and Sorethroat=='true' and Nausea=='true' and Fatigue== 'true' and Ntaste== 'true' :
            web+="<h3><font color='red'>You are very likely to have Corona and must to do PCR test</font></h3>"
            web+="<h3> Adivce by a doctor: you should stay home and take Molnopiravir before sleeping at night and Paxlovid after dinner</h3>"
            
        elif cough=='true'and coryza=='true' and Sorethroat=='true'  and Fatigue== 'true' and Ntaste== 'true' and Nausea=='false':
            web+="<h3><font color='red'>you have Corona suspected and must to do PCR test</font></h3>"
            web+="<h3> Adivce by a doctor: you should stay home and take panadol after dinner</h3>"
            
        elif cough=='true'and coryza=='true' and Sorethroat=='false'  and Fatigue== 'true' and Ntaste== 'true' and Nausea=='true':
            web+="<h3><font color='red'>you have Corona suspected and must to do PCR test</font></h3>"
            web+="<h3> Adivce by a doctor: you should stay home and take panadol after dinner</h3>" 
            
        elif cough=='true'and coryza=='true' and Sorethroat=='true'  and Fatigue== 'true' and Ntaste== 'false' and Nausea=='true':
            web+="<h3><font color='red'>you have Corona suspected and must to do PCR test</font></h3>"
            web+="<h3> Adivce by a doctor: you should stay home and take panadol after dinner</h3>"
             
        elif cough=='false'and coryza=='true' and Sorethroat=='true'  and Fatigue== 'true' and Ntaste== 'true' and Nausea=='true':
            web+="<h3><font color='red'>you have Corona suspected and must to do PCR test</font></h3>"
            web+="<h3> Adivce by a doctor: you should stay home and take panadol after dinner</h3>"
            
        elif cough=='true'and coryza=='true' and Sorethroat=='true'  and Fatigue== 'false' and Ntaste== 'true' and Nausea=='true':
            web+="<h3><font color='red'>you have Corona suspected and must to do PCR test</font></h3>"
            web+="<h3> Adivce by a doctor: you should stay home and take panadol after dinner</h3>"
            
        elif cough=='true'and coryza=='false' and Sorethroat=='true'  and Fatigue== 'true' and Ntaste== 'true' and Nausea=='true':
            web+="<h3><font color='red'>you have Corona suspected and must to do PCR test</font></h3>"
            web+="<h3> Adivce by a doctor: you should stay home and take panadol after dinner</h3>"                                     
        elif cough=='false'and coryza=='true' and Sorethroat=='false'  and Fatigue== 'true' and Ntaste== 'false' and Nausea=='true' :
            web+="<h3><font color='gray'>you have very cold turn</font></h3>"   
            web+="<h3>you should drink hot herbal drinks</h3>"
            
        elif cough=='true'and coryza=='false' and Sorethroat=='true'  and Fatigue== 'ture' and Ntaste== 'true' and Nausea=='true':
            web+="<h3><font color='red'>you have Corona suspected and must to do PCR test</font></h3>"
            web+="<h3> Adivce by a doctor: you should stay home and take panadol after dinner</h3>"
            
        elif cough=='false'and coryza=='true' and Sorethroat=='true'  and Fatigue== 'true' and Ntaste== 'false' and Nausea=='true':
            web+="<h3><font color='gray'>you have very cold turn</font></h3>"    
            web+="<h3>you should drink hot herbal drinks</h3>"
            
        else:
            web+="<h3><font color='green'> you havenot corona </font> </h3>"
            web+="<h3>Eat healthy, follow the precautionary measures for Corona and stay away from gatherings</h3>"
                    
       
        
        # connect to DB
        con = sqlite3.connect('patient.db')
        con.execute("INSERT INTO PATIENT  (NAME       ,AGE            ,EMAIL        )\
        VALUES (?\n,?\n,?)", (name,age,email))
        
        con.commit()
        con.close()
       
           
        nam=f"<h3>Hallo {name}</h3>"     
        link = "<br><a href='/'>Back to Index</a>"
        return nam+web+link

    