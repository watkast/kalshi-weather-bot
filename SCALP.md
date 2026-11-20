# Range-Scalp Bot

*Updated Fri Nov 20 22:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66587 | 58116 | 8471 (128) | 4 | $-17886.31 | -4.3% |
| **+10¢** | 49725 | 39821 | 9904 (170) | 4 | $-16638.33 | -5.3% |
| **+15¢** | 41701 | 31024 | 10677 (217) | 4 | $-14932.87 | -5.7% |
| **+20¢** | 37125 | 25913 | 11212 (273) | 5 | $-13197.43 | -5.7% |
| **+10¢ (15¢ stop)** | 81091 | 80925 | 166 (100) | 0 | $-29952.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 22:10 | +10 stop | ETH | UP | 0.68 | 0.84 | 1.34 |
| 11-20 22:09 | +10 stop | BTC | UP | 0.69 | 0.87 | 1.57 |
| 11-20 22:08 | +10 stop | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 11-20 22:08 | +10 | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 11-20 22:08 | +5 | ZEC | UP | 0.63 | 0.71 | 0.48 |
| 11-20 22:08 | +10 stop | XRP | UP | 0.59 | 0.71 | 0.88 |
| 11-20 22:07 | +10 stop | HYPE | UP | 0.66 | 0.81 | 1.23 |
| 11-20 22:07 | +10 stop | BNB | UP | 0.59 | 0.76 | 1.44 |
| 11-20 22:07 | +5 | ZEC | UP | 0.54 | 0.61 | 0.35 |
| 11-20 22:06 | +5 | HYPE | DOWN | 0.55 | open |  |
| 11-20 22:06 | +10 stop | HYPE | DOWN | 0.66 | 0.50 | -1.94 |
| 11-20 22:05 | +10 stop | HYPE | UP | 0.57 | 0.42 | -1.86 |
| 11-20 22:04 | +10 stop | BTC | UP | 0.71 | 0.54 | -2.03 |
| 11-20 22:04 | +10 | BTC | UP | 0.71 | 0.87 | 1.37 |
| 11-20 22:04 | +5 | BTC | UP | 0.71 | 0.87 | 1.37 |
| 11-20 22:04 | +10 stop | HYPE | UP | 0.52 | 0.63 | 0.75 |
| 11-20 22:03 | +10 stop | XRP | UP | 0.65 | 0.50 | -1.84 |
| 11-20 22:03 | +20 | XRP | UP | 0.65 | open |  |
| 11-20 22:03 | +15 | XRP | UP | 0.65 | 0.83 | 1.54 |
| 11-20 22:03 | +10 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-20 22:03 | +5 | XRP | UP | 0.65 | 0.71 | 0.29 |
| 11-20 22:03 | +10 stop | SOL | UP | 0.54 | 0.70 | 1.27 |
| 11-20 22:03 | +10 stop | ETH | UP | 0.63 | 0.47 | -1.95 |
| 11-20 22:03 | +10 stop | BNB | UP | 0.63 | 0.47 | -1.95 |
| 11-20 22:03 | +10 stop | ZEC | UP | 0.52 | 0.64 | 0.85 |
| 11-20 22:03 | +20 | ZEC | UP | 0.53 | 0.73 | 1.71 |
| 11-20 22:03 | +15 | ZEC | UP | 0.52 | 0.71 | 1.57 |
| 11-20 22:03 | +10 | ZEC | UP | 0.52 | 0.64 | 0.85 |
| 11-20 22:03 | +5 | ZEC | UP | 0.52 | 0.57 | 0.14 |
| 11-20 22:03 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-20 22:03 | +20 | BTC | UP | 0.64 | 0.87 | 2.05 |
| 11-20 22:03 | +15 | BTC | UP | 0.64 | 0.87 | 2.05 |
| 11-20 22:03 | +10 | BTC | UP | 0.63 | 0.73 | 0.69 |
| 11-20 22:03 | +5 | BTC | UP | 0.63 | 0.73 | 0.69 |
| 11-20 22:02 | +10 stop | SOL | DOWN | 0.60 | 0.42 | -2.15 |
| 11-20 22:02 | +20 | SOL | DOWN | 0.60 | open |  |
| 11-20 22:02 | +15 | SOL | DOWN | 0.59 | open |  |
| 11-20 22:02 | +10 | SOL | DOWN | 0.59 | open |  |
| 11-20 22:02 | +5 | SOL | DOWN | 0.59 | open |  |
| 11-20 22:02 | +10 stop | ETH | DOWN | 0.59 | 0.41 | -2.14 |
