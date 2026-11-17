# Range-Scalp Bot

*Updated Tue Nov 17 15:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62958 | 54913 | 8045 (117) | 0 | $-17178.66 | -4.3% |
| **+10¢** | 47024 | 37611 | 9413 (159) | 0 | $-16053.92 | -5.4% |
| **+15¢** | 39414 | 29264 | 10150 (201) | 1 | $-14577.24 | -5.9% |
| **+20¢** | 35125 | 24482 | 10643 (256) | 1 | $-12746.54 | -5.8% |
| **+10¢ (15¢ stop)** | 76606 | 76450 | 156 (92) | 0 | $-28220.39 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 15:47 | +5 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-17 15:46 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 11-17 15:46 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 11-17 15:46 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 11-17 15:46 | +20 | XRP | DOWN | 0.68 | 0.88 | 1.76 |
| 11-17 15:46 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-17 15:46 | +10 | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-17 15:46 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 11-17 15:46 | +10 stop | HYPE | DOWN | 0.70 | 0.84 | 1.18 |
| 11-17 15:46 | +20 | HYPE | DOWN | 0.68 | 0.91 | 2.05 |
| 11-17 15:46 | +15 | HYPE | DOWN | 0.68 | 0.84 | 1.34 |
| 11-17 15:46 | +10 | HYPE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-17 15:46 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.20 |
| 11-17 15:46 | +10 stop | ZEC | UP | 0.48 | 0.27 | -2.41 |
| 11-17 15:46 | +20 | ZEC | UP | 0.46 | open |  |
| 11-17 15:46 | +15 | ZEC | UP | 0.46 | open |  |
| 11-17 15:46 | +10 | ZEC | UP | 0.46 | 0.56 | 0.64 |
| 11-17 15:46 | +5 | ZEC | UP | 0.46 | 0.54 | 0.44 |
| 11-17 15:46 | +10 stop | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-17 15:46 | +20 | DOGE | DOWN | 0.69 | 0.90 | 1.84 |
| 11-17 15:46 | +15 | DOGE | DOWN | 0.67 | 0.87 | 1.78 |
| 11-17 15:46 | +10 | DOGE | DOWN | 0.67 | 0.81 | 1.15 |
| 11-17 15:46 | +5 | DOGE | DOWN | 0.67 | 0.75 | 0.52 |
| 11-17 15:46 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-17 15:46 | +20 | BTC | DOWN | 0.59 | 0.80 | 1.81 |
| 11-17 15:46 | +15 | BTC | DOWN | 0.59 | 0.75 | 1.29 |
| 11-17 15:46 | +10 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-17 15:46 | +5 | BTC | DOWN | 0.58 | 0.65 | 0.36 |
| 11-17 15:46 | +10 stop | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 11-17 15:46 | +20 | ETH | DOWN | 0.64 | 0.88 | 2.15 |
| 11-17 15:46 | +15 | ETH | DOWN | 0.63 | 0.81 | 1.52 |
| 11-17 15:46 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 11-17 15:46 | +5 | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 11-17 15:31 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 11-17 15:31 | +10 stop | BNB | DOWN | 0.71 | 0.85 | 1.16 |
| 11-17 15:31 | +20 | BNB | DOWN | 0.71 | 0.94 | 2.05 |
| 11-17 15:31 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-17 15:31 | +10 | BNB | DOWN | 0.71 | 0.85 | 1.16 |
| 11-17 15:31 | +10 stop | HYPE | DOWN | 0.70 | 0.88 | 1.58 |
| 11-17 15:31 | +20 | HYPE | DOWN | 0.68 | 0.88 | 1.76 |
