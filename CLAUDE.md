# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`employee_management` is a Django-based HRMS/ERP portfolio project (Employee Management System). Django 6.0.7, PostgreSQL, Django Templates + Bootstrap 5, Class-Based Views throughout. This is a from-scratch learning/portfolio project — code quality and idiomatic Django architecture matter more than shipping speed. See the working agreement below.

## Commands

Virtualenv lives at `my_env/`. There is no `requirements.txt` yet — installed packages are Django, psycopg2 (Postgres driver), Pillow (for `ImageField`); install/freeze manually until one exists.

```bash
# activate venv (from project root)
my_env/Scripts/activate          # Windows
source my_env/bin/activate       # Unix

# run dev server
python manage.py runserver

# migrations
python manage.py makemigrations
python manage.py makemigrations <app_name>   # scope to one app
python manage.py migrate

# check for config/import errors without hitting the DB
python manage.py check

# create an admin user
python manage.py createsuperuser

# tests (no tests written yet; each app has an empty tests.py stub)
python manage.py test
python manage.py test <app_name>
```

Database: PostgreSQL, configured directly in `employee_management/settings.py` (`DATABASES`) — not yet environment-variable driven (see Known gaps).

## Architecture

### App layout

One Django app per domain area, all registered in `employee_management/settings.py: INSTALLED_APPS`:

- **`core`** — the application shell: authentication (login/logout) and the dashboard. Owns the shared `base.html` layout (navbar + responsive sidebar) and `core/static/core/`. Nothing else should own layout/auth — new modules plug into this shell rather than growing their own.
- **`master`** — shared lookup/reference data referenced by other apps: `Department`, `DesignationCategory`, `Designation`, `Gender`, `SalaryMode`, `Bank`, `Allowance`, `Deduction`, `Shift`, `Country`, `State`, `City`. All inherit an abstract `BaseMaster` (`is_active`, `created_at`, `updated_at`) — any new master/lookup model should extend `BaseMaster` too, for the free active/inactive toggle and audit timestamps. Has CRUD templates scaffolded (`master/templates/master/{index,list,form,confirm_delete,base}.html`, `templatetags/master_extras.py`) but `views.py`/`urls.py` are not wired up yet.
- **`employee`** — the `Employee` model itself, FKs into several `master` models (department, designation, gender, salary mode, bank).
- **`attendance`** — `DutyRoster` and `Attendance`, both FK into `master.Shift`.
- **`holiday`** — `Holiday`, FKs into `master.Shift` (imported indirectly via `attendance.models` — should really import from `master.models` directly; see Known gaps).
- **`leave`** — `LeaveType`, `leaveBalance`, `LeaveRequest`.
- **`salary`** — `EmployeeAllowance`, `EmployeeDeduction`, both FK into `master.Allowance`/`master.Deduction`.

Dependency direction is one-way: `master` has no knowledge of the other apps; `employee`, `attendance`, `holiday`, `leave`, `salary` all depend on `master` (and increasingly on `employee`). Keep new FKs flowing in that direction — don't have `master` import from a domain app.

None of the domain models are registered in Django admin yet (`admin.py` in every app is still the default stub).

### Authentication & layout (`core` app)

- Auth uses Django's built-in `User` model directly — `Employee` is **not** linked to `User`. There's no login-to-employee-profile connection yet; that's an open design decision for whenever a feature needs "show me my own employee record."
- `CustomLoginView` (subclasses `django.contrib.auth.views.LoginView`) adds real "Remember Me" behavior: unchecking it calls `request.session.set_expiry(0)`.
- `settings.py` auth wiring: `LOGIN_URL='core:login'`, `LOGIN_REDIRECT_URL='core:dashboard'`, `LOGOUT_REDIRECT_URL='core:login'`. All URL names in this project are namespaced per-app (`core:dashboard`, `master:list`, etc.) — follow that convention for new apps' `urls.py` (`app_name = '<app>'`).
- `core/templates/base.html` is the shared shell (navbar, sidebar via `core/_sidebar_nav.html` partial reused for both the desktop `<aside>` and the mobile Bootstrap offcanvas). New feature pages should `{% extends 'base.html' %}` and fill `content`/`breadcrumb` blocks.
- The login page (`core/templates/registration/login.html`) deliberately does **not** extend `base.html` — auth screens use their own minimal centered-card layout, no sidebar/navbar.
- Sidebar links for not-yet-built modules (Master submenu items, Employee, Attendance, Holiday, Leave, Salary, Reports, Settings) are intentionally `href="#"` placeholders — wire them up as each module gets real views/urls.

### Master-data CRUD (planned, not yet built)

`master/templates/` already has generic list/form/confirm_delete templates expecting a URL structure keyed by a `master_slug` (e.g. `master:list <slug>`, `master:add <slug>`, context vars `master_label`, `master_singular`, `display_fields`, `object_list`). When building `master/views.py`, the intended approach (given ~12 structurally similar master models) is a small slug→model registry plus generic CBVs driven by it, rather than one CRUD view set per model — avoids ~12x boilerplate.

## Working agreement

Act as a senior Django reviewer, not just a code generator:
- Class-Based Views unless there's a strong reason otherwise; PEP 8; modular/reusable code.
- Explain non-trivial design decisions; flag a better approach if one exists instead of silently complying.
- Avoid speculative abstractions — build for what's asked, not hypothetical future needs.
- Bootstrap 5 for frontend, PostgreSQL as the database, responsive/professional HRMS look.
- Build the application foundation (auth, layout, dashboard) before feature-module CRUD, even if that module's templates/scaffolding already exist — confirm sequencing rather than assuming "next file to fill in" is next priority.

## Known gaps / punch list

Not urgent, but raise/fix as work reaches these areas — don't silently fix all of these unprompted:

- `settings.py` has a hardcoded `SECRET_KEY` and Postgres credentials (`postgres`/`postgres`), `DEBUG=True`, empty `ALLOWED_HOSTS`. Needs environment-based config (e.g. `django-environ`) before this is ever pushed to a public repo.
- No `requirements.txt`, `.gitignore`, or `.env` yet, and the project isn't a git repo yet.
- No `MEDIA_URL`/`MEDIA_ROOT` configured despite `Employee.photo` being an `ImageField`.
- `holiday/models.py` imports `Shift` via `from attendance.models import Shift` instead of `from master.models import Shift` directly — works, but is a misleading indirection.
- `leave/models.py` has a class named `leaveBalance` — should be `LeaveBalance` per PEP 8.
- `Employee` model has no `Meta` (ordering/verbose_name) and no format validators on `phone_number`/`aadhar_number`/`pan_number`, inconsistent with `master`'s `BaseMaster` convention.
- No decision yet on whether/how `Employee` should link to Django's `User` model for login.
