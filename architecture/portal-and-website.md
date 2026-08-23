# Portal and Corporate Website

## Portal

The ASP.NET Core MVC portal is a server-rendered client of the KiloDrive API. It
supports account operations and authorized administration without directly
owning domain databases. Role and permission checks are enforced by the API even
when a menu item is hidden in the portal.

Portal requests use correlation IDs, anti-forgery protection for mutations,
strict security headers, and a constrained Content Security Policy. API errors
are translated into user-facing views rather than exposing provider responses or
exception text.

System administration is organized around dashboard, users, drivers, riders,
vehicles, verification, finance, support, settings, reports, content, and audit
workflows. Multi-entity details use tabbed views and stable DTO contracts.

## Corporate website

The website is an ASP.NET Core Razor Pages application. Main content pages are
database-driven through published, tenant-scoped API content. Localized routes,
metadata, canonical links, and accessibility are rendered server-side.

Public calculators call approved API endpoints rather than embedding independent
business rules. Anonymous tenant routing is an explicit boundary and is protected
with rate limits and, where configured, challenge/attestation controls.

## Shared rules

- Neither browser application receives database credentials.
- Mutation remains in explicit POST/PUT/PATCH/DELETE actions with anti-forgery
  or bearer protection as appropriate.
- Security headers are applied on success, redirects, validation failures, and
  sanitized errors.
- User-visible text is localized through resource files rather than embedded
  controller/view literals.
- No portal or website log should include authentication tokens, request bodies,
  private document URLs, or provider secrets.
