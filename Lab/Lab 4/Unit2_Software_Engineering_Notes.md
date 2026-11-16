# Software Engineering – Unit 2: Complete Exam Notes
*(Project Management, Architecture, Design, Quality — MCQ-ready)*

---

## SECTION A: PROJECT MANAGEMENT

### 1. Basics
- **Project**: temporary effort to create value through a unique product/service/result. Has a beginning, end, team, budget, schedule, expectations.
- **Project Management**: use of knowledge, skills, tools, techniques to deliver value.
- **Software Project Management**: art + science of planning and leading software projects (sub-discipline of PM); projects are planned, implemented, monitored, controlled.

### 2. Roles of a Software Project Manager
- Defines requirements, builds team, lays out project blueprint (scope + parameters), communicates goals, allocates budget, ensures stakeholder expectations are met.
- **Three key roles**:
  1. **Leader** – gives direction, explains roles, builds a skill-diverse team.
  2. **Liaison** – link between clients, team, and upper management; transfers info both ways.
  3. **Mentor** – guides team, ensures cohesion, gives advice.

### 3. Project Management Triangle (Triple Constraint)
- Balances **Scope, Cost (Budget), Time (Schedule)** to maintain quality.
- No single variable can change without trade-offs on the other two.

### 4. Agile Planning
- Iterative approach — software delivered to customers in **increments**; functionality of increments decided **during** development (not fully pre-planned), based on progress & customer priority.
- **Release planning**: months-ahead outlook; decides features for a release.
- **Iteration planning**: short-term (typically **2–4 weeks**); plans next increment.

**Approaches to Agile Planning:**
- **Planning in Scrum** – managing a **project backlog**, daily progress reviews.
- **Planning Game** – originally part of **Extreme Programming (XP)**; based on **user stories**.

**Story-based Planning (Planning Game):**
- Team discusses user stories, ranks by implementation time/effort.
- Stories assigned **effort points** (size/difficulty).
- **Velocity** = effort points completed per day/iteration → used to estimate total effort.

**Release & Iteration Planning:**
- Release planning selects/refines stories & implementation order.
- Iteration usually **2–3 weeks**; velocity guides how many stories fit.

**Task Allocation:**
- Developers break stories into tasks; each task = **4–16 hours**.
- Developers **sign up** for tasks → sense of ownership, motivation.

**Software Delivery:**
- Increment delivered at the end of **every iteration**.
- If features can't be completed in time → **scope is reduced**, NOT the schedule extended (delivery date is fixed).

**Agile Planning – Difficulties & Applicability:**
- Difficulty: relies on **customer availability**; customers used to traditional plans may struggle.
- Works well: **small, stable, co-located teams**.
- Doesn't work well: large/distributed teams or frequent membership change.

### 5. Time Estimation — WBS & COCOMO
- **WBS (Work Breakdown Structure)**: description of the work to be done for a project.
- **COCOMO (Constructive Cost Model)**: regression model based on **LoC (Lines of Code)**; procedural cost-estimation model predicting **size, effort, cost, time, quality**.
  - **Effort**: labor required, measured in **person-months**.
  - **Schedule**: time required, measured in weeks/months.

**Three Project Categories (COCOMO):**
| Type | Description | Example |
|---|---|---|
| **Organic** | small team, well-understood problem, nominal experience | Inventory Management System |
| **Semi-detached** | in between organic & embedded | OS, DBMS |
| **Embedded** | highest complexity/creativity/experience, larger team | ATM software |

**Three COCOMO Models**: Basic, Intermediate, Detailed.

**Basic Model Formulas:**
```
Effort (E) = a × (KLOC)^b
Time      = c × (Effort)^d
People required = Effort / Time
```
| Project | a | b | c | d |
|---|---|---|---|---|
| Organic | 2.4 | 1.05 | 2.5 | 0.38 |
| Semi-detached | 3.0 | 1.12 | 2.5 | 0.35 |
| Embedded | 3.6 | 1.20 | 2.5 | 0.32 |

*(Memory tip: values increase from Organic → Embedded for a, b, d roughly; c is constant at 2.5)*

### 6. Project Scheduling
- Distributes estimated effort across planned duration by allocating effort to tasks; **evolves over time** (macroscopic schedule early → refined detailed schedule later).
- **Two scheduling perspectives**: (1) fixed end date, effort distributed within it (most common), (2) rough bounds discussed, end date set by engineering org after analysis.
- **7 Basic Principles of Scheduling**:
  1. Compartmentalization
  2. Interdependency
  3. Time allocation
  4. Effort validation
  5. Defined responsibilities
  6. Defined outcomes
  7. Defined milestones

### 7. Risk Management
- Concerned with identifying risks and minimizing their effect on a project.
- Important because of uncertainty: loosely-defined requirements, requirement changes, estimation difficulty, differing skills.

**Risk Classification — Two Dimensions:**
- By **type**: technical, organizational, etc.
- By **what's affected**:
  - **Project risks** → affect schedule/resources
  - **Product risks** → affect quality/performance of software
  - **Business risks** → affect the organization developing/procuring software

**Example risks (memorize a few):**
| Risk | Affects |
|---|---|
| Staff turnover | Project |
| Management change | Project |
| Hardware unavailability | Project |
| Requirements change | Project & Product |
| Specification delays | Project & Product |
| Size underestimate | Project & Product |
| CASE tool underperformance | Product |
| Technology change | Business |
| Product competition | Business |

**Risk Management Process (4 steps, sequential/cyclic):**
1. **Risk identification** – identify project, product, business risks
2. **Risk analysis** – assess likelihood & consequences
3. **Risk planning** – draw up avoidance/mitigation plans
4. **Risk monitoring** – monitor risks throughout project

**Risk Indicators (type → sign):**
- Estimation → missed schedules, unresolved defects
- Organizational → gossip, inaction by management
- People → poor morale, poor relationships, high turnover
- Requirements → many change requests, complaints
- Technology → late hardware delivery, tech problems
- Tools → reluctance to use tools, complaints

### 8. Quality Management — RACI Matrix
- **RACI chart**: responsibility assignment matrix listing stakeholders & involvement per task.
- **R** – Responsible: "the doer"; can be multiple.
- **A** – Accountable: "buck stops here"; has yes/no veto power; **only ONE "A" per task**.
- **C** – Consulted: two-way communication, consulted before action.
- **I** – Informed: one-way communication, informed after decision/action.

### 9. Outcomes & Contents of Project Planning
**Outcomes of Project Planning**: Project Plan, WBS, Schedule, Resource Management, Communication/Metrics Plans, Risk Management Plan, Roles.

**Contents of a Project Plan**: Introduction, Deliverables, Process model, Organization, Standards/guidelines, Management activities, Risks, Staffing, Methods/techniques, Quality criteria, Work packages, Resources, Budget & schedule, Change control process, Delivery means.

### 10. Project Monitoring and Control
- Observes project execution to identify potential problems early and take corrective action.
- Involves decisions/adjustments in **time, cost, organization structure, scope**.
- Includes: monitoring project work (Critical Path Analysis periodically), ensuring change control is followed, keeping scope/deliverables updated, controlling the quality triangle, managing team/performance/communication.

### 11. Gantt Chart
- Shows **activities (tasks) vs time**; bar length/position = start date, duration, end date.
- Shows: what activities are, when they begin/end, duration, overlaps, whole-project start/end.
- **Critical Path**: longest sequence of dependent tasks that must complete on time for the project to finish on time; a delay here delays the whole project.
- Activities with **total slack = 0** are on the critical path.
- **Jira** – common PM tool for bug/issue tracking & project management.

### 12. Teamwork
- Most software engineering is a **group activity** (non-trivial projects need multiple people).
- Good group = **cohesive**, has team spirit; motivated by group success + personal goals.
- **Group cohesiveness advantages**: shared quality standards, mutual learning, reduced ignorance-based inhibition, shared knowledge & continuity if a member leaves, encourages refactoring/collective improvement.
- **Effectiveness of a team depends on**: the people (diverse skill mix), group organization, technical & managerial communication.

---

## SECTION B: SOFTWARE ARCHITECTURE

### 13. Views & Abstraction
- **Abstracted views**: convey specific info, have a well-defined purpose, show only necessary details, hide unnecessary details, use legends/annotations, multiple views tell a larger story.

### 14. Case Study – Therac-25 (KEY case study, likely MCQs)
- Computer-controlled radiation therapy machine; software replaced **hardware safety interlocks** present in earlier models (Therac-6, Therac-20).
- **What went wrong**:
  - **Race conditions** – rapid setting changes caused misconfiguration (high-dose beam without proper setup).
  - **Integer overflow** – a flag variable overflowed (255 → 0), tricking system into thinking it was safe.
  - **Removal of hardware interlocks** – software-only safety, made bugs lethal.
  - **Operator overconfidence** – cryptic errors (e.g., "Malfunction 54") ignored/bypassed.
  - **Inadequate testing** – software/UI testing insufficient; risk underestimated.
- **Architectural failures**: tight coupling (UI/control/machine shared global memory), no fault isolation, no logging/diagnostics, legacy code reused without redesign.
- **Principles violated**: no separation of concerns, no fail-safe layers, reuse without redesign, no defensive programming/redundancy.
- **Impact**: at least 6 incidents, injuries & deaths; led to standards like **IEC 62304** (medical device software safety).
- **Lesson**: safety-critical systems need modular/layered architecture, software interlocks, defensive programming, redundancy, thorough V&V.

### 15. Software Architecture — Definition & Importance
- **Definition**: top-level decomposition of a system into major components + how they interact.
- Used for: stakeholder communication, blueprint, negotiation, balancing functional & non-functional (quality) goals.
- **Motivation**: internal/external communication, documents design decisions & constraints, relates to org structure, enables/precludes NFRs, controls complexity, manages change, aids effort estimation.
- Every system **has** an architecture whether documented or not — if not consciously designed, it evolves by itself.

### 16. Design vs Architecture
| Level | Question type |
|---|---|
| **Requirements** | high-level "what" |
| **Architecture** (high-level design) | high-level "how", mid-level "what" |
| **Design** (low-level design, e.g. design patterns) | mid-level "how", low-level "what" |
| **Code** | low-level "how" |

- Design Q example: "How do I add a menu item?" → Architecture Q example: "How do I extend the app with a plugin?" / "What threads exist and how do they coordinate?"

### 17. Common Software Architectural Patterns/Styles
| Pattern | Key Idea | Example |
|---|---|---|
| **Pipes & Filters** | Data flows through sequence of filters via pipes; filters don't share state; no cycles | Compilers |
| **Object-Oriented** | Collection of interacting objects (state+behavior); encapsulation, inheritance, polymorphism | Adobe Photoshop |
| **Event-Driven** | Components communicate via events (pub/sub); async, loose coupling | Node.js |
| **Blackboard** | Subsystems interact via shared knowledge base; control component decides which acts when | Stock exchange |
| **Layered** | Hierarchical layers; each interacts only with adjacent layers; easy to swap layers | Internet Protocol Suite (TCP/IP) |
| **Client-Server** | Clients request, servers process/respond; centralized control | Online banking |
| **Microservices** | Independent, deployable services | Amazon, Netflix, Uber |

- **Architectural style vs pattern**: a pattern = solution to a problem; a style = more general, doesn't need a specific problem (defines a *family* of systems, vocabulary of components/connectors).

**Which pattern for which system? (Common MCQ)**
- Weather App → **Pipe & Filter** (sequential data transform)
- Email Service → **Client-Server**
- Online Banking → **Layered** (strict separation, security/audit)
- Multi-faceted Store (Amazon) → **Microservices**

### 18. Architecture Considerations
- **Level of Abstraction**: components + interconnections (APIs).
- **Separation of Concerns**: high cohesion (within component) + low coupling (between components).
- **Modularity**: decomposable/composable, localizes changes, limits error spread.

**Cohesion** (how related operations within a module are — **high cohesion = good**):
- Clear purpose/scope, strong internal relationships, good abstraction.

**7 Levels of Cohesion (weakest → strongest)** — classic MCQ list:
1. **Coincidental** – no relation, grouped haphazardly.
2. **Logical** – tasks logically related but don't call each other (e.g., all input routines together).
3. **Temporal** – activated at same time (e.g., initialization module).
4. **Procedural** – elements executed in a given order.
5. **Communicational** – elements operate on same data.
6. **Sequential** – output of one element = input of next.
7. **Functional** – all elements contribute to ONE single function (strongest, best).

*(Quick recall: "input routines" = Logical; "initialization" = Temporal; "read & print" = Procedural)*

**Coupling** (interconnection between modules — **loose coupling = good**):
Tightest → loosest:
1. **Content coupling** – one module directly changes another's data/control (avoid always).
2. **Common coupling** – shared global data (like FORTRAN COMMON blocks / global variables).
3. **External coupling** – communicate via external medium (e.g., a file).
4. **Control coupling** – one module controls another via passed flags.
5. **Stamp coupling** – whole data structures passed between modules.
6. **Data coupling** – only simple/primitive data passed (loosest, best).

**Cohesion/Coupling example**: Low cohesion = everything jammed into one class. High cohesion = operations delegated to dedicated services. Loosely coupled = few structured dependencies. Tightly coupled = "spaghetti" point-to-point dependencies with high ripple effect.

### 19. Model-View-Controller (MVC)
- **Model** – app data & core functionality.
- **View** – presents data / UI.
- **Controller** – handles control flow, mediates between View and Model.

### 20. Documenting Architecture
- Purpose: blueprint, early-analysis artifact, carrier of quality attributes, key to maintenance, supports traceability.
- Notation guidelines: suitable for purpose, usually visual (boxes/arrows), UML possible but may constrain, correct abstraction level (subsystems not classes), always include a legend, one view per page, use hierarchy.

### 21. Security Design and Architecture
- Purpose: embed security principles into architecture to mitigate design-level vulnerabilities.
- Goals: reduce attack surface, separation of concerns, defense-in-depth, align with threat models.
- **Trust boundary**: components within same boundary are "mutually trusted"; consider assets at **origin, in transit, at rest, in use**.
- Techniques: input validation layers, secure channels (TLS/mTLS), encapsulation/service boundaries, subsystem trust boundaries.
- Review checkpoints: sensitive components isolated? APIs authenticated/rate-limited? encryption in transit/rest? secure default configs?
- Outputs: updated architecture diagrams (with trust boundaries), Security Architecture Review Report, Change Requests, Architecture Threat Map.

### 22. Microservices
- A set of independently deployable services working together via **APIs**; e.g., Amazon, Netflix, Uber.
- **Reasons to break up a monolith**: faster deployment, independent update frequency, different scaling needs/tech, codebase too big/complex, scalability, security targeting, better org alignment.
- **Why Netflix can't use monolith**: needs to handle varying computational demand, scale to millions of users, fault tolerance, rapid feature rollout.

**Two patterns to migrate monolith → microservices:**
1. **Strangler Pattern**: new services built as microservices; a **facade/gateway** routes requests; over time more functionality migrates until legacy system is fully "strangled"/retired.
2. **Anti-Corruption Layer Pattern**: similar to Strangler, but used when new services must talk to the legacy app; a translation layer (facade/adapter) maps between domains so new services aren't "corrupted" by old concepts (protocol/schema translation).

**Challenges of Microservices** (know categories):
- Increased operational complexity (many deployment pipelines)
- Inter-service communication reliability (retries, "retry storms")
- Data consistency across distributed services (**Saga pattern** + compensating transactions)
- Testing/debugging difficulty (mocking dependent services)
- Governance/standardization gaps (e.g., camelCase vs snake_case)
- DevOps/infrastructure overhead (per-service pipelines)
- Team/org coordination challenges
- Versioning & backward compatibility issues
- Security & compliance across services (e.g., HIPAA)

### 23. Component Diagrams (UML)
- **Component**: replaceable, executable piece of a system; implementation hidden. Characteristics: modular, replaceable, black box, executable.
- **Notation**: rectangle with `<<component>>` stereotype.
- **Provided Interface** – "lollipop" notation (what it offers).
- **Required Interface** – "socket" notation (what it needs).
- **Assembly connector** – connects provided & required interfaces.
- **Port**: interaction point between classifier & external environment; small square on boundary; on boundary = public; inside = protected/private.
- **Usage Dependency**: dashed arrow with `<<use>>`; arrow points from client (dependent) to supplier.
- **Subsystem**: decomposition unit for large systems; cannot be instantiated at runtime (but contents can be initialized).
- **Why use Component Diagrams**: show structure/organization, model subsystems, aid testing, visualize connections.

---

## SECTION C: SOFTWARE DESIGN

### 24. Levels of Abstraction (repeat, exam favorite)
Requirements (what) → Architecture (high-level how / mid-level what) → Design (mid-level how / low-level what, e.g. design patterns) → Code (low-level how).

### 25. Software Design Principles
- Further decomposition of components post-architecture.
- Describes component/subsystem behavior.
- Describes interface realization (algorithms & data structures).
- Describes UI interaction.
- Uses structural/behavioral design patterns; considers maintenance & reuse.

### 26. Techniques that Enable Design
- **Abstraction** – focus on essential properties.
- **Modularity** – degree to which a system can be decomposed.
- **Information Hiding**:
  - **Encapsulation** – hides data, access only via specific functions.
  - **Separation of interface and implementation** – public interface known to clients; internal details hidden.
- **Limiting Complexity** – intra-modular or inter-modular; higher complexity = worse design.
- **Hierarchical structure** – views system as hierarchy.

### 27. Key Design Issues
Concurrency, Non-functional requirements, Data persistence, Event handling (callbacks), Error/Exception handling & fault tolerance, Distribution of components, Interaction & Presentation.

### 28. Design Methods
- **Booch methodology** – object-oriented software development method.
- **Fusion** – systematic OO development method (developed at HP Labs, Bristol).
- **DFD (Data Flow Diagrams)** – developed by Yourdon & Constantine (early 1970s); 2-step process:
  1. **Structured Analysis (SA)** → logical design as data flow diagrams.
  2. **Structured Design (SD)** → transforms logical design into program structure (structure charts).
  - DFDs have levels showing varying detail.

### 29. UML (Unified Modeling Language)
- Developed mid-1990s; standardized notation for modeling OO systems.
- Diagram types: **Use case, Component, Class/Object, Sequence, State chart**, etc.
- **Sequence Diagram**: models interactions between actors & objects for a use case; objects/actors listed along top with vertical dotted lifelines; interactions shown as annotated arrows.

---

## SECTION D: MODULARITY — API & ABI

### 30. Why API/ABI Matter
- **API** governs source-level interaction; **ABI** governs binary-level interoperability between compiled modules/libraries.
- Enable modular architecture (contracts between modules), independent/parallel development, cross-platform/cross-language interfacing.

### 31. API (Application Programming Interface)
- Formal contract specifying how components interact: functions, inputs, outputs, error codes, protocols.
- Acts as a boundary, hides complexity, allows parallel team work.
- **Benefits**: modularity/encapsulation, reusability/collaboration, maintainability (internal changes don't affect consumers if interface is stable).

**Key Aspects of Good API Design:**
- **Clarity** – descriptive names (e.g., `createUserProfile()` not `userOp()`).
- **Simplicity** – minimal surface area.
- **Error Handling** – standardized codes/messages (structured JSON with errorCode + message).
- **Versioning** – e.g., `/v1/users` vs `/v2/users`, semantic versioning.

**Achieving Modularity via API Design**: Loose coupling (depend on abstractions), High cohesion (related ops together, e.g., a `UserService` with CRUD), Information hiding, Extensibility (plugin/DI patterns).

### 32. Types of APIs
| Level | Description | Example |
|---|---|---|
| **Function/Library** | Static/dynamic libraries (.so files); linked at compile-time or load-time | POSIX `open()`, `read()`, `close()` |
| **IPC-level** | Message queues, shared memory, semaphores | POSIX shared memory (`shm_open`, `mmap`) |
| **Network/REST** | HTTP/HTTPS + JSON/XML; resource-based URLs | REST APIs, OpenAPI spec |

**Synchronous vs Asynchronous APIs:**
- **Synchronous**: caller **blocks/waits** until operation completes. E.g., Linux `read()`/`write()`, Python `requests.get()`.
- **Asynchronous**: caller continues immediately; response handled later (callbacks/promises/event loop). E.g., Node.js HTTP server, Python `asyncio`/`aiohttp`.
- Use **sync** when: simplicity needed, short-lived/internal ops.
- Use **async** when: high-latency/I/O-bound, scaling large apps, need responsiveness (GUI/real-time).

**API Standards:**
- **OpenAPI/Swagger** – contract-first; auto-generate client/server code.
- **gRPC & Protobuf** – define services/messages in `.proto` files; strongly-typed, binary format, high performance.

**Versioning & Compatibility:**
- **Backward compatibility** – newer versions accept older clients' requests.
- **Forward compatibility** – older versions ignore unknown fields from newer clients (Protobuf skips unknown tags).
- **Semantic Versioning** – `MAJOR.MINOR.PATCH`: MAJOR = incompatible change, MINOR = backward-compatible addition, PATCH = bug fix.

### 33. ABI (Application Binary Interface)
- Defines low-level details: calling conventions, data type sizes, symbol names — enables independently compiled binaries to interoperate.
- **Cannot change without breaking binary compatibility** (unlike APIs which are source-level contracts).
- Changing a struct layout or function signature without updating ABI → crashes/undefined behavior.

**Real-world ABI Breakage Examples:**
- **OpenSSL 1.1.0 (2016)** – changed internal structures, removed symbols.
- **Glibc SONAME bump** (e.g., libc.so.6 → libc.so.7) – old binaries fail to find the library.
- **LLVM/Clang** – symbol visibility/data layout changes broke plugins.

**Implications of ABI Breakage**: runtime failures (undefined symbol errors), security risks (mismatched layouts), maintenance burden (forced recompilation), ecosystem fragmentation ("dependency hell").

**Language Specifics:**
- APIs are universal (headers, module exports, IDLs differ by language).
- **Interpreted languages** (Python, JS) – no intrinsic ABI at source level; rely on FFI/runtime.
- **Compiled languages** (C/C++, Rust, Go, Java bytecode) – explicit, managed ABIs.

---

## SECTION E: ERROR HANDLING

### 34. Error Handling Basics
- Process of anticipating, detecting, and responding to runtime errors/exceptions so the program continues correctly or **fails gracefully**.
- Maintains stability, UX, security.

### 35. Defining Errors in API Contracts
- **Error Codes & Enums** – centralized, consistent error constants.
- **Structured Responses** – JSON with `code`, `message`, `details`.
- **Documentation** – meaning, range, recovery suggestions per code.

### 36. Error Propagation & Handling Patterns
- **Return Code Checks** – procedural languages; caller checks status codes.
- **Exception-Based Flow** – OO languages; throw/catch at defined boundaries.
- **Result/Option Types** – functional/modern languages (Rust `Result<T,E>`, Swift `Option<T>`) force explicit handling.
- **HTTP Status Codes** – REST APIs (200, 400, 500) + JSON error body.

### 37. Logging & Observability
- **Structured Logging** – JSON/key-value with timestamp, error_code, module, stack_trace.
- **Error Levels** – INFO, WARN, ERROR, FATAL.
- **Correlation IDs** – unique request/transaction IDs for end-to-end tracing.

### 38. Error Code Organization
- **Scoped Namespaces** – prefix by module (e.g., `AUTH_INVALID_TOKEN`).
- **Central Registry** – single source of truth for all codes.
- **Versioning** – deprecate codes gracefully, keep backward compatibility.

### 39. Best Practices
- **Fail Fast** – detect/report errors early (assertions, invariant checks).
- **Graceful Degradation** – degrade rather than crash (e.g., use cached data).
- **Consistent Strategy** – uniform error handling convention across codebase.
- **Automated Tests** – include negative/error-path test cases.

---

## SECTION F: USABILITY ENGINEERING

### 40. Usability Engineering — Definition
- Systematic process of designing & evaluating software interfaces to be easy to learn, efficient, satisfying; improves UX by aligning software with human needs.

### 41. Case Study — Hawaii False Missile Alert (illustrative example)
- Human error (wrong UI option selected during drill), no safeguard/confirmation separation between test & real modes, no quick cancellation mechanism, organizational/supervision gaps.
- Public reaction: fear/panic, "social milling" (verification-seeking behavior before acting).

### 42. Therac-25 (revisited in Usability context)
- Race conditions, integer overflow/flag bug, removed hardware interlocks, cryptic/bypassable error messages ("Malfunction 54"), inadequate testing — same failure covered under both Architecture and Usability lens (favorite exam case study — know it well).

### 43. Testing Usability
- Should NOT rely on: intuition, testing on yourself, copying other apps' UI, or waiting "until someone dies."
- **Test with actual users**: Can they figure it out? How long does it take? Do they need help? → **"Don't blame the user, blame the design."**

### 44. Dogfooding
- Team uses its **own product internally** before public release.
- Informal, real-world usage testing; catches usability/performance issues before users do; done pre-release/during internal beta; testers = developers, designers, PMs, support staff.

### 45. User Study Methods
- **Interviews & Surveys**
- **Shadowing** – "fly on the wall," observe users in natural setting; rich qualitative data but expensive, time-consuming, hard to access.
- **Lab Study** – controlled setting, full control over tasks, record participant/screen; metrics = task time, correctness, mistakes, opinions; watch for reactivity effects.
- **Field Study** – observe in real-world context.
- **A/B Testing** – compare two design variations; random assignment; needs many users for statistical significance; tells "which is better" but not "why."
- **Prototyping**:
  - **Mockups/Wireframes** – visual blueprints of UI.
  - **Paper Prototype** – hand-drawn sketches.
  - **Wizard of Oz** – users believe system is real/automated, but a human manually controls responses behind the scenes.

### 46. Aspects of Usability — mnemonic "LESEM"
- **L**earnability – can users (new & power) learn to use it correctly?
- **E**fficiency – how fast can users perform tasks correctly?
- **S**atisfaction
- **E**rrors – unlikely to occur? easy to recover? descriptive messages?
- **M**emorability

- **Design for errors**: unambiguous buttons, clear descriptions, no surprises, **every action should be revertible** (e.g., undo, recycle bin, reopen closed tab).

---

## SECTION G: SOFTWARE QUALITY

### 47. Case Study — Heartbleed (OpenSSL, CVE-2014-0160)
- **Cause**: TLS Heartbeat extension (RFC 6520) didn't validate that the claimed payload length matched actual payload → attacker could request large data while sending little, causing server to leak up to 64KB of memory (private keys, session tokens, PII).
- **Discovered**: April 7, 2014, by Neel Mehta (Google Security); patched in OpenSSL 1.0.1g.
- **Quality failures**: no formal code review, insufficient testing (no fuzzing/boundary tests), no formal release quality gates, poor documentation.
- **Fix approach**: defined quality framework (mandatory reviews, coverage thresholds), automated/fuzz testing in CI, documentation & traceability, periodic security audits.

### 48. Software Quality — Perspectives
- **Transcendent** – exceeds normal expectations.
- **User-based** – fitness for use.
- **Manufacturing-based** – conformance to specs.
- **Product-based** – based on measurable attributes.
- **Value-based** – balances time, cost, profits.

**Product Quality Perspectives (4 groups — exam favorite):**
1. **Product Operation**: Correctness, Reliability, Efficiency, Integrity, Usability, Functionality, Availability.
2. **Overall Environment**: Responsiveness, Predictability, Productivity, People (customer & employee satisfaction).
3. **Product Revision**: Maintainability, Testability, Flexibility.
4. **Product Transition**: Portability, Reusability, Interoperability.

**Quality Attributes — mnemonic "FLURPS+"**
- **F**unctionality, **L**ocalization, **U**sability, **R**eliability, **P**erformance, **S**upportability, **+** (Extensibility etc.)

### 49. Software Quality Terminology
- **Attribute** – measurable physical/abstract property of an entity.
- **Measure** – quantitative indication of extent/amount (e.g., number of errors).
- **Metric** – quantitative measure of the *degree* to which a system has an attribute; calculated between two measures (e.g., errors found per person-hour).
- **Why measure**: feedback, diagnostics, evaluating productivity, forecasting, supports estimating/budgeting/scheduling.

**Characteristics of good metrics**: Quantitative, Understandable, Applicable (at all SDLC stages), Repeatable, Economical, Language-independent.

### 50. Cost of Quality (COQ)
- Methodology determining how much resources go toward preventing poor quality, appraising quality, and internal/external failures.
- **COGQ (Cost of Good Quality)**: Prevention costs (training, quality planning) + Appraisal costs (inspections, testing, audits) + Management Control costs (contract reviews, gating criteria).
- **COPQ (Cost of Poor/Bad Quality)**: Internal failure costs (rework, scrap, delays) + External failure costs (support calls, patches) + Technical debt + Management failure costs (unplanned costs, customer damages).

### 51. Software Quality Assurance (SQA)
- Methods to monitor the software engineering process to ensure quality.
- Involves planning (goals, commitments, activities, measurements, verification).
- Encompasses: entire SDLC processes, oversight/record-keeping/reporting, auditing for compliance, ensuring deviations are recorded/reported.

**Contents of an SQA Plan**: Responsibility Management, Document Management & Control, Requirements Scope, Design Control, Development Control & Rigor, Testing & QA, Risks & Mitigation, Quality Audits, Defect Management, Training Requirements.

---

## SECTION H: TECHNICAL DEBT

### 52. Technical Debt — Definition
- "Design or implementation constructs that are expedient in the short term but set up a context that makes future change more costly or impossible" — a **contingent liability** affecting internal system qualities (mainly maintainability & evolvability).
- **Technical Debt ≠ Bad Internal Quality** (it's a deliberate/inadvertent trade-off, not necessarily "bad code").
- Analogy: like **pollution** — accumulates and affects the whole system over time.
- High internal quality = an **investment** (makes future feature addition easier).

### 53. Causes of Technical Debt
Tightly-coupled components, poorly-specified requirements, business pressure, lack of process, lack of documentation, lack of automated testing, lack of knowledge, lack of ownership, delayed refactoring, multiple long-lived branches.

### 54. Consequences of Too Much Technical Debt
Demoralizing to work with, awkward client conversations, team infighting, turnover/attrition, reduced development speed.

### 55. Managing Technical Debt
Continuous challenges: recognizing it, making it **visible**, deciding when/how to resolve, living with some of it (not all debt is equally urgent).

### 56. Common Anti-Patterns (that cause debt)
- No QA process (or nobody follows it).
- Bad version control practices – everyone commits to main, long-lived feature branches, huge PRs.
- Slow/encumbering QA processes – changes take forever to merge.
- Reliance on repetitive **manual** labor – focuses on superficial issues, inconsistent results, mistakes happen.

### 57. Case Study — Knight Capital (Aug 1, 2012)
- Financial services / high-frequency trading firm.
- **Deployment error**: new code deployed to only **7 of 8 servers**; the 8th ran outdated **2003 test-mode code**, sending erroneous stock orders.
- **Result**: lost **$460 million in 45 minutes** (company had only $365M cash) → near-bankruptcy.
- Lesson: importance of deployment discipline, consistency checks, and technical debt (leftover legacy flag/code) management.

---

## SECTION I: TEST-DRIVEN DEVELOPMENT (TDD)

### 58. TDD — Definition
- Approach where **testing and code development are interleaved**; tests written **before** code; passing tests drives development.
- Code developed incrementally with a test per increment; don't move to next increment until current tests pass.
- Originated in **Extreme Programming (XP)** / Agile, but usable in plan-driven processes too.

### 59. TDD Process (sequence — exam favorite)
1. Identify a small increment of required functionality.
2. Write an automated test for it.
3. Run the test (and all existing tests) — it **fails** initially (functionality not yet implemented).
4. Implement the functionality, re-run the test.
5. Once all tests pass, move to the next increment.

### 60. Benefits of TDD
- **Code coverage** – every code segment has ≥1 associated test.
- **Regression testing** – test suite builds up incrementally.
- **Simplified debugging** – failing test pinpoints the newly broken code.
- **System documentation** – tests describe what code should do.

---

## QUICK-FIRE REVISION TABLE (for last-minute MCQ scan)

| Term | One-line meaning |
|---|---|
| COCOMO | LoC-based effort/time/cost estimation model |
| Organic/Semi-detached/Embedded | 3 COCOMO project categories (simple → complex) |
| Velocity | Effort points completed per iteration (Agile) |
| RACI | Responsible, Accountable (only 1), Consulted, Informed |
| Critical Path | Longest task sequence; zero slack; determines project end date |
| Pipes & Filters | Sequential data transformation, no shared state |
| Blackboard | Shared knowledge base + control component |
| Strangler Pattern | Gradually replace monolith via gateway routing |
| Anti-Corruption Layer | Translation layer between legacy & new service domains |
| Cohesion (best→worst is reverse) | Functional > Sequential > Communicational > Procedural > Temporal > Logical > Coincidental |
| Coupling (best→worst) | Data > Stamp > Control > External > Common > Content |
| API | Source-level contract between components |
| ABI | Binary-level compatibility contract (calling conventions, struct layout) |
| Semantic Versioning | MAJOR.MINOR.PATCH |
| LESEM | Learnability, Efficiency, Satisfaction, Errors, Memorability |
| Dogfooding | Using your own product internally before release |
| Wizard of Oz | Fake automated system, human secretly controls responses |
| FLURPS+ | Functionality, Localization, Usability, Reliability, Performance, Supportability |
| COGQ / COPQ | Cost of Good Quality / Cost of Poor (Bad) Quality |
| Technical Debt | Shortcut today = costlier change tomorrow |
| Knight Capital | $460M lost in 45 min due to bad deployment (7/8 servers) |
| Heartbleed | OpenSSL memory-leak bug from unvalidated heartbeat payload length |
| Therac-25 | Radiation overdoses from race conditions + removed hardware interlocks |
| TDD | Write test → fail → implement → pass → repeat |
