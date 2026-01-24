# User Journeys Document

**Job ID:** 9b007d72-d558-4d19-99cc-a6bf88c8d401

> This document is generated from chat discovery + extracted knowledge files.

# Executive Summary

Our platform is an innovative online learning solution designed to offer both subscription and individual course access. Built on a robust tech stack, it supports a variety of learning and admin functions, ensuring a seamless experience for all users involved in education delivery and consumption.

**Who it is for:**
- **Admins:** Manage the platform, oversee courses, and control monetization.
- **Students:** Discover, subscribe to, and engage with courses.
- **Instructors:** Create and publish courses, track performance and earnings.

**Primary Outcomes:**
- Seamless subscription management.
- Enhanced learning experiences with progress tracking and certifications.
- Efficient course authoring and publishing.
- Reliable and transparent payouts for instructors.

**Key Capabilities:**
- Role-Based Access Control (RBAC) for Admins, Students, and Instructors.
- Subscription management with monthly and annual plans.
- Course creation and publishing tools for Instructors.
- Student dashboards for progress tracking and certificate management.
- Instructor earnings calculation based on enrollments.
- Centralized admin management for user, course, and payout oversight. 

**Assumptions:**
The product assumes subscriptions initially unlock all courses on the platform. Further clarification is needed regarding whether subscriptions should allow access to all courses or a specific catalog.

**Questions:**
- Should subscriptions unlock all courses on the platform, or only a specific subscription catalog?

---

## Personas & Roles

### 1. Admin Alex

**Goals:**
- Efficiently manage user accounts and course content.
- Oversee subscription and monetization processes.
- Ensure platform compliance and security.

**Pain Points:**
- Complexity of managing multiple user roles and permissions.
- Ensuring timely and accurate payouts to instructors.
- Maintaining platform performance and resolving issues quickly.

**Permissions/Role:**
- Role: Admin
- Permissions: Full access to user management, content oversight, payment management, and analytics.

**Success Metrics:**
- High user satisfaction and low churn.
- Accurate and timely completion of payouts.
- Minimal downtime and security incidents.

---

### 2. Student Sam

**Goals:**
- Discover and enroll in courses of interest.
- Track and complete course progress to earn certifications.
- Manage subscriptions effectively.

**Pain Points:**
- Difficulty finding relevant courses.
- Tracking progress and staying motivated.
- Managing payments and understanding subscription details.

**Permissions/Role:**
- Role: Student
- Permissions: Access to course catalog, course players, progress tracking, and certificate management.

**Success Metrics:**
- High course completion rates.
- Positive course reviews and feedback.
- Smooth subscription and payment experience.

---

### 3. Instructor Ingrid

**Goals:**
- Create and publish engaging course content.
- Monitor student engagement and performance.
- Track earnings and manage payout methods.

**Pain Points:**
- Navigating the course creation and publishing process.
- Understanding payout structures and receiving timely payments.
- Keeping course content updated and relevant.

**Permissions/Role:**
- Role: Instructor
- Permissions: Course creation and publishing, access to performance analytics, earnings tracking, and profile management.

**Success Metrics:**
- High course enrollment numbers.
- Positive instructor reviews and feedback.
- Consistent and clear payout calculations.

---

### 4. Platform Founder Fiona

**Goals:**
- Launch and grow a successful learning platform.
- Ensure a seamless user experience across all roles.
- Achieve financial sustainability through subscriptions and course sales.

**Pain Points:**
- Balancing budget constraints with feature development.
- Ensuring competitive differentiation and user adoption.
- Managing stakeholder expectations and timelines.

**Permissions/Role:** 
- Role: Stakeholder (non-technical)
- Permissions: N/A

**Success Metrics:**
- Meeting or exceeding subscription and sales targets.
- Positive user engagement and growth metrics.
- Successful and timely MVP launch.

---

### Assumptions

- Each persona’s goals and pain points are aligned with typical user expectations in e-learning platforms.
- "Admin Alex" and "Instructor Ingrid" permissions are structured around assumed best practices for platform management.
- Assumptions made based on standard user interactions; adjustments required as more information becomes available.

### Open Questions

- Are there any additional roles or personas that need to be considered?
- Should the "Admin" role include distinct sub-roles for managing specific platform functions?

---

# Core User Journeys

## New User Onboarding Journey

### Trigger
- User visits the platform for the first time and decides to sign up.

### Steps
1. **Visit Signup Page**: User navigates to the signup page.
2. **Account Creation**: User enters email and password to create an account.
3. **Role Selection**: User selects role: Admin, Student, or Instructor.
4. **Email Verification**: System sends a verification email to the user.
5. **Verification**: User clicks on the verification link in the email.
6. **Welcome Tour**: System provides a quick tour of the platform's features related to the selected role.

### System Behaviors
- Sends verification email via Postmark/SendGrid.
- Grants access based on role (RBAC).

### Completion Criteria
- User's email is verified.
- User understands basic platform navigation based on their role.

### Failure/Edge Cases
- **Email not delivered**: Option to resend verification email.
- **Incorrect role selection**: Ability to edit role in the profile after signup.

## Main Value Journey (Subscription Purchase)

### Trigger
- User wants to access all courses by subscribing to the platform.

### Steps
1. **Explore Plans**: User reviews available subscription plans.
2. **Select Plan**: User chooses Monthly or Annual subscription.
3. **Payment Information**: User enters payment details.
4. **Confirmation**: System processes payment via Stripe.
5. **Activate Subscription**: Access to all courses is granted.

### System Behaviors
- Sends email confirmation and receipt.
- Updates user access permissions.
- Sets up renewal reminders and notifications for upgrade/downgrade options.

### Completion Criteria
- Payment is successful.
- User gains immediate access to all courses.

### Failure/Edge Cases
- **Payment failure**: Notify user and allow retry.
- **Cancellation request during signup**: Offer immediate cancellation and refund options if necessary.

## Admin/Operator Journey

### Trigger
- Admin logs in to manage platform operations.

### Steps
1. **Dashboard Access**: Admin views the central dashboard.
2. **User Management**: Admin views and edits user accounts and roles.
3. **Course Oversight**: Admin reviews and approves course submissions.
4. **Monitor Subscriptions**: Admin tracks active subscriptions and financial health.
5. **Payout Approval**: Admin reviews and approves monthly instructor payouts.

### System Behaviors
- Sends notifications for course submissions pending review.
- Provides alerts on overdue payouts.
- Generates monthly reports on subscription and payout status.

### Completion Criteria
- Admin actions are confirmed and logged.
- Instructors receive payouts on time.

### Failure/Edge Cases
- **Payout approval delays**: Send reminders to admins.
- **Errors in user management**: Provide rollback options for account changes.

## Provider/Instructor Journey

### Trigger
- Instructor wants to create and publish a new course.

### Steps
1. **Course Creation**: Instructor uses tools to design and develop a course.
2. **Submit for Review**: Course submitted to Admin for approval.
3. **Publish**: Upon approval, course is published on the platform.
4. **Track Performance**: Instructor monitors course enrollments and student progress.
5. **Earnings Management**: Instructor accesses earnings dashboard for payout insights.

### System Behaviors
- Sends notifications about course approval status.
- Updates dashboard with real-time enrollment and earnings data.

### Completion Criteria
- Course is live on the platform.
- Instructor receives regular earnings updates.

### Failure/Edge Cases
- **Course rejection**: Provide feedback loop for required changes.
- **Earnings discrepancies**: Offer support channel to resolve payout issues. 

## Open Questions

- Should subscriptions unlock all courses or only a curated subscription catalog?

---

# UI Touchpoints (Screens & Navigation)

## Admin Persona

### Dashboard
- **Purpose:** Provide an overview of platform activity and metrics.
- **Key Components:** Analytics graphs, recent activity logs, quick access links.
- **Main Actions:** View detailed reports, navigate to user/course management.
- **Data Shown:** User sign-ups, active subscriptions, instructor payouts, course enrollments.

### User Management
- **Purpose:** Manage users and their roles.
- **Key Components:** User list, role assignment controls, search/filter options.
- **Main Actions:** Add new users, edit roles, deactivate accounts.
- **Data Shown:** User details, current role, status (active/inactive).

### Course Management
- **Purpose:** Oversee course creation and updates.
- **Key Components:** Course list, details view, status indicators (draft/published).
- **Main Actions:** Approve/reject course submissions, edit course details.
- **Data Shown:** Course title, instructor, enrollment numbers, status.

### Payout Management
- **Purpose:** Handle instructor earnings and payouts.
- **Key Components:** Payout summary, approval buttons, payout history logs.
- **Main Actions:** Approve payouts, view payout history.
- **Data Shown:** Instructor earnings, payout amounts, approval status.

### Subscription Management
- **Purpose:** Oversee platform subscription plans and lifecycle.
- **Key Components:** Subscription plans list, action buttons for each plan.
- **Main Actions:** Edit plans, view subscriber list, cancel subscriptions.
- **Data Shown:** Plan details, subscriber numbers, revenue metrics.

---

## Student Persona

### Course Catalog
- **Purpose:** Discover and explore available courses.
- **Key Components:** Search bar, filter options, course cards.
- **Main Actions:** Search for courses, filter by category, enroll.
- **Data Shown:** Course title, instructor, brief description, price.

### Course Player
- **Purpose:** Facilitate course engagement and learning.
- **Key Components:** Video player, resource links, progress tracker.
- **Main Actions:** Play videos, download resources, mark units as complete.
- **Data Shown:** Current progress, course content.

### Dashboard
- **Purpose:** Manage and track learning activities and subscriptions.
- **Key Components:** Course progress indicators, subscription details.
- **Main Actions:** Resume courses, manage subscription.
- **Data Shown:** Active courses, remaining trial days (if applicable).

### Profile & Settings
- **Purpose:** Manage personal and account information.
- **Key Components:** Profile info, settings options (notifications, payment methods).
- **Main Actions:** Update details, manage payment information.
- **Data Shown:** Personal information, subscription status.

---

## Instructor Persona

### Course Authoring
- **Purpose:** Create and publish courses.
- **Key Components:** Rich text editor, media upload options, course settings.
- **Main Actions:** Add course content, publish/unpublish.
- **Data Shown:** Draft status, content preview.

### Dashboard
- **Purpose:** Monitor course performance and earnings.
- **Key Components:** Earnings graphs, performance metrics.
- **Main Actions:** View earnings breakdown, analyze course performance.
- **Data Shown:** Monthly earnings, enrollment trends.

### Profile & Payout Settings
- **Purpose:** Manage personal information and payout preferences.
- **Key Components:** Profile details editor, payout method selection.
- **Main Actions:** Update profile, link payout account.
- **Data Shown:** Profile information, payout history.

---

### Assumptions
- Subscriptions unlock all courses unless explicitly marked otherwise.
- Students access individual course purchases from the course catalog.

### Open Questions
- Should the subscription unlock all courses or only a subscription catalog?

---

## Edge Cases, Constraints, and Open Questions

### Edge Cases

- Instructors may need to change payout methods post-setup or during ongoing payout cycles.
- Students may cancel their subscriptions but still, need access to previously purchased individual courses.
- Different regions might have specific legal requirements for subscription cancellations or refunds.
- Misalignment between the subscription renewal schedule and instructor payout cycles could complicate earnings calculations.
- Unexpected failures in payment processing that affect subscription renewals or course access.

### Constraints

- **Budget:** The project budget is set at $25–50k.
- **Timeline:** The MVP is to be delivered within 4 months, with clearly defined monthly milestones.
- **Compliance:** Legal compliance, including privacy and data protection regulations, must be ensured.
- **Geographical:** No explicit geographical constraints mentioned, but global reach could imply diverse regulatory requirements.
- **Languages:** No mention of multi-language support, assuming English only unless specified otherwise.

### Open Questions

1. Should subscriptions unlock all courses on the platform, or only a specific subscription catalog?
2. Are there any specific geo-locations with legal requirements that need to be considered?
3. Do instructors have the flexibility to switch between fixed-amount and revenue-share payouts mid-cycle?
4. Is there a need to support multi-language capabilities from the start?
5. Are there any scalability concerns or traffic expectations post-launch?

---

### Acceptance Criteria & Success Metrics

#### Acceptance Criteria

1. **Role-Based Access Control (RBAC)**
   - **Given** a user is assigned a role (Admin, Student, Instructor), **when** the user logs in, **then** the user should see role-specific views and functionalities.

2. **Subscription Management**
   - **Given** a new user wants to subscribe, **when** they select a monthly or annual plan and complete payment, **then** access to all courses should be granted.

3. **Course Creation and Publishing**
   - **Given** an instructor wants to create a course, **when** they complete the course authoring process, **then** the course should be available on the platform for publishing.

4. **Enrollment and Progress Tracking**
   - **Given** a student is enrolled in a course, **when** they progress through the course, **then** their progress should be tracked and displayed in their dashboard.

5. **Certificate Awarding**
   - **Given** a student completes a course, **when** they pass all assessments, **then** a certificate should be automatically issued.

6. **Instructor Payouts**
   - **Given** an enrollment event occurs, **when** the payout cycle is executed, **then** instructors should receive payouts based on the agreed model (fixed or revenue-share).

7. **Notifications**
   - **Given** a subscription or payment event occurs, **when** the event is processed, **then** appropriate email notifications should be sent for receipts, renewals, cancellations, and payouts.

8. **Monetization Controls**
   - **Given** the admin wants to view platform earnings, **when** they access the admin dashboard, **then** a clear earnings summary should be displayed.

#### Success Metrics

##### Product Metrics
- **User Engagement:**
  - Daily Active Users (DAU) and Monthly Active Users (MAU) targets.
  - Average course completion rate of 75%.

- **Feature Adoption:**
  - Over 80% of users successfully create accounts and opt for a subscription plan.
  - At least 60% of instructors publish courses within the first month after onboarding.

##### Business Metrics
- **Revenue Growth:**
  - Achieve subscription revenue targets exceeding 20% month over month growth.
  - Conversion rate from free trial to paid subscriptions above 30%.

- **Market Penetration:**
  - Achieve a user base growth of 150% within the first six months post-launch.

##### Quality/Operations Metrics
- **System Performance:**
  - Application uptime of 99.9%.
  - Page load times under 2 seconds on average.

- **Customer Support:**
  - Response times for customer inquiries within 24 hours.
  - Resolution rate for support tickets above 95% within the first contact.

- **Security and Compliance:**
  - No significant security breaches within the first year.
  - Full compliance with data protection regulations (e.g., GDPR).

#### Assumptions
- Subscriptions unlock all courses by default unless specified otherwise.
- The infrastructure and technologies are capable of supporting the growth metrics outlined.

#### Questions
- Should individual course purchases be part of the initial MVP or in a later phase?
- How should we handle potential discounts or promotions for early subscribers?
