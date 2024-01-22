import fastapi
import psycopg2
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,JSONResponse, RedirectResponse
from fastapi import Request , Form, Depends, FastAPI, HTTPException, status , Response , Cookie, Header, security
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer, OAuth2PasswordRequestForm



app = fastapi.FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="css")


connection = psycopg2.connect(
    host='localhost',\
    port=5432,
    user='postgres',
    password='postgres'
    # dbname=postgres_db
)
cursor = connection.cursor()



@app.get("/")
def read_root(request: Request):
    cursor.execute("SELECT * FROM cadastro")
    users = cursor.fetchall()
    return templates.TemplateResponse("users.html", {"request": request, "users": users})
    # return {"EU AMO A DANI"}

@app.get("/users")
def get_users(request: Request):
    cursor.execute("SELECT * FROM cadastro order by id asc")
    users = cursor.fetchall()
    return templates.TemplateResponse("users.html",  context={"request": request, "users": users})

@app.get("/users/{user_id}")
def get_users(user_id: int):
    cursor.execute(f"SELECT * FROM cadastro where id = {user_id}")
    users = cursor.fetchall()
    return users

@app.get("/add", response_class=HTMLResponse)
def add_users(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/add", response_class=HTMLResponse)  
def post_get_users(request: Request, nome: str = Form(...), sobrenome: str = Form(...), email: str = Form(...), cpf: str = Form(...)):
    cursor.execute('INSERT INTO public.cadastro ("Nome", "Sobrenome", "Email", "CPF") VALUES (%s, %s, %s, %s)',
                (nome, sobrenome, email, cpf))
    connection.commit()
    # return JSONResponse(content={"message": "Dados inseridos com sucesso"}, status_code=200)
    return RedirectResponse(url="/users", status_code=303)


@app.get("/update/{user_id}", response_class=HTMLResponse)
def update_users(request: Request, user_id: int):
    return templates.TemplateResponse("index.html", {"request": request, "user_id": user_id})


@app.post("/update/{user_id}", response_class=HTMLResponse)  
def post_update_users(request: Request, user_id: int, nome: str = Form(...),
                       sobrenome: str = Form(...), email: str = Form(...), cpf: str = Form(...)):
    sql = """
        UPDATE public.cadastro
        SET "Nome" = %s, "Sobrenome" = %s, "Email" = %s, "CPF" = %s
        WHERE id = %s
    """
    # cursor.execute('UPDATE public.cadastro SET "Nome" = %s, "Sobrenome" = %s, "Email" = %s, "CPF" = %s WHERE id = %s', (nome, sobrenome, email, cpf, user_id))
    cursor.execute(sql, (nome, sobrenome, email, cpf, user_id))
    connection.commit()
    return RedirectResponse(url="/users", status_code=303)

@app.post("/delete/{user_id}")
@app.get("/delete/{user_id}")
def deleteUser(request : Request,user_id: int):
    cursor.execute(f"DELETE FROM public.cadastro where id = {user_id}")
    connection.commit()
    return RedirectResponse(url="/users")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)