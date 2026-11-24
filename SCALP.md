# Range-Scalp Bot

*Updated Tue Nov 24 09:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70762 | 61765 | 8997 (148) | 4 | $-18914.63 | -4.2% |
| **+10¢** | 52786 | 42280 | 10506 (193) | 4 | $-17512.64 | -5.3% |
| **+15¢** | 44216 | 32900 | 11316 (250) | 7 | $-15596.13 | -5.6% |
| **+20¢** | 39371 | 27457 | 11914 (316) | 7 | $-13967.27 | -5.7% |
| **+10¢ (15¢ stop)** | 86158 | 85960 | 198 (118) | 0 | $-31677.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 09:27 | +10 stop | XRP | UP | 0.51 | 0.63 | 0.85 |
| 11-24 09:26 | +10 stop | BTC | DOWN | 0.45 | 0.61 | 1.25 |
| 11-24 09:26 | +10 | BTC | DOWN | 0.45 | 0.61 | 1.25 |
| 11-24 09:26 | +5 | BTC | DOWN | 0.45 | 0.61 | 1.25 |
| 11-24 09:26 | +10 stop | ETH | UP | 0.69 | 0.85 | 1.36 |
| 11-24 09:26 | +20 | ETH | UP | 0.69 | open |  |
| 11-24 09:26 | +15 | ETH | UP | 0.71 | open |  |
| 11-24 09:26 | +10 | ETH | UP | 0.71 | 0.85 | 1.16 |
| 11-24 09:26 | +5 | ETH | UP | 0.71 | 0.85 | 1.16 |
| 11-24 09:26 | +10 stop | BNB | DOWN | 0.63 | 0.39 | -2.74 |
| 11-24 09:26 | +10 stop | DOGE | UP | 0.69 | 0.82 | 1.04 |
| 11-24 09:26 | +10 stop | XRP | DOWN | 0.56 | 0.37 | -2.25 |
| 11-24 09:26 | +5 | XRP | DOWN | 0.56 | open |  |
| 11-24 09:25 | +10 stop | BTC | UP | 0.53 | 0.68 | 1.16 |
| 11-24 09:25 | +10 stop | NEAR | UP | 0.59 | 0.20 | -4.19 |
| 11-24 09:25 | +10 stop | BNB | UP | 0.63 | 0.35 | -3.17 |
| 11-24 09:25 | +5 | HYPE | DOWN | 0.67 | 0.81 | 1.14 |
| 11-24 09:24 | +5 | XRP | UP | 0.71 | 0.76 | 0.22 |
| 11-24 09:24 | +15 | NEAR | DOWN | 0.64 | open |  |
| 11-24 09:24 | +10 | NEAR | DOWN | 0.64 | 0.79 | 1.17 |
| 11-24 09:24 | +10 stop | NEAR | DOWN | 0.63 | 0.37 | -2.94 |
| 11-24 09:24 | +5 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 11-24 09:23 | +10 stop | DOGE | UP | 0.54 | 0.67 | 1.00 |
| 11-24 09:23 | +10 stop | ETH | UP | 0.60 | 0.73 | 0.99 |
| 11-24 09:23 | +10 | ETH | UP | 0.60 | 0.73 | 0.99 |
| 11-24 09:23 | +5 | ETH | UP | 0.59 | 0.73 | 1.09 |
| 11-24 09:23 | +10 stop | BNB | DOWN | 0.66 | 0.31 | -3.78 |
| 11-24 09:23 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-24 09:23 | +20 | HYPE | DOWN | 0.69 | 0.89 | 1.78 |
| 11-24 09:23 | +15 | HYPE | DOWN | 0.69 | 0.89 | 1.78 |
| 11-24 09:23 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-24 09:23 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-24 09:23 | +10 stop | NEAR | DOWN | 0.46 | 0.57 | 0.74 |
| 11-24 09:23 | +15 | NEAR | DOWN | 0.48 | 0.67 | 1.56 |
| 11-24 09:23 | +10 | NEAR | DOWN | 0.49 | 0.67 | 1.46 |
| 11-24 09:23 | +5 | NEAR | DOWN | 0.49 | 0.57 | 0.44 |
| 11-24 09:23 | +10 stop | BTC | DOWN | 0.56 | 0.37 | -2.25 |
| 11-24 09:23 | +10 | BTC | DOWN | 0.56 | 0.71 | 1.17 |
| 11-24 09:23 | +5 | BTC | DOWN | 0.56 | 0.71 | 1.17 |
| 11-24 09:22 | +10 stop | ETH | UP | 0.50 | 0.65 | 1.16 |
