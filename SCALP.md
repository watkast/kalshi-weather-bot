# Range-Scalp Bot

*Updated Wed Nov 18 17:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64246 | 56029 | 8217 (124) | 1 | $-17573.28 | -4.3% |
| **+10¢** | 47984 | 38369 | 9615 (165) | 1 | $-16459.41 | -5.5% |
| **+15¢** | 40230 | 29867 | 10363 (210) | 2 | $-14902.61 | -5.9% |
| **+20¢** | 35822 | 24945 | 10877 (265) | 2 | $-13204.31 | -5.9% |
| **+10¢ (15¢ stop)** | 78164 | 78000 | 164 (98) | 0 | $-28798.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 17:12 | +10 stop | ZEC | UP | 0.57 | 0.72 | 1.17 |
| 11-18 17:12 | +20 | ZEC | UP | 0.57 | 0.91 | 3.13 |
| 11-18 17:12 | +15 | ZEC | UP | 0.56 | 0.72 | 1.27 |
| 11-18 17:12 | +10 | ZEC | UP | 0.55 | 0.72 | 1.37 |
| 11-18 17:12 | +5 | ZEC | UP | 0.55 | 0.72 | 1.37 |
| 11-18 17:11 | +10 stop | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-18 17:11 | +10 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-18 17:11 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-18 17:11 | +10 stop | BTC | UP | 0.41 | 0.55 | 1.05 |
| 11-18 17:11 | +20 | BTC | UP | 0.41 | open |  |
| 11-18 17:11 | +15 | BTC | UP | 0.41 | open |  |
| 11-18 17:11 | +10 | BTC | UP | 0.41 | 0.55 | 1.05 |
| 11-18 17:11 | +5 | BTC | UP | 0.41 | 0.55 | 1.05 |
| 11-18 17:07 | +10 stop | HYPE | UP | 0.65 | 0.35 | -3.32 |
| 11-18 17:05 | +10 stop | HYPE | DOWN | 0.61 | 0.41 | -2.34 |
| 11-18 17:04 | +10 stop | HYPE | UP | 0.62 | 0.38 | -2.74 |
| 11-18 17:04 | +20 | HYPE | UP | 0.63 | open |  |
| 11-18 17:01 | +10 stop | BTC | UP | 0.68 | 0.79 | 0.82 |
| 11-18 17:01 | +20 | BTC | UP | 0.68 | 0.88 | 1.76 |
| 11-18 17:01 | +15 | BTC | UP | 0.68 | 0.85 | 1.45 |
| 11-18 17:01 | +10 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-18 17:01 | +5 | BTC | UP | 0.66 | 0.76 | 0.71 |
| 11-18 17:01 | +15 | HYPE | UP | 0.71 | open |  |
| 11-18 17:01 | +10 | HYPE | UP | 0.71 | open |  |
| 11-18 17:01 | +5 | HYPE | UP | 0.71 | open |  |
| 11-18 16:58 | +10 stop | NEAR | DOWN | 0.47 | 0.60 | 0.95 |
| 11-18 16:56 | +5 | BNB | UP | 0.66 | 0.74 | 0.50 |
| 11-18 16:56 | +10 stop | BNB | UP | 0.65 | 0.75 | 0.70 |
| 11-18 16:54 | +10 stop | DOGE | UP | 0.65 | 0.82 | 1.39 |
| 11-18 16:54 | +20 | DOGE | UP | 0.63 | 0.89 | 2.36 |
| 11-18 16:54 | +15 | DOGE | UP | 0.62 | 0.82 | 1.72 |
| 11-18 16:54 | +10 | DOGE | UP | 0.62 | 0.73 | 0.79 |
| 11-18 16:54 | +5 | DOGE | UP | 0.62 | 0.67 | 0.17 |
| 11-18 16:54 | +10 stop | BNB | UP | 0.60 | 0.44 | -1.95 |
| 11-18 16:54 | +15 | BNB | UP | 0.61 | 0.76 | 1.20 |
| 11-18 16:54 | +10 | BNB | UP | 0.61 | 0.74 | 0.99 |
| 11-18 16:54 | +5 | BNB | UP | 0.61 | 0.68 | 0.37 |
| 11-18 16:54 | +10 stop | XRP | DOWN | 0.71 | 0.46 | -2.83 |
| 11-18 16:54 | +10 stop | HYPE | UP | 0.49 | 0.19 | -3.29 |
| 11-18 16:54 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
