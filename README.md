# 🛠️ Guía de Trabajo en Equipo con Git

Este manual describe el flujo de trabajo recomendado para un proyecto con las ramas: `development`, `staging` y `production`. Sigue este paso a paso para evitar errores y mantener un flujo limpio y profesional.

---

## 🔁 Estructura de ramas

- `development`: Rama de integración donde se juntan todas las funcionalidades nuevas.
- `staging`: Rama para pruebas antes de pasar a producción.
- `production`: Rama estable que contiene el código en vivo.

---

## 📌 Flujo de Trabajo Diario

### 1. Clona el repositorio (una sola vez)
```bash
git clone <URL-del-repo>
cd <nombre-del-repo>
```

### 2. Obtén todas las ramas remotas
```bash
git fetch --all
```

### 3. Cámbiate a la rama `development`
```bash
git checkout development
```

### 4. Actualiza tu rama `development`
```bash
git pull origin development
```

### 5. Crea tu rama de funcionalidad (feature)
```bash
git checkout -b feature/nombre-de-la-funcionalidad
```

### 6. Trabaja en tu funcionalidad

Haz commits con mensajes descriptivos:
```bash
git add .
git commit -m "feat: agrega funcionalidad X"
```

### 7. Sube tu rama al repositorio remoto
```bash
git push origin feature/nombre-de-la-funcionalidad
```

---

## ✅ Proceso de Revisión

1. Crea un Pull Request hacia `development`.
2. Pide revisión a tus compañeros.
3. Verifica que pasen las pruebas (si existen).

---

## 🔄 Mantén tu rama actualizada antes de hacer merge
```bash
git checkout development
git pull origin development
git checkout feature/nombre-de-la-funcionalidad
git merge development
```

Si hay conflictos, resuélvelos y luego:
```bash
git add .
git commit -m "fix: resuelve conflictos con development"
```

---

## 🔁 Fusiona tu rama a `development`

Desde el Pull Request o desde terminal:
```bash
git checkout development
git merge feature/nombre-de-la-funcionalidad
git push origin development
```

---

## 🚀 Despliegue a `staging` (para pruebas)

Cuando haya suficientes funcionalidades listas:
```bash
git checkout staging
git pull origin staging
git merge development
git push origin staging
```

---

## ✅ Despliegue a `production`

Cuando `staging` esté probado y validado:
```bash
git checkout production
git pull origin production
git merge staging
git push origin production
```

---

## 🧠 Buenas Prácticas

- Nunca trabajes directamente en `development`, `staging` o `production`.
- Usa nombres descriptivos para tus ramas: `feature/login`, `fix/bug-navbar`, etc.
- Siempre haz `pull` antes de `mergear`.
- Commits frecuentes y con mensajes claros.
- Evita mezclar muchas funcionalidades en una sola rama.

---

💡 **Mantener un flujo limpio facilita la colaboración y reduce errores. ¡Trabajemos en equipo con orden y responsabilidad!**
