# User Journeys Document

**Job ID:** d554abbd-7832-4a70-a4c5-dede28f25726

> This document is generated from chat discovery + extracted knowledge files.

# Executive Summary

This product is a comprehensive learning management platform designed to support both students and instructors. It combines custom-built web and mobile applications, allowing users to access a wide range of educational resources and tools. With a focus on flexibility, the platform provides seamless integration of AI learning assistants to enhance the overall learning experience.

### Who It Is For
- Students seeking flexible and accessible learning options
- Instructors wanting to offer courses and track student progress
- Educational administrators managing course offerings and revenue
- Developers and technical teams implementing scalable learning solutions

### Primary Outcomes
- Enable students to learn anytime, anywhere on both iOS and Android
- Offer instructors efficient tools for course management and payouts
- Provide a scalable, customizable platform that grows with users' needs
- Integrate advanced AI capabilities to support personalized learning

### Key Capabilities
- Hybrid monetization strategy with subscriptions and one-off course purchases
- Comprehensive role-based access control for students, instructors, and admins
- Seamless media delivery with integrated video and file hosting
- Automated instructor payouts based on enrollment counts and revenue events
- Real-time progress tracking and certificate generation for completed courses
- Robust admin controls for managing course eligibility, revenue shares, and platform settings

### Assumptions
- The mobile app will initially be student-only while the web supports all roles.
- Subscription model details regarding access will require clarification. 

### Questions
- Should mobile apps support full functionalities for instructors and admins in the future?
- Will students subscribe to individual courses or the entire platform?

---

## Personas & Roles

### 1. **Alex the Student**

- **Goals**
  - Access a wide range of courses anytime, anywhere.
  - Track learning progress and receive certifications.
  - Find flexible payment options (subscriptions or one-off purchases).

- **Pain Points**
  - Difficulty in finding courses that meet specific needs.
  - Limited access to instructors for personalized learning.
  - Managing progress across multiple courses/platforms.

- **Permissions/Role**
  - Student role: Access to course catalog, purchase courses, view course content, track progress, and download certificates.

- **Success Metrics**
  - High course completion rate.
  - Positive feedback on course content and learning experience.
  - Frequent engagement with the platform and courses.

### 2. **Emma the Instructor**

- **Goals**
  - Create and manage courses effectively.
  - Maximize enrollments and earnings.
  - Access analytics to improve course offerings.

- **Pain Points**
  - Balancing time between teaching and administrative tasks.
  - Difficulty in tracking payouts and earnings.
  - Limited tools for course promotion and student engagement.

- **Permissions/Role**
  - Instructor role: Manage courses, view analytics, access enrollment data, and handle payouts.

- **Success Metrics**
  - High enrollment numbers and positive student reviews.
  - Efficient course management with minimal administrative burden.
  - Consistent and transparent payouts.

### 3. **Sam the Admin**

- **Goals**
  - Ensure smooth platform operations and user satisfaction.
  - Manage subscriptions and revenue effectively.
  - Enforce role-based access and maintain security compliance.

- **Pain Points**
  - Managing a large number of users and instructors.
  - Balancing platform policy enforcement with user experience.
  - Ensuring timely payouts and revenue tracking.

- **Permissions/Role**
  - Admin role: User management, subscription oversight, course moderation, and financial controls.

- **Success Metrics**
  - High user retention and satisfaction rates.
  - Low compliance and operational issues.
  - Accurate and timely financial reports and payouts.

### 4. **Lisa the Founder/Stakeholder**

- **Goals**
  - Launch the platform within the budget and timeline.
  - Achieve high initial user acquisition and retention.
  - Position the platform as a leading learning resource.

- **Pain Points**
  - Balancing investment with returns and scaling quickly.
  - Managing cross-functional teams and communication.
  - Navigating technological challenges and market competition.

- **Success Metrics**
  - On-time and within-budget platform launch.
  - Early adoption metrics and user growth.
  - Positive market positioning and brand recognition.

### Assumptions
- These personas are based on typical roles and therefore assume a user base primarily focused on education (students, instructors, admins).
- The roles include clear distinctions in permissions and responsibilities, which may evolve.

### Open Questions
- Do any additional roles exist within the platform that require consideration?
- Are there specific demographic targets or unique requirements for each persona?

---

# Core User Journeys

## New User Onboarding Journey

**Trigger:** User downloads the app or visits the web platform for the first time.

1. **Access Platform:**
   - User opens the app (iOS/Android) or navigates to the website.
2. **Registration:**
   - User selects "Sign Up."
   - User enters email, password, and optional personal details.
   - System sends an email verification link.
3. **Email Verification:**
   - User clicks verification link.
   - System confirms email and activates user account.
4. **Profile Setup:**
   - User completes profile information (e.g., preferences, learning goals).
5. **Onboarding Guidance:**
   - User receives a guided tour of the platform features.

**System Behaviors:**
- Sends a verification email.
- Confirms registration and welcomes user via push notification.

**Completion Criteria:**
- User’s account is verified and profile is set up.

**Failure/Edge Cases:**
- Link expiration: User requests a new verification email if the link expires.

## Main Value Journey (Subscription/Purchase)

**Trigger:** User decides to purchase a course or subscription.

1. **Browse Catalog:**
   - User searches for courses or browses catalog.
2. **Course/Subscription Selection:**
   - User selects a desired course or subscription plan.
3. **Checkout:**
   - User reviews course details and pricing.
   - User proceeds to checkout.
4. **Payment:**
   - User enters payment details.
   - System processes payment via Stripe.
5. **Confirmation:**
   - System sends confirmation email and receipt.
6. **Access Granted:**
   - User has immediate access to purchased content.

**System Behaviors:**
- Notifies user of successful purchase via email.
- Updates user entitlements granting access.

**Completion Criteria:**
- User gains access to the purchased course/subscription.

**Failure/Edge Cases:**
- Payment failure: User receives an error message, and retry options.

## Admin/Operator Journey

**Trigger:** Admin needs to manage platform content or settings.

1. **Login:**
   - Admin logs into the admin web portal.
2. **Dashboard Access:**
   - Admin accesses the control dashboard.
3. **Content Management:**
   - Admin approves/moderates courses.
   - Admin manages subscriptions/orders/refunds.
4. **Instructor/Revenue Management:**
   - Admin sets revenue share, schedules payouts, and verifies enrollments.
5. **Report Generation:**
   - Admin generates analytical and financial reports.

**System Behaviors:**
- Sends email alerts for important changes (e.g., new course approvals).
- Logs actions for audit trails.

**Completion Criteria:**
- Desired administrative tasks are completed successfully.

**Failure/Edge Cases:**
- Insufficient permissions: Admin receives error message if not authorized for specific actions.

## Instructor Journey

**Trigger:** Instructor logs in to manage courses or view analytics.

1. **Login:**
   - Instructor logs into the web platform.
2. **Dashboard Access:**
   - Instructor views dashboard with course analytics.
3. **Course Creation/Editing:**
   - Instructor creates or edits course content.
   - System supports uploads (videos, documents).
4. **Enrollment Management:**
   - Instructor reviews enrollments and student engagement.
5. **Payout Monitoring:**
   - Instructor accesses payout ledger tied to enrollments.

**System Behaviors:**
- Sends notifications for new enrollments or course updates.
- Generates payout reports for instructor access.

**Completion Criteria:**
- Course content is published/updated.
- Instructor has clear visibility on enrollments and payouts.

**Failure/Edge Cases:**
- Technical issues with content uploads prompt system error messages.

---

### Assumptions and Questions:

- **Assumptions:**
  - Email verification is necessary for all accounts.
  - Payment failures are addressed within the system UX.
  - Instructor and admin functions will be web-first and not available on mobile in v1.

- **Open Questions:**
  - Should students subscribe to the entire platform, or is course-specific subscription preferred?
  - Is it acceptable for the mobile version to have student-only features in v1?

---

# UI Touchpoints (Screens & Navigation)

## Student Persona

### 1. Landing/Marketing Page
- **Purpose**: Introduce the platform and invite potential students to explore courses.
- **Key Components**: Hero banner, course highlights, testimonials, sign-up/login prompts.
- **Main Actions**: Explore courses, Sign up, Log in.
- **Data Shown**: Featured courses, platform benefits, user testimonials.

### 2. Course Catalog/Search
- **Purpose**: Allow students to browse available courses and filter by preferences.
- **Key Components**: Search bar, category filters, course list, pagination.
- **Main Actions**: Search courses, Filter results, View course details.
- **Data Shown**: Course titles, descriptions, ratings, pricing.

### 3. Course Detail Page
- **Purpose**: Provide detailed information about a selected course.
- **Key Components**: Course overview, instructor details, syllabus, pricing options.
- **Main Actions**: Purchase course, Subscribe, Enroll.
- **Data Shown**: Course content, instructor profile, testimonials, available plans.

### 4. Checkout/Payment
- **Purpose**: Facilitate secure transactions for course purchases and subscriptions.
- **Key Components**: Payment form, order summary, billing details.
- **Main Actions**: Enter payment info, Confirm purchase.
- **Data Shown**: Order total, selected courses/plans.

### 5. Student Dashboard
- **Purpose**: Central hub for students to manage their learning activities.
- **Key Components**: Course library, progress tracker, upcoming events.
- **Main Actions**: Continue learning, Track progress, Access certificates.
- **Data Shown**: Enrolled courses, progress stats, upcoming sessions.

### 6. Course Player
- **Purpose**: Provide an interface for course consumption.
- **Key Components**: Video player, lesson list, notes section.
- **Main Actions**: Play/pause videos, Mark lessons as complete.
- **Data Shown**: Video content, lesson resources, completion status.

### 7. Profile/Billing
- **Purpose**: Allow students to manage their profiles and billing information.
- **Key Components**: Personal details, payment methods, subscription status.
- **Main Actions**: Update profile, Change payment info, Manage subscriptions.
- **Data Shown**: User info, billing history, subscription details.

### 8. Certificates
- **Purpose**: Display and verify course completion certificates.
- **Key Components**: Certificate viewer, download options, verification link.
- **Main Actions**: View certificate, Download, Share.
- **Data Shown**: Certificate details, issue date, verification code.

## Instructor Persona

### 9. Instructor Dashboard
- **Purpose**: Provide instructors with a summary of their activities and earnings.
- **Key Components**: Course overview, enrollment stats, income reports.
- **Main Actions**: Analyze data, Manage courses, View payouts.
- **Data Shown**: Course performance, revenue graphs, updated enrollments.

### 10. Course Builder
- **Purpose**: Facilitate course creation and management for instructors.
- **Key Components**: Content uploader, syllabus planner, resource library.
- **Main Actions**: Add content, Organize syllabus, Publish course.
- **Data Shown**: Course outline, media library, release schedule.

### 11. Enrollments/Analytics
- **Purpose**: Provide insights into course performance and student engagement.
- **Key Components**: Enrollment stats, completion rates, feedback.
- **Main Actions**: View analytics, Adjust content, Respond to feedback.
- **Data Shown**: Enrollment trends, engagement metrics, student reviews.

### 12. Payouts
- **Purpose**: Display earnings and manage payout preferences.
- **Key Components**: Earnings summary, payout schedule, transaction history.
- **Main Actions**: View earnings, Set payout preferences.
- **Data Shown**: Revenue details, payout history, upcoming payments.

## Admin Persona

### 13. Admin Dashboard
- **Purpose**: Oversee platform operations and access critical metrics.
- **Key Components**: User management, course approval status, system alerts.
- **Main Actions**: Monitor activity, Approve courses, Manage users.
- **Data Shown**: Platform usage stats, pending approvals, user activity.

### 14. User & Role Management
- **Purpose**: Manage platform users and their roles.
- **Key Components**: User list, role assignments, access controls.
- **Main Actions**: Add/remove users, Assign roles, Edit permissions.
- **Data Shown**: User details, role information, access logs.

### 15. Course Approval/Moderation
- **Purpose**: Review and approve submitted courses.
- **Key Components**: Course submissions, review tools, feedback options.
- **Main Actions**: Approve/Reject courses, Provide feedback.
- **Data Shown**: Course details, moderator notes, submission status.

### 16. Subscriptions/Orders/Refunds
- **Purpose**: Handle financial transactions and resolve billing issues.
- **Key Components**: Order history, refund requests, subscription reports.
- **Main Actions**: Process refunds, Adjust subscriptions.
- **Data Shown**: Transaction data, refund history, active subscriptions.

### 17. Payout Controls
- **Purpose**: Oversee instructor payouts and manage financial settings.
- **Key Components**: Payout settings, revenue share options, payout history.
- **Main Actions**: Configure settings, Review payouts.
- **Data Shown**: Payout distribution, schedule details.

### 18. Platform Settings
- **Purpose**: Manage overall platform configurations.
- **Key Components**: System settings, notification preferences, branding.
- **Main Actions**: Update settings, Configure notifications.
- **Data Shown**: Platform configurations, branding elements.

### 19. Reports
- **Purpose**: Generate detailed reports on platform-wide activities.
- **Key Components**: Report generator, export options, data filters.
- **Main Actions**: Generate, Download reports.
- **Data Shown**: Activity summaries, financial data, usage statistics.

---

### Assumptions & Questions

- **Assumptions**: 
  - Student app in V1 is mobile-only, while instructor/admin is web-only.
  - Visual details such as colors, icons, and typography will be provided by a UI expert.

- **Open Questions**:
  - Should the mobile app in V1 have any instructor functionalities?
  - Is the subscription model for entire platform access or individual courses?

---

# Edge Cases, Constraints, and Open Questions

## Edge Cases
- Handling enrollment changes (additions/cancellations) mid-subscription could complicate payouts and course access management.
- The system must account for refunds or chargebacks on completed courses or subscriptions.
- Ensuring all media content is available and performant across varying internet speeds and device capabilities.
- Handling multi-language support for both content and UI may require dynamic adjustments.

## Constraints
- **Budget**: Total budget size is $50k–$80k.
- **Timeline**: Launch targeted within an 8-month timeframe.
- **Platform**: Initial focus on iOS and Android for student users with web access for instructors and admin.
- **Compliance**: Ensure compliance with data protection regulations such as GDPR and COPPA.
- **Payment Processing**: Use Stripe for subscriptions and one-off payments; manage instructor payouts via Stripe Connect.
- **Role-based Access Control**: Use Clerk or Auth0 with fixed roles (Student, Instructor, Admin).
- **Tech Stack**: Must adhere to the primary stack (React Native, Next.js, NestJS, etc.).
- **Scalability**: The solution should support multiple instructors with centralized administration.

## Open Questions
1. Should mobile apps have full parity for instructor/admin roles, or focus solely on student functionality at v1?
2. Do students subscribe to the entire platform, unlocking eligible courses, or subscribe to individual teachers/courses, allowing multiple subscriptions?
3. How should we differentiate between subscription options and one-off purchases on the course page to maximize user clarity and conversion?
4. What level of integration is necessary for the AI learning assistant, and should it be a core aspect of the user experience upon launch?
5. How do we handle localization for multiple languages, and what languages are prioritized at launch?

**Assumptions:**
- The fallback to Platform LMS (Thinkific/Teachable) is a consideration if budget or timeline constraints cannot be met with a custom build.
- The timeline accounts for potential delays and iteration based on user feedback and technical challenges.

**Further Questions for Consideration:**
- How will engagement and success metrics be measured post-launch to guide subsequent iterations and improvements?
- What strategies are in place for post-launch support and scalability enhancements? 

Please let me know if there are any additional factors or specific details needed for further clarification.

---

# Acceptance Criteria & Success Metrics

## Acceptance Criteria

### 1. Student Mobile Application
- **Course Discovery**
  - *Given* a student user on the mobile app, *when* they search for a course, *then* courses should be filterable by category, instructor, or price.
  
- **Course Purchase**
  - *Given* a student on the course detail page, *when* they choose to purchase or subscribe, *then* the transaction process should be smooth and secured via Stripe.

- **Course Player**
  - *Given* a student who has purchased access to a course, *when* they play a lesson, *then* the content should load without buffering and track progress accurately.

- **Certification**
  - *Given* a student completes a course, *when* they request a certificate, *then* it should be generated and viewable within the app.

### 2. Instructor/Admin Web Application
- **Dashboard Access**
  - *Given* an authenticated instructor or admin, *when* they log in, *then* they should see a personalized dashboard with key metrics and actions.

- **Enrollment Management**
  - *Given* an admin, *when* they access the enrollment section, *then* they should be able to verify and manage enrollments efficiently.

### 3. Backend Integration
- **AI Learning Assistant**
  - *Given* a student using the app, *when* they interact with the AI learning assistant, *then* responses should be accurate and timely.

- **Payment Processing**
  - *Given* any transaction event, *when* processed, *then* it should be logged and handled by Stripe for accurate revenue tracking.

### 4. Notifications and Alerts
- **Email Notifications**
  - *Given* an event such as enrollment or payment, *when* it occurs, *then* an email notification should be sent to the student using Postmark/SendGrid.

## Success Metrics

### Product Metrics
- **User Engagement**
  - Achieve a minimum 60% user engagement rate within the first 3 months post-launch, measured by regular course activity.

- **Feature Utilization**
  - At least 75% of active users to engage with the AI learning assistant within the first 6 months.

### Business Metrics
- **Revenue Targets**
  - Achieve $100,000 in revenue from subscriptions and course purchases within the first 6 months.

- **Instructor Onboarding**
  - Successfully onboard 50 instructors within the first 3 months post-launch.

### Quality/Operations Metrics
- **System Uptime**
  - Maintain a system uptime of 99.5% or higher.

- **Response Time**
  - Ensure average response time for AI assistant interactions is under 3 seconds.

- **Customer Support**
  - Resolve 90% of support tickets within 24 hours.

## Assumptions
- All roles and features as described are achievable and implementable within budget and timeline constraints.
- Instructors and admins are comfortable with a web-only interface initially.

## Open Questions
- Should there be differentiation in subscription models between platform-wide access and instructor/course-specific subscriptions?
- Is it essential for mobile parity across all roles for the initial launch?
