# User Journeys Document

**Job ID:** 788b31e8-db4a-4d0d-b857-68fe9667f253

> This document is generated from chat discovery + extracted knowledge files.

# Executive Summary

The product is a web-based learning management platform designed to facilitate course creation, enrollment, and administration. It allows instructors to publish courses, track student progress, and receive payouts based on enrollments, while students can subscribe to the platform to access a wide range of educational content. The platform also offers flexible subscription models and secure payment processing.

### Who It Is For
- Instructors wanting to create and manage online courses
- Students seeking to enroll in and learn from diverse course offerings
- Platform administrators managing users, courses, and financials

### Primary Outcomes
- Seamless course creation and publication by instructors
- Easy student enrollment and learning progress tracking
- Efficient subscription management and secure payment processing
- Transparent payout system for instructors based on enrollments

### Key Capabilities
- Role-based access control for Admin, Student, and Instructor roles
- Monthly and annual subscription models with optional course purchases
- Course creation, publishing workflow, and progress tracking tools
- Secure payment integration with Stripe and automated payout calculations
- Certification issuance upon course completion
- Comprehensive admin management and reporting features

### Questions
- Should subscriptions unlock all courses on the platform or only a specific subscription catalog?
- What are you trying to build (in one sentence), and who is it for?

---

## Personas & Roles

### 1. Admin: Alex the Administrator

**Goals:**
- Manage user roles and permissions effectively.
- Oversee course approvals and content quality.
- Monitor financial transactions and reconcile instructor payouts.

**Pain Points:**
- Challenges in tracking and moderating high volumes of courses.
- Ensuring timely and accurate payout processing.
- Navigating user disputes and refunds efficiently.

**Permissions/Role:**
- Full access to the system, including user management, course approval, subscription management, and reporting.

**Success Metrics:**
- High course approval times with minimal delays.
- Successful payout reconciliation each cycle.
- Low rate of user complaints and disputes.

---

### 2. Student: Sam the Scholar

**Goals:**
- Easily find and enroll in relevant courses.
- Track learning progress and complete courses.
- Earn certificates of completion to enhance their profile.

**Pain Points:**
- Difficulty navigating the course catalog.
- Frustration with managing billing and subscriptions.
- Challenges in tracking progress across multiple courses.

**Permissions/Role:**
- Access to course catalog, enrollment, learning modules, and personal dashboard.

**Success Metrics:**
- High course completion rate.
- Positive feedback on course content and navigation.
- Enhanced learning dashboard engagement.

---

### 3. Instructor: Ingrid the Instructor

**Goals:**
- Create and publish engaging course content.
- Monitor student progress and provide feedback.
- Maximize earnings through enrollments.

**Pain Points:**
- Complex course creation process.
- Lack of clarity in earnings and payout schedules.
- Managing student interactions efficiently.

**Permissions/Role:**
- Ability to create, manage, and publish courses. Access to earnings dashboard and student progress data.

**Success Metrics:**
- High course enrollment numbers.
- Regular content updates and student engagement.
- Satisfied earnings and timely payouts.

---

### 4. Developer: Dev the Developer

**Goals:**
- Implement robust and scalable features that meet user needs.
- Ensure systems are secure and perform optimally.
- Support seamless user experiences across all roles.

**Pain Points:**
- Balancing multiple feature requests within tight timelines.
- Handling unforeseen technical dilemmas or API limitations.
- Ensuring smooth integration with third-party services like Stripe and Auth0.

**Permissions/Role:**
- Access to code repositories, system configurations, and integration settings.

**Success Metrics:**
- Timely feature releases with minimal bugs.
- Positive user feedback on system performance.
- Successful third-party service integrations.

---

### Assumptions & Questions

**Assumptions:**
- The personas are based on inferred roles and may need additional refinement with direct user insights.
- Success metrics are aligned with typical goals but may vary depending on specific organizational priorities.

**Questions:**
- What are the most critical success metrics for each persona from a business standpoint?
- Are there additional user roles that need to be considered beyond the core personas identified here?

---

# Core User Journeys

## New User Onboarding Journey

### Trigger
A new user visits the platform to explore and potentially subscribe or purchase courses.

### Steps
1. **Visit Landing Page**: User navigates to the website and views the landing page.
2. **Sign Up/Log In**:
   - User selects "Sign Up" or "Log In".
   - User provides email/password or uses third-party authentication (Clerk/Auth0).
3. **Profile Setup**: 
   - User fills in basic profile information (name, role preferences).
   - User selects preference for Student or Instructor role.
4. **Email Confirmation**: 
   - System sends a confirmation email.
   - User clicks the link to verify their email.
5. **Welcome Tour (Optional)**: 
   - User is offered a guided tour of the platform features.

### System Behaviors
- Send verification and welcome emails.
- Confirm account activation upon email link click.
- Store user role selection and profile data.

### Completion Criteria
- User account is active and user is logged in.
  
### Failure/Edge Cases
- **Invalid Email**: System shows error message; prompts correction.
- **Email not received**: User is guided to resend verification email.

## Main Value Journey (Subscription & Course Access)

### Trigger
A logged-in user decides to subscribe to access platform courses.

### Steps
1. **Explore Courses**:
   - User browses catalog using search and filters.
2. **Select Subscription Plan**:
   - User chooses between monthly or annual subscription from the pricing page.
3. **Checkout Process**:
   - User reviews summary of chosen plan and any applicable discounts.
   - User enters payment details (handled via Stripe).
4. **Confirmation**: 
   - System processes payment and confirms subscription activation.
5. **Access Courses**:
   - User gains access to subscribed courses.
   - User starts a course and tracks progress.

### System Behaviors
- Send subscription confirmation and receipt emails.
- Enable course access upon successful payment.
- Trigger notifications for subscription renewal or cancellations.

### Completion Criteria
- Subscription is active.
- User has access to the course library.

### Failure/Edge Cases
- **Payment Failure**: Notify user; allow retry with a different payment method.
- **Expired Card**: User is prompted to update payment info.

## Admin/Operator Journey

### Trigger
Admin logs in to manage the platform and users.

### Steps
1. **Log In**: Admin accesses the system via secure authentication.
2. **User Management**:
   - View user list, modify roles, or deactivate accounts.
3. **Course Approval**:
   - Admin reviews and approves new course submissions from instructors.
4. **Subscription Management**:
   - Configure subscription plans or resolve disputes.
5. **Reporting and Payouts**:
   - Access reports for revenue and enrollment metrics.
   - Manage instructor payouts and scheduling.

### System Behaviors
- Send notifications for pending course approvals.
- Trigger automated reports on selected schedules.
- Document activity logs for audits.

### Completion Criteria
- Tasks are performed as intended (e.g., course approval or user role update).

### Failure/Edge Cases
- **Unauthorized Changes**: System restricts actions based on permission levels.

## Instructor Journey

### Trigger
An instructor logs in to create and manage their courses.

### Steps
1. **Log In**: Instructor enters credentials and accesses dashboard.
2. **Course Creation**:
   - Use course builder to design the course structure.
   - Upload content (videos, documents, quizzes).
3. **Submit for Approval**:
   - Submit created course for admin approval.
4. **Monitor Course Performance**:
   - View student progress and engagement metrics.
5. **Review Earnings**:
   - Check status of enrollments and subsequent payouts.

### System Behaviors
- Notify instructor about course submission status.
- Update performance metrics in real-time.
- Send payout schedules and earnings summaries.

### Completion Criteria
- Successful course publication.
- Continuous update on student engagement and earnings.

### Failure/Edge Cases
- **Content Rejection**: Admin provides feedback; instructor revises and resubmits.

### Assumptions & Questions
- Assumed subscription unlocks all courses; need clarification if limited by catalog.
- Who is the primary audience for the platform, and what specific problem does it aim to solve?

---

# UI Touchpoints (Screens & Navigation)

## Admin Persona

### User Management Screen
- **Purpose:** Manage users' access and roles within the platform.
- **Key Components:** User list, role assignment dropdown, search/filter options.
- **Main Actions:** Add/edit/delete users, assign/revoke roles, search for users.
- **Data Shown:** User names, roles, contact information, status (active/suspended).

### Course Approval Screen
- **Purpose:** Approve or reject courses created by instructors.
- **Key Components:** Course details, approval buttons, comment section for feedback.
- **Main Actions:** Approve/reject courses, leave feedback.
- **Data Shown:** Course title, description, instructor name, status.

### Subscription Management Screen
- **Purpose:** Configure and manage subscription plans.
- **Key Components:** Plan list, configuration settings, pricing fields.
- **Main Actions:** Create/edit/delete subscription plans.
- **Data Shown:** Plan name, type (monthly/annual), price, active status, features.

### Payout Management Screen
- **Purpose:** Handle instructor payouts based on enrollments and revenues.
- **Key Components:** Payout calculation tools, payment history.
- **Main Actions:** Review/approve payouts, generate payout reports.
- **Data Shown:** Instructor names, payout amounts, payout history.

### Reporting Dashboard
- **Purpose:** Provide insights into platform performance and usage.
- **Key Components:** Graphs, charts, tables.
- **Main Actions:** View/export reports, set report schedules.
- **Data Shown:** User enrollments, revenue stats, course popularity.

## Instructor Persona

### Instructor Dashboard
- **Purpose:** Central hub for managing course content and tracking student progress.
- **Key Components:** Course list, progress overview, earnings summary.
- **Main Actions:** View courses, manage content, track student progress.
- **Data Shown:** Course status, student progress statistics, earnings.

### Course Builder Screen
- **Purpose:** Create and edit course content.
- **Key Components:** Content editor, module/lesson structure, media upload.
- **Main Actions:** Add/edit/delete course content, upload materials.
- **Data Shown:** Course layout, uploaded media, lesson details.

### Enrollment Stats Screen
- **Purpose:** Monitor student enrollment and engagement.
- **Key Components:** Enrollment list, engagement graphs.
- **Main Actions:** View enrollment details, track student engagement.
- **Data Shown:** Student names, enrollment dates, course completion percentages.

### Payout/Earnings View
- **Purpose:** Track earnings and payout status.
- **Key Components:** Earnings summary, payout schedule.
- **Main Actions:** Review earnings, request payouts.
- **Data Shown:** Total earnings, upcoming payouts, completed payouts.

## Student Persona

### Student Dashboard
- **Purpose:** Access and manage personal learning journey.
- **Key Components:** Course enrollment, progress tracker, certificate section.
- **Main Actions:** Access courses, track progress, download certificates.
- **Data Shown:** Enrolled courses, progress percentage, earned certificates.

### Course Player Screen
- **Purpose:** View and interact with course content.
- **Key Components:** Video player, downloadable resources, notes area.
- **Main Actions:** Play course videos, download resources, take notes.
- **Data Shown:** Lesson video, supplementary materials, note summaries.

### Progress and Learning History 
- **Purpose:** Monitor learning achievements and history.
- **Key Components:** Progress chart, history log.
- **Main Actions:** Review past courses, assess learning progress.
- **Data Shown:** Completed modules, assessment results, historical achievements.

### Billing and Subscription Management
- **Purpose:** Manage billing details and subscription services.
- **Key Components:** Subscription details, payment methods.
- **Main Actions:** Update payment information, change subscription plans.
- **Data Shown:** Current subscription, billing history, payment information.

## Public Screens

### Landing Page
- **Purpose:** Introduce the platform to new users.
- **Key Components:** Introduction sections, benefits list, testimonials.
- **Main Actions:** Explore the platform, start the signup process.
- **Data Shown:** Platform features, success stories, calls to action.

### Course Catalog/Preview
- **Purpose:** Display available courses for browsing.
- **Key Components:** Course thumbnails, search/filter options.
- **Main Actions:** Search courses, preview course content.
- **Data Shown:** Course titles, descriptions, instructor names.

### Pricing and Checkout
- **Purpose:** Facilitate course and subscription purchases.
- **Key Components:** Pricing options, checkout form.
- **Main Actions:** Select purchasing options, complete transactions.
- **Data Shown:** Pricing details, subscription benefits, payment summaries.

### Auth Screens (Sign Up/In, Forgot Password)
- **Purpose:** Handle user authentication and account recovery.
- **Key Components:** Login form, password recovery link.
- **Main Actions:** Log in, reset password.
- **Data Shown:** Authentication fields, recovery instructions.

---

**Assumptions & Questions:**
- Assumed that UI follows a straightforward layout for ease of use.
- Are there any additional personas that need specific screens?
- Should there be any language localization considerations beyond English?

---

# Edge Cases, Constraints, and Open Questions

## Edge Cases
- **Subscription Downgrades**: How will subscription downgrade scenarios be managed, especially with immediate vs end-of-cycle downgrades?
- **Instructor Payout Variability**: Dealing with unusual cases like refund adjustments and multiple payout configurations.
- **Partial Course Access**: Handling cases where users might have access to only parts of courses due to specific subscription levels.

## Constraints
- **Budget and Timeline**: 
  - Target budget: $25-50k with a 4-month timeline for MVP.
  - Budget flexibility ranges between $20-60k.

- **Compliance**:
  - Ensure compliance with data protection regulations (e.g., GDPR, CCPA).
  - Stripe Billing necessitates adherence to financial compliance standards.

- **Geo and Languages**:
  - English-first interface at launch; consider geo-based restrictions or requirements.
  
- **Technology**:
  - Must avoid plugin constraints specific to WordPress fallback options.

## Open Questions (Prioritized)
1. Should subscriptions unlock all courses on the platform or only a specific subscription catalog?
2. What are you trying to build (in one sentence), and who is it for?
3. How do we handle refunds and subscription cancellations that might affect instructor payouts?
4. How will trial subscriptions be managed, and what will be the conversion strategy?
5. What specific geographic markets should be prioritized based on audience and compliance? 

Feel free to provide further details on these questions to help refine the product scope and ensure alignment with business goals.

---

# Acceptance Criteria & Success Metrics

## Acceptance Criteria

### 1. Subscription Management
- **Given** a user selects a subscription plan, **when** they proceed to checkout, **then** the payment process must be seamless with immediate access to the selected courses.
- **Given** a user wants to upgrade their plan, **when** they choose a new plan, **then** the subscription must adjust accordingly without losing access to existing courses.

### 2. Role-Based Access Control (RBAC)
- **Given** a user is an admin, **when** they log in, **then** they should have access to all management and reporting features.
- **Given** a user is a student, **when** they log in, **then** they should only have access to their course dashboard, learning history, and profile management.
- **Given** a user is an instructor, **when** they log in, **then** they should be able to create and manage courses, view student progress, and check payout details.

### 3. Course Authoring and Publishing
- **Given** an instructor submits a course for approval, **when** an admin reviews it, **then** the admin should be able to approve or reject it, with a notification sent to the instructor.

### 4. Progress Tracking and Certification
- **Given** a student completes a course, **when** they view their dashboard, **then** a completion certificate should be available for download.

### 5. Payout Management
- **Given** an enrollment occurs, **when** an instructor logs in, **then** their earnings should reflect the new enrollment.
- **Given** the end of a payout cycle, **when** an admin reconciles payouts, **then** all instructor earnings must be accurate and ready for disbursement.

## Success Metrics

### Product Metrics
- **User Engagement**: Target 70% of subscribed students actively participating in at least one course per month.
- **Course Completion**: Achieve a course completion rate of 50% within 3 months post-subscription.

### Business Metrics
- **Revenue Growth**: Reach $50k in monthly recurring revenue within 6 months of launch.
- **Conversion Rate**: Attain a 10% conversion rate from free trials to paid subscriptions.

### Quality/Operations Metrics
- **Uptime**: Ensure 99.9% uptime for the platform at launch.
- **Response Time**: Keep average page load times under 2 seconds.
- **Customer Support Efficiency**: Resolve 90% of customer support tickets within 24 hours.

## Assumptions & Questions
- Assumption: Subscription plans include access to all available courses unless stated otherwise.
- Question: Should individual course purchases be prioritized for post-MVP phases?
- Question: What specific success metrics would most align with the stakeholders' broader business goals?
