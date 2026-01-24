# Requirements Document

**Job ID:** `d554abbd-7832-4a70-a4c5-dede28f25726`


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

We are building a comprehensive educational platform designed to facilitate seamless learning experiences through both web and mobile applications. This platform serves students, instructors, and administrators, offering a broad range of functionalities tailored to each user group. By integrating a modern tech stack, including React Native for the mobile app and Next.js for the web interface, the platform aims to provide a robust, scalable solution that meets the diverse needs of its users.

### Product
- **Student Mobile Application (v1):** Focused on providing core learning functionalities such as browsing, purchasing courses, course playback, and tracking progress.
- **Web Application:** Tailored for instructors and administrators, featuring course management, analytics, enrollments, and payout management.
- **AI Learning Assistant:** Integrated into both platforms to enhance the learning experience.

### Target Users
- **Students:** Access courses on iOS and Android, learn anytime, and track their progress and achievements.
- **Instructors:** Manage courses, analyze enrollments, and process payouts through the web application.
- **Administrators:** Oversee platform operations, manage user roles, and handle subscription and payout configurations.

### Core Value
- **Comprehensive Learning Experience:** Enable students to learn efficiently through structured courses and AI assistance.
- **Flexible Monetization:** Offer a hybrid model of subscriptions and one-off purchases to maximize revenue potential.
- **Scalability and Robustness:** Built on a modern tech stack, ensuring long-term scalability and operational efficiency.

### Non-goals
- **Limited Mobile Features for Instructors/Admins (v1):** Initial release will focus solely on student functionalities for mobile applications.
  
### Open Questions
- Should the mobile apps have full feature parity with the web for instructor/admin roles?
- Will subscriptions unlock the entire platform or be tied to individual courses/instructors?

### Assumptions
- Default subscription model includes monthly and annual options granting access to a defined range of courses.


### Goals and Success Criteria

#### Goals
- Develop a custom learning management system with a shared backend to avoid platform limitations.
- Launch both student-only mobile and instructor/admin web applications within 8 months.
- Ensure cross-platform availability on iOS and Android for student mobile use.
- Integrate an AI learning assistant across web and mobile applications.
- Build a scalable platform that accommodates multiple instructors and role-based access control.

#### Success Metrics
- Achieve project delivery within the $50k–$80k budget.
- Launch student mobile and web applications on schedule within 8 months.
- Attain seamless functionality for subscription and one-off purchase monetization strategies.
- Ensure integration success for Stripe and Stripe Connect, enabling subscription management and instructor payouts.
- Implement cross-platform AI functionality with an OpenAI or Anthropic API.
- Establish smooth role-based access for students, instructors, and admins with Clerk/Auth0.

#### Acceptance Criteria
- Functional mobile applications for students available on both iOS and Android, supporting core features such as browse, purchase, course player, progress, certificates, and billing.
- Web application for instructors and admins operational with dashboards, course builder, analytics, and payout management.
- Successful implementation of payments and entitlements using Stripe APIs.
- Role-based access control efficiently managed with Clerk/Auth0 across the platform.
- AI learning assistant operational and accessible within both web and mobile applications.
- Every transaction, including subscriptions, purchases, refunds, and payouts, is properly recorded and managed via the backend.
- Admin controls are fully functional for managing subscriptions, courses, and payout schedules.

#### Open Questions
- Should mobile apps achieve full parity with instructor/admin roles in the future iterations, or maintain student-centric functionality?
- What model of subscription should be prioritized: subscription to the entire platform or individual teachers/courses?


### Scope

#### In Scope
- **Mobile and Web Applications**  
  - Development of a student-only mobile app for iOS and Android.
  - Web applications for instructors and admins.

- **Core Features**
  - Role-based access control.
  - Catalog with search and filtering.
  - Payment processing for subscriptions and one-off purchases.
  - Entitlements to verify user access to courses.
  - Course delivery, including video/file hosting and lesson completion tracking.
  - Certificate generation and verification.
  - Instructor payout ledger based on enrollments.
  - Administrative controls for managing subscriptions, payouts, and platform settings.
  
- **Technology Stack**
  - **Mobile App**: React Native with TypeScript.
  - **Web App**: Next.js with TypeScript.
  - **Backend API**: NestJS with TypeScript.
  - **Database**: PostgreSQL.
  - **Auth/RBAC**: Clerk or Auth0.
  - **Payments**: Stripe (for payments) and Stripe Connect (for instructor payouts).
  - **Content Delivery**: S3-Compatible storage and CloudFront CDN.
  - **Background Tasks**: Redis and BullMQ.
  - **Email Notifications**: Postmark or SendGrid.
  - **AI Learning Assistant**: Integration as a separate service, using APIs like OpenAI or Anthropic.

- **Monetization**
  - Platform subscriptions (monthly and annual).
  - One-off course purchases.
  - Instructor payouts based on enrollment counts.

- **Timeline and Budget**
  - Fit within the $50k–$80k budget.
  - Achieve launch within 8 months.

#### Out of Scope
- **Full Mobile Parity for Instructors/Admins**  
  - Instructor and admin functionalities on mobile are not included in v1.

- **Unconfirmed Subscription Model**
  - Decision pending on whether subscriptions are for the entire platform or specific courses/teachers.

#### Notes
- **Dependencies on Budget/Timeline**  
  - A fallback option exists: Platform LMS (e.g., Thinkific/Teachable) with light custom web/admin and minimal mobile companion, in case of time/scope constraints.
  
- **Open Questions**
  - Decision needed on the subscription model: platform-wide versus individual teacher/course subscriptions.


## Personas and Roles

| Role       | Description                                                                                         | Key Permissions                                                                                                                                                                    |
|------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Student    | Users who purchase and engage with courses on the platform, using the mobile app.                   | - Access course catalog and search/filtering<br>- Purchase courses and subscriptions<br>- Access purchased courses and eligible subscriptions<br>- Track progress and obtain certificates |
| Instructor | Course creators who manage and sell their content on the platform via the web application.          | - Build and manage courses<br>- View enrollments and analytics<br>- Access instructor payouts and manage profile<br>- Engage with course content creation tools                       |
| Admin      | Platform administrators responsible for overall management and oversight via the web application.   | - Manage users and roles<br>- Approve and moderate courses<br>- Oversee subscriptions, orders, and refunds<br>- Configure payout controls and platform settings<br>- Generate reports  |

### Open Questions

- Should mobile apps have complete parity with web roles for instructors and admins, or is a user-focused mobile experience acceptable for v1?
- How should student subscriptions be structured? Is it subscription access to the entire platform or individually for each teacher/course?

### Assumptions

- Role-based access control will use either Clerk or Auth0 for authentication, with 3 fixed roles as detailed above.
- Students will initially only have access via a mobile app, while instructors and admins will access the platform through the web application.


# High-level User Journeys

## Student User Journey

1. **Account Creation and Authentication**
   - Download and install the mobile app on iOS or Android.
   - Sign up using email or third-party authentication (e.g., Google, Facebook).
   - Complete email verification process if required.

2. **Browsing Courses**
   - Open the app and access the course catalog.
   - Use search and filter functions to discover courses.
   - View course details including syllabus, instructor information, and reviews.

3. **Course Enrollment**
   - Choose between subscribing to the platform or purchasing a course (Assumption: Both options are visible).
   - For subscriptions, select a Monthly or Annual plan.
   - Complete purchase via Stripe integration.
   - Receive confirmation email.

4. **Learning and Course Interaction**
   - Access enrolled courses from the Dashboard or My Courses section.
   - Use the course player to view video content or access downloadable materials.
   - Track lesson completion and interact with quizzes and assignments.

5. **Progress and Certification**
   - View progress and completion status within courses.
   - Upon course completion, receive a digital certificate.
   - Certificates are verifiable via a unique code.

6. **Billing and Account Management**
   - Manage subscription and purchase history.
   - Update billing information and view payment receipts.
   - Option to cancel or switch subscription plans.

7. **Edge Cases & Exceptions**
   - **Failed Payment**: Retry payment process or update payment details.
   - **Subscription Expiry**: Access becomes restricted; renew subscription to continue course access.
  
## Instructor User Journey

1. **Account Creation and Profile Setup**
   - Access the web application.
   - Sign up and complete instructor verification process (may include identity verification).

2. **Course Creation and Management**
   - Navigate to Course Builder to create new courses.
   - Upload course content, including videos and documents.
   - Set pricing, enrollment caps, and other course settings.

3. **Enrollment and Analytics**
   - Monitor student enrollments and progress.
   - Access course analytics and generate reports on student engagement.
   - Adjust course content based on feedback and analytics.

4. **Payouts**
   - Instructor payouts are driven by student enrollments attributed to courses.
   - View payout schedule and related transactions via Stripe Connect.
   - Withdraw available funds based on payout schedule.

5. **Edge Cases & Exceptions**
   - **Content Update Required**: Easily edit or update course content post-publication.
   - **Refund Requests**: Handle student refund requests adhering to platform policies.

## Admin User Journey

1. **Platform Setup and Configuration**
   - Access web application with admin privileges.
   - Configure platform settings including subscription options and pricing schemes.

2. **User and Role Management**
   - Manage roles and permissions using role-based access control (RBAC).
   - Approve or moderate new instructor applications and course submissions.

3. **Subscription and Revenue Management**
   - Define courses eligible for subscription access.
   - Oversee transactions and manage refunds or chargebacks.
   - Configure instructor revenue shares and payout schedules.

4. **Reporting and Analytics**
   - Access platform-wide analytics and generate business reports.
   - Monitor KPIs like user growth, revenue trends, and course performance.

5. **Edge Cases & Exceptions**
   - **Fraudulent Activity**: Detect and manage suspicious activities or transactions.
   - **Platform Downtime**: Implement measures for resolving service disruptions swiftly.

### Open Questions

- **Mobile Parity for Instructors/Admins**: Should future mobile versions include full functionality for instructors and admins?
  
- **Subscription Model for Students**: Do students subscribe to the entire platform or have the option to subscribe to individual courses or instructors?


### Functional Requirements

#### Student Module

- **Mobile Application Access**
  - MUST support iOS and Android platforms.
  - MUST include core student flows: browse, purchase, course player, track progress, certificates, and billing.
  - MUST integrate AI learning assistant as a separate backend service.

- **Course Catalog and Search**
  - MUST allow users to search and filter courses.
  - MUST display course details, pricing, and enrollment options.

- **Course Purchasing and Subscription**
  - MUST support both subscription (monthly, annual) and one-off course purchase models.
  - SHOULD display subscription and purchase options side-by-side unless otherwise prioritized.

- **Course Delivery**
  - MUST integrate video and file hosting for lesson delivery.
  - MUST track lesson completion for progress monitoring.

- **Certificates**
  - MUST generate and verify certificates upon course completion.

- **Notifications**
  - MUST send email notifications for receipts, enrollments, certificates, and payout events.

#### Instructor Module (Web)

- **Course Management**
  - MUST include tools for course building, enrollment tracking, and analytics.
  - MUST support profile and verification processes for instructors.

- **Payout System**
  - MUST calculate instructor payouts based on enrollments for both one-off purchases and subscriptions.
  - MUST integrate with Stripe Connect for payout processing.

#### Admin Module (Web)

- **User and Role Management**
  - MUST support role-based access control with at least 3 fixed roles.
  - MUST provide user management interfaces for admin.

- **Subscription and Payment Management**
  - MUST manage subscriptions, one-off purchases, refunds, and chargebacks.
  - MUST track transactions as ledgered events.

- **Platform Management**
  - MUST define subscription-eligible courses.
  - MUST manage instructor revenue shares and payout schedules.
  - SHOULD include tools for course approval and moderation.

#### Backend and Integrations

- **API**
  - MUST use NestJS and provide shared backend services for both web and mobile applications.

- **Storage and Content Delivery**
  - MUST store and deliver content via S3-compatible storage integrated with CloudFront CDN.

- **Authentication and Authorization**
  - MUST implement using Clerk or Auth0 for authentication and role-based access control.

- **Asynchronous Processing**
  - MUST handle async tasks such as certificate issuance and email notifications using Redis and BullMQ.

- **AI Learning Assistant**
  - COULD use OpenAI or Anthropic as backend service providers.

#### Payment Integration

- **Stripe Integration**
  - MUST support subscriptions and one-off payments via Stripe.
  - MUST manage instructor payouts through Stripe Connect.

#### Open Questions

- Should the mobile application have full feature parity for instructor/admin roles in future versions?
- Will students subscribe to the entire platform or individual instructors/courses?
- Clarification needed on the priority or UI presentation order of subscription versus one-off purchase options.


# Non-Functional Requirements

## Performance
- The application should handle up to 10,000 simultaneous users with minimal latency.
- Response times for API requests should be under 200ms on average.
- The AI learning assistant should provide feedback within 2 seconds.

## Security
- Implement OAuth 2.0 using Auth0 or Clerk for authentication and role-based access control.
- Use HTTPS for all data transmission.
- Store sensitive data such as passwords and payment information securely using encryption mechanisms.
- Regularly conduct security audits and penetration testing.

## Compliance
- Ensure compliance with GDPR and CCPA for handling user data.
- Stripe integration for payments must comply with PCI-DSS standards.

## Reliability
- Achieve 99.9% uptime, excluding scheduled maintenance.
- Implement daily data backups with a retention period of at least 30 days.
- Ensure failover systems are in place to manage API or database failures.

## Scalability
- Design the architecture to accommodate horizontal scaling for both web and mobile components.
- Database should support scaling, potentially using managed services like AWS RDS or Supabase.

## Localization
- Support English for the initial launch with a framework to add additional languages easily.
- Currency support for USD, with future potential for multi-currency readiness.

## Observability
- Integrate logging and monitoring tools like Datadog or New Relic.
- Set up automated alerting for application performance issues and potential downtime.
- Monitor user behavior for continuous improvement opportunities.

## Assumptions
- Assumed availability of a dedicated DevOps team to manage scalability and observability requirements.
- Assumed AI learning assistant integrations will maintain the required performance levels without additional latency.

## Open Questions
- What specific security standards are required for instructor data handling, if different from student data?
- Are there any specific compliance requirements beyond GDPR and CCPA for international markets?
- Should mobile app releases be coordinated with web updates, or are separate release schedules acceptable?


# Integrations and Data

## Integrations List

- **React Native**: Mobile app development for student access.
- **Next.js**: Web application for instructors and administrators.
- **NestJS**: Backend API services.
- **PostgreSQL**: Database management.
- **Stripe**: Payment processing for subscriptions and one-off purchases.
- **Stripe Connect**: Facilitates instructor payouts.
- **S3-compatible Storage + CDN (CloudFront)**: Media streaming and content delivery.
- **Redis + BullMQ**: Handling of asynchronous tasks, including jobs and notifications.
- **Clerk/Auth0**: Authentication and role-based access control.
- **Postmark/SendGrid**: Email communication.
- **OpenAI or Anthropic APIs**: AI learning assistant integration.
- **Firebase Cloud Messaging/APNs**: Push notifications.

## Key Data Entities

- **User Profiles**: Includes students, instructors, and admin roles.
- **Courses**: Details, media content, progress tracking.
- **Enrollments**: Linking students to courses.
- **Subscriptions**: Monthly and annual plans.
- **Transactions**: Recording of all payments and related events.
- **Instructor Payouts**: Ledger for payout calculations based on enrollments.
- **Notifications**: Email and push notifications.
- **AI Interaction Data**: AI learning assistant usage logs.

## Data Flow Notes

- **User Registration and Authentication**:
  - Users register and authenticate via Clerk/Auth0, creating profiles in PostgreSQL.
  
- **Course Catalog and Enrollment**:
  - Courses are stored and retrieved from PostgreSQL, with media delivered via S3/CDN. Students enroll in courses, updating respective tables with transaction data.

- **Subscription and Payment Processing**:
  - Handled by Stripe, with transaction records logged in the database. Subscription data determines access entitlements.

- **Instructor Payouts**:
  - Payouts processed through Stripe Connect, using enrollment data to calculate disbursements.

- **Content Delivery**:
  - Media streamed from S3-compatible storage; progress and completion reported back to the database.

- **AI Learning Assistant**:
  - AI interactions tracked and stored, potentially informed by OpenAI or Anthropic services.

- **Asynchronous Tasks and Notifications**:
  - Redis and BullMQ queue jobs for notifications and payments; Emails sent via Postmark/SendGrid, push notifications via Firebase/APNs.

## Open Questions

1. What specific data is required for interaction tracking with the AI learning assistant?
2. Is there a need to capture course-specific analytics for instructors beyond enrollment numbers?
3. What level of detail is required for instructor payout records in terms of audit and transparency?


## Constraints and Assumptions

### Constraints
- **Budget and Timeline:**
  - Total budget is confirmed at $50k–$80k.
  - Launch target is set for 8 months.

- **Technology Stack:**
  - Approved primary stack includes:
    - **Mobile (Student v1):** React Native with TypeScript.
    - **Web (Instructor/Admin):** Next.js with TypeScript.
    - **API:** NestJS with TypeScript.
    - **Database:** PostgreSQL.
    - **Auth/RBAC:** Clerk or Auth0.
    - **Payments:** Stripe for subscriptions and one-off payments, Stripe Connect for instructor payouts.
    - **Content Delivery:** S3-compatible object storage and CDN (CloudFront).
    - **Jobs and Notifications:** Redis with BullMQ (asynchronous tasks), Postmark/SendGrid (email).
    - **AI Learning Assistant:** Integration possibly using OpenAI or Anthropic APIs.

- **Platform Compliance:**
  - The application must be available on both iOS and Android.

### Assumptions
- **Fallback Options:**
  - If time/scope constraints arise, consider a platform LMS (Thinkific/Teachable) with light custom web/admin and minimal mobile companion.

- **Monetization Strategy:**
  - The monetization will follow a hybrid model: platform subscriptions (monthly and annual) and one-off course purchases.

- **Mobile and Web Application Roles:**
  - Initial launch includes a student-only mobile app, while instructors and admin will access the platform via web.
  - Web-first responsive design is prioritized, with a potential for a mobile app later.

- **Feature Parity:**
  - Both web and mobile applications should be ready at launch.
  - Instructor and admin remain web-first at launch.

- **Subscription and Access:**
  - Students may either subscribe to the entire platform or to individual teachers/courses; this decision is pending.

### Open Questions
- Should the mobile apps have full feature parity with the web for instructor/admin roles in v1, or is student-only mobile sufficient?
- Should students subscribe to the entire platform or have multiple subscriptions for individual teachers/courses?


# Open Questions

**P0 (Critical Priority)**

1. **Instructor/Admin Parity on Mobile**
   - Is it necessary for the mobile app to eventually support instructor and admin roles, or is the student-only mobile application sufficient for the foreseeable future?
   - *Owner: Founder/Product*

2. **Subscription Model Clarification**
   - Should students subscribe to the platform as a whole, unlocking all eligible courses, or should they have the option to subscribe to individual teachers/courses, potentially leading to multiple concurrent subscriptions?
   - *Owner: Product*

**P1 (High Priority)**

1. **AI Learning Assistant Integration**
   - Have the precise requirements and specifications for the AI learning assistant been defined, including which APIs (OpenAI, Anthropic, etc.) to utilize?
   - *Owner: Engineering*

2. **Tech Stack Management**
   - Will PostgreSQL be managed by an external provider such as Supabase or AWS RDS, or will it be self-managed?
   - *Owner: Engineering*

**P2 (Normal Priority)**

1. **Subscription Options Display**
   - On the course page, should both the 'Subscribe' and 'Buy this course' options be displayed side-by-side or should one option be prioritized over the other to streamline the user experience?
   - *Owner: Product/UI Expert*

2. **Subscription Entitlement System**
   - What specific rules and logic need to apply within the entitlements system to precisely verify and maintain student access to various courses?
   - *Owner: Engineering*

3. **Instructor Payout Model Details**
   - Besides enrollment counts, will any other metrics or conditions influence instructor payouts, and if so, what are these parameters?
   - *Owner: Founder/Product*
