# User Journeys Document

**Job ID:** b7058f3c-9a4a-483c-a711-ac9cac9a0827

> This document is generated from chat discovery + extracted knowledge files.

# Executive Summary

Our product is a versatile online teaching and learning platform designed to connect teachers and students through structured digital courses. Built with a custom technology stack, it aims to create a scalable, production-ready environment that supports multiple instructors, a growing student base, and integrated monetization from day one.

### Who It Is For:
- **Students** seeking accessible, online education.
- **Instructors/Teachers** wanting to create, manage, and monetize digital courses.
- **Administrators** managing platform activities, user roles, and functionalities.

### Primary Outcomes:
- Enable seamless digital learning experiences for students.
- Provide robust course creation and management tools for instructors.
- Support scalable operations and monetization strategies for administrators.

### Key Capabilities:
- Subscription-based model offering an "all-access pass" to courses.
- Role-based access control (RBAC) ensuring security and role-specific features.
- Course authoring tools allowing instructors to publish and manage courses.
- Payout system for instructors based on enrollments.
- Progress tracking, certifications, and analytics to enhance learning and teaching.
- Shared backend for seamless integration across web and mobile platforms.

---

## Personas & Roles

### 1. Ashley - Aspiring Learner

- **Goals:**
  - Access a variety of courses to improve skills and career prospects.
  - Obtain certifications for completed courses.
  - Easily track learning progress across multiple devices.

- **Pain Points:**
  - Difficulty finding all-inclusive course subscriptions.
  - Challenges in tracking course progress and certifications.
  - Payment difficulties, especially with subscriptions.

- **Permissions/Role:**
  - **Role:** Student
  - Can browse course catalog, purchase subscriptions, enroll in courses, and access certificates.

- **Success Metrics:**
  - Enrollment in multiple courses.
  - High engagement and completion rates.
  - Positive feedback on platform usability.

---

### 2. Jordan - Expert Instructor

- **Goals:**
  - Create and publish high-quality courses.
  - Monitor student enrollments and progress.
  - Receive timely and accurate payouts.

- **Pain Points:**
  - Complexity in course creation and management.
  - Lack of visibility into student analytics.
  - Challenges in tracking and receiving payouts.

- **Permissions/Role:**
  - **Role:** Instructor/Teacher
  - Can create and manage courses, view analytics, and manage payouts.

- **Success Metrics:**
  - High course enrollment and student satisfaction.
  - Positive student feedback and course ratings.
  - Regular and accurate payout cycles.

---

### 3. Sam - Platform Administrator

- **Goals:**
  - Ensure platform runs smoothly and securely.
  - Manage user roles and permissions effectively.
  - Oversee subscription plans and payment processes.

- **Pain Points:**
  - Managing a large number of users and courses.
  - Ensuring security across the platform.
  - Balancing feature control and accessibility.

- **Permissions/Role:**
  - **Role:** Admin
  - Full access to platform tools, user management, course moderation, subscription plans, and reporting.

- **Success Metrics:**
  - Efficient platform operations with minimal downtime.
  - High user satisfaction ratings.
  - Secure and compliant payment processing.

---

### 4. Taylor - Business Founder

- **Goals:**
  - Launch and grow a scalable, monetized e-learning platform.
  - Achieve a balanced budget within the established timeline.
  - Support a growing base of instructors and students.

- **Pain Points:**
  - Budget constraints and tight development timelines.
  - Balancing feature set with development complexity.
  - Need for a reliable tech stack that supports growth.

- **Permissions/Role:**
  - **Role:** Business Oversight
  - Access to strategic reports, financial summaries, and platform growth metrics.

- **Success Metrics:**
  - Successful launch within budget and timeline.
  - Steady growth in user base and course offerings.
  - Positive return on investment.

---

### Assumptions & Questions

- Personas for **Customer Support Specialists** or **Marketing Managers** not defined. These roles may be relevant for ongoing operations and platform growth.
- **Questions:**
  - Are there additional roles beyond those defined (e.g., Support, Marketing)?
  - What specific functionalities are prioritized for initial launch versus later phases?

---

# Core User Journeys

## 1. New User Onboarding Journey

### Trigger
A new visitor arrives at the platform for the first time.

### Steps
1. **Landing Page:** User lands on the homepage and explores the platform’s offerings.
2. **Sign-Up:** 
   - User clicks "Sign Up" and enters personal details, including email and password.
   - User selects role (Student or Instructor).
3. **Email Confirmation:** 
   - System sends an email with a verification link.
   - User clicks the link to verify their email.
4. **Profile Completion:** 
   - User is prompted to complete their profile with additional details, like payment information for Students or teaching credentials for Instructors.
5. **Welcome Tour:** 
   - System optionally provides a quick tour of the dashboard and key features.

### System Behaviors
- Sends verification and welcome emails.
- Assigns default role-based permissions.
- Tracks completion status.

### Completion Criteria
- User is fully registered and can navigate the platform.
- Profile is marked as complete.
  
### Failure/Edge Cases
- **Verification email not received:** Provide a "resend" option.
- **Incomplete profile:** Notify user with reminders to complete it.

## 2. Main Value Journey (Subscription Purchase)

### Trigger
User decides to access courses through a subscription.

### Steps
1. **Browse Courses:** User explores the catalog and decides to subscribe.
2. **Subscription Plan Selection:** 
   - User selects a subscription plan (monthly or annual).
3. **Checkout:** 
   - User enters payment details using Stripe.
   - User confirms purchase.
4. **Confirmation:** 
   - System verifies payment.
   - User receives confirmation email and notification in the app.
5. **Access Courses:** 
   - Subscription activates.
   - User gets access to all eligible courses.

### System Behaviors
- Processes payments through Stripe.
- Sends confirmation emails and app notifications.
- Updates user permissions to allow course access.

### Completion Criteria
- Subscription is active.
- User is able to access courses.

### Failure/Edge Cases
- **Payment failure:** Notify user to retry with different payment details.
- **Access issue:** Provide support contact if user cannot access courses post-purchase.

## 3. Admin/Operator Journey

### Trigger
Admin logs in to manage the platform.

### Steps
1. **Dashboard Access:** Admin logs in and accesses the admin dashboard.
2. **User Management:** 
   - Admin reviews and manages users, roles, and permissions.
3. **Course Moderation:** 
   - Admin monitors course content and approvals if necessary.
4. **Subscription & Payouts:** 
   - Admin reviews subscription metrics.
   - Manages payouts for instructors based on enrollments.
5. **Reporting:** 
   - Admin generates reports for platform activity and financials.

### System Behaviors
- Provides real-time analytics and reports.
- Sends approval alerts and payout notifications.
  
### Completion Criteria
- Admin maintains the platform as required.
- Ensures smooth operations and compliance.

### Failure/Edge Cases
- **Access issues:** Log errors and provide support.
- **Data inconsistencies:** Alert team for investigation.

## 4. Provider/Instructor Journey

### Trigger
An instructor logs in to create and manage courses.

### Steps
1. **Dashboard Access:** Instructor logs into the instructor dashboard.
2. **Course Creation:** 
   - Instructor creates or edits course material.
   - Submits course for approval if moderation is required.
3. **Analytics Review:** 
   - Instructor views enrollment and performance analytics.
4. **Payout Management:** 
   - Instructor monitors payout history and upcoming payments.

### System Behaviors
- Sends notifications for course approvals and payouts.
- Provides access to course analytics.

### Completion Criteria
- Instructor successfully publishes courses.
- Receives payout as per enrollment data.

### Failure/Edge Cases
- **Course rejection:** Notify instructor with feedback for revisions.
- **Payout issues:** Provide support for any discrepancies.

---

### Assumptions and Open Questions
- Assumed course access for subscribers includes all courses unless specified.
- **Questions:**
  - Are instructors allowed to offer free courses?
  - Should there be a manual approval process for course submissions?

---

# UI Touchpoints (Screens & Navigation)

## Admin Persona

### 1. Admin Management Dashboard
- **Purpose**: Central hub for managing the platform's users, roles, courses, and settings.
- **Key Components**: User list, role assignments, course moderation tools, subscription plan management.
- **Main Actions**: View/edit user roles, approve/reject course content, manage subscription plans.
- **Data Shown**: User details, role assignments, course content status, subscription details.

### 2. Payouts and Reports
- **Purpose**: Monitor and manage instructor payouts and generate platform reports.
- **Key Components**: Payout cycle setup, approval interface, detailed reporting tools.
- **Main Actions**: Review/approve payouts, generate financial and course enrollment reports.
- **Data Shown**: Payout details, enrollment numbers, financial summaries.

## Instructor Persona

### 1. Instructor Dashboard
- **Purpose**: Allow instructors to manage their courses and view analytics.
- **Key Components**: Course management tools, analytics graphs, payout history.
- **Main Actions**: Create/edit courses, publish/unpublish content, view enrollment analytics.
- **Data Shown**: Course details, enrollment stats, payout history.

### 2. Course Builder/Manage
- **Purpose**: Facilitate course creation and management by instructors.
- **Key Components**: Content editor, media uploader, course settings.
- **Main Actions**: Add/edit course sections, upload materials, set course pricing.
- **Data Shown**: Course structure, media files, pricing tiers.

## Student Persona

### 1. Student Dashboard
- **Purpose**: Provide students with an overview of their courses and progress.
- **Key Components**: Enrollment list, progress trackers, certificate downloads.
- **Main Actions**: View course status, download certificates, track learning journey.
- **Data Shown**: Course progress bars, completed certifications, enrollment dates.

### 2. Course Catalog/Browse
- **Purpose**: Enable students to explore available courses.
- **Key Components**: Search bar, course categories, course tiles.
- **Main Actions**: Search for courses, filter by category, view course previews.
- **Data Shown**: Course titles, brief descriptions, instructor names, ratings.

### 3. Course Detail
- **Purpose**: Provide detailed course information to assist with enrollment decisions.
- **Key Components**: Course description, syllabus, instructor bio, reviews.
- **Main Actions**: Enroll in course, read reviews, view syllabus.
- **Data Shown**: Detailed course info, student reviews, enrollment button.

## Common Screens for All

### Signup/Login/Verify Email
- **Purpose**: Allow users to create an account, log in, or verify their email.
- **Key Components**: Input fields, verification code entry.
- **Main Actions**: Register an account, log in, verify email address.
- **Data Shown**: Input errors, success messages.

### Pricing and Subscription Management
- **Purpose**: Display available subscription options and manage existing subscriptions.
- **Key Components**: Pricing plans, payment methods, billing history.
- **Main Actions**: View pricing, upgrade/downgrade subscription, view payment history.
- **Data Shown**: Subscription tiers, current plan details, billing records.

### Course Player
- **Purpose**: Deliver course content through an interactive player interface.
- **Key Components**: Video player, progress tracker, content outline.
- **Main Actions**: Play course videos, track progress, navigate content.
- **Data Shown**: Video content, course timeline, current progress.

### Questions
1. Is it assumed that a user with an active subscription gets access to all courses?
2. Are there specific customization preferences for the UI components?

---

### Edge Cases

- **Subscription Access**: Ensure that users with active subscriptions can seamlessly access all courses without encountering paywalls unless specified otherwise.
- **Course Purchase Flexibility**: Check if special promotions or discounts might conflict with standard pricing or subscription access.
- **Role Management**: Handle scenarios where a user might have multiple roles (e.g., both Student and Instructor).
- **Network Dependability**: Address potential issues with offline access or slow network conditions, especially for mobile users.
- **Enrollment Tracking**: Consider courses with minimal enrollments or high dropout rates impacting instructor payouts.

### Constraints

- **Budget**: $25k-$50k, which needs cautious allocation toward essential features and high-impact areas.
- **Timeline**: 4-month development window, requiring efficient project management and milestones.
- **Compliance**: Data protection and privacy laws (e.g., GDPR) must be adhered to, especially with user data and payments.
- **Geographical Reach**: Language support considerations and potential currency conversion for international users.
- **Technology Limits**: Integration within the chosen tech stack without exceeding feature complexity or operational overhead.

### Open Questions

1. **Tech Stack Preferences**: Are there specific preferences for services like AWS vs GCP, or should the development team make recommendations?
2. **Subscription Model Details**: Does an active subscription provide universal course access, or are some courses intended to be pay-per-course?
3. **Multi-role Handling**: What is the preferred way to manage users with multiple roles (e.g., both Teacher and Student)?
4. **Offline Capability**: Is there a requirement for offline course consumption, especially for mobile users?
5. **Promotional Offers**: Are there plans for discounts or promotions that might affect the pricing model or revenue expectations?

---

# Acceptance Criteria & Success Metrics

## Acceptance Criteria

1. **User Roles and Permissions**
   - **Admin Role:**
     - Given an admin user, when accessing the platform, then they should have the ability to manage user roles, view platform analytics, and approve payouts.
   - **Student Role:**
     - Given a student user, when browsing courses, then they should have the ability to enroll via subscriptions or pay-per-course options.
     - Given a student user with an active subscription, when accessing courses, then they should have access to all designated courses.
   - **Instructor Role:**
     - Given an instructor user, when managing courses, then they should have the ability to create, publish, and view course analytics.

2. **Platform Functionality**
   - **Course Access:**
     - Given a valid subscription, when a student is logged in, then they should access the full course catalog.
   - **Payment Processing:**
     - Given a user selects a subscription or course purchase, when they proceed to checkout, then payment should be processed successfully using Stripe.
   - **Progress Tracking:**
     - Given a student is enrolled in a course, when they complete modules, then their progress should be accurately tracked and displayed.
   - **Notifications:**
     - Given a change in course content or enrollment status, when updates occur, then users should receive notifications.

3. **System Performance**
   - **Load Times:**
     - Given peak usage times, when multiple users access the platform, then page load times should remain under 3 seconds.
   - **Uptime:**
     - Given normal operations, when the platform is live, then uptime should be at least 99.5%.

## Success Metrics

### Product Metrics
- **User Engagement:**
  - Number of active users per month (target: 1,000+ active users).
  - Average time spent on platform per session (target: 15+ minutes).
- **Course Completion:**
  - Percentage of courses completed per student (target: 60%).

### Business Metrics
- **Revenue:**
  - Monthly recurring revenue from subscriptions (target: $10,000+ by month 6).
  - Total revenue from one-time course purchases (target: $5,000+ by month 6).
- **Growth:**
  - Increase in user registrations month over month (target: 20%).

### Quality/Operations Metrics
- **Customer Support Tickets:**
  - Number of support tickets related to technical issues (target: reduce by 20% after first month).
- **System Reliability:**
  - Uptime percentage (target: 99.5% or higher).
- **Bug Fixes:**
  - Resolution time for critical bugs (target: within 48 hours).

## Assumptions & Questions

- Assumption: The subscription model initially provides access to all courses.
- Question: Should users have specific access to only a subset of courses under certain types of subscriptions?

Feel free to reach out with any additional questions or areas requiring clarity!
