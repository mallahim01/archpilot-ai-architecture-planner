# Requirements Document

**Job ID:** `9b007d72-d558-4d19-99cc-a6bf88c8d401`


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


## Overview

The initiative involves creating a comprehensive e-learning platform featuring a custom build utilizing Next.js, NestJS, Postgres, Prisma, managed authentication with Clerk/Auth0, and Stripe Billing. This platform is engineered to serve three primary roles: Admin, Student, and Instructor. It will facilitate course creation, subscription-based access, instructor payout management, and student learning progress tracking.

**Product:**
- Custom stack with Next.js, NestJS, Postgres, and Prisma.
- Subscription features with Stripe Billing.
- Managed auth via Clerk/Auth0.
- Supports course authoring, progress tracking, certifications, and instructor payouts. 

**Target Users:**
- **Admin:** Oversee platform and manage monetization, enrollments, and payouts.
- **Student:** Discover and enroll in courses, track progress, and earn certifications.
- **Instructor:** Create and publish courses, manage performance and earnings.

**Core Value:**
- Centralized platform for creating and accessing educational content.
- Simplifies subscription management and provides flexible payment options.
- Empowers instructors with transparent and manageable earnings tracking.

**Non-goals (if any):**
- No initial support for buying individual courses; focus first on subscription access.
- Alternative fallback stack (WordPress) noted but not prioritized.

**Open Questions:**
- Should subscriptions unlock all courses on the platform, or a specific subscription catalog?


### Goals and Success Criteria

#### Goals
- Implement a custom platform using the primary tech stack (Next.js, NestJS, Postgres, Prisma).
- Launch an MVP within a 4-month timeline with core functionalities.
- Enable role-based access control (RBAC) for Admin, Student, and Instructor roles.
- Provide subscription-based access with both monthly and annual plans.
- Support individual course purchases (future phase).
- Calculate instructor payouts monthly based on enrollments.
- Develop user interfaces for subscription management, course access, and payment flows.

#### Success Metrics
- Completion of MVP features within the 4-month timeline.
- Successful deployment and integration of primary tech stack components.
- At least 90% uptime of the platform’s services post-launch.
- User adoption rates with at least 100 monthly active users (MAU) post 3 months of launch.
- Successful calculation and distribution of instructor payouts for 90% of enrolled courses.
- Positive user feedback post-launch with a satisfaction survey score above 80%.

#### Acceptance Criteria
- **RBAC Implementation**: Users can perform role-specific actions (administering platform, managing courses, tracking progress).
- **Subscriptions Management**: Users can subscribe, renew, cancel, and manage both monthly and annual plans effectively.
- **Instructor Payouts**: Admin can approve monthly payout runs with accurate balance calculations for enrolled courses.
- **Course Access and Player**: Students can access courses and play content seamlessly without interruptions.
- **Sales and Payment Handling**: Integration with Stripe for seamless transactions and error-free payment processing.
- **Notification System**: Users receive timely and accurate email notifications on subscription and payment changes.
- **4-Month Roadmap Fulfillment**: All critical paths are achieved, and QA processes passed, by end of the timeline.

#### Open Questions
- Should subscriptions unlock all courses on the platform, or only a subscription catalog?


### Scope

#### In Scope
- **Technology Stack**
  - Custom build with Next.js, NestJS, Postgres, Prisma, Clerk/Auth0, Stripe Billing.
  
- **Role Management**
  - Admin, Student, Instructor roles with RBAC implementation.
  
- **Subscriptions**
  - Monthly and Annual subscription plans.
  - Subscriptions initially unlock all courses.
  - Subscription lifecycle management including trial, upgrade, cancel, renew.

- **Course Management**
  - Course authoring and publishing workflow.
  - Student progress tracking.
  - Certificate awarding upon course completion.

- **Monetization and Payouts**
  - Subscription plans and payments managed via Stripe Billing.
  - Instructor payouts based on enrollments: fixed or revenue-share per enrollment.
  - Monthly admin-approved payout runs.

- **User Journeys**
  - Admin: User management, course oversight, monetization controls, enrollment and access management, payout operations, platform monitoring and analytics.
  - Student: Course discovery, subscription management, course player access, assessments, certificate receipt, account management.
  - Instructor: Course creation and publishing, course performance tracking, earnings tracking, profile and payout management.

- **Infrastructure and Integrations**
  - Video streaming via Mux or Cloudflare Stream.
  - Email and notifications via Postmark or SendGrid.
  - Infrastructure support via Vercel, Render/Fly.io, managed Postgres.

- **UI/UX Design**
  - Purchase flows and teacher earnings dashboards.
  
- **Additional Features**
  - Centralized admin system for platform management.
  - Support for email notifications regarding receipts, renewals, cancellations, and payouts.

#### Out of Scope
- **Individual Course Purchases**
  - Considered for a later or optional phase, not included in the initial development.

- **Fallback Tech Stack**
  - WordPress + LearnDash/LifterLMS, custom service for payouts/reporting is not part of the primary development plan.

#### Notes
- The development is to be completed within a 4-month timeline with an estimated budget of $25–50k.
- Budget and timeline constraints are critical; additional features or adjustments should be carefully evaluated against these constraints.

#### Open Questions
- Should subscriptions unlock all courses on the platform, or only a subscription catalog?


### Personas and Roles

| Role       | Description                                                                                     | Key Permissions                                                                                  |
|------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Admin      | Central role managing the platform. Responsibilities include user management, course oversight, and monetization control.                                        | - Manage users (create, update, delete) <br> - Oversee courses <br> - Control monetization and payouts <br> - Enrollment and access management <br> - Platform monitoring and analytics |
| Student    | User who enrolls in and completes courses. Can manage subscriptions and track progress.                                      | - Discover and enroll in courses <br> - Access course player and complete assessments <br> - Manage subscriptions <br> - Receive certificates <br> - Manage account                         |
| Instructor | Educator responsible for course creation and student engagement. Earnings based on course enrollments.                        | - Create and publish courses <br> - View course performance <br> - Track earnings <br> - Manage profile and payout methods                                     |

### Open Questions

- Should subscriptions unlock all courses on the platform, or only a subscription catalog?


# High-level User Journeys

## Admin

1. **User Management**
   - Access admin dashboard.
   - Add, edit, or remove users in the platform.
   - Assign roles to users (Admin, Student, Instructor).
   
2. **Course Oversight**
   - Monitor overall course performance.
   - Review and approve course content before publishing.
   
3. **Monetization Controls**
   - Set up and manage subscription plans (Monthly and Annual).
   - Configure pricing and revenue-sharing options.
   
4. **Enrollment and Access Management**
   - Manage user enrollments and assign course access.
   - Handle access overrides in special situations.
   
5. **Payout Operations**
   - Approve monthly payout runs for instructors based on enrollments.
   - Review instructor earnings calculations.
   
6. **Platform Monitoring and Analytics**
   - Monitor platform usage and performance analytics.
   - Implement security measures and audit logs.
   
7. **Support Flows**
   - Manage customer support requests, including refunds and access issues.

## Student

1. **Discover Courses**
   - Browse and search for courses via catalog.
   - Filter courses based on categories and interests.
   
2. **Manage Subscriptions**
   - Subscribe to plans for platform-level access (Monthly/Annual).
   - Manage subscription options and upgrades.
   
3. **Access Course Player**
   - Access course content through integrated course player.
   - Track progress and complete assessments.
   
4. **Receive Certificates**
   - Earn certificates upon course completion.
   - Download or share certificates.
   
5. **Manage Account**
   - Update personal details and preferences.
   - Manage billing information and view payment history.

## Instructor

1. **Course Creation and Publishing**
   - Access instructor dashboard.
   - Create and submit courses for admin approval.
   
2. **View Course Performance**
   - Monitor enrollment statistics and student progress.
   - Analyze feedback and improve course content.
   
3. **Earnings Tracking**
   - Track earnings based on enrollments.
   - Configure preferred payout methods.
   
4. **Manage Profile**
   - Update profile information and credentials.
   - Customize personal and course-related content. 

## Edge Cases & Exceptions

- **Admin Payout Approval Delay**: If an admin does not approve payouts in the scheduled run, the payout process should be paused until confirmation is received.
  
- **Subscription Expiry and Course Access**: Ensure that after subscription expiry, students can no longer access the locked content unless renewed.

## Open Questions

- Should subscriptions unlock all courses on the platform, or only a subscription catalog? 
- During the trial phase of a subscription, should students have full access to the course content?
- What are the specific criteria for an instructor to submit a course for approval? 

## Assumptions

- Individual course purchases are to be added in a later phase, and current user journeys do not account for this feature yet. 
- Admin role includes the ability to override decisions or errors in any process for immediate correction.


# Functional Requirements

The functional requirements for the platform are grouped by key modules and defined using MUST/SHOULD/COULD tags to indicate their priority and necessity.

## Authentication and Authorization

- **MUST** implement managed authentication using Clerk/Auth0.
- **MUST** support Role-Based Access Control (RBAC) for roles: Admin, Student, Instructor.
- **SHOULD** allow server-side RBAC enforcement for security compliance.

## Subscription Management

- **MUST** support both Monthly and Annual subscription plans using Stripe Billing.
- **MUST** manage the subscription lifecycle: trial, upgrade, cancel, and renew.
- **COULD** include individual course purchases as a later phase.

### Open Question:
- Should subscriptions unlock all courses or a specific subscription catalog?

## Course Management

- **MUST** enable course creation and publishing workflows for Instructors.
- **MUST** support a discovery feature for Students to find courses via catalog search and filtering.

## Payment and Billing

- **MUST** integrate payments for subscriptions and course purchases via Stripe.
- **MUST** implement a payout system for Instructors, based on enrollments, configurable as a fixed amount or revenue share.
- **MUST** support monthly payout calculations with an admin-approved payout run process.

## Learning Experience

- **MUST** provide a course player for Students.
- **MUST** track Student progress and award certificates upon completion.
- **SHOULD** enable Students to manage their subscriptions and access course content seamlessly.

## Notifications

- **MUST** send email notifications regarding receipts, renewals, cancellations, and payouts via Postmark or SendGrid.

## Admin Capabilities

- **MUST** include user management, course oversight, monetization controls, and enrollment management within the admin dashboard.
- **SHOULD** offer platform monitoring and analytics features for data-driven decision-making.

## Payout and Reporting

- **MUST** calculate Instructor earnings based on enrollment events.
- **MUST** maintain a history of payout cycles and generate basic reports.

## Infrastructure and Tech Stack

- **MUST** build the frontend using Next.js (React) and Tailwind CSS.
- **MUST** implement backend with NestJS (Node/TypeScript) REST API and Prisma ORM.
- **MUST** utilize managed Postgres for the database.

## Storage and Media

- **MUST** store media using S3-compatible storage (e.g., AWS S3) and enable video streaming via Mux or Cloudflare Stream.

## Development Lifecycle

- **MUST** follow a 4-month timeline with specific monthly deliverables focused on foundations, learning experience, monetization, and hardening.
- **SHOULD** address QA, security, legal compliance, and production readiness in the final month before launch.

## Performance and Compliance

- **SHOULD** optimize platform performance and ensure legal compliance with relevant regulations.

## Support and Maintenance

- **COULD** design support flows for handling refunds and access overrides.


# Non-Functional Requirements

### Performance
- Must support up to 2,000 concurrent users to ensure smooth platform operation.
- Response time for all key operations (e.g., course enrollment, payout calculations) should not exceed 500 ms under normal load conditions.
- Video streaming should support adaptive bitrate delivery to ensure optimal user experience across varying network conditions.

### Security
- Implement OAuth2 for secure authentication via Auth0 or Clerk with server-side RBAC.
- Data encryption must be enforced both in transit and at rest for all sensitive information.
- Regular security audits should be scheduled every quarter to identify and rectify vulnerabilities.

### Compliance
- Ensure adherence to GDPR for handling any user data.
- PCI-DSS compliance for all payment-related operations via Stripe.
- Maintain a clear audit trail of all user interactions, course enrollments, and financial transactions.

### Reliability
- Achieve 99.9% uptime for the platform excluding scheduled maintenance.
- Implement failover strategies for essential services using multi-zone deployments where feasible.

### Scalability
- Application and infrastructure must be able to scale horizontally to handle increased load (e.g., during promotions or events).
- Database should be optimized for performance and scalability, accommodating future growth in courses and user base.

### Localization
- Platform must support English as the primary language. Additional languages can be added as a future enhancement.
- Currency settings for course purchases and payouts should accommodate multiple currencies as managed by Stripe.

### Observability
- Implement logging for critical events like user enrollments, login attempts, and payments.
- Utilize monitoring tools such as New Relic or Datadog for tracking system performance metrics and user interactions.
- Set up alerts for unusual spikes in activities or errors exceeding a predefined threshold.

### Open Questions
- Should subscriptions unlock all courses on the platform, or only a subscription catalog? This needs clarification to appropriately tailor access controls.

### Assumptions
- Assumed acceptable database latency of 100 ms for reads and writes.
- Default to Vercel's CDN for efficient content delivery unless specified otherwise.


# Section: Integrations and Data

## Integrations List
- **Auth0/Clerk:** Managed authentication with server-side Role-Based Access Control (RBAC).
- **Stripe Billing:** Manages payments and subscriptions. Utilize Stripe Connect for instructor payouts.
- **AWS S3:** Storage for course content and other static assets.
- **Mux/Cloudflare Stream:** Video streaming services for course delivery.
- **Postmark/SendGrid:** Email services for notifications such as receipts, renewals, cancellations, and payouts.
- **Next.js + NestJS API:** Core applications for frontend and backend logic with REST API.

## Key Data Entities
- **Users:** Roles include Admin, Student, Instructor. Users can manage their accounts, subscriptions, and access courses.
- **Courses:** Attributes include course details, content, author, enrollment status, and progress tracking.
- **Subscriptions:** Details of active, trial, or historical subscriptions, linked to user accounts, and associated with payment plans.
- **Enrollments:** Tracks student enrollment in courses, including progress and completion status.
- **Transactions:** Logs of payments, refunds, and payouts.
- **Payouts:** Instructor earnings calculations and history based on student enrollments, with admin-approved payout runs.

## Data Flow Notes
- **User Authentication and Access:**
  - Authenticated via Auth0/Clerk with roles managed server-side.
  - Users authenticated will have access to courses and subscription management.
  
- **Course Access and Enrollment:**
  - Students can subscribe for course access via Stripe Billing.
  - Enrollment data captured per course, linked with user progress and certification eligibility.
  
- **Payment and Subscription Management:**
  - Payments processed through Stripe Billing, includes handling subscription lifecycle (trial, upgrade, renewal, cancellation).
  - Payouts calculated monthly and initiated through Stripe Connect, requiring admin approval.

- **Content Management:**
  - Course content uploaded and managed via S3, streamed via Mux/Cloudflare.
  - Instructors can create and publish courses, manage course content through the platform interfaces.

- **Notifications:**
  - Transactional emails sent via Postmark/SendGrid for subscription confirmations, payment receipts, and other notifications.

## Open Questions
- Should subscriptions unlock all courses on the platform, or just a specific subscription catalog?
- Clarification needed on fallback strategy involving WordPress + LearnDash/LifterLMS stack integration. Under what circumstances should this be considered or tested?
- How should individual course purchases be integrated with existing subscription logic?

## Assumptions
- It is assumed all features and roles will be available from launch, despite the optional phase consideration for individual course purchases.
- Instructor payouts are presumed to employ a fixed amount or revenue-sharing model as detailed, pending further refinement based on pilot or early-launch feedback.


### Constraints and Assumptions

#### Constraints
- **Budget:** 
  - Confirmed budget range between $25–50k.

- **Timeline:** 
  - Project timeline for MVP is set at 4 months with specific monthly goals.

- **Platform:**
  - Primary tech stack is custom-built using:
    - Frontend with Next.js (React) + Tailwind.
    - Backend with NestJS (Node/TypeScript) REST API.
    - Database with Postgres (managed) + Prisma ORM.
    - Authentication via Auth0 or Clerk.
    - Payments via Stripe Billing and potential use of Stripe Connect for instructor payouts.
    - Storage on S3-compatible platforms, video streaming with Mux or Cloudflare Stream.
    - Email and notifications via Postmark or SendGrid.
    - Infrastructure includes hosting via Vercel for frontend, Render/Fly.io for API, managed Postgres.
  - Fallback stack: WordPress + LearnDash/LifterLMS + Stripe add-ons.

- **Compliance:**
  - Legal compliance integrated in the final month as part of production readiness.

- **Payouts and Subscriptions:**
  - Subscriptions initially unlock all courses.
  - Instructor payouts are based on enrollments—either a fixed amount or revenue-share per enrollment.

#### Assumptions
- **Subscription Model:**
  - Initial subscriptions unlock all courses, pending further clarification (Open Question remains on whether it should be all courses or a catalog).

- **User Roles:**
  - Initial launch roles include Admin, Student, and Instructor.

- **Feature Roadmap:**
  - The platform will support both subscription-based access and individual course purchases at a later phase.

- **Instructor Payouts:**
  - Calculations and runs for instructor payouts will occur monthly with an admin approval step.

#### Open Questions
- **Subscription Access:**
  - Should subscriptions unlock all courses on the platform, or only a specific subscription catalog?


# Open Questions

## P0 (Critical)
1. **Subscription Access:**
   - Should subscriptions unlock all courses on the platform, or only a subscription catalog?
   - **Owner:** Product

2. **Instructor Payout Method:**
   - Should the instructor payout be a fixed amount per enrollment or a revenue share? This impacts both business logic and UI design.
   - **Owner:** Founder

## P1 (High Priority)
1. **Fallback Tech Stack:**
   - Is the fallback stack (WordPress + LearnDash/LifterLMS) being actively considered if any critical issue arises with the primary stack? What criteria will trigger this fallback?
   - **Owner:** Engineering

2. **Individual Course Purchases:**
   - Given individual course purchases are considered a later phase, should the initial MVP leave hooks for easy integration for this functionality?
   - **Owner:** Engineering

## P2 (Medium Priority)
1. **Instructor Earnings Dashboard:**
   - What specific metrics or data should the teacher earnings dashboard display beyond basic payouts and enrollments?
   - **Owner:** Product

2. **Support for Refund and Access Override Flows:**
   - Should support flows like refunds and access overrides be part of the MVP or handled in a later phase?
   - **Owner:** Product

3. **Streaming Service Choice:**
   - Between Mux and Cloudflare Stream, which should be preferred for video streaming, considering factors like cost and scalability?
   - **Owner:** Engineering
