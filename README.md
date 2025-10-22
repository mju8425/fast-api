# FastAPI en Vercel (Plantilla mínima)

Proyecto listo para desplegar un backend **FastAPI** en **Vercel** con configuración cero.

## Estructura
```
/ (raíz)
  requirements.txt
  src/
    index.py
    router/
      __init__.py
      router.py
```

## Ejecutar localmente
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
# source .venv/bin/activate

pip install -r requirements.txt
uvicorn src.index:app --reload
# http://127.0.0.1:8000  y  http://127.0.0.1:8000/users
```

## Despliegue en Vercel
- Sube este repo a GitHub.
- En Vercel, **Import Project** desde GitHub y despliega.
- No necesitas `vercel.json`.
- Si configuras “Root Directory”, déjalo vacío (raíz del repo) o asegúrate de apuntar a la carpeta correcta.

## Notas
- Las Functions de Vercel son sin estado; usa una base de datos gestionada si la necesitas.
- Puedes renombrar `src/index.py` a `index.py` en la raíz si prefieres.
