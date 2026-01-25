# Requirements Document

**Job ID:** `5822657b-8e97-4644-bfc5-d7ab636cfeb7`


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

We are developing a comprehensive online educational platform designed to facilitate seamless interaction between educational content creators and learners. The platform supports three primary roles: Admin, Teacher, and Student. Each role is tailored to meet specific needs within the ecosystem, ensuring effective governance, content creation, and learning experiences.

The core value of this platform lies in its ability to provide a secure, scalable environment for hosting and managing educational courses. By leveraging modern technologies like Next.js, NestJS, and robust third-party integrations for payments and authentication, it promises maintainability and high security, which are critical for compliance with standards such as GDPR and PCI-DSS.

Key elements include:

- **Product**: A modular platform for educational content delivery, complete with role-based access, payment handling, and compliance features.
- **Target Users**:
  - **Admins**: Manage compliance, content moderation, and monetization.
  - **Teachers**: Create, publish, and monetize courses.
  - **Students**: Discover courses, track learning progress, and earn certificates.
- **Core Value**:
  - Secure environment with advanced authentication.
  - Scalability and maintainability focus using a modern tech stack.
  - Compliance with major privacy and data protection regulations.
- **Non-goals**: The initial build focuses on core functionalities. Extended features, such as advanced analytics, will be targeted in Phase 2.
- **Open Questions**:
  - Are there additional compliance obligations specific to SOC 2 and enterprise SSO (Okta/SAML) that need consideration?
  - Is the current roles set (Admin, Teacher, Student) sufficient, or is a distinct Support role necessary?


## Goals and Success Criteria

### Goals

- Develop a high-security educational platform emphasizing maintainability.
- Implement core platform functionality during Phase 1 (14–16 weeks).
- Enhance and optimize the platform during Phase 2 (8–12 weeks).
- Ensure compliance with GDPR, SOC-2, and PCI-DSS standards.
- Facilitate seamless role-based access control and management.
- Enable easy course creation, management, and consumption by Teachers and Students.
- Integrate efficient payment processing and teacher payout systems.
- Deploy robust user authentication and authorization.
- Support comprehensive activity logging and audit trails.
- Align product delivery with the defined budget of $40k–$50k.
- Develop platforms for Admin, Teacher, and Student roles with specific functionalities for each.

### Success Metrics

- Successful deployment of core features within 14–16 weeks without exceeding the budget.
- Passing compliance audits for GDPR, SOC-2 readiness, and PCI-DSS.
- Achieving >95% uptime and functionality accuracy across all platform components.
- User adoption goal: X amount of active users within Y months post-launch.
- Metrics-driven assessment improvements in course engagement and completion rates.
- Reduction in support request volume by Z% due to enhanced UX design.
  
### Acceptance Criteria

- Completion of all Phase 1 components: roles management, courses, subscriptions, payouts, and certificates.
- Phase 2 deliverables include analytics, UX polish, and performance optimizations.
- Demonstration of secure, encrypted data handling both at rest and during transit.
- Verified integration with Stripe for payment processing and teacher payouts.
- Confident execution of role-specific tasks and responsibilities for Admin, Teacher, and Student.
- Activity logs and audit trails must be fully operational and exportable.
- Final platform usability testing and feedback integration are completed before official launch.

### Open Questions

- Is the current set of roles (Admin, Teacher, Student) sufficient, or should there be a distinct Support role?
- Are additional compliance obligations needed beyond SOC 2, GDPR, HIPAA/PCI, such as enterprise SSO requirements like Okta/SAML?


# Scope

## In Scope

- **Tech Stack Implementation**
  - Next.js for web applications.
  - NestJS for backend API.
  - Postgres for core data storage.
  - S3-compatible object storage for video/files.
  - Stripe for Billing/Checkout and teacher payouts.
  - Auth0 or Clerk for authentication and RBAC.

- **Security, Compliance & Trust Layer**
  - Secure Authentication using JWT/OAuth-based techniques.
  - Data encryption at rest and in transit.
  - Role-Based Permissions.
  - Secure Payment Handling with no card data storage.
  - Activity Logging & Audit Trails.
  - US compliance with SOC-2 readiness, GDPR-aligned data handling, and PCI-DSS compliance.

- **Platform Functionality: Phase 1 Focus**
  - User roles and management for Admin, Teacher, and Student.
  - Core platform functions for course creation and management.
  - Subscriptions, payouts, and certificate issuance.

- **Feature Development:**
  - Append-only audit log with export for admin.
  - Background jobs/queues for tasks like payouts sync, email notifications, certificate generation, and webhooks.
  - Managed authentication and app-level RBAC.
  - Notifications via email/in-app.

- **Primary User Journeys:**
  - Admin tasks: User/RBAC management, teacher verification, course moderation, pricing oversight, payout management, certificate rules management, notifications, audit logs, and platform analytics.
  - Teacher tasks: Profile verification, course creation/editing, pricing, publishing, engagement metrics, and earnings management.
  - Student tasks: Course discovery, subscription management, purchase history, progress tracking, certificate acquisition, and profile management.

## Out of Scope

- **Phase 2 Enhancements:**
  - Analytics and performance tuning.
  - UX polish.

- **Additional Compliance Considerations:**
  - Unaddressed compliance items beyond SOC-2, GDPR, HIPAA/PCI, or enterprise SSO mandates such as Okta/SAML (Open Question).

- **Support Role Implementation:**
  - Any potential support role functionalities not covered by Admin/Teacher/Student roles (Open Question).

### Notes:
- The current scope is determined by a budget of $40k–$50k and a timeline of 14–16 weeks for Phase 1, followed by 8–12 weeks for Phase 2.
- Assumption: No support role beyond the roles specified (Admin, Teacher, Student) unless identified as a necessity during development.


### Personas and Roles

| Role     | Description                                                                                           | Key Permissions                                                                                               |
|----------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Admin    | Responsible for governance, compliance, monetization oversight, and quality control.                  | - Manage users and roles with RBAC<br>- Verify teachers<br>- Moderate courses and content<br>- Manage monetization controls<br>- Oversee payouts/ledger<br>- Manage certificate templates/rules<br>- Access notifications and audit logs<br>- Access platform analytics |
| Teacher  | Content creators who publish courses, attract enrollments, and earn revenue.                         | - Signup/login and complete onboarding/verification<br>- Create/edit courses<br>- Set pricing and publish courses<br>- Version courses<br>- View enrollments and student engagement<br>- Manage earnings and payouts<br>- Access course analytics         |
| Student  | Consumers of educational content who track progress and earn certificates.                           | - Browse the course catalog<br>- Signup/login<br>- Purchase/subscribe to courses<br>- Manage billing/payment history/invoices<br>- Enroll and track learning progress<br>- Download/share certificates<br>- Manage profile and notification preferences |

### Open Questions

- **Compliance Obligations**: Are there additional compliance requirements such as SOC 2, GDPR, HIPAA/PCI, or enterprise SSO mandates like Okta/SAML that need to be considered?
- **Role Completeness**: Does the current role set (Admin/Teacher/Student) cover all needed functions, or is a distinct Support role necessary?


## High-level User Journeys

### Admin User Journey

1. **Login and Authentication**
   - Admins log in via the web interface using Auth0 or Clerk.
   
2. **User and Role Management**
   - Access user management screens.
   - Manage users and set RBAC permissions.

3. **Teacher Verification**
   - Verify teacher profiles via the verification/KYC screen.
   - Approve or reject teacher applications.

4. **Course Moderation**
   - Review and moderate courses submitted by teachers.

5. **Monetization and Pricing Oversight**
   - Manage and adjust pricing rules for courses.
   
6. **Payout Controls**
   - Access and oversee payouts/ledger for teachers using Stripe Connect.

7. **Certificate Management**
   - Manage certificate templates and rules.
   - Oversee certificate generation processes.

8. **Notifications Management**
   - Configure email and in-app notifications for compliance and updates.

9. **Audit and Compliance**
   - Access append-only audit logs.
   - Export logs for auditability and compliance purposes.

10. **Analytics and Reporting**
    - View platform analytics for performance insights.

### Teacher User Journey

1. **Signup and Verification**
   - Signup/login via Auth0 or Clerk.
   - Complete verification/KYC process.

2. **Course Creation**
   - Access course builder for creating modules, lessons, quizzes, and assignments.
   - Upload media and set course pricing.

3. **Publishing and Versioning**
   - Publish courses after creation.
   - Manage course versions and updates.

4. **Student Engagement Tracking**
   - View enrollments and student engagement analytics.

5. **Earnings and Payouts**
   - Track earnings via the teacher profile screen.
   - Receive payouts managed through Stripe Connect.

6. **Analytics and Feedback**
   - Access course analytics for performance review.

### Student User Journey

1. **Discovery and Enrollment**
   - Browse the course catalog.
   - Enroll by purchasing/subscribing to courses through Stripe Checkout.

2. **Learning and Progress Tracking**
   - Access courses using the learning player.
   - Track learning progress via the progress dashboard.

3. **Subscription and Payment Management**
   - Manage subscriptions and view purchase history.
   - Handle billing/payment history and view invoices.

4. **Certificate Management**
   - Download and share earned certificates.
   - Verify certificates through a public URL.

5. **Profile and Notification Preferences**
   - Manage profile settings.
   - Configure and manage notification preferences.

### Edge Cases & Exceptions

- **Admin Exception:** Unsuccessful verification of a teacher could trigger a notification to the Admin for manual review.
- **Teacher Exception:** If course media uploads exceed storage constraints, a notification should be triggered.
- **Student Exception:** Failed payment or subscription renewal will send an automated notification prompting action.

### Open Questions

- Is a distinct Support role necessary to manage high-volume inquiries?
- Are there additional compliance tools needed beyond SOC-2 readiness and PCI-DSS via payment providers?


# Functional Requirements

## User Management Module

- **MUST** support three primary roles: Admin, Teacher, Student.
- **MUST** incorporate Role-Based Access Control (RBAC) managed by Auth0 or Clerk.
- **MUST** provide secure authentication using JWT/OAuth.
- **SHOULD** allow Admins to manage user roles and permissions.
- **MUST** enable Admins to verify and approve teachers.
- **COULD** include optional SSO integration.

## Course Management Module

- **MUST** allow Teachers to create, edit, and publish courses, including course versioning.
- **MUST** enable course moderation by Admins.
- **MUST** support various content types: modules, lessons, quizzes, and assignments.
- **SHOULD** provide tools for Teachers to set course pricing.
- **SHOULD** include student engagement analytics for Teachers.

## Payment and Payout Module

- **MUST** handle secure payments using Stripe Billing/Checkout.
- **MUST** support subscriptions, one-off purchases, refunds, and chargebacks.
- **SHOULD** generate invoices/receipts for Students.
- **MUST** facilitate Teacher payouts through Stripe Connect.
- **SHOULD** provide payout reports for Teachers and Admins.

## Certificate and Progress Module

- **MUST** enable progress tracking and completion validation for Students.
- **MUST** issue certificates upon course completion.
- **SHOULD** provide a public certificate verification endpoint.
- **SHOULD** allow Admins to manage certificate templates and rules.

## Notifications and Logging Module

- **MUST** support email and in-app notifications for all roles.
- **MUST** include activity logging and audit trails for security and compliance.
- **SHOULD** offer append-only audit log tables with export capability for Admins.

## Compliance and Security Module

- **MUST** ensure encrypted data at rest and in transit.
- **MUST** comply with GDPR data handling principles.
- **MUST** demonstrate SOC-2 readiness.
- **MUST** ensure PCI-DSS compliance through Stripe.
- **SHOULD** implement privacy policy and terms enforcement.

## User Interface Module

- **MUST** provide comprehensive screens for each user role:
  - **Admin:** user/role management, teacher approval, course moderation, payout controls, audit logs, analytics.
  - **Teacher:** signup/login, onboarding/verification, course builder, earnings/payouts, analytics.
  - **Student:** onboarding, catalog browsing, subscription management, learning player, progress dashboard, certificates.
- **SHOULD** enhance UX in Phase 2, including polish and performance tuning.

## Background Processes Module

- **MUST** utilize background jobs/queues for:
  - Payout sync
  - Email dispatch
  - Certificate generation
  - Webhook management

## Open Questions

- How should enterprise SSO mandates like Okta/SAML be addressed?
- Does the existing role set (Admin/Teacher/Student) suffice, or is a separate Support role needed?

## Assumptions

- Default technology choices include using AWS S3 for storage and managed queues for async operations based on the recommended tech stack.
- Phase timelines and budget constraints of $40k–$50k for Phase 1 are assumed to be fixed unless additional features are introduced.


### Non-Functional Requirements

#### Performance
- The technology stack should efficiently handle web application demands: using Next.js for frontend and NestJS for backend.
- Background tasks such as payouts sync, email notifications, certificate generation, and webhooks should utilize a managed queue for scaling.

#### Security
- Managed authentication with Auth0 or Clerk implementing role-based access control (RBAC) and JWT/OAuth-based secure authentication.
- Encrypted data at rest and in transit must be ensured.
- No card data storage: payment security handled via Stripe.
- Activity logging and audit trails for compliance.

#### Compliance
- The system should align with GDPR data handling principles.
- Ensure SOC-2 readiness.
- PCI-DSS compliance through Stripe for payment processing.
- Development should include Privacy Policy and Terms Enforcement.
- Clear data retention and deletion policies need to be implemented.

#### Reliability
- The platform will be built as a custom modular monolith to maintain resilience within the budget constraints.
- An append-only audit log table will support data integrity and admin export capability.

#### Scalability
- The architecture must support future scalability needs, including phase-based enhancements and optimizations.
- Background jobs and activities are expected to scale using services like AWS SQS or equivalents.

#### Localization
- Currently, there is no explicit requirement for localization. Assume the platform initially serves the US market. (Assumption)

#### Observability
- Development should include tools for monitoring and logging to track platform performance and user activities.

#### Open Questions
- Are there existing mandates for enterprise SSO integrations such as Okta/SAML, or should defaults be used?
- Is the current role set adequate, or is there a need for additional roles like Support?

#### Assumptions
- US-based compliance and localization requirements as primary focus.
- The managed queue for background tasks implies AWS SQS or similar for industry-standard support.


# Integrations and Data

## Integrations

- **Stripe Billing/Checkout**: Used for managing payments and subscriptions. Key functionalities include:
  - Subscription setup and management
  - One-off purchases
  - Invoice generation and management
  - Handling refunds and chargebacks

- **Stripe Connect**: Facilitates teacher payouts. Key components include:
  - Earnings tracking
  - Payout processing and synchronization

- **Auth0 or Clerk**: Provides authentication with RBAC (Role-Based Access Control). Features include:
  - User authentication (JWT/OAuth-based)
  - Role management for Admin, Teacher, and Student

- **AWS S3-Compatible Storage**: Used for storing video files and other media uploads.

- **Background Jobs/Queue (SQS or Managed Equivalent)**: Handles asynchronous operations such as:
  - Payout synchronization
  - Email dispatching
  - Certificate generation
  - Webhook processing

## Key Data Entities

- **User**: Represents individuals interacting with the platform, characterized by roles (Admin, Teacher, Student).

- **Course**: Contains information about course content, including modules, lessons, quizzes, and assignments.

- **Subscription**: Details user subscriptions to courses, including pricing and renewal terms.

- **Payment**: Captures transaction data related to payments and refunds.

- **Payout**: Represents financial transfers made to teachers.

- **Certificate**: Tracks completion certificates issued upon course completion and includes public verification functionality.

- **Audit Log**: Maintains records of user activities for compliance and security audits.

## Data Flow Notes

- **User Authentication**: Managed via Auth0/Clerk, allowing secure login and role assignment.

- **Payment Processing**: Initiated by user actions (subscriptions, purchases) and processed through Stripe Billing/Checkout.

- **Payouts Synchronization**: Managed using Stripe Connect and a background jobs queue to ensure timely disbursement to teachers.

- **Content Delivery**: Courses and media files stored in S3-compatible storage are served to users.

- **Compliance and Auditing**: Activity logging ensures all user actions are tracked for audit trails, supporting GDPR and SOC-2 readiness.

## Open Questions

- Is there a need for additional integrations, especially concerning compliance requirements (e.g., SOC 2, GDPR mandates)?
  
- Are there any other external systems that need to be considered for future phases?

- How frequently are payouts synchronized, and is real-time synchronization required?

- With regards to SSO, which enterprise SSO mandates (e.g., Okta/SAML) are necessary for implementation?


## Constraints and Assumptions

### Constraints
- **Budget and Timeline:**
  - Phase 1: $40k–$50k budget, 14–16 weeks.
  - Phase 2: 8–12 weeks for enhancements.

- **Platform and Tech Stack:**
  - Frontend: Next.js.
  - Backend: NestJS modular monolith.
  - Database: Postgres.
  - Storage: S3-compatible for video/files.
  - Authentication: Managed by Auth0 or Clerk with RBAC.
  - Payments: Stripe Billing/Checkout and Stripe Connect.
  - Background Tasks: SQS or equivalent service.
  - Hosting: AWS (ECS/Fargate) or Vercel.

- **Compliance and Security:**
  - US compliance includes GDPR-aligned data handling, SOC-2 readiness, and PCI-DSS compliance via payment providers.
  - Secure authentication (JWT/OAuth-based).
  - Encrypted data at rest and in transit.
  - Activity logging and audit trails.
  - Role-based permissions and secure payment handling (no card data storage).

- **Roles and Responsibilities:**
  - Primary roles: Admin, Teacher, Student.
  - Admin oversees governance, compliance, monetization, quality control.
  - Teachers create content and manage enrollments.
  - Students consume content and manage learning.

### Assumptions
- The existing role set (Admin, Teacher, Student) is sufficient to cover all platform functions. This is subject to review if a Support role is necessary.
- Compliance alignment with HIPAA/PCI and enterprise SSO mandates (e.g., Okta/SAML) will be evaluated and integrated as needed.
- The mid-range budget implies a focus on maintainability; adjustments for future scalability are included in Phase 2 planning.
- All compliance policies and enforcement mechanisms are assumed to be fully documented and operational by the end of Phase 1.


# Open Questions

## P0

- **Compliance Obligations Review**
  - What are the necessary compliance standards beyond SOC 2, GDPR, HIPAA/PCI, and how do these impact implementation?
  - Owner: Product

- **Role Coverage**
  - Does the current role set (Admin/Teacher/Student) adequately cover all operational needs, or should we consider adding a Support role?
  - Owner: Founder

## P1

- **Auth Provider Decision**
  - Should we finalize on Auth0 or Clerk for authentication/RBAC? What are the specific trade-offs in terms of features, cost, and complexity?
  - Owner: Engineering

- **Video/File Storage Details**
  - Which S3-compatible object storage provider should be used, considering costs and technical integration?
  - Owner: Engineering

## P2

- **Hosting Strategy**
  - Should the application be hosted on AWS (ECS/Fargate) or Vercel, given budget constraints and expected traffic?
  - Owner: Engineering

- **SSO and Keycloak Integration**
  - Is there any need for enterprise SSO integration (Okta/SAML), and what would be the impact on timelines and costs?
  - Owner: Product
