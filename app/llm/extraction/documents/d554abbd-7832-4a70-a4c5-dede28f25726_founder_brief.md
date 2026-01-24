# Founder & Team Brief

**Job ID:** `d554abbd-7832-4a70-a4c5-dede28f25726`


## Table of Contents
- Executive Summary (Founder-friendly)
- Problem, Solution, and Business Value
- Users, Roles, and High-level User Flows
- Feature Set (Detailed, Grouped)
- Scope Split: MVP vs V1 vs V2
- Budget, Timeline, and Tradeoffs
- Risks, Assumptions, and Open Questions
- Next Steps


## Executive Summary (Founder-friendly)

We are building a versatile online learning platform designed to cater to students, instructors, and administrators. The application aims to provide a seamless learning experience through a student-focused mobile app and a comprehensive web application for instructors and admins. Our solution integrates an AI learning assistant to personalize education, making it accessible on both iOS and Android devices. This platform will be launched within a budget of $50k–$80k over an 8-month timeline, emphasizing scalability and long-term value.

### Target Audience

- **Students:** Accessible learning via a dedicated mobile app.
- **Instructors:** Web-based tools for course creation and monitoring.
- **Administrators:** Advanced platform management capabilities via the web.

### Key Capabilities

- **AI Learning Assistant:** Integrated into web and mobile for personalized learning experiences.
- **Subscription and Purchase Models:** Hybrid monetization through subscriptions (monthly/annual) and one-off course purchases.
- **Comprehensive Role-Based Access:** Customizable through Clerk or Auth0, supporting 3 fixed roles for users.
- **Instructor Payouts:** Managed via Stripe Connect, tied to enrollment counts.
- **Scalable and Flexible Tech Stack:** Custom build using React Native, Next.js, and NestJS, ensuring alignment with modern web standards.

### Why It Matters

With a focus on breaking geographical and technological barriers, this platform enables students to learn anywhere and anytime while providing instructors with efficient tools for course delivery and administration. The hybrid monetization strategy ensures revenue growth while maintaining accessibility.

Success looks like launching a fully operational platform within budget and on time, delivering a superior learning experience across all devices.


## Problem, Solution, and Business Value

### Problem

1. **Platform Limitations**: Existing platforms like Thinkific and Teachable often restrict customization, leading to inadequate long-term scalability and flexibility for businesses aiming to offer a unique learning experience.

2. **Engagement and Accessibility**: Users need the ability to learn anytime and anywhere, requiring a seamless experience across both mobile (iOS and Android) and web platforms, coupled with modern UI/UX design.

3. **Complex Monetization**: Managing a hybrid series of revenue channels through subscriptions, one-off purchases, and instructor payouts requires a robust system to handle entitlements, payments, and financial flows efficiently.

4. **Role Management**: Various user roles (students, instructors, admins) need tailored access and administrative capabilities to ensure smooth platform operations and user experience.

5. **Scalability Concerns**: The platform must be built to scale with growing user bases and course offerings while managing backend performance and load efficiently.

### Solution

1. **Custom Technology Stack**: 
   - **Web and Mobile Apps**: Utilize React Native for a student-only mobile app and Next.js for the instructor/admin web platform, all connected to a shared backend with NestJS.
   - **Core Technologies**: Leverage PostgreSQL for the database, Stripe for payment processing, and S3/CDN for media delivery, ensuring a reliable and performance-oriented infrastructure.

2. **AI Integration**: Include an AI learning assistant within both web and mobile applications, potentially harnessing APIs from OpenAI or Anthropic, enhancing user engagement and offering personalized assistance.

3. **Monetization Strategy**: Implement a comprehensive model using Stripe for subscriptions and one-off payments, paired with Stripe Connect for managing instructor payouts, optimizing financial operations with options for monthly and annual plans.

4. **Role-Based Access Control (RBAC)**: Introduce Clerk/Auth0 for authentication and role management, ensuring secure and efficient management of user permissions and access.

5. **Scalable Backend Systems**: Employ Redis and BullMQ for managing asynchronous tasks, enhancing platform scalability and performance in handling emails, certificate issuance, and financial transactions.

### Business Value

- **Increased Engagement**: By providing cross-platform access and an AI learning assistant, the platform fosters higher user retention and engagement, driving more educational interactions and course completions.

- **Revenue Growth**: A diversified monetization structure with subscriptions and one-off payments maximizes revenue potential. The integrated payout model incentivizes instructors, creating a thriving learning ecosystem.

- **Operational Efficiency**: Advance capabilities in admin controls and role management streamline platform operations, reducing administrative overhead and enabling focus on strategic growth activities.

- **Scalability and Longevity**: The custom-build approach guarantees long-term scalability, supporting growing user demands and feature expansions without platform constraints.

- **Measured Outcomes**: Tracking of explicit financial events, entitlements, and user activity translates into actionable insights, contributing to continuous improvement and growth forecasting.

- **Budget and Timeline Adherence**: Structured planning within a $50k–$80k budget and an 8-month timeline ensures that the solution delivers value promptly and cost-effectively.

---

*Open Questions*
- Should mobile apps for instructors/admins achieve parity with the web version in v1?
- Will a single subscription unlock access to all eligible courses, or are multiple subscriptions to individual courses/teachers necessary?


### Users, Roles, and High-level User Flows

#### Roles

1. **Student**
2. **Instructor**
3. **Admin**

---

#### Student Role

**Happy Path Flows:**

1. **Browse Courses:**
   - Open the mobile app.
   - Access the course catalog through the landing page.
   - Search or filter by categories, ratings, or instructors.

2. **Purchase Course:**
   - Select a course from the catalog.
   - Choose to buy the course or subscribe to available plans.
   - Complete the transaction using Stripe, ensuring secure payment.

3. **Engage with Course:**
   - Access purchased courses through “My Courses”.
   - Start lessons using the course player.
   - Use the AI learning assistant for guidance and queries.

4. **Track Progress:**
   - View course progress on the dashboard.
   - Check lesson completion and milestones.

5. **Receive Certificates:**
   - Complete all required lessons.
   - Automatically receive a completion certificate via email.

6. **Manage Account:**
   - Update profile and billing details.
   - Review subscription status.

**Edge Cases:**

- **Failed Payment:**
  - If a payment fails, the student is notified and can retry or use a different payment method.

---

#### Instructor Role

**Happy Path Flows:**

1. **Dashboard Access:**
   - Log in via the web application.
   - Access the instructor dashboard to view key metrics.

2. **Create Course:**
   - Use the course builder to create a new course.
   - Upload materials and media (integrated with S3/CDN).

3. **Monitor Enrollments:**
   - Track student enrollments and course views.
   - View breakdowns by course/module.

4. **Payout Management:**
   - Check payout reports linked to enrollments.
   - Manage payout settings via Stripe Connect.

**Edge Cases:**

- **Content Approval Required:**
  - Admin moderation may delay the publication of new content if approval is required.

---

#### Admin Role

**Happy Path Flows:**

1. **User & Role Management:**
   - Log in via the web application.
   - Manage users and assign roles (e.g., promoting a student to instructor).

2. **Course Moderation:**
   - Review and approve new courses submitted by instructors.

3. **Monitor Platform Activity:**
   - Access reports on platform usage, revenue, and subscriptions.

4. **Subscription and Revenue Control:**
   - Define subscription-eligible courses.
   - Adjust revenue share settings for instructors.

5. **Manage Payouts:**
   - Oversee payout schedules.
   - Resolve any discrepancies in instructor payouts.

**Edge Cases:**

- **Enrollment Verification:**
  - Review flagged enrollments for potential fraud or policy violations.

---

#### Open Questions

- Do students subscribe to the entire platform or individual instructors/courses?
- Should the mobile app eventually provide full functionality for instructors and admins like the web application?


## Feature Set (Detailed, Grouped)

### Authentication (Auth)
- **User Roles:** 
  - Three fixed roles: Student, Instructor, Admin.
  - Role-based access control via Clerk/Auth0.
- **User Authentication:**
  - Sign up/in, forgot password, and email verification.
  
### Mobile Application (Student v1)
- **Core Student Flows:**
  - Browse courses, purchase, course player.
  - Track progress and access certificates.
  - Manage billing information.

- **Platform Availability:**
  - Support for both iOS and Android.

### Web Application (Instructor & Admin)
- **Instructor Features:**
  - Dashboard access for course management.
  - Tools for building courses, tracking enrollments and analytics.
  - Profile and verification management.
  - Payout management via Stripe Connect.

- **Admin Features:**
  - User and role management.
  - Course approval and moderation.
  - Subscription, orders, and refunds handling.
  - Payout controls and platform settings.
  - Reporting capabilities.

### Content Management
- **Catalog and Search:**
  - Course catalog with search and filtering.
  - Course detail pages with pricing information.
  
- **Content Delivery:**
  - Video/file hosting integration with S3-compatible storage and CDN.
  - Lesson completion tracking.

### Payments and Monetization
- **Payment Options:**
  - Platform subscriptions (monthly/annual) and one-off course purchases via Stripe.
  - Subscription grants access to a specific catalog scope.
  - Entitlements system to verify user access to courses.

- **Transaction Management:**
  - Every transaction recorded as a ledgered event: subscription invoices, renewals, one-off payments, refunds, chargebacks.
  
- **Instructor Payouts:**
  - Payouts tied to enrollments for one-off purchases and subscriptions.
  - Admin can define subscription-eligible courses and set revenue shares.

### AI Learning Assistant
- **Integration:**
  - Included in both web and mobile applications.
  - Possibly leveraging OpenAI or Anthropic for backend services.

### Notifications
- **Email Notifications:**
  - Managed through Postmark or SendGrid.
  - Triggered for events like receipts, enrollment confirmations, certificate issuances, payout activities.

- **Push Notifications:**
  - Delivered via Firebase Cloud Messaging/APNs for mobile updates.

### Background Jobs and Scalability
- **Asynchronous Task Management:**
  - Redis and BullMQ used for background jobs (e.g., certificate issuance, email dispatch, payout processing).
  
- **Platform Scalability:**
  - Designed to support multiple instructors and role-based management with centralized administrative controls.

### Open Questions
- **Mobile Parity:**
  - Decision needed on whether the mobile app should support instructor/admin roles in v1 or if it remains student-only.

- **Subscription Model:**
  - Clarification required on whether students subscribe to the entire platform or to individual teachers/courses.


# Scope Split: MVP vs V1 vs V2

## MVP

- **Student Mobile App (Core Features)**
  - **Key Focus**: Launch a student-only mobile application supporting iOS and Android.
  - **Features**:
    - Course browsing and search
    - Course purchase (subscriptions and one-off)
    - Course player with progress and completion tracking
    - Certificate generation and verification
    - User profile and billing management
  - **Rationale**:
    - Prioritize student access to learning anytime, anywhere.
    - Align with budget of $50k–$80k and 8-month timeline.
    - Establish revenue stream through subscriptions and course purchases.

- **Web Application (Instructor and Admin)**
  - **Access**:
    - Web-based dashboard for instructor and admin roles.
  - **Features**:
    - Role-based access control
    - Course management and analytics for instructors
    - Basic admin controls for user management and course approval
  - **Rationale**:
    - Ensures initial launch includes necessary functionalities for instructors and admins.
    - Utilizes Next.js for responsive design, optimizing long-term growth potential.

## V1

- **Enhanced Mobile Functionality**
  - **Features**:
    - Additional notifications system
    - Introduction of AI learning assistant as a backend service
  - **Rationale**:
    - Improves student engagement and learning efficacy.
    - Builds on existing infrastructure while introducing valuable AI tools.

- **Expanded Web Capabilities**
  - **Instructor Features**:
    - Payout analytics and more detailed course analytics
  - **Admin Features**:
    - Advanced subscription, refund management, and detailed reports
  - **Rationale**:
    - Supports more complex operations and analytics for instructors.
    - Enhances platform management for admins, maintaining scalability.

## V2

- **Full Feature Parity Across Platforms**
  - **Objective**: Achieve feature parity for student, instructor, and admin roles across web and mobile platforms.
  - **Rationale**:
    - Addresses open question regarding mobile parity for instructor/admin roles.
    - Maximizes accessibility and usability by extending all key functionalities to mobile.

- **Advanced Learning Tools and Analytics**
  - **Additions**:
    - Enhanced AI learning assistant capabilities
    - Comprehensive analytics dashboards for all user roles
  - **Rationale**:
    - Leverages AI for personalized learning paths and recommendations.
    - Provides deeper insights and tracking possibilities for both users and administrators.

## Open Questions

- **Subscription Model**: Clarification needed on whether subscriptions are platform-wide or course/teacher-specific.


# Budget, Timeline, and Tradeoffs

## Timeline Estimate
- **Launch Target:** 8 months
- **Project Phases:**
  - Initial focus on student-only mobile app (iOS and Android) and web application for instructors and admins.
  - Integration of AI learning assistant as a separate backend service.

## Budget Bands

### Low Budget: $50k
- **Scope:**
  - Core student mobile app features: browse, purchase, course player, progress, certificates, billing.
  - Essential web functionalities for instructors/admins.
  - Basic integration of AI learning assistant.
- **Tradeoffs:**
  - Limited customizations and potential reliance on existing LMS platforms like Thinkific/Teachable for non-core features.
  - Minimal mobile companion apps for instructors and admins.

### Medium Budget: $65k
- **Scope:**
  - Enhanced feature set for mobile app with additional student flows.
  - More comprehensive web functionalities for instructors/admins.
  - Improved AI assistant capabilities using either OpenAI or Anthropic.
  - Initial implementation of advanced role-based access and payment systems.
- **Tradeoffs:**
  - May still rely on third-party integrations for some advanced functionalities.
  - Possible reduction in visual customizations.

### High Budget: $80k
- **Scope:**
  - Full spectrum of features for both mobile and web applications.
  - Advanced AI assistant integration with higher complexity models.
  - Robust backend with complete integration for role-based access, payment systems, and instructor payouts.
  - Extensive UI/UX customizations for a modern, smooth interface.
- **Tradeoffs:**
  - Less flexibility in the timeline to incorporate additional, non-core features post-launch.

## Tradeoffs
- **Platform Choice:** Balancing between a custom-built solution for long-term growth versus a quick deployment via existing platforms for rapid initial launch.
- **Feature Parity:** Deciding whether the mobile version should accommodate instructor/admin roles or remain student-focused in V1.
- **Monetization Options:** Determining whether to enable platform-wide subscriptions or allow subscription to individual courses/teachers.

## Risks
- **Timeline Risks:**
  - Potential delays in feature completion, particularly with AI integration and mobile app development.
  
- **Budget Overruns:**
  - Risk of exceeding budget due to unforeseen technical challenges or scope creep.

- **Technology Risks:**
  - Dependency on third-party services like Stripe, AI providers, and cloud storage could introduce integration complexities or cost variations.

---

### Open Questions
- Should the mobile apps accommodate instructor/admin roles in future releases?
- Do students subscribe to the entire platform or have options for individual course subscriptions?


## Risks, Assumptions, and Open Questions

### Risks

- **Budget Constraints**: Adhering to the $50k–$80k budget while meeting feature and quality expectations might be challenging. There is a risk of cost overruns if unexpected technical issues arise.
- **Timeline Pressure**: The 8-month launch timeline is ambitious given the scope and complexity of features, including the integration of an AI learning assistant.
- **Technical Dependencies**: Reliance on third-party services like Stripe, Clerk/Auth0, and S3 could pose risks if there are service outages or changes in their services.
- **Feature Scope**: The phased rollout, with student-only mobile and web-first for instructors/admins, may not meet the expectations of users who anticipate full parity across platforms.
- **Platform Scalability**: Designing for multiple instructors with centralized admin control and scalability could encounter performance issues if not carefully managed.

### Assumptions

- **User Roles**: It is assumed there will be three fixed roles (Student, Instructor, Admin) managed via Clerk/Auth0.
- **AI Learning Assistant**: Assumed to be integrated using OpenAI or Anthropic APIs, though the specific vendor choice has not been finalized.
- **Payment Processing**: Assumed that Stripe and Stripe Connect will smoothly handle subscriptions, one-off purchases, and instructor payouts without significant integration issues.
- **Custom Tech Stack**: Assumed that the proposed tech stack (React Native, Next.js, NestJS, PostgreSQL, etc.) will support all required features effectively for both mobile and web applications.
- **Fallback Option**: The fallback to a platform LMS (Thinkific/Teachable) only occurs if significant time or scope constraints arise.

### Open Questions

- **Mobile App Parity**: Should mobile apps have full feature parity for instructors and admins or is a student-only version acceptable for the initial launch?
- **Subscription Model**: Do students subscribe to the entire platform with one subscription granting access to all eligible courses, or do they subscribe to individual teachers/courses, allowing multiple subscriptions?
- **AI Vendor Choice**: Which vendor will be chosen for the AI learning assistant (OpenAI or Anthropic), and what implications will this have on integration and cost?
- **Post-launch Support**: What are the plans for post-launch support and potential feature expansions given the tight initial budget and timeline constraints?


### Next Steps

To efficiently move forward with the project, please consider the following actionable items and schedule a workshop to ensure alignment across teams.

#### Checklist

1. **Confirm Technical Decisions:**
   - Finalize the use of OpenAI or Anthropic for the AI learning assistant integration.
   - Decide if PostgreSQL will be managed by Supabase or AWS RDS.
   - Confirm choice between Clerk and Auth0 for authentication and role-based access control.

2. **Design and User Experience:**
   - Schedule work with a UI expert to finalize modern and smooth design criteria.
   - Decide on the presentation of subscription options within the course pages: side-by-side (Subscribe vs. Buy) or another prioritized display.

3. **Feature Scope and Implementation:**
   - Confirm phased rollout plan: emphasis on mobile app for students and web app for instructors/admin.
   - Validate the core features for initial release: course browsing, purchasing, playing, tracking, and certificate generation.
   - Clarify the implementation of notifications strategy with Postmark/SendGrid and Firebase Cloud Messaging/APNs for push notifications.

4. **Monetization Structure Confirmation:**
   - Verify if the subscription model will focus on platform-wide access or individual courses/teachers.

5. **Budget and Timeline Adherence:**
   - Reaffirm the budget constraints of $50k–$80k and the launch timeline of 8 months.

6. **Open Questions Resolution:**
   - Determine how mobile app parity will be addressed in relation to instructor/admin roles.
   - Decide on subscription models: platform-wide vs. individual offerings.

#### Suggested Workshop Agenda (45 minutes)

- **Introduction (5 minutes)**
  - Quick overview of objectives and expected outcomes of the workshop.

- **Technical Decisions (10 minutes)**
  - Discuss and confirm open technical items and architecture decisions.

- **User Experience and Design (10 minutes)**
  - Collaborate on the final design approach and user experience priorities.

- **Feature Scope and Monetization (10 minutes)**
  - Review all feature requirements and decide on subscription strategies.

- **Budget and Timeline (5 minutes)**
  - Ensure all teams understand budget constraints and project timeline goals.

- **Open Discussion (5 minutes)**
  - Address any lingering questions or concerns and outline next steps.

By following these steps and using the workshop to ensure alignment, the project can proceed effectively towards a successful launch.
