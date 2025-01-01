from datetime import datetime


class Report:
    def __int__(self, report_id, user_id, title=None, content=None, created_at=None, updated_at=None, data=None):
        self.report_id = report_id
        self.user_id = user_id  # Associate the report with a specific user
        if isinstance(data, dict):
            self.title = data.get("title", title)
            self.content = data.get("content", content)
            self.created_at = data.get("created_at", created_at or datetime.now().isoformat())
            self.updated_at = data.get("updated_at", updated_at or datetime.now().isoformat())
        else:
            self.title = title
            self.content = content
            self.created_at = created_at or datetime.now().isoformat()
            self.updated_at = updated_at or datetime.now().isoformat()

    def to_dic(self):
        return {
            "report_id": self.report_id ,
            "user_id": self.user_id ,
            "title": self.title,
            "content" :self.content,
            "created_at" : self.created_at,
            "updated_at" : self.updated_at,
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