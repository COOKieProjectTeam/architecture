# COOKie GitHub Organization Structure

> **Organization**: `COOKieProjectTeam`
> **Purpose**: Separate concerns, enable collaboration, maintain clean architecture

---

## 📦 Repository Overview

### 1. `architecture` (THIS REPO)

**Purpose**: Central documentation and architecture hub

**Contains**:
- ✅ Technical architecture specifications
- ✅ Requirements documentation
- ✅ Business and market analysis
- ✅ PlantUML diagrams
- ✅ Project planning and backlog
- ✅ File organization guides
- ❌ NO CODE

**Tech**: Markdown, PlantUML

**Access**: Public (after MVP launch) or Private (during development)

**Team**: All developers (read), Architect (write)

---

### 2. `cookie-frontend`

**Purpose**: Web application (user-facing)

**Contains**:
- Next.js 14 application
- React components
- TailwindCSS styles
- Zustand state management
- API integration layer

**Tech**: TypeScript, Next.js 14, TailwindCSS, Zustand

**Structure**:
```
cookie-frontend/
├── src/
│   ├── app/              Next.js 14 app router
│   ├── components/       Reusable React components
│   ├── lib/              Utilities and helpers
│   ├── stores/           Zustand stores
│   └── types/            TypeScript types
├── public/               Static assets
├── .env.example          Environment variables template
├── README.md             Setup and development guide
└── package.json
```

**Access**: Private (until launch)

**Team**: Frontend developers, Full-stack developers

---

### 3. `cookie-backend`

**Purpose**: API server and business logic

**Contains**:
- ASP.NET Core 8 application
- RESTful API endpoints
- Entity Framework Core
- Authentication logic (JWT + OAuth)
- Business logic services

**Tech**: C#, ASP.NET Core 8, Entity Framework Core, PostgreSQL, Redis

**Structure**:
```
cookie-backend/
├── src/
│   ├── Controllers/
│   │   ├── RecipeController.cs   Recipe CRUD, search, filters
│   │   ├── UserController.cs     User management, auth
│   │   ├── RatingController.cs   Rating system
│   │   ├── FavoriteController.cs Favorites management
│   │   └── AdminController.cs    Admin panel APIs
│   ├── Models/               Entity models
│   ├── Services/             Business logic services
│   ├── Data/                 DbContext and migrations
│   ├── DTOs/                 Data transfer objects
│   └── Program.cs            Application entry point
├── .env.example              Environment variables template
├── README.md                 API documentation
└── COOKieBackend.csproj
```

**Access**: Private

**Team**: Backend developers, Full-stack developers

---

### 4. `cookie-infrastructure`

**Purpose**: DevOps configurations and deployment scripts

**Contains**:
- Docker configurations
- Terraform scripts (Yandex Cloud)
- GitHub Actions workflows
- Environment setup scripts
- Deployment guides

**Tech**: Docker, Terraform, Bash, YAML

**Structure**:
```
cookie-infrastructure/
├── docker/
│   ├── frontend/         Dockerfile for Next.js
│   ├── backend/          Dockerfile for ASP.NET Core
│   └── docker-compose.yml Development environment
├── terraform/
│   ├── modules/          Reusable Terraform modules
│   ├── environments/
│   │   ├── dev/          Development environment
│   │   ├── staging/      Staging environment
│   │   └── production/   Production environment
│   └── README.md         Terraform guide
├── github-actions/
│   └── workflows/        Reusable workflows
├── scripts/
│   ├── setup.sh          Local setup script
│   └── deploy.sh         Deployment script
└── README.md             Infrastructure overview
```

**Access**: Private

**Team**: DevOps, Architect, Full-stack developers

---

### 5. `cookie-recipes-data`

**Purpose**: Recipe datasets and data migrations

**Contains**:
- LLM-generated recipe data (JSON/CSV)
- Data validation scripts
- Import/export tools
- Recipe images (or links to storage)
- Data documentation

**Tech**: JSON, CSV, Python/Node.js scripts

**Structure**:
```
cookie-recipes-data/
├── recipes/
│   ├── breakfast/        JSON files for breakfast recipes
│   ├── lunch/            JSON files for lunch recipes
│   ├── dinner/           JSON files for dinner recipes
│   └── desserts/         JSON files for dessert recipes
├── images/               Recipe images (or .gitignore if using external storage)
├── scripts/
│   ├── validate.js       Validate recipe data
│   ├── import.js         Import to database
│   └── generate.js       LLM generation helper
├── templates/
│   └── recipe-template.json Recipe data format
└── README.md             Data format documentation
```

**Access**: Private

**Team**: Content creators, Data team, Developers

---

## 🔄 Repository Relationships

```
┌──────────────────────────────────────────────────┐
│           architecture (docs only)               │
│  - Defines specs, requirements, diagrams         │
│  - Referenced by all other repos                 │
└───────────────────┬──────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
┌──────────────┐        ┌──────────────┐
│   frontend   │◄──────►│   backend    │
│  (Next.js)   │  API   │  (ASP.NET)   │
└──────┬───────┘        └───────┬──────┘
       │                        │
       │                        │
       ▼                        ▼
┌──────────────────────────────────┐
│      cookie-infrastructure       │
│   (Deploys frontend + backend)   │
└──────────────┬───────────────────┘
               │
               ▼
      ┌────────────────┐
      │ recipes-data   │
      │ (Imported to   │
      │  backend DB)   │
      └────────────────┘
```

---

## 🔐 Access Control

### Repository Visibility

| Repository | Visibility | Reason |
|------------|-----------|--------|
| architecture | Private → Public (after MVP) | Contains business strategy initially |
| cookie-frontend | Private | Contains proprietary UI/UX |
| cookie-backend | Private | Contains business logic and secrets |
| cookie-infrastructure | Private | Contains deployment configs |
| cookie-recipes-data | Private | Proprietary recipe database |

**Post-MVP**: Consider open-sourcing `architecture` repo to demonstrate technical expertise

---

### Team Permissions

| Team | architecture | frontend | backend | infrastructure | recipes-data |
|------|--------------|----------|---------|----------------|--------------|
| **Solo Dev** (You) | Admin | Admin | Admin | Admin | Admin |
| **Frontend Devs** | Read | Write | Read | Read | Read |
| **Backend Devs** | Read | Read | Write | Read | Write |
| **DevOps** | Read | Read | Read | Write | Read |
| **Content Team** | Read | - | - | - | Write |
| **Investors** | Read | - | - | - | - |

---

## 📝 Workflow Examples

### Adding a New Feature

1. **Document first** (`architecture`):
   - Update [PROJECT_BACKLOG.md](docs/planning/PROJECT_BACKLOG.md)
   - Add requirement to [COOKie-requirements-v1.md](docs/requirements/COOKie-requirements-v1.md)
   - Update diagrams if needed

2. **Implement backend** (`cookie-backend`):
   - Create feature branch
   - Implement API endpoints
   - Add tests
   - Update backend README
   - Reference architecture docs in PR

3. **Implement frontend** (`cookie-frontend`):
   - Create feature branch
   - Implement UI components
   - Integrate with backend API
   - Update frontend README
   - Reference architecture docs in PR

4. **Deploy** (`cookie-infrastructure`):
   - Update deployment scripts if needed
   - Deploy to staging → production
   - Monitor

5. **Update docs** (`architecture`):
   - Mark task as completed in backlog
   - Update architecture if changes made

---

### Updating Architecture

1. **Create issue** in `architecture` repo
2. **Discuss** with team (if applicable)
3. **Update docs** (specs, diagrams)
4. **Create PR** with clear description
5. **Review** and approve
6. **Merge** to main
7. **Communicate** changes to development teams
8. **Reference** updated docs in code repo PRs

---

## 🚀 Setup Guide

### Initial Organization Setup

1. **Create GitHub Organization**: `@COOKAITeam` ✅

2. **Create repositories** (in order):
   ```bash
   # 1. Architecture (this repo)
   git remote add origin git@github.com:COOKAITeam/architecture.git

   # 2. Other repos (created)
   # git@github.com:COOKAITeam/cookie-frontend.git
   # git@github.com:COOKAITeam/cookie-backend.git
   # git@github.com:COOKAITeam/cookie-infrastructure.git
   # git@github.com:COOKAITeam/recipes-data.git
   ```

3. **Set up repository settings**:
   - Enable branch protection on `main`
   - Require pull request reviews
   - Enable status checks (if CI configured)
   - Configure GitHub Pages (for architecture docs, optional)

4. **Configure secrets** (per repository):
   - Database credentials
   - API keys
   - Deployment tokens

5. **Set up GitHub Actions** (per repository):
   - Linting and testing workflows
   - Deployment workflows
   - Documentation generation (for architecture)

---

### Cloning All Repositories

```bash
# Create organization folder
mkdir cookie-project
cd cookie-project

# Clone all repos
git clone git@github.com:COOKAITeam/architecture.git
git clone git@github.com:COOKAITeam/cookie-frontend.git
git clone git@github.com:COOKAITeam/cookie-backend.git
git clone git@github.com:COOKAITeam/cookie-infrastructure.git
git clone git@github.com:COOKAITeam/recipes-data.git

# Your project structure
cookie-project/
├── architecture/           (this repo)
├── cookie-frontend/
├── cookie-backend/
├── cookie-infrastructure/
└── recipes-data/
```

---

## 📚 Documentation Cross-References

Each code repository should reference architecture docs:

### In Frontend README.md
```markdown
## Architecture

See [COOKie Architecture](https://github.com/COOKAITeam/architecture) for:
- System architecture
- API contracts
- Requirements
```

### In Backend README.md
```markdown
## Architecture

See [COOKie Architecture](https://github.com/COOKAITeam/architecture) for:
- Database schema
- API specifications
- Business requirements
```

---

## 🔄 Keeping Repositories in Sync

### When Architecture Changes

1. Update `architecture` repo first
2. Create issues in affected code repos:
   - Link to architecture PR/commit
   - Describe required code changes
3. Implement changes in code repos
4. Reference architecture docs in code PRs

### Version Alignment

Consider tagging releases:
```bash
# In architecture repo
git tag -a v1.0.0-mvp -m "MVP Launch"
git push origin v1.0.0-mvp

# In code repos (after implementing MVP specs)
git tag -a v1.0.0 -m "MVP Release"
git push origin v1.0.0
```

---

## 📞 Questions?

- **Organization setup**: Create issue in `architecture` repo
- **Repository structure**: See this document
- **Access permissions**: Contact repository admin

---

**Organization**: `@COOKAITeam` ✅
**Repositories**: 5 (architecture + 4 code repos) ✅
**Status**: 🟢 Organization created, architecture ready for development

**Last Updated**: 2025-10-14
