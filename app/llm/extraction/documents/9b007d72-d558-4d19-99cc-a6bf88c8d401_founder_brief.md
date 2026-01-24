# Founder & Team Brief

**Job ID:** `9b007d72-d558-4d19-99cc-a6bf88c8d401`


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

Our project aims to develop a robust online learning platform that serves administrators, students, and instructors, enabling seamless course creation, management, and delivery. Built with a custom technology stack (Next.js, NestJS, Postgres), this platform will streamline educational interactions while ensuring secure and efficient operations. It's designed for anyone looking to offer, access, or manage educational content in a highly adaptable and scalable environment.

This platform is significant because it addresses key challenges in today’s digital learning landscape by combining content subscription models with individual course purchases. It ensures that instructors are fairly compensated based on enrollments and provides students with accessible learning paths. By leveraging cutting-edge technology and a focus on user-friendly design, we aim to improve engagement, flexibility, and overall satisfaction for all users.

**Top Capabilities:**

- **Subscription Management:** Offers monthly and annual subscription plans for platform access, with future capabilities for individual course purchases.
- **Role-Based Access Control (RBAC):** Secure access tailored for different roles—Admin, Student, Instructor—to ensure customized user experiences.
- **Instructor Payouts:** Automatic calculations of instructor earnings based on enrollments, managed by a secure payout process every month.
- **Comprehensive Course Interaction:** Includes course authoring, student progress tracking, and certificate awarding, enhancing the learning journey.
- **Robust Tech Stack:** Utilizes a primary stack that includes Next.js and NestJS, providing a reliable and scalable platform infrastructure.

Success looks like a seamlessly functioning platform delivering educational value, fostering a thriving community of educators and learners, all within a 4-month development cycle.


## Problem, Solution, and Business Value

### Problem
The current online learning platforms face several challenges that impact students, instructors, and platform administrators:

- **Limited Access**: Existing systems often restrict learners to specific courses unless they subscribe to higher-tier plans, which can limit learning opportunities.
- **Inefficient Payout Systems**: Instructors struggle with complex and delayed payout processes based on course enrollments and revenue sharing.
- **Lack of Integrated Features**: Many platforms lack cohesive features like comprehensive role-based access, robust subscription management, and detailed progress tracking for learners.

### Solution
Our platform addresses these challenges by offering a tailor-made, scalable solution built on a modern tech stack, ensuring flexibility and efficiency:

- **Comprehensive Access via Subscriptions**:
  - Monthly and Annual hybrid subscription plans that initially unlock all courses.
  - Support for individual course purchases as a future enhancement.

- **Simplified Payout System**:
  - Instructor payouts based on enrollments, calculated monthly with options for fixed or revenue-sharing models.
  - An admin-approved payout run enhances accuracy and transparency.

- **Integrated Platform Features**:
  - Primary stack includes Next.js, NestJS, Postgres, Prisma, and managed auth via Clerk/Auth0.
  - Key MVP features: role-based access control (RBAC), course authoring, student progress tracking, certificate awarding, and enrollment-based instructor payouts.
  - Managed infrastructure to support seamless subscriptions, billing (via Stripe), video streaming (via Mux/Cloudflare), and storage (S3).

### Business Value
The proposed solution delivers quantifiable business benefits for each stakeholder:

- **For Students**:
  - Increased learning opportunities due to broader access at competitive pricing.
  - Enhanced user experience with a streamlined subscription lifecycle and intuitive dashboards for course discovery, progress tracking, and certificate management.

- **For Instructors**:
  - Increased revenue potential with clear, reliable monthly payouts based on actual enrollments.
  - Easy-to-use tools for course creation, publishing, and performance monitoring.

- **For Platform Administrators**:
  - Efficient platform management with centralized, role-based oversight capabilities.
  - Robust analytics and reporting to inform strategic decisions and improve platform performance.

**Metrics to Measure Success**:
- **Subscription Growth**: Number of active and new subscriptions.
- **Instructor Satisfaction**: Payout timeliness and enrollment growth.
- **Student Engagement**: Course completion rates and certificate awards.

**Assumptions**:
- Default assumption that all courses will initially be accessible through subscriptions, pending a final decision on the subscription catalog strategy.
- The instructor payout models (fixed/revenue-share) are flexible and designed to adapt based on platform needs and feedback.

**Open Question**:
- Should subscriptions unlock all courses on the platform, or offer access to a curated catalog? Further input from stakeholders is required to finalize this aspect.


## Users, Roles, and High-level User Flows

### Roles

1. **Admin**
2. **Student**
3. **Instructor**

### Admin User Flow

1. **User Management:**
   - Access the admin dashboard.
   - Create, edit, or remove user accounts.
   - Assign roles and manage permissions.

2. **Course Oversight:**
   - Review and approve course content.
   - Monitor course performance across the platform.

3. **Monetization and Enrollment:**
   - Manage subscription plans and pricing.
   - Review enrollment data and trends.

4. **Payout Operations:**
   - Calculate monthly payouts for instructors.
   - Approve payout runs based on enrollment data.

5. **Platform Monitoring:**
   - Monitor analytics and platform health.
   - Ensure compliance and security measures are in place.

**Edge Cases:**
   - Handle refund requests and access overrides.
   - Address technical issues or user complaints.

### Student User Flow

1. **Discover Courses:**
   - Browse and search for available courses.
   - Use filters to find courses by interest or skill level.

2. **Manage Subscription:**
   - Choose between Monthly and Annual plans.
   - Access all courses via subscription or purchase individual courses (future phase).

3. **Access Course Player:**
   - Engage with course materials and complete assessments.
   - Track progress through the student dashboard.

4. **Certificate Awarding:**
   - Complete course requirements.
   - Receive digital certificates upon course completion.

5. **Account Management:**
   - Update personal information and payment methods.
   - Manage email notification preferences.

**Edge Cases:**
   - Address failed payment transactions.
   - Requests for course-specific refunds.

### Instructor User Flow

1. **Course Creation and Publishing:**
   - Access course authoring tools.
   - Develop course content and submit for admin approval.

2. **View Course Performance:**
   - Track enrollment statistics and student engagement.
   - Access feedback to make course improvements.

3. **Earnings Tracking:**
   - Review earnings based on enrollments.
   - Understand payout calculations and history.

4. **Profile and Payout Management:**
   - Update personal and banking information for payouts.
   - Choose payout preferences (fixed amount or revenue-share).

**Edge Cases:**
   - Manage disputes related to earnings or unauthorized content use.
   - Update content based on student feedback or admin requests.

### Assumptions and Open Questions

- **Assumption:** Subscriptions initially unlock all courses unless decided otherwise.
- **Open Question:** Should subscriptions unlock all courses on the platform, or only a subscription catalog?


## Feature Set (Detailed, Grouped)

SECTION TITLE:
Feature Set (Detailed, Grouped)

---

## Authentication (Auth)
- **Managed Authentication Services**: Utilize Clerk or Auth0 for authentication.
- **Role-Based Access Control (RBAC)**: Implement RBAC for Admin, Student, and Instructor roles.
- **Server-Side RBAC**: Securely manage access and permissions on the server side.

## Administration (Admin)
- **User Management**: Capabilities to add, remove, and manage user roles and access.
- **Course Oversight**: Monitor course content and performance.
- **Monetization Controls**: Manage subscription plans and pricing.
- **Enrollment and Access Management**: Oversee student enrollments and access permissions.
- **Payout Operations**: Approve and manage instructor payout runs.
- **Platform Monitoring and Analytics**: Track usage statistics and platform performance.

## Booking/Payments
- **Subscription Plans**: Support for Monthly and Annual subscription models.
- **Payments and Webhooks**: Integration with Stripe Billing for processing payments and handling webhooks.
- **Subscription Lifecycle Management**: Trial, upgrade, cancel, and renew subscriptions.
- **Individual Course Purchases**: Allow users to buy courses separately in a later phase (assumption).
- **Payout Calculations**: Equal or revenue-share based payouts to instructors.

## Content Management
- **Course Creation and Publishing**: Tools for instructors to author and publish courses.
- **Catalog and Search/Filter**: Provide a searchable catalog of courses.
- **Course Model Development**: Establish foundational structures for course delivery.

## Learning Experience
- **Student Dashboard**: A personalized dashboard for students to manage courses and progress.
- **Course Player**: An interface for consuming course content.
- **Progress Tracking**: Track student progress through courses.
- **Assessments and Certificates**: Completion of assessments and awarding of certificates.

## Notifications
- **Email Notifications**: Use Postmark or SendGrid for sending critical emails.
  - Receipt confirmations, renewal reminders, cancellations.
  - Instructor payout notifications.

## Reporting and Analytics
- **Basic Reporting**: Generate reports for enrollment, earnings, and user activity.
- **Audit Logs**: Maintain logs for security and compliance purposes.

## Performance and Compliance
- **Performance Optimization**: Ensure system scalability and responsiveness.
- **Legal Compliance**: Implement necessary legal and compliance measures.
- **Quality Assurance (QA)**: Conduct rigorous testing to ensure system readiness for launch.

## Support and Operations
- **Support Flows**: Develop processes for refunds and access overrides.
- **Payout History**: Enable instructors to view and track their payout history.

---

Open Question:
- Should subscriptions unlock all courses on the platform, or only a specific subscription catalog? 

Assumption:
- Individual course purchases will be a later-added feature based on user demand.


### Scope Split: MVP vs V1 vs V2

#### MVP (Minimum Viable Product)
- **Roles & Access**
  - Implement role-based access control (RBAC) for Admin, Student, Instructor.
- **Course Management**
  - Develop course model, authoring, and publishing workflow.
- **Subscriptions & Payments**
  - Enable monthly and annual subscription plans using Stripe Billing.
  - Implement payment processing, webhooks, and core admin management for subscriptions.
- **Learning Experience**
  - Basic catalog, course player, and student dashboard to track progress.
- **Instructor Payouts**
  - Calculate payouts based on enrollments, with a fixed or revenue-share per enrollment.
  - Run monthly admin-approved payout cycles.
- **Notifications**
  - Basic email notifications for receipts, renewals, cancellations, and payout statuses.

**Rationale:**
- Allocated 4-month timeline demands focus on core functionalities.
- Budget ($25–50k) constraints necessitate prioritizing essential features.
- Target early market entry to validate product-market fit and gather user feedback.
  
#### V1
- **Enhanced Learning Features**
  - Advanced catalog search and filter capabilities.
  - Expanded student dashboard functionalities to include assessments and certificates.
- **Monetization Options**
  - Implementation of individual course purchases in addition to subscription access.
- **Instructor Dashboard**
  - Detailed earnings tracking and reporting for instructors.
- **Basic Analytics & Reporting**
  - Incorporate basic reporting tools for admin and instructor insights.
  
**Rationale:**
- Build on MVP feedback to enhance user experience and functionality.
- Prepare platform for scalability with individual course sales and better analytics.
- Maintain alignment with budget through incremental feature delivery.

#### V2
- **Subscription Flexibility**
  - Introduce subscription tiers and possibly a subscription catalog model.
- **Comprehensive Analytics**
  - Advanced analytics for user engagement, course performance, and sales trends.
- **Instructor Tools Expansion**
  - Additional tools for instructor communication and course management.
- **Platform Optimization**
  - Performance enhancements, security hardening, and support flows (e.g., refunds).
  
**Rationale:**
- Enable further customization and personalization based on user needs.
- Competitive differentiation through advanced analytics and instructor tools.
- Continuous improvement and optimization to sustain business growth.

#### Open Questions
- Should subscriptions unlock all courses on the platform, or only a specific catalog? Addressing this will clarify the monetization strategy and guide future development stages.


### Budget, Timeline, and Tradeoffs

#### Timeline Estimate
- **MVP Target Timeline:** 4 months
  - **Month 1:** Foundation setup, including Role-Based Access Control (RBAC), course model, publishing workflow, subscription plans, payments integration.
  - **Month 2:** Learning experience enhancements like catalog search, user dashboards, and notifications.
  - **Month 3:** Monetization and payouts implementation, including subscription lifecycle, earnings calculations.
  - **Month 4:** Final hardening and launch preparations, including QA, security, and compliance.

#### Budget Bands
- **Low Band:** $25k
  - Focus on core MVP features: subscriptions, RBAC, core admin management.
  - Limited customizations and optimizations; basic UI/UX.
  - Potential risks in scalability and user experience.

- **Medium Band:** $35k
  - Incorporates more advanced features such as student dashboards and detailed reporting.
  - Enhanced user experience and design elements.
  - Better performance optimizations and initial marketing integration.

- **High Band:** $50k
  - Comprehensive build with all planned features and advanced customization.
  - Includes extensive QA, security measures, and legal compliance.
  - Fully optimized performance, robust analytics, and complete support flow setup.

#### Tradeoffs
- **Feature Breadth vs. Depth:**
  - **Low:** May have to limit some features; focus on essential functions.
  - **Medium/High:** Allows for more comprehensive and detailed functionality.

- **Customization vs. Cost:**
  - **Low:** Focus on standardized solutions to cut costs.
  - **High:** Custom solutions and unique branding possibilities.

- **Timeline Flexibility:**
  - Budget constraints could extend timelines for smaller teams or when more iterations are needed.

#### Risks
- **Budget Overruns:** Potential for exceeding the maximum budget if scope expands or unforeseen complexities arise.
- **Timeline Slippage:** Delays in feature implementation can affect the entire launch schedule.
- **Feature Creep:** Risk of adding more features beyond the essential MVP scope without adjusting time/resources.
- **User Experience:** Limited budgets may impact the smoothness and intuitiveness of user interfaces and journeys.

#### Open Questions
- **Subscription Access:** Should subscriptions unlock all courses or only a specific catalog subset?

These structured elements outline the important considerations for budget, timeline, and tradeoffs ensuring clarity in decision-making processes. Adjustments to budget bands impact features, customization, and potential risks, requiring careful evaluation by the business owner or founder.


# Risks, Assumptions, and Open Questions

## Risks

- **Tech Stack Complexity**: The primary tech stack involves multiple technologies (Next.js, NestJS, Postgres, Prisma, etc.), which may create integration challenges, particularly for authentication and billing.

- **Budget Constraints**: With a budget of $25–50k, there is a risk of overspending if any unforeseen complexities arise during development or if additional features are requested.

- **Timeline Pressure**: The 4-month MVP timeline is tight, especially considering the breadth of different features planned. Delays in any phase could impact the launch schedule.

- **Instructor Payouts**: The complexity of handling multiple payout models (fixed per enrollment vs. revenue sharing) could create accounting and administrative overhead.

- **Fallback Options**: Relying on fallback options such as WordPress could lead to limitations in functionality and scalability if the custom stack is not viable.

- **Security and Compliance**: Ensuring compliance with legal and security standards is critical, especially with user data and financial transactions involved.

## Assumptions

- **Subscription Model**: It is assumed that subscriptions will initially unlock all courses. Any change to unlock only a subscription catalog will be considered later.

- **Instructor Payouts**: Assumed that payouts will be handled monthly with an admin-approved run, aligning with available resources and existing internal processes.

- **User Roles**: The initial launch will include Admin, Student, and Instructor roles, which will cover the basic platform requirements.

- **Fallback Strategy**: In case of any critical issues with the primary stack, WordPress with add-ons is assumed to be a viable alternative.

- **Managed Services**: Authentication and billing are assumed to be managed via third-party services (Clerk/Auth0 and Stripe), expecting these to simplify development efforts.

- **Infrastructure Support**: Hosting and infrastructure requirements (Vercel, Render/Fly.io) are assumed to support the planned scale and performance needs.

## Open Questions

- **Subscription Access**: Should subscriptions unlock all courses on the platform, or should access be limited to a specific subscription catalog?

- **Revenue Model**: What will be the criteria for deciding between fixed payout per enrollment and revenue sharing for instructors? How will these models affect pricing?

- **UI/UX Details**: Are there specific user interface requirements or preferences for the purchase flows and earnings dashboards that need further exploration?

- **Legal Compliance**: Are there any specific legal compliance requirements that need to be addressed beyond standard data protection and privacy regulations?

- **Fallback Viability**: How viable is the WordPress fallback in terms of feature parity and user experience compared to the custom stack?

- **Email and Notifications**: Clarification needed on whether Postmark or SendGrid will be used for email services. What are the deciding factors?


## Next Steps

To ensure the successful launch of the platform, the following actions need to be confirmed and prepared:

### Checklist

1. **Confirm Subscription Access Model:**
   - Decide whether subscriptions should unlock all courses or only a specific subscription catalog.

2. **Finalize Monthly Goals:**
   - Ensure alignment on the monthly objectives for each stage of development, as outlined in the 4-month timeline.

3. **Authentication Provider Selection:**
   - Choose between Clerk and Auth0 for managed authentication services.

4. **Video Streaming Service Decision:**
   - Confirm whether to use Mux or Cloudflare Stream for video streaming.

5. **Finalize UI/UX Design Scope:**
   - Validate the design elements such as purchase flows and teacher earnings dashboards.

6. **Platform Roles Verification:**
   - Confirm the functionalities and access levels for Admin, Student, and Instructor roles.

7. **Subscription Plan Details:**
   - Outline specific features for Monthly and Annual subscription plans.

8. **Instructor Payout Details:**
   - Confirm payout calculations based on fixed amounts or revenue-share per enrollment.

9. **Compliance and Legal Preparations:**
   - Ensure all legal and compliance measures are integrated into the platform's development phase.

### Suggested Workshop Agenda (30–60 minutes)

1. **Introduction (5 minutes):**
   - Brief review of the project goals and timeline.

2. **Subscription Model Discussion (10 minutes):**
   - Decide on the access model for subscriptions.

3. **Authentication and Video Streaming Decisions (10 minutes):**
   - Select between Clerk/Auth0 for authentication and Mux/Cloudflare for streaming services.

4. **UI/UX Review (10 minutes):**
   - Review proposed designs and confirm elements for user journeys.

5. **Roles and Access Control (5 minutes):**
   - Verify role definitions and associated permissions.

6. **Budget Review (5 minutes):**
   - Reassess budget allocation to ensure alignment with the outlined timeline and features.

7. **Open Questions and Clarifications (5 minutes):**
   - Address and resolve any remaining uncertainties or questions.

8. **Next Steps and Assignments (5 minutes):**
   - Summarize decisions made and delegate action items to relevant stakeholders.

This structure ensures that all critical aspects of the project are considered and aligns the team on the immediate priorities for development and launch.
