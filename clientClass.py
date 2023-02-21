class client:
  def __init__(self):
    pass
  def signin(self,username,password,TYPE,made):
    #made is a boolean defining if it is a signin or signup
    if made == True:
      #check if the username and password are correct
      con = sqlite3.connect("orders.db")
      cur = con.cursor()
      cur.execute("CREATE TABLE IF NOT EXISTS login(username,password,TYPE)") #probably unecessary but create if someone tries to access and doesn't exist
      cur.execute("SELECT * FROM login WHERE username IS ? AND password is ? AND TYPE is ?;",(username,password,TYPE))
      valid = cur.fetchall()
      if len(valid) == 0:
        valid = False
      else:
        #add code here to connect to sockets because it is a valid login
        pass
      cur.close()
    else:
      #add to db and let them in to next page
      con = sqlite3.connect("orders.db")
      cur = con.cursor()
      cur.execute("CREATE TABLE IF NOT EXISTS login(username,password,TYPE)")
      cur.execute("INSERT INTO login VALUES (?,?,?);",(username,password,TYPE))
      cur.close()
      #add code to let them in
  def sendToHost(self,string,username):
    pass
