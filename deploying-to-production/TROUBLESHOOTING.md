# Deployment Troubleshooting

Common issues and solutions for GitHub and Vercel deployment.

## GitHub Repository Creation Issues

### Error: "GitHub CLI (gh) not installed"

**Cause**: GitHub CLI is not installed on the system.

**Solution**:
```bash
# Install GitHub CLI
brew install gh

# Authenticate
gh auth login
```

Follow the prompts to authenticate with your GitHub account.

### Error: "GitHub CLI not logged in"

**Cause**: GitHub CLI is installed but not authenticated.

**Solution**:
```bash
gh auth login
```

Select "GitHub.com", choose authentication method (browser or token), and complete the login flow.

### Error: "Repository already exists"

**Cause**: A repository with the same name already exists in your GitHub account.

**Solution**:

Option 1 - Use existing repository:
```bash
# Add remote manually
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git push -u origin main
```

Option 2 - Rename the project:
```bash
# Rename project directory
mv old-name new-name

# Run script with new name
bash scripts/create-github-repo.sh new-name
```

Option 3 - Delete existing repository:
```bash
# Delete via CLI (careful!)
gh repo delete REPO_NAME --yes

# Then run script again
bash scripts/create-github-repo.sh REPO_NAME
```

### Error: "Project directory does not exist"

**Cause**: The project is not in the expected location.

**Expected location**: `/Volumes/Time/go to wild/websites/<project-name>`

**Solution**:
```bash
# Check current location
pwd

# Move project to correct location
mv /path/to/project "/Volumes/Time/go to wild/websites/project-name"

# Run script
bash scripts/create-github-repo.sh project-name
```

### Error: "failed to push some refs"

**Cause**: Local branch is behind remote, or push was rejected.

**Solution**:
```bash
# Pull changes first
git pull origin main --rebase

# Then push
git push -u origin main
```

## Vercel Deployment Issues

### Error: "Vercel CLI not installed"

**Cause**: Vercel CLI is not installed.

**Solution**:
```bash
# Install Vercel CLI globally
npm install -g vercel

# Verify installation
vercel --version
```

### Error: "Not authenticated with Vercel"

**Cause**: Vercel CLI is not logged in.

**Solution**:
```bash
# Login to Vercel
vercel login
```

Enter your email address and click the verification link sent to your email.

### Error: "Build failed" during deployment

**Cause**: Code doesn't compile or build script failed.

**Solution**:

1. **Check build logs**:
```bash
vercel logs
```

2. **Common build errors**:

**TypeScript errors**:
```bash
# Fix TypeScript errors locally
npm run build

# Check specific errors
npx tsc --noEmit
```

**Missing dependencies**:
```bash
# Install all dependencies
npm install

# Commit package-lock.json
git add package-lock.json
git commit -m "Update dependencies"
git push
```

**Environment variables missing**:
- Add required variables in Vercel dashboard
- Go to Project Settings > Environment Variables
- Add variables for Production environment

3. **Redeploy after fixes**:
```bash
vercel --prod
```

### Error: "No framework detected"

**Cause**: Vercel cannot detect the framework (Next.js).

**Solution**:

Check `package.json` has correct scripts:
```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

If using Next.js 15, verify `next` is in dependencies:
```bash
npm list next
```

### Error: "Deployment timeout"

**Cause**: Build process takes too long (> 10 minutes on free tier).

**Solution**:

1. **Optimize build**:
   - Remove unused dependencies
   - Reduce bundle size
   - Check for infinite loops in build scripts

2. **Upgrade Vercel plan** (if needed for longer builds)

### Error: "Module not found" in production

**Cause**: Dependency is in `devDependencies` but needed in production.

**Solution**:

Move dependency to `dependencies`:
```bash
npm install <package-name> --save

# Remove from devDependencies
npm uninstall <package-name> --save-dev

# Commit changes
git add package.json package-lock.json
git commit -m "Fix dependency location"
git push
```

### Error: "CORS errors" in production

**Cause**: API requests blocked by CORS policy.

**Solution**:

Add CORS headers in `next.config.mjs`:
```javascript
const nextConfig = {
  async headers() {
    return [
      {
        source: '/api/:path*',
        headers: [
          { key: 'Access-Control-Allow-Origin', value: '*' },
          { key: 'Access-Control-Allow-Methods', value: 'GET,POST,PUT,DELETE,OPTIONS' },
          { key: 'Access-Control-Allow-Headers', value: 'Content-Type, Authorization' },
        ],
      },
    ];
  },
};
```

## Environment Variables Issues

### Error: "Environment variable undefined"

**Cause**: Variable not configured in Vercel.

**Solution**:

1. Go to Vercel dashboard
2. Select your project
3. Settings > Environment Variables
4. Add the missing variable
5. **Important**: Redeploy after adding variables

```bash
vercel --prod --force
```

### Database connection fails in production

**Cause**: Database URL not configured or incorrect.

**Solution**:

1. **Check connection string format**:
```
postgres://user:password@host:port/database?sslmode=require
```

2. **Verify in Vercel**:
   - Environment Variables section
   - Variable name matches code (e.g., `DATABASE_URL`)
   - Variable set for "Production" environment

3. **Test connection**:
```bash
# Use Vercel CLI to check
vercel env ls
```

## Performance Issues

### Site loads slowly after deployment

**Cause**: Images not optimized, JavaScript bundles too large.

**Solution**:

1. **Optimize images**:
```bash
node scripts/optimize-images.js
```

2. **Analyze bundle size**:
```bash
npm run build

# Check .next/analyze (if configured)
```

3. **Enable Vercel Analytics**:
   - Free tier includes basic analytics
   - Enable in Project Settings

### High function execution time

**Cause**: Server-side functions take too long.

**Solution**:

1. **Use static generation** where possible (ISR, SSG)
2. **Implement caching** for API responses
3. **Optimize database queries**
4. **Consider edge functions** for faster response

## General Debugging

### Check deployment status

```bash
# List recent deployments
vercel ls

# View specific deployment logs
vercel logs [deployment-url]
```

### Access production environment

```bash
# View environment variables
vercel env ls

# Pull environment variables locally
vercel env pull
```

### Force redeploy

Sometimes a fresh deployment fixes issues:
```bash
vercel --prod --force
```

## Getting Help

If the issue persists:

1. **Check Vercel status**: https://www.vercel-status.com/
2. **Review build logs** carefully for specific errors
3. **Search Vercel documentation**: https://vercel.com/docs
4. **GitHub issues**: Check if others have similar problems
5. **Vercel community**: https://github.com/vercel/vercel/discussions

## Prevention Tips

**Before every deployment**:
- [ ] Test build locally: `npm run build`
- [ ] Check environment variables are documented
- [ ] Review recent code changes
- [ ] Test in development mode first
- [ ] Use preview deployments for testing (push to non-main branch)

**Best practices**:
- Keep dependencies up to date
- Use TypeScript for type safety
- Write tests for critical paths
- Monitor deployment notifications
- Set up Slack/Discord webhooks for deployment alerts
