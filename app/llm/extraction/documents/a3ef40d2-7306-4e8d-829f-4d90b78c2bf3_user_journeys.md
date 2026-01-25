# User Journeys Document

**Job ID:** a3ef40d2-7306-4e8d-829f-4d90b78c2bf3

> This document is generated from chat discovery + extracted knowledge files.

# Executive Summary

This product is a secure and scalable SaaS platform designed for creating and delivering educational content. Built with a balanced architecture using Next.js, NestJS, and Postgres, it facilitates multi-role access for admins, teachers, and students while ensuring high security and maintainability.

### Who It Is For:
- **Admins**: Platform authority managing governance, compliance, and monetization.
- **Teachers**: Content creators publishing courses and earning revenue.
- **Students**: Learners accessing courses and obtaining certifications.

### Primary Outcomes:
- Streamlined creation and delivery of educational content.
- Secure and compliant platform operations.
- Transparent and efficient payment and payout processes.
- Enhanced user engagement through certificates and analytics.

### Key Capabilities:
- **Role-Based Access Control (RBAC)**: Tailored permissions for admins, teachers, and students.
- **Secure Payment Processing**: Subscriptions and one-off purchases via Stripe.
- **Automated Payout System**: Efficient payouts to teachers using Stripe Connect.
- **Robust Course Management**: Course creation, versioning, and moderation.
- **Certificate Issuance and Verification**: Awarding and validating completion certificates.
- **Comprehensive Audit Logging**: Maintains audit trails for compliance and transparency.

---

## Personas & Roles

### 1. Admin - Platform Authority

**Goals:**
- Ensure smooth platform operations and governance.
- Maintain compliance and security standards.
- Oversee monetization and payouts.

**Pain Points:**
- Balancing security and user experience.
- Handling compliance obligations and data security.
- Efficient processing of teacher approvals and content moderation.

**Permissions/Role:**
- Full access to platform's administrative tools.
- Manage users, roles, content, and financial transactions.

**Success Metrics:**
- High compliance and security adherence.
- Efficient handling of user verifications and disputes.
- Positive feedback from teachers and students.

### 2. Teacher - Course Creator

**Goals:**
- Create engaging courses that attract students.
- Maximize earnings through course sales and subscriptions.
- Receive timely and accurate payouts.

**Pain Points:**
- Navigating course creation tools effectively.
- Ensuring courses meet platform standards for approval.
- Understanding and managing revenue streams.

**Permissions/Role:**
- Access to course creation, editing, and pricing tools.
- View earnings and payout options.

**Success Metrics:**
- High course approval rate.
- Positive student engagement and feedback.
- Consistent growth in earnings.

### 3. Student - Learner

**Goals:**
- Discover and enroll in courses of interest.
- Successfully complete courses and earn certificates.
- Manage subscriptions effectively.

**Pain Points:**
- Finding courses that match learning goals.
- Tracking progress and completion easily.
- Managing subscription and purchase options.

**Permissions/Role:**
- Access to course catalog, learning dashboard, and certificates.
- Manage personal account settings and payments.

**Success Metrics:**
- High course completion and satisfaction rates.
- Effective use of subscription benefits.
- Positive course feedback and ratings.

### 4. Compliance Officer (Assumption)

**Goals:**
- Ensure platform operations comply with regulatory standards.
- Monitor data security and privacy practices.

**Pain Points:**
- Keeping up with evolving compliance regulations.
- Ensuring all platform components adhere to compliance standards.

**Permissions/Role:**
- Access to audit logs and compliance reports.
- Input on data handling policies and processes.

**Success Metrics:**
- Zero compliance breaches.
- Successful audits and regulatory reviews.

### Assumptions:
- The Compliance Officer role is inferred based on security and compliance needs.
- Details about specific user personas may need user confirmation.

### Questions:
- Are there specific compliance obligations or roles beyond Admin, Teacher, and Student?
- Is a distinct Compliance Officer expected, or are these duties included under Admin or another role?

---

# Core User Journeys

## New User Onboarding Journey

### Trigger
- A new user lands on the platform and decides to sign up.

### Steps
1. **Landing Page**: User visits the homepage and clicks on "Sign Up."
2. **Account Creation**:
   - User selects role: Admin, Teacher, or Student.
   - Fills in registration form with email and password or uses SSO.
3. **Email/Phone Verification**:
   - User receives a verification code via email or SMS.
   - Enters the code to verify their account.
4. **Role-Specific Setup**:
   - Admin: Proceeds to configure platform settings.
   - Teacher: Completes profile and submits for verification.
   - Student: Explores course catalog.

### System Behaviors
- Sends verification email/SMS.
- Updates user role and permissions.
- Logs the action in the audit log.

### Completion Criteria
- User account is verified and active with a confirmed role.

### Failure/Edge Cases
- Email/SMS not received: Option to resend verification.
- Incorrect verification code: Prompts re-entry and limits attempts.

## Main Value Journey (Subscription/Purchase)

### Trigger
- A registered user decides to subscribe or purchase a course.

### Steps
1. **Course/Browse Catalog**:
   - User searches for desired course.
2. **Course Selection**:
   - Views course details.
3. **Purchase/Subscribe**:
   - Chooses between subscription or one-time purchase.
4. **Payment Processing**:
   - Enters payment details via Stripe.
5. **Confirmation**:
   - Receives confirmation of successful purchase.
6. **Access Content**:
   - Gains access to the course content.

### System Behaviors
- Processes payment securely via Stripe.
- Sends purchase confirmation email.
- Updates user access permissions.

### Completion Criteria
- User can access purchased/subscribed content.

### Failure/Edge Cases
- Payment failure: Notifies user to retry.
- Course availability issue: Informs user of delays.

## Admin/Operator Journey

### Trigger
- Admin logs in to manage platform operations.

### Steps
1. **Login and Dashboard View**:
   - Accesses the admin dashboard.
2. **User and Role Management**:
   - Reviews and modifies user roles.
3. **Content Moderation**:
   - Approves or declines teacher-submitted courses.
4. **Subscription and Revenue Oversight**:
   - Monitors subscriptions and financials.
5. **Audit and Reports**:
   - Generates audit logs and reports.

### System Behaviors
- Updates permissions and logs actions.
- Sends notifications to concerned roles (e.g., in case of a moderation outcome).

### Completion Criteria
- Tasks like moderation and role changes are complete, with notifications sent.

### Failure/Edge Cases
- System outage: Temporary inability to access dashboard.
- Insufficient permissions: Alerts admin to role restrictions.

## Teacher/Instructor Journey

### Trigger
- A verified teacher wants to create and publish a new course.

### Steps
1. **Login and Dashboard Access**:
   - Accesses the teacher dashboard.
2. **Profile and Verification**:
   - Updates personal profile, if needed.
3. **Course Creation**:
   - Uses course builder to create a course.
   - Uploads content (videos, docs).
4. **Course Submission**:
   - Submits for admin approval.
5. **Price Setting**:
   - Configures pricing.
6. **Engagement and Feedback**:
   - Interacts with students through comments/questions.
7. **Earnings and Analytics**:
   - Reviews earnings and performance metrics.

### System Behaviors
- Sends notifications for course submission status.
- Logs course creation and updates.
- Generates earnings insights.

### Completion Criteria
- Course is live and visible in catalog, earnings start reflecting.

### Failure/Edge Cases
- Rejection of course: Provides feedback for revisions.
- Media uploading issues: Allows retry or support contact.

## Open Questions
- Does the user require any specific compliance features (e.g., SOC 2, GDPR)?
- Is a distinct Support role necessary beyond the Admin, Teacher, and Student roles for V1?
- Which role interface should be prioritized: Student, Teacher, or Admin?

---

# UI Touchpoints (Screens & Navigation)

## Admin Persona

### 1. Admin Dashboard
- **Purpose**: Provide an overview of platform activities and metrics.
- **Key Components**: Dashboard widgets, navigation panel.
- **Main Actions**: View system metrics, navigate to detailed sections.
- **Data Shown**: User statistics, revenue reports, pending approvals.

### 2. User & Role Management
- **Purpose**: Manage platform users and roles.
- **Key Components**: User list, role assignment tool.
- **Main Actions**: Add/edit/delete users, assign roles.
- **Data Shown**: User profiles, roles, activity status.

### 3. Teacher Verification & Approval
- **Purpose**: Handle teacher applications and verifications.
- **Key Components**: Application list, approval buttons.
- **Main Actions**: Approve/reject applications.
- **Data Shown**: Teacher profile data, application status.

### 4. Course Review & Moderation
- **Purpose**: Ensure course content meets platform standards.
- **Key Components**: Course list, approval tools.
- **Main Actions**: Approve/reject courses, flag content.
- **Data Shown**: Course details, moderation status.

### 5. Subscription & Pricing Control
- **Purpose**: Manage subscription models and pricing.
- **Key Components**: Subscription table, pricing editor.
- **Main Actions**: Edit pricing, set subscription rules.
- **Data Shown**: Current plans, pricing options.

### 6. Revenue & Payout Oversight
- **Purpose**: Oversee financial transactions and teacher payouts.
- **Key Components**: Payout history, revenue analytics.
- **Main Actions**: View financial reports, initiate payouts.
- **Data Shown**: Revenue data, payout schedules.

### 7. Certificate Templates & Rules
- **Purpose**: Design and manage certificate templates.
- **Key Components**: Template editor, rules configurator.
- **Main Actions**: Create/edit certificates.
- **Data Shown**: Available templates, issuance rules.

### 8. Reports & Analytics
- **Purpose**: Access detailed analytics and reports for the platform.
- **Key Components**: Analytics dashboard, report generator.
- **Main Actions**: Generate and download reports.
- **Data Shown**: Usage statistics, engagement metrics.

## Teacher Persona

### 1. Teacher Profile & Verification
- **Purpose**: Set up and verify teacher profile.
- **Key Components**: Profile editor, verification upload.
- **Main Actions**: Edit profile, submit verification documents.
- **Data Shown**: Personal details, verification status.

### 2. Course Creation & Editing
- **Purpose**: Develop and manage course content.
- **Key Components**: Course builder, content uploader.
- **Main Actions**: Add/edit course content, set course status.
- **Data Shown**: Course materials, version history.

### 3. Content Upload (Video, Docs, Resources)
- **Purpose**: Upload educational materials.
- **Key Components**: File uploader, media manager.
- **Main Actions**: Upload files, organize resources.
- **Data Shown**: Upload progress, file previews.

### 4. Course Pricing Configuration
- **Purpose**: Define course pricing and access.
- **Key Components**: Pricing editor, discount tool.
- **Main Actions**: Set prices, configure access.
- **Data Shown**: Current pricing, discount settings.

### 5. Enrollment & Performance Insights
- **Purpose**: Monitor student engagement and course performance.
- **Key Components**: Enrollment dashboard, performance charts.
- **Main Actions**: View insights, analyze trends.
- **Data Shown**: Enrollment numbers, course completion rates.

### 6. Earnings Dashboard
- **Purpose**: Track and manage earnings.
- **Key Components**: Earnings graph, payout request form.
- **Main Actions**: Request payouts, review earnings.
- **Data Shown**: Monthly earnings, pending payouts.

## Student Persona

### 1. Account Registration & Login
- **Purpose**: Allow students to register and access their accounts.
- **Key Components**: Registration form, login fields.
- **Main Actions**: Create account, log in, reset password.
- **Data Shown**: Input fields for credentials.

### 2. Course Discovery & Search
- **Purpose**: Explore available courses.
- **Key Components**: Search bar, course catalog.
- **Main Actions**: Search courses, filter by category.
- **Data Shown**: Course listings, categories.

### 3. Subscription Management
- **Purpose**: Manage enrollment and subscriptions.
- **Key Components**: Subscription overview, management tools.
- **Main Actions**: Subscribe, cancel subscription, view benefits.
- **Data Shown**: Active subscriptions, billing cycle.

### 4. Course Purchase Flow
- **Purpose**: Facilitate course purchases.
- **Key Components**: Pricing page, checkout form.
- **Main Actions**: Purchase courses, apply discounts.
- **Data Shown**: Course details, pricing, totals.

### 5. Learning Dashboard
- **Purpose**: Central hub for course engagement.
- **Key Components**: Dashboard view, progress indicators.
- **Main Actions**: Access courses, track progress.
- **Data Shown**: Current courses, progress bars.

### 6. Progress Tracking
- **Purpose**: Monitor learning progress and achievements.
- **Key Components**: Progress tracker, milestones.
- **Main Actions**: Track progress, view achievements.
- **Data Shown**: Completion percentages, milestones achieved.

### 7. Completion Validation
- **Purpose**: Validate and confirm course completions.
- **Key Components**: Completion checklist, validator tool.
- **Main Actions**: Validate completion, obtain certificates.
- **Data Shown**: Checklist items, validation status.

### 8. Certificate Download & Verification
- **Purpose**: Access and verify earned certificates.
- **Key Components**: Certificate list, download links.
- **Main Actions**: Download certificates, share verification URL.
- **Data Shown**: Certificate details, verification status.

## Assumptions
- All personas have access to a consistent navigation system.
- Pages are mobile-responsive and optimized for tablets.
- UX focuses on minimal onboarding friction.

## Open Questions
- Are there any specific compliance screens needed?
- Is there a need for a dedicated support/help center screen?

---

## Edge Cases, Constraints, and Open Questions

### Edge Cases
- **Payout Delays**: Handling of delayed payouts due to bank holidays or Stripe issues.
- **Course Content Moderation**: Dealing with inappropriate content uploaded by teachers.
- **Subscription Cancellations**: Ensuring students retain access to courses already paid for but not completed.
- **Certificate Validation Errors**: Addressing discrepancies in certificate issuance or validation.
- **Authentication Failures**: Handling failed MFA or account lockouts.

### Constraints
- **Budget**: Mid-range of $40k to $50k. Must ensure all core functionalities are covered within this budget.
- **Timeline**: 
  - Phase 1 (MVP): 14–16 weeks.
  - Phase 2 (Enhancements): 8–12 weeks.
- **Compliance**: 
  - GDPR-aligned data handling, SOC-2 readiness, PCI-DSS compliance.
  - Potential need for additional compliance like HIPAA or enterprise SSO mandates.
- **Geographical Reach**: No explicit geo restrictions mentioned; assuming US compliance is a priority.
- **Languages**: Platform language is not specified; assuming English for V1 unless otherwise stated.
- **Security Posture**: Set to High, which includes JWT/OAuth, encrypted data at rest and in transit, and secure payment handling.

### Open Questions
1. **Compliance Obligations**: Are there any additional compliance obligations beyond the stated ones?
2. **Security Level Confirmation**: Is the High security posture the final requirement, or are adjustments needed?
3. **Support Role**: Do we need a distinct Support role for V1, or is the Admin role sufficient?
4. **Interface Priority**: Should we prioritize designing the Student learning experience, Teacher course creation, or Admin moderation/ops first? 
5. **Language Requirements**: Are there any additional language requirements for V1 beyond English?

If further clarification is required, these questions should be addressed with stakeholders before proceeding.

---

# Acceptance Criteria & Success Metrics

## Acceptance Criteria

### Admin Features

- **Platform-Wide Dashboard**
  - **Given** an Admin logs into the dashboard  
  - **When** they access platform analytics  
  - **Then** they should see real-time data on user activity, subscriptions, and revenue.

- **User & Role Management**
  - **Given** a request to manage roles  
  - **When** the Admin updates user roles  
  - **Then** the changes should reflect immediately and be logged in the audit trail.

- **Teacher Verification & Approval**
  - **Given** a new teacher application  
  - **When** the Admin verifies and approves the teacher  
  - **Then** the teacher should receive a confirmation notification and appear as active in the system.

### Teacher Features

- **Course Creation & Editing**
  - **Given** a Teacher starts creating a course  
  - **When** they save their progress  
  - **Then** the course should be saved as a draft, and the Teacher should receive a confirmation message.

- **Earnings Dashboard**
  - **Given** a Teacher accesses their earnings dashboard  
  - **When** they request a payout  
  - **Then** the payout should be processed through Stripe Connect, and a notification should confirm the transaction.

### Student Features

- **Course Discovery & Search**
  - **Given** a Student visits the course catalog  
  - **When** they search for a course  
  - **Then** they should see relevant results, which they can add to their cart or wishlist.

- **Subscription Management**
  - **Given** a Student subscribes to the platform  
  - **When** they manage their subscription settings  
  - **Then** changes should take effect immediately, with confirmation details sent via email.

## Success Metrics

### Product Metrics

- **User Engagement**: 
  - Target 70% monthly active users. 
- **Course Completion Rate**: 
  - Aim for 60% average completion across courses.

### Business Metrics

- **Revenue Growth**: 
  - Achieve a 20% monthly increase in subscription revenue.
- **Teacher Retention**: 
  - Maintain at least an 80% retention rate among active teachers.

### Quality/Operations Metrics

- **System Uptime**: 
  - Ensure 99.5% uptime.
- **Response Time**: 
  - Average response time for page loads under 3 seconds.

## Assumptions 

- Stripe Connect is the selected payout method.
- Auth0 or Clerk will be implemented for secure authentication.
- High security posture is part of the ongoing project goals.

## Questions

1. Are there specific user engagement metrics beyond monthly active users that are considered critical?
2. Would a distinct support role affect the acceptance criteria for admin tasks?
3. Does the team require specific quality assurance procedures beyond standard practices?
