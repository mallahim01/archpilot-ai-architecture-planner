# Founder & Team Brief

**Job ID:** `579f622a-bbbf-4887-a082-62f87090f9ad`


## Table of Contents
- Executive Summary (Founder-friendly)
- Problem, Solution, and Business Value
- Users, Roles, and High-level User Flows
- Feature Set (Detailed, Grouped)
- Scope Split: MVP vs V1 vs V2
- Budget, Timeline, and Tradeoffs
- Risks, Assumptions, and Open Questions
- Next Steps


### Executive Summary (Founder-friendly)

We are building a comprehensive online learning platform designed to cater to educators, learners, and administrators by providing robust course management and monetization tools. Developed to operate seamlessly on both iOS and Android using React Native, the platform ensures consistency and cost efficiency across devices within a budget of $25k–$50k and a 4-month development timeline. 

This platform is particularly valuable for its hybrid monetization model, which includes subscription access and per-course purchase options. It supports a multi-instructor environment, facilitating instructor payouts based on enrollments through a flexible, API-first architecture. By leveraging a managed LMS/e-commerce backbone, the platform efficiently handles complex processes like user roles, content management, and financial transactions.

#### Key Capabilities

- **Cross-Platform Availability**: Seamlessly supports web and mobile applications using a shared API, ensuring uniform experiences across iOS and Android.

- **Comprehensive Monetization**: Offers both subscription models and a la carte purchases, unlocking all courses for subscribers initially, with future options for individual purchases.

- **Flexible Course Management**: Includes tools for course creation, delivery, progress tracking, and certification, catering to both instructors and students effectively.

- **Advanced User Roles**: Implements role-based access control for students, instructors, and admins, with tailored features for each role, including dashboards and analytics.

- **Secure and Efficient Transactions**: Powered by Stripe for payments, with instructor payouts calculated based on enrollments, ensuring transparent financial operations.

Success looks like a tightly integrated platform that scales with user needs, enhances learning experiences, and supports robust revenue models for educators.


## Problem, Solution, and Business Value

### Problem

1. **Platform Inconsistencies Across Devices**
   - Need for a seamless learning experience on both iOS and Android platforms.
   - Issues with managing separate systems for web and mobile applications.

2. **Complex Monetization and Payout Models**
   - Requirement for a flexible monetization model that supports subscriptions, a la carte purchases, and instructor payouts.
   - Challenges in managing revenue sharing or enrollment-based payouts for multiple instructors.

3. **Lack of Unified System Architecture**
   - Inefficiencies from not having a shared API and system architecture across web and mobile, leading to increased development time and costs.
   - Complexity in ensuring feature consistency and role-based access across different platforms.

4. **Scalability and Flexibility Concerns**
   - Need for a scalable solution that allows future growth, including individual course purchases and additional content delivery modules.

### Solution

1. **Unified Platform Development**
   - Use React Native (Expo) for mobile app development to maintain feature parity and shared API across web and mobile.
   - Implement a custom API-first development strategy to streamline maintenance and updates.

2. **Robust Monetization and Payout System**
   - Implement a hybrid monetization model supporting monthly/annual subscriptions and individual course purchases.
   - Develop an instructor payout system based on enrollment counts, supporting either revenue share or per-enrollment models.

3. **Consistent User Experience**
   - Role-based access ensures tailored experiences for Admin, Student, and Instructor roles.
   - Shared TypeScript types/components for consistency in system behavior across platforms.

4. **Flexible and Scalable Tech Stack**
   - Stack includes Next.js for frontend, NestJS/AWS Lambda for backend, and PostgreSQL for database—chosen for scalability and flexibility.
   - Use Stripe for streamlined payment handling and S3 + CloudFront or Mux/Vimeo for efficient content storage/streaming.

### Business Value

- **Cost Efficiency**
  - $25k-$50k budget managed through shared development strategies and scalable tech stack.
  - Four-month timeline achieved with a streamlined development process.

- **Revenue Growth**
  - Potential for increased revenue through a hybrid monetization strategy, accommodating diverse payment preferences.
  - Instructor satisfaction and retention improved through transparent payout processes.

- **Enhanced User Engagement**
  - Consistent experience across devices improves user satisfaction and engagement.
  - Comprehensive feature set, including course catalog browsing, progress tracking, and certificate issuance, increases platform stickiness.

- **Scalability and Future-Proofing**
  - Architecture supports future enhancements and new monetization opportunities, ensuring long-term sustainability and growth.  

By addressing the outlined pain points with these solutions, the platform is well-positioned to deliver a seamless, scalable, and profitable experience for all users.


# Users, Roles, and High-level User Flows

## Roles

1. **Admin**
2. **Student**
3. **Instructor (Teacher)**

## User Flows

### Admin

#### Flow: Managing Users and Courses
1. **Log In**: Admin logs into the platform.
2. **Access Dashboard**: Admin sees options to manage users, courses, subscriptions, and payouts.
3. **Manage Users**: Admin can add, edit, or remove users and assign roles.
4. **Course Moderation**: Admin reviews and approves submitted courses or content updates.
5. **Subscription Management**: Admin sets and updates subscription plans and pricing.
6. **Payout Management**: Admin schedules and manages instructor payouts.
7. **Audit & Reports**: Admin accesses and reviews platform analytics and audit logs.

#### Edge Case: Unauthorized Access
- If an admin attempts to access unauthorized sections, they are redirected with an error message.

### Student

#### Flow: Course Enrollment and Learning
1. **Sign Up/Log In**: Student registers or logs into their account.
2. **Browse Courses**: Student navigates the course catalog to find courses of interest.
3. **Subscription/Purchase**: Student either subscribes to unlock all courses or purchases individual courses.
4. **Access Courses**: Student views and begins enrolled courses.
5. **Track Progress**: Student's course progress is tracked, and they can resume from where they left off.
6. **Certificates**: Upon completion, students receive digital certificates.
7. **Manage Account**: Students can update account details and view billing information.

#### Edge Case: Payment Failure
- If a payment fails, the student receives an immediate error notification and guidance to retry or contact support.

### Instructor

#### Flow: Course Creation and Payouts
1. **Log In**: Instructor logs into their dashboard.
2. **Create Courses**: Instructor uses the course builder to draft and submit courses.
3. **Publish Courses**: Courses are reviewed for approval before being published.
4. **Analytics**: Instructor accesses student engagement and performance analytics on their courses.
5. **Manage Payout**: Instructor views enrollment counts and payout history.
6. **Profile Management**: Instructor updates personal and profile settings.

#### Edge Case: Course Rejection
- If a course is rejected during moderation, the instructor receives feedback for revisions.

## Assumptions and Open Questions

- **Assumption**: Subscription initially provides access to all courses, pending clarification on constraints.
- **Open Question**: Are there specific 'native-only' features required beyond standard streaming, progress, and certificate functionalities?


### Feature Set (Detailed, Grouped)

#### Authentication
- **User Roles & Access Control**: 
  - Roles include Admin, Student, and Instructor.
  - Role-based access control managed via Supabase Auth or Auth0.
- **User Authentication Processes**: 
  - Sign-up/Login.
  - Email verification and password recovery.

#### Admin Module
- **User Management**: 
  - Admins can manage users and assign roles.
- **Content Management**:
  - Manage courses and moderate content.
- **Monetization & Entitlement Management**:
  - Oversee subscriptions, one-off purchases, and entitlements.
- **Payout Management**:
  - Calculate instructor payouts based on enrollments.
  - Administer payout cycles.
- **Reporting & Monitoring**:
  - Generate reports and monitor platform activities.

#### Student Module
- **Course Interaction**: 
  - Browse course catalog and access course content.
  - View course details and pricing.
- **Subscription & Purchase Management**:
  - Purchase subscriptions (monthly and annual options).
  - Option for a la carte course purchases.
- **Progress Tracking and Certification**:
  - Track learning progress and receive certificates.
- **Account Management**:
  - Manage billing and subscription details from the dashboard.

#### Instructor Module
- **Course Authoring & Management**: 
  - Create and publish courses.
- **Analytics & Payout Management**:
  - Access analytics dashboard for course performance.
  - Manage profile and view payout history.

#### Booking/Payments
- **Payment Integration**: 
  - Utilize Stripe for handling subscriptions, one-time payments, and payouts.
- **Hybrid Monetization Model**:
  - Supports both subscriptions and individual course purchases.
- **Subscription Management**:
  - Manage lifecycle and entitlement of all courses with active subscriptions.

#### Content Delivery
- **Video Streaming & Storage**:
  - Content delivered using S3 and CloudFront, with optional Mux/Vimeo for video streaming.
- **Consistent Cross-Platform Experience**:
  - Shared API enables consistency across web and mobile applications.
  - Standard streaming and progress tracking without native-only requirements.

#### Notifications
- **Email Notifications**:
  - Use Postmark or SendGrid for dispatching email alerts.

#### Technology Platform
- **Development Platforms**: 
  - Web: Next.js (React) and NestJS or AWS Lambda for API.
  - Mobile: React Native (Expo) to ensure consistency across platforms.
- **Data & Storage Solutions**:
  - PostgreSQL database via Supabase or AWS RDS for storing data.

### Assumptions
- **Access with Subscription**:
  - Assumption: Active subscribers have access to all courses unless otherwise stated.
- **Platform Development Approach**:
  - Custom API-first approach to aid both web and mobile experiences, avoiding separate builds.

### Open Questions
- **App Requirements**:
  - Need confirmation if the standard streaming + progress + certificates app suffices or requires further native-only features.
- **Build Preference**:
  - Clarification needed on preference for custom development versus platforms like WordPress.


## Scope Split: MVP vs V1 vs V2

### MVP (Minimum Viable Product)
- **Platforms and Development:**
  - React Native for mobile (iOS and Android) and web using a shared API.
  - Focus on key tech stack: Next.js, NestJS, PostgreSQL, Supabase Auth/Auth0, Stripe, S3 + CloudFront.
  - Budget: $25k–$50k; Timeline: 4 months.

- **Core Features:**
  - **User Roles:**
    - Admin, Student, Instructor.
  
  - **Student Functionality:**
    - Sign-up/login, browse course catalog, purchase subscriptions, access and track learning progress.

  - **Instructor Functionality:**
    - Create and manage courses, view basic analytics, manage payouts.

  - **Admin Functionality:**
    - Manage users, courses, subscriptions, entitlements, and basic reporting.

  - **Monetization:**
    - Implement subscription model unlocking all courses initially.

  - **Content and Certification:**
    - Standard streaming, progress tracking, and certificate issuance.

- **Assumptions:**
  - Utilizing a custom LMS/e-commerce backbone.
  - No hard 'native-only' requirements.

### V1
- **Expanded Features:**
  - **Monetization Options:**
    - Add individual course purchase capability to support flexible access models.
  
  - **Instructor Dashboard:**
    - Enhanced analytics for courses, student engagement, and earnings.

  - **Advanced Admin Tools:**
    - Detailed role-based access control, extended subscription plan management, and comprehensive reporting.

- **User Experience:**
  - Streamline onboarding and navigation for increased user engagement.
  - Optimize mobile and web fonts, layout, and animations for a seamless look and feel.
  
- **Payout Management:**
  - Develop a robust revenue share or per-enrollment payout model and cycle handling.

### V2
- **Advanced Functionality:**
  - **Personalization:**
    - Personalized course recommendations and user-driven content discovery.

  - **Community Features:**
    - Forums or discussion boards integrated into courses for enhanced peer interaction.
  
  - **Gamification:**
    - Leaderboards, badges, and achievements to boost motivation and engagement.

- **Integration and Scalability:**
  - Integrate additional third-party services (e.g., advanced video streaming with Mux/Vimeo).
  - Scale infrastructure to handle increased user load and data processing.

- **Internationalization:**
  - Implement multi-language support and localization to reach a global audience.

- **Open Questions:**
  - Determine whether gamification elements align with company goals.
  - Clarify expectations on personalized user experiences preferences.


### Budget, Timeline, and Tradeoffs

#### Timeline Estimate
- **Overall Project Timeline:** 4 months
- **Platforms Supported:** iOS and Android

#### Budget Bands

- **Low Budget ($25k–$35k):**
  - **Features Included:**
    - Core functionalities including subscriptions, a la carte payments, and basic instructor payout mechanisms.
    - Limited customization in user interface (UI) and user experience (UX).
  - **Tradeoffs:**
    - Minimal design iterations.
    - Reliance on out-of-the-box features from chosen stack components.
  - **Risks:**
    - Risk of minimal differentiation if UI/UX is too basic.

- **Medium Budget ($35k–$45k):**
  - **Features Included:**
    - Advanced customizations for role-based access control, analytics dashboards, and flexible monetization models.
    - Moderate UI/UX enhancements.
  - **Tradeoffs:**
    - Some complexity in managing additional customizations.
    - Potential need for scaling infrastructure beyond initial scope.
  - **Risks:**
    - Possible delays in timeline if additional features are added mid-project.

- **High Budget ($45k–$50k):**
  - **Features Included:**
    - Comprehensive UI/UX customizations and extensive features like detailed analytics, multitiered instructor payouts, and internationalization.
    - Thorough testing and scalability planning.
  - **Tradeoffs:**
    - Higher initial investment but potentially faster return due to better user engagement and retention.
  - **Risks:**
    - Increased complexity may lead to longer maintenance windows and ongoing costs.

#### Primary Tradeoffs

- **Time vs. Features:**
  - Adding features can extend the timeline. Prioritization of core features versus nice-to-haves is crucial.
  
- **Cost vs. Customization:**
  - Higher budgets enable more customization, impacting user engagement and retention positively.

- **Technical Stack Complexity:**
  - Opting for technology like Next.js, NestJS, PostgreSQL, etc., while powerful, can increase development time if the team is unfamiliar with them.

#### Risks and Assumptions

- **Risks:**
  - Potential requirement changes can lead to scope creep.
  - Integration challenges with third-party services (e.g., Stripe, Mux/Vimeo).

- **Open Questions:**
  - Confirmation on whether any "native-only" features are required.
  - Decision on custom development versus WordPress-like platforms.
  - Clarity on subscription access: full course access vs. subset.

This overview aims to guide you in matching your goals with budgetary and timeline constraints, helping ensure a successful project launch balanced between cost, time, and desired features.


## Risks, Assumptions, and Open Questions

### Risks

- **Budget Overruns**: The project is set within a $25k–$50k budget. Any unforeseen complexities could push costs beyond this range.
- **Timeline Constraints**: The goal is to complete development within a 4-month timeframe. Delays in any component, such as mobile or API development, could extend the timeline.
- **Technology Integration**: Using a combination of technologies (Next.js, NestJS, React Native, etc.) could pose challenges in ensuring seamless integration and consistent performance across platforms.
- **Instructor Payout Model**: The effectiveness of the revenue share or per-enrollment model is yet unproven and may not meet instructor expectations, affecting platform adoption.
- **Platform Stability**: Reliance on a shared API means dependencies across web and mobile versions may lead to instability if changes are not carefully managed.

### Assumptions

- **No Hard Native Requirements**: Assumption is that standard streaming, progress tracking, and certificates suffice and there are no additional 'native-only' requirements.
- **Shared Access**: Assumes that a subscription would ideally provide access to all courses, unless otherwise decided.
- **Custom Build Preference**: It is assumed that custom development, rather than using WordPress or similar platforms, aligns with the business goals.

### Open Questions

- **Native Requirements**: Are there definitive 'native-only' requirements that must be addressed beyond standard streaming, progress tracking, and certificates?
- **Platform Choice for Custom Development**: Is there a clear preference against using an existing platform like WordPress for development, despite the custom build recommendation?
- **Subscription Access Scope**: When users have an active subscription, should it provide access to all courses, or is there a plan to limit access to a subset of offerings?


### Next Steps

Here's a structured plan to guide us forward, ensuring we remain aligned and focused on delivering the project successfully:

#### Checklist for Confirmation and Preparation

1. **Platform Requirements:**
   - Confirm the absence of any hard 'native-only' requirements, ensuring the standard app will meet all needs.

2. **Development Approach:**
   - Decide between custom development or using platforms like WordPress for LMS/e-commerce backbone.

3. **Subscription Model:**
   - Clarify if an active subscription should grant access to all courses or only a specific subset.

4. **Tech Stack Confirmation:**
   - Finalize the preferred tech stack:
     - Frontend: Next.js
     - Backend/API: NestJS or AWS Lambda
     - Database: PostgreSQL (Supabase or AWS RDS option)
     - Auth/RBAC: Supabase Auth or Auth0
     - Payments: Stripe
     - Content Storage/Streaming: S3 + CloudFront or Mux/Vimeo
     - Emails/Notifications: Postmark/SendGrid
     - Admin Tools: Retool or lightweight internal admin in Next.js

5. **Role and Access Definition:**
   - Validate role-based access control for Admin, Students, and Instructors.

6. **Monetization Structure:**
   - Confirm the hybrid model of monthly/annual subscriptions plus a la carte purchases.

7. **Instructor Payouts:**
   - Decide on payout structures based on enrollments, including revenue share or per-enrollment models.

#### Suggested Workshop Agenda (60 Minutes)

1. **Introduction (5 minutes)**
   - Overview of project goals and objectives.

2. **Platform and Tech Stack Discussion (15 minutes)**
   - Review platform requirements and confirm tech stack choices.
   - Discuss any technical queries related to the API strategy and mobile app development.

3. **Monetization and Access Strategy (15 minutes)**
   - Explore subscription models and clarify course access entitlements.
   - Discuss the envisioned instructor payout structure.

4. **User Roles and Privacy (10 minutes)**
   - Validate role-based access control and privacy considerations for each user role.

5. **Q&A and Open Discussion (10 minutes)**
   - Address any remaining questions or concerns.
   - Allow for feedback and additional input from participants.

This plan ensures clarity and alignment across all stakeholders and supports our goals for a successful project execution.
