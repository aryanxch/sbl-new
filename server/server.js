const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '.env') });
const express = require('express');
const nodemailer = require('nodemailer');

const PORT = process.env.PORT || 8123;
const SITE_ROOT = path.join(__dirname, '..');
const TO_EMAIL = process.env.TO_EMAIL || 'info@sblenergy.com';
// Career applications can go to a separate HR inbox; falls back to TO_EMAIL if unset.
const CAREER_EMAIL = process.env.CAREER_EMAIL || TO_EMAIL;

const app = express();
app.use(express.json());
// No caching while testing locally — avoids the browser silently running stale JS/HTML.
app.use(express.static(SITE_ROOT, { setHeaders: (res) => res.setHeader('Cache-Control', 'no-store') }));

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.GMAIL_USER,
    pass: process.env.GMAIL_APP_PASSWORD,
  },
});

// Very small in-memory rate limit: max 5 submissions per IP per 10 minutes.
const hits = new Map();
function rateLimited(ip) {
  const now = Date.now();
  const windowMs = 10 * 60 * 1000;
  const entry = hits.get(ip) || [];
  const recent = entry.filter((t) => now - t < windowMs);
  recent.push(now);
  hits.set(ip, recent);
  return recent.length > 5;
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function makeFormHandler({ toEmail, subjectPrefix, buildHtml, logLabel }) {
  return async (req, res) => {
    const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
    if (rateLimited(ip)) {
      return res.status(429).json({ error: 'Too many requests, please try again later.' });
    }

    const { name, email, website } = req.body || {};

    // Honeypot: bots fill every field, real users never see/fill this one.
    if (website) {
      return res.status(200).json({ ok: true });
    }

    if (!name || !email) {
      return res.status(400).json({ error: 'Name and email are required.' });
    }
    if (!emailPattern.test(email)) {
      return res.status(400).json({ error: 'Invalid email address.' });
    }

    try {
      const info = await transporter.sendMail({
        from: `"SBL Energy Website" <${process.env.GMAIL_USER}>`,
        to: toEmail,
        replyTo: escapeHtml(email),
        subject: `${subjectPrefix} ${escapeHtml(name)}`,
        html: buildHtml(req.body),
      });
      console.log(`${logLabel} accepted by Gmail:`, info.messageId, info.response);
      res.json({ ok: true });
    } catch (err) {
      console.error(`Failed to send ${logLabel.toLowerCase()}:`, err.message);
      res.status(500).json({ error: 'Failed to send message.' });
    }
  };
}

app.post('/api/contact', makeFormHandler({
  toEmail: TO_EMAIL,
  subjectPrefix: 'New enquiry from',
  logLabel: 'Contact email',
  buildHtml: ({ name, email, country, phone, message }) => {
    const safe = {
      name: escapeHtml(name).slice(0, 200),
      email: escapeHtml(email).slice(0, 200),
      country: escapeHtml(country || '—').slice(0, 100),
      phone: escapeHtml(phone || '—').slice(0, 50),
      message: escapeHtml(message || '—').slice(0, 5000),
    };
    return `
      <h2>New website enquiry</h2>
      <p><strong>Name:</strong> ${safe.name}</p>
      <p><strong>Email:</strong> ${safe.email}</p>
      <p><strong>Country:</strong> ${safe.country}</p>
      <p><strong>Phone:</strong> ${safe.phone}</p>
      <p><strong>Message:</strong><br>${safe.message.replace(/\n/g, '<br>')}</p>
    `;
  },
}));

app.post('/api/career', makeFormHandler({
  toEmail: CAREER_EMAIL,
  subjectPrefix: 'New job application from',
  logLabel: 'Career application email',
  buildHtml: ({ name, email, phone, position, message }) => {
    const safe = {
      name: escapeHtml(name).slice(0, 200),
      email: escapeHtml(email).slice(0, 200),
      phone: escapeHtml(phone || '—').slice(0, 50),
      position: escapeHtml(position || '—').slice(0, 150),
      message: escapeHtml(message || '—').slice(0, 5000),
    };
    return `
      <h2>New job application</h2>
      <p><strong>Name:</strong> ${safe.name}</p>
      <p><strong>Email:</strong> ${safe.email}</p>
      <p><strong>Phone:</strong> ${safe.phone}</p>
      <p><strong>Applying for:</strong> ${safe.position}</p>
      <p><strong>Cover note:</strong><br>${safe.message.replace(/\n/g, '<br>')}</p>
    `;
  },
}));

app.listen(PORT, () => {
  console.log(`SBL Energy site + contact API running on http://localhost:${PORT}`);
});
