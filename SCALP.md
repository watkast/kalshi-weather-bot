# Range-Scalp Bot

*Updated Tue Nov 03 21:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46382 | 40385 | 5997 (72) | 1 | $-13358.52 | -4.6% |
| **+10¢** | 34627 | 27679 | 6948 (96) | 1 | $-12211.66 | -5.6% |
| **+15¢** | 28987 | 21516 | 7471 (124) | 1 | $-11147.01 | -6.1% |
| **+20¢** | 25752 | 17922 | 7830 (164) | 1 | $-9857.51 | -6.1% |
| **+10¢ (15¢ stop)** | 56573 | 56480 | 93 (56) | 0 | $-21217.05 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 21:47 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-03 21:47 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-03 21:47 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-03 21:47 | +10 stop | BNB | DOWN | 0.59 | 0.74 | 1.19 |
| 11-03 21:46 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-03 21:46 | +20 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 11-03 21:46 | +15 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 11-03 21:46 | +10 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-03 21:46 | +5 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-03 21:46 | +10 stop | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 11-03 21:46 | +20 | DOGE | DOWN | 0.53 | 0.74 | 1.78 |
| 11-03 21:46 | +15 | DOGE | DOWN | 0.53 | 0.70 | 1.37 |
| 11-03 21:46 | +10 | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 11-03 21:46 | +5 | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 11-03 21:46 | +10 stop | BTC | DOWN | 0.57 | 0.68 | 0.76 |
| 11-03 21:46 | +20 | BTC | DOWN | 0.57 | 0.77 | 1.69 |
| 11-03 21:46 | +15 | BTC | DOWN | 0.57 | 0.76 | 1.59 |
| 11-03 21:46 | +10 | BTC | DOWN | 0.57 | 0.68 | 0.76 |
| 11-03 21:46 | +5 | BTC | DOWN | 0.57 | 0.65 | 0.46 |
| 11-03 21:46 | +10 stop | ETH | DOWN | 0.60 | 0.72 | 0.88 |
| 11-03 21:46 | +20 | ETH | DOWN | 0.59 | 0.83 | 2.13 |
| 11-03 21:46 | +15 | ETH | DOWN | 0.59 | 0.76 | 1.40 |
| 11-03 21:46 | +10 | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 11-03 21:46 | +5 | ETH | DOWN | 0.59 | 0.65 | 0.27 |
| 11-03 21:46 | +10 stop | BNB | UP | 0.58 | 0.43 | -1.90 |
| 11-03 21:46 | +20 | BNB | UP | 0.58 | open |  |
| 11-03 21:46 | +15 | BNB | UP | 0.58 | open |  |
| 11-03 21:46 | +10 | BNB | UP | 0.58 | open |  |
| 11-03 21:46 | +5 | BNB | UP | 0.58 | open |  |
| 11-03 21:46 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 11-03 21:46 | +20 | SOL | DOWN | 0.65 | 0.89 | 2.17 |
| 11-03 21:46 | +15 | SOL | DOWN | 0.65 | 0.81 | 1.33 |
| 11-03 21:46 | +10 | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 11-03 21:46 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 11-03 21:45 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.82 |
| 11-03 21:45 | +20 | ZEC | DOWN | 0.65 | 0.86 | 1.86 |
| 11-03 21:45 | +15 | ZEC | DOWN | 0.65 | 0.81 | 1.34 |
| 11-03 21:45 | +10 | ZEC | DOWN | 0.65 | 0.76 | 0.82 |
| 11-03 21:45 | +5 | ZEC | DOWN | 0.65 | 0.76 | 0.82 |
| 11-03 21:43 | +10 stop | HYPE | DOWN | 0.66 | 0.03 | -6.45 |
