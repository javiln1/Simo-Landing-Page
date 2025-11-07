# Funnel Template System

A comprehensive, customizable HTML funnel template system that allows you to quickly create client-specific landing pages, education pages, and confirmation pages by simply updating a JSON configuration file.

## 🚀 Features

- **Easy Customization**: Change colors, content, videos, and forms through a simple JSON config
- **Responsive Design**: Mobile-first design that works on all devices
- **Video Integration**: Support for Vidalytics video embeds
- **Form Handling**: Built-in form generation with validation
- **SEO Optimized**: Meta tags, Open Graph, and structured data
- **Fast Build Process**: Generate client sites in seconds
- **Template Variables**: Use `{{variable}}` syntax throughout HTML templates

## 📁 Project Structure

```
funnel-template/
├── config/
│   └── client-config.json      # Main configuration file
├── templates/
│   ├── index.html              # Main funnel page template
│   ├── education-page.html     # Education page template
│   └── confirmation-page.html  # Confirmation page template
├── assets/                     # Client assets (images, videos, etc.)
├── output/                     # Generated client site (created on build)
├── build-template.js           # Template engine
├── package.json
└── README.md
```

## 🛠️ Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Configure Your Client
Edit `config/client-config.json` with your client's information:

```json
{
  "client": {
    "name": "Your Client Name",
    "businessName": "Your Business Name",
    "website": "https://yourwebsite.com",
    "email": "contact@yourwebsite.com",
    "phone": "(555) 123-4567"
  },
  "branding": {
    "primaryColor": "#07204A",
    "secondaryColor": "#F5F5DC",
    "accentColor": "#CFAF6E"
  }
}
```

### 3. Add Client Assets
Place your client's assets in the `assets/` folder:
- Logo images
- Testimonial photos
- Hero video fallback image
- Favicon

### 4. Build the Site
```bash
npm run build
```

### 5. Preview the Site
```bash
npm run serve
```
Then open http://localhost:8000 in your browser.

## 🎨 Customization Guide

### Branding
Update the `branding` section in your config:

```json
"branding": {
  "primaryColor": "#07204A",      // Main background color
  "secondaryColor": "#F5F5DC",    // Card/panel background
  "accentColor": "#CFAF6E",       // Accent/highlight color
  "textColor": "#F5F5DC",         // Main text color
  "buttonColor": "#CFAF6E",       // Button background
  "buttonTextColor": "#07204A"    // Button text color
}
```

### Content
Customize all text content in the `content` section:

```json
"content": {
  "heroTitle": "Your Main Headline",
  "heroSubtitle": "Your Subheadline",
  "heroDescription": "Your description text",
  "missionTitle": "Our Mission",
  "missionText": "Mission statement...",
  "ctaButtonText": "Get Started Now",
  "ctaButtonUrl": "#application-form"
}
```

### Media
Configure videos, images, and testimonials:

```json
"media": {
  "heroVideo": {
    "type": "vidalytics",
    "embedId": "your-video-id",
    "fallbackImage": "assets/hero-video-fallback.jpg"
  },
  "testimonials": [
    {
      "image": "assets/testimonial-1.jpg",
      "name": "John Doe",
      "result": "Increased sales by 300%",
      "description": "This program changed my business"
    }
  ]
}
```

### Forms
Configure application forms:

```json
"forms": {
  "applicationForm": {
    "action": "https://formspree.io/f/your-form-id",
    "method": "POST",
    "fields": [
      {
        "name": "name",
        "type": "text",
        "label": "Full Name",
        "required": true,
        "placeholder": "Enter your full name"
      }
    ]
  }
}
```

## 📝 Template Variables

Use these variables in your HTML templates:

### Client Information
- `{{client.name}}` - Client name
- `{{client.businessName}}` - Business name
- `{{client.email}}` - Contact email
- `{{client.phone}}` - Phone number
- `{{client.website}}` - Website URL

### Branding
- `{{branding.primaryColor}}` - Primary color
- `{{branding.secondaryColor}}` - Secondary color
- `{{branding.accentColor}}` - Accent color
- `{{branding.textColor}}` - Text color
- `{{branding.buttonColor}}` - Button color

### Content
- `{{content.heroTitle}}` - Hero section title
- `{{content.heroSubtitle}}` - Hero subtitle
- `{{content.ctaButtonText}}` - CTA button text
- `{{content.pillars}}` - Pillars section (auto-generated)
- `{{media.testimonials}}` - Testimonials (auto-generated)

### Forms
- `{{forms.applicationForm}}` - Complete form HTML

## 🚀 Deployment

### Vercel (Recommended)
1. Connect your GitHub repository to Vercel
2. Set build command: `npm run build`
3. Set output directory: `output`
4. Deploy!

### Netlify
1. Connect your repository to Netlify
2. Set build command: `npm run build`
3. Set publish directory: `output`
4. Deploy!

### Manual Upload
1. Run `npm run build`
2. Upload the contents of the `output` folder to your web server
3. Ensure your form action URLs are correct

## 🔧 Advanced Usage

### Custom Config Files
Create multiple config files for different clients:

```bash
# Build with custom config
npm run build:custom config/client-2-config.json
```

### Adding New Template Variables
1. Add the variable to your config JSON
2. Update `build-template.js` to replace the variable
3. Use `{{your.variable}}` in your HTML templates

### Custom CSS
Add custom CSS by modifying the `<style>` sections in the template files, or create separate CSS files and link them.

## 📋 Checklist for New Clients

- [ ] Update `client-config.json` with client information
- [ ] Add client assets to `assets/` folder
- [ ] Update form action URLs
- [ ] Test video embeds
- [ ] Verify all links work
- [ ] Test on mobile devices
- [ ] Run `npm run build`
- [ ] Preview the generated site
- [ ] Deploy to hosting platform

## 🐛 Troubleshooting

### Common Issues

**Template variables not replacing:**
- Check that variable names match exactly in config and template
- Ensure no typos in variable names
- Verify JSON syntax is valid

**Images not loading:**
- Check file paths in config
- Ensure images are in the `assets/` folder
- Verify file extensions are correct

**Forms not working:**
- Update form action URLs
- Check form field names match your backend
- Test form submission

**Video not playing:**
- Verify video embed ID is correct
- Check if video platform is supported
- Test with different browsers

## 📞 Support

For support or questions:
- Email: {{client.email}}
- Phone: {{client.phone}}
- Website: {{client.website}}

## 📄 License

MIT License - feel free to use and modify for your projects.

---

**Happy Funnel Building! 🚀**
