#!/usr/bin/env python3
"""Generate About, People, Services, Career, Contact pages."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate import head, TOPBAR, navbar, FOOTER, write

# ========== ABOUT (Company Profile) ==========
ABOUT = f"""{head('About SBL Energy Limited | Company Profile | Industrial Explosives', 'SBL Energy Limited — incorporated 2002. 225-acre facility in Nagpur. Manufacturer of industrial/mining explosives in technical collaboration with CMRI Dhanbad (CSIR).')}
{TOPBAR}
{navbar('about')}

<section class="page-hero">
  <div class="page-hero-bg" style="background-image:url('images/hero/manufacturing-floor.jpg')"></div>
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <nav class="breadcrumb"><a href="index.html">Home</a><span>›</span><span class="current">About Us</span></nav>
    <div class="prod-hero-tag"><span class="dot"></span> LEARN MORE</div>
    <h1 class="prod-hero-title">About Us.</h1>
    <p class="prod-hero-sub">Since our inception, SBL Energy has totally focused on building an ethical work environment &amp; delivering excellence in the field of industrial / mining explosives manufacturing.</p>
  </div>
</section>

<section class="section">
  <div class="container about-grid">
    <div class="about-visual reveal">
      <div class="visual-frame">
        <img src="images/hero/facility-aerial.jpg" alt="SBL Energy facility aerial view" class="visual-image"/>
        <div class="visual-badge">
          <div class="badge-num">2002</div>
          <div class="badge-text">Year<br/>Incorporated</div>
        </div>
      </div>
    </div>
    <div class="about-text reveal">
      <div class="section-tag"><span class="tag-line"></span> COMPANY PROFILE</div>
      <h2 class="section-title">An <span class="accent">acclaimed manufacturer</span> of industrial explosives since 2002.</h2>
      <p class="lead">SBL ENERGY LIMITED is an acclaimed company that was incorporated in the year 2002 with the purpose of manufacturing industrial explosives and accessories. The factory is spread over 225 acres of land and is located 45 km from Nagpur at Village — Yenerva, Tahsil Katol, District Nagpur, in the state of Maharashtra, India.</p>
      <p>The production units are very modern and are set up in technical collaboration with the <strong>Central Mining Research Institute (CMRI) Dhanbad</strong> — a Government of India body under the Council of Scientific and Industrial Research (CSIR).</p>
      <p>Today, we manufacture a complete range of Commercial High Explosives (slurry/emulsion cartridges), Bulk Explosives, all kinds of Detonators, Detonating Fuse and PETN. Experience and expertise have made the group one of the leading producers of industrial explosives and accessories in India.</p>
    </div>
  </div>
</section>

<section class="capacity">
  <div class="container">
    <div class="cap-head reveal">
      <div class="section-tag light"><span class="tag-line"></span> ANNUAL MANUFACTURING CAPACITY (APPROVED BY PESO)</div>
      <h2 class="section-title light">One of India's largest <span class="accent">approved capacities.</span></h2>
    </div>
    <div class="cap-grid">
      <div class="cap-card reveal"><div class="cap-num">50,000 <span>MT</span></div><div class="cap-label">Cartridge Explosive<br/>(Emulsion / Slurry)</div></div>
      <div class="cap-card reveal"><div class="cap-num">21,699 <span>MT</span></div><div class="cap-label">Bulk Explosive</div></div>
      <div class="cap-card reveal"><div class="cap-num">45 <span>Million</span></div><div class="cap-label">Detonators</div></div>
      <div class="cap-card reveal"><div class="cap-num">55 <span>Million m</span></div><div class="cap-label">Detonating Fuse</div></div>
      <div class="cap-card reveal"><div class="cap-num">400 <span>MT</span></div><div class="cap-label">PETN</div></div>
    </div>
  </div>
</section>

<section class="section vmv">
  <div class="container">
    <div class="section-head reveal">
      <div class="section-tag"><span class="tag-line"></span> WHO WE ARE</div>
      <h2 class="section-title">Vision, Mission &amp; <span class="accent">Values.</span></h2>
    </div>
    <div class="vmv-grid">
      <div class="vmv-card reveal">
        <div class="vmv-num">⬢ 01</div><h3>Vision</h3>
        <p>To be the most dependable, respected, safest, value-driven and customer-centric company in the industrial explosives industry.</p>
      </div>
      <div class="vmv-card reveal">
        <div class="vmv-num">⬢ 02</div><h3>Mission</h3>
        <p>To deliver world-class explosives and end-to-end blasting solutions backed by rigorous quality control, modern technology and dedicated technical support.</p>
      </div>
      <div class="vmv-card reveal">
        <div class="vmv-num">⬢ 03</div><h3>Values</h3>
        <p>We commit to ethical and value-driven business practices and strive for trustworthiness, innovation &amp; customer satisfaction while caring for our employees, labour and the society.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="container cta-inner">
    <div class="cta-text"><h2>Want to learn more about our team?</h2><p>Meet the engineers and leaders behind SBL Energy Limited.</p></div>
    <div class="cta-actions"><a href="people-clients.html" class="btn btn-white">Meet the team <span class="arrow">→</span></a></div>
  </div>
</section>

{FOOTER}"""

# ========== PEOPLE & CLIENTS ==========
PEOPLE = f"""{head('People & Clients | SBL Energy Limited', 'Meet the leadership at SBL Energy Limited and explore some of our major clients including Aditya Birla Group, Coal India, Reliance, ACC, MOIL and SAIL.')}
{TOPBAR}
{navbar('about')}

<section class="page-hero">
  <div class="page-hero-bg" style="background-image:url('images/hero/manufacturing-floor.jpg')"></div>
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <nav class="breadcrumb"><a href="index.html">Home</a><span>›</span><a href="about.html">About Us</a><span>›</span><span class="current">People &amp; Clients</span></nav>
    <div class="prod-hero-tag"><span class="dot"></span> MEET THE TEAM</div>
    <h1 class="prod-hero-title">People &amp; Clients.</h1>
    <p class="prod-hero-sub">The people who lead SBL Energy Limited — and some of the major mining, cement and infrastructure groups who trust us.</p>
  </div>
</section>

<section class="section team">
  <div class="container">
    <div class="section-head reveal">
      <div class="section-tag"><span class="tag-line"></span> MEET THE TEAM</div>
      <h2 class="section-title">The people behind<br/><span class="accent">SBL Energy Limited.</span></h2>
    </div>
    <div class="team-grid">
      <div class="team-card reveal">
        <div class="team-initials">BK</div>
        <h3>BK Paul</h3>
        <div class="team-role">Production Head</div>
        <p>Master's degree in Chemistry with 40 years of experience in manufacturing industrial explosives. Formerly with India's biggest explosives company. Expert in emulsion explosives and developer of Permitted emulsion explosives P1, P3 &amp; P5, along with Nitroglycerin-based permitted explosives for long-hole gallery blasting.</p>
      </div>
      <div class="team-card reveal">
        <div class="team-initials">CS</div>
        <h3>CS Parhadkar</h3>
        <div class="team-role">Administrative Head</div>
        <p>Experienced mining engineer with 33 years in the field of explosive marketing and technical services. Has served the industry at various levels and joined SBL Energy in 2009 as the Marketing Head.</p>
      </div>
      <div class="team-card reveal">
        <div class="team-initials">AJ</div>
        <h3>Abhishek Jaiswal</h3>
        <div class="team-role">General Manager — Marketing &amp; Administration</div>
        <p>A highly qualified professional with exceptional managerial skills. Heads the Marketing and Administration of the company and manages all import/export operations and transactions.</p>
      </div>
      <div class="team-card reveal">
        <div class="team-initials">PJ</div>
        <h3>Pradeep Jain</h3>
        <div class="team-role">R&amp;D Head</div>
        <p>Post-graduate in Chemistry with 12+ years of experience in manufacturing units of explosives, pharmaceuticals and defense products. Leads the in-house R&amp;D department.</p>
      </div>
      <div class="team-card reveal">
        <div class="team-initials">VN</div>
        <h3>Mr. Vaidya Nathan</h3>
        <div class="team-role">President — Global Sales</div>
        <p>10+ years in the explosives export business with commendable achievements. Previously served the Indian Air Force for 16 years and has 7 years of experience in telecom and networking projects.</p>
      </div>
      <div class="team-card reveal">
        <div class="team-initials">AK</div>
        <h3>AK Singh</h3>
        <div class="team-role">CGM Quality</div>
        <p>Leads the quality assurance and control operations across SBL Energy's manufacturing facilities, ensuring rigid QC at every step of production.</p>
      </div>
    </div>
  </div>
</section>

<section class="section clients-section">
  <div class="container">
    <div class="section-head reveal">
      <div class="section-tag"><span class="tag-line"></span> OUR CLIENTS</div>
      <h2 class="section-title">Some of our <span class="accent">major clients.</span></h2>
      <p class="lead" style="margin-top:18px;max-width:760px">SBL Energy is proud to supply industrial explosives and accessories to some of India's largest mining, cement, steel and infrastructure groups.</p>
    </div>
    <div class="client-grid reveal">
      <div class="client-logo"><img src="images/clients/aditya-birla.jpg" alt="Aditya Birla Group"/></div>
      <div class="client-logo"><img src="images/clients/coal-india.jpg" alt="Coal India Limited"/></div>
      <div class="client-logo"><img src="images/clients/ucil.jpg" alt="UCIL"/></div>
      <div class="client-logo"><img src="images/clients/reliance.jpg" alt="Reliance Industries"/></div>
      <div class="client-logo"><img src="images/clients/acc.jpg" alt="ACC Cement"/></div>
      <div class="client-logo"><img src="images/clients/moil.jpg" alt="MOIL"/></div>
      <div class="client-logo"><img src="images/clients/sail.jpg" alt="SAIL"/></div>
      <div class="client-logo"><img src="images/clients/birla-corp.jpg" alt="Birla Corporation"/></div>
      <div class="client-logo"><img src="images/clients/ultratech.jpg" alt="UltraTech Cement"/></div>
      <div class="client-logo"><img src="images/clients/lafarge.png" alt="Lafarge Cement"/></div>
      <div class="client-logo"><img src="images/clients/hpcl.png" alt="Hindustan Petroleum"/></div>
      <div class="client-logo"><img src="images/clients/jaiprakash.jpg" alt="Jaiprakash Power Ventures"/></div>
    </div>
  </div>
</section>

{FOOTER}"""

# ========== SERVICES ==========
SERVICES = f"""{head('Services | Consultancy & Technical Blast Management | SBL Energy', 'SBL Energy — consultancy, blast design, blast management, explosive selection, technical blast management services. Team of 50 mining engineers dedicated to optimisation.')}
{TOPBAR}
{navbar('services')}

<section class="page-hero">
  <div class="page-hero-bg" style="background-image:url('images/hero/blast-panoramic.jpg')"></div>
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <nav class="breadcrumb"><a href="index.html">Home</a><span>›</span><span class="current">Services</span></nav>
    <div class="prod-hero-tag"><span class="dot"></span> SERVICES</div>
    <h1 class="prod-hero-title">Consultancy &amp; Technical Blast Management.</h1>
    <p class="prod-hero-sub">Our efforts have always been towards optimisation of the mining system in total — not just the reduction in blasting cost.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div class="section-tag"><span class="tag-line"></span> CONSULTANCY SERVICE</div>
      <h2 class="section-title">We are here to help you<br/>select the right product for <span class="accent">your requirements.</span></h2>
    </div>
    <div class="services-text reveal">
      <p class="lead">We extend our services to ensure that our customers get maximum benefit. This is possible with the help of the latest technology and a great Consultancy Service Team. Our consultancy service group is supported by a team of expert mining/blasting engineers.</p>
      <h4 class="svc-subhead">We assist our customers in:</h4>
      <ul class="adv-list">
        <li><span class="check">✓</span>Explosive selection</li>
        <li><span class="check">✓</span>Blast management and optimization</li>
        <li><span class="check">✓</span>Blast Design</li>
        <li><span class="check">✓</span>Explosive regulatory compliance</li>
      </ul>
      <p>Our profound Sales &amp; Technical engineers give customers a complete insight on designs, measurements, applications, safety, training &amp; handling of our products. Professional knowledge on drilling, blasting, mine development activities, analysis and rock-face analysis is also provided.</p>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head reveal">
      <div class="section-tag light"><span class="tag-line"></span> TECHNICAL BLAST MANAGEMENT</div>
      <h2 class="section-title light">SBL has a team of<br/><span class="accent">50 mining engineers.</span></h2>
    </div>
    <div class="services-text light reveal">
      <p class="lead" style="color:rgba(255,255,255,.8)">We have completely dedicated ourselves to this area as we understand the importance of providing technical services to our customers. Technical services are always available by SBL on prior notice. Our technical services wing can handle problems related to blast &amp; cost optimization, controlled blasting and blast design — along with imparting training to perform the assignments.</p>
      <h4 class="svc-subhead light">We will concentrate on blasting by:</h4>
      <ul class="adv-list light">
        <li><span class="check">✓</span>Controlling vibrations</li>
        <li><span class="check">✓</span>Top fragmentation</li>
        <li><span class="check">✓</span>Digging ability of the muck-pile profile</li>
        <li><span class="check">✓</span>Overall blasting cost with considerable results</li>
      </ul>
      <h4 class="svc-subhead light" style="margin-top:36px">Special technical services:</h4>
      <ul class="adv-list light">
        <li><span class="check">✓</span>Improving the power factor at the Dragline bench to challenging levels</li>
        <li><span class="check">✓</span>Sessions on blasting technology for blasting officers and managers</li>
      </ul>
      <p style="color:rgba(255,255,255,.65);margin-top:24px">Our technical services cell is continuously updating the user on all the latest technical developments on blasting products, technology and applications.</p>
    </div>
  </div>
</section>

<section class="section vmv">
  <div class="container">
    <div class="section-head reveal">
      <div class="section-tag"><span class="tag-line"></span> RESEARCH &amp; DEVELOPMENT</div>
      <h2 class="section-title">A dedicated <span class="accent">R&amp;D cell.</span></h2>
    </div>
    <div class="services-text reveal">
      <p class="lead">We have a special cell for R&amp;D, headed by our consultant. All the personnel have an experience of 10 to 30 years in the explosives industry.</p>
      <p>It is our endeavour to give the best products to our customers and also to introduce more and more products in our product-line in order to cater to the special needs of our customers. We are also in the process of developing the entire series of permitted explosives through our own R&amp;D efforts.</p>
      <p>We're committed to continuously improving the way we manage our environmental impacts and develop sustainable business — to achieve all of this we have a special cell headed by our consultant.</p>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="container cta-inner">
    <div class="cta-text"><h2>Need our technical team on-site?</h2><p>Contact us to discuss your blast optimization, R&amp;D or consultancy requirements.</p></div>
    <div class="cta-actions"><a href="contact.html" class="btn btn-white">Get in touch <span class="arrow">→</span></a></div>
  </div>
</section>

{FOOTER}"""

# ========== CAREER ==========
CAREER = f"""{head('Join SBL Energy Limited | Career Opportunities', "Join one of India's top-rated industrial explosives manufacturers. Apply for positions at our Nagpur facility — chemical engineers, mining engineers, plant operators.")}
{TOPBAR}
{navbar('career')}

<section class="page-hero">
  <div class="page-hero-bg" style="background-image:url('images/hero/manufacturing-floor.jpg')"></div>
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <nav class="breadcrumb"><a href="index.html">Home</a><span>›</span><span class="current">Career</span></nav>
    <div class="prod-hero-tag"><span class="dot"></span> JOIN SBL ENERGY LIMITED</div>
    <h1 class="prod-hero-title">Come work with us.</h1>
    <p class="prod-hero-sub">SBL Energy Limited is one of the top-rated mining/industrial explosives manufacturers in India, incorporated in 2002. We are always looking for talented people to join our growing team.</p>
  </div>
</section>

<section class="section">
  <div class="container career-grid">
    <div class="career-text reveal">
      <div class="section-tag"><span class="tag-line"></span> WORK WITH US</div>
      <h2 class="section-title">At SBL Energy Limited<br/>we look for <span class="accent">talented professionals.</span></h2>
      <p class="lead">If you're interested in being part of India's leading industrial explosives manufacturer, share your details and the position you're applying for — our HR team will get back to you within a few working days.</p>
      <p>We hire across production, R&amp;D, quality control, marketing, technical services, plant operations and corporate functions at both our office in Shivaji Nagar, Nagpur and our manufacturing facility at Yenvera.</p>
      <div class="contact-blocks" style="margin-top:30px">
        <div class="contact-block">
          <h4>HR Contact</h4>
          <p>Vikas Mishra</p>
          <a href="tel:+917972232886">+91-7972232886</a>
          <a href="mailto:info@sblenergy.com">info@sblenergy.com</a>
        </div>
        <div class="contact-block">
          <h4>Office Address</h4>
          <p>230, Hill Road, Da Rock Building, 2nd Floor, Shivaji Nagar, Nagpur — 440010</p>
        </div>
      </div>
    </div>

    <div class="career-form-wrap reveal">
      <form class="contact-form" onsubmit="event.preventDefault(); alert('Thank you — our HR team will reach out shortly.'); this.reset();">
        <h3>Come Work With Us</h3>
        <div class="form-field"><label>Full Name</label><input type="text" required placeholder="Your full name" /></div>
        <div class="form-row">
          <div class="form-field"><label>Email</label><input type="email" required placeholder="you@example.com" /></div>
          <div class="form-field"><label>Phone</label><input type="tel" placeholder="+91-" /></div>
        </div>
        <div class="form-field"><label>Applying for the position</label><input type="text" placeholder="e.g. Production Engineer" /></div>
        <div class="form-field"><label>Cover Note</label><textarea rows="4" placeholder="Tell us a bit about your background..."></textarea></div>
        <button type="submit" class="btn btn-primary btn-full">Apply Now <span class="arrow">→</span></button>
      </form>
    </div>
  </div>
</section>

{FOOTER}"""

# ========== CONTACT ==========
CONTACT = f"""{head('Contact SBL Energy Limited | Industrial Explosives Manufacturer Nagpur', 'Contact SBL Energy. Phone: +91-712-2542357. Email: info@sblenergy.com. Office: Shivaji Nagar, Nagpur. Plant: Yenvera, Katol, Nagpur.')}
{TOPBAR}
{navbar('contact')}

<section class="page-hero">
  <div class="page-hero-bg" style="background-image:url('images/hero/facility-aerial.jpg')"></div>
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <nav class="breadcrumb"><a href="index.html">Home</a><span>›</span><span class="current">Contact</span></nav>
    <div class="prod-hero-tag"><span class="dot"></span> CONTACT US</div>
    <h1 class="prod-hero-title">Need an Estimate?<br/>Let's talk.</h1>
    <p class="prod-hero-sub">Please fill the contact form, call us or email us. Our team responds within one business day.</p>
  </div>
</section>

<section class="section">
  <div class="container contact-grid">
    <div class="contact-info reveal">
      <div class="section-tag"><span class="tag-line"></span> REACH US</div>
      <h2 class="section-title">Get in <span class="accent">touch.</span></h2>
      <div class="contact-blocks">
        <div class="contact-block">
          <h4>Domestic Sales / Purchase</h4>
          <a href="tel:+919158898202">+91-9158898202</a>
          <a href="tel:+917887888986">+91-7887888986</a>
          <a href="tel:+917122542357">+91-712-2542357</a>
          <a href="tel:+917122543257">+91-712-2543257</a>
        </div>
        <div class="contact-block">
          <h4>Import / Export</h4>
          <a href="tel:+919980837004">+91-9980837004</a>
          <a href="tel:+918308810133">+91-8308810133</a>
        </div>
        <div class="contact-block">
          <h4>HR — Vikas Mishra</h4>
          <a href="tel:+917972232886">+91-7972232886</a>
        </div>
        <div class="contact-block">
          <h4>Email</h4>
          <a href="mailto:info@sblenergy.com">info@sblenergy.com</a>
        </div>
        <div class="contact-block full">
          <h4>Office Address</h4>
          <p>230, Hill Road, Da Rock Building, 2nd Floor,<br/>Shivaji Nagar, Nagpur — 440010 (MH), India.</p>
        </div>
        <div class="contact-block full">
          <h4>Manufacturing Plant</h4>
          <p>At Yenvera, Post — Raulgaon, Tah. Katol,<br/>Dist. Nagpur — 441502 (MH), India.</p>
        </div>
        <div class="contact-block full">
          <h4>Opening Hours</h4>
          <p>Mon–Fri: 9:00 am – 6:00 pm<br/>Saturday: 9:00 am – 4:00 pm<br/>Sunday: Closed</p>
        </div>
      </div>
    </div>

    <div class="contact-form-wrap reveal">
      <form class="contact-form" onsubmit="event.preventDefault(); alert('Thank you — our team will reach out shortly.'); this.reset();">
        <h3>Contact Form</h3>
        <div class="form-row">
          <div class="form-field"><label>Name</label><input type="text" required placeholder="Your name" /></div>
          <div class="form-field"><label>Country</label><input type="text" placeholder="Country" /></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label>Email</label><input type="email" required placeholder="you@company.com" /></div>
          <div class="form-field"><label>Phone</label><input type="tel" placeholder="+91-" /></div>
        </div>
        <div class="form-field"><label>Type your requirement here</label><textarea rows="5" placeholder="Tell us about your requirements..."></textarea></div>
        <button type="submit" class="btn btn-primary btn-full">Send <span class="arrow">→</span></button>
      </form>
    </div>
  </div>
</section>

{FOOTER}"""

# Write all pages
write('about.html', ABOUT)
write('people-clients.html', PEOPLE)
write('services.html', SERVICES)
write('career.html', CAREER)
write('contact.html', CONTACT)
print("\nDone.")
