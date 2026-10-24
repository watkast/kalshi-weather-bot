# Range-Scalp Bot

*Updated Sat Oct 24 03:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31402 | 27365 | 4037 (40) | 0 | $-9069.64 | -4.6% |
| **+10¢** | 23495 | 18834 | 4661 (58) | 0 | $-8044.57 | -5.4% |
| **+15¢** | 19668 | 14660 | 5008 (81) | 0 | $-7167.53 | -5.8% |
| **+20¢** | 17423 | 12178 | 5245 (103) | 0 | $-6387.65 | -5.8% |
| **+10¢ (15¢ stop)** | 38539 | 38480 | 59 (32) | 0 | $-14691.66 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
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
| 10-24 03:46 | +20 | BNB | DOWN | 0.61 | 0.82 | 1.82 |
| 10-24 03:46 | +15 | BNB | DOWN | 0.61 | 0.79 | 1.51 |
| 10-24 03:46 | +10 | BNB | DOWN | 0.61 | 0.74 | 0.99 |
| 10-24 03:46 | +5 | BNB | DOWN | 0.61 | 0.68 | 0.37 |
| 10-24 03:46 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-24 03:46 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 10-24 03:46 | +15 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 10-24 03:46 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-24 03:46 | +5 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-24 03:46 | +10 stop | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-24 03:46 | +20 | XRP | DOWN | 0.62 | 0.84 | 1.93 |
