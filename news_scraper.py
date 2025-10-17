import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import time
import re
from dateutil import parser

class RecentFinanceNewsScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.cutoff_time = datetime.now() - timedelta(hours=24)
    
    def parse_relative_time(self, time_str):
        """Convert relative time strings to datetime"""
        try:
            time_str = time_str.lower().strip()
            now = datetime.now()
            
            if 'minute' in time_str or 'min' in time_str:
                mins = int(re.search(r'\d+', time_str).group())
                return now - timedelta(minutes=mins)
            elif 'hour' in time_str or 'hr' in time_str:
                hours = int(re.search(r'\d+', time_str).group())
                return now - timedelta(hours=hours)
            elif 'day' in time_str:
                days = int(re.search(r'\d+', time_str).group())
                return now - timedelta(days=days)
            elif 'yesterday' in time_str:
                return now - timedelta(days=1)
            elif 'today' in time_str or 'just now' in time_str:
                return now
            else:
                # Try parsing absolute date
                return parser.parse(time_str)
        except:
            return None
    
    def is_within_24_hours(self, article_time):
        """Check if article is within last 24 hours"""
        if article_time and article_time >= self.cutoff_time:
            return True
        return False
    
    def scrape_yahoo_finance_recent(self, ticker=None, max_articles=200):
        """Scrape recent news from Yahoo Finance"""
        try:
            if ticker:
                url = f"https://finance.yahoo.com/quote/{ticker}/news"
            else:
                url = "https://finance.yahoo.com/topic/stock-market-news/"
            
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles = []
            # Find article containers
            article_containers = soup.find_all('li', {'class': 'stream-item'})[:max_articles]
            
            for container in article_containers:
                try:
                    # Find title and link
                    title_elem = container.find('h3')
                    if not title_elem:
                        continue
                    
                    link = title_elem.find('a')
                    if not link:
                        continue
                    
                    title = link.get_text(strip=True)
                    article_url = link.get('href', '')
                    if article_url and not article_url.startswith('http'):
                        article_url = 'https://finance.yahoo.com' + article_url
                    
                    # Find timestamp
                    time_elem = container.find('time')
                    if time_elem:
                        time_text = time_elem.get_text(strip=True)
                        article_time = self.parse_relative_time(time_text)
                        
                        # Only include if within 24 hours
                        if self.is_within_24_hours(article_time):
                            articles.append({
                                'title': title,
                                'url': article_url,
                                'source': 'Yahoo Finance',
                                'ticker': ticker if ticker else 'General',
                                'published': time_text,
                                'parsed_time': article_time.strftime('%Y-%m-%d %H:%M:%S') if article_time else None,
                                'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            })
                except Exception as e:
                    continue
            
            return articles
        except Exception as e:
            print(f"Error scraping Yahoo Finance: {e}")
            return []
    
    def scrape_marketwatch_recent(self, max_articles=200):
        """Scrape recent news from MarketWatch"""
        try:
            url = "https://www.marketwatch.com/latest-news"
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles = []
            article_elements = soup.find_all('div', {'class': 'article__content'})[:max_articles]
            
            for elem in article_elements:
                try:
                    title_elem = elem.find('a', {'class': 'link'})
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text(strip=True)
                    article_url = title_elem.get('href', '')
                    if article_url and not article_url.startswith('http'):
                        article_url = 'https://www.marketwatch.com' + article_url
                    
                    # Find timestamp
                    time_elem = elem.find('span', {'class': 'article__timestamp'})
                    if time_elem:
                        time_text = time_elem.get_text(strip=True)
                        article_time = self.parse_relative_time(time_text)
                        
                        if self.is_within_24_hours(article_time):
                            articles.append({
                                'title': title,
                                'url': article_url,
                                'source': 'MarketWatch',
                                'published': time_text,
                                'parsed_time': article_time.strftime('%Y-%m-%d %H:%M:%S') if article_time else None,
                                'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            })
                except Exception as e:
                    continue
            
            return articles
        except Exception as e:
            print(f"Error scraping MarketWatch: {e}")
            return []
    
    def scrape_benzinga_recent(self, max_articles=200):
        """Scrape recent news from Benzinga"""
        try:
            url = "https://www.benzinga.com/news"
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles = []
            article_elements = soup.find_all('div', {'class': 'article'})[:max_articles]
            
            for elem in article_elements:
                try:
                    title_elem = elem.find('a')
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text(strip=True)
                    article_url = title_elem.get('href', '')
                    if article_url and not article_url.startswith('http'):
                        article_url = 'https://www.benzinga.com' + article_url
                    
                    time_elem = elem.find('time')
                    if time_elem:
                        time_text = time_elem.get_text(strip=True)
                        article_time = self.parse_relative_time(time_text)
                        
                        if self.is_within_24_hours(article_time):
                            articles.append({
                                'title': title,
                                'url': article_url,
                                'source': 'Benzinga',
                                'published': time_text,
                                'parsed_time': article_time.strftime('%Y-%m-%d %H:%M:%S') if article_time else None,
                                'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            })
                except Exception as e:
                    continue
            
            return articles
        except Exception as e:
            print(f"Error scraping Benzinga: {e}")
            return []
    
    def scrape_cnbc_recent(self, max_articles=200):
        """Scrape recent news from CNBC"""
        try:
            url = "https://www.cnbc.com/markets/"
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles = []
            article_elements = soup.find_all('div', {'class': 'Card-titleContainer'})[:max_articles]
            
            for elem in article_elements:
                try:
                    title_elem = elem.find('a')
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text(strip=True)
                    article_url = title_elem.get('href', '')
                    
                    # CNBC usually shows recent articles on homepage
                    articles.append({
                        'title': title,
                        'url': article_url,
                        'source': 'CNBC',
                        'published': 'Recent',
                        'parsed_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                except Exception as e:
                    continue
            
            return articles
        except Exception as e:
            print(f"Error scraping CNBC: {e}")
            return []
    
    def scrape_all_sources(self, tickers=None):
        """Scrape from all sources"""
        all_articles = []
        
        print("Scraping Yahoo Finance...")
        all_articles.extend(self.scrape_yahoo_finance_recent())
        time.sleep(2)
        
        if tickers:
            for ticker in tickers:
                print(f"Scraping Yahoo Finance for {ticker}...")
                all_articles.extend(self.scrape_yahoo_finance_recent(ticker))
                time.sleep(2)
        
        print("Scraping MarketWatch...")
        all_articles.extend(self.scrape_marketwatch_recent())
        time.sleep(2)
        
        print("Scraping Benzinga...")
        all_articles.extend(self.scrape_benzinga_recent())
        time.sleep(2)
        
        print("Scraping CNBC...")
        all_articles.extend(self.scrape_cnbc_recent())
        
        return all_articles
    
    def filter_by_keywords(self, articles, keywords):
        """Filter articles by keywords in title"""
        if not keywords:
            return articles
        
        pattern = re.compile('|'.join(keywords), re.IGNORECASE)
        return [a for a in articles if pattern.search(a['title'])]
    
    def remove_duplicates(self, articles):
        """Remove duplicate articles based on URL"""
        unique = []
        seen_urls = set()
        
        for article in articles:
            if article['url'] not in seen_urls:
                unique.append(article)
                seen_urls.add(article['url'])
        
        return unique
    
    def save_to_csv(self, articles, filename='recent_finance_news.csv'):
        """Save articles to CSV"""
        df = pd.DataFrame(articles)
        df.to_csv(filename, index=False)
        print(f"\nSaved {len(articles)} articles to {filename}")
    
    def save_to_json(self, articles, filename='recent_finance_news.json'):
        """Save articles to JSON"""
        df = pd.DataFrame(articles)
        df.to_json(filename, orient='records', indent=2)
        print(f"Saved {len(articles)} articles to {filename}")
    
    def print_summary(self, articles):
        """Print summary of scraped articles"""
        print(f"\n{'='*60}")
        print(f"SCRAPING SUMMARY - Last 24 Hours")
        print(f"{'='*60}")
        print(f"Total articles found: {len(articles)}")
        print(f"Cutoff time: {self.cutoff_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        if articles:
            df = pd.DataFrame(articles)
            print(f"\nArticles by source:")
            print(df['source'].value_counts().to_string())
            
            print(f"\n{'='*60}")
            print("LATEST ARTICLES:")
            print(f"{'='*60}")
            for i, article in enumerate(articles[:10], 1):
                print(f"\n{i}. {article['title']}")
                print(f"   Source: {article['source']} | Published: {article['published']}")
                print(f"   URL: {article['url']}")


# Example usage
if __name__ == "__main__":
    scraper = RecentFinanceNewsScraper()
    
    # Option 1: Scrape all sources for general news
    print("Fetching recent financial news from all sources...")
    articles = scraper.scrape_all_sources()
    
    # Option 2: Include specific tickers
    # tickers = ['AAPL', 'TSLA', 'NVDA', 'MSFT', 'GOOGL']
    # articles = scraper.scrape_all_sources(tickers=tickers)
    
    # Option 3: Filter by keywords
    keywords = ['stock', 'earnings', 'market', 'investment', 'shares', 'trading', 
                'CEO', 'merger', 'acquisition', 'dividend', 'revenue', 'profit']
    filtered_articles = scraper.filter_by_keywords(articles, keywords)
    
    # Remove duplicates
    unique_articles = scraper.remove_duplicates(filtered_articles)
    
    # Sort by most recent
    unique_articles.sort(key=lambda x: x['parsed_time'] if x['parsed_time'] else '', reverse=True)
    
    # Display results
    scraper.print_summary(unique_articles)
    
    # Save results
    scraper.save_to_csv(unique_articles)
    scraper.save_to_json(unique_articles)