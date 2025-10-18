# Pre-Deployment Checklist

Comprehensive checklist for deploying websites to production. This ensures code quality, SEO compliance, and E-E-A-T standards.

## Code Quality

### Build and Compilation
- [ ] `npm run build` completes successfully with no errors
- [ ] No TypeScript errors
- [ ] No ESLint warnings (or only acceptable warnings)
- [ ] All imports resolve correctly

### Functionality
- [ ] All core features tested and working
- [ ] Forms submit correctly
- [ ] Navigation works on all pages
- [ ] Links are not broken
- [ ] Images load properly

### Responsive Design
- [ ] Tested on mobile devices (or responsive mode)
- [ ] Tested on tablet devices
- [ ] Tested on desktop
- [ ] All breakpoints work correctly

## SEO Elements

### Meta Tags
- [ ] All pages have unique `<title>` tags (50-60 characters)
- [ ] All pages have unique `<meta description>` (150-160 characters)
- [ ] Open Graph tags configured (`og:title`, `og:description`, `og:image`)
- [ ] Twitter Card tags configured
- [ ] Canonical URLs set correctly

### Structured Data
- [ ] JSON-LD structured data added (WebSite, Organization, etc.)
- [ ] Schema.org markup valid (test with Google Rich Results Test)

### Sitemap and Robots
- [ ] `sitemap.xml` exists and includes all pages
- [ ] `robots.txt` configured correctly
- [ ] All language versions included in sitemap (for i18n sites)

### Internationalization (if applicable)
- [ ] `hreflang` tags configured for all language versions
- [ ] Language switcher works correctly
- [ ] URLs follow correct structure (`/en/`, `/ja/`, etc.)

## E-E-A-T Standards

### Experience & Expertise
- [ ] Content based on real experience (not AI-generated without review)
- [ ] First-hand usage examples included
- [ ] Real data and screenshots (not fabricated)

### Authoritativeness
- [ ] About page exists and shows professional background
- [ ] Author bio links to personal website or portfolio
- [ ] Content aligns with author's professional expertise

### Trustworthiness
- [ ] Contact information provided
- [ ] Privacy policy page exists (if collecting data)
- [ ] Terms of service page exists (if needed)
- [ ] AI usage disclosed transparently
- [ ] All claims are verifiable

## Performance

### Core Web Vitals
- [ ] LCP (Largest Contentful Paint) < 2.5s
- [ ] FCP (First Contentful Paint) < 1.8s
- [ ] TBT (Total Blocking Time) < 200ms
- [ ] CLS (Cumulative Layout Shift) < 0.1

### Optimization
- [ ] Images optimized (WebP format, proper sizing)
- [ ] JavaScript bundles minimized
- [ ] CSS optimized (unused styles removed)
- [ ] Fonts optimized (subset, preload)

### Caching
- [ ] Static assets have cache headers
- [ ] API responses cached appropriately

## Security

### HTTPS
- [ ] SSL certificate configured (Vercel provides automatically)
- [ ] All resources loaded over HTTPS

### Headers
- [ ] Security headers configured (CSP, X-Frame-Options, etc.)
- [ ] CORS configured correctly (if needed)

## Configuration

### Environment Variables
- [ ] All required environment variables documented
- [ ] Production environment variables configured in Vercel
- [ ] No secrets committed to repository

### Dependencies
- [ ] All dependencies up to date (or intentionally pinned)
- [ ] No known security vulnerabilities (`npm audit`)

## Analytics and Monitoring

### Analytics Setup
- [ ] Google Analytics or Plausible configured
- [ ] Analytics tracking code added to all pages
- [ ] Consent banner implemented (if needed for GDPR)

### Search Console
- [ ] Google Search Console property created (can be done after deployment)
- [ ] Sitemap submitted to Search Console (post-deployment)

## Project-Specific Checks

### Database (if applicable)
- [ ] Database migrations run successfully
- [ ] Connection strings configured in Vercel
- [ ] Database backups configured

### Authentication (if applicable)
- [ ] Auth providers configured (Google, GitHub, etc.)
- [ ] Callback URLs set correctly
- [ ] Session management working

### Payment (if applicable)
- [ ] Payment gateway configured (Stripe, etc.)
- [ ] Webhook endpoints configured
- [ ] Test mode disabled, production keys active

## Final Verification

### Manual Testing
- [ ] Homepage loads in under 3 seconds
- [ ] All CTAs (Call to Actions) work correctly
- [ ] Error pages (404, 500) render correctly
- [ ] Favicon displays correctly

### Pre-Launch Review
- [ ] All TODO comments removed or documented
- [ ] Console logs removed (or debug mode off)
- [ ] No placeholder content ("Lorem ipsum", etc.)
- [ ] Version number updated (if versioning)

## Post-Deployment Tasks

These can be done after deployment:
- [ ] Submit sitemap to Google Search Console
- [ ] Submit to Bing Webmaster Tools
- [ ] Monitor initial crawl activity
- [ ] Check indexing status after 24-48 hours
- [ ] Set up uptime monitoring (UptimeRobot, etc.)

---

**Remember**: If any critical item fails, fix it before deploying. It's easier to fix issues before launch than after.

Use this checklist as a guide, but always apply judgment based on the specific project needs.
