# Requirements Document

**Job ID:** `579f622a-bbbf-4887-a082-62f87090f9ad`


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

The system under development is a custom Learning Management System (LMS) and e-commerce platform designed for both web and mobile applications, targeting students and instructors primarily. It is built to support iOS and Android using React Native (Expo) with an API-first approach, creating a seamless and consistent experience across devices. The platform emphasizes hybrid monetization, offering subscriptions, a la carte purchases, and a revenue share or per-enrollment payout model for instructors.

**Product:**
- Multi-platform LMS and e-commerce platform
- Supports both web and mobile (iOS/Android)
- Built with React Native, Next.js, and NestJS or AWS Lambda

**Target Users:**
- Students
- Instructors (Teachers)
- Admins

**Core Value:**
- Centralized learning management with flexible monetization
- Simplified instructor payouts based on enrollments
- Unified content delivery and management for all user roles

**Non-goals:**
- Hard 'native-only' app features are not prioritized unless specified
- Avoid standalone web and mobile products by sharing APIs and components

**Open Questions:**
- Are there any specific 'native-only' requirements that need to be considered?
- Should WordPress or existing platforms be considered for custom vs. custom build?
- Does an active subscription unlock all courses, or is access restricted to a subset?


## Goals and Success Criteria

### Goals
- Develop a system supporting both iOS and Android platforms using a single codebase (React Native).
- Implement a custom API-first strategy to enable shared web and mobile app development.
- Create a robust e-commerce and LMS system with multi-instructor capabilities and a hybrid monetization model.
- Support subscription-based and a la carte payments for content access.
- Ensure seamless instructor payout functionality based on enrollments.
- Deliver the project within a budget of $25k–$50k and a timeline of 4 months.

### Success Metrics
- **Platform Compatibility**: Successful deployment on both iOS and Android with shared API/TypeScript components.
- **Budget & Timeline Adherence**: Completion within the defined budget and 4-month timeline.
- **User Engagement**: X% increase in user engagement via subscriptions and individual course purchases.
- **Monetization Effectiveness**: X% growth in monthly revenue through subscription and one-off purchases.
- **Instructor Satisfaction**: Achieve an instructor satisfaction score of 80% or higher regarding payout processes.
- **System Stability**: Maintain a system uptime of 99.9% post-launch.

### Acceptance Criteria
- The mobile app is operational and consistent in functionality with the web application.
- Subscriptions provide access to all courses unless specified otherwise.
- Users can purchase courses individually, supported by a flexible data model.
- Instructor payout mechanisms function as per the revenue share or per-enrollment model.
- All key product modules (Course authoring, Content delivery, Learning tracking, etc.) are fully operational.
- Subscription management, including lifecycle and entitlements, is effectively implemented.
- Admin functionalities like user management, course moderation, and payout management are accessible and operational.

### Open Questions
- Is there a requirement for any 'native-only' features, or will standard streaming + progress + certificates suffice?
- Is there a preference for using existing platforms (e.g., WordPress) to avoid custom development?
- Should an active subscription grant access to all courses or only to a subset of courses?

### Assumptions
- The standard web and mobile app experience will adequately meet user expectations without specific native-only features.
- Subscriptions are initially assumed to unlock all course content unless otherwise clarified.


## Scope

### In Scope

- Support for both iOS and Android platforms using React Native (Expo).
- API-first development strategy to support web and mobile applications simultaneously.
- Custom build on a managed LMS/e-commerce backbone for multi-instructor support.
- Implementation of a hybrid monetization model:
  - Monthly and annual subscriptions.
  - A la carte payments for individual courses.
- Subscription entitlements granting access to all courses initially.
- Instructor payouts based on enrollment counts:
  - Revenue share or per-enrollment model.
- Payment processing using Stripe for subscriptions and one-time purchases.
- Core product modules:
  - Course authoring, content delivery, access & monetization, learning tracking, certification, payouts, and admin system.
- High-level interfaces and roles:
  - Student, Instructor (Teacher), Admin.
  - Shared API and TypeScript types/components for consistency.
- Key areas:
  - Public (Landing, course catalog/browse, course detail, pricing).
  - Auth (Signup/login, verify email, forgot password).
  - Student (Dashboard, course player, certificates, billing/subscription).
  - Instructor (Dashboard, course builder/manage, analytics, payout history).
  - Admin (Manage users/roles, courses/moderation, subscription plans, payouts, reports).
- Progress tracking, certificates, and standard streaming capabilities.

### Out of Scope

- Hard 'native-only' requirements for the mobile application.
- Custom development of platforms other than the custom build.
- WordPress or other non-react platform-based solutions.
- Features beyond the 4-month timeline or $25k-$50k budget limit.

### Notes

- The timeline and budget constraints ($25k-$50k, 4 months) significantly influence the scope. Increased investment could allow for more advanced features or platform expansions.
- Open Questions:
  - Are there any mandatory 'native-only' application requirements?
  - Should a platform like WordPress be considered instead of full custom development?
  - Clarification needed on whether an active subscription unlocks all courses or only a subset.


## Personas and Roles

| Role       | Description                                                                 | Key Permissions                                                                                     |
|------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Admin      | Manages the platform including user roles, courses, content, and monetization.| - Manage users and roles<br>- Oversee courses and content moderation<br>- Configure subscription plans and payouts<br>- Access reports and audit activities                                     |
| Instructor | Creates and manages courses, views analytics, and manages payouts.          | - Create and publish courses<br>- View course-related analytics<br>- Manage payout details and profile                              |
| Student    | Engages with courses, tracks progress, and manages subscriptions.           | - Browse and purchase courses/subscriptions<br>- Access and participate in courses<br>- Track learning progress and obtain certificates<br>- Manage own account and billing information |

### Open Questions
- Are there additional roles needed beyond Admin, Instructor, and Student?
- Should Students with a subscription always have access to all courses, or only a designated subset?


## High-level User Journeys

### Admin

1. **Login and Access Dashboard**
   - Admin logs into the system using credentials.
   - Access main dashboard for system overview.

2. **Manage Users**
   - Navigate to user management section.
   - Add, edit, or remove users.
   - Assign or update user roles (student, instructor).

3. **Manage Courses/Content**
   - Access course management.
   - Approve or modify course content submitted by instructors.

4. **Monetization and Entitlements**
   - Configure subscription plans and entitlements.
   - Oversee hybrid monetization model (subscriptions, a la carte).

5. **Payments and Payouts**
   - Manage payout schedules and calculations for instructors.
   - Monitor revenue share or per-enrollment payouts.

6. **Audit and Monitoring**
   - Track user activity and system health.
   - Generate reports for system performance.

7. **Manage Subscription Plans**
   - Set pricing and access rules for subscriptions.
   - Update subscription details as needed.

### Student

1. **Sign Up and Verify Account**
   - Register on the platform via web or app.
   - Confirm email to activate account.

2. **Browse and Purchase**
   - Explore course catalog.
   - Purchase access via subscription or one-off payment.

3. **Access Learning**
   - Use dashboard to access enrolled courses.
   - Engage with the course player for content delivery.
   - Track progress with built-in tools.

4. **Certification**
   - Complete course requirements.
   - Download or share completion certificates.

5. **Manage Account and Billing**
   - Update personal information and preferences.
   - Monitor billing details and subscription status.

### Instructor

1. **Create and Manage Courses**
   - Develop course content using course builder tools.
   - Submit courses for admin approval.

2. **Course Publishing**
   - Once approved, publish courses to the catalog.
   - Monitor course analytics post-launch.

3. **Access Dashboard and Analytics**
   - View student enrollments and engagement metrics.
   - Analyze performance data and reporting tools.

4. **Manage Payouts**
   - Track enrollment-based earnings.
   - Review payout history and upcoming disbursements.

5. **Profile Management**
   - Update instructor profile and settings.

### Edge Cases & Exceptions

- **Subscription Uncertainty**
  - Open Question: When a user has an active subscription, should they get access to all courses or only a subset?

- **User Role Ambiguity**
  - Open Question: Clarification needed on role-based restrictions for content access and system navigation.

- **Monetization Models**
  - Assumption: Default subscription grants access to all courses unless specified otherwise.

### Open Questions

- Are there any hard 'native-only' requirements or is standard streaming + progress + certificates app sufficient?
- Clarification on preference for custom build versus using an established platform like WordPress for certain functionality.


# Functional Requirements

## Platform Support
- **MUST** support both iOS and Android platforms using React Native (Expo).
- **MUST** use a shared API to ensure consistency between web and mobile applications.

## Development Strategy
- **MUST** implement a custom API-first development strategy to support both web and mobile platforms.

## Role Management
- **MUST** define and manage roles including Admin, Student, and Instructor.
- **MUST** implement role-based access control for all defined roles.

## Course Management
- **MUST** allow Instructors to create, publish, and manage courses.
- **SHOULD** support a flexible data model for potential addition of individual course purchases.

## Monetization and Payments
- **MUST** support hybrid monetization models, including:
  - Monthly and annual subscriptions.
  - A la carte payments for individual courses.
- **MUST** enable Subscription to unlock all courses.
- **MUST** calculate Instructor payouts based on enrollment, structured as revenue share or per-enrollment.
- **MUST** use Stripe for handling payments.
- **COULD** allow for individual course purchases in the future.

## Content Delivery
- **MUST** provide standard streaming capabilities with options to integrate with S3, CloudFront, and Mux/Vimeo.
- **SHOULD** include a course player for Students.

## Learning Tracking and Certification
- **MUST** track learning progress and issue certificates upon course completion.

## Admin Functions
- **MUST** include functionality for Admins to manage:
  - Users and roles
  - Courses and content moderation
  - Subscription plans and payouts
  - Reporting and auditing

## User Account Management
- **MUST** enable Students to manage accounts, subscriptions, and billing information.
- **MUST** provide authentication and RBAC using Supabase Auth or Auth0.
  
## Communication and Notifications
- **MUST** utilize Postmark or SendGrid for email and notification services.

## UI/UX
- **MUST** include the following high-level screens/pages:
  - Public: Landing, course catalog/browse, course detail, pricing.
  - Auth: Signup/login, verify email, forgot password.
  - Student: Dashboard, course player, certificates, billing/subscription.
  - Instructor: Dashboard, course builder/manage, analytics, payout history.
  - Admin: Manage users/roles, courses/moderation, subscription plans, payouts, reports.
  
## Technology Stack
- **MUST** include the following technologies:
  - Next.js for the frontend
  - NestJS or AWS Lambda for backend/API
  - PostgreSQL as the database
  - S3 and CloudFront for storage and media delivery

## Open Questions
- Are there any hard 'native-only' requirements beyond the current scope?
- Is there a preference for a custom build versus using a platform like WordPress?
- Should active subscriptions provide access to all courses, or just a subset?


# Non-Functional Requirements

## Performance
- The system must provide a seamless user experience on both iOS and Android devices.
- Ensure API response times are optimized to support real-time interactions, particularly for course content streaming and progress tracking.
- React Native and Next.js should be configured to ensure optimal performance on mobile and web platforms, respectively.

## Security
- Implement authentication and role-based access control using Supabase Auth or Auth0 to ensure secure access for Admin, Student, and Instructor roles.
- Ensure all data transmissions are encrypted using SSL/TLS.
- Payment processing via Stripe must comply with PCI DSS standards.

## Compliance
- **Assumption**: The system must comply with GDPR regulations for handling personal data as it may cater to EU residents.
- Ensure all third-party service integrations (e.g., Stripe, Supabase, Auth0) comply with relevant industry standards.

## Reliability
- Use AWS infrastructure (e.g., RDS, Lambda) to provide high availability and minimize downtime.
- Implement regular data backups for PostgreSQL to prevent data loss.
- Design the system to handle spikes in traffic, especially during course enrollments and streaming.

## Scalability
- The architecture must support scaling horizontally to accommodate increased user load without degrading performance, particularly in content delivery and user management.
- Use S3 and CloudFront or Mux/Vimeo for scalable content storage and streaming.

## Localization
- **Assumption**: The system should be designed to support multiple languages to expand into different regions.
- Ensure the codebase supports localization frameworks for dynamic content adaptation.

## Observability
- Implement monitoring tools for real-time tracking of system performance and user activity.
- Set up alerting for anomalies in API usage, database interactions, and front-end load times.

## Open Questions
- Confirmation is needed on whether there are any unique localization requirements for specific regions.
- Should there be specific compliance considerations beyond GDPR, such as CCPA for Californian users?
  
These non-functional requirements aim to ensure that the platform operates efficiently, securely, and can scale and localize to meet business and technical demands.


# Integrations and Data

## Integrations List

- **Authentication and Authorization**
  - Supabase Auth or Auth0 for handling authentication and role-based access control (RBAC).

- **Payments**
  - Stripe for processing payments, including subscriptions and one-time purchases.

- **Content Storage and Streaming**
  - Amazon S3 + CloudFront or Mux/Vimeo for content storage and streaming.

- **Email and Notifications**
  - Postmark or SendGrid for sending emails and notifications.

- **Admin Tools**
  - Retool or a lightweight internal admin built on Next.js.

## Key Data Entities

- **User**
  - Roles: Admin, Student, Instructor.
  - Attributes: user profile, authentication details, subscription status.

- **Course**
  - Attributes: course details, pricing, access entitlements.

- **Subscription**
  - Attributes: type (monthly, annual), status, linked user.

- **Payment**
  - Attributes: amount, status, related user/course, transaction details.

- **Instructor Payout**
  - Attributes: enrollment count, payment model (revenue share, per-enrollment).

- **Content**
  - Attributes: media files, metadata, streaming links.

## Data Flow Notes

- **Authentication Flow**
  - Users authenticate using Supabase Auth or Auth0.
  - User roles are checked for access permissions.

- **Payment Processing Flow**
  - Transactions are initiated via Stripe.
  - Payment records are created and linked to users and courses for entitlements.

- **Content Access Flow**
  - Users access content stored on S3 or streamed via CloudFront/Mux/Vimeo.
  - Access is verified against user entitlements.

- **Instructor Payout Flow**
  - Enrollment data is collected and processed.
  - Payouts are calculated based on defined models and enrollment counts.

## Open Questions

1. Are there additional external systems or integrations required that are not listed?
2. How frequently should instructor payout cycles be executed?
3. Is there a need for additional data privacy or compliance integrations (e.g., GDPR tools)?
4. Confirmation needed on if the app requires specific native-only integrations or if current integrations suffice.
5. Should any additional event-driven integrations be considered, such as webhooks for real-time updates?


### Constraints and Assumptions

#### Constraints
- **Budget and Timeline:**
  - The development needs to fit within a $25k–$50k budget.
  - The project must be completed within a 4-month timeline.

- **Platform Requirements:**
  - Support for both iOS and Android platforms through React Native (Expo).
  - Shared API and types are required across web and mobile applications to ensure consistency.
  - Use of the same API for both the web application and the React Native app is necessary.

- **Technical Stack:**
  - Frontend: Next.js.
  - Backend/API: NestJS or AWS Lambda.
  - Database: PostgreSQL (options include Supabase or AWS RDS).
  - Authentication and RBAC: Supabase Auth or Auth0.
  - Payments: Stripe (supporting subscriptions and one-time purchases).
  - Storage and Media Delivery: S3 and CloudFront, with optional integration of Mux/Vimeo for video streaming.
  - Email/Notifications: Postmark/SendGrid.
  - Admin Tools: Retool or a lightweight admin in Next.js.

- **Product Features:**
  - Implementation of an API-first development strategy to support both web and mobile without maintaining two distinct products.
  - Roles are restricted to Admin, Student, and Instructor.

- **Monetization:**
  - Hybrid model with monthly and annual subscriptions, plus a la carte course payments.
  - Subscription initially provides complete access to all courses.

- **Instructor Payouts:**
  - Payout calculations based on enrollment counts, structured either as a revenue share or per-enrollment model.

#### Assumptions
- **Platform and Tech Stack:**
  - It is assumed that there are no hard 'native-only' requirements, allowing for a standard streaming, progress tracking, and certificate model.

- **Monetization:**
  - Assumed that the data model is flexible enough to allow for potential future changes enabling individual course purchases.

- **Access and Entitlements:**
  - Assumed that when a user has an active subscription, they will have access to all courses, unless otherwise specified.

#### Open Questions
- Are there any specific access restrictions or course subsets for active subscribers?
- Is there a preference for avoiding custom development by using platforms like WordPress, or is a custom build necessary?


### Open Questions

#### Priority: P0

1. **Subscription Access Scope**
   - **Question:** When a user has an active subscription, should they have access to all courses, or is access limited to a subset?
   - **Owner:** Product

2. **Native-Only Requirements**
   - **Question:** Are there any specific 'native-only' requirements that must be fulfilled, or is a standard streaming + progress + certificates app sufficient?
   - **Owner:** Founder

#### Priority: P1

1. **Custom vs. Platform Development**
   - **Question:** Is there a preference for avoiding custom development in favor of using a platform like WordPress, or should we proceed with a complete custom build?
   - **Owner:** Product

#### Priority: P2

1. **Monetization Options and Flexibility**
   - **Question:** Should the platform support further monetization options beyond the currently defined monthly and annual subscriptions, plus a la carte payments?
   - **Owner:** Product

2. **Instructor Payout Model Clarification**
   - **Question:** Can the instructor payout model be clarified further, particularly the revenue share vs. per-enrollment model?
   - **Owner:** Product/Engineering

3. **Tech Stack Finalization**
   - **Question:** Are there any specific non-functional requirements (e.g., scalability, performance) that may impact the choice between NestJS and AWS Lambda for the backend?
   - **Owner:** Engineering

#### Assumptions

- **Default Subscription Access:** It is assumed that a subscription will initially unlock all courses for complete access unless specified otherwise.
- **Technology Stack Configuration:** The tech stack is assumed to be confirmed as listed, with options for slight alterations as necessary.

These open questions need to be addressed to finalize the requirements document and proceed with development planning.
