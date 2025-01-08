from datetime import datetime


class Report:
    def __init__(self, risk_profile=None,update=None, risk_level=None,is_reported=None, data=None):
        

        if isinstance(data, dict):
            self.risk_profile = data.get("risk_profile",risk_profile)
            self.update = data.get("update", update or datetime.now().isoformat())
            self.risk_level = int(data.get("risk_level", risk_level))

        else:
            self.risk_profile = risk_profile 
            self.update = update or datetime.now().isoformat()
            self.risk_level = int(risk_level)
        
        if self.risk_level== -1:
            self.is_reported = True
        else: 
            self.is_reported = False  

    def to_dict(self):           
        return {
            "risk_profile": self.risk_profile ,
            "update": self.update ,
            "risk_level" : self.risk_level,
            "is_reported" : self.is_reported
        }

    #Updating report details
    def update_level(self,data):
        self.risk_level = data.get("risk_level")
        self.update = datetime.now().isoformat()
    
        
