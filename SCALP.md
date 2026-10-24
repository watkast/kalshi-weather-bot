# Range-Scalp Bot

*Updated Sat Oct 24 04:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31405 | 27368 | 4037 (40) | 0 | $-9067.75 | -4.6% |
| **+10¢** | 23497 | 18836 | 4661 (58) | 0 | $-8042.22 | -5.4% |
| **+15¢** | 19669 | 14661 | 5008 (81) | 1 | $-7165.91 | -5.8% |
| **+20¢** | 17424 | 12179 | 5245 (103) | 1 | $-6385.40 | -5.8% |
| **+10¢ (15¢ stop)** | 38541 | 38482 | 59 (32) | 0 | $-14689.41 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 04:00 | +10 stop | SOL | UP | 0.70 | 0.84 | 1.15 |
| 10-24 04:00 | +20 | SOL | UP | 0.70 | open |  |
| 10-24 04:00 | +15 | SOL | UP | 0.70 | open |  |
| 10-24 04:00 | +10 | SOL | UP | 0.70 | 0.84 | 1.15 |
| 10-24 04:00 | +5 | SOL | UP | 0.70 | 0.78 | 0.52 |
| 10-24 03:55 | +5 | BNB | DOWN | 0.63 | 0.76 | 1.00 |
| 10-24 03:54 | +10 stop | BNB | DOWN | 0.62 | 0.76 | 1.10 |
| 10-24 03:54 | +20 | BNB | DOWN | 0.62 | 0.87 | 2.25 |
| 10-24 03:54 | +15 | BNB | DOWN | 0.62 | 0.81 | 1.62 |
| 10-24 03:54 | +10 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-24 03:54 | +5 | BNB | DOWN | 0.61 | 0.68 | 0.37 |
| 10-24 03:48 | +5 | BNB | DOWN | 0.70 | 0.79 | 0.63 |
| 10-24 03:48 | +5 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-24 03:47 | +10 stop | NEAR | UP | 0.60 | 0.36 | -2.74 |
| 10-24 03:46 | +10 stop | BTC | DOWN | 0.55 | 0.77 | 1.89 |
| 10-24 03:46 | +20 | BTC | DOWN | 0.55 | 0.77 | 1.89 |
| 10-24 03:46 | +15 | BTC | DOWN | 0.55 | 0.77 | 1.89 |
| 10-24 03:46 | +10 | BTC | DOWN | 0.55 | 0.77 | 1.89 |
| 10-24 03:46 | +5 | BTC | DOWN | 0.55 | 0.63 | 0.45 |
| 10-24 03:46 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.74 |
| 10-24 03:46 | +20 | ZEC | DOWN | 0.67 | 0.88 | 1.89 |
| 10-24 03:46 | +15 | ZEC | DOWN | 0.67 | 0.85 | 1.58 |
| 10-24 03:46 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.74 |
| 10-24 03:46 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.22 |
| 10-24 03:46 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 10-24 03:46 | +20 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-24 03:46 | +15 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 10-24 03:46 | +10 | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 10-24 03:46 | +5 | SOL | DOWN | 0.68 | 0.75 | 0.40 |
| 10-24 03:46 | +10 stop | NEAR | DOWN | 0.59 | 0.40 | -2.24 |
| 10-24 03:46 | +20 | NEAR | DOWN | 0.59 | 0.83 | 2.13 |
| 10-24 03:46 | +15 | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 10-24 03:46 | +10 | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
| 10-24 03:46 | +5 | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
| 10-24 03:46 | +10 stop | DOGE | DOWN | 0.63 | 0.82 | 1.62 |
| 10-24 03:46 | +20 | DOGE | DOWN | 0.63 | 0.89 | 2.36 |
| 10-24 03:46 | +15 | DOGE | DOWN | 0.63 | 0.82 | 1.62 |
| 10-24 03:46 | +10 | DOGE | DOWN | 0.63 | 0.82 | 1.62 |
| 10-24 03:46 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 10-24 03:46 | +10 stop | BNB | DOWN | 0.61 | 0.74 | 0.99 |
