import sqlite3
from mapClass import mapping
class host:
    def __init__(self,command,name):
        self.command = command
        self.name = name

    #takes in command from sockets and executes   

        con = sqlite3.connect("orders.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS orders(name NOT NULL PRIMARY KEY,address,phone,topping,slices,tracking,route)")
        cur.execute(self.command)
        con.commit()

        cur.close()
        mapping.mapRoute(self.name,self.address)

    def sendDBToDriver(self):
        con = sqlite3.connect("orders.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM orders;")
        return(cur.fetchall)
        cur.close()
    
    def sendRoute(self,ids):
        con = sqlite3.connect("orders.db")
        cur = con.cursor()
        routelist = []
        for i in ids:        
            cur.execute("SELECT FROM orders values WHERE id IS ?",(i))
            routelist.append(cur.fetchall)
        cur.close()
        com.sendToDriver(routelist)

    def chooseOrders(self):
        #this will take the route
        con = sqlite3.connect("orders.db")
        cur = con.cursor()
        cur.execute("SELECT FROM orders (name,slices,route) VALUES WHERE topping IS 'cheese'")
        
        routes=cur.fetchall()
        
        #make a list of streets in each route
        for i in routes:
            route.append(i[2])
        #check for common roads
        common_routes = {}
        
        for route in routes:
            #keep track of how many adsresses go through a certain road
            
            if i[2] in common_routes.keys():
                common_routes[i[2]].append([route[0],route[1]]) 
            else:
                common_routes[i[2]] = [[route[0],route[1]]]
            
        
        common_streets = {}
        #check dictionary for most used roads and make groups each group will be a list in common routes
        
        for info in common_routes:
            total_slices = 0
            ids = []
            for i in info:
                total_slices += i[1]
                ids.append(i[0])
            common_streets[info] = [total_slices,ids]
        
        index = 0 #place holder    
        for info in common_streets:
            if total_slices == 8:
                self.sendRoute()
                common_streets.pop(index)
            elif total_slices < 8:
                try:
                    groups.append(info)
                except:
                    groups = []
            else:
                self.splitGroup(info)
            index +=1
    #takes in a list containing ids that go through a road and finds the best group to merge it with
    def mergeGroups(self,groups):
        
    #takes in same as mergeGroup function but splits group
    def splitGroup(self,info):
        pass 

                

                
            

            
            
            
                    
            
            
  
