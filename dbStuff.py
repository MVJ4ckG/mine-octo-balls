import sqlite3
import traceback

class Database:
  def __init__(self, dbName):
    self.dbName = dbName
    self.conn = sqlite3.connect(dbName)
    self.c = self.conn.cursor()

    #create tables
    self.c.execute("CREATE TABLE IF NOT EXISTS agent(agentId integer PRIMARY KEY, firstname text, surname text, email text, password text)")
    self.c.execute("CREATE TABLE IF NOT EXISTS property(propertyId integer PRIMARY KEY, managedby text, area text, bedroomno integer, price real, status text)")
    self.c.execute("CREATE TABLE IF NOT EXISTS client(clientId integer PRIMARY KEY, name text, phonenum integer, prefarea text, maxprice real, minrooms integer)")
    self.c.execute("CREATE TABLE IF NOT EXISTS viewing(viewingId integer PRIMARY KEY, clientId integer, propertyId integer)")

    self.conn.commit()

  def listAllTables(self):
    print("agent")
    self.c.execute("SELECT * FROM agent")
    data = self.c.fetchall()    
    for item in data:
      print(item)

    print("client")
    self.c.execute("SELECT * FROM client")
    data = self.c.fetchall()    
    for item in data:
      print(item)

    print("property")
    self.c.execute("SELECT * FROM property")
    data = self.c.fetchall()    
    for item in data:
      print(item)

    print("viewing")
    self.c.execute("SELECT * FROM viewing")
    data = self.c.fetchall()    
    for item in data:
      print(item)



  def close(self):
    self.conn.close()

  def execute(self, sql, params=None):
    try:
      if params:
        self.c.execute(sql, params)
      else:
        self.c.execute(sql)
      self.conn.commit()
    except:
      print(traceback.format_exc())


  def addagentToDB(self, firstname, surname, email, password):
    #add agent to database
    self.c.execute("INSERT INTO agent (firstname, surname, email, password) VALUES (?, ?, ?, ?)", (firstname, surname, email, password))

  def addclientToDB(self, name, phonenum, prefarea, maxprice, minrooms):
    self.c.execute("INSERT INTO client (name, phonenum, prefarea, maxprice, minrooms) VALUES (?, ?, ?, ?, ?)", (name, phonenum, prefarea, maxprice, minrooms))
  
  def addpropertytoDB(self, managedby, area, bedroomno, price, status):
                      )
  def getagentFromDB(self, wordList, debug=False):
    self.c.execute("SELECT * FROM agent")
    data = self.c.fetchall()    
    for item in data:
      wordId = item[0]
      word = item[1]
      meaning = item[2]
      phonetic = item[3]
      wordList.addWord(word, meaning, phonetic, wordId)
    return wordList

  def getagentAndclientFromDB(self):
    agent = []
    self.c.execute("SELECT * FROM agent LEFT JOIN viewing ON agent.wordId = viewing.wordId")
    data = self.c.fetchall()    
    for item in data:
      newWord = []
      newWord.append(item[0]) #wordId
      newWord.append(item[1]) #word
      newWord.append(item[2]) #meaning 
      newWord.append(item[3]) #phonetics
      newWord.append(item[4]) #viewingId 
      newWord.append(item[5]) #playerId 
      newWord.append(item[6]) #wordId 
      newWord.append(item[7]) #correct
      agent.append(newWord)
    return agent





  def showCurrentUsernames(self):
    self.execute("SELECT username, name, score, password FROM property LEFT JOIN client ON property.playerId = client.playerId ORDER BY score DESC")
    print("Current usernames (plus highest score):")
    data = self.c.fetchall()
    for item in data:
      print(item[0], " (score: " + str(item[2]) + ")" + item[3])
    print("---------------")
