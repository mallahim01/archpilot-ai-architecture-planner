# User Journeys Document

**Job ID:** 579f622a-bbbf-4887-a082-62f87090f9ad

> This document is generated from chat discovery + extracted knowledge files.

# Executive Summary

### What the Product Is
The product is a comprehensive learning management system (LMS) with integrated e-commerce functionalities designed for both web and mobile users. It aims to streamline the learning experience by providing a unified platform for course delivery, subscription management, and monetization. Built within a budget of $25k–$50k and a 4-month timeline, the system offers a flexible, API-first approach to support multi-instructor interactions, hybrid monetization, and seamless administrator control.

### Who It Is For
- Students seeking efficient and accessible learning solutions
- Instructors looking to create and monetize educational content
- Administrators managing an extensive learning platform
- Founders and business owners in the e-learning industry

### Primary Outcomes
- Simplified course purchase and subscription processes for students
- Enhanced visibility and control for instructors over their courses and earnings
- Streamlined platform management for administrators
- Increased revenue opportunities through hybrid monetization

### Key Capabilities
- Role-based access control for Admin, Student, and Instructor roles
- Supports both platform-level subscriptions and individual course purchases
- Unified web and mobile application experience using a shared API
- Comprehensive progress tracking and certification issuance
- Robust instructor payout system based on enrollments
- Admin tools for user management, course moderation, and financial oversight

---

# Personas & Roles

## 1. Alex, the Admin

**Goals:**
- Efficiently manage users and roles.
- Oversee course content and enrollment processes.
- Ensure smooth financial transactions and payouts.

**Pain Points:**
- Difficulty in tracking numerous users and courses.
- Challenges in maintaining up-to-date financial records.
- Balancing security with user accessibility.

**Permissions/Role:**
- Role: Admin
- Access to user management, course moderation, subscription plans, payouts, and system reports.

**Success Metrics:**
- Reduced time in managing user queries.
- Seamless integration of new courses.
- Timely and accurate payouts.

---

## 2. Sara, the Student

**Goals:**
- Easily access a variety of courses.
- Track learning progress and achievements.
- Conveniently manage billing and subscriptions.

**Pain Points:**
- Navigating the course catalog can be overwhelming.
- Difficulty in tracking progress across multiple courses.
- Confusion over subscription and billing processes.

**Permissions/Role:**
- Role: Student
- Access to course catalog, learning progress, and billing information.

**Success Metrics:**
- Completion of courses and receipt of certificates.
- High satisfaction with the user interface and experience.
- Clarity in subscription and billing processes.

---

## 3. Tom, the Instructor

**Goals:**
- Create engaging and comprehensive courses.
- Gain insights from student progress and feedback.
- Ensure accurate and timely payout for enrollments.

**Pain Points:**
- Understanding the platform's course-building tools can be challenging.
- Lack of detailed analytics on student engagement.
- Uncertainties in payout processes.

**Permissions/Role:**
- Role: Instructor
- Access to course builder, analytics, and payout history.

**Success Metrics:**
- Successful course creation and high engagement rates.
- Clear and insightful analytics leading to course improvements.
- Consistent timely payouts without discrepancies.

---

## 4. Chris, the Founder

**Goals:**
- Ensure the platform is financially viable and scalable.
- Achieve a smooth user experience for all roles.
- Monitor the progress and effectiveness of the platform.

**Pain Points:**
- Controlling costs while maintaining quality.
- Balancing feature requests with development timelines.
- Maintaining high satisfaction across different user roles.

**Permissions/Role:**
- Role: Admin (with founder-level decision permissions)
- Access to all aspects of the system, with emphasis on reports, strategy, and user feedback.

**Success Metrics:**
- Steady growth in user subscriptions.
- Positive feedback from all user personas.
- Achieving KPIs within the budget and timeline constraints.

---

## Assumptions and Questions

- Assumption: The platform does not have additional roles such as guest users or external partners.
- Question: Are there any additional persona roles specific to business strategy, such as marketing or support?

---

# Core User Journeys

Below are outlined the core user journeys for our software platform, focusing on new user onboarding, key value processes like purchases and subscriptions, administrative actions, and instructor engagements.

## 1. New User Onboarding Journey

**Trigger:** A new user visits the platform for the first time.

### Steps:
1. User lands on the homepage and clicks "Sign Up."
2. User fills in required information on the signup form (name, email, password).
3. User submits the form.
4. System sends a verification email.
5. User verifies their email by clicking the link provided.
6. System confirms email verification and welcomes the user.

### System Behaviors:
- Automated email with verification link.
- Welcome message upon successful verification.

### Completion Criteria:
- User successfully verifies their email and accesses their account.

### Failure/Edge Cases:
- User does not receive verification email (check spam/junk).
- Email link expires (user can request a new link).

## 2. Main Value Journey: Subscription Purchase

**Trigger:** A user decides to subscribe to courses.

### Steps:
1. User logs into their account.
2. User navigates to the "Pricing" page.
3. User selects a subscription plan (monthly/annual).
4. User enters payment information.
5. System processes the payment via Stripe.
6. User receives confirmation of subscription via email.

### System Behaviors:
- Payment processing through Stripe.
- Confirmation email with subscription details.
- User granted access to all courses.

### Completion Criteria:
- User successfully subscribes and gains course access.

### Failure/Edge Cases:
- Payment fails (user gets notified with reason and can retry).
- System error during checkout (user prompted to try again later).

## 3. Admin/Operator Journey

**Trigger:** An admin logs in to manage platform operations.

### Steps:
1. Admin logs into the admin dashboard.
2. Admin views user, course, and payment data.
3. Admin makes changes (e.g., adjusts subscriptions, moderates content).
4. Admin reviews and processes instructor payouts.
5. Admin generates reports for performance and monitoring.

### System Behaviors:
- Real-time data update and access.
- Notifications for any required actions (e.g., pending payouts).

### Completion Criteria:
- Admin successfully manages and updates platform operations.

### Failure/Edge Cases:
- Data access issues (system prompts to retry or contact support).

## 4. Provider/Instructor Journey

**Trigger:** An instructor wants to create and manage courses.

### Steps:
1. Instructor logs into their account.
2. Instructor navigates to course builder.
3. Instructor creates or updates a course, including content and pricing.
4. Instructor publishes the course.
5. Instructor monitors enrollment and engagement through an analytics dashboard.

### System Behaviors:
- Access control ensuring instructors can only manage their content.
- Automated updates to course listings.

### Completion Criteria:
- Instructor successfully publishes and manages a course.

### Failure/Edge Cases:
- Content upload issues (system prompts to check formats).
- Publishing fails due to system errors (retry option provided).

## Assumptions

- The assumption is that users will receive emails reliably.
- Stripe will process payments efficiently without frequent errors.

## Open Questions

- Are there any additional onboarding steps required?
- Should instructors receive instant payouts or through scheduled cycles?
- Are there specific permissions that need configuring for admins?

---

# UI Touchpoints (Screens & Navigation)

To support the user journeys, let's break down the screens/pages needed, grouped by persona: Students, Instructors, Admins, and Public users. Each screen will include its purpose, key components, main actions, and data shown.

## Student Screens

### 1. **Dashboard**
- **Purpose**: Provide an overview of the student's enrolled courses and progress.
- **Key Components**: Course thumbnails, progress bars, upcoming events.
- **Main Actions**: View course details, track progress, resume courses.
- **Data Shown**: Enrolled courses, percentage of completion, upcoming deadlines.

### 2. **Course Player**
- **Purpose**: Deliver course content and enable learning.
- **Key Components**: Video player, progress tracker, resource links.
- **Main Actions**: Watch videos, track progress, access resources.
- **Data Shown**: Current lesson details, course progress percentage, downloadable resources.

### 3. **Certificates**
- **Purpose**: View and download earned certificates.
- **Key Components**: List of certificates, download buttons.
- **Main Actions**: Download certificates.
- **Data Shown**: Course name, completion date, certificate status.

### 4. **Billing/Subscription**
- **Purpose**: Manage subscription details and payments.
- **Key Components**: Subscription plan details, payment history, upgrade/downgrade options.
- **Main Actions**: Update payment info, change subscription plan.
- **Data Shown**: Current subscription status, billing cycles, past payments.

## Instructor Screens

### 1. **Dashboard**
- **Purpose**: Overview of courses taught, enrollments, and earnings.
- **Key Components**: Course list, earnings overview, notifications.
- **Main Actions**: View course details, check earnings.
- **Data Shown**: Number of students, earnings, recent activity.

### 2. **Course Builder/Manage**
- **Purpose**: Create and manage courses.
- **Key Components**: Course editor, resource uploader, publishing controls.
- **Main Actions**: Create new course, edit existing courses, publish/unpublish courses.
- **Data Shown**: Course details, content list, resource attachments.

### 3. **Analytics**
- **Purpose**: Provide insights into course performance.
- **Key Components**: Enrollment graphs, completion rates, feedback.
- **Main Actions**: Review analytics data, download reports.
- **Data Shown**: Enrollment statistics, course completion rates, feedback surveys.

### 4. **Payout History**
- **Purpose**: Track earnings and payment history.
- **Key Components**: Earnings summary, payout schedule, transaction history.
- **Main Actions**: View and download payout history.
- **Data Shown**: Total earnings, upcoming payouts, past transaction records.

## Admin Screens

### 1. **Manage Users/Roles**
- **Purpose**: Oversee user accounts and permissions.
- **Key Components**: User list, role assignment tools.
- **Main Actions**: Add/remove users, assign roles, edit user details.
- **Data Shown**: User profiles, role allocations, activity logs.

### 2. **Courses/Moderation**
- **Purpose**: Approve and manage courses on the platform.
- **Key Components**: Course approval interface, moderation tools.
- **Main Actions**: Approve/reject courses, manage reports.
- **Data Shown**: Submitted courses, approval status, flagged content.

### 3. **Subscription Plans**
- **Purpose**: Manage and configure subscription offerings.
- **Key Components**: Plan details, pricing options.
- **Main Actions**: Create/edit plans, adjust pricing.
- **Data Shown**: Plan features, pricing tiers, user metrics.

### 4. **Payouts/Reports**
- **Purpose**: Oversee instructor payouts and access financial reports.
- **Key Components**: Payout cycle management, financial reports.
- **Main Actions**: Manage payout cycles, generate financial reports.
- **Data Shown**: Payout schedules, financial summaries.

## Public Screens

### 1. **Landing Page**
- **Purpose**: Introduce visitors to the platform and encourage sign-ups.
- **Key Components**: Highlights, testimonials, call-to-action buttons.
- **Main Actions**: Navigate to sign-up, browse course catalog.
- **Data Shown**: Featured courses, testimonials, key benefits.

### 2. **Course Catalog/Browse**
- **Purpose**: Explore available courses.
- **Key Components**: Course filters, search bar, course thumbnails.
- **Main Actions**: Search courses, view course details.
- **Data Shown**: Course categories, ratings, short descriptions.

### 3. **Course Detail**
- **Purpose**: Provide detailed information about a specific course.
- **Key Components**: Course description, instructor details, enrollment button.
- **Main Actions**: Enroll in course, share course, view instructor profile.
- **Data Shown**: Detailed course outline, instructor bio, course reviews.

### 4. **Pricing**
- **Purpose**: Display pricing details for subscriptions and courses.
- **Key Components**: Pricing tables, discount offers.
- **Main Actions**: Purchase subscription, view plan details.
- **Data Shown**: Subscription tiers, payment options, special offers.

## Assumptions
- All data shown on screens will be dynamically loaded based on user interactions.
- The navigation across screens will be intuitive with clear back and forward actions.
- Role-based access controls will ensure users only see screens relevant to their roles.

## Open Questions
- Are there any additional screens needed for specific processes not covered here?
- What are the specific branding requirements and how will they influence UI components?
- Can instructors have the ability to modify course prices independently, or is it admin-controlled?

---

# Edge Cases, Constraints, and Open Questions

## Edge Cases
- Users attempting to access courses without a valid subscription or purchase.
- Handling instructor payouts when enrollments are low or below expectations.
- Users changing subscription plans frequently, impacting entitlements and billing cycles.
- Edge cases in content delivery during high traffic, impacting streaming and progress tracking.
- Addressing course access when switching from a subscription model to a la carte purchases or vice versa.

## Constraints
- **Budget**: $25k–$50k for initial development.
- **Timeline**: 4-month development period.
- **Platform Support**: Must support both iOS and Android via React Native.
- **Payment Processing**: Must handle both subscriptions and one-off purchases through Stripe.
- **Compliance**: Ensure adherence to data protection regulations such as GDPR.
- **Technology Stack**: Utilize Next.js, NestJS or AWS Lambda, PostgreSQL, Supabase Auth or Auth0, Stripe, S3 + CloudFront or Mux/Vimeo.
- **Languages/Locale**: Consider multi-language support for diverse user base.
- **Role Management**: Strict role-based access needed for Admin, Student, and Instructor roles.

## Open Questions
1. Are there any hard 'native-only' requirements for the mobile application?
2. Is there a preference for using a turnkey platform like WordPress versus a custom build?
3. Should a subscription grant access to all courses by default, or only a subset?
4. Does the budget include post-launch support and maintenance phases?
5. Will there be specific geographical restrictions or localizations needed for course offerings?

These questions will help refine the product strategy and ensure alignment with stakeholder expectations and user needs.

---

# Acceptance Criteria & Success Metrics

## Acceptance Criteria for MVP

### Admin Role
- **User Management**
  - **Given** an admin is logged in,
  - **When** they access the user management section,
  - **Then** they can add, update, or deactivate users.

- **Course Management**
  - **Given** an admin is logged in,
  - **When** they access the course management section,
  - **Then** they can approve, edit, or remove courses.

- **Payout Management**
  - **Given** an admin wants to manage payouts,
  - **When** they access the payout section,
  - **Then** they can view payout cycles and initiate payouts.

### Student Role
- **Course Access**
  - **Given** a student has an active subscription,
  - **When** they browse the course catalog,
  - **Then** they can access all available courses.

- **Progress Tracking**
  - **Given** a student is enrolled in a course,
  - **When** they complete a module,
  - **Then** their progress is tracked automatically.

- **Certificate Issuance**
  - **Given** a student completes a course,
  - **When** they pass all required assessments,
  - **Then** they receive a completion certificate.

### Instructor Role
- **Course Creation**
  - **Given** an instructor wants to create a new course,
  - **When** they use the course builder,
  - **Then** they can publish the course for student access.

- **Analytics Access**
  - **Given** an instructor has published a course,
  - **When** they view course analytics,
  - **Then** they can see aggregated student engagement data.

## Success Metrics

### Product Metrics
- **User Engagement**
  - Track the average time spent on the platform per user per session.
- **Course Completion Rate**
  - Measure the percentage of enrolled users who complete courses.
- **New User Sign-Up Rate**
  - Monitor the number of new users registering daily.

### Business Metrics
- **Revenue Growth**
  - Track monthly subscription revenue and a la carte sales.
- **Retention Rate**
  - Measure the percentage of users maintaining subscriptions month-over-month.
- **Instructor Payout Efficiency**
  - Evaluate the frequency and timeliness of instructor payouts.

### Quality/Operations Metrics
- **System Uptime**
  - Ensure 99.9% uptime for both web and mobile applications.
- **API Response Time**
  - Average API response times should be under 200ms.
- **Error Rates**
  - Maintain error rates below 1% for critical user actions (e.g., purchases, enrollments).

## Assumptions
- Subscription automatically grants access to all courses unless specified otherwise.
- No native-only features are required if standard app capabilities suffice.
- Use of a custom-built platform over options like WordPress is preferred.

## Open Questions
- Are there any specific native functionalities that are critical to include?
- Should users with subscriptions have access to all courses or only selected ones?
