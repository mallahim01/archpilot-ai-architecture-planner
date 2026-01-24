# Requirements Document

**Job ID:** `ca1f7caf-fb36-4039-a063-5acbfe869de1`


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

The product under development is a hybrid-monetized, multi-instructor Learning Management System (LMS) and marketplace. It is designed to offer both monthly and annual subscription models, alongside optional single-course purchases. The system will primarily serve instructors and a growing student base by providing a scalable platform for creating, delivering, and managing educational content. A key component of the platform is its role-based access control, supporting Admin, Student, and Instructor roles to facilitate distinct user experiences.

### Product
- Hybrid-monetized multi-instructor LMS/marketplace
- Offers monthly/annual subscriptions and individual course purchases
- Includes role-based access with Admin, Student, and Instructor roles

### Target Users
- Multiple instructors wanting to publish and monetize courses
- Students seeking diverse educational content from multiple instructors

### Core Value
- Scalable platform for course creation and management
- Monetization through subscriptions and course purchases
- Comprehensive role-based functionalities for diverse user needs

### Non-goals
- The document does not address mobile app development at this stage (Assumption: web-first focus)
- Detailed instructor payout distribution (Open Question: How are instructor payouts managed?)

### Open Questions
- Will the platform be exclusively web-based, or will it include mobile/responsive components?
- How are subscriptions structured regarding platform revenue sharing or direct instructor payouts?


### Goals and Success Criteria

#### Goals
- Develop a hybrid-monetized LMS/marketplace supporting multi-instructor capabilities.
- Achieve MVP launch within a 4-month timeline.
- Implement monthly/annual subscription plans and single-course purchase options.
- Ensure role-based access control for Admin, Student, and Instructor roles.
- Design a responsive web-first platform with scalable architecture.

#### Success Metrics
- Launch an MVP under the budget of $25–50k within the 4-month timeline.
- Implement functional RBAC, subscription plans, and payment systems by the end of Month 1.
- Complete catalog/search, checkout, dashboards, and notifications by the end of Month 2.
- Finalize lifecycle management, enrollment events, earnings, and payout cycles by Month 3.
- Conduct comprehensive QA to ensure performance and security readiness by Month 4.
- Validate system functionalities including subscription lifecycle, course authoring, and enrollment tracking.

#### Acceptance Criteria
- Successfully deploy an MVP platform with key features: subscriptions, role-based access, course publishing, and progress tracking.
- Adequately implement instructor payout logic with initial internal management, allowing future integration with Stripe Connect.
- Efficiently manage all platform functionalities from the Admin role, such as user management and monetization tools.
- Provide verified pathways for students to browse, purchase, enroll, and track course progress.
- Ensure instructors can create, manage, and track their courses and earnings.

#### Open Questions
- Will the platform initially be web-only, or should it include mobile/responsive components?
- How will subscription revenues be distributed? Is it direct to instructors with an added platform fee, or centralized with platform revenue-sharing?


## Scope

### In Scope

- **Platform Roles**
  - **Admin Role:**
    - User and instructor management
    - Course moderation
    - Subscription plan configuration
    - Payout cycle management
    - Reporting and analytics
  - **Student Role:**
    - Course discovery and purchases
    - Learning modules and assessments
    - Certificate management
    - Subscription and account settings
  - **Instructor Role:**
    - Course creation and management
    - Student progress tracking
    - Revenue and payout monitoring

- **Monetization and Subscription**
  - Monthly and annual subscriptions for platform-level access
  - Optional single-course purchases
  - Subscription lifecycle management: trial, upgrade, cancel, renew

- **Core Features for MVP**
  - Role-based access control (RBAC)
  - Course creation and publishing workflow
  - Enrollment and progress tracking
  - Certificate generation
  - Instructor earnings and payout calculations
  - Email notifications, including receipts and renewal/cancellation notices

- **Tech Stack Implementation**
  - Frontend with Next.js (React) and Tailwind
  - Backend with NestJS (Node/TypeScript) REST API
  - Managed Postgres with Prisma ORM
  - Auth0 or Clerk for authentication and RBAC
  - Stripe Billing for payments
  - S3-compatible storage and Mux/Cloudflare Stream for media
  - Postmark/SendGrid for emails and notifications
  - Vercel and Render/Fly.io for hosting

- **UI/UX Features**
  - Catalog browsing, search, and filter capabilities
  - Checkout flows for subscription and course purchases
  - Student and instructor dashboards

- **Project Phases**
  - Month 1: RBAC, course model, subscription plans, payments, and admin management
  - Month 2: Catalog/search, checkout, student dashboard, course player, and notifications
  - Month 3: Subscription lifecycle, enrollment events, instructor earnings, and payout cycles
  - Month 4: QA, security, analytics, audit logs, support flows, and production readiness

### Out of Scope

- **Mobile Application**
  - Initial release will be web-first; mobile app development is not included in current scope

- **Alternative Tech Stack**
  - Fallback stack using WordPress with LearnDash/LifterLMS is not included in MVP

- **Subscription Exclusivity**
  - UI decision on whether subscriptions unlock all courses or a selective catalog remains undecided

- **External Instructor Payout Handling**
  - Integration with Stripe Connect for instructor payouts is not included in MVP

### Open Questions

- Will the platform be exclusively web, or should it include mobile/responsive components at launch?
- Are subscriptions paid to the platform with revenue sharing to instructors, or do instructors get direct payouts with a platform fee on top?


# Personas and Roles

The following table outlines the defined roles/personas, their responsibilities, and key permissions. The system will initially include three primary roles: Admin, Student, and Instructor (Teacher).

| Role      | Description | Key Permissions |
|-----------|-------------|-----------------|
| Admin     | The admin is responsible for overseeing the entire platform, managing users, and ensuring smooth operations. | - Manage users/roles<br>- Approve courses/instructors<br>- Configure subscription plans<br>- Oversee payout cycle management<br>- Access to reporting and analytics<br>- Handle refunds/disputes<br>- Enforce content policy |
| Student   | Students are end-users who enroll in courses, actively participate in learning, and manage their subscriptions. | - Browse and discover courses<br>- Purchase and access courses<br>- Track learning progress<br>- Participate in assessments<br>- Manage certificates<br>- Manage billing/subscription settings |
| Instructor | Instructors create and manage courses, track student progress, and monitor their earnings and payouts. | - Create and publish courses<br>- Upload and manage content<br>- View student enrollment and progress<br>- Track earnings and payout status<br>- Manage personal profile |

**Open Questions:**
- Are there additional roles required beyond Admin, Student, and Instructor for the MVP?
- How will the platform handle instructor payouts? Will it be internal or require external solutions like Stripe Connect?


# High-level User Journeys

## Admin Role

1. **User Management**
   - Access the admin dashboard.
   - Manage user roles and permissions.
   - Approve or reject instructor applications.

2. **Course Moderation**
   - Review and approve newly submitted courses.
   - Monitor course content for compliance with content policies.

3. **Monetization Controls**
   - Configure subscription plans (monthly/annual).
   - Set pricing for single-course purchases.

4. **Payout Operations**
   - Manage instructor payout cycles.
   - Reconcile payouts based on enrollments and revenue-sharing agreements.

5. **Platform Monitoring**
   - Access reporting and analytics.
   - Generate reports related to user activity, course performance, and financials.

6. **Subscription Management**
   - Handle user subscription lifecycle processes including upgrades, cancellations, and renewals.

7. **Edge Cases & Exceptions**
   - Handle refund requests and disputes.
   - Monitor support tickets for any issue resolution.

## Student Role

1. **Course Discovery**
   - Browse and search through the course catalog.
   - Use filters to find specific courses.

2. **Subscription and Purchase**
   - Choose between platform subscription (monthly/annual) and individual course purchases.
   - Complete checkout using integrated payment solutions.

3. **Learning Experience**
   - Access enrolled courses via the student dashboard.
   - Engage with course materials and complete modules.

4. **Assessment and Certification**
   - Complete assessments and quizzes.
   - Generate and download certificates upon course completion.

5. **Account Management**
   - Manage personal profile and learning history.
   - Handle billing and subscription settings.

6. **Edge Cases & Exceptions**
   - Trial periods before subscription commitments.
   - Process for handling subscription upgrades or cancellations.

## Instructor Role

1. **Course Creation and Management**
   - Access the instructor dashboard.
   - Use the course builder to create and publish courses.
   - Manage course content and modules.

2. **Student Engagement**
   - Monitor student impact and progress through enrollment stats.

3. **Earnings and Payout Tracking**
   - Track earnings related to course enrollments.
   - View payout status and details in the earnings view.

4. **Profile Management**
   - Update instructor profile and course offerings.

5. **Edge Cases & Exceptions**
   - Handle enrollment anomalies (e.g., administrative enrollment corrections).
   - Manage disputes or refund requests as per platform guidelines.

## Open Questions

- Clarification needed on web-only versus mobile/responsive platform offerings.
- Details on payout structure: platform revenue-sharing model versus direct instructor payout with platform fee.

## Assumptions

- All subscription services will initially be managed internally with an option to integrate Stripe Connect in future phases.
- Platform will start as web-responsive with possibilities of mobile app development later.


# Functional Requirements

## Role Management
- **MUST** implement Role-Based Access Control (RBAC) with three initial roles: Admin, Student, Instructor.
- **SHOULD** allow dynamic role assignment and changes by Admin.
- **MUST** support managed authentication solutions such as Clerk or Auth0.

## Subscription Management
- **MUST** support both monthly and annual subscription plans.
- **MUST** provide trials, upgrades, cancellations, and renewals for subscriptions.
- **MUST** allow single-course purchases in addition to subscriptions.
- **SHOULD** enable platform-level access for all or only selected courses in subscription plans.

## Course Management
- **MUST** offer a course builder tool for instructors to create and manage courses.
- **MUST** provide a content delivery system using S3 and Mux/Cloudflare Stream.
- **SHOULD** support course moderation and approval by Admin.

## Enrollment and Progress Tracking
- **MUST** track student enrollments and course progress.
- **MUST** allow students to view course progress and completed modules.
- **SHOULD** integrate assessments and quizzes for students with tracking capabilities.

## Payment System
- **MUST** integrate with Stripe Billing for processing payments.
- **MUST** support one-time purchases and ongoing subscription billing.
- **SHOULD** keep initial payout logic internal with an option to incorporate Stripe Connect later.

## Instructor Earnings and Payouts
- **MUST** calculate instructor earnings based on enrollments (either fixed per enrollment or revenue-share).
- **SHOULD** offer a ledge system in the instructor dashboard for tracking payouts.
- **MUST** enable payout cycle management by Admin.

## Notifications and Communications
- **MUST** use Postmark or SendGrid for email notifications.
- **MUST** send enrollment confirmations, payment receipts, and subscription-related notices.
- **SHOULD** include notifications for course status updates.

## Analytics and Reporting
- **MUST** provide Admin access to platform analytics for monitoring user activity, courses, and financial metrics.
- **SHOULD** include reporting capabilities for subscription metrics and instructor performance.

## Security and Production Readiness
- **MUST** maintain data security with standard practices.
- **SHOULD** finalize QA processes for platform readiness by Month 4.
- **MUST** ensure performance optimization for scalability.

## User Interface and Experience
- **MUST** support responsive web design with Next.js for front-end implementation.
- **SHOULD** consider mobile app development in later phases.
- **MUST** implement user-friendly interfaces for checkout flow, catalog browsing, and dashboards.

## Assumptions and Open Questions
- **Assumption**: Platform will initially focus on a web-only experience, expanding to mobile in the future.
- **Open Question**: Should all subscription plans unlock all courses, or should certain courses be excluded?
- **Open Question**: Are subscriptions paid directly to the platform with platform handling revenue sharing with instructors?


# Non-Functional Requirements

## Performance
- The platform should handle initial traffic expected from a multi-instructor setup with a growing student base.
- Page load times should not exceed 2 seconds under normal traffic conditions.
- Video streaming should maintain a resolution of at least 720p without buffering on an average internet connection.

## Security
- Use managed authentication services like Auth0 or Clerk to ensure secure user authentication and Role-Based Access Control (RBAC).
- All data should be encrypted in transit and at rest.

## Compliance
- Follow GDPR guidelines for user data protection and privacy.
- Payment processing should comply with PCI-DSS standards.

## Reliability
- Ensure 99.9% uptime SLAs for both frontend and backend services.
- Backup and recovery procedures should be in place for databases and critical data (e.g., course enrollments, user details).

## Scalability
- The platform should support modular growth, accommodating more instructors and students without significant performance degradation.
- Ensure the database and media storage solutions (e.g., S3, Postgres) are scalable with demand.

## Localization
- Provide support for multiple languages in the UI as the user base grows globally (Assumption).

## Observability
- Implement monitoring tools for real-time analytics on user behavior and system performance.
- Provide logging and audit trails for critical actions in the system (e.g., course creation, user role changes).

## Open Questions
- Should the platform include mobile app development in the initial phase or later, considering the "web-first" design?
- Should subscriptions unlock all courses by default, or will certain courses remain outside subscription access?

## Assumptions
- The platform monetization model includes both monthly and annual subscriptions as well as individual course purchases as per standard market practice.
- The system architecture is expected to be responsive, catering primarily to web users initially.


# Integrations and Data

## Integrations List

- **Authentication/RBAC**: 
  - **Clerk/Auth0** for authentication and role-based access control.
  
- **Payments and Subscriptions**:
  - **Stripe Billing** for managing subscriptions, payments, and billing processes.

- **Storage**:
  - **S3** or S3-compatible services for storing files.
  - **Mux/Cloudflare Stream** for video content delivery.

- **Email Notifications**:
  - **Postmark** or **SendGrid** for transactional emails and notifications.

- **Hosting and API**:
  - **Vercel** for frontend hosting.
  - **Render/Fly.io** for backend API hosting.

- **Database**:
  - **Postgres** with **Prisma** for database management and ORM.

## Key Data Entities

- **User**: Information related to Admins, Students, and Instructors, including authentication details and role assignments.

- **Course**: Details including course metadata, content, and instructor information.

- **Subscription**: Data concerning users’ subscription status, subscription plans, and payment details.

- **Enrollment**: Records of student course enrollments and corresponding enrollment statuses.

- **Instructor Payout**: Information on instructor earnings, payout cycle, and payout amounts.

- **Progress Tracking**: Data relating to student progress, including lesson completions and assessments.

- **Certificates**: Details on issued certificates and associated achievements.

## Data Flow Notes

- **User Authentication**: 
  - Users sign in through **Clerk/Auth0**, triggering authentication flows that manage access permissions via RBAC.

- **Course Access**:
  - Upon successful authentication, students access courses based on their subscriptions, tracked by Stripe Billing data.

- **Content Delivery**:
  - Course materials and videos are served through **S3** and **Mux/Cloudflare Stream** following user access validation.

- **Payments and Subscriptions**:
  - Subscription payments are processed through **Stripe**, updating records in Postgres and impacting user access to content.

- **Instructor Payouts**:
  - Enrollment data influences payout calculations, logged internally with potential expansion to **Stripe Connect** later.

- **Notifications**:
  - Postmark handles notification workflows, sending email receipts and updates directly to users.

## Open Questions

- Will the platform be web-only or include mobile/responsive components initially?
- How are revenue-sharing and instructor payouts structured? Are subscriptions paid to the platform with revenue-sharing, or does each instructor get paid directly with a platform fee applied?

## Assumptions

- The data flow prioritizes internal processing of instructor payouts for MVP, with potential integration of **Stripe Connect** post-MVP.


### Constraints and Assumptions

#### Constraints

- **Budget:**
  - Total budget is constrained to $25–50k.

- **Timeline:**
  - Project timeline is fixed at 4 months for MVP launch.
  - Development is planned in phases across the months:
    - **Month 1:** RBAC, course model, subscription plans, payments, core admin management.
    - **Month 2:** Catalog/search features, checkout system, student dashboard, course player, email notifications.
    - **Month 3:** Subscription lifecycle, enrollment events, instructor earnings, payout cycles.
    - **Month 4:** QA, security enhancements, analytics, audit logs, support flows, performance optimization, legal compliance, production readiness.

- **Platform:**
  - Initial deployment will be web-first, optimized for responsiveness.
  - Only three roles at launch: Admin, Student, Instructor (Teacher).

- **Compliance and Security:**
  - Inclusion of legal pages and adherence to relevant regulations.

- **Tech Stack:**
  - Use of Next.js for frontend, NestJS for API, Postgres with Prisma, Stripe for billing, S3 for file storage, Mux/Cloudflare Stream for video, and Postmark for emails.

#### Assumptions

- **Monetization Model:**
  - Platform will support both monthly and annual subscription models.
  - Capability for users to purchase individual courses.

- **Mobile Component:**
  - Assumed web-first launch without a dedicated mobile app initially, with potential consideration later.

- **Subscription Access:**
  - Assumed that subscription may include access limitations or exclusivity tiers for different courses. Clarification required whether all courses are unlocked under any subscription.

- **Instructor Payout Logic:**
  - Default assumption is to manage payouts internally for MVP, with an option to integrate Stripe Connect later.

#### Open Questions

- **Platform Accessibility:**
  - Will the platform be strictly web-based, or is there a requirement for a mobile/responsive component in the initial phase?

- **Revenue Model:**
  - Will subscriptions be paid to the platform and then revenue shared with instructors, or will instructors directly collect fees with a platform surcharge?


### Open Questions

#### P0 (Critical)
- **Subscription Access Clarification**
  - Should subscriptions unlock all courses on the platform, or is there a separate subscription catalog with some excluded courses?  
  *Owner: Product*

- **Mobile Component Decision**
  - Will the platform initially support only web, or include responsive/mobile components in the MVP?  
  *Owner: Founder*

- **Revenue Sharing Model**
  - How will subscriptions work in terms of payments? Are subscriptions paid to the platform with the platform managing revenue-sharing and payouts to instructors, or do instructors get paid directly with a platform fee on top?  
  *Owner: Product*

#### P1 (High Priority)
- **Instructor Payout Structure**
  - How precisely will instructor payouts be structured? Confirm if this will be a fixed amount per enrollment, a revenue-share per enrollment, or another method.  
  *Owner: Product/Engineering*

- **Certificate Generation**
  - Confirm if certificate generation will indeed be a lightweight feature included in the MVP.  
  *Owner: Product*

#### P2 (Normal Priority)
- **Platform Scalability Limits**
  - What are the expected scalability constraints, particularly regarding the number of instructors and students the platform can support initially?  
  *Owner: Engineering*

- **Support for Non-English Languages**
  - Is there a requirement for supporting multiple languages in the UI/UX from the beginning, or will this be planned for a future update?  
  *Owner: Product*

- **Content Policy and Moderation**
  - Define the content policy and moderation guidelines for instructors' courses and materials. Is this to be automated or manually reviewed?  
  *Owner: Admin/Product*

- **Instructor Interaction with Students**
  - What level of interaction is expected between instructors and students (e.g., messaging, Q&A boards)?  
  *Owner: Product*

- **Post-MVP Features**
  - Confirm which features are strictly necessary for post-MVP and not required to be built initially.  
  *Owner: Product*
