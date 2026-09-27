# Kalshi Weather Paper Bot

Paper-trades Kalshi's daily high-temperature markets (NY, Chicago, Miami, Austin, Denver, LA, Philadelphia). **No real money, no Kalshi account needed.**

**How it works:** every 3 hours it pulls the National Weather Service forecast for tomorrow's high, estimates the odds for each Kalshi temperature bracket, and logs a fake 10-contract trade when the odds beat the price by at least 8 cents after fees. Once Kalshi settles a market, the bot scores the trade.

- `trades.csv` holds every paper trade and its result.
- Each run's summary line (wins, P&L, return on risk) shows on its page under the **Actions** tab.
- **Run it now:** Actions → paper-trade → Run workflow.

Settings (edge, size, forecast error) are at the top of `bot.py`.
