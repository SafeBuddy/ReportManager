from datetime import datetime


class Report:
    def __int__(self, report_id, user_id=None, riskyprofile=None,created_at=None, title=None, content=None, risklevel=None, data=None):
        self.report_id = report_id

        if isinstance(data, dict):
            self.user_id = data.get("user_id",user_id)
            self.riskyprofile = data.get("riskyprofile", riskyprofile)
            self.created_at = data.get("created_at", created_at or datetime.now().isoformat())
            self.title = data.get("title", title)
            self.content = data.get("content", content)
            self.risklevel = data.get("risklevel", risklevel)
            

        else:

            self.user_id = user_id 
            self.riskyprofile = riskyprofile
            self.created_at = created_at or datetime.now().isoformat()
            self.title = title
            self.content = content
            self.risklevel = risklevel
            


    def to_dic(self):
        return {
            
            "report_id": self.report_id ,
            "user_id": self.user_id ,
            "riskyprofile" : self.riskyprofile,
            "created_at" : self.created_at,
            "title": self.title,
            "content" :self.content,
            "risklevel" : self.risklevel

        }

    #Updating report details
    def update(self,title=None,content=None):
        pass

    #Reading report
    def read(self):
        pass

    #Deleting report
    def delete(report_id,reports):
        if report_id in reports:
            del reports[report_id]
            return True
        return False
