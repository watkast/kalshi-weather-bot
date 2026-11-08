# Range-Scalp Bot

*Updated Sun Nov 08 12:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52457 | 45733 | 6724 (83) | 2 | $-14549.41 | -4.4% |
| **+10¢** | 39156 | 31321 | 7835 (108) | 2 | $-13530.74 | -5.5% |
| **+15¢** | 32801 | 24357 | 8444 (138) | 2 | $-12396.73 | -6.0% |
| **+20¢** | 29174 | 20325 | 8849 (182) | 3 | $-10905.85 | -6.0% |
| **+10¢ (15¢ stop)** | 63875 | 63769 | 106 (63) | 0 | $-23646.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 12:12 | +10 stop | HYPE | DOWN | 0.70 | 0.84 | 1.18 |
| 11-08 12:12 | +20 | HYPE | DOWN | 0.70 | 0.91 | 1.89 |
| 11-08 12:12 | +15 | HYPE | DOWN | 0.70 | 0.91 | 1.89 |
| 11-08 12:12 | +10 | HYPE | DOWN | 0.70 | 0.84 | 1.18 |
| 11-08 12:11 | +10 stop | BNB | DOWN | 0.65 | 0.85 | 1.75 |
| 11-08 12:11 | +15 | BNB | DOWN | 0.66 | 0.85 | 1.68 |
| 11-08 12:11 | +10 | BNB | DOWN | 0.66 | 0.85 | 1.70 |
| 11-08 12:11 | +5 | BNB | DOWN | 0.66 | 0.85 | 1.70 |
| 11-08 12:10 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-08 12:10 | +20 | BTC | DOWN | 0.64 | 0.88 | 2.15 |
| 11-08 12:10 | +15 | BTC | DOWN | 0.65 | 0.88 | 2.06 |
| 11-08 12:10 | +10 | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-08 12:10 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-08 12:10 | +10 stop | NEAR | DOWN | 0.67 | 0.83 | 1.33 |
| 11-08 12:10 | +15 | NEAR | DOWN | 0.67 | 0.83 | 1.33 |
| 11-08 12:10 | +10 | NEAR | DOWN | 0.67 | 0.83 | 1.33 |
| 11-08 12:10 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.29 |
| 11-08 12:08 | +10 stop | ZEC | UP | 0.68 | 0.50 | -2.12 |
| 11-08 12:07 | +10 stop | XRP | UP | 0.71 | 0.87 | 1.37 |
| 11-08 12:07 | +10 | XRP | UP | 0.71 | 0.87 | 1.37 |
| 11-08 12:06 | +10 stop | HYPE | DOWN | 0.57 | 0.42 | -1.86 |
| 11-08 12:06 | +5 | HYPE | DOWN | 0.57 | 0.64 | 0.35 |
| 11-08 12:06 | +10 stop | NEAR | DOWN | 0.59 | 0.42 | -2.05 |
| 11-08 12:05 | +10 stop | ZEC | DOWN | 0.61 | 0.42 | -2.25 |
| 11-08 12:04 | +10 stop | NEAR | DOWN | 0.55 | 0.65 | 0.66 |
| 11-08 12:04 | +5 | SOL | UP | 0.66 | 0.72 | 0.29 |
| 11-08 12:04 | +10 stop | BTC | UP | 0.68 | 0.79 | 0.82 |
| 11-08 12:04 | +10 | BTC | UP | 0.68 | 0.79 | 0.82 |
| 11-08 12:04 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 11-08 12:04 | +10 stop | HYPE | UP | 0.61 | 0.40 | -2.44 |
| 11-08 12:03 | +10 stop | NEAR | UP | 0.55 | 0.39 | -1.95 |
| 11-08 12:03 | +10 | NEAR | UP | 0.55 | 0.73 | 1.48 |
| 11-08 12:03 | +5 | NEAR | UP | 0.55 | 0.73 | 1.48 |
| 11-08 12:03 | +10 stop | SOL | UP | 0.70 | 0.92 | 1.95 |
| 11-08 12:03 | +10 stop | ZEC | UP | 0.67 | 0.47 | -2.34 |
| 11-08 12:03 | +10 | ZEC | UP | 0.68 | open |  |
| 11-08 12:03 | +5 | ZEC | UP | 0.68 | open |  |
| 11-08 12:03 | +5 | XRP | UP | 0.66 | 0.73 | 0.40 |
| 11-08 12:03 | +5 | SOL | UP | 0.68 | 0.77 | 0.61 |
| 11-08 12:02 | +10 stop | HYPE | DOWN | 0.54 | 0.37 | -2.05 |
