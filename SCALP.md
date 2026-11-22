# Range-Scalp Bot

*Updated Sun Nov 22 01:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68100 | 59435 | 8665 (138) | 2 | $-18255.21 | -4.3% |
| **+10¢** | 50846 | 40726 | 10120 (181) | 2 | $-16905.46 | -5.3% |
| **+15¢** | 42625 | 31714 | 10911 (230) | 2 | $-15167.40 | -5.7% |
| **+20¢** | 37945 | 26477 | 11468 (288) | 2 | $-13495.45 | -5.7% |
| **+10¢ (15¢ stop)** | 82902 | 82724 | 178 (110) | 0 | $-30424.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 01:55 | +10 stop | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 11-22 01:53 | +10 stop | NEAR | DOWN | 0.60 | 0.86 | 2.34 |
| 11-22 01:53 | +15 | NEAR | DOWN | 0.60 | 0.86 | 2.34 |
| 11-22 01:53 | +10 | NEAR | DOWN | 0.61 | 0.86 | 2.24 |
| 11-22 01:53 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 11-22 01:51 | +10 stop | ZEC | UP | 0.62 | 0.38 | -2.74 |
| 11-22 01:51 | +15 | ZEC | UP | 0.62 | open |  |
| 11-22 01:51 | +10 | ZEC | UP | 0.62 | open |  |
| 11-22 01:51 | +5 | ZEC | UP | 0.62 | open |  |
| 11-22 01:50 | +10 stop | HYPE | DOWN | 0.55 | 0.70 | 1.16 |
| 11-22 01:50 | +10 stop | NEAR | UP | 0.57 | 0.32 | -2.84 |
| 11-22 01:48 | +10 stop | HYPE | UP | 0.60 | 0.41 | -2.24 |
| 11-22 01:47 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-22 01:47 | +20 | XRP | UP | 0.70 | 0.91 | 1.89 |
| 11-22 01:47 | +15 | XRP | UP | 0.70 | 0.85 | 1.26 |
| 11-22 01:47 | +10 | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-22 01:47 | +5 | XRP | UP | 0.69 | 0.74 | 0.21 |
| 11-22 01:47 | +10 stop | BTC | UP | 0.68 | 0.79 | 0.82 |
| 11-22 01:47 | +20 | BTC | UP | 0.68 | 0.91 | 2.02 |
| 11-22 01:47 | +15 | BTC | UP | 0.68 | 0.86 | 1.55 |
| 11-22 01:47 | +10 | BTC | UP | 0.68 | 0.79 | 0.82 |
| 11-22 01:47 | +5 | BTC | UP | 0.68 | 0.79 | 0.82 |
| 11-22 01:47 | +10 stop | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 11-22 01:47 | +5 | ZEC | UP | 0.71 | 0.79 | 0.53 |
| 11-22 01:47 | +10 stop | NEAR | DOWN | 0.67 | 0.47 | -2.34 |
| 11-22 01:47 | +20 | NEAR | DOWN | 0.67 | 0.89 | 1.97 |
| 11-22 01:47 | +15 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 11-22 01:47 | +10 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 11-22 01:47 | +5 | NEAR | DOWN | 0.68 | 0.82 | 1.13 |
| 11-22 01:46 | +10 stop | HYPE | DOWN | 0.61 | 0.45 | -1.95 |
| 11-22 01:45 | +10 stop | HYPE | UP | 0.61 | 0.45 | -1.98 |
| 11-22 01:45 | +20 | HYPE | UP | 0.64 | open |  |
| 11-22 01:45 | +15 | HYPE | UP | 0.59 | open |  |
| 11-22 01:45 | +10 | HYPE | UP | 0.59 | open |  |
| 11-22 01:45 | +5 | HYPE | UP | 0.59 | open |  |
| 11-22 01:45 | +20 | ZEC | UP | 0.71 | open |  |
| 11-22 01:45 | +15 | ZEC | UP | 0.71 | 0.88 | 1.47 |
| 11-22 01:45 | +10 | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 11-22 01:45 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 11-22 01:45 | +10 stop | ETH | UP | 0.66 | 0.80 | 1.12 |
