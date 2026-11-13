# Range-Scalp Bot

*Updated Fri Nov 13 00:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57552 | 50188 | 7364 (101) | 2 | $-15720.13 | -4.3% |
| **+10¢** | 43011 | 34413 | 8598 (133) | 7 | $-14661.57 | -5.4% |
| **+15¢** | 36055 | 26801 | 9254 (167) | 7 | $-13228.26 | -5.8% |
| **+20¢** | 32121 | 22412 | 9709 (217) | 8 | $-11587.10 | -5.8% |
| **+10¢ (15¢ stop)** | 70177 | 70049 | 128 (78) | 0 | $-25852.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 00:39 | +10 stop | ZEC | DOWN | 0.61 | 0.18 | -4.58 |
| 11-13 00:39 | +20 | ZEC | DOWN | 0.60 | 0.84 | 2.12 |
| 11-13 00:39 | +15 | ZEC | DOWN | 0.60 | 0.84 | 2.12 |
| 11-13 00:39 | +10 | ZEC | DOWN | 0.60 | 0.71 | 0.77 |
| 11-13 00:39 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.41 |
| 11-13 00:37 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
| 11-13 00:37 | +10 stop | NEAR | UP | 0.66 | 0.29 | -4.01 |
| 11-13 00:37 | +20 | NEAR | UP | 0.66 | open |  |
| 11-13 00:37 | +10 | NEAR | UP | 0.66 | open |  |
| 11-13 00:37 | +10 stop | HYPE | DOWN | 0.46 | 0.65 | 1.56 |
| 11-13 00:37 | +15 | HYPE | DOWN | 0.46 | 0.65 | 1.56 |
| 11-13 00:37 | +10 | HYPE | DOWN | 0.46 | 0.65 | 1.56 |
| 11-13 00:37 | +5 | HYPE | DOWN | 0.46 | 0.55 | 0.54 |
| 11-13 00:35 | +5 | ETH | UP | 0.43 | 0.59 | 1.25 |
| 11-13 00:35 | +10 stop | ETH | UP | 0.52 | 0.33 | -2.24 |
| 11-13 00:35 | +5 | DOGE | DOWN | 0.71 | 0.79 | 0.53 |
| 11-13 00:34 | +15 | NEAR | UP | 0.69 | open |  |
| 11-13 00:34 | +5 | NEAR | UP | 0.69 | open |  |
| 11-13 00:34 | +10 stop | ETH | DOWN | 0.41 | 0.54 | 0.95 |
| 11-13 00:34 | +10 stop | SOL | DOWN | 0.66 | 0.82 | 1.33 |
| 11-13 00:33 | +10 stop | XRP | DOWN | 0.69 | 0.85 | 1.36 |
| 11-13 00:33 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 11-13 00:33 | +10 stop | BTC | DOWN | 0.63 | 0.87 | 2.15 |
| 11-13 00:33 | +5 | BTC | DOWN | 0.62 | 0.87 | 2.25 |
| 11-13 00:33 | +10 stop | NEAR | UP | 0.62 | 0.29 | -3.62 |
| 11-13 00:33 | +10 | NEAR | UP | 0.57 | 0.70 | 0.97 |
| 11-13 00:33 | +5 | NEAR | UP | 0.57 | 0.64 | 0.35 |
| 11-13 00:33 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 11-13 00:33 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-13 00:33 | +10 stop | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-13 00:33 | +10 stop | BNB | DOWN | 0.67 | 0.52 | -1.84 |
| 11-13 00:33 | +10 stop | ETH | UP | 0.42 | 0.59 | 1.35 |
| 11-13 00:32 | +10 stop | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 11-13 00:32 | +5 | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 11-13 00:32 | +5 | DOGE | DOWN | 0.55 | 0.61 | 0.25 |
| 11-13 00:32 | +10 stop | SOL | DOWN | 0.50 | 0.66 | 1.26 |
| 11-13 00:32 | +5 | SOL | DOWN | 0.50 | 0.55 | 0.14 |
| 11-13 00:32 | +10 stop | BTC | UP | 0.54 | 0.39 | -1.85 |
| 11-13 00:32 | +5 | BTC | UP | 0.54 | 0.59 | 0.15 |
| 11-13 00:32 | +10 stop | HYPE | UP | 0.62 | 0.77 | 1.17 |
