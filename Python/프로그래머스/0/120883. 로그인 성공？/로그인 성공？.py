def solution(id_pw, db):
    db = dict(db)
    id, pw = id_pw[:]
    
    if id in db.keys():
        if db[id] == pw:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"