#!/usr/bin/env python3
"""
SZEINER Contact Form Backend API
================================
Jednoduchý Python backend pro zpracování kontaktního formuláře a newsletter signupu.

Použití:
    python contact.py

Závislosti:
    pip install flask flask-cors python-dotenv

Konfigurace:
    Vytvořte .env soubor s následujícími proměnnými:
    - SMTP_HOST=smtp.example.com
    - SMTP_PORT=587
    - SMTP_USER=your@email.com
    - SMTP_PASSWORD=your_password
    - RECIPIENT_EMAIL=info@szeiner.com
    - MAILCHIMP_API_KEY=your_mailchimp_api_key (volitelné)
    - MAILCHIMP_LIST_ID=your_list_id (volitelné)
"""

import os
import re
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from functools import wraps
from typing import Optional, Dict, Any

try:
    from flask import Flask, request, jsonify
    from flask_cors import CORS
except ImportError:
    print("Chyba: Nainstalujte Flask pomocí 'pip install flask flask-cors'")
    exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Varování: python-dotenv není nainstalován, používám proměnné prostředí")

# Konfigurace aplikace
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["https://szeiner.com", "http://localhost:*"]}})

# Nastavení loggeru
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Konfigurace emailu
SMTP_CONFIG = {
    'host': os.getenv('SMTP_HOST', 'smtp.gmail.com'),
    'port': int(os.getenv('SMTP_PORT', 587)),
    'user': os.getenv('SMTP_USER', ''),
    'password': os.getenv('SMTP_PASSWORD', ''),
    'recipient': os.getenv('RECIPIENT_EMAIL', 'info@szeiner.com'),
    'use_tls': os.getenv('SMTP_USE_TLS', 'true').lower() == 'true'
}

# Mailchimp konfigurace (volitelné)
MAILCHIMP_CONFIG = {
    'api_key': os.getenv('MAILCHIMP_API_KEY', ''),
    'list_id': os.getenv('MAILCHIMP_LIST_ID', ''),
    'server': os.getenv('MAILCHIMP_SERVER', 'us1')  # např. us1, us2, atd.
}

# Rate limiting - jednoduchá in-memory implementace
request_counts: Dict[str, list] = {}
RATE_LIMIT = 5  # maximální počet požadavků
RATE_WINDOW = 3600  # za hodinu (v sekundách)


def rate_limit(f):
    """Dekorátor pro rate limiting"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        client_ip = request.remote_addr
        now = datetime.now().timestamp()

        # Vyčistíme staré záznamy
        if client_ip in request_counts:
            request_counts[client_ip] = [
                t for t in request_counts[client_ip]
                if now - t < RATE_WINDOW
            ]
        else:
            request_counts[client_ip] = []

        # Kontrola limitu
        if len(request_counts[client_ip]) >= RATE_LIMIT:
            logger.warning(f"Rate limit překročen pro IP: {client_ip}")
            return jsonify({
                'success': False,
                'error': 'Příliš mnoho požadavků. Zkuste to prosím později.'
            }), 429

        # Přidáme aktuální požadavek
        request_counts[client_ip].append(now)

        return f(*args, **kwargs)
    return decorated_function


def validate_email(email: str) -> bool:
    """Validace emailové adresy"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def sanitize_input(text: str) -> str:
    """Sanitizace vstupního textu"""
    if not text:
        return ''
    # Odstranění HTML tagů
    text = re.sub(r'<[^>]+>', '', text)
    # Omezení délky
    return text[:5000]


def send_email(
    subject: str,
    body: str,
    to_email: Optional[str] = None,
    reply_to: Optional[str] = None
) -> bool:
    """
    Odeslání emailu pomocí SMTP

    Args:
        subject: Předmět emailu
        body: Tělo emailu (HTML)
        to_email: Příjemce (výchozí: RECIPIENT_EMAIL)
        reply_to: Reply-To adresa

    Returns:
        True pokud byl email úspěšně odeslán
    """
    if not SMTP_CONFIG['user'] or not SMTP_CONFIG['password']:
        logger.error("SMTP přihlašovací údaje nejsou nakonfigurovány")
        return False

    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = SMTP_CONFIG['user']
        msg['To'] = to_email or SMTP_CONFIG['recipient']

        if reply_to:
            msg['Reply-To'] = reply_to

        # HTML část
        html_part = MIMEText(body, 'html', 'utf-8')
        msg.attach(html_part)

        # Připojení k SMTP serveru
        if SMTP_CONFIG['use_tls']:
            server = smtplib.SMTP(SMTP_CONFIG['host'], SMTP_CONFIG['port'])
            server.starttls()
        else:
            server = smtplib.SMTP_SSL(SMTP_CONFIG['host'], SMTP_CONFIG['port'])

        server.login(SMTP_CONFIG['user'], SMTP_CONFIG['password'])
        server.send_message(msg)
        server.quit()

        logger.info(f"Email úspěšně odeslán na {msg['To']}")
        return True

    except smtplib.SMTPException as e:
        logger.error(f"SMTP chyba: {e}")
        return False
    except Exception as e:
        logger.error(f"Chyba při odesílání emailu: {e}")
        return False


@app.route('/api/contact', methods=['POST'])
@rate_limit
def contact_form():
    """
    Endpoint pro zpracování kontaktního formuláře

    Očekává JSON s poli:
        - name: Jméno odesílatele (povinné)
        - email: Email odesílatele (povinné)
        - subject: Předmět zprávy (volitelné)
        - message: Zpráva (povinné)
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                'success': False,
                'error': 'Neplatný formát dat'
            }), 400

        # Validace povinných polí
        name = sanitize_input(data.get('name', ''))
        email = data.get('email', '').strip().lower()
        subject = sanitize_input(data.get('subject', 'Kontaktní formulář'))
        message = sanitize_input(data.get('message', ''))

        errors = []

        if not name or len(name) < 2:
            errors.append('Jméno je povinné a musí mít alespoň 2 znaky')

        if not validate_email(email):
            errors.append('Neplatná emailová adresa')

        if not message or len(message) < 10:
            errors.append('Zpráva je povinná a musí mít alespoň 10 znaků')

        if errors:
            return jsonify({
                'success': False,
                'errors': errors
            }), 400

        # Sestavení emailu
        email_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background: linear-gradient(135deg, #8b5cf6, #ec4899); color: white; padding: 20px; border-radius: 8px 8px 0 0; }}
                .content {{ background: #f9f9f9; padding: 20px; border: 1px solid #ddd; border-radius: 0 0 8px 8px; }}
                .field {{ margin-bottom: 15px; }}
                .label {{ font-weight: bold; color: #666; }}
                .value {{ margin-top: 5px; }}
                .footer {{ margin-top: 20px; font-size: 12px; color: #999; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h2>Nová zpráva z kontaktního formuláře</h2>
                </div>
                <div class="content">
                    <div class="field">
                        <div class="label">Jméno:</div>
                        <div class="value">{name}</div>
                    </div>
                    <div class="field">
                        <div class="label">Email:</div>
                        <div class="value"><a href="mailto:{email}">{email}</a></div>
                    </div>
                    <div class="field">
                        <div class="label">Předmět:</div>
                        <div class="value">{subject}</div>
                    </div>
                    <div class="field">
                        <div class="label">Zpráva:</div>
                        <div class="value">{message.replace(chr(10), '<br>')}</div>
                    </div>
                    <div class="footer">
                        <p>Odesláno: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}</p>
                        <p>IP adresa: {request.remote_addr}</p>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

        # Odeslání emailu
        email_sent = send_email(
            subject=f"[SZEINER Web] {subject}",
            body=email_body,
            reply_to=email
        )

        if email_sent:
            logger.info(f"Kontaktní formulář zpracován: {name} <{email}>")
            return jsonify({
                'success': True,
                'message': 'Děkujeme za vaši zprávu. Odpovíme co nejdříve.'
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Nepodařilo se odeslat zprávu. Zkuste to prosím později.'
            }), 500

    except Exception as e:
        logger.error(f"Chyba při zpracování kontaktního formuláře: {e}")
        return jsonify({
            'success': False,
            'error': 'Nastala neočekávaná chyba'
        }), 500


@app.route('/api/newsletter', methods=['POST'])
@rate_limit
def newsletter_signup():
    """
    Endpoint pro přihlášení k newsletteru

    Očekává JSON s polem:
        - email: Email pro přihlášení (povinné)
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                'success': False,
                'error': 'Neplatný formát dat'
            }), 400

        email = data.get('email', '').strip().lower()

        if not validate_email(email):
            return jsonify({
                'success': False,
                'error': 'Neplatná emailová adresa'
            }), 400

        # Pokud je nakonfigurován Mailchimp, použijeme ho
        if MAILCHIMP_CONFIG['api_key'] and MAILCHIMP_CONFIG['list_id']:
            try:
                import requests

                url = f"https://{MAILCHIMP_CONFIG['server']}.api.mailchimp.com/3.0/lists/{MAILCHIMP_CONFIG['list_id']}/members"

                response = requests.post(
                    url,
                    auth=('anystring', MAILCHIMP_CONFIG['api_key']),
                    json={
                        'email_address': email,
                        'status': 'subscribed',
                        'tags': ['website-signup']
                    }
                )

                if response.status_code in [200, 400]:  # 400 = already subscribed
                    logger.info(f"Newsletter signup: {email}")
                    return jsonify({
                        'success': True,
                        'message': 'Děkujeme za přihlášení k odběru novinek!'
                    }), 200
                else:
                    raise Exception(f"Mailchimp API error: {response.text}")

            except ImportError:
                logger.warning("requests není nainstalován, ukládám lokálně")
            except Exception as e:
                logger.error(f"Mailchimp chyba: {e}")

        # Fallback - uložíme do souboru
        subscribers_file = os.path.join(os.path.dirname(__file__), 'subscribers.txt')

        # Kontrola duplicit
        existing_emails = set()
        if os.path.exists(subscribers_file):
            with open(subscribers_file, 'r') as f:
                existing_emails = set(line.strip().split(',')[0] for line in f if line.strip())

        if email in existing_emails:
            return jsonify({
                'success': True,
                'message': 'Tento email je již přihlášen k odběru.'
            }), 200

        # Přidání nového subscribera
        with open(subscribers_file, 'a') as f:
            f.write(f"{email},{datetime.now().isoformat()},{request.remote_addr}\n")

        logger.info(f"Newsletter signup (local): {email}")

        return jsonify({
            'success': True,
            'message': 'Děkujeme za přihlášení k odběru novinek!'
        }), 200

    except Exception as e:
        logger.error(f"Chyba při newsletter signup: {e}")
        return jsonify({
            'success': False,
            'error': 'Nastala neočekávaná chyba'
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'smtp_configured': bool(SMTP_CONFIG['user'] and SMTP_CONFIG['password']),
        'mailchimp_configured': bool(MAILCHIMP_CONFIG['api_key'])
    }), 200


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Endpoint nenalezen'}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Interní chyba serveru'}), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'production') == 'development'

    print(f"""
╔═══════════════════════════════════════════════════════════╗
║           SZEINER Contact Form API Server                 ║
╠═══════════════════════════════════════════════════════════╣
║  Port:      {port}                                          ║
║  Debug:     {debug}                                        ║
║  SMTP:      {'Configured' if SMTP_CONFIG['user'] else 'Not configured'}                               ║
║  Mailchimp: {'Configured' if MAILCHIMP_CONFIG['api_key'] else 'Not configured'}                               ║
╚═══════════════════════════════════════════════════════════╝
    """)

    app.run(host='0.0.0.0', port=port, debug=debug)
