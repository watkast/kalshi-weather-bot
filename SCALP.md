# Range-Scalp Bot

*Updated Tue Nov 03 13:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46000 | 40054 | 5946 (69) | 5 | $-13272.58 | -4.6% |
| **+10¢** | 34339 | 27451 | 6888 (91) | 7 | $-12133.85 | -5.6% |
| **+15¢** | 28737 | 21331 | 7406 (119) | 8 | $-11086.23 | -6.1% |
| **+20¢** | 25523 | 17761 | 7762 (156) | 8 | $-9854.14 | -6.2% |
| **+10¢ (15¢ stop)** | 56106 | 56017 | 89 (53) | 3 | $-21033.62 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 13:20 | +10 stop | DOGE | UP | 0.57 | 0.41 | -1.95 |
| 11-03 13:20 | +20 | DOGE | UP | 0.57 | open |  |
| 11-03 13:20 | +15 | DOGE | UP | 0.57 | open |  |
| 11-03 13:20 | +10 | DOGE | UP | 0.56 | open |  |
| 11-03 13:20 | +5 | DOGE | UP | 0.56 | 0.62 | 0.25 |
| 11-03 13:19 | +5 | NEAR | UP | 0.66 | open |  |
| 11-03 13:19 | +5 | ETH | UP | 0.68 | open |  |
| 11-03 13:19 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 11-03 13:19 | +10 stop | BNB | UP | 0.71 | 0.54 | -2.03 |
| 11-03 13:19 | +5 | BNB | UP | 0.71 | open |  |
| 11-03 13:19 | +10 | HYPE | DOWN | 0.68 | 0.82 | 1.13 |
| 11-03 13:19 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-03 13:19 | +10 stop | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-03 13:19 | +10 stop | ZEC | DOWN | 0.66 | open |  |
| 11-03 13:19 | +5 | NEAR | UP | 0.60 | 0.66 | 0.27 |
| 11-03 13:17 | +10 stop | BTC | UP | 0.70 | open |  |
| 11-03 13:17 | +20 | BTC | UP | 0.70 | open |  |
| 11-03 13:17 | +15 | BTC | UP | 0.70 | open |  |
| 11-03 13:17 | +10 | BTC | UP | 0.70 | open |  |
| 11-03 13:17 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 11-03 13:16 | +10 stop | HYPE | DOWN | 0.55 | 0.67 | 0.82 |
| 11-03 13:16 | +20 | HYPE | DOWN | 0.55 | 0.82 | 2.37 |
| 11-03 13:16 | +15 | HYPE | DOWN | 0.55 | 0.73 | 1.44 |
| 11-03 13:16 | +10 | HYPE | DOWN | 0.55 | 0.67 | 0.82 |
| 11-03 13:16 | +5 | HYPE | DOWN | 0.55 | 0.67 | 0.82 |
| 11-03 13:16 | +10 stop | ETH | UP | 0.64 | open |  |
| 11-03 13:16 | +20 | ETH | UP | 0.64 | open |  |
| 11-03 13:16 | +15 | ETH | UP | 0.64 | open |  |
| 11-03 13:16 | +10 | ETH | UP | 0.64 | open |  |
| 11-03 13:16 | +5 | ETH | UP | 0.64 | 0.72 | 0.48 |
| 11-03 13:16 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 11-03 13:16 | +20 | BNB | UP | 0.66 | open |  |
| 11-03 13:16 | +15 | BNB | UP | 0.66 | open |  |
| 11-03 13:16 | +10 stop | XRP | UP | 0.66 | 0.77 | 0.81 |
| 11-03 13:16 | +20 | XRP | UP | 0.66 | open |  |
| 11-03 13:16 | +15 | XRP | UP | 0.67 | open |  |
| 11-03 13:16 | +10 | XRP | UP | 0.67 | 0.77 | 0.71 |
| 11-03 13:16 | +5 | XRP | UP | 0.67 | 0.75 | 0.50 |
| 11-03 13:16 | +10 stop | NEAR | UP | 0.71 | 0.45 | -2.93 |
| 11-03 13:16 | +20 | NEAR | UP | 0.71 | open |  |
