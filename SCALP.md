# Range-Scalp Bot

*Updated Wed Nov 25 03:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71343 | 62270 | 9073 (156) | 0 | $-19015.82 | -4.2% |
| **+10¢** | 53216 | 42617 | 10599 (202) | 0 | $-17634.07 | -5.3% |
| **+15¢** | 44569 | 33159 | 11410 (259) | 0 | $-15675.54 | -5.6% |
| **+20¢** | 39681 | 27665 | 12016 (325) | 0 | $-14083.43 | -5.7% |
| **+10¢ (15¢ stop)** | 86860 | 86657 | 203 (123) | 0 | $-31923.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 03:28 | +10 stop | ETH | UP | 0.47 | 0.60 | 0.95 |
| 11-25 03:28 | +20 | ETH | UP | 0.47 | no | -4.88 |
| 11-25 03:28 | +15 | ETH | UP | 0.48 | no | -4.98 |
| 11-25 03:28 | +10 | ETH | UP | 0.50 | 0.60 | 0.65 |
| 11-25 03:28 | +5 | ETH | UP | 0.42 | 0.60 | 1.45 |
| 11-25 03:28 | +10 stop | SOL | DOWN | 0.67 | 0.89 | 1.97 |
| 11-25 03:28 | +20 | SOL | DOWN | 0.67 | 0.89 | 1.97 |
| 11-25 03:28 | +15 | SOL | DOWN | 0.67 | 0.89 | 1.97 |
| 11-25 03:28 | +10 | SOL | DOWN | 0.67 | 0.89 | 1.97 |
| 11-25 03:28 | +5 | SOL | DOWN | 0.67 | 0.89 | 1.97 |
| 11-25 03:27 | +10 | ETH | DOWN | 0.58 | 0.76 | 1.49 |
| 11-25 03:27 | +10 stop | XRP | DOWN | 0.46 | 0.59 | 0.95 |
| 11-25 03:27 | +10 stop | ETH | DOWN | 0.58 | 0.76 | 1.49 |
| 11-25 03:27 | +5 | ETH | DOWN | 0.61 | 0.66 | 0.17 |
| 11-25 03:27 | +10 stop | DOGE | DOWN | 0.64 | 0.23 | -4.40 |
| 11-25 03:27 | +20 | DOGE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-25 03:27 | +15 | DOGE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-25 03:27 | +10 | DOGE | DOWN | 0.66 | 0.85 | 1.65 |
| 11-25 03:27 | +5 | DOGE | DOWN | 0.64 | 0.85 | 1.84 |
| 11-25 03:26 | +10 stop | ETH | UP | 0.33 | 0.54 | 1.76 |
| 11-25 03:26 | +5 | ETH | UP | 0.32 | 0.54 | 1.86 |
| 11-25 03:26 | +10 stop | BNB | UP | 0.61 | 0.72 | 0.78 |
| 11-25 03:26 | +20 | BNB | UP | 0.62 | no | -6.37 |
| 11-25 03:26 | +15 | BNB | UP | 0.64 | no | -6.57 |
| 11-25 03:26 | +10 | BNB | UP | 0.62 | 0.72 | 0.68 |
| 11-25 03:26 | +5 | BNB | UP | 0.62 | 0.72 | 0.68 |
| 11-25 03:25 | +10 stop | BTC | UP | 0.66 | 0.51 | -1.84 |
| 11-25 03:23 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 11-25 03:23 | +10 stop | HYPE | UP | 0.64 | 0.31 | -3.65 |
| 11-25 03:23 | +10 | HYPE | UP | 0.64 | no | -6.60 |
| 11-25 03:23 | +10 stop | ETH | UP | 0.71 | 0.56 | -1.83 |
| 11-25 03:23 | +5 | ETH | UP | 0.71 | 0.78 | 0.42 |
| 11-25 03:22 | +10 stop | NEAR | UP | 0.65 | 0.40 | -2.83 |
| 11-25 03:22 | +20 | NEAR | UP | 0.64 | no | -6.57 |
| 11-25 03:22 | +15 | NEAR | UP | 0.64 | no | -6.57 |
| 11-25 03:22 | +10 | NEAR | UP | 0.64 | no | -6.57 |
| 11-25 03:22 | +5 | NEAR | UP | 0.64 | no | -6.57 |
| 11-25 03:21 | +5 | ZEC | UP | 0.54 | 0.60 | 0.25 |
| 11-25 03:20 | +10 stop | ZEC | UP | 0.66 | 0.35 | -3.37 |
| 11-25 03:20 | +20 | ZEC | UP | 0.65 | no | -6.66 |
