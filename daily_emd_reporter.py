#!/usr/bin/env python3
"""
Daily EMD Reporter for GitHub Actions
Automatically fetches property addresses from Podio's Daily EMD Due Report
and posts them to Slack channel daily.
"""

import os
import sys
import logging
import requests
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class PodioAPI:
    def __init__(self):
        self.client_id = os.getenv('PODIO_CLIENT_ID')
        self.client_secret = os.getenv('PODIO_CLIENT_SECRET')
        self.username = os.getenv('PODIO_USERNAME')
        self.password = os.getenv('PODIO_PASSWORD')
        self.app_id = os.getenv('PODIO_APP_ID')
        self.view_id = os.getenv('PODIO_VIEW_ID')
        self.access_token = None
        
        if not all([self.client_id, self.client_secret, self.username, self.password, self.app_id, self.view_id]):
            raise ValueError("Missing required Podio environment variables")
    
    def authenticate(self):
        """Authenticate with Podio API and get access token"""
        auth_url = "https://podio.com/oauth/token"
        auth_data = {
            'grant_type': 'password',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': self.username,
            'password': self.password
        }
        
        response = requests.post(auth_url, data=auth_data)
        response.raise_for_status()
        
        auth_result = response.json()
        self.access_token = auth_result['access_token']
        logger.info("Successfully authenticated with Podio API")
    
    @property
    def headers(self):
        """Get headers for API requests"""
        if not self.access_token:
            raise ValueError("Not authenticated. Call authenticate() first.")
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
    
    def fetch_emd_due_items(self):
        """Fetch items from the Daily EMD Due Report view"""
        url = f"https://api.podio.com/item/app/{self.app_id}/?view_id={self.view_id}"
        
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        
        data = response.json()
        items = data.get('items', [])
        logger.info(f"Successfully fetched {len(items)} items from Daily EMD Due Report view")
        
        return items

class SlackNotifier:
    def __init__(self):
        self.webhook_url = os.getenv('SLACK_WEBHOOK_URL')
        if not self.webhook_url:
            raise ValueError("Missing SLACK_WEBHOOK_URL environment variable")
    
    def post_message(self, message):
        """Post message to Slack channel"""
        payload = {
            'text': message,
            'username': 'Daily EMD Reporter',
            'icon_emoji': ':house:'
        }
        
        response = requests.post(self.webhook_url, json=payload)
        response.raise_for_status()
        logger.info("Successfully posted message to Slack")

class EMDReporter:
    def __init__(self):
        self.podio_api = PodioAPI()
        self.slack_notifier = SlackNotifier()
    
    def extract_property_addresses(self, items):
        """Extract property addresses from Podio items"""
        addresses = []
        
        for item in items:
            fields = item.get('fields', [])
            
            # Look for the field containing property address
            for field in fields:
                if field.get('external_id') == 'deal-text' or 'address' in field.get('label', '').lower():
                    values = field.get('values', [])
                    if values and len(values) > 0:
                        value = values[0].get('value', '')
                        if value and isinstance(value, str):
                            # Clean up the address
                            address = value.strip()
                            if address and len(address) > 10:  # Basic validation
                                addresses.append(address)
                            break
        
        logger.info(f"Extracted {len(addresses)} property addresses")
        return addresses
    
    def format_slack_message(self, addresses):
        """Format addresses into a Slack message"""
        if not addresses:
            return "📋 **Daily EMD Due Report**\n\nNo properties with EMD due today."
        
        message = "📋 **Daily EMD Due Report - Property Addresses**\n\n"
        
        for i, address in enumerate(addresses, 1):
            message += f"{i}. **{address}**\n"
        
        message += f"\n*Total: {len(addresses)} properties with EMD due*"
        
        return message
    
    def run_daily_report(self):
        """Execute the daily EMD report process"""
        try:
            logger.info("Starting daily EMD report process")
            
            # Authenticate with Podio
            self.podio_api.authenticate()
            
            # Fetch EMD due items
            items = self.podio_api.fetch_emd_due_items()
            
            # Extract property addresses
            addresses = self.extract_property_addresses(items)
            
            # Format and post to Slack
            message = self.format_slack_message(addresses)
            self.slack_notifier.post_message(message)
            
            logger.info("Daily EMD report completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error in daily EMD report: {str(e)}")
            # Post error message to Slack
            try:
                error_message = f"❌ **Daily EMD Reporter Error**\n\nFailed to generate report: {str(e)}"
                self.slack_notifier.post_message(error_message)
            except:
                pass
            return False

def main():
    """Main function"""
    logger.info("Daily EMD Reporter starting...")
    
    try:
        reporter = EMDReporter()
        success = reporter.run_daily_report()
        
        if success:
            logger.info("Daily EMD Reporter completed successfully")
            sys.exit(0)
        else:
            logger.error("Daily EMD Reporter failed")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

