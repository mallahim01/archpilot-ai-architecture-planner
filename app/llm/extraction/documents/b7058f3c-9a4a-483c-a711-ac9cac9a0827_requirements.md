# Requirements Document

**Job ID:** `b7058f3c-9a4a-483c-a711-ac9cac9a0827`


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

We are building a comprehensive, role-based online teaching and learning platform designed to connect teachers and students through structured digital courses. The platform will provide both web and mobile applications using a unified codebase. The primary technology stack includes Next.js, NestJS, Postgres, Stripe, Supabase Auth or Auth0, and React Native (Expo).

**Product**
- A scalable, production-ready education platform that supports multiple instructors and a growing student base.
- Features include course authoring, content delivery, access and monetization, learning tracking, certification, and payouts.

**Target Users**
- **Students**: Access, browse, and enroll in courses; purchase subscriptions; track learning progress; earn certificates.
- **Instructors**: Create, publish, and manage courses; view analytics; manage payouts based on enrollments.
- **Admins**: Oversee platform operation, manage users and roles, and handle subscription plans and payouts.

**Core Value**
- Offers a hybrid monetization model with subscription options ('all-access pass') and potential for individual course purchases.
- Supports enrollment-based instructor payouts and flexible data model changes.
- Delivers consistent user experience across mobile and web through shared components and API.

**Non-goals**
- Initial build does not require advanced AI-driven recommendations or machine learning analytics.

**Open Questions**
- Clarification needed on whether a user with an active subscription gains access to all courses or just a subset.
- Are there any preferences between AWS vs. GCP, or should this be decided by the development team?


### Goals and Success Criteria

#### Goals
- Develop a scalable and production-ready online education platform.
- Support multiple instructors and a growing base of students.
- Enable monetization from day one through subscription and individual course purchases.
- Provide web and mobile applications with a single codebase for iOS and Android.
- Implement role-based access control for Admin, Instructor, and Student roles.

#### Success Metrics
- Achieve full platform deployment within a budget of $25k–$50k and a timeline of 4 months.
- Ensure consistent user experience across web and mobile through shared API and components.
- Implement subscription models with monthly and annual options, alongside individual course purchases.
- Track instructor payouts accurately based on enrollment counts.
- Ensure system capacity to handle an increasing number of instructors and students.

#### Acceptance Criteria
- Platform must enable instructors to create, publish, and manage courses with analytics capabilities.
- Students should be able to enroll in courses, track progress, obtain certificates, and manage subscriptions.
- Admins must have full control over platform activity, user roles, and content moderation.
- Integration with Stripe for payment processing, supporting both subscriptions and one-time purchases.
- Successful deployment of React Native app for iOS and Android.
- Completion of all specified high-level screens and pages, including dashboards, course catalogs, and payment management.
- Compliance with custom tech stack requirements using Next.js, NestJS, Postgres, Supabase/Auth0, S3/CloudFront, and Stripe.
- Open Questions: Confirm tech stack preferences (AWS vs GCP). Clarify whether active subscriptions unlock access to all courses or if some courses remain pay-per-course.


## Scope

### In Scope

- Development of both web and mobile applications using a custom tech stack:
  - **Web**: Next.js for web application (React)
  - **Backend**: NestJS (Node) API with background jobs
  - **Database**: Postgres (Supabase or AWS RDS)
  - **Auth/RBAC**: Supabase Auth or Auth0
  - **Payments**: Stripe for subscriptions and one-time purchases
  - **Storage/Media**: S3 + CloudFront, with the optional use of Mux/Vimeo for video
  - **Mobile**: React Native (Expo) for iOS and Android

- Implementation of subscription-based monetization features with an 'all-access pass' model including:
  - Monthly and annual subscription plans
  - Individual course purchase capability
  - Enrollment-based instructor payout system

- Platform roles and functionalities:
  - **Admin**: Platform activity tracking, complete control over features, management dashboard
  - **Student**: Browsing, purchasing subscriptions, enrolling in courses, progress tracking, obtaining certificates
  - **Instructor**: Course creation and publishing, viewing analytics, managing payouts
  - **Shared**: Auth, catalog, course player UI, progress tracking, downloads, push notifications

- Implementation of high-level screens and pages such as:
  - Landing, course catalog/browse, course detail, pricing, signup/login, verify email, forgot password, student dashboard, course player, certificates, billing/subscription, instructor dashboard, course builder/manage, analytics, payout history, admin management dashboard

- Admin tools for managing users/roles, courses, subscription plans, payouts, and generating reports.

### Out of Scope

- Integration with external Learning Management Systems (LMS) beyond the provided fallback plan (WordPress + LearnDash)
- Advanced personalization features and AI-driven recommendations
- Non-essential third-party integrations not explicitly stated in the tech stack

### Notes

- The fallback tech stack (WordPress + LearnDash) will only be considered if necessary to compress scope or timeline.
- Budget is set at $25k-$50k with a timeline of approximately 4 months. Adjustments to the scope may be required to maintain budget and timeline constraints.

### Open Questions

- Does the user have any tech stack preferences beyond those listed, such as AWS vs GCP for hosting and services?
- Clarification needed on whether a user with an active subscription gets access to all courses or only a subset, with some remaining pay-per-course?


## Personas and Roles

| Role         | Description                                                                                             | Key Permissions                                                                                                                                          |
|--------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Admin        | Oversees the entire platform, manages users, courses, and subscriptions.                                                                        | - Full control over features<br>- Platform activity tracking<br>- User and role management<br>- Course moderation<br>- Subscription plans management<br>- Payout cycle setup and approvals |
| Student      | Engages with the platform by browsing, purchasing, and enrolling in courses.                                                                    | - Browse courses<br>- Purchase subscriptions and individual courses<br>- Enroll in courses<br>- Track learning progress<br>- Obtain certificates                                   |
| Instructor   | Creates and manages courses, analyzes engagement, and handles payouts.                                                                          | - Create and publish courses<br>- View analytics on enrollments<br>- Manage payouts                                                                                              |

### Open Questions
- Are there specific permissions within the Admin role for granular access control (e.g., different levels of admin access)?
- Will there be any roles beyond Admin, Student, and Instructor, such as a Moderator or Support role? If so, what permissions should they have?
- Should Instructors have permissions to modify enrollments or issue certificates manually?


### High-level User Journeys

#### Student Role

1. **Browse Courses**
   - Access the course catalog on both web and mobile platforms.
   - View detailed information about each course.

2. **Subscription Purchase**
   - Choose between monthly or annual subscription models.
   - Complete payment through Stripe.
   - Assumption: An active subscription unlocks all courses unless specified otherwise.

3. **Individual Course Purchase**
   - Select an individual course for one-time purchase, if not subscribing.
   - Complete payment through Stripe.

4. **Enroll in Courses**
   - Enroll using either subscription or individual purchase.
   - Receive enrollment confirmation.

5. **Learning and Progress Tracking**
   - Access enrolled courses from the student dashboard.
   - Track progress within the course player.

6. **Certification**
   - Complete courses and receive a digital certificate.
   - Certificates appear within the user dashboard.

7. **Account Management**
   - Authenticate using Supabase Auth or Auth0.
   - Manage account settings, subscription options, and password recovery.

8. **Exception Handling**
   - Missed payments deactivate access; notification sent.
   - Failed authentication prompts error message with recovery options.

#### Instructor Role

1. **Course Creation**
   - Use the course builder tool to design and develop new courses.
   - Publish courses for student access.

2. **View Analytics**
   - Access enrollment and engagement analytics via the instructor dashboard.

3. **Manage Payouts**
   - Monitor payout history based on enrollment counts.
   - Receive earnings through a predetermined payment cycle.

4. **Account Management**
   - Authenticate using Supabase Auth or Auth0.
   - Update personal and payout information.

5. **Exception Handling**
   - Course inaccuracies or quality issues prompt moderation.
   - Payout discrepancies trigger support contact.

#### Admin Role

1. **Platform Management**
   - Access the admin management dashboard for user roles and course moderation.
   - Modify subscription plans and set payout processes.

2. **Monitor Activity**
   - Track platform activity and usage metrics.
   - Generate comprehensive reports.

3. **User Role Management**
   - Assign roles and manage permissions for Students and Instructors.

4. **Content Moderation**
   - Review and approve course content and instructor submissions.

5. **Exception Handling**
   - Resolve disputes related to subscriptions, content, or payouts.
   - Open Question: What are the specific escalation paths for unresolved issues?

#### Edge Cases & Exceptions

- **Subscription Renewal Failure:** Notifications sent to users with a grace period for payment update.
- **Auth Failure:** Users directed to a verification prompt or recover page.
- **Course Completion Issues:** Ensure tracking mechanisms reflect true course status.
  
**Open Questions:**
- Does an active subscription provide access to all courses, or do some remain exclusive for individual purchase?
- Clarification needed on resolution procedures for significant admin-level disputes.


# Functional Requirements

## User Management
- **Authentication and Authorization**
  - MUST implement user authentication using Supabase Auth or Auth0 for Admin, Instructor, and Student roles.
  - MUST support role-based access control (RBAC) to ensure proper permissions across roles.
  - SHOULD include features for account creation, login, logout, password reset, and email verification.

## Course Management
- **Course Creation and Management**
  - MUST allow Instructors to create and publish courses through a Course Builder interface.
  - SHOULD support editing and updating of course content post-publication.
  - COULD allow Instructors to set course prerequisites if applicable.

## Student Experience
- **Course Access and Interaction**
  - MUST provide Students with a course catalog for browsing.
  - MUST enable Students to enroll in courses via subscription or individual purchase.
  - SHOULD include a course player with functionality for video streaming, progress tracking, and downloads.

- **Subscription and Payments**
  - MUST offer subscription models (monthly/annual) via Stripe to unlock all courses.
  - SHOULD support one-time purchases for individual courses.

- **Progress and Certification**
  - MUST track student progress across enrolled courses.
  - SHOULD issue certificates upon course completion.

## Instructor Features
- **Analytics and Payouts**
  - MUST provide analytics on enrollment counts for Instructors.
  - SHOULD manage payouts to Instructors based on enrollment metrics.

## Admin System
- **Platform Management**
  - MUST offer a management dashboard for Admins to track platform activity and manage users, courses, and subscription plans.

- **Reporting and Moderation**
  - SHOULD allow Admins to generate reports on overall user engagement and subscription metrics.
  - COULD provide tools for content moderation within courses.

## Technology Stack
- **Shared Codebase and APIs**
  - MUST utilize a single codebase for both iOS and Android using React Native (Expo).
  - MUST ensure the same APIs are used across web and mobile clients for consistency.

## Constraints and Considerations
- **Budget and Timeline**
  - MUST deliver the platform within the confirmed budget of $25k–$50k and a timeline of 4 months.

## Open Questions
- Does a user with an active subscription get access to all courses, or are some courses intended to remain pay-per-course?
- Are there any specific tech stack preferences, such as AWS vs GCP, that need to be considered?

## Assumptions
- Assumed that initial course access requires a subscription model at launch and individual purchases are a future enhancement.


# Non-Functional Requirements

## Performance

- The platform must support rapid load times for both web and mobile applications, aiming for sub-second response times on average.
- API endpoints should handle up to 100 concurrent requests to accommodate peak loads.

## Security

- Implement strong user authentication via Supabase Auth or Auth0, securing both web and mobile platforms.
- Ensure data encryption in transit and at rest using industry-standard protocols.
- Support role-based access control (RBAC) for Admin, Instructor, and Student roles.

## Compliance

- Ensure GDPR compliance by implementing data privacy and user consent mechanisms.
- Incorporate accessibility standards (WCAG 2.1) into web and mobile designs.

## Reliability

- Aim for 99.9% uptime, employing cloud solutions like AWS with built-in redundancy for hosting.
- Regular data backups must be automated, with a disaster recovery plan in place.

## Scalability

- Design architecture to be horizontally scalable, allowing seamless traffic and user growth.
- Utilize managed database services like AWS RDS or Supabase for scaling database operations.

## Localization

- Prepare infrastructure to support multi-language content if expansion requires it in the future (Assumption).

## Observability

- Employ monitoring and logging tools such as AWS CloudWatch or DataDog to track system performance and errors.
- Set up alerts for critical failures and performance bottlenecks.

## Open Questions

- What specific compliance standards beyond GDPR need to be adhered to?
- Are there specific geographic regions for which initial localization is required?
- Is there a preference for AWS or other cloud providers (e.g., GCP)? 

## Assumptions

- The initial deployment will focus on English only, with localizations added based on user demand.
- Managed cloud services will be used for scalability and to reduce infrastructure management overhead.


### Integrations and Data

#### Integrations List
- **Web and Mobile App:** Next.js for web, React Native (Expo) for mobile (iOS and Android).
- **Backend/API:** NestJS (Node.js) with a shared API for both web and mobile clients.
- **Database:** Postgres (Supabase or AWS RDS).
- **Authentication/RBAC:** Supabase Auth or Auth0 for managing user roles and permissions.
- **Payments/Subs**: Stripe for handling monthly/annual subscriptions and one-time course purchases.
- **Content Storage/Streaming:** S3 + CloudFront with optional use of Mux/Vimeo for video streaming.
- **Email/Notifications**: Postmark or SendGrid for communication purposes.
- **Admin Tools:** Retool or a lightweight internal admin tool built with Next.js.

#### Key Entities
- **User Roles:**
  - Admin
  - Student
  - Instructor/Teacher
- **Course Content:**
  - Course details
  - Enrollment records
  - Progress tracking
  - Certificates
- **Monetization:**
  - Subscription plans
  - One-off purchases
  - Payout records
- **System Operations:**
  - User authentication data
  - Payment transactions
  - Storage of media content

#### High-Level Data Flows
- **User Authentication:**
  - Users authenticate via Supabase Auth or Auth0, with sessions managed across web and mobile platforms.
  
- **Course Access and Management:**
  - Admins manage course content and monitor platform activity.
  - Instructors create, publish, and manage courses, accessing analytics for performance.
  - Students browse, enroll, and track course progress, with the ability to view or download certificates.

- **Payment Processing:**
  - Stripe manages both subscription billing cycles and one-off course payments, integrating directly with user accounts for seamless transactions.

- **Content Delivery:**
  - Course media is stored and streamed via S3 and CloudFront, ensuring efficient content delivery to users.

- **Reporting and Payouts:**
  - Enrollment data is collected for analytics and determines payout calculations for instructors based on enrollment counts.

#### Open Questions
- Does the authentication solution need to support multiple methods (e.g., social login)?
- Are there specific reporting requirements beyond basic enrollment and payment analytics?
- Is there additional detail regarding the integration with Mux/Vimeo for video streaming?


## Constraints and Assumptions

### Constraints

- **Budget and Timeline:**
  - Budget is limited to $25k-$50k.
  - Project timeline is set at 4 months.

- **Platform and Technology:**
  - Primary tech stack includes:
    - Next.js for the web.
    - React Native (Expo) for mobile (iOS and Android).
    - NestJS for the backend/API.
    - Postgres as the database.
    - Stripe for payments.
    - Supabase Auth or Auth0 for authentication and RBAC.
  - Fallback stack: WordPress + LearnDash + Stripe for time or scope constraints.

- **Compliance and Security:**
  - Authentication and authorization need to comply with standard security protocols, using managed services like Supabase Auth or Auth0.

- **Operational Requirements:**
  - The system must support a role-based access control system: Admin, Student, and Instructor/Teacher.
  - Shared backend for web and mobile applications to ensure consistency.

- **Business Requirements:**
  - Monetization includes subscription model and future capability for individual course purchases.
  - Instructor payouts are based on enrollment counts.

### Assumptions

- **Platform Assumptions:**
  - The custom tech stack will be feasible within the budget and timeline constraints.
  - React Native is assumed to be the cost-effective solution for both iOS and Android within budget constraints.

- **Monetization Assumptions:**
  - An "all-access pass" subscription initially provides access to all courses, with future flexibility for individual purchases.

- **Product Assumptions:**
  - The design must support scalable growth for a growing student base and multiple instructors.

- **Fallback Plan:**
  - If custom development faces challenges, transitioning to the fallback stack (WordPress + LearnDash + Stripe) will be possible without significant loss in functionality.

### Open Questions

- Does the user have specific preferences or mandates between AWS and GCP, or are recommendations to be made by developers?
- Clarification is needed on whether an active subscription grants access to all courses, or if some courses will remain pay-per-course.


# Open Questions

### P0: Critical Questions (Immediate Resolution Needed)
1. **Subscription Model Clarification**  
   - Clarification needed on whether a user with an active subscription gets access to all courses or only a subset, with some courses remaining pay-per-course.  
   - **Owner Suggestion**: Product Owner

2. **Tech Stack Preferences**  
   - Does the user have specific preferences regarding the tech stack (e.g., AWS vs GCP, Stripe, React/Next.js), or should developers make these recommendations?  
   - **Owner Suggestion**: Founder/Product

### P1: High-Priority Questions (Answer Needed Soon)
1. **Instructor Payouts Detail**  
   - How is the instructor payout structure defined? Specifically, what criteria will be used to calculate payouts based on enrollment counts?  
   - **Owner Suggestion**: Product Owner

2. **Fallback Plan Execution Criteria**  
   - Under what circumstances will the fallback tech stack (WordPress + LearnDash + Stripe) be activated to compress scope or time?  
   - **Owner Suggestion**: Engineering

3. **Authorization Provider Confirmation**  
   - Final decision needed on whether to use Supabase Auth or Auth0 for managed authentication and role-based access control.  
   - **Owner Suggestion**: Engineering

### P2: Medium-Priority Questions (Answer Needed for Future Planning)
1. **Content Storage Strategy**  
   - Decision required on whether to use Mux/Vimeo in addition to S3 + CloudFront for video content storage and streaming.  
   - **Owner Suggestion**: Engineering

2. **Admin Tools Specification**  
   - Clarification on whether Retool or a custom internal admin tool in Next.js is preferred for administrative functionalities.  
   - **Owner Suggestion**: Product Owner

3. **Payment Flexibility and Future Scalability**  
   - What are the anticipated future requirements for payment methods, and how will they be integrated with the current system?  
   - **Owner Suggestion**: Product Owner

### Assumptions (Require Confirmation)
- **Subscription Model Assumption**  
  - Initially, the subscription will provide an 'all-access pass' to all courses unless specified otherwise.
  
- **Tech Stack Default**  
  - Developers will proceed with the recommended stack (Next.js, NestJS, Postgres, Stripe, React Native) if no specific preferences are expressed.
