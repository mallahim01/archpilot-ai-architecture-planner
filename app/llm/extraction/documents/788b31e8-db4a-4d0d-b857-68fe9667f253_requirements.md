# Requirements Document

**Job ID:** `788b31e8-db4a-4d0d-b857-68fe9667f253`


## Table of Contents
- Overview
- Goals and Success Criteria
- Scope
- Personas and Roles
- High-level User Journeys
- Functional Requirements
- Non-Functional Requirements
- Integrations and Data
- Constraints and Assumptions
- Open Questions


# Overview

The project aims to develop a web-only, comprehensive e-learning platform designed to serve three primary user roles: Admin, Student, and Instructor. Built on a robust tech stack featuring Next.js, NestJS, and Postgres, it will facilitate seamless course authoring, enrollment, and learning experiences while enabling monetization through subscriptions and a la carte purchases.

- **Product**:
  - Web-only e-learning platform
  - Features include subscription management, RBAC, course authoring, progress tracking, and instructor payouts

- **Target Users**:
  - **Admins**: Manage users, courses, subscriptions, payouts, enforce content policy
  - **Students**: Enroll in courses, track progress, earn certificates
  - **Instructors**: Create/manage courses, track student progress, view earnings

- **Core Value**:
  - Provides a user-friendly, scalable platform for e-learning with flexible monetization options
  - Supports both subscription models and individual course purchases

- **Non-goals**:
  - Mobile or offline access is not included in the MVP

**Open Questions**:
- Should subscriptions unlock all courses or only a specific catalog?


# Goals and Success Criteria

## Goals

- Develop a web-only MVP featuring vital elements such as subscriptions, RBAC, course authoring, progress tracking, and enrollment-based instructor payouts within a 4-month timeline.
- Implement a hybrid subscription model offering both monthly and annual platform-level access, alongside optional a la carte course purchases.
- Establish a primary tech stack using Next.js, NestJS, Postgres, Prisma, Clerk/Auth0, and Stripe Billing with web-first design principles.

## Success Metrics

- Successful deployment of a web-only MVP within the specified 4-month timeline.
- Achievement of a fully functioning subscription lifecycle management system and RBAC for Admin, Student, and Instructor roles by Month 1.
- Enablement of course creation and publishing, enrollment and progress tracking, and certificate issuance by Month 2.
- Completion of monetization components, including accurate instructor payout calculations and reporting capabilities, by Month 3.
- Attainment of production readiness with QA, security measures, and analytics by Month 4.

## Acceptance Criteria

- **Functional Requirements:**
  - Subscription system must support lifecycle events like trial, upgrade, cancel, and renew.
  - RBAC implemented for distinct roles: Admin, Student, and Instructor.
  - Course creation and management workflows allow Instructors to upload content and track student progress.
  - Subscription plans and payments successfully integrated with Stripe.

- **User Experience:**
  - Students can browse courses, subscribe/enroll, access learning materials, and track progress.
  - Instructors can efficiently manage courses, track enrollments, and view earning statements.
  - Admin users have tools for managing users/roles, moderating courses, and configuring payout cycles.

- **Technical Constraints:**
  - Adherence to primary stack: Next.js, NestJS, Postgres, Clerk/Auth0, Stripe.
  - Ensure system security and compliance with web standards throughout development phases.

## Open Questions

- Should all courses be accessible under every subscription plan, or should there be exclusive courses for specific plans?
- What is the exact product vision in one sentence, and who is the intended audience?


# Scope

This section defines the functionality and features included in the initial version of the product and identifies areas deliberately excluded from this iteration.

## In Scope

- **Technology Stack**
  - Next.js + NestJS + Postgres + Prisma for core architecture.
  - Clerk/Auth0 for authentication.
  - Stripe Billing for payment processing.
  - Managed services such as AWS S3 or Cloudflare Stream for storage.
  - Postmark or SendGrid for email communications.

- **Core Features**
  - **Role-Based Access Control (RBAC)**
    - Defined roles for Admin, Student, and Instructor.
  - **Subscription Management**
    - Supports monthly and annual plans.
    - Subscription lifecycle: trial, upgrade, cancel, renew.
  - **Course Authoring and Management**
    - Creation and publishing workflow for courses.
  - **Progress Tracking and Certifications**
    - Track student enrollment progress.
    - Issue certificates upon course completion.
  - **Instructor Payouts**
    - Payments based on enrollment metrics.
    - Options for fixed per enrollment or revenue-share model.
  - **User Interfaces**
    - Public Interface: landing page, course catalog, and checkout.
    - Auth Interface: sign up/in, password recovery.
    - Student Dashboard: course player, profile, certificates, subscriptions.
    - Instructor Dashboard: course builder, earnings view.
    - Admin Dashboard: user management, subscription plan configuration, reporting, payouts.
  - **Notifications and Email Communication**
    - Automated notifications for transactions such as renewal, cancellation, and payouts.

## Out of Scope

- **Native Mobile Applications**
  - The scope is limited to a web-only MVP for this version.
- **A La Carte Course Purchases**
  - Individual course purchases are excluded initially; focus is on all-access subscriptions.
- **Advanced Analytics and Reporting**
  - Basic reporting will be available, but complex analytics are excluded.
- **Multiple Language Support**
  - English interface only; translations are postponed.
- **Comprehensive Security Framework**
  - Only essential security measures will be implemented initially.
- **Extensive Plugin Support**
  - Custom build will not include extensive plugin integration; focus is on functionality included in the primary tech stack.

## Notes

- The scope is influenced by a budget range of $20-60k and a 4-month development timeline.
- Specific decisions on subscription access (all courses vs. catalog) remain under evaluation. 

## Open Questions

- Should subscriptions unlock all courses on the platform or only a specific subscription catalog?


### Personas and Roles

| Role       | Description                                                                                                                                    | Key Permissions                                                                                                                                               |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Admin**  | Manages the platform, ensuring all operations run smoothly, from user management to subscription plans.                                        | - Manage users and roles<br>- Approve courses and instructors<br>- Manage subscriptions and plans<br>- Reconcile payouts and generate reports<br>- Handle refunds and disputes<br>- Enforce content policy |
| **Student**| Engages with course content, tracks progress, and manages personal subscription details.                                                       | - Browse and enroll in courses<br>- Access course content and progress tracking<br>- Earn certificates<br>- Manage profile and learning history<br>- Subscription management (view, upgrade, cancel)  |
| **Instructor** | Responsible for course creation, managing student progress, and tracking earnings and payouts.                                                | - Create and manage courses<br>- Upload and organize course content<br>- View student progress and enrollment statistics<br>- Check earnings and payout status |

### Open Questions

- Should subscriptions unlock access to all courses or be limited to a specific catalog?
- Is there a clear differentiation between monthly and annual subscription management in terms of permissions?


### High-level User Journeys

#### Admin Role

1. **User Management:**
   - Admin logs into the platform via the Auth system (Clerk/Auth0).
   - Navigates to the user management dashboard.
   - Performs actions such as adding, editing, or removing users and roles.
   
2. **Course Approval:**
   - Admin views pending course submissions.
   - Reviews courses and takes actions to approve or reject them.
   
3. **Subscription Management:**
   - Configures subscription plans (monthly/annual) in the admin interface.
   - Manages subscription changes, upgrades, and cancellations.
   
4. **Payout Processing:**
   - Sets up and configures payout cycles based on defined schedules.
   - Reconciles payout requests and confirms payment processing.

5. **Reporting:**
   - Accesses and generates user, course, and financial reports.
   - Monitors analytics and system usage.

6. **Handling Disputes:**
   - Manages refund requests and disputes.
   - Enforces content policies.

7. **Exceptions:**
   - User data sync failure with external systems. Admin notified via email.

#### Student Role

1. **Course Exploration:**
   - Browses the course catalog and previews course details.
   - Uses search and filter functionalities to find relevant courses.
   
2. **Subscriptions and Enrollment:**
   - Selects subscription plan and completes checkout via Stripe.
   - Enrolls in courses, based on all-access or specific catalog unlocks.

3. **Learning Experience:**
   - Accesses the student dashboard to navigate enrolled courses.
   - Engages with course materials, completes modules, and takes assessments.
   
4. **Progress and Certification:**
   - Tracks learning progress through the dashboard.
   - Earns certificates upon course/module completion.
   
5. **Profile and Billing Management:**
   - Updates profile details and manages subscription settings.
   - Reviews billing history and manages payment information.

6. **Exceptions:**
   - Retry mechanism for failed transactions during checkout.

#### Instructor Role

1. **Course Creation:**
   - Logs in and accesses the instructor dashboard.
   - Uses the course builder/manager to create and publish new courses.
   
2. **Student Monitoring:**
   - Views student progress and engagement stats for their courses.
   - Provides feedback and support to enrolled students.
   
3. **Earnings and Payouts:**
   - Checks earnings reports based on enrollment and engagement metrics.
   - Views payout status and history on the dashboard.

4. **Content Upload and Management:**
   - Uploads and manages course content (videos, documents) using S3-compatible storage.

5. **Exceptions:**
   - Feature to notify Admin for manual approval if content flags any policy violation.

### Open Questions

- Should subscriptions unlock all courses or a specific subscription catalog?
- What is the default protocol when users cancel subscriptions mid-cycle?
- Are there any specific requirements for handling special cases in payouts?


# Functional Requirements

## Account Management Module
- **Authentication and Authorization**
  - MUST provide authentication using Clerk/Auth0.
  - MUST implement Role-Based Access Control (RBAC) for Admin, Student, and Instructor roles.
  - SHOULD allow password reset functionality.

- **User Profile**
  - MUST enable profile management for Students and Instructors.
  - SHOULD include learning history and achievements display.

## Subscription and Payment Module
- **Subscription Management**
  - MUST support monthly and annual subscription plans.
  - MUST manage subscription lifecycle: trial, upgrade, cancel, renew.
  - SHOULD allow a la carte course purchases (Assumption: to be implemented post-MVP).

- **Payment Processing**
  - MUST integrate with Stripe for payment processing.
  - MUST handle payment notifications via webhooks.

## Course Management Module
- **Course Authoring and Publishing**
  - MUST allow Instructors to create, edit, and publish courses.
  - MUST support a course preview function for Students.

- **Progress Tracking and Assessment**
  - MUST track student progress throughout the course.
  - SHOULD implement basic assessment and certification functionalities.

## Learning Experience Module
- **Catalog and Discovery**
  - MUST include a searchable course catalog with filter options.
  - MUST support course details and enrollment pages.

- **Course Player**
  - MUST provide a course player with access to lessons/modules.

## Instructor and Earnings Management Module
- **Course Management Dashboard**
  - MUST allow Instructors to view and manage their courses and enrolled students.

- **Earnings and Payout Management**
  - MUST calculate payouts based on enrollments using fixed or revenue-share options.
  - MUST provide Instructors with earnings dashboards and payout statuses.

## Administrative Module
- **User and Course Management**
  - MUST enable Admins to manage users, roles, and approve courses.
  
- **Subscription and Payouts**
  - MUST allow Admins to manage subscription plans and payout cycles.
  - MUST include reporting features for reconciliation and auditing.

- **Notifications and Communication**
  - MUST send notifications such as email receipts, renewal/cancellation, and payout notices.
  - Postmark or SendGrid for managing email communications.

## Security and Compliance Module
- **Data Protection**
  - MUST implement security measures to protect user data (details TBD).

- **Audit and Reporting**
  - SHOULD include audit logs for admin actions.
  - SHOULD provide reporting tools for system analytics.

## Open Questions
- Should subscriptions unlock all courses on the platform or only a specific subscription catalog?
- What are you trying to build (in one sentence), and who is it for?

## Assumptions
- A la carte course purchases to be implemented after MVP.
- English-first interface for launch.
- Lightweight certificate generator to be included as basic functionality.


### Non-Functional Requirements

#### Performance
- **Response Time:** User interactions, including browsing courses and navigating dashboards, should have a response time of less than 2 seconds.
- **Transactions:** High-volume transactions such as subscriptions and course enrollments should have a response time of less than 5 seconds.
- **Load Handling:** The system must support up to 10,000 concurrent users without degradation in performance.

#### Security
- **Authentication:** Utilize managed services like Clerk/Auth0 to secure user authentication processes.
- **Data Protection:** All user data must be encrypted at rest and in transit.
- **Access Control:** Strong Role-Based Access Control (RBAC) must be implemented for Admin, Student, and Instructor roles.

#### Compliance
- **GDPR Compliance:** The system should be designed with GDPR compliance for handling user data, considering that it will potentially be accessed by users within the EU.
  
#### Reliability
- **Uptime:** Aim for 99.9% system uptime, ensuring minimal downtime for essential services like course access and payment processing.
- **Backup:** Implement regular automated backups for the database to prevent data loss.

#### Scalability
- **Vertical Scaling:** The architecture should support vertical scaling of the Next.js frontend and NestJS API to handle increased loads.
- **Horizontal Scaling:** Consider horizontal scaling for the Postgres database using managed services to accommodate growing datasets.

#### Localization
- **Language:** Initial rollout in English. Future expansions should consider localization strategy for multi-language support. (Assumption)
- **Currency:** Payments to be processed in USD with a future capability for multi-currency support.

#### Observability
- **Monitoring:** Implement comprehensive monitoring using tools integrated with Vercel and Render/Fly.io.
- **Logging:** Maintain detailed logs for user activities, transactions, and system errors to facilitate issue diagnostics and audits.

#### Open Questions
- Should localized content and support for multi-currency be prioritized in future phases?
- Are there specific security compliance requirements beyond GDPR that should be considered?

#### Assumptions
- It is assumed that the system will initially focus on domestic (U.S.) users until further localization is deemed necessary.
- Multi-language support will be considered post-MVP based on user demand and market expansion.

This section provides a detailed outline of the non-functional requirements, addressing key areas necessary to ensure a robust, secure, and scalable platform. Each domain has been carefully considered with current knowledge, and open questions highlight areas needing further clarification.


# Integrations and Data

## Integrations List

- **Authentication**
  - Clerk/Auth0 for user authentication and RBAC (Role-Based Access Control).

- **Payment Processing**
  - Stripe Billing for subscription management and payment processing.

- **Data Storage**
  - Postgres (managed) with Prisma ORM for database management.

- **Media Storage**
  - AWS S3 or Cloudflare Stream for storing media content related to courses.

- **Email Services**
  - Postmark or SendGrid for email notifications, including receipts, renewal notices, and payout notices.

## Key Data Entities

- **User**
  - Attributes: ID, role (Admin, Student, Instructor), profile details, subscription status.
 
- **Course**
  - Attributes: ID, title, description, author (instructor), multimedia content links, pricing details.

- **Subscription**
  - Attributes: ID, user ID, plan type (monthly/annual), status (active/trial/canceled), payment history.

- **Enrollment**
  - Attributes: ID, course ID, user ID, enrollment date, progress, certification status.

- **Payment Transaction**
  - Attributes: ID, user ID, course or subscription ID, amount, payment method, transaction date.

- **Payout**
  - Attributes: ID, instructor ID, amount, payout method, payout date, enrollment details.

## High-Level Data Flow Notes

- **User Authentication Flow**
  - Users will authenticate via Clerk/Auth0. User roles are assigned upon account creation or by an admin. Access to various platform features is controlled based on role.

- **Course Management Flow**
  - Instructors create and publish courses. Courses are stored in a Postgres database, with multimedia content managed via S3 or Cloudflare Stream.

- **Subscription and Payment Flow**
  - Subscriptions (monthly/annual) are managed through Stripe. Stripe handles payment processing and transaction history, with updates to user subscription status in the database.

- **Enrollment and Progress Tracking Flow**
  - Enrollments are linked to user and course records. User progress is tracked and updated in real-time to facilitate certificate issuance upon completion.

- **Payouts and Revenue Share Flow**
  - Instructor payouts are calculated based on enrollment data and processed on a scheduled cycle. Details are managed in the database and payments executed via Stripe.

## Open Questions

- Should subscriptions unlock all courses on the platform or only a specific subscription catalog?
- How will disputes or refunds be handled within the payment processing flow?
- Is there a requirement or preference for specific media storage beyond S3 or Cloudflare Stream?

## Assumptions

- The email service choice between Postmark or SendGrid will not impact the core logic for notifications and is flexible based on further testing or preference.
- Subscription changes will automatically trigger updates to access permissions and notifications without additional user intervention.


## Constraints and Assumptions

### Constraints

- **Budget:**
  - Confirmed budget between $25,000 and $50,000.
  - Target range of $20,000 to $60,000.

- **Timeline:**
  - 4-month timeline for MVP launch.
  
- **Platform:**
  - Web-only application.
  - Primary tech stack: Next.js + NestJS + Postgres + Prisma with managed services like Clerk/Auth0 for authentication and Stripe Billing for payments.
  - Fallback option is WordPress with LearnDash/LifterLMS.

- **Compliance:**
  - Must comply with standard web security and user authentication practices.
  
- **Role Definitions:**
  - Roles: Admin, Student, Instructor (Teacher).
  - Key features include RBAC, subscription management, course authoring, and progress tracking.
  
- **Feature Scope:**
  - Monthly and annual subscription plans.
  - Instructor payouts based on enrollments; options for fixed amount or revenue-share.
  - Subscription lifecycle management and course publishing required.

- **UI/UX:**
  - Web-first product design focusing on backend-relevant screens for various roles.
  - UI development in phases over 4 months.

### Assumptions

- **Feature Implementation:**
  - Subscription lifecycle, RBAC, course publishing, and enrollment-based payouts to be implemented without plugin reliance when using the custom stack.
  - Certificate generation will be lightweight and initially in English only.

- **Payment and Subscriptions:**
  - Stripe will handle all payment processing.
  - All-access subscriptions for launch, with potential for individual course purchases as a future phase.

- **Support and Maintenance:**
  - AWS S3 or Cloudflare Stream for storage, with Postmark or SendGrid for email services.

- **Open Questions:**
  - Should subscriptions provide access to all platform courses or just a specific catalog?
  - Clarification needed on the core purpose and target audience of the product in one sentence.


## Open Questions

### P0 Questions
1. **Subscription Access Model**  
   - *Clarification Needed*: Should subscriptions unlock all courses on the platform, or should they offer access to a specific subscription catalog?
   - *Owner Suggestion*: Product Owner

2. **Core Product Definition**  
   - *Clarification Needed*: Define the product vision succinctly: What is being built in one sentence, and who is the primary target audience?
   - *Owner Suggestion*: Founder

3. **Specific Subscription Catalog**  
   - *Clarification Needed*: If a specific subscription catalog is pursued, how will courses be selected for inclusion in this catalog?
   - *Owner Suggestion*: Product Owner

### P1 Questions
1. **Instructor Payout Calculations**  
   - *Clarification Needed*: For the revenue-share payout model, what percentage or calculation method will be applied?
   - *Owner Suggestion*: Product Owner

2. **Course Purchase Flow**  
   - *Clarification Needed*: How will the a la carte course purchase flow differ from subscription flows? What specific UI elements will need differentiation?
   - *Owner Suggestion*: Engineering

3. **Role-Based Access Configuration**  
   - *Clarification Needed*: Are there any special permissions or restrictions for Admin, Student, or Instructor roles beyond standard RBAC?
   - *Owner Suggestion*: Product Owner

### P2 Questions
1. **Localization and Language Support**  
   - *Clarification Needed*: Will additional language support be a consideration post-launch beyond the initially assumed English-only interface?
   - *Owner Suggestion*: Product Owner

2. **Fallback Tech Stack Feasibility**  
   - *Clarification Needed*: Should the fallback option (WordPress with LearnDash/LifterLMS) be considered viable and competitive enough to meet MVP launch goals?
   - *Owner Suggestion*: Engineering

3. **Support and Maintenance Roles**  
   - *Clarification Needed*: What will be the designated process for handling user support and content moderation post-launch?
   - *Owner Suggestion*: Product Owner

4. **Security and Compliance**  
   - *Clarification Needed*: What specific security measures must be integrated to ensure compliance with data protection regulations (e.g., GDPR)?
   - *Owner Suggestion*: Engineering

These questions need to be addressed to ensure a clear path forward and prevent roadblocks in the development and launch process.
