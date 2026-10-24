# Range-Scalp Bot

*Updated Sat Oct 24 23:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32213 | 28086 | 4127 (40) | 0 | $-9206.13 | -4.5% |
| **+10¢** | 24113 | 19335 | 4778 (58) | 2 | $-8233.98 | -5.4% |
| **+15¢** | 20192 | 15053 | 5139 (81) | 2 | $-7371.92 | -5.8% |
| **+20¢** | 17888 | 12509 | 5379 (103) | 2 | $-6536.21 | -5.8% |
| **+10¢ (15¢ stop)** | 39585 | 39526 | 59 (32) | 2 | $-15132.52 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 23:17 | +10 stop | XRP | DOWN | 0.69 | open |  |
| 10-24 23:17 | +20 | XRP | DOWN | 0.69 | open |  |
| 10-24 23:17 | +15 | XRP | DOWN | 0.69 | open |  |
| 10-24 23:17 | +10 | XRP | DOWN | 0.69 | open |  |
| 10-24 23:17 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 10-24 23:17 | +10 stop | HYPE | DOWN | 0.69 | open |  |
| 10-24 23:17 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-24 23:17 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-24 23:17 | +10 | HYPE | DOWN | 0.69 | open |  |
| 10-24 23:17 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.38 |
| 10-24 23:16 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-24 23:16 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 10-24 23:16 | +15 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-24 23:16 | +10 | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-24 23:16 | +5 | BTC | DOWN | 0.68 | 0.76 | 0.51 |
| 10-24 23:15 | +10 stop | ZEC | DOWN | 0.70 | 0.95 | 2.32 |
| 10-24 23:15 | +20 | ZEC | DOWN | 0.70 | 0.95 | 2.32 |
| 10-24 23:15 | +15 | ZEC | DOWN | 0.70 | 0.95 | 2.32 |
| 10-24 23:15 | +10 | ZEC | DOWN | 0.70 | 0.95 | 2.32 |
| 10-24 23:15 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-24 23:12 | +10 stop | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 23:12 | +20 | ZEC | DOWN | 0.64 | 0.92 | 2.52 |
| 10-24 23:12 | +15 | ZEC | DOWN | 0.64 | 0.92 | 2.52 |
| 10-24 23:12 | +10 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 23:12 | +5 | ZEC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-24 23:12 | +10 stop | ETH | DOWN | 0.55 | 0.73 | 1.48 |
| 10-24 23:12 | +5 | ETH | DOWN | 0.55 | 0.73 | 1.48 |
| 10-24 23:11 | +10 stop | BTC | UP | 0.58 | 0.77 | 1.59 |
| 10-24 23:11 | +20 | BTC | UP | 0.58 | 0.78 | 1.69 |
| 10-24 23:11 | +15 | BTC | UP | 0.58 | 0.77 | 1.59 |
| 10-24 23:11 | +10 | BTC | UP | 0.59 | 0.77 | 1.50 |
| 10-24 23:11 | +5 | BTC | UP | 0.59 | 0.77 | 1.50 |
| 10-24 23:11 | +10 stop | ETH | DOWN | 0.68 | 0.48 | -2.34 |
| 10-24 23:10 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 10-24 23:10 | +10 stop | SOL | UP | 0.53 | 0.82 | 2.61 |
| 10-24 23:10 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 10-24 23:10 | +10 stop | BNB | UP | 0.59 | 0.69 | 0.68 |
| 10-24 23:09 | +10 stop | BNB | DOWN | 0.34 | 0.55 | 1.76 |
| 10-24 23:09 | +10 stop | XRP | DOWN | 0.48 | 0.60 | 0.85 |
| 10-24 23:09 | +15 | XRP | DOWN | 0.48 | 0.91 | 4.00 |
