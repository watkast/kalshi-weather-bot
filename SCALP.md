# Range-Scalp Bot

*Updated Thu Oct 22 05:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28383 | 24732 | 3651 (39) | 1 | $-8165.06 | -4.6% |
| **+10¢** | 21299 | 17074 | 4225 (55) | 0 | $-7268.80 | -5.4% |
| **+15¢** | 17843 | 13298 | 4545 (78) | 0 | $-6495.14 | -5.8% |
| **+20¢** | 15785 | 11019 | 4766 (98) | 1 | $-5870.70 | -5.9% |
| **+10¢ (15¢ stop)** | 34814 | 34755 | 59 (32) | 0 | $-13058.52 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 05:53 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-22 05:53 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-22 05:53 | +5 | ZEC | DOWN | 0.54 | 0.67 | 0.96 |
| 10-22 05:52 | +5 | ZEC | DOWN | 0.51 | 0.62 | 0.75 |
| 10-22 05:51 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-22 05:51 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-22 05:50 | +10 | NEAR | DOWN | 0.70 | 0.84 | 1.15 |
| 10-22 05:50 | +10 stop | ZEC | DOWN | 0.56 | 0.67 | 0.76 |
| 10-22 05:50 | +15 | ZEC | DOWN | 0.56 | 0.72 | 1.27 |
| 10-22 05:50 | +10 | ZEC | DOWN | 0.57 | 0.68 | 0.74 |
| 10-22 05:50 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-22 05:50 | +5 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 10-22 05:50 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.44 |
| 10-22 05:50 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-22 05:49 | +5 | BNB | UP | 0.49 | 0.55 | 0.24 |
| 10-22 05:49 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-22 05:49 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-22 05:49 | +5 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-22 05:48 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-22 05:48 | +5 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-22 05:48 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-22 05:48 | +5 | ZEC | UP | 0.59 | 0.70 | 0.78 |
| 10-22 05:48 | +10 stop | NEAR | UP | 0.57 | 0.41 | -1.95 |
| 10-22 05:48 | +5 | BTC | UP | 0.50 | open |  |
| 10-22 05:47 | +5 | SOL | DOWN | 0.53 | 0.59 | 0.25 |
| 10-22 05:47 | +5 | ETH | DOWN | 0.52 | 0.58 | 0.24 |
| 10-22 05:47 | +10 stop | DOGE | DOWN | 0.52 | 0.63 | 0.75 |
| 10-22 05:47 | +5 | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 10-22 05:46 | +10 stop | ZEC | UP | 0.50 | 0.70 | 1.65 |
| 10-22 05:46 | +20 | ZEC | UP | 0.50 | open |  |
| 10-22 05:46 | +15 | ZEC | UP | 0.50 | 0.70 | 1.67 |
| 10-22 05:46 | +10 | ZEC | UP | 0.50 | 0.70 | 1.67 |
| 10-22 05:46 | +5 | ZEC | UP | 0.50 | 0.56 | 0.24 |
| 10-22 05:46 | +10 stop | SOL | DOWN | 0.55 | 0.67 | 0.86 |
| 10-22 05:46 | +20 | SOL | DOWN | 0.55 | 0.76 | 1.79 |
| 10-22 05:46 | +15 | SOL | DOWN | 0.55 | 0.71 | 1.27 |
| 10-22 05:46 | +10 | SOL | DOWN | 0.55 | 0.67 | 0.86 |
| 10-22 05:46 | +5 | SOL | DOWN | 0.55 | 0.60 | 0.15 |
| 10-22 05:46 | +10 stop | NEAR | DOWN | 0.54 | 0.37 | -2.05 |
| 10-22 05:46 | +20 | NEAR | DOWN | 0.54 | 0.77 | 1.99 |
