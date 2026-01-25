- The feature set includes payouts via Stripe Connect, teacher verification, certificate issuance, and verification URLs.
- Admin-grade audit logs and exports are part of the system requirements.
- Custom build recommended for multi-role RBAC, payments, subscriptions, payouts, audit logs, certificate verification, and analytics.
- Primary approach involves Next.js for frontend, NestJS for backend, Postgres for database, Auth0 or Clerk for authentication, Stripe for payments, S3 for storage, SQS + workers for async jobs, Postmark/SendGrid for notifications, and AWS for hosting.
- Phase 1 - Core Platform (MVP): 14–16 weeks; includes roles, courses, subscriptions, payouts, certificates.
- Phase 2 - Enhancements & Optimization: 8–12 weeks; includes analytics, UX polish, performance tuning.
- Admin journey includes governance & RBAC, teacher verification, course moderation, monetization oversight, payout controls, certificate management, notifications, audit & compliance, and analytics.
- Teacher journey includes profile & verification, course creation, pricing & publishing, student engagement, earnings & payouts, and analytics.
- Student journey includes discovery, purchase/access, learning, progress tracking, completion & certificates, and account management.
- Core backend features: RBAC + org-wide permissions, payments (subscriptions and one-off purchases), payouts to teachers, course content/versioning + moderation workflow, progress/completion validation + certificate issuance, notifications, and audit logging.
- Admin Features:
- Platform-Wide Dashboard
- User & Role Management
- Teacher Verification & Approval
- Course Review & Moderation
- Subscription & Pricing Control
- Revenue & Payout Oversight
- Certificate Templates & Rules
- Reports & Analytics
- Content Policy Enforcement
- Security & Compliance Controls

Teacher Features:
- Teacher Profile & Verification
- Course Creation & Editing
- Content Upload (Video, Docs, Resources)
- Course Pricing Configuration
- Enrollment & Performance Insights
- Earnings Dashboard
- Payout Requests
- Course Update & Versioning

Student Features:
- Account Registration & Login
- Course Discovery & Search
- Subscription Management
- Course Purchase Flow
- Learning Dashboard
- Progress Tracking
- Completion Validation
- Certificate Download & Verification
- Payment History

Platform & System Features:
- Role-Based Access Control (RBAC)
- Secure Payment Processing
- Subscription Management
- Automated Payout System
- Notifications (Email / In-App)
- Audit Logs
- Certificate Verification URLs
- API-First Architecture
