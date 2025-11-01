Perfect ✅ — here’s the **clean, production-style instruction set** for your **Django + DRF portfolio project (`DSGenAI_Portfolio`)**.

This tells you exactly:

* what each app should contain
* what models (with column names) you must create
* what URLs (endpoints) you should expose
* and what each endpoint should return (briefly)

---

# 🧩 **APP 1 — `users`**

### 🎯 **Purpose**

Handles authentication, user info, and your professional profile.

---

### 🧱 **Models**

#### 1️⃣ `User`

*(Extend Django’s `AbstractUser`)*
Columns:

* `username`
* `email` (unique)
* `password`
* `first_name`
* `last_name`
* `role` → choices: `Admin`, `Visitor`, `Recruiter`
* `is_active`, `is_staff`, `is_superuser`, `date_joined`

#### 2️⃣ `Profile`

Linked with `OneToOneField(User)`
Columns:

* `user`
* `headline` → short title (e.g. *Data Scientist | GenAI Engineer*)
* `bio` → about you
* `profile_picture` → image upload
* `location`
* `phone_number` *(optional)*
* `github_url`
* `linkedin_url`
* `portfolio_website`
* `created_at`, `updated_at`

---

### 🌐 **Endpoints**

| Method    | URL                           | Purpose              | Returns               |
| --------- | ----------------------------- | -------------------- | --------------------- |
| GET       | `/api/v1/users/profile/`      | List all profiles    | JSON list of profiles |
| GET       | `/api/v1/users/profile/<id>/` | Retrieve one profile | Single profile JSON   |
| PUT/PATCH | `/api/v1/users/profile/<id>/` | Update your profile  | Updated JSON          |
| POST      | `/api/v1/users/register/`     | Register new user    | Success + user data   |
| POST      | `/api/v1/users/login/`        | Login (JWT/token)    | Auth token            |

---

# 🧩 **APP 2 — `portfolio`**

### 🎯 **Purpose**

Showcase your projects and technologies.

---

### 🧱 **Models**

#### 1️⃣ `Technology`

Columns:

* `name`
* `category` *(e.g., Backend, ML, GenAI)*
* `description` *(optional)*

#### 2️⃣ `Project`

Columns:

* `title`
* `description`
* `tech_stack` → ManyToMany with `Technology`
* `github_link`
* `demo_link`
* `image`
* `created_at`
* `featured` (boolean)
* `tags` *(optional)*

---

### 🌐 **Endpoints**

| Method    | URL                      | Purpose              | Returns         |
| --------- | ------------------------ | -------------------- | --------------- |
| GET       | `/api/v1/projects/`      | List all projects    | JSON list       |
| GET       | `/api/v1/projects/<id>/` | Get specific project | JSON object     |
| POST      | `/api/v1/projects/`      | Create project       | Created project |
| PUT/PATCH | `/api/v1/projects/<id>/` | Update project       | Updated project |
| DELETE    | `/api/v1/projects/<id>/` | Delete project       | 204 response    |
| GET       | `/api/v1/technologies/`  | List tech stack      | JSON list       |

🧭 Filters:

* `/api/v1/projects/?tech=python` → filter by technology
* `/api/v1/projects/?search=chatbot` → search by title/description

---

# 🧩 **APP 3 — `experience`**

### 🎯 **Purpose**

Display your professional experience and education timeline.

---

### 🧱 **Models**

#### 1️⃣ `Experience`

Columns:

* `company`
* `role`
* `start_date`
* `end_date` (nullable)
* `location`
* `description`

#### 2️⃣ `Education` *(optional)*

Columns:

* `institution`
* `degree`
* `field_of_study`
* `start_year`
* `end_year`
* `grade` *(optional)*

---

### 🌐 **Endpoints**

| Method    | URL                        | Purpose              | Returns       |
| --------- | -------------------------- | -------------------- | ------------- |
| GET       | `/api/v1/experience/`      | List all experiences | JSON list     |
| GET       | `/api/v1/experience/<id>/` | One experience       | JSON object   |
| POST      | `/api/v1/experience/`      | Add new              | Created entry |
| PUT/PATCH | `/api/v1/experience/<id>/` | Update               | Updated entry |
| DELETE    | `/api/v1/experience/<id>/` | Delete               | 204 response  |
| GET       | `/api/v1/education/`       | List education       | JSON list     |

---

# 🧩 **APP 4 — `skills`**

### 🎯 **Purpose**

Show your technical skills and proficiency bars.

---

### 🧱 **Model: `Skill`**

Columns:

* `name`
* `category` → (e.g. ML, Web, Cloud)
* `proficiency` → Integer (0–100 %)
* `description` *(optional)*

---

### 🌐 **Endpoints**

| Method    | URL                    | Purpose         | Returns           |
| --------- | ---------------------- | --------------- | ----------------- |
| GET       | `/api/v1/skills/`      | List all skills | JSON list         |
| POST      | `/api/v1/skills/`      | Add new skill   | Created skill     |
| GET       | `/api/v1/skills/<id>/` | Retrieve        | Single skill JSON |
| PUT/PATCH | `/api/v1/skills/<id>/` | Update          | Updated skill     |
| DELETE    | `/api/v1/skills/<id>/` | Delete          | 204 response      |

---

# 🧩 **APP 5 — `certificates`**

### 🎯 **Purpose**

Display professional certifications (e.g., Azure AI-102, ML, DL).

---

### 🧱 **Model: `Certificate`**

Columns:

* `name`
* `issuer` (e.g., Microsoft, Coursera)
* `issue_date`
* `credential_id` *(optional)*
* `credential_url`
* `image` (optional)
* `description` *(optional)*

---

### 🌐 **Endpoints**

| Method | URL                          | Purpose             | Returns                 |
| ------ | ---------------------------- | ------------------- | ----------------------- |
| GET    | `/api/v1/certificates/`      | List certificates   | JSON list               |
| POST   | `/api/v1/certificates/`      | Add new certificate | Created certificate     |
| GET    | `/api/v1/certificates/<id>/` | Retrieve            | Single certificate JSON |
| DELETE | `/api/v1/certificates/<id>/` | Delete              | 204 response            |

---

# 🧩 **APP 6 — `contact`**

### 🎯 **Purpose**

Store recruiter messages or contact form submissions.

---

### 🧱 **Model: `ContactMessage`**

Columns:

* `name`
* `email`
* `subject`
* `message`
* `created_at` (auto)

---

### 🌐 **Endpoints**

| Method | URL                     | Purpose                    | Returns              |
| ------ | ----------------------- | -------------------------- | -------------------- |
| POST   | `/api/v1/contact/`      | Submit message             | Success + saved data |
| GET    | `/api/v1/contact/`      | View messages (admin only) | List of messages     |
| DELETE | `/api/v1/contact/<id>/` | Delete message             | 204 response         |

---

# 🔗 **Main URL Integration**

In `portfolio_project/urls.py`, include all:

```python
urlpatterns = [
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/', include('apps.portfolio.urls')),
    path('api/v1/', include('apps.experience.urls')),
    path('api/v1/', include('apps.skills.urls')),
    path('api/v1/', include('apps.certificates.urls')),
    path('api/v1/', include('apps.contact.urls')),
]
```

---

# 📦 **Final Output Summary**

| App            | Main Models           | Example Endpoint         | Returns              |
| -------------- | --------------------- | ------------------------ | -------------------- |
| `users`        | User, Profile         | `/api/v1/users/profile/` | Profile JSON         |
| `portfolio`    | Project, Technology   | `/api/v1/projects/`      | Project list         |
| `experience`   | Experience, Education | `/api/v1/experience/`    | Experience JSON      |
| `skills`       | Skill                 | `/api/v1/skills/`        | Skills list          |
| `certificates` | Certificate           | `/api/v1/certificates/`  | Certificates JSON    |
| `contact`      | ContactMessage        | `/api/v1/contact/`       | Contact form success |

---

Would you like me to provide the **database relationship diagram (ERD)** next — showing how all these models connect (User → Profile → Projects, etc.)?
