# Kalshi Paper Bots

Paper-trades Kalshi's daily high-temperature markets (NY, Chicago, Miami, Austin, Denver, LA, Philadelphia). **No real money, no Kalshi account needed.**

**How it works:** every 3 hours it pulls the National Weather Service forecast for tomorrow's high, estimates the odds for each Kalshi temperature bracket, and logs a fake 10-contract trade when the odds beat the price by at least 8 cents after fees. Once Kalshi settles a market, the bot scores the trade.

- `trades.csv` holds every paper trade and its result.
- Each run's summary line (wins, P&L, return on risk) shows on its page under the **Actions** tab.
- **Run it now:** Actions → paper-trade → Run workflow.

Settings (edge, size, forecast error) are at the top of `bot.py`.

## Bots
| Bot | File | Log | Idea |
|---|---|---|---|
| Temperature | `bot.py` | `trades.csv` | NWS forecast high vs Kalshi daily high brackets |
| Rain | `rain_bot.py` | `rain_trades.csv` | NWS hourly rain chance vs Kalshi "Will it rain?" markets (28 cities) |
| Longshot fade | `longshot_bot.py` | `longshot_trades.csv` | Bets against liquid long shots (YES ≤ 10¢) closing within a week |
| MLB 1-cent | `mlb_bot.py` | `mlb_trades.csv`, `mlb_price_log.csv` | Buys a team at 1¢ mid-game (checked live against MLB's feed), holds to the final out, logs the price every minute |
| NFL / NHL 1-cent | `one_cent_bot.py` | `nfl_trades.csv`, `nfl_price_log.csv`, `nhl_trades.csv`, `nhl_price_log.csv` | Same as MLB 1-cent, live-checked against ESPN's scoreboard |
